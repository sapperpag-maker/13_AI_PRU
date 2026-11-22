"""tie_out.py - recompute every figure listed in figures.csv from its source.

Usage:  python3.14 -I -B tie_out.py <figures.csv> [--out <result.csv>]

Serves the skill pru-figures-tie-out. Standard library plus openpyxl only.
The program guesses nothing: every reading is stated in figures.csv or refused.
Never prints or writes a GL line: only sums and counts.

Kinds: cell and gl only. Any other kind is ERROR "kind not supported (cell
and gl only)"; a blank source (or a blank or none kind) is NO SOURCE.

figures.csv columns: id, label, shown, unit, period, kind, source, detail,
scale, md5, size.  scale is one of as-is, fraction-to-pct (x100), points; a gl
row must be as-is. md5 and size are required on every row that has a source.

A figure is TIED only when
  - the recomputed value, rounded half up (Decimal ROUND_HALF_UP) to exactly
    the decimals and scale suffix (k, M) of shown, equals shown, and
  - the sign of shown equals the sign of the unrounded value, where an exact
    0 counts as either sign ("-0" never ties +0.30; "0" never ties -0.30).
A float read from a workbook is first cut to 15 significant digits, as Excel
does, so 14.499999999999998 is 14.5 and shows as 15.

Exit codes: 0 = RESULT: PASS, 1 = RESULT: FAIL, 2 = bad input or a crash.
"""

import csv
import hashlib
import os
import re
import sys
from datetime import date, datetime, time, timedelta
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

csv.field_size_limit(2**31 - 1)  # a very long field must not crash the run

REQUIRED_COLS = ["id", "label", "shown", "unit", "period", "kind", "source", "detail", "scale"]
OPTIONAL_COLS = ["md5", "size"]
GL_HEADER = "Account ,Journal ,Date,Doc #,Description,Debit Amount,Credit Amount,Balance,Store"
GL_WIDTH = 9
I_ACC, I_JNL, I_DT, I_DR, I_CR, I_ST = 0, 1, 2, 5, 6, 8
GL_KEYS = ("accounts", "store", "from", "to", "side", "journal")
KINDS = ("cell", "gl")
OUT_COLS = ["id", "label", "shown", "recomputed", "difference", "status", "note"]
GL_OUT_COLS = ["id", "account", "sum", "lines matched"]
SCALES = ("as-is", "fraction-to-pct", "points")
ROUNDING = ROUND_HALF_UP          # Sergio, Q55: "Half up: 1,235"
HUNDRED = Decimal(100)
FORMAT_ERR = "scale disagrees with the cell's format"

TIED, OFF, NOSRC, ERR = "TIED", "OFF", "NO SOURCE", "ERROR"


class BadInput(Exception):
    pass


class RowError(Exception):
    pass


def scale_of(row):
    return row["scale"].strip().lower()


# ---------------------------------------------------------------- numbers

# integer part: proper thousands groups, first group 1-3 digits with no
# leading zero; or plain digits with no leading zero; or a lone 0
_INT = r"(?P<int>[1-9][0-9]{0,2}(?:,[0-9]{3})+|[1-9][0-9]*|0)"
_NUM = _INT + r"(?P<dec>\.[0-9]+)?(?P<suf>[kM%])?"
_PLAIN_RE = re.compile(r"(?P<sign>[-−])?\$?" + _NUM)
_PAREN_RE = re.compile(r"\(\$?" + _NUM + r"\)")
_AMT = _INT + r"(?P<dec>\.[0-9]+)?"
_AMT_PLAIN_RE = re.compile(r"(?P<sign>-)?\$?" + _AMT)
_AMT_PAREN_RE = re.compile(r"\(\$?" + _AMT + r"\)")


def parse_shown(text):
    """Shown figure -> {signed, neg, decimals, mult, pct}. Raises ValueError.

    Grammar: optional '-' or U+2212, OR whole parentheses (never both);
    optional '$' after the sign or just inside the parentheses; ASCII digits
    with proper thousands commas and no leading zero; optional .digits;
    optional k, M or %. Plain ASCII spaces only around the whole value.
    """
    s = (text or "").strip(" ")
    m = _PAREN_RE.fullmatch(s)
    if m:
        neg = True
    else:
        m = _PLAIN_RE.fullmatch(s)
        if not m:
            raise ValueError("shown not readable")
        neg = m.group("sign") is not None
    suf = m.group("suf")
    mult = {"k": Decimal(1000), "M": Decimal(1000000)}.get(suf, Decimal(1))
    dec = m.group("dec") or ""
    num = Decimal(m.group("int").replace(",", "") + dec)
    signed = -num if neg else num
    return {"signed": signed, "neg": neg, "decimals": max(len(dec) - 1, 0),
            "mult": mult, "pct": suf == "%"}


