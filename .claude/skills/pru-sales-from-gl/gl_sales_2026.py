"""PRU 2026 sales from the GL, by category and month, tied to Operating Statements PRUAct row 13.

Rick's rebuild steps 1-5 (JOBS\\01 ...\\PRU 2026 SALES - source, categories, rebuild steps (from Rick).md).

Usage:
  python gl_sales_2026.py --gl <GL csv> --opstmt <Operating Statements xlsx> --out <csv> [--through N]

Reads from the GL only the columns Account, Journal, Date, Debit Amount, Credit Amount,
plus Store to filter on. Prints aggregates only, never a GL line.
Last line is RESULT: PASS (exit 0) or RESULT: STOP (exit 1).
"""
import argparse
import csv
import hashlib
import os
import sys
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP

import openpyxl

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
CATEGORIES = ["2-Wheel", "3-Wheel", "Advance Rider/BRC2", "IME", "HD Academy", "Other training", "LDW"]
USED = ["Account", "Journal", "Date", "Debit Amount", "Credit Amount"]
STORE = "Store"
TIE_TOL = Decimal("0.005")
CENT = Decimal("0.01")


class Stop(Exception):
    pass


def category(acct5):
    if acct5 == "47700":
        return "LDW"
    if acct5.startswith("460"):
        return "2-Wheel"
    if acct5.startswith("461"):
        return "3-Wheel"
    if acct5.startswith("462"):
        return "Advance Rider/BRC2"
    return {"46350": "IME", "46400": "HD Academy", "46450": "Other training"}.get(acct5)


def money(text):
    t = (text or "").strip().replace(",", "").replace("$", "")
    if not t:
        return Decimal("0")
    neg = t.startswith("(") and t.endswith(")")
    if neg:
        t = t[1:-1]
    v = Decimal(t)
    return -v if neg else v


def parse_date(text):
    t = (text or "").strip()
    for fmt in ("%m/%d/%Y", "%Y-%m-%d", "%m/%d/%y"):
        try:
            return datetime.strptime(t, fmt)
        except ValueError:
            pass
    raise Stop("a date the program cannot read in the Date column")


def read_gl(path):
    """Return {category: {month: Decimal}} and {account: net} for store POW, 2026."""
    sums = {c: {m: Decimal("0") for m in range(1, 13)} for c in CATEGORIES}
    unknown = {}
    seen = set()  # months holding any PRU 46xxx-30/47700-30 line in store POW
    with open(path, newline="", encoding="utf-8-sig", errors="replace") as f:
        reader = csv.reader(f)
        header = [h.strip() for h in next(reader)]
        idx = {}
        for name in USED + [STORE]:
            if name not in header:
                raise Stop(f"GL header has no column '{name}'")
            idx[name] = header.index(name)
        need = max(idx.values())
        for row in reader:
            if len(row) <= need:
                continue
            if row[idx[STORE]].strip() != "POW":
                continue
            acct = row[idx["Account"]].strip()
            if len(acct) != 8 or acct[5] != "-" or acct[6:] != "30":
                continue
            a5 = acct[:5]
            if not (a5.startswith("46") or a5 == "47700"):
                continue
            d = parse_date(row[idx["Date"]])
            if d.year != 2026:
                continue
            net = money(row[idx["Credit Amount"]]) - money(row[idx["Debit Amount"]])
            seen.add(d.month)
            cat = category(a5)
            if cat is None:
                unknown[acct] = unknown.get(acct, Decimal("0")) + net
                continue
            sums[cat][d.month] += net
    return sums, {a: v for a, v in unknown.items() if v != 0}, seen


