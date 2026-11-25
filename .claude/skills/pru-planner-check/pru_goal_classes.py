"""pru_goal_classes.py - checks the classes in a PRU planner goal file.

Usage: python3.14 -I pru_goal_classes.py --goal <goal xlsx> --classes <class data xlsx> [--year 2027]

Reads only, writes nothing. Last line is RESULT: PASS (exit code 0) or RESULT: STOP (exit code 1).
From the class data file it reads only the sheet "2026 Demand Analysis". From the goal file it skips the Dirt Bike tab.
"""
import argparse
import datetime
import math
import re
import sys
from collections import defaultdict

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
DEMAND_SHEET = "2026 Demand Analysis"
DEMAND_HEADER_ROW = 3
DEMAND_COLUMNS = ["WE Date !", "Course", "Site", "Limit", "# Stud", "Fees"]
RANGE_CODES = {
    "Manassas Mall": ["MANMALL"],
    "Woodbridge": ["WOOD"],
    "Fairfax GMU": ["FAIRFAX"],
    "Manassas GMU": ["MANGMU"],
    "Colonial Heights": ["COLONIAL"],
    "Stafford": ["STAFFORD"],
    "Newport News": ["NEWPORT"],
    "Virginia Beach": ["VABEACH", "VABEACH2", "VABEACH3"],
    "Clarksburg": ["CLARKSBG"],
}
GOAL_HEADER_ROW = 3
RANGE_TOTAL = "Range total"
CLASSES_BY_RANGE = "Classes by range"
NOT_CHECKED = ["Dirt Bike"]


class Stop(Exception):
    pass


def blank(v):
    return v is None or (isinstance(v, str) and v.strip() == "")


