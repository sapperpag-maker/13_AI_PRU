"""Job 07: 2026 students from the v3 log's Master sheet by class date, by the budget book's class type and site, against the book's Prior column (PRU GP, column R).
Reads Master columns B to E only. Writes one CSV of totals. Never prints or writes a customer row."""
import collections
import csv
import datetime as dt
import hashlib
import re
import sys
import openpyxl

LOG, BOOK, OUT = sys.argv[1:4]
assert hashlib.md5(open(LOG, "rb").read()).hexdigest().startswith("37c427cf")
SITE = {"MANMALL": "Manassas Mall", "WOOD": "Woodbridge", "FAIRFAX": "Fairfax", "MANGMU": "Manassas-GMU", "COLONIAL": "Colonial Heights", "STAFFORD": "Stafford", "NEWPORT": "Newport News", "VABEACH": "VA Beach-1", "VABEACH2": "VA Beach-2", "VABEACH3": "VA Beach-3", "CLARKSBG": "Clarksburg"}
TYPE = {"BRCE": "2-Wheel", "BRCEM": "2-Wheel", "BRCES": "2-Wheel", "BRCR": "Harley Davidson", "3WBRE": "3-Wheel", "3WBRM": "3-Wheel", "BRC2W": "BRC2", "BRC2P": "BRC2", "IME": "Start", "ARC": "ARC"}
BLOCK = {"2-Wheel": (307, 322), "3-Wheel": (324, 339), "Harley Davidson": (341, 356), "ARC": (358, 373), "BRC2": (375, 390), "Start": (426, 441)}
ALLSITES = {"ARC", "BRC2", "Start"}   # the book holds these on its All sites row
n = collections.Counter()
wb = openpyxl.load_workbook(LOG, read_only=True, data_only=True)
for site, code, course, week in wb["Master"].iter_rows(min_row=2, min_col=2, max_col=5, values_only=True):
    m = re.match(r"[A-Za-z](\d{2})(\d{2})(\d{2})-", str(code or ""))
    if not m or int(m[1]) != 26 or not isinstance(week, (dt.datetime, dt.date)):
        continue
    t = TYPE[course]
    n[(t, "All sites" if t in ALLSITES else SITE[site])] += 1
wb.close()
assert sum(n.values()) == 4606, sum(n.values())
ws = openpyxl.load_workbook(BOOK, data_only=True)["PRU GP"]
rows, used = [], set()
for t, (a, z) in BLOCK.items():
    for r in range(a, z + 1):
        lab = [ws.cell(r, c).value for c in range(1, 6) if isinstance(ws.cell(r, c).value, str)]
        s = lab[-1]
        prior = ws.cell(r, 18).value or 0
        q = n.get((t, s), 0)
        if (t, s) in n:
            used.add((t, s))
        if q or prior:
            rows.append([r, t, s, "hidden" if ws.row_dimensions[r].hidden else "shown", prior, q, q - prior])
assert used == set(n), set(n) - used
with open(OUT, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["PRU GP row", "Class type", "Site", "Row", "Book Prior (column R)", "Master 2026 by class date", "Change"])
    w.writerows(rows)
print("rows", len(rows), "| book", sum(x[4] for x in rows), "| Master", sum(x[5] for x in rows))
for x in rows:
    if x[6] or x[3] == "hidden":
        print(x)