def shown_value(sh):
    return sh["signed"] * sh["mult"]


def round_to_shown(value, sh):
    """The recomputed value at the precision of shown, half up."""
    quantum = Decimal(1).scaleb(-sh["decimals"])
    return (value / sh["mult"]).quantize(quantum, rounding=ROUNDING)


def sign_agrees(value, sh):
    """The sign of shown equals the sign of the unrounded value; exact 0 is either."""
    if value > 0 and sh["neg"]:
        return False
    if value < 0 and not sh["neg"]:
        return False
    return True


def is_tied(value, sh):
    return round_to_shown(value, sh) == sh["signed"] and sign_agrees(value, sh)


def parse_amount(text):
    """GL Debit or Credit to Decimal by one strict grammar. Raises ValueError.

    Blank or spaces only = 0. Otherwise: optional '-', OR whole parentheses
    (never both); optional '$' after the sign or just inside the parentheses;
    ASCII digits with proper thousands commas; optional .digits.
    """
    s = (text or "").strip(" ")
    if s == "":
        return Decimal(0)
    m = _AMT_PAREN_RE.fullmatch(s)
    neg = True
    if not m:
        m = _AMT_PLAIN_RE.fullmatch(s)
        if not m:
            raise ValueError("bad amount")
        neg = m.group("sign") is not None
    d = Decimal(m.group("int").replace(",", "") + (m.group("dec") or ""))
    return -d if neg else d


def to_decimal(value):
    if isinstance(value, int):
        return Decimal(value)
    return Decimal(format(value, ".15g"))  # Excel's 15 significant digits


def fmt(v):
    if v is None:
        return ""
    try:
        return f"{v:,.2f}"
    except (InvalidOperation, ValueError):
        return str(v)


# ---------------------------------------------------------------- files

_md5_cache = {}


def file_md5(path):
    if path not in _md5_cache:
        h = hashlib.md5()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(1 << 20), b""):
                h.update(chunk)
        _md5_cache[path] = h.hexdigest()
    return _md5_cache[path]


def check_source(row):
    """md5 and size required; existence, size and md5 checked. Raises RowError."""
    path = row["source"]
    want_size = (row.get("size") or "").strip().replace(",", "")
    want_md5 = (row.get("md5") or "").strip().lower()
    if not want_size or not want_md5:
        raise RowError("md5/size not given")
    if not os.path.isfile(path):
        raise RowError("source file not found")
    if not re.fullmatch(r"[0-9]+", want_size):
        raise RowError("size column not a whole number")
    if not re.fullmatch(r"[0-9a-f]{8}|[0-9a-f]{32}", want_md5):
        raise RowError("md5 column must be 8 or 32 hex characters")
    if os.path.getsize(path) != int(want_size):
        raise RowError("source changed (size)")
    if not file_md5(path).startswith(want_md5):
        raise RowError("source changed (md5)")


# ---------------------------------------------------------------- cell

_books = {}


def get_book(path):
    if path not in _books:
        from openpyxl import load_workbook
        _books[path] = load_workbook(path, read_only=True, data_only=True)
    return _books[path]


def split_ref(detail):
    d = (detail or "").strip()
    if "!" not in d:
        raise RowError("cell detail must be Sheet!A1")
    sheet, cell = d.rsplit("!", 1)
    sheet = sheet.strip()
    if len(sheet) >= 2 and sheet[0] == "'" and sheet[-1] == "'":
        sheet = sheet[1:-1].replace("''", "'")
    cell = cell.strip().replace("$", "").upper()
    m = re.fullmatch(r"([A-Z]{1,3})([1-9][0-9]*)", cell)
    if not sheet or not m:
        raise RowError("cell detail must be Sheet!A1")
    return sheet, m.group(1), int(m.group(2))


def col_index(letters):
    n = 0
    for ch in letters:
        n = n * 26 + (ord(ch) - 64)
    return n


