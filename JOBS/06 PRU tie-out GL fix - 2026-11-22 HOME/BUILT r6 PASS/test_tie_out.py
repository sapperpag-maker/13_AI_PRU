"""test_tie_out.py - tests for tie_out.py on made-up files only.

Usage:  python3.14 -I -B test_tie_out.py --bench <folder>

--bench is required: the test builds every file itself in a new folder under
<folder>\\test-runs (never real data, never the system temp folder), writes
no __pycache__ and deletes nothing.
Last line: TESTS: PASS (n) or TESTS: FAIL (names).
"""

import sys

sys.dont_write_bytecode = True  # before any import of tie_out

import contextlib
import csv
import hashlib
import importlib.util
import io
import os
import re
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
FIG_HEADER = ["id", "label", "shown", "unit", "period", "kind", "source", "detail", "md5", "size"]
OLD_HEADER = ["id", "label", "shown", "unit", "period", "kind", "source", "detail", "scale", "md5", "size"]
FORMAT_NAMES = ("check_format", "format_section_for", "format_has_pct", "format_scan",
                "format_sections", "scale_of", "SCALES", "FORMAT_ERR")
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
                         ("E28", 50, "0;0;@"),                 # @ as the third section
                         ("E29", -0.5, '0%;"neg"'),            # r7 A1: second section shows no number
                         ("E30", -0.125, "0.0%;;0.0%"),        # r7 A1: empty second section
                         ("E31", -50, "0%;"),                  # r7 A1: empty second section
                         ("E32", 50, '"pos";0%'),              # r7 A1: first section shows no number
                         ("E33", -50, "0%;[Red]"),             # r7 A1: colour only
                         ("E34", -50, "0%;-")):                # r7 A1: a bare -
        ws[ref] = val
        ws[ref].number_format = nf
    ws["B13"] = datetime(2026, 1, 5)         # a date (openpyxl gives it a date format)
    ws["B14"] = True                           # a boolean
    ws["B15"] = 1e30                           # too large to round to whole units
    ws["B16"] = 0.5
    ws["B17"] = 999999999999999000           # 18 digits before the point (15 significant, as Excel holds): read
    ws["B18"] = 10 ** 18                     # 19 digits: ERROR
    ws["B19"] = -(10 ** 18)                  # 19 digits, negative: ERROR
    ws["B20"] = 1e18                         # a float with 19 digits: ERROR
    ws["B21"] = 10 ** 28 + 1                 # 29 digits, beyond Decimal's default 28: ERROR
    ws["B22"] = 0.1234567                    # 7 digits after the point: read (cells have no decimal cap)
    ws["B23"] = -0.123456                    # 6 digits after the point: read
    ws["B24"] = 1e-7                         # 15g gives 1e-07: read
    ws["B25"] = 1 / 3                        # a formula's =1/3: 0.333333333333333 after the cut
    ws["B26"] = 1.23456789012345e-20         # 15 significant digits, far after the point
    ws["B27"] = 1234567890123456             # ints (read back as int): Excel shows 15 significant digits
    ws["B28"] = 333331                       # placeholder: <v>12345678901234567</v> put in below
    ws["B29"] = 333332                       # placeholder: <v>123456789012345678</v>
    ws["B30"] = 123456789012345              # 15 digits: as it is
    ws["B31"] = 1234567890123445             # half up: ...450 (half even would give ...440)
    ws["B32"] = 333333                       # placeholder: <v>123456789012345499</v>; exact cut ...345000,
    #                                          through a float ...346000
    ws["B33"] = 0.000145                     # shown 0.0145%: the column must not print 0.01
    ws["B34"] = -0.0                         # -0: prints as 0
    ws["B35"] = 0.0778                       # job 06: shown +8%
    ws["B36"] = -0.0019771529                # job 06: shown 0%
    ws["B37"] = -0.4                         # job 06: shown 0 ties
    ws["B38"] = -0.6                         # job 06: shown 0 does not tie
    ws["B39"] = -5                           # job 06: shown +$5, signs differ
    ws["B40"] = 5                            # job 06: shown +5 ties
    ws["B41"] = " 45\t"                      # job 06 point 5: a text cell padded, still text
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
                # openpyxl writes a 17-digit int as 1.23e+16; Excel's file holds the digits, read as an int
                for ph, digits in (("333331", "12345678901234567"), ("333332", "123456789012345678"),
                                   ("333333", "123456789012345499")):
                    assert text.count(f"<v>{ph}</v>") == 1
                    text = text.replace(f"<v>{ph}</v>", f"<v>{digits}</v>")
                data = text.encode("utf-8")
            zout.writestr(item, data)


def md5_size(path):
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()[:8], str(os.path.getsize(path))


def write_figures(path, rows, header=FIG_HEADER):
    """8-field rows of kind cell/gl get the source's real md5 and size;
    10-field rows keep what they give (blank md5/size included)."""
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        for r in rows:
            r = list(r)
            if len(r) == 8 and r[5] in ("cell", "gl") and r[6] and os.path.isfile(r[6]):
                r += list(md5_size(r[6]))
            w.writerow(r + [""] * (len(header) - len(r)))