def read_pruact(path, through):
    """Return {month: Decimal} from sheet PRUAct row 13, month columns found from the header rows."""
    wb = openpyxl.load_workbook(path, data_only=True, read_only=True)
    try:
        if "PRUAct" not in wb.sheetnames:
            raise Stop("workbook has no sheet PRUAct")
        ws = wb["PRUAct"]
        rows = list(ws.iter_rows(min_row=1, max_row=13, values_only=True))
    finally:
        wb.close()
    cols = None
    for r in rows[:12]:
        found = {}
        for j, v in enumerate(r):
            if isinstance(v, str):
                key = v.strip()[:3].title()
                if key in MONTHS and MONTHS.index(key) + 1 not in found:
                    found[MONTHS.index(key) + 1] = j
        if all(m in found for m in range(1, through + 1)):
            cols = found
            break
    if cols is None:
        raise Stop(f"PRUAct header rows do not name months 1..{through}")
    r13 = rows[12] if len(rows) >= 13 else ()
    out = {}
    for m in range(1, through + 1):
        j = cols[m]
        v = r13[j] if j < len(r13) else None
        if not isinstance(v, (int, float)):
            raise Stop(f"PRUAct row 13 has no number for {MONTHS[m - 1]}")
        out[m] = Decimal(repr(float(v)))
    return out


def md5(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def same_file(a, b):
    try:
        if os.path.exists(a) and os.path.exists(b) and os.path.samefile(a, b):
            return True
    except OSError:
        pass
    return os.path.normcase(os.path.realpath(a)) == os.path.normcase(os.path.realpath(b))


def run(args):
    n = args.through
    if not 1 <= n <= 12:
        raise Stop("--through must be 1..12")
    for other, label in ((args.gl, "--gl"), (args.opstmt, "--opstmt")):
        if same_file(args.out, other):
            raise Stop(f"--out is the same file as {label}")
    sums, unknown, seen = read_gl(args.gl)
    empty = [MONTHS[m - 1] for m in range(1, n + 1) if m not in seen]
    if empty:  # a month with no GL line is not closed yet: never report it as zero sales
        raise Stop("the GL has no PRU line for " + ", ".join(empty) + "; --through is past the data")
    if unknown:
        for a in sorted(unknown):
            print(f"Unknown account {a} nets {unknown[a]:.2f}")
        raise Stop("GL holds a 46xxx-30 account with a nonzero net outside the categories")
    act = read_pruact(args.opstmt, n)
    bad = False
    for m in range(1, n + 1):
        gl_total = sum(sums[c][m] for c in CATEGORIES)
        if abs(gl_total - act[m]) > TIE_TOL:
            print(f"{MONTHS[m - 1]}: GL {gl_total:.2f} vs PRUAct row 13 {act[m]:.2f}")
            bad = True
    if bad:
        raise Stop("a month does not tie to PRUAct row 13")

    def r(x):
        return x.quantize(CENT, rounding=ROUND_HALF_UP)

    with open(args.out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["category"] + MONTHS[:n] + ["total"])
        for c in CATEGORIES:
            vals = [sums[c][m] for m in range(1, n + 1)]
            w.writerow([c] + [f"{r(v):.2f}" for v in vals] + [f"{r(sum(vals)):.2f}"])
        tot = [sum(sums[c][m] for c in CATEGORIES) for m in range(1, n + 1)]
        w.writerow(["Total"] + [f"{r(v):.2f}" for v in tot] + [f"{r(sum(tot)):.2f}"])
    for c in CATEGORIES:
        print(f"{c}: {r(sum(sums[c][m] for m in range(1, n + 1))):.2f}")
    grand = sum(sums[c][m] for c in CATEGORIES for m in range(1, n + 1))
    print(f"Total: {r(grand):.2f}")
    print(f"out md5: {md5(args.out)}")


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--gl", required=True)
    p.add_argument("--opstmt", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--through", type=int, default=9)
    args = p.parse_args(argv)
    try:
        run(args)
    except Stop as e:
        print(f"STOP: {e}")
        print("RESULT: STOP")
        return 1
    except Exception as e:  # any other fault is a stop, not a pass
        print(f"STOP: {type(e).__name__}: {e}")
        print("RESULT: STOP")
        return 1
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