def format_scan(number_format):
    """Split a number format on ';' outside quotes, brackets and escapes.
    Returns (sections, brackets): quoted, bracketed and escaped text is left
    out of the sections; the text inside each [...] is listed in brackets."""
    f = number_format or ""
    sections, cur, brackets, br = [], "", [], ""
    i, in_quote, in_bracket = 0, False, False
    while i < len(f):
        c = f[i]
        if in_quote:
            if c == '"':
                in_quote = False
        elif in_bracket:
            if c == "]":
                in_bracket = False
                brackets.append(br)
            else:
                br += c
        elif c == '"':
            in_quote = True
        elif c == "[":
            in_bracket, br = True, ""
        elif c in "\\_*":
            i += 2  # escaped, spacing or fill character: the next one is literal
            continue
        elif c == ";":
            sections.append(cur)
            cur = ""
        else:
            cur += c
        i += 1
    sections.append(cur)
    return sections, brackets


def format_sections(number_format):
    return format_scan(number_format)[0]


def check_format(number_format):
    """Refuse a number format whose meaning this program does not read. Raises RowError."""
    sections, brackets = format_scan(number_format)
    if any(b.strip()[:1] in ("<", ">", "=") for b in brackets):
        raise RowError("conditional number format not supported")
    if len(sections) > 4:
        raise RowError("conditional number format not supported")
    for k, s in enumerate(sections):
        if "@" in s and k != 3:
            raise RowError("format has a text section outside the fourth")
        if s.count("%") > 1:
            raise RowError("format has more than one %")
        if re.search(r"[0#?],+(?![0#?,])", s):
            raise RowError("format scales by thousands")


def format_section_for(number_format, value):
    """Exact 0: the third section when there is one. Negative: the second
    section when there is one. Otherwise, and for a positive value, the first."""
    secs = format_sections(number_format)
    if value == 0 and len(secs) > 2:
        return secs[2]
    if value < 0 and len(secs) > 1:
        return secs[1]
    return secs[0]


def format_has_pct(section):
    return "%" in section


def recompute_cell(row):
    sheet, col, rownum = split_ref(row["detail"])
    ci = col_index(col)
    if sheet.strip().lower() == "master":
        if ci > 5:
            raise RowError("Master past column E")
        if ci < 2:
            raise RowError("Master column A refused (only B to E)")
    check_source(row)
    try:
        wb = get_book(row["source"])
    except Exception as e:
        raise RowError(f"workbook could not be opened ({type(e).__name__})")
    if sheet not in wb.sheetnames:
        raise RowError("sheet not found")
    cell = None
    for r in wb[sheet].iter_rows(min_row=rownum, max_row=rownum, min_col=ci, max_col=ci):
        cell = r[0] if r else None
    value = getattr(cell, "value", None)
    if value is None:
        raise RowError("no cached value (empty cell or formula never calculated)")
    if isinstance(value, bool):
        raise RowError("cell holds a boolean")
    if isinstance(value, (datetime, date, time, timedelta)):
        raise RowError("cell holds a date")
    if isinstance(value, str):
        raise RowError("cell holds text, not a number")
    if not isinstance(value, (int, float)):
        raise RowError(f"cell holds {type(value).__name__}, not a number")
    try:
        v = to_decimal(value)
    except (InvalidOperation, ValueError):
        raise RowError("cell value not a finite number")
    if not v.is_finite():
        raise RowError("cell value not a finite number")
    check_format(getattr(cell, "number_format", None))
    section = format_section_for(getattr(cell, "number_format", None), v)
    pct_format = format_has_pct(section)
    scale = scale_of(row)
    if scale == "fraction-to-pct" and not pct_format:
        raise RowError(FORMAT_ERR + " (fraction-to-pct needs a % format)")
    if scale == "points" and pct_format:
        raise RowError(FORMAT_ERR + " (points needs a format without %)")
    if scale == "as-is" and pct_format:
        raise RowError(FORMAT_ERR + " (as-is with a % format)")
    if scale == "fraction-to-pct":
        return v * HUNDRED
    return v


# ---------------------------------------------------------------- gl

def parse_date(text):
    """Only M/D/YYYY (4-digit year) or ISO YYYY-MM-DD; anything else is unreadable."""
    s = (text or "").strip()
    m = re.fullmatch(r"([0-9]{4})-([0-9]{2})-([0-9]{2})", s)
    if m:
        y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
    else:
        m = re.fullmatch(r"([0-9]{1,2})/([0-9]{1,2})/([0-9]{4})", s)
        if not m:
            raise ValueError("bad date")
        mo, d, y = int(m.group(1)), int(m.group(2)), int(m.group(3))
    return date(y, mo, d)


def account_matches(pattern, account):
    """Exact, or x/X standing for one ASCII digit 0-9, same length only."""
    if len(pattern) != len(account):
        return False
    for p, a in zip(pattern, account):
        if p in "xX":
            if a not in "0123456789":
                return False
        elif p != a:
            return False
    return True