def run_tie(fig, out=None):
    cmd = [sys.executable, "-I", "-B", TIE_OUT, fig]
    if out is not None:
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
    def reads(fn):  # a refusal or any other error is a failed check, never a crash of the suite
        try:
            return fn()
        except Exception:
            return False
    check("shown with 18 digits before the point read",
          reads(lambda: ps("999,999,999,999,999,999")["signed"] == D(10 ** 18 - 1)
                and ps("-123456789012345678.5k")["signed"] == D("-123456789012345678.5")))
    for big in ("1,000,000,000,000,000,000", "1000000000000000000", "(1000000000000000000.5)",
                "1234567890123456789012345499.6", "-1,000,000,000,000,000,000k"):
        try:
            ps(big)
            check(f"shown {big!r} refused: more than 18 digits", False)
        except ValueError as e:
            check(f"shown {big!r} refused: more than 18 digits",
                  str(e) == "shown has more than 18 digits before the point")
    check("shown with 6 digits after the point read",
          reads(lambda: ps("-999,999,999,999,999,999.999999")["signed"] == D("-999999999999999999.999999")
                and ps("(0.123456%)")["signed"] == D("-0.123456") and ps("1.123456k")["decimals"] == 6))
    for long_ in ("1.1234567", "-0.0000001", "(1.1234567)", "1.1234567k", "45.1234567%",
                  "-1." + "0" * 57 + "449"):
        try:
            ps(long_)
            check(f"shown {long_[:20]!r} refused: more than 6 digits after the point", False)
        except ValueError as e:
            check(f"shown {long_[:20]!r} refused: more than 6 digits after the point",
                  str(e) == "shown has more than 6 digits after the point")
    # $ together with % is refused (M3); $ alone and % alone still read
    for both in ("$12.5%", "-$12.5%", "($12.5%)", "−$0.5%"):
        try:
            ps(both)
            check(f"shown {both!r} refused: $ with %", False)
        except ValueError as e:
            check(f"shown {both!r} refused: $ with %", str(e) == "shown has both $ and %")
    check("shown $12.5 and 12.5% still read",
          reads(lambda: ps("$12.5")["signed"] == D("12.5") and ps("12.5%")["pct"] and not ps("$12.5")["pct"]))
    # ints are cut to 15 significant digits half up, exactly, never through a float (F1)
    for n, want in ((123456789012345, "123456789012345"), (1234567890123456, "1234567890123460"),
                    (1234567890123445, "1234567890123450"), (12345678901234567, "12345678901234600"),
                    (123456789012345678, "123456789012346000"), (-1234567890123445, "-1234567890123450"),
                    (99999999999999999, "100000000000000000"),
                    (123456789012345499, "123456789012345000")):   # through a float: ...346000
        check(f"int {n} cut to {want}", reads(lambda: mod.to_decimal(n) == D(want)))
    check("a 15-digit int keeps every digit as it is",
          reads(lambda: str(mod.to_decimal(123456789012345)) == "123456789012345"))
    # the columns print every digit held, never rounded; -0 prints as 0 (M1)
    for v, want in (("0.0145", "0.0145"), ("-0.000001", "-0.000001"), ("-0.00", "0.00"), ("-0", "0"),
                    ("1234567.891", "1,234,567.891"), ("1.23456789012346E+15", "1,234,567,890,123,460"),
                    ("1.23456789012345E-20", "0.0000000000000000000123456789012345")):
        check(f"fmt {v} -> {want}", reads(lambda: mod.fmt(D(v)) == want))
    # negation itself must never round: with the 6-decimal cap lifted, a 72-digit negative is refused
    saved_cap = mod.MAX_DEC_DIGITS
    mod.MAX_DEC_DIGITS = 200
    try:
        long_neg = "1." + "0" * 70 + "1"
        for name, fn in (("shown -", lambda: ps("-" + long_neg)), ("shown ( )", lambda: ps("(" + long_neg + ")")),
                         ("amount -", lambda: mod.parse_amount("-" + long_neg)),
                         ("amount ( )", lambda: mod.parse_amount("(" + long_neg + ")"))):
            try:
                fn()
                check(f"cap lifted: {name} of a 72-digit number refused, never rounded", False)
            except ValueError:
                check(f"cap lifted: {name} of a 72-digit number refused, never rounded", True)
            except Exception:
                check(f"cap lifted: {name} of a 72-digit number refused, never rounded", False)
    finally:
        mod.MAX_DEC_DIGITS = saved_cap
    for bad in ("(-12)", "--12", "-$-12", "1 2", "1$2", "1,00", "12,3456", "١٢", "$-12",
                "-(12)", "abc", "", "12.", ".5", "1,234,56", "12%%", "1.2MM", "(12", "12)", "1.2K",
                "0,123", "01,234", "01", "00", "1,2,3", " 1,234", "1,234 ", "\t1,234",
                "$$900", "$ 900", "- 900", "( 900)", "-$$900"):
        try:
            ps(bad)
            check(f"shown {bad!r} refused", False)
        except ValueError:
            check(f"shown {bad!r} refused", True)
        except Exception:  # any other error is not the refusal asked for
            check(f"shown {bad!r} refused", False)
    # job 06 point 2: a leading + means positive; + anywhere else, or doubled, is refused
    for txt, want, decs, pct in (("+8%", "8", 0, True), ("+$18,233", "18233", 0, False), ("+47", "47", 0, False),
                                 ("+1.2k", "1.2", 1, False), ("+0", "0", 0, False), ("+$0.50", "0.50", 2, False)):
        check(f"job06 shown {txt!r} read as positive {want}",
              reads(lambda: ps(txt)["signed"] == D(want) and not ps(txt)["neg"]
                    and ps(txt)["decimals"] == decs and ps(txt)["pct"] == pct))
    for bad in ("++5", "+-5", "-+5", "+−5", "5+", "+(5)", "(+5)", "$+5", "+ 5", "1+2", "+", "+$", "+5%+",
                "+,5", "+01", "+.5"):
        try:
            ps(bad)
            check(f"job06 shown {bad!r} refused", False)
        except ValueError:
            check(f"job06 shown {bad!r} refused", True)
        except Exception:
            check(f"job06 shown {bad!r} refused", False)
    try:
        ps("+$12.5%")
        check("job06 shown '+$12.5%' refused: $ with %", False)
    except ValueError as e:
        check("job06 shown '+$12.5%' refused: $ with %", str(e) == "shown has both $ and %")

    # --- rounding and sign
    rs = mod.round_to_shown
    check("round 1234.50 to 1,234 precision -> 1235 (half up)", rs(D("1234.50"), ps("1,234")) == D(1235))
    check("round -1234.5 -> -1235 (half up, away from zero)", rs(D("-1234.5"), ps("1,234")) == D(-1235))
    check("round 1,250 at 1.2k precision -> 1.3", rs(D(1250), ps("1.2k")) == D("1.3"))
    check("round 1,234,000 at 1.2M precision -> 1.2", rs(D(1234000), ps("1.2M")) == D("1.2"))
    it = mod.is_tied
    check("sign: -0 against +0.30 is not tied", not it(D("0.30"), ps("-0")))
    check("sign: -0 against -0.30 is tied", it(D("-0.30"), ps("-0")))
    check("sign: -0.0 and 0 both tie an exact 0", it(D(0), ps("-0.0")) and it(D(0), ps("0")))
    # job 06 point 3: a shown zero with no sign ties any value that rounds to zero, either sign
    for txt, val in (("0", "-0.30"), ("0", "-0.4"), ("0", "0.4"), ("0", "-0.4999999"), ("0.0", "-0.04"),
                     ("$0", "-0.49"), ("0k", "-499"), ("0k", "499"), ("0%", "-0.19771529"), ("0.00", "-0.004")):
        check(f"job06 shown {txt!r} ties {val}", reads(lambda: it(D(val), ps(txt))))
    for txt, val in (("0", "-0.6"), ("0", "-0.5"), ("0", "0.5"), ("0.0", "-0.05"), ("0k", "-500"), ("$0", "-1")):
        check(f"job06 shown {txt!r} does not tie {val}", reads(lambda: not it(D(val), ps(txt))))
    check("job06 signed zeros keep their sign: -0 not +0.4, (0) not +0.4, +0 not -0.4; -0 ties -0.4",
          reads(lambda: not it(D("0.4"), ps("-0")) and not it(D("0.4"), ps("(0)"))
                and not it(D("-0.4"), ps("+0")) and it(D("-0.4"), ps("-0")) and it(D("0.4"), ps("+0"))))
    check("job06 + against a negative value: signs differ (+5 vs -5 and +$5 vs -5 not tied; +5 vs 5 tied)",
          reads(lambda: not it(D(-5), ps("+5")) and not it(D(-5), ps("+$5")) and it(D(5), ps("+5"))
                and not mod.sign_agrees(D(-5), ps("+$5"))))
    check("excel float: 14.499999999999998 -> 14.5", mod.to_decimal(float(FLOAT_A)) == D("14.5"))
    check("excel float: 1234.4999999999998 -> 1234.5", mod.to_decimal(float(FLOAT_B)) == D("1234.5"))
    # r4 F1: a float cell is cut to 15 digits half UP from its exact value, as an int is
    check("r4 F1 float 1234567890123.125 cut half up to 1234567890123.13",
          reads(lambda: mod.to_decimal(1234567890123.125) == D("1234567890123.13")))
    check("r4 F1 float -1234567890123.125 cut half up to -1234567890123.13",
          reads(lambda: mod.to_decimal(-1234567890123.125) == D("-1234567890123.13")))
    check("r4 F1 float 1234567890123.125 does not tie shown 1,234,567,890,123.12; ties ...123.13",
          reads(lambda: not it(mod.to_decimal(1234567890123.125), ps("1,234,567,890,123.12"))
                and it(mod.to_decimal(1234567890123.125), ps("1,234,567,890,123.13"))))
    check("r4 F1 float -1234567890123.125 does not tie shown -1,234,567,890,123.12",
          reads(lambda: not it(mod.to_decimal(-1234567890123.125), ps("-1,234,567,890,123.12"))))
    check("r4 F1 float 1234567890123445.0 and int 1234567890123445 both cut to 1234567890123450",
          reads(lambda: mod.to_decimal(1234567890123445.0) == mod.to_decimal(1234567890123445)
                == D(1234567890123450)))
    check("r4 F1 guard: -0.0 reads as 0; NaN and inf stay not finite; 0.1 prints 0.1",
          reads(lambda: mod.to_decimal(-0.0) == 0 and not mod.to_decimal(float("nan")).is_finite()
                and not mod.to_decimal(float("inf")).is_finite()
                and not mod.to_decimal(float("-inf")).is_finite()
                and mod.fmt(mod.to_decimal(0.1)) == "0.1"))
    # r4 F2: the difference is exact or the row is ERROR (recompute_cell stubbed, put back after)
    def run_stub(value, shown_text):
        real = mod.recompute_cell
        mod.recompute_cell = lambda row, pct: value
        try:
            row = {"id": "x", "label": "x", "shown": shown_text, "unit": "", "period": "", "kind": "cell",
                   "source": "stub.xlsx", "detail": "S!A1", "md5": "", "size": ""}
            return mod.run([row])[0][0]
        finally:
            mod.recompute_cell = real
    o = reads(lambda: run_stub(D("1.23456789012345E-50"), "1"))
    check("r4 F2 tiny cell vs shown 1: difference needs rounding -> ERROR, blank difference, clear note",
          bool(o) and o["status"] == mod.ERR and o["difference"] == ""
          and "difference too long to compute without rounding" in o["note"])
    o = reads(lambda: run_stub(D("1234.4"), "1,234"))
    check("r4 F2 guard: an exact difference still prints and the status stands (1234.4 vs 1,234: TIED, 0.4)",
          bool(o) and o["status"] == mod.TIED and o["difference"] == "0.4")

    # --- amounts, patterns, formats, dates
    check("amount (50.00) -> -50", mod.parse_amount("(50.00)") == -50)
    check("amount blank -> 0", mod.parse_amount("") == 0)
    check("amount $1,000.00 -> 1000", mod.parse_amount("$1,000.00") == 1000)
    check("amount spaces only -> 0", mod.parse_amount("   ") == 0)
    check("amount -5 -> -5, -$5 -> -5, ($5) -> -5", mod.parse_amount("-5") == -5
          and mod.parse_amount("-$5") == -5 and mod.parse_amount("($5)") == -5)
    check("amount with 18 digits before the point read",
          reads(lambda: mod.parse_amount("999,999,999,999,999,999.99") == D("999999999999999999.99")
                and mod.parse_amount("(123456789012345678)") == D(-123456789012345678)))
    for big in ("1,000,000,000,000,000,000", "1000000000000000000.00", "($1000000000000000000)",
                "1234567890123456789012345499.6"):
        try:
            mod.parse_amount(big)
            check(f"amount {big!r} refused: more than 18 digits", False)
        except ValueError:
            check(f"amount {big!r} refused: more than 18 digits", True)
    check("amount with 6 digits after the point read, at the cap both ways",
          reads(lambda: mod.parse_amount("(999,999,999,999,999,999.999999)") == D("-999999999999999999.999999")
                and mod.parse_amount("-999,999,999,999,999,999.999999") == D("-999999999999999999.999999")
                and mod.parse_amount("0.000001") == D("0.000001")))
    for long_ in ("1.1234567", "-0.0000001", "(1.1234567)", "1." + "0" * 57 + "449"):
        try:
            mod.parse_amount(long_)
            check(f"amount {long_[:20]!r} refused: more than 6 digits after the point", False)
        except ValueError:
            check(f"amount {long_[:20]!r} refused: more than 6 digits after the point", True)
    oc = mod.out_colon_ok
    check("--out colon rule: a drive letter's colon only",
          oc("C:\\a\\b.csv") and oc("d:b.csv") and oc("rel\\b.csv") and oc("b.csv")
          and not oc("C:\\a\\b.csv:zz") and not oc("b.csv:zz") and not oc("\\\\?\\C:\\a.csv")
          and not oc(":b.csv") and not oc("C:\\a:b\\c.csv") and not oc("1:\\b.csv") and not oc("C::b"))
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
    # --- no number-format reading and no scale left in the program
    with open(TIE_OUT, encoding="utf-8") as f:
        src = f.read()
    check("tie_out.py never reads a number format (no 'number_format' in it)", "number_format" not in src)
    check("tie_out.py has no format reader or scale left",
          not any(hasattr(mod, n) for n in FORMAT_NAMES))
    check("tie_out.py no longer requires a scale column", "scale" not in mod.REQUIRED_COLS + mod.OPTIONAL_COLS)
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
    gl_lower = os.path.join(tmp, "made_up_gl_lower_case_header.csv")
    gl_upper = os.path.join(tmp, "made_up_gl_upper_case_header.csv")
    gl_hsec = os.path.join(tmp, "made_up_gl_header_with_a_secret.csv")
    gl_18 = os.path.join(tmp, "made_up_gl_18_digit_amount.csv")
    gl_19 = os.path.join(tmp, "made_up_gl_19_digit_amount.csv")
    gl_28 = os.path.join(tmp, "made_up_gl_28_digit_amount.csv")
    gl_31 = os.path.join(tmp, "made_up_gl_31_significant_digits.csv")
    gl_70 = os.path.join(tmp, "made_up_gl_70_decimals.csv")
    write_gl(gl_lower, header_line=",".join(GL_HEADER).lower())
    write_gl(gl_upper, header_line=",".join(GL_HEADER).upper())
    write_gl(gl_hsec, header_line=",".join(GL_HEADER[:-1]) + ",Store " + SECRET_DESC)
    write_gl(gl_18, extra=[("46100-30", "SJ", "5/5/2026", "", "999,999,999,999,999,999.00", "POW")])
    write_gl(gl_19, extra=[("46100-30", "SJ", "5/5/2026", "", "1,000,000,000,000,000,000.00", "POW")])
    write_gl(gl_28, extra=[("46100-30", "SJ", "5/5/2026", "", "1234567890123456789012345499.6", "POW")])
    write_gl(gl_31, extra=[("46100-30", "SJ", "5/5/2026", "", "123,456,789,012,345,678.123456", "POW")])
    write_gl(gl_70, extra=[("46100-30", "SJ", "5/5/2026", "", "0." + "1" * 70, "POW")])
    N1_DEBIT = "1." + "0" * 57 + "449"       # the checker's N1 case: a debit of 61 significant digits
    gl_n1 = os.path.join(tmp, "made_up_gl_n1_long_debit.csv")
    gl_neg6 = os.path.join(tmp, "made_up_gl_debit_6_decimals.csv")
    gl_dec7 = os.path.join(tmp, "made_up_gl_amount_7_decimals.csv")
    gl_brk = os.path.join(tmp, "made_up_gl_bracket_credit_at_cap.csv")
    gl_min = os.path.join(tmp, "made_up_gl_minus_credit_at_cap.csv")
    gl_big = os.path.join(tmp, "made_up_gl_11000_lines_at_cap.csv")
    write_gl(gl_n1, extra=[("46100-30", "SJ", "5/5/2026", N1_DEBIT, "", "POW")])
    # 18 + 43 = 61 significant digits: rounded to 60 by the subtraction, the sum with 3,350 would then be exact,
    # so only a trapped subtraction shows it
    gl_n1b = os.path.join(tmp, "made_up_gl_n1_long_debit_18_digits.csv")
    write_gl(gl_n1b, extra=[("46100-30", "SJ", "5/5/2026", "123,456,789,012,345,678." + "0" * 40 + "449", "", "POW")])
    # 60 decimals: the subtraction is exact, only the sum with 3,350 (64 digits) needs rounding
    gl_60 = os.path.join(tmp, "made_up_gl_60_decimals.csv")
    write_gl(gl_60, extra=[("46100-30", "SJ", "5/5/2026", "", "0." + "1" * 60, "POW")])
    gl_n1c = os.path.join(tmp, "made_up_gl_n1_long_debit_18_digits_copy.csv")   # own file: one GL read per row
    write_gl(gl_n1c, extra=[("46100-30", "SJ", "5/5/2026", "123,456,789,012,345,678." + "0" * 40 + "449", "", "POW")])
    write_gl(gl_neg6, extra=[("46100-30", "SJ", "5/5/2026", "123,456,789,012,345,678.123456", "", "POW")])
    write_gl(gl_dec7, extra=[("46100-30", "SJ", "5/5/2026", "", "1.1234567", "POW")])
    write_gl(gl_brk, extra=[("46100-30", "SJ", "5/5/2026", "", "(999,999,999,999,999,999.999999)", "POW")])
    write_gl(gl_min, extra=[("46100-30", "SJ", "5/5/2026", "", "-999,999,999,999,999,999.999999", "POW")])
    write_gl(gl_big, extra=[("46100-30", "SJ", "5/5/2026", "", "999,999,999,999,999,999.999999", "POW")] * 11000)
    # sum 11,000,000,000,000,000,003,349.499995 (29 digits): / 1,000,000 at 28 digits would round to ...3349.50000,
    # then half up to .003350M; held exactly it is .003349M
    gl_big7 = os.path.join(tmp, "made_up_gl_11000_lines_at_cap_29th_digit.csv")
    write_gl(gl_big7, extra=[("46100-30", "SJ", "5/5/2026", "", "999,999,999,999,999,999.999999", "POW")] * 11000
             + [("46100-30", "SJ", "5/5/2026", "0.489005", "", "POW")])
    # job 06 point 1: a GL whose header copies the real one's shape, trailing spaces and CRLF included
    REAL_HEADER = "Account ,Journal ,Date,Doc #,Description,Debit Amount,Credit Amount,Balance,Store "
    gl_real = os.path.join(tmp, "made_up_gl_real_header_shape.csv")
    gl_realbom = os.path.join(tmp, "made_up_gl_real_header_shape_bom.csv")
    gl_tabname = os.path.join(tmp, "made_up_gl_header_tab_after_account.csv")
    gl_nbsp = os.path.join(tmp, "made_up_gl_header_nbsp_after_account.csv")
    gl_eight = os.path.join(tmp, "made_up_gl_header_eight_names.csv")
    gl_sp_in = os.path.join(tmp, "made_up_gl_header_space_inside_name.csv")
    write_gl(gl_real, header_line=REAL_HEADER)
    write_gl(gl_realbom, header_line=REAL_HEADER, bom=True)
    write_gl(gl_tabname, header_line=REAL_HEADER.replace("Account ", "Account\t"))
    write_gl(gl_nbsp, header_line=REAL_HEADER.replace("Account ", "Account "))
    write_gl(gl_eight, header_line=REAL_HEADER.replace(",Store ", ""))
    write_gl(gl_sp_in, header_line=REAL_HEADER.replace("Debit Amount", "Debit  Amount"))
    with open(gl_real, "rb") as f:
        check("job06 made-up GL header is the real shape byte for byte, CRLF ended",
              f.readline() == REAL_HEADER.encode("ascii") + b"\r\n")
    with open(gl_realbom, "rb") as f:
        check("job06 made-up BOM GL: BOM then the real header shape",
              f.readline() == b"\xef\xbb\xbf" + REAL_HEADER.encode("ascii") + b"\r\n")
    with open(gl, encoding="utf-8") as f:
        check("made-up GL header has trailing spaces", f.readline().startswith("Account ,Journal ,Date"))
    with open(gl_bom, "rb") as f:
        check("made-up BOM GL starts with a BOM", f.read(3) == b"\xef\xbb\xbf")

    G = "accounts=46xxx-30;store=POW;from=2026-01-01;to=2026-09-30;side=credit-debit"
    BK = "'Budget 2027'!"
    fig = os.path.join(tmp, "figures_main.csv")
    out = os.path.join(tmp, "result_main.csv")
    bmd5, bsize = md5_size(book)
    with open(book, "rb") as f:
        bfull = hashlib.md5(f.read()).hexdigest()
    with open(gl, "rb") as f:
        glfull = hashlib.md5(f.read()).hexdigest()
    write_figures(fig, [
        ("KS1", "Sum kind", "4,584", "usd", "2026", "sum", "", "C1+G1"),
        ("KS2", "Sum kind with a source", "1,234", "usd", "2026", "sum", book, BK + "B7"),
        ("KR1", "Ratio kind", "36.8%", "pct", "2026", "ratio", "", "C1/G1"),
        ("KO1", "Other kind", "1,234", "usd", "2026", "formula", book, BK + "B7"),
        ("C1", "Budget cell", "1,234", "usd", "2027", "cell", book, BK + "B7"),
        ("C2", "Budget cell planted wrong", "1,240", "usd", "2027", "cell", book, BK + "B7"),
        ("G1", "Training GL", "$3,350", "usd", "Jan-Sep 2026", "gl", gl, G),
        ("G2", "Training GL flipped line", "3,350", "usd", "Jan-Sep 2026", "gl", gl_flip, G),
        ("G3", "Training GL journal SJ", "3,500", "usd", "Jan-Sep 2026", "gl", gl, G + ";journal=SJ"),
        ("G4", "Training GL debit side", "(3,350)", "usd", "Jan-Sep 2026", "gl", gl,
         G.replace("credit-debit", "debit-credit")),
        ("G5", "GL matching nothing", "0", "usd", "2026", "gl", gl, G.replace("46xxx-30", "99xxx-30")),
        ("G6", "GL with a malformed line", "3,350", "usd", "2026", "gl", gl_mal, G),
        ("G7", "GL with a bad amount", "3,350", "usd", "2026", "gl", gl_bad, G),
        ("G8", "GL with a 300k field", "3,350", "usd", "2026", "gl", gl_long, G),
        ("G9", "GL repeated key", "3,350", "usd", "2026", "gl", gl, G + ";store=POW"),
        ("G10", "GL exact account", "850", "usd", "2026", "gl", gl, G.replace("46xxx-30", "46100-30")),
        ("G11", "GL bad date, other journal", "3,500", "usd", "2026", "gl", gl_date, G + ";journal=SJ"),
        ("G12", "GL quote spanning lines", "3,350", "usd", "2026", "gl", gl_span, G),
        ("G14", "GL from the 2nd", "2,350", "usd", "2026", "gl", gl, G.replace("2026-01-01", "2026-01-02")),
        ("G15", "GL bad amount, other journal, out of range", "3,500", "usd", "2026", "gl", gl_bad2,
         G + ";journal=SJ"),
        ("G16", "GL two-digit year", "3,350", "usd", "2026", "gl", gl_date2, G),
        ("G17", "GL date with a time", "3,350", "usd", "2026", "gl", gl_date3, G),
        ("G18", "GL with a BOM", "3,350", "usd", "2026", "gl", gl_bom, G),
        ("G19", "GL trimmed header", "3,350", "usd", "2026", "gl", gl_trim, G),
        ("G20", "GL reordered header", "3,350", "usd", "2026", "gl", gl_order, G),
        ("G21", "GL duplicate column", "3,350", "usd", "2026", "gl", gl_dup, G),
        ("G22", "GL shown with %", "3,350%", "usd", "2026", "gl", gl, G),
        ("G23", "GL from as 20260101", "3,350", "usd", "2026", "gl", gl, G.replace("2026-01-01", "20260101")),
        ("G24", "GL from and to as M/D/YYYY", "3,350", "usd", "2026", "gl", gl,
         G.replace("2026-01-01", "1/1/2026").replace("2026-09-30", "9/30/2026")),
        ("G25", "GL three bad amounts off range or journal", "3,500", "usd", "2026", "gl", gl_amt,
         G + ";journal=SJ"),
        ("G27", "GL accounts list with a dead account", "850", "usd", "2026", "gl", gl,
         G.replace("46xxx-30", "46100-30,46999-30")),
        ("G28", "GL accounts list, both live", "3,350", "usd", "2026", "gl", gl,
         G.replace("46xxx-30", "46100-30,46200-30")),
        ("G29", "GL header with a trailing space", "3,350", "usd", "2026", "gl", gl_tsp, G),
        ("G30", "GL header with a tab before Store", "3,350", "usd", "2026", "gl", gl_tab, G),
        ("G31", "GL header in lower case", "3,350", "usd", "2026", "gl", gl_lower, G),
        ("G32", "GL header in upper case", "3,350", "usd", "2026", "gl", gl_upper, G),
        ("G33", "GL header carrying a secret", "3,350", "usd", "2026", "gl", gl_hsec, G),
        ("G34", "GL 18-digit amount", "1,000,000,000,000,003.349k", "usd", "2026", "gl", gl_18, G),
        ("G35", "GL 19-digit amount", "1,000,000,000,000,003.349k", "usd", "2026", "gl", gl_19, G),
        ("G36", "GL 28-digit amount, shown ...346k", "1,234,567,890,123,456,789,012,346k", "usd", "2026",
         "gl", gl_28, G),
        ("G37", "GL 28-digit amount, shown ...345k", "1,234,567,890,123,456,789,012,345k", "usd", "2026",
         "gl", gl_28, G),
        ("G38", "GL sum of 24 significant digits, shown to 6 decimals",
         "123,456,789,012,349,028.123456", "usd", "2026", "gl", gl_31, G),
        ("G39", "GL sum of 24 significant digits, shown off in the 6th decimal",
         "123,456,789,012,349,028.123457", "usd", "2026", "gl", gl_31, G),
        ("N1A", "N1: a debit of 61 significant digits", "3,349", "usd", "2026", "gl", gl_n1, G),
        ("NG6", "Debit with 6 decimals, negated, ties", "-123,456,789,012,342,328.123456", "usd", "2026",
         "gl", gl_neg6, G),
        ("NG7", "GL amount with 7 decimals", "3,351.123457", "usd", "2026", "gl", gl_dec7, G),
        ("BRK", "Bracket credit at the cap", "(999,999,999,999,996,649.999999)", "usd", "2026", "gl", gl_brk, G),
        ("MIN", "Minus credit at the cap", "-999,999,999,999,996,649.999999", "usd", "2026", "gl", gl_min, G),
        ("BIG", "11,000 lines at the cap (29-digit sum)", "11,000,000,000,000,000.003350M", "usd", "2026",
         "gl", gl_big, G),
        ("BIG2", "11,000 lines at the cap, shown 1 off", "11,000,000,000,000,000.003349M", "usd", "2026",
         "gl", gl_big, G),
        ("BIG3", "29th digit decides the rounding, shown .003349M", "11,000,000,000,000,000.003349M", "usd", "2026",
         "gl", gl_big7, G),
        ("BIG4", "29th digit decides the rounding, shown .003350M", "11,000,000,000,000,000.003350M", "usd", "2026",
         "gl", gl_big7, G),
        ("G40", "GL amount of 70 decimals", "3,350", "usd", "2026", "gl", gl_70, G),
        ("G41", "GL 28-digit amount, shown 3,350", "3,350", "usd", "2026", "gl", gl_28, G),
        ("G26", "GL to as 2026-9-30", "3,350", "usd", "2026", "gl", gl, G.replace("2026-09-30", "2026-9-30")),
        # the % rule: shown with % = stored x 100; shown without % = stored as it is
        ("P1", "Stored 0.452, shown 45.2%", "45.2%", "pct", "2027", "cell", book, BK + "E5"),
        ("P2", "Stored 0.452, shown 0.45%", "0.45%", "pct", "2027", "cell", book, BK + "E5"),
        ("P3", "Stored 0.452, shown 0.452", "0.452", "usd", "2027", "cell", book, BK + "E5"),
        ("P4", "Stored 0.452, shown 45.2 (no %)", "45.2", "usd", "2027", "cell", book, BK + "E5"),
        ("P5", "Stored 45.2, shown 45.2%", "45.2%", "pct", "2027", "cell", book, BK + "E6"),
        ("P6", "Stored 45.2, shown 4,520%", "4,520%", "pct", "2027", "cell", book, BK + "E6"),
        ("P7", "General-format 0.452, shown 45.2%", "45.2%", "pct", "2027", "cell", book, BK + "E7"),
        ("P8", "Stored 45.2, shown 45.2", "45.2", "usd", "2027", "cell", book, BK + "E6"),
        ("P10", "Quoted-% format 0.452, shown 45.2%", "45.2%", "pct", "2027", "cell", book, BK + "E10"),
        ("P11", "% format, stored 12, shown 12", "12", "usd", "2027", "cell", book, BK + "E11"),
        ("P13", "% format, stored 12, shown 12%", "12%", "pct", "2027", "cell", book, BK + "E11"),
        ("P12", "Text cell", "45", "usd", "2027", "cell", book, BK + "E12"),
        ("P14", "Text cell shown with %", "45%", "pct", "2027", "cell", book, BK + "E12"),
        # formats that used to decide the reading: now ignored, the stored value decides
        ("FS1", "-0.452, 0.0%;-0.0, shown -45.2%", "-45.2%", "pct", "2027", "cell", book, BK + "E13"),
        ("FS2", "-0.452, 0.0%;(0.0%), shown (45.2%)", "(45.2%)", "pct", "2027", "cell", book, BK + "E14"),
        ("FS3", "0.452, 0.0;0.0%, shown 45.2%", "45.2%", "pct", "2027", "cell", book, BK + "E15"),
        ("FS4", "0.452, 0.0;0.0%, shown 0.452", "0.452", "usd", "2027", "cell", book, BK + "E15"),
        ("FS5", "-0.452, 0.0%, shown -45.2%", "-45.2%", "pct", "2027", "cell", book, BK + "E16"),
        ("FS6", "-0.452, 0.0%;-0.0, shown -0.452", "-0.452", "usd", "2027", "cell", book, BK + "E13"),
        ("FS7", "-0.452, 0.0;0.0%;0, shown (45.2%)", "(45.2%)", "pct", "2027", "cell", book, BK + "E17"),
        ("CF1", "Condition [<1], cell 5, shown 500%", "500%", "pct", "2027", "cell", book, BK + "E18"),
        ("CF2", "Condition [>=1], cell 0.5, shown 0.5", "0.5", "usd", "2027", "cell", book, BK + "E19"),
        ("CF4", "Condition [<1], cell 5, shown 5.0%", "5.0%", "pct", "2027", "cell", book, BK + "E18"),
        ("CF3", "Five sections, cell 7, shown 7", "7", "usd", "2027", "cell", book, BK + "E25"),
        ("FZ1", "Zero, 0.0;-0.0;0.0%, shown 0.0%", "0.0%", "pct", "2027", "cell", book, BK + "E20"),
        ("FZ2", "Zero, 0.0%;-0.0%;0.0, shown 0.0", "0.0", "usd", "2027", "cell", book, BK + "E21"),
        ("FZ3", "Zero, 0.0;-0.0;0.0%, shown 0.0", "0.0", "usd", "2027", "cell", book, BK + "E20"),
        ("FP1", "Format 0%%, 0.452, shown 45.2%", "45.2%", "pct", "2027", "cell", book, BK + "E22"),
        ("FT1", "Format #,##0, (thousands), 1234, shown 1,234", "1,234", "usd", "2027", "cell", book, BK + "E23"),
        ("FT2", "Format #,##0, (thousands), 1234, shown 1", "1", "usd", "2027", "cell", book, BK + "E23"),
        ("FA1", "Cell -50, 0%;@, shown -50%", "-50%", "pct", "2027", "cell", book, BK + "E26"),
        ("FA2", "Cell -0.5, 0%;@, shown -50%", "-50%", "pct", "2027", "cell", book, BK + "E27"),
        ("FA3", "Cell 50, 0;0;@, shown 50", "50", "usd", "2027", "cell", book, BK + "E28"),
        ("FA4", "Cell -0.5, 0%;@, shown -0.5%", "-0.5%", "pct", "2027", "cell", book, BK + "E27"),
        ("FA5", "Cell -50, 0%;@, shown -50", "-50", "usd", "2027", "cell", book, BK + "E26"),
        # r7's A1 cases
        ("R1", 'Cell -0.5, 0%;"neg", shown -0.5%', "-0.5%", "pct", "2027", "cell", book, BK + "E29"),
        ("R2", 'Cell -0.5, 0%;"neg", shown -50%', "-50%", "pct", "2027", "cell", book, BK + "E29"),
        ("R3", "Cell -0.125, 0.0%;;0.0%, shown -0.1%", "-0.1%", "pct", "2027", "cell", book, BK + "E30"),
        ("R4", "Cell -0.125, 0.0%;;0.0%, shown -12.5%", "-12.5%", "pct", "2027", "cell", book, BK + "E30"),
        ("R5", "Cell -50, 0%;, shown -50%", "-50%", "pct", "2027", "cell", book, BK + "E31"),
        ("R6", "Cell -50, 0%;, shown -50", "-50", "usd", "2027", "cell", book, BK + "E31"),
        ("R7", 'Cell 50, "pos";0%, shown 50%', "50%", "pct", "2027", "cell", book, BK + "E32"),
        ("R8", 'Cell 50, "pos";0%, shown 50', "50", "usd", "2027", "cell", book, BK + "E32"),
        ("R9", 'Cell 50, "pos";0%, shown 5,000%', "5,000%", "pct", "2027", "cell", book, BK + "E32"),
        ("R10", "Cell -50, 0%;[Red], shown -50%", "-50%", "pct", "2027", "cell", book, BK + "E33"),
        ("R11", "Cell -50, 0%;-, shown -50%", "-50%", "pct", "2027", "cell", book, BK + "E34"),
        ("R12", "Cell -50, 0%;-, shown -5,000%", "-5,000%", "pct", "2027", "cell", book, BK + "E34"),
        ("FL1", "% only in a locale bracket", "0.452", "usd", "2027", "cell", book, BK + "E24"),
        ("BD1", "Date cell", "46,027", "usd", "2027", "cell", book, BK + "B13"),
        ("BB1", "Boolean cell", "1", "usd", "2027", "cell", book, BK + "B14"),
        ("BL1", "1e30 cell shown 1", "1", "usd", "2027", "cell", book, BK + "B15"),
        ("CAP1", "18-digit cell, shown 18 digits", "999,999,999,999,999,000", "usd", "2027", "cell", book, BK + "B17"),
        ("CAP2", "18-digit cell, shown 1 off", "999,999,999,999,999,001", "usd", "2027", "cell", book, BK + "B17"),
        ("CAP3", "19-digit cell", "1", "usd", "2027", "cell", book, BK + "B18"),
        ("CAP4", "19-digit negative cell", "-1", "usd", "2027", "cell", book, BK + "B19"),
        ("CAP5", "19-digit float cell, shown in M", "1,000,000,000,000M", "usd", "2027", "cell", book, BK + "B20"),
        ("CAP6", "29-digit cell, shown 1", "1", "usd", "2027", "cell", book, BK + "B21"),
        ("CAP7", "Shown with 19 digits", "1,234,567,890,123,456,789", "usd", "2027", "cell", book, BK + "B7"),
        ("CAP8", "18-digit cell, shown in k", "999,999,999,999,999k", "usd", "2027", "cell", book, BK + "B17"),
        ("DC7", "Cell with 7 decimals", "0.123457", "usd", "2027", "cell", book, BK + "B22"),
        ("DC6", "Cell with 6 decimals", "-0.123456", "usd", "2027", "cell", book, BK + "B23"),
        ("DC6P", "Cell with 6 decimals, shown with %", "-12.3456%", "pct", "2027", "cell", book, BK + "B23"),
        ("DC8", "Cell 1e-7", "0", "usd", "2027", "cell", book, BK + "B24"),
        ("DC7B", "Cell with 7 decimals, shown 1 off", "0.123456", "usd", "2027", "cell", book, BK + "B22"),
        ("TH1", "Cell =1/3, shown 33.3%", "33.3%", "pct", "2027", "cell", book, BK + "B25"),
        ("TH2", "Cell =1/3, shown 33.4%", "33.4%", "pct", "2027", "cell", book, BK + "B25"),
        ("TE20", "Cell 1.23456789012345e-20, shown 0", "0", "usd", "2027", "cell", book, BK + "B26"),
        ("I16", "16-digit int, shown at the cut", "1,234,567,890,123,460", "usd", "2027", "cell", book, BK + "B27"),
        ("I16R", "16-digit int, shown raw", "1,234,567,890,123,456", "usd", "2027", "cell", book, BK + "B27"),
        ("I17", "17-digit int, shown at the cut", "12,345,678,901,234,600", "usd", "2027", "cell", book, BK + "B28"),
        ("I17R", "17-digit int, shown raw", "12,345,678,901,234,567", "usd", "2027", "cell", book, BK + "B28"),
        ("I18", "18-digit int, shown at the cut", "123,456,789,012,346,000", "usd", "2027", "cell", book, BK + "B29"),
        ("I18R", "18-digit int, shown raw", "123,456,789,012,345,678", "usd", "2027", "cell", book, BK + "B29"),
        ("I15", "15-digit int, as it is", "123,456,789,012,345", "usd", "2027", "cell", book, BK + "B30"),
        ("IHU", "int cut half up", "1,234,567,890,123,450", "usd", "2027", "cell", book, BK + "B31"),
        ("IFL", "int cut exactly, not through a float", "123,456,789,012,345,000", "usd", "2027", "cell",
         book, BK + "B32"),
        ("DP1", "Cell 0.000145, shown 0.0145%", "0.0145%", "pct", "2027", "cell", book, BK + "B33"),
        ("DP2", "Cell -0.0, shown 0", "0", "usd", "2027", "cell", book, BK + "B34"),
        ("SD1", "Shown $ with %", "$12.5%", "pct", "2027", "cell", book, BK + "B10"),
        ("SH7", "Shown with 7 decimals", "1,234.4000000", "usd", "2027", "cell", book, BK + "B7"),
        ("V1", "Shown 0.5 against 0.5", "0.5", "usd", "2027", "cell", book, BK + "B16"),
        ("E1", "Excel float 14.499999999999998", "15", "usd", "2027", "cell", book, BK + "E8"),
        ("E2", "Excel float 1234.4999999999998", "1,235", "usd", "2027", "cell", book, BK + "E9"),
        ("E3", "Excel float shown 14", "14", "usd", "2027", "cell", book, BK + "E8"),
        ("H1", "Half: 1,234 against 1234.50", "1,234", "usd", "2027", "cell", book, BK + "B8"),
        ("H2", "Half: 1,235 against 1234.50", "1,235", "usd", "2027", "cell", book, BK + "B8"),
        ("H3", "Negative shown, positive value", "-1,235", "usd", "2027", "cell", book, BK + "B8"),
        ("H4", "Negative half", "(1,235)", "usd", "2027", "cell", book, BK + "B9"),
        ("H5", "Positive shown, negative value", "1,235", "usd", "2027", "cell", book, BK + "B9"),
        ("Z0A", "-0 against +0.30", "-0", "usd", "2027", "cell", book, BK + "B10"),
        ("Z0B", "(0) against -0.30", "(0)", "usd", "2027", "cell", book, BK + "B11"),
        ("Z0C", "0 against -0.30", "0", "usd", "2027", "cell", book, BK + "B11"),
        ("Z0D", "-0.0 against 0", "-0.0", "usd", "2027", "cell", book, BK + "B12"),
        ("Z0E", "0 against +0.30", "0", "usd", "2027", "cell", book, BK + "B10"),
        ("SH1", "Shown 1,00", "1,00", "usd", "2027", "cell", book, BK + "B7"),
        ("SH2", "Shown (-12)", "(-12)", "usd", "2027", "cell", book, BK + "B7"),
        ("SH3", "Shown 0,123", "0,123", "usd", "2027", "cell", book, BK + "B7"),
        ("SH4", "Shown 01,234", "01,234", "usd", "2027", "cell", book, BK + "B7"),
        ("SH5", "Shown padded with no-break spaces", " 1,234 ", "usd", "2027", "cell", book, BK + "B7"),
        ("SH6", "Shown padded with ASCII spaces", "  1,234  ", "usd", "2027", "cell", book, BK + "B7"),
        ("Z0F", "0 against exact 0", "0", "usd", "2027", "cell", book, BK + "B12"),
        ("K1", "1.2M against 1,234,000", "1.2M", "usd", "2027", "cell", book, BK + "C2"),
        ("K2", "1.2M against 1,260,000", "1.2M", "usd", "2027", "cell", book, BK + "C3"),
        ("K3", "1.2k against 1,249", "1.2k", "usd", "2027", "cell", book, BK + "C4"),
        ("K4", "1.3k against 1,250", "1.3k", "usd", "2027", "cell", book, BK + "C5"),
        ("K5", "1.2k against 1,250", "1.2k", "usd", "2027", "cell", book, BK + "C5"),
        ("N1", "Students", "12", "count", "2026", "none", "", ""),
        ("N2", "Cell kind, blank source", "12", "count", "2026", "cell", "", BK + "B7"),
        ("N3", "Blank kind, blank source", "12", "count", "2026", "", "", ""),
        ("N4", "Gl kind, blank source", "3,350", "usd", "2026", "gl", "", G),
        ("M1", "Cell md5 wrong", "1,234", "usd", "2027", "cell", book, BK + "B7", "deadbeef", bsize),
        ("M2", "Cell md5 right (full 32)", "1,234", "usd", "2027", "cell", book, BK + "B7",
         hashlib.md5(open(book, "rb").read()).hexdigest(), bsize),
        ("M3", "Cell md5 and size blank", "1,234", "usd", "2027", "cell", book, BK + "B7", "", ""),
        ("M4", "GL md5 and size blank", "3,350", "usd", "2026", "gl", gl, G, "", ""),
        ("M5", "Cell size wrong", "1,234", "usd", "2027", "cell", book, BK + "B7", bmd5, "12"),
        ("M6", "Cell md5 blank, size right", "1,234", "usd", "2027", "cell", book, BK + "B7", "", bsize),
        ("M7", "GL md5 blank, size right", "3,350", "usd", "2026", "gl", gl, G, "", md5_size(gl)[1]),
        ("M8", "Cell size blank, md5 right", "1,234", "usd", "2027", "cell", book, BK + "B7", bmd5, ""),
        ("X1", "Master past E", "99", "usd", "2027", "cell", book, "Master!F2"),
        ("X2", "Master in B", "10", "usd", "2027", "cell", book, "Master!B2"),
        ("X3", "Master column A", "5", "usd", "2027", "cell", book, "Master!A2"),
        ("F1", "Formula never calculated", "2,469", "usd", "2027", "cell", book, BK + "D1"),
        ("EC1", "Empty cell", "0", "usd", "2027", "cell", book, BK + "Z99"),
        ("EC2", "Empty cell shown 0%", "0%", "pct", "2027", "cell", book, BK + "Z99"),
        # md5 field's shape: 8 or 32 hex only (r7 mutant m53); prefixes of the true md5 otherwise tie
        ("MD1", "md5 1 hex", "1,234", "usd", "2027", "cell", book, BK + "B7", bfull[:1], bsize),
        ("MD2", "md5 7 hex", "1,234", "usd", "2027", "cell", book, BK + "B7", bfull[:7], bsize),
        ("MD3", "md5 9 hex", "1,234", "usd", "2027", "cell", book, BK + "B7", bfull[:9], bsize),
        ("MD4", "md5 31 hex", "1,234", "usd", "2027", "cell", book, BK + "B7", bfull[:31], bsize),
        ("MD5", "md5 33 hex", "1,234", "usd", "2027", "cell", book, BK + "B7", bfull + "0", bsize),
        ("MD6", "md5 8 non-hex", "1,234", "usd", "2027", "cell", book, BK + "B7", "zzzzzzzz", bsize),
        ("MD7", "md5 8 hex upper case", "1,234", "usd", "2027", "cell", book, BK + "B7", bfull[:8].upper(), bsize),
        ("MD8", "gl md5 1 hex", "3,350", "usd", "2026", "gl", gl, G, glfull[:1], md5_size(gl)[1]),
        ("MD9", "md5 8 with a space inside", "1,234", "usd", "2027", "cell", book, BK + "B7",
         bfull[:4] + " " + bfull[4:8], bsize),
        # job 06
        ("J1", "Real-shape GL header", "3,350", "usd", "2026", "gl", gl_real, G),
        ("J2", "Real-shape GL header after a BOM", "3,350", "usd", "2026", "gl", gl_realbom, G),
        ("J3", "Real-shape GL, shown +3,350", "+3,350", "usd", "2026", "gl", gl_real, G),
        ("J4", "Real-shape GL debit side, shown +$3,350", "+$3,350", "usd", "2026", "gl", gl_real,
         G.replace("credit-debit", "debit-credit")),
        ("J5", "GL shown +3,350%", "+3,350%", "usd", "2026", "gl", gl_real, G),
        ("J6", "GL header, tab after Account", "3,350", "usd", "2026", "gl", gl_tabname, G),
        ("J7", "GL header, no-break space after Account", "3,350", "usd", "2026", "gl", gl_nbsp, G),
        ("J8", "GL header, eight names", "3,350", "usd", "2026", "gl", gl_eight, G),
        ("J9", "GL header, two spaces inside a name", "3,350", "usd", "2026", "gl", gl_sp_in, G),
        ("J10", "Cell 0.0778, shown +8%", "+8%", "pct", "2027", "cell", book, BK + "B35"),
        ("J11", "Cell -5, shown +$5", "+$5", "usd", "2027", "cell", book, BK + "B39"),
        ("J12", "Cell 5, shown -5", "-5", "usd", "2027", "cell", book, BK + "B40"),
        ("J13", "Cell -0.0019771529, shown 0%", "0%", "pct", "2027", "cell", book, BK + "B36"),
        ("J14", "Cell -0.4, shown 0", "0", "usd", "2027", "cell", book, BK + "B37"),
        ("J15", "Cell -0.6, shown 0", "0", "usd", "2027", "cell", book, BK + "B38"),
        ("J16", "Cell -0.4, shown -0", "-0", "usd", "2027", "cell", book, BK + "B37"),
        ("J17", "Cell -0.4, shown $0", "$0", "usd", "2027", "cell", book, BK + "B37"),
        ("J18", "Cell 5, shown +5", "+5", "usd", "2027", "cell", book, BK + "B40"),
        ("J19", "Cell 5, shown ++5", "++5", "usd", "2027", "cell", book, BK + "B40"),
        ("J20", "Cell 5, shown 5+", "5+", "usd", "2027", "cell", book, BK + "B40"),
        ("J21", "Cell -0.4, shown 0k", "0k", "usd", "2027", "cell", book, BK + "B37"),
        ("J22", "Cell -0.4, shown 0.0", "0.0", "usd", "2027", "cell", book, BK + "B37"),
        ("J23", "Cell -0.4, shown +0", "+0", "usd", "2027", "cell", book, BK + "B37"),
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
                "E1", "E2", "H2", "H4", "Z0B", "Z0D", "Z0E", "Z0F", "K1", "K3", "K4", "M2", "X2",
                "V1", "SH6", "FL1", "G28", "MD7",
                "P1", "P3", "P6", "P7", "P8", "P10", "P11",
                "FS1", "FS2", "FS3", "FS4", "FS5", "FS6", "FS7", "CF1", "CF2", "CF3",
                "FZ1", "FZ2", "FZ3", "FP1", "FT1", "FA2", "FA3", "FA5",
                "R2", "R4", "R6", "R8", "R9", "R12"):
        is_(rid, "TIED")
    for rid in ("C2", "G2", "E3", "H1", "H3", "H5", "Z0A", "K2", "K5",
                "P2", "P4", "P5", "P13", "CF4", "FT2", "FA1", "FA4",
                "R1", "R3", "R5", "R7", "R10", "R11"):
        is_(rid, "OFF")
    # the % rule both ways, with the recomputed figure written out
    check("P1 stored 0.452 against 45.2%: TIED, recomputed 45.200 (stored x 100, every digit held)",
          st.get("P1") == "TIED" and rows.get("P1", {}).get("recomputed") == "45.200"
          and "stored value x 100" in note.get("P1", "") and "rounds to 45.2%" in note.get("P1", ""))
    check("P5 stored 45.2 against 45.2%: OFF, recomputed 4,520.0",
          st.get("P5") == "OFF" and rows.get("P5", {}).get("recomputed") == "4,520.0")
    check("P8 stored 45.2 against 45.2 (no %): TIED, recomputed 45.2, no x 100",
          st.get("P8") == "TIED" and rows.get("P8", {}).get("recomputed") == "45.2"
          and "x 100" not in note.get("P8", ""))
    check('R1 cell -0.5, format 0%;"neg", shown -0.5%: OFF, recomputed -50.0',
          st.get("R1") == "OFF" and rows.get("R1", {}).get("recomputed") == "-50.0")
    for rid in ("MD1", "MD2", "MD3", "MD4", "MD5", "MD6", "MD8", "MD9"):
        exactly(rid, "ERROR", "md5 column must be 8 or 32 hex characters")
    for rid in ("KS1", "KS2", "KR1", "KO1"):
        exactly(rid, "ERROR", "kind not supported (cell and gl only)")
    for rid in ("N1", "N2", "N3", "N4"):
        exactly(rid, "NO SOURCE", "no source named")
    is_("G22", "ERROR", "a gl row's shown cannot hold %")
    is_("G23", "ERROR", "gl from/to must be YYYY-MM-DD or M/D/YYYY")
    is_("G26", "ERROR", "gl from/to must be YYYY-MM-DD or M/D/YYYY")
    is_("G25", "ERROR", "3 matched lines with unreadable amount, 0 with unreadable date")
    exactly("G27", "ERROR", "account 46999-30 matched no line")
    # the header: 9 names in order, each trimmed of spaces at its ends (job 06), case included,
    # never echoed (exactly: no header text in the note)
    for rid in ("G20", "G21", "G30", "G31", "G32", "G33", "J6", "J7", "J8", "J9"):
        exactly(rid, "ERROR", "GL header not as expected")
    # job 06 point 1: the real header's shape (Store with a trailing space) and the trimmed one tie
    for rid in ("G19", "G29", "J1", "J2"):
        exactly(rid, "TIED", "4 GL lines matched; rounds to 3350")
    check("job06 J1 recomputed 3,350.00", rows.get("J1", {}).get("recomputed") == "3,350.00")
    # job 06 point 2: a leading +
    exactly("J3", "TIED", "4 GL lines matched; rounds to 3350")
    exactly("J4", "OFF", "4 GL lines matched; rounds to -3350; sign differs from shown")
    exactly("J5", "ERROR", "a gl row's shown cannot hold %")
    exactly("J10", "TIED", "stored value x 100; rounds to 8%")
    exactly("J11", "OFF", "rounds to -5; sign differs from shown")
    exactly("J12", "OFF", "rounds to 5; sign differs from shown")
    exactly("J18", "TIED", "rounds to 5")
    for rid in ("J19", "J20"):
        exactly(rid, "ERROR", "shown not readable")
    exactly("J23", "OFF", "rounds to 0; sign differs from shown")
    # job 06 point 3: a shown zero ties either sign; no note prints -0
    exactly("Z0C", "TIED", "rounds to 0")
    exactly("J13", "TIED", "stored value x 100; rounds to 0%")
    exactly("J14", "TIED", "rounds to 0")
    exactly("J15", "OFF", "rounds to -1")
    exactly("J16", "TIED", "rounds to 0")
    exactly("J17", "TIED", "rounds to 0")
    exactly("J21", "TIED", "rounds to 0k")
    exactly("J22", "OFF", "rounds to -0.4")
    minus_zero = [k for k, n in note.items() if re.search(r"-0(\.0+)?(?![0-9.])", n)]
    check("job06 no note prints -0", not minus_zero and bool(note))
    check("job06 stdout prints no -0 in a note", not re.search(r"rounds to -0(\.0+)?(?![0-9.])", so))
    # the 18-digit cap and the 60-digit context
    for rid in ("CAP1", "CAP8", "G34", "G38", "NG6", "BRK", "MIN", "BIG", "BIG3", "DC6", "DC6P"):
        is_(rid, "TIED")
    for rid in ("CAP2", "G39", "BIG2", "BIG4"):
        is_(rid, "OFF")
    check("G38 recomputed keeps all 24 digits in its note",
          "rounds to 123456789012349028.123456" in note.get("G38", ""))
    check("BIG recomputed the 29-digit sum exactly",
          rows.get("BIG", {}).get("recomputed") == "11,000,000,000,000,000,003,349.989000"
          and rows.get("BIG", {}).get("difference") == "-0.011000"
          and "11000 GL lines" not in note.get("BIG", "") and "11004 GL lines matched" in note.get("BIG", ""))
    for rid in ("CAP3", "CAP4", "CAP5", "CAP6", "BL1"):
        exactly(rid, "ERROR", "cell value has more than 18 digits before the point")
    # cells have no decimal cap: the value decides TIED or OFF
    for rid in ("DC7", "DC8", "TH1", "TE20"):
        is_(rid, "TIED")
    for rid in ("DC7B", "TH2"):
        is_(rid, "OFF")
    # ints cut to 15 significant digits (F1); the test book must hand them over as ints
    def int_cells():
        from openpyxl import load_workbook
        wbk = load_workbook(book, read_only=True, data_only=True)
        try:
            vals = [wbk["Budget 2027"][c].value for c in ("B27", "B28", "B29", "B30", "B31", "B32")]
        finally:
            wbk.close()
        return vals == [1234567890123456, 12345678901234567, 123456789012345678, 123456789012345,
                        1234567890123445, 123456789012345499] and all(type(v) is int for v in vals)
    check("the int cells are read back as exact ints (16, 17 and 18 digits)", reads(int_cells))
    for rid in ("I16", "I17", "I18", "I15", "IHU", "IFL"):
        is_(rid, "TIED")
    for rid in ("I16R", "I17R", "I18R"):
        is_(rid, "OFF")
    check("I16 recomputed 1,234,567,890,123,460 (the cut), I15 recomputed as it is",
          rows.get("I16", {}).get("recomputed") == "1,234,567,890,123,460"
          and rows.get("I15", {}).get("recomputed") == "123,456,789,012,345")
    # the columns print every digit, never rounded; -0 as 0 (M1)
    is_("DP1", "TIED")
    check("DP1 recomputed is 0.0145 to every digit (never 0.01)",
          reads(lambda: D(rows["DP1"]["recomputed"]) == D("0.0145")))
    check("DC7 difference printed in full (-0.0000003), never 0.00",
          rows.get("DC7", {}).get("difference") == "-0.0000003")
    check("DP2 (cell -0.0): recomputed and difference print 0, not -0",
          st.get("DP2") == "TIED" and rows.get("DP2", {}).get("recomputed") == "0"
          and rows.get("DP2", {}).get("difference") == "0")
    zero_shown = [(r["id"], c) for r in rows.values() for c in ("recomputed", "difference")
                  if re.fullmatch(r"-0(\.0*)?", r.get(c, "") or "")]
    check("no recomputed or difference prints as -0", not zero_shown)
    nonzero_as_zero = [r["id"] for r in rows.values() if r.get("difference")
                       and re.fullmatch(r"-?0(\.0*)?", r["difference"])
                       and r.get("recomputed") and r["status"] == "OFF"
                       and D(r["recomputed"].replace(",", "")) != D(0)]
    check("no OFF row shows a difference of 0", not nonzero_as_zero)
    exactly("SD1", "ERROR", "shown has both $ and %")
    check("TH1 recomputed from 0.333333333333333 x 100 (no cap, no rounding before the shown decimals)",
          rows.get("TH1", {}).get("recomputed", "").startswith("33.3"))
    for rid in ("CAP7", "G36", "G37"):
        exactly(rid, "ERROR", "shown has more than 18 digits before the point")
    exactly("SH7", "ERROR", "shown has more than 6 digits after the point")
    for rid in ("G35", "G41", "G40", "N1A", "NG7"):
        exactly(rid, "ERROR", "1 matched lines with unreadable amount, 0 with unreadable date")
    exactly("BD1", "ERROR", "cell holds a date")
    exactly("BB1", "ERROR", "cell holds a boolean")
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
    is_("G15", "ERROR", "1 matched lines with unreadable amount")
    is_("G16", "ERROR", "1 with unreadable date")
    is_("G17", "ERROR", "1 with unreadable date")
    is_("G20", "ERROR", "GL header not as expected")
    is_("G21", "ERROR", "GL header not as expected")
    exactly("P12", "ERROR", "cell holds text, not a number")
    exactly("P14", "ERROR", "cell holds text, not a number")
    check("no row's note speaks of a format or a scale",
          not any(w in n for n in note.values() for w in ("format", "scale")))
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
    for rid in ("EC1", "EC2"):
        is_(rid, "ERROR", "no cached value")
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
    hdr_echo = any(s in text.lower() for s in ("debit amount", "credit amount", "journal ,", "doc #")
                   for text in (so, se, out_text))
    check("no GL header text (any case) in stdout, stderr or out CSV", not hdr_echo)

    # --- with the 6-decimal cap lifted, the trapping context alone must refuse any rounding
    lifted = os.path.join(tmp, "figures_cap_lifted.csv")
    write_figures(lifted, [
        ("L1", "N1 debit, subtracted", "3,349", "usd", "2026", "gl", gl_n1, G),
        ("L2", "N1 debit, debit-credit side", "-3,349", "usd", "2026", "gl", gl_n1,
         G.replace("credit-debit", "debit-credit")),
        ("L3", "70-decimal credit, summed", "3,350", "usd", "2026", "gl", gl_70, G),
        ("L4", "61-digit debit, credit-debit side", "-123,456,789,012,342,328", "usd", "2026", "gl", gl_n1b, G),
        ("L5", "61-digit debit, debit-credit side", "123,456,789,012,342,328", "usd", "2026", "gl", gl_n1c,
         G.replace("credit-debit", "debit-credit")),
        ("L6", "60-decimal credit: exact alone, the sum needs rounding", "3,350", "usd", "2026", "gl", gl_60, G),
    ])
    saved_cap = mod.MAX_DEC_DIGITS
    mod.MAX_DEC_DIGITS = 200
    try:
        lres, _ = mod.run(mod.load_figures(lifted))
    except Exception as e:
        lres = [{"id": "crash", "status": type(e).__name__, "note": ""}]
    finally:
        mod.MAX_DEC_DIGITS = saved_cap
    lst = {r["id"]: (r["status"], r["note"]) for r in lres}
    for rid in ("L1", "L2", "L3", "L4", "L5", "L6"):
        check(f"cap lifted: {rid} is exactly ERROR / 'GL sum too long to add without rounding'",
              lst.get(rid) == ("ERROR", "GL sum too long to add without rounding"))
    saved_h = mod.HUNDRED
    mod.HUNDRED = D("1." + "0" * 70 + "1")
    try:
        with __import__("decimal").localcontext(mod.WIDE):
            mod.recompute_cell({"detail": BK + "E5", "source": book, "md5": bmd5, "size": bsize}, True)
        x100_refused = False
    except mod.RowError as e:
        x100_refused = str(e) == "cell value x 100 needs rounding"
    except Exception:
        x100_refused = False
    finally:
        mod.HUNDRED = saved_h
    check("x 100 that would need rounding is refused (multiplier made 72 digits)", x100_refused)

    # --- self-check: it can pass, and it fails on a planted wrong figure
    clean = os.path.join(tmp, "figures_clean.csv")
    planted = os.path.join(tmp, "figures_planted.csv")
    base = [
        ("C1", "Budget cell", "1,234", "usd", "2027", "cell", book, BK + "B7"),
        ("G1", "Training GL", "3,350", "usd", "2026", "gl", gl, G),
        ("P1", "Pct cell", "45.2%", "pct", "2027", "cell", book, BK + "E5"),
    ]
    write_figures(clean, base)
    code, so, _ = run_tie(clean)
    check("self-check clean file: RESULT: PASS, exit 0", code == 0 and last_line(so) == "RESULT: PASS")
    write_figures(planted, [("C1", "Budget cell", "1,334") + base[0][3:]] + base[1:])
    code, so, _ = run_tie(planted)
    check("self-check planted wrong figure: RESULT: FAIL, exit 1",
          code == 1 and last_line(so) == "RESULT: FAIL (1 of 3 rows not TIED)")

    # --- job 06 point 5: every field read from a raw file and from figures.csv is trimmed of
    # spaces and tabs at both ends; blank after the trim is blank; the files are never changed
    tr = getattr(mod, "trim", None)
    check("job06 p5 trim() trims spaces and tabs at both ends only (a no-break space stays)",
          tr is not None and tr(" \t 46100-30\t ") == "46100-30" and tr("\t \t") == ""
          and tr(None) == "" and tr(" 1,234 ") == " 1,234 " and tr("a \t b") == "a \t b")
    PADS = (" ", "\t", " \t", "\t ", "  \t  ")
    gl_pad = os.path.join(tmp, "made_up_gl_padded_fields.csv")
    with open(gl_pad, "w", encoding="utf-8", newline="") as f:
        f.write(REAL_HEADER + "\r\n")
        w = csv.writer(f, lineterminator="\r\n")
        for i, (a, j, d, dr, cr, s) in enumerate(gl_rows()):
            p, q = PADS[i % len(PADS)], PADS[(i + 2) % len(PADS)]
            w.writerow([p + a + q, q + j + p, p + d + q, f"{SECRET_DOC}-{i}", SECRET_DESC,
                        p + dr + q, q + cr + p, "1,234.00", p + s + q])
    with open(gl_pad, "rb") as f:
        pad_bytes = f.read()
    check("job06 p5 made-up padded GL is real: real header, CRLF, tabs and spaces around every used field",
          pad_bytes.startswith(REAL_HEADER.encode("ascii") + b"\r\n") and b"\t" in pad_bytes
          and b'\t46100-30' in pad_bytes and b'POW\t' in pad_bytes and b' SJ\t' in pad_bytes
          and b'\t2/3/2026' in pad_bytes and b'$2,500.00\t' in pad_bytes
          and pad_bytes.count(b"\r\n") == len(gl_rows()) + 1)
    gl_blank = os.path.join(tmp, "made_up_gl_amounts_of_only_spaces_and_tabs.csv")
    write_gl(gl_blank, header_line=REAL_HEADER,
             extra=[("46100-30", "SJ", "5/5/2026", "\t \t", "   ", "POW")])   # a matched line, both amounts blank
    pmd5, psize = hashlib.md5(pad_bytes).hexdigest(), str(len(pad_bytes))
    GP = (" accounts = 46xxx-30 ;\tstore=\tPOW ; from= 2026-01-01\t;to =2026-09-30 ;"
          " side= credit-debit\t;\tjournal = SJ , GJ \t")
    pad_fig = os.path.join(tmp, "figures_padded_fields.csv")
    write_figures(pad_fig, [
        (" T1\t", "\tPadded cell row ", "\t1,234 ", " usd\t", "\t2027 ", " cell\t", " " + book + "\t",
         " \t'Budget 2027' ! \tB7 \t", "\t" + bfull + "  ", " " + bsize + "\t"),
        ("\tT2 ", " Padded gl row\t", " $3,350\t", "\tusd", "2026 ", "\tgl ", "\t" + gl_pad + " ",
         GP, " " + pmd5[:8] + "\t", "\t" + psize + " "),
        ("T3", "Padded GL, blank amounts of only tabs and spaces", "3,350", "usd", "2026", "gl", gl_blank, G),
        ("T4", "Source of only spaces", "1,234", "usd", "2027", "cell", "   ", BK + "B7"),
        ("T5", "Kind of only a tab", "1,234", "usd", "2027", "\t", book, BK + "B7", bmd5, bsize),
        ("T6", "md5 of only spaces and a tab", "1,234", "usd", "2027", "cell", book, BK + "B7", " \t ", bsize),
        ("T7", "Padded text cell stays ERROR", "45", "usd", "2027", "cell", book, BK + "B41"),
    ])
    pad_fig_md5 = md5_size(pad_fig)
    pad_out = os.path.join(tmp, "result_padded_fields.csv")
    code, so, se = run_tie(pad_fig, pad_out)
    prow, _ = read_out(pad_out)
    pst = {k: (v["status"], v["note"]) for k, v in prow.items()}
    check("job06 p5 T1 padded cell row (shown, kind, source, Sheet!A1, md5, size) is exactly TIED / 'rounds to 1234'",
          pst.get("T1") == ("TIED", "rounds to 1234"))
    check("job06 p5 T2 padded gl row (shown, md5, size, every detail part) on the padded GL is exactly TIED",
          pst.get("T2") == ("TIED", "4 GL lines matched; rounds to 3350"))
    check("job06 p5 T3 GL amounts of only tabs and spaces count as blank (0): exactly TIED, 5 lines",
          pst.get("T3") == ("TIED", "5 GL lines matched; rounds to 3350"))
    check("job06 p5 T4 a source of only spaces is exactly NO SOURCE", pst.get("T4") == ("NO SOURCE", "no source named"))
    check("job06 p5 T5 a kind of only a tab is exactly NO SOURCE", pst.get("T5") == ("NO SOURCE", "no source named"))
    check("job06 p5 T6 an md5 of only spaces and a tab is blank: exactly ERROR / 'md5/size not given'",
          pst.get("T6") == ("ERROR", "md5/size not given"))
    check("job06 p5 T7 a text cell padded with spaces and a tab stays exactly ERROR (text)",
          pst.get("T7") == ("ERROR", "cell holds text, not a number"))
    with open(gl_pad, "rb") as f:
        same_gl = f.read() == pad_bytes
    check("job06 p5 the raw files are never changed (padded GL and figures byte for byte the same after the run)",
          same_gl and md5_size(pad_fig) == pad_fig_md5)
    leak5 = any(s in text for s in (SECRET_DESC, SECRET_DOC) for text in (so, se))
    check("job06 p5 no GL Description or Doc # printed from the padded GL", not leak5)
    pad_clean = os.path.join(tmp, "figures_padded_clean.csv")
    with open(pad_fig, encoding="utf-8", newline="") as f:
        prow_all = list(csv.reader(f))
    write_figures(pad_clean, prow_all[1:4], header=prow_all[0])
    code, so, _ = run_tie(pad_clean)
    check("job06 p5 padded figures (T1-T3) alone: RESULT: PASS, exit 0", code == 0 and last_line(so) == "RESULT: PASS")

    # --- job 06 check r2, findings 1 and 2: a stray quote or other whitespace in a used GL field or a
    # figures.csv field is ERROR, naming the column and never the content
    R3G = "accounts=46000-30;store=POW;from=2026-01-01;to=2026-01-31;side=credit-debit"
    R3_MARK = "ZQX9"
    R3_COLS = {0: "Account", 1: "Journal", 2: "Date", 5: "Debit Amount", 6: "Credit Amount", 8: "Store"}
    R3_VALS = {0: "46000-30", 1: "GJ", 2: "1/5/2026", 5: "1.00", 6: "50.00", 8: "POW"}
    R3_WS = (("NBSP", " "), ("VT", "\x0b"), ("FF", "\x0c"), ("US", "\x1f"), ("EM SPACE", " "))
    r3_n = [0]

    def r3_gl(second):
        """A made-up GL: POW 100, then one raw line given as its 9 fields, already spelled."""
        r3_n[0] += 1
        path = os.path.join(tmp, f"made_up_gl_r3_{r3_n[0]}.csv")
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(REAL_HEADER + "\r\n")
            f.write("46000-30,GJ,1/5/2026,D1,note,,100.00,0,POW\r\n")
            f.write(",".join(second) + "\r\n")
        return path

    def r3_line(col=None, spelled=""):
        fields = ["46000-30", "GJ", "1/5/2026", "D2", "note", "", "50.00", "0", "POW"]
        if col is not None:
            fields[col] = spelled
        return fields

    r3_cases = []     # (id, gl, shown, detail, column the note must name)
    for col, val in R3_VALS.items():
        det = R3G + (";journal=GJ" if col == 1 else "")
        shown_ = "100" if col in (0, 1, 8) else "150"
        for nm, sp in (("space", " "), ("tab", "\t")):
            r3_cases.append((f"Q{col}{nm}", r3_gl(r3_line(col, f'{sp}"{val}"')), shown_, det, R3_COLS[col]))
        r3_cases.append((f"Q{col}inner", r3_gl(r3_line(col, val[:1] + '"' + val[1:])), shown_, det, R3_COLS[col]))
        for nm, ch in R3_WS:
            key = nm.replace(" ", "")
            r3_cases.append((f"W{col}{key}end", r3_gl(r3_line(col, val + ch)), shown_, det, R3_COLS[col]))
            r3_cases.append((f"W{col}{key}start", r3_gl(r3_line(col, ch + val)), shown_, det, R3_COLS[col]))
            r3_cases.append((f"W{col}{key}pad", r3_gl(r3_line(col, " " + val + ch + "\t")), shown_, det, R3_COLS[col]))
    r3_cases.append(("Qescaped", r3_gl(r3_line(8, '"PO""W"')), "100", R3G, "Store"))
    r3_cases.append(("Qother", r3_gl(r3_line(8, f' "{R3_MARK}"')), "100", R3G, "Store"))
    r3_fig = os.path.join(tmp, "figures_r3_gl.csv")
    r3_out = os.path.join(tmp, "result_r3_gl.csv")
    write_figures(r3_fig, [(i, "r3", s_, "usd", "Jan 2026", "gl", g, d) for i, g, s_, d, _ in r3_cases])
    code, so, se = run_tie(r3_fig, out=r3_out)
    r3_main, _ = read_out(r3_out)
    for i, _, _, _, col in r3_cases:
        row_ = r3_main.get(i, {})
        check(f"job06 r3 {i}: ERROR, blank recomputed, note names column {col}",
              row_.get("status") == "ERROR" and row_.get("recomputed") == "" and f"column {col}" in row_.get("note", ""))
    check("job06 r3 the ERROR notes and output never print the field's content",
          code == 1 and bool(r3_main) and R3_MARK not in so and R3_MARK not in se
          and not any(R3_MARK in v for r_ in r3_main.values() for v in r_.values())
          and "column Store" in r3_main.get("Qother", {}).get("note", ""))

    # --- job 06 check r3, F1: a byte that is not valid UTF-8 in a used GL field is ERROR, at any place
    def r4_gl(col, spelled):
        """A made-up GL in bytes: POW 100, then one line whose field col is the bytes given."""
        r3_n[0] += 1
        path = os.path.join(tmp, f"made_up_gl_r4_{r3_n[0]}.csv")
        fields = [x.encode("ascii") for x in r3_line()]
        fields[col] = spelled
        with open(path, "wb") as f:
            f.write(REAL_HEADER.encode("ascii") + b"\r\n")
            f.write(b"46000-30,GJ,1/5/2026,D1,note,,100.00,0,POW\r\n")
            f.write(b",".join(fields) + b"\r\n")
        return path

    r4_cases = []
    for col, val in R3_VALS.items():
        det = R3G + (";journal=GJ" if col == 1 else "")
        shown_ = "100" if col in (0, 1, 8) else "150"
        v = val.encode("ascii")
        for nm, b in (("A0", b"\xa0"), ("85", b"\x85"), ("FF", b"\xff"), ("FFFD", "�".encode("utf-8"))):
            for place, sp in (("end", v + b), ("start", b + v), ("inner", v[:1] + b + v[1:])):
                r4_cases.append((f"B{col}{nm}{place}", r4_gl(col, sp), shown_, det, R3_COLS[col]))
    r4_fig = os.path.join(tmp, "figures_r4_gl.csv")
    r4_out = os.path.join(tmp, "result_r4_gl.csv")
    write_figures(r4_fig, [(i, "r4", s_, "usd", "Jan 2026", "gl", g, d) for i, g, s_, d, _ in r4_cases])
    code, so, se = run_tie(r4_fig, out=r4_out)
    r4_main, _ = read_out(r4_out)
    for i, _, _, _, col in r4_cases:
        row_ = r4_main.get(i, {})
        check(f"job06 r4 {i}: ERROR, blank recomputed, note names column {col}",
              row_.get("status") == "ERROR" and row_.get("recomputed") == ""
              and "not printable ASCII" in row_.get("note", "") and f"column {col}" in row_.get("note", ""))
    check("job06 r4 bad-byte file: exit 1", code == 1 and bool(r4_main))

    # --- job 06 shape 1 (Piston's pick), r4 F1: anything but printable ASCII in a used GL field is ERROR
    S1_CHARS = ("​", "﻿", "­", "⁠", "‌", "‍", "\x00", "\x01", "\x7f",
                " ", " ", "\x0b", "　", "\t", "é")
    s1_cases = []
    for col, val in R3_VALS.items():
        det = R3G + (";journal=GJ" if col == 1 else "")
        shown_ = "100" if col in (0, 1, 8) else "150"
        v = val.encode("ascii")
        for n_, ch in enumerate(S1_CHARS):
            b = ch.encode("utf-8")
            for place, sp in (("end", v + b), ("start", b + v), ("inner", v[:1] + b + v[1:])):
                if ch == "\t" and place != "inner":
                    continue  # a tab at an end is trimmed, by point 5
                s1_cases.append((f"S{col}c{n_}{place}", r4_gl(col, sp), shown_, det, R3_COLS[col]))
    s1_fig = os.path.join(tmp, "figures_s1_gl.csv")
    s1_out = os.path.join(tmp, "result_s1_gl.csv")
    write_figures(s1_fig, [(i, "s1", s_, "usd", "Jan 2026", "gl", g, d) for i, g, s_, d, _ in s1_cases])
    code, so, se = run_tie(s1_fig, out=s1_out)
    s1_main, _ = read_out(s1_out)
    for i, _, _, _, col in s1_cases:
        row_ = s1_main.get(i, {})
        check(f"job06 shape1 {i}: ERROR, blank recomputed, note names column {col}",
              row_.get("status") == "ERROR" and row_.get("recomputed") == ""
              and f"column {col}" in row_.get("note", ""))

    # guard: every printable ASCII character but the quote, inside an unused field, and inner spaces in a used one
    s1_guard = os.path.join(tmp, "made_up_gl_s1_guard.csv")
    with open(s1_guard, "wb") as f:
        f.write(REAL_HEADER.encode("ascii") + b"\r\n")
        f.write(b"46000-30,GJ,1/5/2026,D1,note,,100.00,0,POW\r\n")
        f.write(b"46000-30,G J,1/5/2026,D2,no~te!,,50.00,0,POW\r\n")
    s1g_fig = os.path.join(tmp, "figures_s1_guard.csv")
    s1g_out = os.path.join(tmp, "result_s1_guard.csv")
    write_figures(s1g_fig, [("Sg", "s1", "150", "usd", "Jan 2026", "gl", s1_guard, R3G)])
    code, so, se = run_tie(s1g_fig, out=s1g_out)
    s1g_main, _ = read_out(s1g_out)
    check("job06 shape1 guard: plain ASCII with an inner space still ties", s1g_main.get("Sg", {}).get("status") == "TIED")

    # --- job 06 shape 1, r4 M1: a quote closed early is refused, by the strict csv reader
    m1_cases = [("M1store", 8, b'"10"E', "100"), ("M1acct", 0, b'"46"000-30', "100"), ("M1cr", 6, b'"5"0.00', "150"),
                ("M1date", 2, b'"1/5"/2026', "150"), ("M1desc", 4, b'"no"te', "150"), ("M1open", 8, b'"POW', "100"),
                ("M1space", 8, b'"POW" ', "150")]
    m1_rows = [(i, "m1", s_, "usd", "Jan 2026", "gl", r4_gl(col, sp), R3G) for i, col, sp, s_ in m1_cases]
    m1_fig = os.path.join(tmp, "figures_m1.csv")
    m1_out = os.path.join(tmp, "result_m1.csv")
    write_figures(m1_fig, m1_rows)
    code, so, se = run_tie(m1_fig, out=m1_out)
    m1_main, _ = read_out(m1_out)
    for i, _, _, _ in m1_cases:
        check(f"job06 shape1 {i}: a quote closed early or left open is ERROR",
              m1_main.get(i, {}).get("status") == "ERROR" and m1_main.get(i, {}).get("recomputed") == "")

    # --- job 06 shape 1, r4 F2: a cell reference is matched before any change of case
    f2_refs = ["ſ7", "ı7", "ß7", "ﬁ7", "ﬀ7", "ﬂ7", "ﬃ7", "ﬄ7", "ﬅ7", "ﬆ7",
               "Bſ7", "K7"]
    f2_rows = [(f"F2c{n_}", "f2", "1,234", "usd", "2027", "cell", book, BK + ref) for n_, ref in enumerate(f2_refs)]
    f2_rows += [("F2lower", "f2", "1,234", "usd", "2027", "cell", book, BK + "b7"),
                ("F2dollar", "f2", "1,234", "usd", "2027", "cell", book, BK + "$B$7")]
    f2_fig = os.path.join(tmp, "figures_f2.csv")
    f2_out = os.path.join(tmp, "result_f2.csv")
    write_figures(f2_fig, f2_rows)
    code, so, se = run_tie(f2_fig, out=f2_out)
    f2_main, _ = read_out(f2_out)
    for n_ in range(len(f2_refs)):
        row_ = f2_main.get(f"F2c{n_}", {})
        check(f"job06 shape1 F2c{n_}: a letter that upper-cases to ASCII is ERROR",
              row_.get("status") == "ERROR" and "cell detail must be" in row_.get("note", ""))
    check("job06 shape1 F2 guard: lower-case b7 still reads B7", f2_main.get("F2lower", {}).get("status") == "TIED")
    check("job06 shape1 F2 guard: $B$7 still reads B7", f2_main.get("F2dollar", {}).get("status") == "TIED")

    # --- job 06 shape 1 round 2, r5 F1: the reference is matched as written, $ included
    d_bad = ["B7$5", "B$C7", "$$B7", "B7$", "B$$7", "$B$7$5", "B$7$5", "$B$$7", "$$B$7", "$", "B$", "$7"]
    d_good = ["B7", "$B$7", "$B7", "B$7"]
    d_rows = [(f"Dbad{n_}", "d", "1,234", "usd", "2027", "cell", book, BK + r_) for n_, r_ in enumerate(d_bad)]
    d_rows += [(f"Dgood{n_}", "d", "1,234", "usd", "2027", "cell", book, BK + r_) for n_, r_ in enumerate(d_good)]
    d_fig = os.path.join(tmp, "figures_dollar.csv")
    d_out = os.path.join(tmp, "result_dollar.csv")
    write_figures(d_fig, d_rows)
    code, so, se = run_tie(d_fig, out=d_out)
    d_main, _ = read_out(d_out)
    for n_, r_ in enumerate(d_bad):
        row_ = d_main.get(f"Dbad{n_}", {})
        check(f"job06 round2 {r_}: not a reference, ERROR",
              row_.get("status") == "ERROR" and "cell detail must be" in row_.get("note", ""))
    for n_, r_ in enumerate(d_good):
        check(f"job06 round2 legal spelling {r_}: TIED", d_main.get(f"Dgood{n_}", {}).get("status") == "TIED")

    # --- job 06 shape 1 round 2, r5 M1: a space inside an account or store that hides a target is ERROR
    R5W = "accounts=46xxx-30;store=POW;from=2026-01-01;to=2026-01-31;side=credit-debit"
    sp_bad = [("Xacc", 0, b"460 00-30", R3G), ("Xacc2", 0, b"4 6 0 0 0 - 3 0", R3G), ("Xst", 8, b"P OW", R3G),
              ("Xwild", 0, b"461 00-30", R5W), ("Xstw", 8, b"PO W", R5W)]
    sp_rows = [(i, "x", "100", "usd", "Jan 2026", "gl", r4_gl(col, b_), d) for i, col, b_, d in sp_bad]
    sp_good = [("Yacc", 0, b"471 00-30"), ("Yst", 8, b"L DS"), ("Ydesc", 4, b"no te")]
    sp_rows += [(i, "x", "100" if col != 4 else "150", "usd", "Jan 2026", "gl", r4_gl(col, b_), R3G)
                for i, col, b_ in sp_good]
    sp_fig = os.path.join(tmp, "figures_spaced.csv")
    sp_out = os.path.join(tmp, "result_spaced.csv")
    write_figures(sp_fig, sp_rows)
    code, so, se = run_tie(sp_fig, out=sp_out)
    sp_main, _ = read_out(sp_out)
    for i, _, _, _ in sp_bad:
        row_ = sp_main.get(i, {})
        check(f"job06 round2 {i}: a space hiding a target is ERROR, blank recomputed",
              row_.get("status") == "ERROR" and row_.get("recomputed") == ""
              and "inner spaces" in row_.get("note", ""))
    for i, _, _ in sp_good:
        check(f"job06 round2 guard {i}: a space hiding no target changes nothing, TIED",
              sp_main.get(i, {}).get("status") == "TIED")

    # guards: the same bytes in an unused field, and good UTF-8 there, still tie at 150
    r4_guards = [("Hdesc", r4_gl(4, b"no\xa0te\x85")), ("Hdoc", r4_gl(3, b"\xffD2")),
                 ("Hbal", r4_gl(7, b"0\xa0")), ("Hutf8", r4_gl(4, "café".encode("utf-8")))]
    r4g_fig = os.path.join(tmp, "figures_r4_guard.csv")
    r4g_out = os.path.join(tmp, "result_r4_guard.csv")
    write_figures(r4g_fig, [(i, "r4", "150", "usd", "Jan 2026", "gl", g, R3G) for i, g in r4_guards])
    code, so, se = run_tie(r4g_fig, out=r4g_out)
    r4g_main, _ = read_out(r4g_out)
    for i, _ in r4_guards:
        check(f"job06 r4 guard {i}: an unused field's byte changes nothing, TIED",
              r4g_main.get(i, {}).get("status") == "TIED")

    # guards: properly quoted fields and whitespace in the unused fields still tie
    r3_guards = [
        ("Gquoted", r3_gl(['"46000-30"', '"GJ"', '"1/5/2026"', '"D2"', '"note, with comma"', '""', '"50.00"', '"0"', '"POW"'])),
        ("Gquotedpad", r3_gl(['" 46000-30 "', '"GJ\t"', '" 1/5/2026"', "D2", "note", '" "', '" 50.00 "', "0", '"POW"'])),
        ("Gdesc", r3_gl(["46000-30", "GJ", "1/5/2026", "D2", " note ", "", "50.00", "0", "POW"])),
        ("Gdoc", r3_gl(["46000-30", "GJ", "1/5/2026", "\x0cD2\x1f", "note", "", "50.00", "0", "POW"])),
        ("Gbal", r3_gl(["46000-30", "GJ", "1/5/2026", "D2", "note", "", "50.00", " 0\x0b", "POW"])),
        ("Gdescq", r3_gl(["46000-30", "GJ", "1/5/2026", 'D"2', ' "note"', "", "50.00", '0"', "POW"])),
    ]
    r3_gfig = os.path.join(tmp, "figures_r3_guards.csv")
    r3_gout = os.path.join(tmp, "result_r3_guards.csv")
    write_figures(r3_gfig, [(i, "r3", "150", "usd", "Jan 2026", "gl", g, R3G) for i, g in r3_guards])
    code, so, _ = run_tie(r3_gfig, out=r3_gout)
    r3_gmain, _ = read_out(r3_gout)
    for i, _ in r3_guards:
        row_ = r3_gmain.get(i, {})
        check(f"job06 r3 guard {i}: exactly TIED at 150.00, 2 lines",
              row_.get("status") == "TIED" and row_.get("recomputed") == "150.00"
              and row_.get("note", "").startswith("2 GL lines matched"))
    check("job06 r3 guards: RESULT: PASS, exit 0", code == 0 and last_line(so) == "RESULT: PASS")

    # figures.csv: any field, either end
    r3_good = r3_gl(r3_line())
    r3_gmd5, r3_gsize = md5_size(r3_good)
    r3_base = ["", "r3", "150", "usd", "Jan 2026", "gl", r3_good, R3G, r3_gmd5, r3_gsize]
    r3_frows, r3_fwant = [["OK1"] + r3_base[1:]], {}
    for ci, cname in enumerate(FIG_HEADER):
        for nm, ch in R3_WS:
            for where in ("end", "start"):
                rid = f"F{ci}{nm.replace(' ', '')}{where}"
                row_ = [rid] + r3_base[1:]
                row_[ci] = row_[ci] + ch if where == "end" else ch + row_[ci]
                r3_frows.append(row_)
                r3_fwant[row_[0]] = cname
    r3_frows.append([" "] * 10)
    r3_ffig = os.path.join(tmp, "figures_r3_fields.csv")
    r3_fout = os.path.join(tmp, "result_r3_fields.csv")
    write_figures(r3_ffig, r3_frows)
    code, _, _ = run_tie(r3_ffig, out=r3_fout)
    r3_fmain, _ = read_out(r3_fout)
    for rid, cname in r3_fwant.items():
        row_ = r3_fmain.get(rid, {})
        want_note = "shown not readable" if cname == "shown" else "figures column " + cname
        check(f"job06 r3 figures {rid!r}: ERROR, note names column {cname}",
              row_.get("status") == "ERROR" and want_note in row_.get("note", ""))
    check("job06 r3 figures: a row of only NBSP is ERROR, never dropped",
          r3_fmain.get(" ", {}).get("status") == "ERROR")
    check("job06 r3 figures guard: the clean row beside them is still TIED", r3_fmain.get("OK1", {}).get("status") == "TIED")
    r3_hfig = os.path.join(tmp, "figures_r3_header.csv")
    write_figures(r3_hfig, [["H1"] + r3_base[1:]], header=["id "] + FIG_HEADER[1:])
    code, so, se = run_tie(r3_hfig)
    check("job06 r3 figures header name ending in NBSP: exit 2, nothing run",
          code == 2 and so == "" and "figures header has whitespace" in se)

    # --- job 06, after r3: inside the detail field, gl keys, values and list items and the sheet and
    # cell parts trim spaces and tabs only; other whitespace at an end is ERROR naming the part
    R4P = (("journal", "GJ"), ("accounts", "46000-30"), ("store", "POW"), ("from", "2026-01-01"),
           ("to", "2026-01-31"), ("side", "credit-debit"))

    def r4_det(pos=None, form=None, ch=""):
        parts = []
        for i, (k, v) in enumerate(R4P):
            if i == pos:
                k, v = {"vend": (k, v + ch), "vstart": (k, ch + v), "kend": (k + ch, v),
                        "kstart": (ch + k, v)}[form]
            parts.append(k + "=" + v)
        return ";".join(parts)

    r4_rows, r4_want = [], {}
    for pos, (key, _) in enumerate(R4P):
        for nm, ch in R3_WS:
            for form in ("vend", "vstart", "kend", "kstart"):
                rid = f"D{key}{nm.replace(' ', '')}{form}"
                r4_rows.append((rid, "r4", "150", "usd", "Jan 2026", "gl", r3_good, r4_det(pos, form, ch)))
                r4_want[rid] = f"gl detail {key} value" if form[0] == "v" else f"gl detail part {pos + 1}"
                if (pos, form) in ((0, "kstart"), (len(R4P) - 1, "vend")):  # the end of the whole field
                    r4_want[rid] = "figures column detail"
    for nm, ch in R3_WS:
        key_ = nm.replace(" ", "")
        for rid, det, want in ((f"Iacc{key_}", r4_det().replace("accounts=46000-30", f"accounts=46000-30{ch},46000-30"),
                                "gl detail accounts value"),
                               (f"Ijnl{key_}", r4_det().replace("journal=GJ", f"journal=GJ{ch},SJ"),
                                "gl detail journal value"),
                               (f"Ionly{key_}", r4_det().replace(";store=", f";{ch};store="), "gl detail part 3")):
            r4_rows.append((rid, "r4", "150", "usd", "Jan 2026", "gl", r3_good, det))
            r4_want[rid] = want
    r4_book = os.path.join(tmp, "made_up_r4_sheets.xlsx")
    wb4 = __import__("openpyxl").Workbook()
    wb4.active.title = "Sales"
    wb4["Sales"]["A3"] = 7.78
    wb4.create_sheet("Sales ")["A3"] = 50
    wb4.create_sheet("Sales ")["A3"] = 99
    wb4.save(r4_book)
    for nm, ch in R3_WS:
        key_ = nm.replace(" ", "")
        r4_rows.append((f"Csheet{key_}", "r4", "8", "usd", "2027", "cell", r4_book, f"Sales{ch}!A3"))
        r4_want[f"Csheet{key_}"] = "the sheet part"
        r4_rows.append((f"Ccell{key_}", "r4", "8", "usd", "2027", "cell", r4_book, f"Sales!{ch}A3"))
        r4_want[f"Ccell{key_}"] = "the cell part"
    r4_guard = [
        ("Gpad", "150", "gl", r3_good, " journal = GJ\t;\taccounts =\t46000-30 , 46000-30\t; store = POW ;from= 2026-01-01 ;"
                                       "to =2026-01-31\t;side\t= credit-debit "),
        ("Gunq", "8", "cell", r4_book, "Sales !A3"),
        ("Gunqt", "8", "cell", r4_book, "Sales\t! A3\t"),
        ("Gq", "8", "cell", r4_book, "'Sales'!A3"),
        ("Gqsp", "50", "cell", r4_book, "'Sales '!A3"),
        ("Gqnb", "99", "cell", r4_book, "'Sales '!A3"),
        ("Gqpad", "50", "cell", r4_book, " 'Sales '\t!\t$A$3 "),
    ]
    for rid, sh_, kind_, src_, det in r4_guard:
        r4_rows.append((rid, "r4", sh_, "usd", "2027", kind_, src_, det))
    r4_fig = os.path.join(tmp, "figures_r4.csv")
    r4_out = os.path.join(tmp, "result_r4.csv")
    write_figures(r4_fig, r4_rows)
    code, so, se = run_tie(r4_fig, out=r4_out)
    r4_main, _ = read_out(r4_out)
    for rid, want in r4_want.items():
        row_ = r4_main.get(rid, {})
        check(f"job06 r4 {rid}: ERROR, note names {want}",
              row_.get("status") == "ERROR" and row_.get("recomputed") == "" and want in row_.get("note", ""))
    for rid, *_ in r4_guard:
        check(f"job06 r4 guard {rid}: exactly TIED", r4_main.get(rid, {}).get("status") == "TIED")
    check("job06 r4 unquoted 'Sales !A3' reads sheet Sales (7.78), quoted 'Sales ' reads its own sheet (50)",
          r4_main.get("Gunq", {}).get("recomputed") == "7.78" and r4_main.get("Gqsp", {}).get("recomputed") == "50")

    # --- bad input
    code, _, _ = run_tie(os.path.join(tmp, "no_such_figures.csv"))
    check("missing figures file: exit 2", code == 2)
    badhdr = os.path.join(tmp, "figures_bad_header.csv")
    with open(badhdr, "w", encoding="utf-8", newline="") as f:
        f.write("id,label,value\nA,b,1\n")
    code, _, _ = run_tie(badhdr)
    check("bad figures header: exit 2", code == 2)
    dupid = os.path.join(tmp, "figures_duplicate_id.csv")
    write_figures(dupid, [base[0], ("C1", "Same id again", "1,234") + base[0][3:]])
    code, so, se = run_tie(dupid)
    check("figures with a duplicate id: exit 2, nothing run", code == 2 and "duplicate id C1" in se and so == "")
    # a crash inside the program: csv.reader broken before tie_out runs as __main__
    crash_code = ("import csv, runpy, sys; sys.argv = [sys.argv[1], sys.argv[2]]; "
                  "csv.reader = None; runpy.run_path(sys.argv[0], run_name='__main__')")
    p = subprocess.run([sys.executable, "-I", "-B", "-c", crash_code, TIE_OUT, clean],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    check("a crash exits 2 with one 'stopped on an unexpected' line and no RESULT",
          p.returncode == 2 and "tie_out stopped on an unexpected TypeError; no result" in p.stderr
          and "RESULT" not in p.stdout and "Traceback" not in p.stderr)
    withscale =os.path.join(tmp, "figures_with_scale_column.csv")
    write_figures(withscale, [base[0] + ("as-is", bmd5, bsize)], header=OLD_HEADER)
    wout = os.path.join(tmp, "result_with_scale.csv")
    code, so, se = run_tie(withscale, out=wout)
    usage_lines = [ln for ln in se.splitlines() if ln.startswith("usage:")]
    check("figures with a scale column: exit 2, a usage line says the column is gone, nothing run or written",
          code == 2 and len(usage_lines) == 1 and "scale column is gone" in usage_lines[0]
          and "RESULT" not in so and not os.path.exists(wout))
    withscale2 = os.path.join(tmp, "figures_with_scale_column_last.csv")
    write_figures(withscale2, [base[0] + (bmd5, bsize, "")], header=FIG_HEADER + [" Scale "])
    code, _, se = run_tie(withscale2)
    check("figures with a ' Scale ' column (any case, last): exit 2", code == 2 and "scale column is gone" in se)
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
    # --- --out must name a path where nothing exists yet
    def state(p):
        st_ = os.stat(p)
        if os.path.isdir(p):
            return ("dir", st_.st_mtime_ns, sorted(os.listdir(p)))
        return md5_size(p) + (st_.st_mtime_ns,)

    def out_refused(name, out_arg, guarded, says="already exists"):
        before = [state(p) for p in guarded]
        code, so, se = run_tie(clean, out=out_arg)
        check(f"--out {name}: exit 2, nothing run, file unchanged (md5, size, modified time)",
              code == 2 and so == "" and says in se
              and [state(p) for p in guarded] == before)
    COLON = "--out must hold no ':' other than a drive letter's"
    old_out = os.path.join(tmp, "existing_result.csv")
    with open(old_out, "w", encoding="utf-8", newline="") as f:
        f.write("an earlier result, not to be overwritten\n")
    absolute = os.path.abspath(old_out)
    out_refused("on an existing file, plain path", old_out, [old_out])
    out_refused("equal to the figures file", clean, [clean])
    out_refused("equal to a source file (with a ./ in it)", os.path.join(tmp, ".", "made_up_gl.csv"), [gl])
    out_refused("equal to the source workbook", book, [book])
    out_refused("on an existing file by \\\\?\\", "\\\\?\\" + absolute, [old_out], COLON)
    out_refused("on the figures file by \\\\?\\", "\\\\?\\" + os.path.abspath(clean), [clean], COLON)
    # NTFS alternate data streams: file:zz must never be written onto the file
    for nm, target in (("an existing file", old_out), ("the figures file", clean),
                       ("a source GL", gl), ("the source workbook", book), ("a folder", tmp)):
        out_refused(f"{nm} + ':zz' (a data stream)", target + ":zz", [target], COLON)
        check(f"no ':zz' stream made on {nm}", not os.path.exists(target + ":zz"))
    out_refused("figures file + ':zz:$DATA'", clean + ":zz:$DATA", [clean], COLON)
    out_refused("a relative name with a stream", os.path.relpath(clean) + ":zz", [clean], COLON)
    fresh = os.path.join(tmp, "fresh_result.csv")
    out_refused("a new file name holding ':'", fresh + ":zz", [tmp], COLON)
    check("no file made for a new name holding ':'", not os.path.exists(fresh))
    # a file made between the existence check and the open: mode "x" must refuse it
    race = os.path.join(tmp, "race_result.csv")
    with open(race, "w", encoding="utf-8", newline="") as f:
        f.write("made between the check and the open\n")
    race_before = state(race)
    real_lexists = os.path.lexists
    os.path.lexists = lambda p: False if p == race else real_lexists(p)
    buf_o, buf_e = io.StringIO(), io.StringIO()
    try:
        with contextlib.redirect_stdout(buf_o), contextlib.redirect_stderr(buf_e):
            rc = mod.main([clean, "--out", race])
    finally:
        os.path.lexists = real_lexists
    check("--out made after the check (check blinded): exit 2, file unchanged, no RESULT line",
          rc == 2 and "already exists" in buf_e.getvalue() and state(race) == race_before
          and "RESULT" not in buf_o.getvalue())
    drive, rest = os.path.splitdrive(absolute)
    unc = "\\\\localhost\\" + drive[0] + "$" + rest
    check("the \\\\localhost\\C$ spelling reaches the file (the test is real)",
          os.path.isfile(unc) and os.path.samefile(unc, absolute))
    out_refused("on an existing file by \\\\localhost\\C$", unc, [old_out])
    link = os.path.join(tmp, "hard_link_to_figures.csv")
    os.link(clean, link)
    check("the hard link is the figures file (the test is real)", os.path.samefile(link, clean))
    out_refused("on a hard link to the figures file", link, [clean, link])
    out_refused("on an existing folder", tmp, [old_out])
    code, _, se = run_tie(clean, out="")
    check("--out with an empty path: exit 2", code == 2 and "--out needs a path" in se)
    new_out = os.path.join(tmp, "new_result.csv")
    code, so, _ = run_tie(clean, out=new_out)
    check("--out on a new path: written, last line RESULT: PASS",
          code == 0 and os.path.isfile(new_out) and last_line(open(new_out, encoding="utf-8").read()) == "RESULT: PASS")
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
