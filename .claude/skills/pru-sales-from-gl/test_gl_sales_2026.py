"""Test for gl_sales_2026.py: real inputs, a made-up pair, and planted faults.

Usage: python test_gl_sales_2026.py [--bench <scratch folder>]
Prints RESULT: PASS only if every check holds.
"""
import argparse
import csv
import os
import subprocess
import sys

import openpyxl

HERE = os.path.dirname(os.path.abspath(__file__))
PROG = os.path.join(HERE, "gl_sales_2026.py")
REAL_GL = r"C:\AI_Building\AI_Financials\00 Raw data\GL\2026 YTD 101E GL History Detail Postings - All Accounts.csv"
REAL_OS = r"C:\AI_Building\AI_Financials\04 Budget\2027\raw files\3 Operating statements\02 - Operating Statements 2026-09.xlsx"
DEFAULT_BENCH = r"C:\AI_Building\AI_MISC\06 Benches\2026-11-21 PRU budget skill - ANGIE-HOME\gl"

REAL_CATS = {
    "2-Wheel": "1180249.00", "3-Wheel": "119428.00", "Advance Rider/BRC2": "36032.00",
    "IME": "6534.00", "HD Academy": "22135.50", "Other training": "8323.95", "LDW": "26518.37",
}
REAL_MONTHS = ["15552.61", "60160.28", "201004.26", "200237.82", "246286.44",
               "191234.34", "171425.99", "180524.17", "132794.91"]
REAL_TOTAL = "1399220.82"

fails = []


def check(cond, what):
    print(("ok   " if cond else "FAIL ") + what)
    if not cond:
        fails.append(what)


def run(gl, os_, out, through=None):
    cmd = [sys.executable, PROG, "--gl", gl, "--opstmt", os_, "--out", out]
    if through:
        cmd += ["--through", str(through)]
    p = subprocess.run(cmd, capture_output=True, text=True)
    lines = p.stdout.strip().splitlines()
    return p.returncode, lines


def read_out(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.reader(f))


HEADER = ["Account ", "Journal ", "Date", "Doc #", "Description", "Debit Amount", "Credit Amount", "Balance", "Store "]


def write_gl(path, extra=()):
    rows = [
        ["46001-30", "Sales", "1/5/2026", "1", "x", "", "100.00", "", "POW"],
        ["46001-30", "Sales", "1/9/2026", "2", "x", "10.00", "", "", "POW"],
        ["46101-30", "Sales", "2/3/2026", "3", "x", "", "1,200.50", "", "POW"],
        ["46201-30", "Sales", "2/4/2026", "4", "x", "", "50.00", "", "POW"],
        ["46350-30", "Sales", "3/1/2026", "5", "x", "", "30.00", "", "POW"],
        ["46400-30", "Sales", "3/2/2026", "6", "x", "", "40.25", "", "POW"],
        ["46450-30", "Sales", "3/3/2026", "7", "x", "", "5.10", "", "POW"],
        ["47700-30", "Sales", "1/20/2026", "8", "x", "", "7.77", "", "POW"],
        ["46013-30", "Sales", "2/1/2026", "9", "x", "", "25.00", "", "POW"],
        ["46013-30", "Sales", "2/2/2026", "10", "x", "25.00", "", "", "POW"],
        ["46001-30", "Sales", "1/5/2026", "11", "x", "", "999.00", "", "FC1"],
        ["46000-70", "Sales", "1/5/2026", "12", "x", "", "999.00", "", "POW"],
        ["46001-30", "Sales", "12/31/2025", "13", "x", "", "999.00", "", "POW"],
        ["46001-30", "Sales", "4/1/2026", "14", "x", "", "888.00", "", "POW"],
        ["Account Department: ", "", "", "", "", "", "", "", ""],
    ] + list(extra)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(HEADER)
        w.writerows(rows)