def parse_gl_detail(detail):
    spec = {}
    for part in (detail or "").split(";"):
        if not part.strip():
            continue
        if "=" not in part:
            raise RowError("gl detail must be key=value pairs separated by ;")
        k, v = part.split("=", 1)
        k = k.strip().lower()
        if k in spec:
            raise RowError("repeated key in gl detail: " + k)
        spec[k] = v.strip()
    unknown = set(spec) - set(GL_KEYS)
    if unknown:
        raise RowError("gl detail has unknown key " + ", ".join(sorted(unknown)))
    missing = [k for k in ("accounts", "store", "from", "to", "side") if not spec.get(k)]
    if missing:
        raise RowError("gl detail missing " + ", ".join(missing))
    accounts = [a.strip() for a in spec["accounts"].split(",") if a.strip()]
    if not accounts:
        raise RowError("gl detail has no accounts")
    try:
        d_from = parse_date(spec["from"])
        d_to = parse_date(spec["to"])
    except ValueError:
        raise RowError("gl from/to must be YYYY-MM-DD or M/D/YYYY")
    if d_from > d_to:
        raise RowError("gl from is after to")
    side = spec["side"].lower()
    if side not in ("credit-debit", "debit-credit"):
        raise RowError("gl side must be credit-debit or debit-credit")
    journals = None
    if "journal" in spec:
        journals = {j.strip() for j in spec["journal"].split(",") if j.strip()}
        if not journals:
            raise RowError("gl journal is blank")
    return {
        "accounts": accounts, "store": spec["store"].strip(),
        "from": d_from, "to": d_to, "side": side, "journals": journals,
        "sum": Decimal(0), "lines": 0, "per_account": {}, "bad_amount": 0,
        "bad_date": 0,
    }


def read_gl(path, specs):
    """One streaming pass over the GL for every gl row on this path.

    The header line must be exactly GL_HEADER after only a BOM is stripped.
    Physical data lines are counted on the raw bytes (split on \\n, header and
    blank lines left out) while the csv module reads the records. Raises
    RowError, for every row on the path, on a header not as expected, records
    and lines that differ, or a record whose field count is not 9.
    """
    counts = {"physical": 0, "first": True, "header": None}

    def raw_lines():
        with open(path, "rb") as f:
            for raw in f:
                if counts["first"]:
                    counts["first"] = False
                    if raw.startswith(b"\xef\xbb\xbf"):
                        raw = raw[3:]
                    counts["header"] = raw
                elif raw.strip():
                    counts["physical"] += 1
                yield raw.decode("utf-8", errors="replace")

    lines = raw_lines()
    first = next(lines, None)
    if first is None:
        raise RowError("GL file is empty")
    if counts["header"].rstrip(b"\r\n") != GL_HEADER.encode("ascii"):
        raise RowError("GL header not as expected")
    reader = csv.reader(lines)
    speclist = list(specs.values())
    records = 0
    malformed = 0
    for fields in reader:
        if not fields or (len(fields) == 1 and not fields[0].strip()):
            continue  # a blank line
        records += 1
        if len(fields) != GL_WIDTH:
            malformed += 1
            continue
        account = fields[I_ACC].strip()
        store = fields[I_ST].strip()
        journal = fields[I_JNL].strip()
        parsed = None  # (date or None, debit or None, credit or None), read once per line
        for sp in speclist:
            if store != sp["store"]:
                continue
            if not any(account_matches(p, account) for p in sp["accounts"]):
                continue
            if parsed is None:
                try:
                    d = parse_date(fields[I_DT])
                except ValueError:
                    d = None
                try:
                    dr, cr = parse_amount(fields[I_DR]), parse_amount(fields[I_CR])
                except ValueError:
                    dr = cr = None
                parsed = (d, dr, cr)
            d, dr, cr = parsed
            if d is None:
                sp["bad_date"] += 1
            if dr is None:
                sp["bad_amount"] += 1
            if d is None or dr is None:
                continue
            if sp["journals"] is not None and journal not in sp["journals"]:
                continue
            if not (sp["from"] <= d <= sp["to"]):
                continue
            if sp["side"] == "credit-debit":
                amt = cr - dr
            else:
                amt = dr - cr
            sp["sum"] += amt
            sp["lines"] += 1
            pa = sp["per_account"].setdefault(account, [Decimal(0), 0])
            pa[0] += amt
            pa[1] += 1
    problems = []
    if records != counts["physical"]:
        problems.append(f"GL records {records} ≠ lines {counts['physical']}")
    if malformed:
        problems.append(f"{malformed} malformed GL lines")
    if problems:
        raise RowError("; ".join(problems))