def is_number(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def fmt(v):
    if is_number(v) and float(v).is_integer():
        return str(int(v))
    return str(v)


# ---------- holidays and weekends ----------

def touching_sunday(d):
    """The Sunday of the weekend a date touches, or None (Tue to Thu)."""
    wd = d.weekday()  # Mon 0 .. Sun 6
    if wd == 4:
        return d + datetime.timedelta(days=2)
    if wd == 5:
        return d + datetime.timedelta(days=1)
    if wd == 6:
        return d
    if wd == 0:
        return d - datetime.timedelta(days=1)
    return None


def nth_weekday(year, month, weekday, n):
    d = datetime.date(year, month, 1)
    d += datetime.timedelta(days=(weekday - d.weekday()) % 7)
    return d + datetime.timedelta(weeks=n - 1)


def last_weekday(year, month, weekday):
    nxt = datetime.date(year + (month == 12), month % 12 + 1, 1)
    d = nxt - datetime.timedelta(days=1)
    return d - datetime.timedelta(days=(d.weekday() - weekday) % 7)


def holiday_sundays(year):
    """List of (name, holiday date, Sunday or None)."""
    out = []
    ny = datetime.date(year, 1, 1)
    out.append(("New Year", ny, touching_sunday(ny)))
    mem = last_weekday(year, 5, 0)
    out.append(("Memorial Day", mem, touching_sunday(mem)))
    j4 = datetime.date(year, 7, 4)
    out.append(("July 4", j4, touching_sunday(j4)))
    lab = nth_weekday(year, 9, 0, 1)
    out.append(("Labor Day", lab, touching_sunday(lab)))
    tg = nth_weekday(year, 11, 3, 4)
    out.append(("Thanksgiving", tg, tg + datetime.timedelta(days=(6 - tg.weekday()) % 7)))
    xm = datetime.date(year, 12, 25)
    out.append(("Christmas", xm, touching_sunday(xm)))
    return out


def weekends_by_month(year, holidays):
    """Weekends per month, each Saturday-Sunday weekend in its Saturday's month; a holiday's weekend left out."""
    off = {s for _, _, s in holidays if s is not None}
    counts = [0] * 12
    d = datetime.date(year, 1, 1)
    d += datetime.timedelta(days=(5 - d.weekday()) % 7)
    while d.year == year:
        if d + datetime.timedelta(days=1) not in off:
            counts[d.month - 1] += 1
        d += datetime.timedelta(days=7)
    return counts


# ---------- goal file ----------

def load_goal(path):
    import openpyxl
    try:
        wb = openpyxl.load_workbook(path, data_only=True, read_only=True)
    except Exception as e:
        raise Stop(f"cannot read goal file {path}: {e}")
    sheets = {}
    for ws in wb.worksheets:
        if ws.title in NOT_CHECKED:
            continue
        rows = [list(r) for r in ws.iter_rows(values_only=True)]
        sheets[ws.title] = rows
    wb.close()
    return sheets


def cell(row, i):
    return row[i] if i < len(row) else None


def is_class_count(label, heading):
    """True for a row that counts classes: its label holds the word "classes" (any case) and no "fee",
    or it sits under the heading "Classes by range" (Summary's rows named by range)."""
    if not isinstance(label, str) or blank(label):
        return False
    low = label.lower()
    if "fee" in low:
        return False
    if re.search(r"\bclasses\b", low):
        return True
    return isinstance(heading, str) and heading.strip().lower() == CLASSES_BY_RANGE.lower()


def classes_rows(sheets):
    """Yield (sheet, row number, heading, label, row) for every row that counts classes (is_class_count)."""
    for name, rows in sheets.items():
        heading = None
        found = []
        for n, row in enumerate(rows, 1):
            a = cell(row, 0)
            if is_class_count(a, heading):
                found.append((name, n, heading, a, row))
            if blank(cell(row, 1)):
                heading = a
        if found:
            hdr = rows[GOAL_HEADER_ROW - 1] if len(rows) >= GOAL_HEADER_ROW else []
            got = [cell(hdr, i) for i in range(1, 13)]
            if got != MONTHS:
                raise Stop(f"goal sheet '{name}' row {GOAL_HEADER_ROW} columns B to M are {got}, not Jan to Dec")
        yield from found


def range_total_classes(rows):
    heading = None
    for n, row in enumerate(rows, 1):
        a = cell(row, 0)
        if a == "Classes" and heading == RANGE_TOTAL:
            return n, row
        if blank(cell(row, 1)):
            heading = a
    return None, None


# ---------- class data ----------

def load_limits(path):
    import openpyxl
    try:
        wb = openpyxl.load_workbook(path, data_only=True, read_only=True)
    except Exception as e:
        raise Stop(f"cannot read class data file {path}: {e}")
    if DEMAND_SHEET not in wb.sheetnames:
        raise Stop(f"class data file has no sheet '{DEMAND_SHEET}'")
    ws = wb[DEMAND_SHEET]
    rows = [list(r) for r in ws.iter_rows(min_row=DEMAND_HEADER_ROW, values_only=True)]
    wb.close()
    if not rows:
        raise Stop(f"sheet '{DEMAND_SHEET}' has no row {DEMAND_HEADER_ROW}")
    hdr = rows[0]
    ix = {}
    for col in DEMAND_COLUMNS:
        hits = [i for i, h in enumerate(hdr) if h == col]
        if len(hits) != 1:
            raise Stop(f"sheet '{DEMAND_SHEET}' row {DEMAND_HEADER_ROW}: column '{col}' found {len(hits)} times, not once")
        ix[col] = hits[0]
    code_to_range = {c: r for r, codes in RANGE_CODES.items() for c in codes}
    per_week = defaultdict(int)
    skipped_course = skipped_empty = counted = other_site = 0
    for n, row in enumerate(rows[1:], DEMAND_HEADER_ROW + 1):
        g = lambda k: cell(row, ix[k])
        if all(blank(v) for v in row):
            continue
        if blank(g("Course")):
            skipped_course += 1
            continue
        if blank(g("Limit")) and blank(g("# Stud")) and blank(g("Fees")):
            skipped_empty += 1
            continue
        site = g("Site")
        rng = code_to_range.get(site.strip() if isinstance(site, str) else site)
        if rng is None:
            other_site += 1
            continue
        we = g("WE Date !")
        if isinstance(we, datetime.datetime):
            we = we.date()
        if not isinstance(we, datetime.date):
            raise Stop(f"sheet '{DEMAND_SHEET}' row {n}: WE Date is {we!r}, not a date")
        per_week[(rng, we)] += 1
        counted += 1
    limits = {}
    busiest = {}
    for (rng, we), c in per_week.items():
        if c > limits.get(rng, 0) or (c == limits.get(rng) and we < busiest[rng]):
            limits[rng] = c
            busiest[rng] = we
    stats = dict(counted=counted, skipped_course=skipped_course, skipped_empty=skipped_empty, other_site=other_site)
    return limits, busiest, stats


# ---------- main ----------

def run(goal, classes, year):
    stops = []
    summary = []

    sheets = load_goal(goal)

    # Check 1: whole numbers
    print("CHECK 1: whole numbers in every row that counts classes, months B to M")
    checked = 0
    not_whole = []
    for name, n, heading, label, row in classes_rows(sheets):
        for m in range(12):
            v = cell(row, m + 1)
            if blank(v):
                continue
            if not is_number(v):
                raise Stop(f"goal sheet '{name}' row {n} {MONTHS[m]}: value {v!r} is not a number")
            checked += 1
            if not float(v).is_integer():
                not_whole.append((name, n, heading, MONTHS[m], v))
    for name, n, heading, mon, v in not_whole:
        print(f"NOT WHOLE | sheet {name} | row {n} | section {heading} | {mon} | {fmt(v)}")
    print(f"CELLS CHECKED: {checked}")
    print(f"NOT WHOLE: {len(not_whole)}")
    summary.append(f"Check 1 whole numbers: {checked} cells checked, {len(not_whole)} not whole: " + ("STOP" if not_whole else "PASS"))
    if not_whole:
        stops.append("check 1")

    # Check 2: weekends
    print(f"CHECK 2: weekends in {year}, each in its Saturday's month, holidays out")
    hols = holiday_sundays(year)
    for hname, hd, sun in hols:
        if sun is None:
            print(f"HOLIDAY {hname} {hd.isoformat()} {hd.strftime('%a')}: touches no weekend")
        elif sun.year != year:
            print(f"HOLIDAY {hname} {hd.isoformat()} {hd.strftime('%a')}: Sunday {sun.isoformat()} is outside {year}")
        else:
            print(f"HOLIDAY {hname} {hd.isoformat()} {hd.strftime('%a')}: Sunday {sun.isoformat()} out")
    weekends = weekends_by_month(year, hols)
    for m in range(12):
        print(f"WEEKENDS {MONTHS[m]} {weekends[m]}")
    print(f"WEEKENDS TOTAL {sum(weekends)}")
    summary.append(f"Check 2 weekends {year}: {sum(weekends)} after holidays: done")

    # Check 3: limits
    print(f"CHECK 3: each range's limit, its busiest week in '{DEMAND_SHEET}'")
    range_sheets = [nm for nm, rows in sheets.items() if any(cell(r, 0) == RANGE_TOTAL for r in rows)]
    unmapped = [nm for nm in range_sheets if nm not in RANGE_CODES]
    if unmapped:
        raise Stop(f"range(s) in the goal file with no code in the map: {unmapped}")
    missing = [r for r in RANGE_CODES if r not in sheets]
    if missing:
        raise Stop(f"range(s) of the map with no sheet in the goal file: {missing}")
    limits, busiest, stats = load_limits(classes)
    print(f"DEMAND ROWS COUNTED {stats['counted']} | skipped no Course {stats['skipped_course']} | "
          f"skipped no Limit, # Stud, Fees {stats['skipped_empty']} | other site {stats['other_site']}")
    for rng in RANGE_CODES:
        if rng not in limits:
            raise Stop(f"range {rng} ({'+'.join(RANGE_CODES[rng])}) has no class in '{DEMAND_SHEET}'")
        print(f"LIMIT {rng} | {'+'.join(RANGE_CODES[rng])} | {limits[rng]} | first busiest week {busiest[rng].isoformat()}")
    summary.append(f"Check 3 limits: {len(limits)} ranges found: done")

    # Check 4: month test
    print("CHECK 4: each class line rounded up, then summed, against limit x weekends")
    over = []
    for rng in RANGE_CODES:
        n, row = range_total_classes(sheets[rng])
        if row is None:
            raise Stop(f"goal sheet '{rng}' has no row Classes under the heading '{RANGE_TOTAL}'")
        lines = [r for _, _, h, _, r in classes_rows({rng: sheets[rng]}) if h != RANGE_TOTAL]
        if not lines:
            raise Stop(f"goal sheet '{rng}' has no class line above the heading '{RANGE_TOTAL}'")
        for m in range(12):
            v = cell(row, m + 1)
            if not is_number(v):
                raise Stop(f"goal sheet '{rng}' row {n} {MONTHS[m]}: value {v!r} is not a number")
            c = 0
            for line in lines:
                lv = cell(line, m + 1)
                if blank(lv):
                    continue
                if not is_number(lv):
                    raise Stop(f"goal sheet '{rng}' {MONTHS[m]}: class line value {lv!r} is not a number")
                c += math.ceil(lv)
            cap = limits[rng] * weekends[m]
            if c > cap:
                over.append((rng, MONTHS[m], c, limits[rng], weekends[m], cap, n))
    for rng, mon, c, lim, wk, cap, n in over:
        print(f"OVER | {rng} | {mon} | classes {c} | limit {lim} | weekends {wk} | limit x weekends {cap} | row {n}")
    print(f"OVER MONTHS: {len(over)}")
    summary.append(f"Check 4 month test: {len(over)} months over: " + ("STOP" if over else "PASS"))
    if over:
        stops.append("check 4")

    print("SUMMARY")
    for s in summary:
        print(s)
    return not stops


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--goal", required=True)
    ap.add_argument("--classes", required=True)
    ap.add_argument("--year", type=int, default=2027)
    args = ap.parse_args(argv)
    try:
        ok = run(args.goal, args.classes, args.year)
    except Stop as e:
        print(f"STOP REASON: {e}")
        ok = False
    except Exception as e:  # a layout the program does not know
        print(f"STOP REASON: unexpected error: {type(e).__name__}: {e}")
        ok = False
    print("RESULT: PASS" if ok else "RESULT: STOP")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