def write_os(path, mar_value=75.35):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "PRUAct"
    ws["B1"] = "made-up"
    hdr = {"D": "Jan", "E": "Feb", "F": "Mar", "G": "Q1", "H": "% Sales", "I": "Apr", "Y": "Total"}
    for c, v in hdr.items():
        ws[f"{c}6"] = v
    ws["B13"] = "Training"
    ws["D13"] = 97.77
    ws["E13"] = 1250.50
    ws["F13"] = mar_value
    ws["G13"] = 999999
    ws["I13"] = 888.00
    wb.save(path)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bench", default=DEFAULT_BENCH)
    a = ap.parse_args()
    os.makedirs(a.bench, exist_ok=True)
    b = a.bench

    # (1) real inputs
    out = os.path.join(b, "t_real_out.csv")
    rc, lines = run(REAL_GL, REAL_OS, out, 9)
    check(rc == 0 and lines and lines[-1] == "RESULT: PASS", "real inputs give RESULT: PASS, exit 0")
    for c, v in REAL_CATS.items():
        check(f"{c}: {v}" in lines, f"real {c} = {v}")
    check(f"Total: {REAL_TOTAL}" in lines, f"real total = {REAL_TOTAL}")
    if os.path.exists(out):
        rows = read_out(out)
        check(rows[0] == ["category", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "total"],
              "real out header")
        tot = rows[-1]
        check(tot[0] == "Total" and tot[1:10] == REAL_MONTHS and tot[10] == REAL_TOTAL,
              "real out Total row months and total match Rick's table")
    else:
        check(False, "real out file written")

    # (2) made-up pair
    gl = os.path.join(b, "t_fake_gl.csv")
    xl = os.path.join(b, "t_fake_os.xlsx")
    out = os.path.join(b, "t_fake_out.csv")
    write_gl(gl)
    write_os(xl)
    rc, lines = run(gl, xl, out, 3)
    check(rc == 0 and lines and lines[-1] == "RESULT: PASS", "made-up pair --through 3 gives PASS")
    expect = {"2-Wheel": "90.00", "3-Wheel": "1200.50", "Advance Rider/BRC2": "50.00", "IME": "30.00",
              "HD Academy": "40.25", "Other training": "5.10", "LDW": "7.77"}
    for c, v in expect.items():
        check(f"{c}: {v}" in lines, f"made-up {c} = {v}")
    if os.path.exists(out):
        rows = read_out(out)
        check(rows[-1] == ["Total", "97.77", "1250.50", "75.35", "1423.62"],
              "made-up out Total row exact")
    rc, lines = run(gl, xl, os.path.join(b, "t_fake_out4.csv"), 4)
    check(rc == 0 and lines[-1] == "RESULT: PASS", "made-up pair --through 4 (skips quarter columns) gives PASS")
    rc, lines = run(gl, xl, os.path.join(b, "t_fake_out5.csv"), 5)
    check(rc == 1 and lines[-1] == "RESULT: STOP" and any("May" in l for l in lines),
          "--through past the GL's data (May) gives STOP and names May")
    rc, lines = run(REAL_GL, REAL_OS, os.path.join(b, "t_real_out10.csv"), 10)
    check(rc == 1 and lines[-1] == "RESULT: STOP" and any("Oct" in l for l in lines),
          "real inputs --through 10 give STOP and name Oct")

    # (3) planted faults
    write_os(os.path.join(b, "t_bad_os.xlsx"), mar_value=75.36)
    rc, lines = run(gl, os.path.join(b, "t_bad_os.xlsx"), os.path.join(b, "t_bad1.csv"), 3)
    check(rc == 1 and lines[-1] == "RESULT: STOP" and any(l.startswith("Mar:") for l in lines),
          "month that does not tie gives STOP and names Mar")
    gl2 = os.path.join(b, "t_fake_gl_unknown.csv")
    write_gl(gl2, extra=[["46777-30", "Sales", "2/2/2026", "99", "x", "", "12.00", "", "POW"]])
    rc, lines = run(gl2, xl, os.path.join(b, "t_bad2.csv"), 3)
    check(rc == 1 and lines[-1] == "RESULT: STOP" and any("46777-30" in l for l in lines),
          "unknown 46xxx account with nonzero net gives STOP and names it")
    gl3 = os.path.join(b, "t_fake_gl_zero.csv")
    write_gl(gl3, extra=[["46777-30", "Sales", "2/2/2026", "99", "x", "", "12.00", "", "POW"],
                         ["46777-30", "Sales", "2/3/2026", "98", "x", "12.00", "", "", "POW"]])
    rc, lines = run(gl3, xl, os.path.join(b, "t_ok3.csv"), 3)
    check(rc == 0 and lines[-1] == "RESULT: PASS", "unknown account netting to zero does not stop")
    before = open(gl, "rb").read()
    rc, lines = run(gl, xl, gl, 3)
    check(rc == 1 and lines[-1] == "RESULT: STOP", "--out equal to --gl gives STOP")
    check(open(gl, "rb").read() == before, "--gl left unchanged after refused --out")
    rc, lines = run(gl, xl, xl, 3)
    check(rc == 1 and lines[-1] == "RESULT: STOP", "--out equal to --opstmt gives STOP")

    print(f"{len(fails)} failed")
    print("RESULT: PASS" if not fails else "RESULT: FAIL")
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
