"""test_tie_out.py - tests for tie_out.py on made-up files only.

Usage:  python3.14 -I -B test_tie_out.py --bench <folder>

--bench is required: the test builds every file itself in a new folder under
<folder>\\test-runs (never real data, never the system temp folder), writes
no __pycache__ and deletes nothing.
Last line: TESTS: PASS (n) or TESTS: FAIL (names).
"""

import sys

sys.dont_write_bytecode = True  # before any import of tie_out

import csv
import hashlib
import importlib.util
import os
import subprocess
import tempfile
import zipfile
from datetime import datetime
from decimal import Decimal

HERE = os.path.dirname(os.path.abspath(__file__))
TIE_OUT = os.path.join(HERE, "tie_out.py")
PYCACHE = os.path.join(HERE, "__pycache__")
USAGE = "usage: test_tie_out.py --bench <folder>"

GL_HEADER = ["Account ", "Journal ", "Date", "Doc #", "Description",
             "Debit Amount", "Credit Amount", "Balance", "Store"]
SECRET_DESC = "ZEBRA-QUOKKA-7731 private customer note"
SECRET_DOC = "DOCSECRET998"
FIG_HEADER = ["id", "label", "shown", "unit", "period", "kind", "source", "detail", "scale", "md5", "size"]
FLOAT_A = "14.499999999999998"     # what Excel caches for =0.145*100; shows 15
FLOAT_B = "1234.4999999999998"     # shows 1,235

results = []


def check(name, cond):
    results.append((name, bool(cond)))
    print(("ok   " if cond else "FAIL ") + name)


def pycache_state():
    if not os.path.isdir(PYCACHE):
        return None
    return sorted((n, os.path.getmtime(os.path.join(PYCACHE, n))) for n in os.listdir(PYCACHE))