# ---------------------------------------------------------------- main

def load_figures(path):
    if not os.path.isfile(path):
        raise BadInput(f"figures file not found: {path}")
    try:
        with open(path, "r", encoding="utf-8-sig", newline="") as f:
            reader = csv.reader(f)
            header = next(reader, None)
            if header is None:
                raise BadInput("figures file is empty")
            names = [h.strip().lower() for h in header]
            if len(set(names)) != len(names):
                raise BadInput("figures header has a duplicate column name")
            missing = [c for c in REQUIRED_COLS if c not in names]
            if missing:
                raise BadInput("figures header lacks: " + ", ".join(missing))
            rows = []
            for n, fields in enumerate(reader, 2):
                if not any(x.strip() for x in fields):
                    continue
                if len(fields) > len(header):
                    raise BadInput(f"figures row {n} has more fields than the header")
                row = {}
                for c in REQUIRED_COLS + OPTIONAL_COLS:
                    raw = fields[names.index(c)] if c in names and names.index(c) < len(fields) else ""
                    row[c] = raw if c == "shown" else raw.strip()  # shown: parse_shown strips ASCII spaces only
                rows.append(row)
    except UnicodeDecodeError:
        raise BadInput("figures file is not UTF-8")
    except csv.Error:
        raise BadInput("figures file is not a readable CSV")
    if not rows:
        raise BadInput("figures file has no rows")
    seen = set()
    for r in rows:
        if not r["id"]:
            raise BadInput("a figures row has no id")
        if r["id"] in seen:
            raise BadInput("duplicate id " + r["id"])
        seen.add(r["id"])
    return rows


def run(rows):
    results = {r["id"]: {"value": None, "status": None, "note": ""} for r in rows}
    gl_tables = {}

    def fail(rid, status, note):
        results[rid]["status"], results[rid]["note"] = status, note

    # pass 0: shown, kind, source and scale, stated or refused
    shown = {}
    for r in rows:
        rid, kind, scale = r["id"], r["kind"].strip().lower(), scale_of(r)
        try:
            shown[rid] = parse_shown(r["shown"])
        except ValueError:
            fail(rid, ERR, "shown not readable")
            continue
        if kind not in KINDS + ("", "none"):
            fail(rid, ERR, "kind not supported (cell and gl only)")
            continue
        if kind in ("", "none") or not r["source"]:
            fail(rid, NOSRC, "no source named")
            continue
        if not scale:
            fail(rid, ERR, "scale not given")
        elif scale not in SCALES:
            fail(rid, ERR, "unknown scale " + scale)
        elif kind == "gl" and scale != "as-is":
            fail(rid, ERR, "a gl row's scale must be as-is")
        elif kind == "gl" and shown[rid]["pct"]:
            fail(rid, ERR, "a gl row's shown cannot hold %")
        elif shown[rid]["pct"] and scale == "as-is":
            fail(rid, ERR, "scale/% mismatch")

    # pass 1: cell; collect gl specs by path
    gl_by_path = {}
    for r in rows:
        rid, kind = r["id"], r["kind"].strip().lower()
        if results[rid]["status"] is not None:
            continue
        if kind == "cell":
            try:
                results[rid]["value"] = recompute_cell(r)
            except RowError as e:
                fail(rid, ERR, str(e))
            except Exception as e:
                fail(rid, ERR, f"cell could not be read ({type(e).__name__})")
        else:
            try:
                spec = parse_gl_detail(r["detail"])
                check_source(r)
            except RowError as e:
                fail(rid, ERR, str(e))
                continue
            gl_by_path.setdefault(os.path.normcase(os.path.realpath(r["source"])), {})[rid] = spec

    # pass 2: each GL once
    for path, specs in gl_by_path.items():
        try:
            read_gl(path, specs)
        except RowError as e:
            for rid in specs:
                fail(rid, ERR, str(e))
            continue
        except (OSError, csv.Error) as e:
            for rid in specs:
                fail(rid, ERR, f"GL could not be read ({type(e).__name__})")
            continue
        for rid, sp in specs.items():
            table = [(acc, v[0], v[1]) for acc, v in sorted(sp["per_account"].items())]
            dead = []
            for p in sp["accounts"]:
                if not any(account_matches(p, acc) for acc, _, _ in table):
                    dead.append(p)
            for p in dead:
                table.append((p, Decimal(0), 0))
            gl_tables[rid] = table
            if sp["bad_amount"] or sp["bad_date"]:
                fail(rid, ERR, f"{sp['bad_amount']} matched lines with unreadable amount, "
                               f"{sp['bad_date']} with unreadable date")
                continue
            if sp["lines"] == 0:
                fail(rid, ERR, "no GL lines matched")
                continue
            if dead:
                fail(rid, ERR, "; ".join(f"account {p} matched no line" for p in dead))
                continue
            results[rid]["value"] = sp["sum"]
            results[rid]["note"] = f"{sp['lines']} GL lines matched"

    # pass 3: compare by rounding to the precision of shown, sign included
    out = []
    for r in rows:
        res = results[r["id"]]
        diff = None
        if res["status"] is None:
            sh = shown[r["id"]]
            try:
                rounded = round_to_shown(res["value"], sh)
                diff = res["value"] - shown_value(sh)
                res["status"] = TIED if is_tied(res["value"], sh) else OFF
            except InvalidOperation:
                res["status"], res["note"] = ERR, "value too large to round"
            else:
                suffix = {Decimal(1000): "k", Decimal(1000000): "M"}.get(sh["mult"], "")
                note = f"rounds to {rounded}{suffix}"
                if not sign_agrees(res["value"], sh):
                    note += "; sign differs from shown"
                res["note"] = "; ".join(x for x in (res["note"], note) if x)
        out.append({
            "id": r["id"], "label": r["label"], "shown": r["shown"],
            "recomputed": fmt(res["value"]), "difference": fmt(diff),
            "status": res["status"], "note": res["note"],
        })
    gl_out = []
    for r in rows:
        for acc, s, n in gl_tables.get(r["id"], []):
            gl_out.append({"id": r["id"], "account": acc, "sum": fmt(s), "lines matched": str(n)})
    return out, gl_out


