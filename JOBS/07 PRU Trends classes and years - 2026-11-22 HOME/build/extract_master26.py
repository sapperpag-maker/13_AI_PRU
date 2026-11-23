"""Job 07 repair (Q79, Q109). 2026 students, class fees and classes from the v3 log's Master sheet, each in the month of the class date in the class code, rows with a week.
Reads columns B to E, and J as sums only. Writes totals by class, range, site and month to master26.json. Never prints or writes a row."""
import collections
import datetime as dt
import hashlib
import json
import re
import sys
import openpyxl

LOG, OUT = sys.argv[1], sys.argv[2]
assert hashlib.md5(open(LOG, "rb").read()).hexdigest().startswith("37c427cf")
SITE = {"MANMALL": "Manassas Mall", "WOOD": "Woodbridge", "FAIRFAX": "Fairfax GMU", "MANGMU": "Manassas GMU", "COLONIAL": "Colonial Heights", "STAFFORD": "Stafford", "NEWPORT": "Newport News", "VABEACH": "Virginia Beach", "VABEACH2": "Virginia Beach", "VABEACH3": "Virginia Beach", "CLARKSBG": "Clarksburg"}
RANGE = {"Manassas Mall": "Manassas -  Mall", "Woodbridge": "Woodbridge - Potomac Mills", "Fairfax GMU": "Fairfax", "Manassas GMU": "Manassas - GMU", "Colonial Heights": "Colonial Heights -Southpark", "Stafford": "Stafford", "Newport News": "Newport News - Patrick Henry Mall", "Virginia Beach": "Virginia Beach", "Clarksburg": "Clarksburg (MD)"}
TYPE = {"BRCE": "2-Wheel", "BRCEM": "2-Wheel", "BRCES": "2-Wheel", "BRCR": "2-Wheel", "3WBRE": "3-Wheel", "3WBRM": "3-Wheel", "BRC2W": "BRC2", "BRC2P": "BRC2", "IME": "First Ride", "ARC": "ARC"}
LOGCLS = {"2-Wheel": "2-Wheel", "3-Wheel": "3-Wheel", "BRC2": "BRC2", "First Ride": "IME", "ARC": "ARC"}
lines = collections.defaultdict(lambda: {"n": [0] * 12, "d": [0.0] * 12})
fill = collections.defaultdict(lambda: {"c": [0] * 12, "s": [0] * 12})
first = {}
courses = collections.defaultdict(set)
places = collections.defaultdict(set)
wb = openpyxl.load_workbook(LOG, read_only=True, data_only=True)
ws = wb["Master"]
for (site, code, course, week), (fee,) in zip(ws.iter_rows(min_row=2, min_col=2, max_col=5, values_only=True), ws.iter_rows(min_row=2, min_col=10, max_col=10, values_only=True)):
    m = re.match(r"[A-Za-z](\d{2})(\d{2})(\d{2})-", str(code or ""))
    if not m or int(m[1]) != 26 or not isinstance(week, (dt.datetime, dt.date)):
        continue
    mo = int(m[2]) - 1
    place, kind = SITE[site], TYPE[course]
    first.setdefault(code, (mo, place + "|" + kind))
    courses[code].add(course)
    places[code].add(place)
    if course == "BRCR":
        assert place == "Manassas GMU"
        cls, rng = "HD", RANGE[place]
    elif kind in ("2-Wheel", "3-Wheel"):
        cls, rng = kind, RANGE[place]
    else:
        cls, rng = LOGCLS[kind], "All Locations"
    e = lines[(cls, rng)]
    e["n"][mo] += 1
    e["d"][mo] += fee if isinstance(fee, (int, float)) else 0
    if course != "BRCR":   # HD students stand on their own line, as on Trends
        fill[place + "|" + kind]["s"][mo] += 1
hd_classes = 0
for code, (mo, key) in first.items():
    if courses[code] == {"BRCR"}:   # a class holding only HD students is an HD class
        key = key.split("|")[0] + "|HD"
        hd_classes += 1
    fill[key]["c"][mo] += 1
many = [(first[k], len(places[k]), len(courses[k])) for k in first if len(places[k]) > 1]
assert hd_classes == 6 and len(many) == 1 and many[0] == ((11, "Clarksburg|2-Wheel"), 8, 8), (hd_classes, many)
out = {"lines": [{"cls": k[0], "range": k[1], "n": v["n"], "d": [round(x, 2) for x in v["d"]]} for k, v in sorted(lines.items())], "fill": {k: fill[k] for k in sorted(fill)}}
n = sum(sum(x["n"]) for x in out["lines"])
d = sum(sum(x["d"]) for x in out["lines"])
c = sum(sum(x["c"]) for x in out["fill"].values())
s = sum(sum(x["s"]) for x in out["fill"].values())
hd = sum(sum(x["n"]) for x in out["lines"] if x["cls"] == "HD")
assert (n, round(d, 2), c, hd, s) == (4606, 1602640.0, 573, 48, 4558), (n, d, c, hd, s)
json.dump(out, open(OUT, "w", encoding="utf-8"), separators=(",", ":"))
print("students", n, "| fees", round(d, 2), "| classes", c, "| HD", hd, "| students on site rows", s)
print("students by month", [sum(x["n"][k] for x in out["lines"]) for k in range(12)])