def load_module():
    spec = importlib.util.spec_from_file_location("tie_out_mod", TIE_OUT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def gl_rows(flip=False):
    # (account, journal, date, debit, credit, store)
    rows = [
        ("46100-30", "SJ", "1/1/2026", "", "1,000.00", "POW"),      # in: +1000 (first day)
        ("46200-30", "SJ", "2/3/2026", "", "$2,500.00", "POW"),     # in: +2500
        ("46100-30", "GJ", "3/1/2026", "100.00", "", "POW"),        # in: -100
        ("46100-30", "GJ", "12/31/2025", "", "5000", "POW"),        # out: date
        ("46100-30", "SJ", "4/1/2026", "", "7000", "LDS"),          # out: store
        ("47100-30", "SJ", "4/1/2026", "", "9000", "POW"),          # out: account
        ("46100-31", "SJ", "4/1/2026", "", "800", "POW"),           # out: suffix
        ("46A00-30", "SJ", "4/1/2026", "", "7777", "POW"),          # out: x is a digit, A is not
        ("46100-301", "SJ", "4/1/2026", "", "4444", "POW"),         # out: longer account
        ("46100-30", "SJ", "4/1/2026", "", "5555", "POWX"),         # out: store is not a prefix match
        ("46100-30", "SJ", "4/1/2026", "", "6666", "pow"),          # out: store matches exactly
        ("46100-30", "GJ", "9/30/2026", "", "(50.00)", "POW"),      # in: -50 (parens, last day)
        ("46100-30", "GJ", "10/1/2026", "", "333", "POW"),          # out: date
    ]
    if flip:  # planted: line 1 booked as a debit instead of a credit
        a, j, d, _, cr, s = rows[0]
        rows[0] = (a, j, d, cr, "", s)
    return rows


def write_gl(path, flip=False, extra=None, raw_extra=None, desc=SECRET_DESC, header_line=None, bom=False):
    with open(path, "w", encoding="utf-8-sig" if bom else "utf-8", newline="") as f:
        if header_line is not None:
            f.write(header_line + "\r\n")
        w = csv.writer(f)
        if header_line is None:
            w.writerow(GL_HEADER)
        for i, (a, j, d, dr, cr, s) in enumerate(gl_rows(flip) + (extra or [])):
            w.writerow([a, j, d, f"{SECRET_DOC}-{i}", desc, dr, cr, "1,234.00", s])
        if raw_extra:
            f.write(raw_extra)


def write_book(path):
    from openpyxl import Workbook
    wb = Workbook()
    ws = wb.active
    ws.title = "Budget 2027"
    ws["B7"] = 1234.4
    ws["B8"] = 1234.5
    ws["B9"] = -1234.5
    ws["B10"] = 0.3
    ws["B11"] = -0.3
    ws["B12"] = 0
    ws["C2"] = 1234000
    ws["C3"] = 1260000
    ws["C4"] = 1249
    ws["C5"] = 1250
    ws["D1"] = "=B7*2"          # formula, never calculated: no cached value
    ws["E5"] = 0.452
    ws["E5"].number_format = "0.0%"
    ws["E6"] = 45.2
    ws["E6"].number_format = "0.0"
    ws["E7"] = 0.452            # General format
    ws["E8"] = 111111           # placeholder, replaced in the XML by FLOAT_A
    ws["E9"] = 222222           # placeholder, replaced in the XML by FLOAT_B
    ws["E10"] = 0.452
    ws["E10"].number_format = '0.0"%"'   # a quoted %, not a percent format
    ws["E11"] = 12
    ws["E11"].number_format = "0%"
    ws["E12"] = "45"            # text that looks like a number
    ws["E13"] = -0.452
    ws["E13"].number_format = "0.0%;-0.0"      # negative section has no %
    ws["E14"] = -0.452
    ws["E14"].number_format = "0.0%;(0.0%)"    # negative section has %
    ws["E15"] = 0.452
    ws["E15"].number_format = "0.0;0.0%"       # positive section has no %
    ws["E16"] = -0.452
    ws["E16"].number_format = "0.0%"           # one section: negatives read it
    ws["E17"] = -0.452
    ws["E17"].number_format = "0.0;0.0%;0"     # three sections: negatives read the second
    for ref, val, nf in (("E18", 5, "[<1]0.0%;0.0"),           # condition bracket: reads as 5.0
                         ("E19", 0.5, "[>=1]0.0;0.0%"),        # condition bracket: shows 50.0%
                         ("E20", 0, "0.0;-0.0;0.0%"),          # zero section has %
                         ("E21", 0, "0.0%;-0.0%;0.0"),         # zero section has no %
                         ("E22", 0.452, "0%%"),                # two %
                         ("E23", 1234, "#,##0,"),              # scales by thousands
                         ("E24", 0.452, "[$%-409]0.000"),      # % only inside a locale bracket
                         ("E25", 7, "0;0;0;0;0"),              # five sections
                         ("E26", -50, "0%;@"),                 # @ as the second section
                         ("E27", -0.5, "0%;@"),                # @ as the second section
                         ("E28", 50, "0;0;@")):                # @ as the third section
        ws[ref] = val
        ws[ref].number_format = nf
    ws["B13"] = datetime(2026, 1, 5)         # a date (openpyxl gives it a date format)
    ws["B14"] = True                           # a boolean
    ws["B15"] = 1e30                           # too large to round to whole units
    ws["B16"] = 0.5
    m = wb.create_sheet("Master")
    m["A2"] = 5
    m["B2"] = 10
    m["B3"] = 4
    m["F2"] = 99
    raw = path + ".openpyxl.xlsx"
    wb.save(raw)
    # put the two floats into the sheet XML directly, as Excel would cache them
    with zipfile.ZipFile(raw) as zin, zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "xl/worksheets/sheet1.xml":
                text = data.decode("utf-8")
                assert text.count("<v>111111</v>") == 1 and text.count("<v>222222</v>") == 1
                text = text.replace("<v>111111</v>", f"<v>{FLOAT_A}</v>")
                text = text.replace("<v>222222</v>", f"<v>{FLOAT_B}</v>")
                data = text.encode("utf-8")
            zout.writestr(item, data)


def md5_size(path):
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()[:8], str(os.path.getsize(path))


def write_figures(path, rows, header=FIG_HEADER):
    """9-field rows of kind cell/gl get the source's real md5 and size;
    11-field rows keep what they give (blank md5/size included)."""
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        for r in rows:
            r = list(r)
            if len(r) == 9 and r[5] in ("cell", "gl") and r[6] and os.path.isfile(r[6]):
                r += list(md5_size(r[6]))
            w.writerow(r + [""] * (len(header) - len(r)))


def run_tie(fig, out=None):
    cmd = [sys.executable, "-I", "-B", TIE_OUT, fig]
    if out:
        cmd += ["--out", out]
    p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    return p.returncode, p.stdout, p.stderr


def last_line(text):
    lines = text.strip().splitlines()
    return lines[-1] if lines else ""


def read_out(path):
    if not os.path.isfile(path):
        return {}, []
    with open(path, encoding="utf-8", newline="") as f:
        allrows = list(csv.reader(f))
    main, gl, i = {}, [], 1
    while i < len(allrows) and allrows[i]:
        main[allrows[i][0]] = dict(zip(allrows[0], allrows[i]))
        i += 1
    if i + 2 < len(allrows) and allrows[i + 1] == ["GL accounts"]:
        hdr = allrows[i + 2]
        i += 3
        while i < len(allrows) and allrows[i]:
            gl.append(dict(zip(hdr, allrows[i])))
            i += 1
    return main, gl


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if "--bench" not in argv or argv.index("--bench") + 1 >= len(argv):
        print(USAGE, file=sys.stderr)
        return 2
    bench = argv[argv.index("--bench") + 1]
    if not os.path.isdir(bench):
        print(USAGE + " (folder not found)", file=sys.stderr)
        return 2
    cache_before = pycache_state()
    runs = os.path.join(bench, "test-runs")
    os.makedirs(runs, exist_ok=True)
    tmp = tempfile.mkdtemp(prefix="run-", dir=runs)
    print("test folder: " + tmp)

    mod = load_module()
    D = Decimal

    # --- shown grammar
    ps = mod.parse_shown
    sh = ps("1,234")
    check("shown 1,234 -> 1234, 0 decimals", sh["signed"] == D(1234) and sh["decimals"] == 0)
    sh = ps("1.2M")
    check("shown 1.2M -> 1.2 x 1e6, 1 decimal", sh["signed"] == D("1.2") and sh["mult"] == D(1000000) and sh["decimals"] == 1)
    sh = ps("45.2%")
    check("shown 45.2% -> 45.2, % seen", sh["signed"] == D("45.2") and sh["pct"])
    check("shown (1,234) -> -1234", ps("(1,234)")["signed"] == D(-1234))
    check("shown -1,234 -> -1234", ps("-1,234")["signed"] == D(-1234))
    check("shown −1,234 (Unicode minus) -> -1234", ps("−1,234")["signed"] == D(-1234))
    check("shown $1,234 -> 1234", ps("$1,234")["signed"] == D(1234))
    check("shown -$1,234 -> -1234", ps("-$1,234")["signed"] == D(-1234))
    check("shown ($1,234.50) -> -1234.50", ps("($1,234.50)")["signed"] == D("-1234.50"))
    check("shown (1.2M) -> -1.2 x 1e6", ps("(1.2M)")["signed"] == D("-1.2") and ps("(1.2M)")["mult"] == D(1000000))
    check("shown 1.2k -> 1.2 x 1000", ps("1.2k")["mult"] == D(1000))
    check("shown with spaces around it read", ps("  1,234  ")["signed"] == D(1234))
    check("shown -0 is a negative zero", ps("-0")["neg"] and ps("(0)")["neg"] and not ps("0")["neg"])
    check("shown 0.5 and 0 read", ps("0.5")["signed"] == D("0.5") and ps("0")["signed"] == D(0))
    check("shown 0.452 read (lone 0 integer part)", ps("0.452")["signed"] == D("0.452"))
    check("shown 1,234,567 read", ps("1,234,567")["signed"] == D(1234567))
    for bad in ("(-12)", "--12", "-$-12", "1 2", "1$2", "1,00", "12,3456", "١٢", "$-12",
                "-(12)", "abc", "", "12.", ".5", "1,234,56", "12%%", "1.2MM", "(12", "12)", "+12", "1.2K",
                "0,123", "01,234", "01", "00", "1,2,3", " 1,234", "1,234 ", "\t1,234",
                "$$900", "$ 900", "- 900", "( 900)", "-$$900"):
        try:
            ps(bad)
            check(f"shown {bad!r} refused", False)
        except ValueError:
            check(f"shown {bad!r} refused", True)
        except Exception:  # any other error is not the refusal asked for
            check(f"shown {bad!r} refused", False)

    # --- rounding and sign
    rs = mod.round_to_shown
    check("round 1234.50 to 1,234 precision -> 1235 (half up)", rs(D("1234.50"), ps("1,234")) == D(1235))
    check("round -1234.5 -> -1235 (half up, away from zero)", rs(D("-1234.5"), ps("1,234")) == D(-1235))
    check("round 1,250 at 1.2k precision -> 1.3", rs(D(1250), ps("1.2k")) == D("1.3"))
    check("round 1,234,000 at 1.2M precision -> 1.2", rs(D(1234000), ps("1.2M")) == D("1.2"))
    it = mod.is_tied
    check("sign: -0 against +0.30 is not tied", not it(D("0.30"), ps("-0")))
    check("sign: -0 against -0.30 is tied", it(D("-0.30"), ps("-0")))
    check("sign: 0 against -0.30 is not tied", not it(D("-0.30"), ps("0")))
    check("sign: -0.0 and 0 both tie an exact 0", it(D(0), ps("-0.0")) and it(D(0), ps("0")))
    check("excel float: 14.499999999999998 -> 14.5", mod.to_decimal(float(FLOAT_A)) == D("14.5"))
    check("excel float: 1234.4999999999998 -> 1234.5", mod.to_decimal(float(FLOAT_B)) == D("1234.5"))

    # --- amounts, patterns, formats, dates
    check("amount (50.00) -> -50", mod.parse_amount("(50.00)") == -50)
    check("amount blank -> 0", mod.parse_amount("") == 0)
    check("amount $1,000.00 -> 1000", mod.parse_amount("$1,000.00") == 1000)
    check("amount spaces only -> 0", mod.parse_amount("   ") == 0)
    check("amount -5 -> -5, -$5 -> -5, ($5) -> -5", mod.parse_amount("-5") == -5
          and mod.parse_amount("-$5") == -5 and mod.parse_amount("($5)") == -5)
    check("amount 0.50 and 1,234,567.89 read", mod.parse_amount("0.50") == D("0.50")
          and mod.parse_amount("1,234,567.89") == D("1234567.89"))
    check("amount with spaces around it read", mod.parse_amount(" 12.00 ") == 12)
    for bad in ("12x", "1e5", "NaN", "١٢", "$", "-", "()", "1 2", "--5", "(-5)", "-$-5", "1,23",
                "1,2,3", "01,234", "0,123", ".5", "(5", "5)", "$-5", "-(5)", "+5", "5.", "1,2345",
                " 5", "(  )", "$$5", "-$$5", "($$5)", "$ 5"):
        try:
            mod.parse_amount(bad)
            check(f"amount {bad!r} refused", False)
        except ValueError:
            check(f"amount {bad!r} refused", True)
        except Exception:  # any other error is not the refusal asked for
            check(f"amount {bad!r} refused", False)
    am = mod.account_matches
    check("pattern 46xxx-30 matches 46100-30", am("46xxx-30", "46100-30"))
    check("pattern 46xxx-30 refuses 46100-31", not am("46xxx-30", "46100-31"))
    check("pattern 46xxx-30 refuses 46100-301 (longer)", not am("46xxx-30", "46100-301"))
    check("exact 46100-30 refuses 46100-301 (longer)", not am("46100-30", "46100-301"))
    check("pattern x refuses a letter (46A00-30)", not am("46xxx-30", "46A00-30"))
    check("pattern x refuses a space or sign", not am("46xxx-30", "46 00-30") and not am("46xxx-30", "46-00-30"))
    check("pattern x refuses a non-ASCII digit", not am("46xxx-30", "46١٠٠-30"))
    def fp(f):
        return mod.format_has_pct(mod.format_section_for(f, D(1)))
    check("format 0.0% has %", fp("0.0%") and fp("0%"))
    check('format 0.0"%" has no % (quoted)', not fp('0.0"%"'))
    check("format [Red]0.0 / 0\\% / General have no %", not fp("[Red]0.0") and not fp("0\\%") and not fp("General"))
    fs = mod.format_section_for
    check("format section: value >= 0 reads the first", fs("0.0%;-0.0", D("0.5")) == "0.0%"
          and fs("0.0%;-0.0", D(0)) == "0.0%")
    check("format section: value < 0 reads the second", fs("0.0%;-0.0", D("-0.5")) == "-0.0")
    check("format section: value < 0 with one section reads the first", fs("0.0%", D("-0.5")) == "0.0%")
    check('format section: a quoted ";" is not a split', fs('0.0";"%', D("-1")) == "0.0%")
    check("format section: three sections, value < 0 reads the second", fs("0.0;0.0%;0", D("-1")) == "0.0%")
    check("format section: exact 0 reads the third when there is one", fs("0.0;-0.0;0.0%", D(0)) == "0.0%")
    check("format section: exact 0 with four sections reads the third", fs("0.0;-0.0;0.0%;@", D(0)) == "0.0%")
    check("format section: exact 0 with two sections reads the first", fs("0.0%;-0.0", D(0)) == "0.0%"
          and fs("0.0;-0.0%", D(0)) == "0.0")
    check("format section: a positive value with three sections reads the first", fs("0.0;-0.0;0.0%", D(1)) == "0.0")
    check("format [$%-409]0.00 is not a % format", not fp("[$%-409]0.00"))
    check("format [$-409]0.0% is a % format", fp("[$-409]0.0%"))
    cf = mod.check_format

    def refused(f, msg):
        try:
            cf(f)
            return False
        except mod.RowError as e:
            return str(e) == msg
        except Exception:
            return False
    for f in ("[<1]0.0%;0.0", "[>=1]0.0;0.0%", "[=0]0", "[>100]0", "[Red][<=5]0", "0;0;0;0;0"):
        check(f"format {f!r} refused as conditional", refused(f, "conditional number format not supported"))
    for f in ("0%%", "0.0%;0%%", "0%0%", "%0%"):
        check(f"format {f!r} refused: more than one %", refused(f, "format has more than one %"))
    for f in ("0%;@", "0.0%;@", "[Red]0%;@", "@", "0;@", "0;0;@", "0;@;0;@", "@;0"):
        check(f"format {f!r} refused: text section outside the fourth", refused(f, "format has a text section outside the fourth"))
    for f in ("0,", "#,##0,,", "0.0,", "#,##0,;-#,##0", "0,%"):
        check(f"format {f!r} refused: scales by thousands", refused(f, "format scales by thousands"))
    for f in ("General", "#,##0", "#,##0.00", "[Red]#,##0;[Blue]-#,##0", '0.0" ,"', "[$%-409]0.00",
              "[$-409]#,##0.0%", '0.0%"%"', "0;0;0;@", "0\\,", "[h]:mm",
              '0%;"@"', "0\\@", '0;0;0;"x"@'):
        try:
            cf(f)
            check(f"format {f!r} accepted by the format check", True)
        except Exception:
            check(f"format {f!r} accepted by the format check", False)
    pd = mod.parse_date
    check("date 1/5/2026 and 2026-01-05 read", pd("1/5/2026") == pd("2026-01-05"))
    for bad in ("1/5/26", "2026/01/05", "1/5/2026 0:00", "2026-1-5", "13/1/2026", "١/5/2026", "5.1.2026"):
        try:
            pd(bad)
            check(f"date {bad!r} unreadable", False)
        except ValueError:
            check(f"date {bad!r} unreadable", True)
        except Exception:  # any other error is not the refusal asked for
            check(f"date {bad!r} unreadable", False)

    # --- made-up sources
    book = os.path.join(tmp, "made_up_budget.xlsx")
    gl = os.path.join(tmp, "made_up_gl.csv")
    gl_flip = os.path.join(tmp, "made_up_gl_flipped.csv")
    gl_mal = os.path.join(tmp, "made_up_gl_malformed.csv")
    gl_bad = os.path.join(tmp, "made_up_gl_bad_amount.csv")
    gl_bad2 = os.path.join(tmp, "made_up_gl_bad_amount_out_of_range.csv")
    gl_amt = os.path.join(tmp, "made_up_gl_three_bad_amounts.csv")
    gl_tsp = os.path.join(tmp, "made_up_gl_header_trailing_space.csv")
    gl_tab = os.path.join(tmp, "made_up_gl_header_tab_before_store.csv")
    gl_long = os.path.join(tmp, "made_up_gl_long_field.csv")
    gl_date = os.path.join(tmp, "made_up_gl_bad_date.csv")
    gl_date2 = os.path.join(tmp, "made_up_gl_two_digit_year.csv")
    gl_date3 = os.path.join(tmp, "made_up_gl_date_with_time.csv")
    gl_span = os.path.join(tmp, "made_up_gl_spanning_quote.csv")
    gl_bom = os.path.join(tmp, "made_up_gl_bom.csv")
    gl_trim = os.path.join(tmp, "made_up_gl_trimmed_header.csv")
    gl_order = os.path.join(tmp, "made_up_gl_reordered_header.csv")
    gl_dup = os.path.join(tmp, "made_up_gl_duplicate_column.csv")
    write_book(book)
    from openpyxl import load_workbook
    wbx = load_workbook(book, read_only=True, data_only=True)
    e8 = [c.value for r in wbx["Budget 2027"].iter_rows(min_row=8, max_row=9, min_col=5, max_col=5) for c in r]
    check("made-up xlsx carries the raw Excel floats", e8 == [float(FLOAT_A), float(FLOAT_B)]
          and repr(e8[0]) == FLOAT_A and repr(e8[1]) == FLOAT_B)
    wbx.close()
    write_gl(gl)
    write_gl(gl_flip, flip=True)
    write_gl(gl_mal, raw_extra="46100-30,SJ,5/5/2026,D1,extra field,,10,0,POW,SURPLUS\r\n")
    write_gl(gl_bad, extra=[("46100-30", "SJ", "5/5/2026", "", "12x", "POW")])
    write_gl(gl_bad2, extra=[("46100-30", "ZZ", "12/1/2025", "", "12x", "POW")])   # other journal, out of range
    write_gl(gl_amt, extra=[("46100-30", "ZZ", "12/1/2025", "", "$", "POW"),        # out of range, other journal
                            ("46100-30", "SJ", "10/5/2026", "--5", "", "POW"),      # out of range
                            ("46100-30", "ZZ", "5/5/2026", "", "1,23", "POW"),      # other journal
                            ("47100-30", "SJ", "5/5/2026", "", "(-5)", "POW"),      # account not asked
                            ("46100-30", "SJ", "5/5/2026", "", "1,2,3", "LDS")])    # store not asked
    write_gl(gl_tsp, header_line=",".join(GL_HEADER) + " ")
    write_gl(gl_tab, header_line=",".join(GL_HEADER[:-1]) + "\tStore")
    write_gl(gl_long, desc="ZEBRA" * 60000)  # 300,000-char field
    write_gl(gl_date, extra=[("46100-30", "ZZ", "13/45/2026", "", "1", "POW"),   # matches account+store
                             ("47100-30", "SJ", "99/99/2026", "", "1", "POW")])  # matches nothing
    write_gl(gl_date2, extra=[("46100-30", "SJ", "1/5/26", "", "1", "POW")])
    write_gl(gl_date3, extra=[("46100-30", "SJ", "1/5/2026 0:00", "", "1", "POW")])
    write_gl(gl_span, raw_extra='46100-30,SJ,5/5/2026,D9,"line one\nline two",,10,0,POW\r\n')
    write_gl(gl_bom, bom=True)
    write_gl(gl_trim, header_line="Account,Journal,Date,Doc #,Description,Debit Amount,Credit Amount,Balance,Store")
    write_gl(gl_order, header_line="Account ,Journal ,Date,Description,Doc #,Debit Amount,Credit Amount,Balance,Store")
    write_gl(gl_dup, header_line="Account ,Journal ,Date,Doc #,Description,Debit Amount,Credit Amount,Balance,Store,Store")
    with open(gl, encoding="utf-8") as f:
        check("made-up GL header has trailing spaces", f.readline().startswith("Account ,Journal ,Date"))
    with open(gl_bom, "rb") as f:
        check("made-up BOM GL starts with a BOM", f.read(3) == b"\xef\xbb\xbf")

    G = "accounts=46xxx-30;store=POW;from=2026-01-01;to=2026-09-30;side=credit-debit"
    BK = "'Budget 2027'!"
    fig = os.path.join(tmp, "figures_main.csv")
    out = os.path.join(tmp, "result_main.csv")
    bmd5, bsize = md5_size(book)
    write_figures(fig, [
        ("KS1", "Sum kind", "4,584", "usd", "2026", "sum", "", "C1+G1", "as-is"),
        ("KS2", "Sum kind with a source", "1,234", "usd", "2026", "sum", book, BK + "B7", "as-is"),
        ("KR1", "Ratio kind", "36.8%", "pct", "2026", "ratio", "", "C1/G1", "fraction-to-pct"),
        ("KO1", "Other kind", "1,234", "usd", "2026", "formula", book, BK + "B7", "as-is"),
        ("C1", "Budget cell", "1,234", "usd", "2027", "cell", book, BK + "B7", "as-is"),
        ("C2", "Budget cell planted wrong", "1,240", "usd", "2027", "cell", book, BK + "B7", "as-is"),
        ("G1", "Training GL", "$3,350", "usd", "Jan-Sep 2026", "gl", gl, G, "as-is"),
        ("G2", "Training GL flipped line", "3,350", "usd", "Jan-Sep 2026", "gl", gl_flip, G, "as-is"),
        ("G3", "Training GL journal SJ", "3,500", "usd", "Jan-Sep 2026", "gl", gl, G + ";journal=SJ", "as-is"),
        ("G4", "Training GL debit side", "(3,350)", "usd", "Jan-Sep 2026", "gl", gl,
         G.replace("credit-debit", "debit-credit"), "as-is"),
        ("G5", "GL matching nothing", "0", "usd", "2026", "gl", gl, G.replace("46xxx-30", "99xxx-30"), "as-is"),
        ("G6", "GL with a malformed line", "3,350", "usd", "2026", "gl", gl_mal, G, "as-is"),
        ("G7", "GL with a bad amount", "3,350", "usd", "2026", "gl", gl_bad, G, "as-is"),
        ("G8", "GL with a 300k field", "3,350", "usd", "2026", "gl", gl_long, G, "as-is"),
        ("G9", "GL repeated key", "3,350", "usd", "2026", "gl", gl, G + ";store=POW", "as-is"),
        ("G10", "GL exact account", "850", "usd", "2026", "gl", gl, G.replace("46xxx-30", "46100-30"), "as-is"),
        ("G11", "GL bad date, other journal", "3,500", "usd", "2026", "gl", gl_date, G + ";journal=SJ", "as-is"),
        ("G12", "GL quote spanning lines", "3,350", "usd", "2026", "gl", gl_span, G, "as-is"),
        ("G13", "GL with scale points", "3,350", "usd", "2026", "gl", gl, G, "points"),
        ("G14", "GL from the 2nd", "2,350", "usd", "2026", "gl", gl, G.replace("2026-01-01", "2026-01-02"), "as-is"),
        ("G15", "GL bad amount, other journal, out of range", "3,500", "usd", "2026", "gl", gl_bad2,
         G + ";journal=SJ", "as-is"),
        ("G16", "GL two-digit year", "3,350", "usd", "2026", "gl", gl_date2, G, "as-is"),
        ("G17", "GL date with a time", "3,350", "usd", "2026", "gl", gl_date3, G, "as-is"),
        ("G18", "GL with a BOM", "3,350", "usd", "2026", "gl", gl_bom, G, "as-is"),
        ("G19", "GL trimmed header", "3,350", "usd", "2026", "gl", gl_trim, G, "as-is"),
        ("G20", "GL reordered header", "3,350", "usd", "2026", "gl", gl_order, G, "as-is"),
        ("G21", "GL duplicate column", "3,350", "usd", "2026", "gl", gl_dup, G, "as-is"),
        ("G22", "GL shown with %", "3,350%", "usd", "2026", "gl", gl, G, "as-is"),
        ("G23", "GL from as 20260101", "3,350", "usd", "2026", "gl", gl, G.replace("2026-01-01", "20260101"), "as-is"),
        ("G24", "GL from and to as M/D/YYYY", "3,350", "usd", "2026", "gl", gl,
         G.replace("2026-01-01", "1/1/2026").replace("2026-09-30", "9/30/2026"), "as-is"),
        ("G25", "GL three bad amounts off range or journal", "3,500", "usd", "2026", "gl", gl_amt,
         G + ";journal=SJ", "as-is"),
        ("G27", "GL accounts list with a dead account", "850", "usd", "2026", "gl", gl,
         G.replace("46xxx-30", "46100-30,46999-30"), "as-is"),
        ("G28", "GL accounts list, both live", "3,350", "usd", "2026", "gl", gl,
         G.replace("46xxx-30", "46100-30,46200-30"), "as-is"),
        ("G29", "GL header with a trailing space", "3,350", "usd", "2026", "gl", gl_tsp, G, "as-is"),
        ("G30", "GL header with a tab before Store", "3,350", "usd", "2026", "gl", gl_tab, G, "as-is"),
        ("G26", "GL to as 2026-9-30", "3,350", "usd", "2026", "gl", gl, G.replace("2026-09-30", "2026-9-30"), "as-is"),
        ("P1", "Pct cell tied", "45.2%", "pct", "2027", "cell", book, BK + "E5", "fraction-to-pct"),
        ("P2", "Pct cell off", "0.45%", "pct", "2027", "cell", book, BK + "E5", "fraction-to-pct"),
        ("P3", "Pct shown, scale as-is", "45.2%", "pct", "2027", "cell", book, BK + "E5", "as-is"),
        ("P4", "Pct format, scale points", "0.5%", "pct", "2027", "cell", book, BK + "E5", "points"),
        ("P5", "Points cell tied", "45.2%", "pct", "2027", "cell", book, BK + "E6", "points"),
        ("P6", "Points cell called fraction", "4,520%", "pct", "2027", "cell", book, BK + "E6", "fraction-to-pct"),
        ("P7", "General-format fraction called fraction", "45.2%", "pct", "2027", "cell", book, BK + "E7", "fraction-to-pct"),
        ("P8", "Scale blank", "1,234", "usd", "2027", "cell", book, BK + "B7", ""),
        ("P9", "Scale unknown", "1,234", "usd", "2027", "cell", book, BK + "B7", "thousands"),
        ("P10", "Quoted % format called fraction", "45.2%", "pct", "2027", "cell", book, BK + "E10", "fraction-to-pct"),
        ("P11", "% format read as-is", "12", "usd", "2027", "cell", book, BK + "E11", "as-is"),
        ("P12", "Text cell", "45", "usd", "2027", "cell", book, BK + "E12", "as-is"),
        ("FS1", "Neg value, neg section without %", "-45.2%", "pct", "2027", "cell", book, BK + "E13", "fraction-to-pct"),
        ("FS2", "Neg value, neg section with %", "(45.2%)", "pct", "2027", "cell", book, BK + "E14", "fraction-to-pct"),
        ("FS3", "Pos value, pos section without %", "45.2%", "pct", "2027", "cell", book, BK + "E15", "fraction-to-pct"),
        ("FS4", "Pos value, pos section without %, as-is", "0.452", "usd", "2027", "cell", book, BK + "E15", "as-is"),
        ("FS5", "Neg value, one % section", "-45.2%", "pct", "2027", "cell", book, BK + "E16", "fraction-to-pct"),
        ("FS6", "Neg value, neg section without %, as-is", "-0.452", "usd", "2027", "cell", book, BK + "E13", "as-is"),
        ("FS7", "Neg value, three sections, second has %", "(45.2%)", "pct", "2027", "cell", book, BK + "E17", "fraction-to-pct"),
        ("CF1", "Condition [<1], cell 5, shown 500%", "500%", "pct", "2027", "cell", book, BK + "E18", "fraction-to-pct"),
        ("CF2", "Condition [>=1], cell 0.5, shown 0.5", "0.5", "usd", "2027", "cell", book, BK + "E19", "as-is"),
        ("CF3", "Five sections", "7", "usd", "2027", "cell", book, BK + "E25", "as-is"),
        ("FZ1", "Zero, third section has %", "0.0%", "pct", "2027", "cell", book, BK + "E20", "fraction-to-pct"),
        ("FZ2", "Zero, third section has no %", "0.0", "usd", "2027", "cell", book, BK + "E21", "as-is"),
        ("FZ3", "Zero, third section has %, read as-is", "0.0", "usd", "2027", "cell", book, BK + "E20", "as-is"),
        ("FP1", "Format with two %", "45.2%", "pct", "2027", "cell", book, BK + "E22", "fraction-to-pct"),
        ("FT1", "Format scales by thousands", "1,234", "usd", "2027", "cell", book, BK + "E23", "as-is"),
        ("FA1", "Cell -50, 0%;@, points, shown -50%", "-50%", "pct", "2027", "cell", book, BK + "E26", "points"),
        ("FA2", "Cell -0.5, 0%;@, fraction-to-pct, shown -50%", "-50%", "pct", "2027", "cell", book, BK + "E27", "fraction-to-pct"),
        ("FA3", "Cell 50, 0;0;@, as-is, shown 50", "50", "usd", "2027", "cell", book, BK + "E28", "as-is"),
        ("FL1", "% only in a locale bracket", "0.452", "usd", "2027", "cell", book, BK + "E24", "as-is"),
        ("BD1", "Date cell", "46,027", "usd", "2027", "cell", book, BK + "B13", "as-is"),
        ("BB1", "Boolean cell", "1", "usd", "2027", "cell", book, BK + "B14", "as-is"),
        ("BL1", "1e30 cell shown 1", "1", "usd", "2027", "cell", book, BK + "B15", "as-is"),
        ("V1", "Shown 0.5 against 0.5", "0.5", "usd", "2027", "cell", book, BK + "B16", "as-is"),
        ("E1", "Excel float 14.499999999999998", "15", "usd", "2027", "cell", book, BK + "E8", "as-is"),
        ("E2", "Excel float 1234.4999999999998", "1,235", "usd", "2027", "cell", book, BK + "E9", "as-is"),
        ("E3", "Excel float shown 14", "14", "usd", "2027", "cell", book, BK + "E8", "as-is"),
        ("H1", "Half: 1,234 against 1234.50", "1,234", "usd", "2027", "cell", book, BK + "B8", "as-is"),
        ("H2", "Half: 1,235 against 1234.50", "1,235", "usd", "2027", "cell", book, BK + "B8", "as-is"),
        ("H3", "Negative shown, positive value", "-1,235", "usd", "2027", "cell", book, BK + "B8", "as-is"),
        ("H4", "Negative half", "(1,235)", "usd", "2027", "cell", book, BK + "B9", "as-is"),
        ("H5", "Positive shown, negative value", "1,235", "usd", "2027", "cell", book, BK + "B9", "as-is"),
        ("Z0A", "-0 against +0.30", "-0", "usd", "2027", "cell", book, BK + "B10", "as-is"),
        ("Z0B", "(0) against -0.30", "(0)", "usd", "2027", "cell", book, BK + "B11", "as-is"),
        ("Z0C", "0 against -0.30", "0", "usd", "2027", "cell", book, BK + "B11", "as-is"),
        ("Z0D", "-0.0 against 0", "-0.0", "usd", "2027", "cell", book, BK + "B12", "as-is"),
        ("Z0E", "0 against +0.30", "0", "usd", "2027", "cell", book, BK + "B10", "as-is"),
        ("SH1", "Shown 1,00", "1,00", "usd", "2027", "cell", book, BK + "B7", "as-is"),
        ("SH2", "Shown (-12)", "(-12)", "usd", "2027", "cell", book, BK + "B7", "as-is"),
        ("SH3", "Shown 0,123", "0,123", "usd", "2027", "cell", book, BK + "B7", "as-is"),
        ("SH4", "Shown 01,234", "01,234", "usd", "2027", "cell", book, BK + "B7", "as-is"),
        ("SH5", "Shown padded with no-break spaces", " 1,234 ", "usd", "2027", "cell", book, BK + "B7", "as-is"),
        ("SH6", "Shown padded with ASCII spaces", "  1,234  ", "usd", "2027", "cell", book, BK + "B7", "as-is"),
        ("Z0F", "0 against exact 0", "0", "usd", "2027", "cell", book, BK + "B12", "as-is"),
        ("K1", "1.2M against 1,234,000", "1.2M", "usd", "2027", "cell", book, BK + "C2", "as-is"),
        ("K2", "1.2M against 1,260,000", "1.2M", "usd", "2027", "cell", book, BK + "C3", "as-is"),
        ("K3", "1.2k against 1,249", "1.2k", "usd", "2027", "cell", book, BK + "C4", "as-is"),
        ("K4", "1.3k against 1,250", "1.3k", "usd", "2027", "cell", book, BK + "C5", "as-is"),
        ("K5", "1.2k against 1,250", "1.2k", "usd", "2027", "cell", book, BK + "C5", "as-is"),
        ("N1", "Students", "12", "count", "2026", "none", "", "", ""),
        ("N2", "Cell kind, blank source", "12", "count", "2026", "cell", "", BK + "B7", "as-is"),
        ("N3", "Blank kind, blank source", "12", "count", "2026", "", "", "", ""),
        ("N4", "Gl kind, blank source", "3,350", "usd", "2026", "gl", "", G, "as-is"),
        ("M1", "Cell md5 wrong", "1,234", "usd", "2027", "cell", book, BK + "B7", "as-is", "deadbeef", bsize),
        ("M2", "Cell md5 right (full 32)", "1,234", "usd", "2027", "cell", book, BK + "B7", "as-is",
         hashlib.md5(open(book, "rb").read()).hexdigest(), bsize),
        ("M3", "Cell md5 and size blank", "1,234", "usd", "2027", "cell", book, BK + "B7", "as-is", "", ""),
        ("M4", "GL md5 and size blank", "3,350", "usd", "2026", "gl", gl, G, "as-is", "", ""),
        ("M5", "Cell size wrong", "1,234", "usd", "2027", "cell", book, BK + "B7", "as-is", bmd5, "12"),
        ("M6", "Cell md5 blank, size right", "1,234", "usd", "2027", "cell", book, BK + "B7", "as-is", "", bsize),
        ("M7", "GL md5 blank, size right", "3,350", "usd", "2026", "gl", gl, G, "as-is", "", md5_size(gl)[1]),
        ("M8", "Cell size blank, md5 right", "1,234", "usd", "2027", "cell", book, BK + "B7", "as-is", bmd5, ""),
        ("X1", "Master past E", "99", "usd", "2027", "cell", book, "Master!F2", "as-is"),
        ("X2", "Master in B", "10", "usd", "2027", "cell", book, "Master!B2", "as-is"),
        ("X3", "Master column A", "5", "usd", "2027", "cell", book, "Master!A2", "as-is"),
        ("F1", "Formula never calculated", "2,469", "usd", "2027", "cell", book, BK + "D1", "as-is"),
    ])
    code, so, se = run_tie(fig, out)
    rows, glt = read_out(out)
    st = {k: v["status"] for k, v in rows.items()}
    note = {k: v["note"] for k, v in rows.items()}

    def is_(rid, status, note_has=None):
        ok = st.get(rid) == status and (note_has is None or note_has in note.get(rid, ""))
        check(f"{rid} is {status}" + (f" ({note_has})" if note_has else ""), ok)

    def exactly(rid, status, note_is):
        check(f"{rid} is exactly {status} / {note_is!r}", st.get(rid) == status and note.get(rid) == note_is)

    for rid in ("C1", "G1", "G3", "G4", "G8", "G10", "G14", "G18", "G24",
                "P1", "P5", "E1", "E2", "H2", "H4", "Z0B", "Z0D", "Z0E", "Z0F", "K1", "K3", "K4", "M2", "X2",
                "FS2", "FS4", "FS5", "FS6", "FS7", "V1", "SH6", "FZ1", "FZ2", "FL1", "G28"):
        is_(rid, "TIED")
    for rid in ("C2", "G2", "P2", "E3", "H1", "H3", "H5", "Z0A", "Z0C", "K2", "K5"):
        is_(rid, "OFF")
    for rid in ("KS1", "KS2", "KR1", "KO1"):
        exactly(rid, "ERROR", "kind not supported (cell and gl only)")
    for rid in ("N1", "N2", "N3", "N4"):
        exactly(rid, "NO SOURCE", "no source named")
    is_("G22", "ERROR", "a gl row's shown cannot hold %")
    is_("G23", "ERROR", "gl from/to must be YYYY-MM-DD or M/D/YYYY")
    is_("G26", "ERROR", "gl from/to must be YYYY-MM-DD or M/D/YYYY")
    is_("G25", "ERROR", "3 matched lines with unreadable amount, 0 with unreadable date")
    for rid in ("FS1", "FS3"):
        is_(rid, "ERROR", "scale disagrees with the cell's format (fraction-to-pct needs a % format)")
    for rid in ("CF1", "CF2", "CF3"):
        exactly(rid, "ERROR", "conditional number format not supported")
    is_("FZ3", "ERROR", "scale disagrees with the cell's format (as-is with a % format)")
    exactly("FP1", "ERROR", "format has more than one %")
    exactly("FT1", "ERROR", "format scales by thousands")
    for rid in ("FA1", "FA2", "FA3"):
        exactly(rid, "ERROR", "format has a text section outside the fourth")
    exactly("G27", "ERROR", "account 46999-30 matched no line")
    for rid in ("G29", "G30"):
        is_(rid, "ERROR", "GL header not as expected")
    exactly("BD1", "ERROR", "cell holds a date")
    exactly("BB1", "ERROR", "cell holds a boolean")
    exactly("BL1", "ERROR", "value too large to round")
    check("BL1 does not stop the run (exit is 1, not 2)", code == 1)
    check("G1 recomputed 3,350.00 on 4 lines",
          rows.get("G1", {}).get("recomputed") == "3,350.00" and "4 GL lines matched" in note.get("G1", ""))
    check("G2 recomputed 1,350.00 (flipped line)", rows.get("G2", {}).get("recomputed") == "1,350.00")
    is_("G5", "ERROR", "no GL lines matched")
    is_("G6", "ERROR", "1 malformed GL lines")
    is_("G7", "ERROR", "1 matched lines with unreadable amount")
    is_("G9", "ERROR", "repeated key")
    is_("G11", "ERROR", "1 with unreadable date")
    is_("G12", "ERROR", "GL records 14 ≠ lines 15")
    is_("G13", "ERROR", "scale must be as-is")
    is_("G15", "ERROR", "1 matched lines with unreadable amount")
    is_("G16", "ERROR", "1 with unreadable date")
    is_("G17", "ERROR", "1 with unreadable date")
    is_("G19", "ERROR", "GL header not as expected")
    is_("G20", "ERROR", "GL header not as expected")
    is_("G21", "ERROR", "GL header not as expected")
    is_("P3", "ERROR", "scale/% mismatch")
    for rid in ("P4", "P6", "P7", "P10", "P11"):
        is_(rid, "ERROR", "scale disagrees with the cell's format")
    is_("P8", "ERROR", "scale not given")
    is_("P9", "ERROR", "unknown scale")
    is_("P12", "ERROR", "cell holds text")
    is_("SH1", "ERROR", "shown not readable")
    for rid in ("SH2", "SH3", "SH4", "SH5"):
        exactly(rid, "ERROR", "shown not readable")
    is_("M1", "ERROR", "source changed")
    for rid in ("M3", "M4", "M6", "M7", "M8"):
        is_(rid, "ERROR", "md5/size not given")
    is_("M5", "ERROR", "source changed")
    is_("X1", "ERROR", "Master past column E")
    is_("X3", "ERROR", "Master column A")
    is_("F1", "ERROR", "no cached value")
    g1 = {r["account"]: r for r in glt if r["id"] == "G1"}
    check("GL table: 46100-30 sum 850.00 on 3 lines",
          g1.get("46100-30", {}).get("sum") == "850.00" and g1.get("46100-30", {}).get("lines matched") == "3")
    check("GL table: 46200-30 sum 2,500.00 on 1 line",
          g1.get("46200-30", {}).get("sum") == "2,500.00" and g1.get("46200-30", {}).get("lines matched") == "1")
    check("GL table: 46A00-30 and 46100-301 never matched", "46A00-30" not in g1 and "46100-301" not in g1)
    check("stdout shows the GL accounts table", "GL accounts" in so and "46200-30" in so)
    n_bad = sum(1 for s in st.values() if s != "TIED")
    check("main run exit code 1", code == 1)
    check("main run last line RESULT: FAIL (n of m)",
          last_line(so) == f"RESULT: FAIL ({n_bad} of {len(st)} rows not TIED)")
    out_text = open(out, encoding="utf-8").read() if os.path.isfile(out) else ""
    leak = any(s in text for s in (SECRET_DESC, "ZEBRA", SECRET_DOC, "line one") for text in (so, se, out_text))
    check("no GL Description or Doc # in stdout, stderr or out CSV", not leak)

    # --- self-check: it can pass, and it fails on a planted wrong figure
    clean = os.path.join(tmp, "figures_clean.csv")
    planted = os.path.join(tmp, "figures_planted.csv")
    base = [
        ("C1", "Budget cell", "1,234", "usd", "2027", "cell", book, BK + "B7", "as-is"),
        ("G1", "Training GL", "3,350", "usd", "2026", "gl", gl, G, "as-is"),
        ("P1", "Pct cell", "45.2%", "pct", "2027", "cell", book, BK + "E5", "fraction-to-pct"),
    ]
    write_figures(clean, base)
    code, so, _ = run_tie(clean)
    check("self-check clean file: RESULT: PASS, exit 0", code == 0 and last_line(so) == "RESULT: PASS")
    write_figures(planted, [("C1", "Budget cell", "1,334") + base[0][3:]] + base[1:])
    code, so, _ = run_tie(planted)
    check("self-check planted wrong figure: RESULT: FAIL, exit 1",
          code == 1 and last_line(so) == "RESULT: FAIL (1 of 3 rows not TIED)")

    # --- bad input
    code, _, _ = run_tie(os.path.join(tmp, "no_such_figures.csv"))
    check("missing figures file: exit 2", code == 2)
    badhdr = os.path.join(tmp, "figures_bad_header.csv")
    with open(badhdr, "w", encoding="utf-8", newline="") as f:
        f.write("id,label,value\nA,b,1\n")
    code, _, _ = run_tie(badhdr)
    check("bad figures header: exit 2", code == 2)
    noscale = os.path.join(tmp, "figures_no_scale_column.csv")
    write_figures(noscale, [base[0][:8] + (bmd5, bsize)],
                  header=[c for c in FIG_HEADER if c != "scale"])
    code, _, se = run_tie(noscale)
    check("figures without a scale column: exit 2", code == 2 and "scale" in se)
    extra = os.path.join(tmp, "figures_extra_field.csv")
    with open(extra, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(FIG_HEADER)
        w.writerow(list(base[0]) + [bmd5, bsize, "SURPLUS"])
    code, _, se = run_tie(extra)
    check("figures row with more fields than the header: exit 2", code == 2 and "more fields" in se)
    dup = os.path.join(tmp, "figures_duplicate_column.csv")
    with open(dup, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(FIG_HEADER + ["shown"])
        w.writerow(list(base[0]) + [bmd5, bsize, "9,999"])
    code, _, se = run_tie(dup)
    check("figures header with a duplicate column name: exit 2", code == 2 and "duplicate column" in se)
    fewer = os.path.join(tmp, "figures_same_row_no_extra.csv")
    with open(fewer, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(FIG_HEADER)
        w.writerow(list(base[0]) + [bmd5, bsize])
    code, so, _ = run_tie(fewer)
    check("the same row without the extra field: RESULT: PASS", code == 0 and last_line(so) == "RESULT: PASS")
    fig_md5 = md5_size(clean)
    code, _, _ = run_tie(clean, out=clean)
    check("--out equal to the figures file: exit 2, file unchanged", code == 2 and md5_size(clean) == fig_md5)
    gl_md5 = md5_size(gl)
    code, _, _ = run_tie(clean, out=os.path.join(tmp, ".", "made_up_gl.csv"))
    check("--out equal to a source file: exit 2, file unchanged", code == 2 and md5_size(gl) == gl_md5)
    p = subprocess.run([sys.executable, "-I", "-B", os.path.abspath(__file__)],
                       capture_output=True, text=True, encoding="utf-8")
    check("test without --bench: exit 2 with a usage line", p.returncode == 2 and "usage" in p.stderr)
    check("no __pycache__ written or changed beside the programs", pycache_state() == cache_before)

    failed = [n for n, ok in results if not ok]
    if failed:
        print("TESTS: FAIL (" + "; ".join(failed) + ")")
        return 1
    print(f"TESTS: PASS ({len(results)})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