def print_table(title, cols, rows):
    widths = {c: max([len(c)] + [len(str(r[c])) for r in rows]) for c in cols}
    print(title)
    print(" | ".join(c.ljust(widths[c]) for c in cols))
    print("-+-".join("-" * widths[c] for c in cols))
    for r in rows:
        print(" | ".join(str(r[c]).ljust(widths[c]) for c in cols))
    print()


def same_path(a, b):
    return os.path.normcase(os.path.realpath(a)) == os.path.normcase(os.path.realpath(b))


def main(argv):
    args = list(argv)
    out_path = None
    if "--out" in args:
        i = args.index("--out")
        if i + 1 >= len(args):
            print("bad input: --out needs a path", file=sys.stderr)
            return 2
        out_path = args[i + 1]
        del args[i:i + 2]
    if len(args) != 1:
        print("usage: tie_out.py <figures.csv> [--out <result.csv>]", file=sys.stderr)
        return 2
    try:
        rows = load_figures(args[0])
    except BadInput as e:
        print("bad input: " + str(e), file=sys.stderr)
        return 2
    if out_path:
        protected = [args[0]] + [r["source"] for r in rows if r["source"]]
        if any(same_path(out_path, p) for p in protected):
            print("bad input: --out must not be the figures file or a source file", file=sys.stderr)
            return 2

    out, gl_out = run(rows)
    print_table("FIGURES", OUT_COLS, out)
    if gl_out:
        print_table("GL accounts", GL_OUT_COLS, gl_out)
    bad = [r for r in out if r["status"] != TIED]
    result = "RESULT: PASS" if not bad else f"RESULT: FAIL ({len(bad)} of {len(out)} rows not TIED)"

    if out_path:
        with open(out_path, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            w.writerow(OUT_COLS)
            for r in out:
                w.writerow([r[c] for c in OUT_COLS])
            if gl_out:
                w.writerow([])
                w.writerow(["GL accounts"])
                w.writerow(GL_OUT_COLS)
                for r in gl_out:
                    w.writerow([r[c] for c in GL_OUT_COLS])
            w.writerow([])
            w.writerow([result])
    print(result)
    return 0 if not bad else 1


if __name__ == "__main__":
    sys.dont_write_bytecode = True
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        code = main(sys.argv[1:])
    except Exception as e:  # any crash: exit 2 with a message, no data echoed
        sys.stdout.flush()
        print(f"bad input: tie_out stopped on an unexpected {type(e).__name__}; no result", file=sys.stderr)
        code = 2
    sys.exit(code)
