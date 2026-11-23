"""Job 07, Q112: Virginia Beach's 2027 rent by month, 33 weekends against 32, and total rent by month, for the book.
Reads r3.before-q112.json and r3.json. Writes one CSV. Total rent is checked against the page's two year totals."""
import csv
import json
import sys

OLD, NEW, OUT = sys.argv[1:4]
MON = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()


def rent(r3):
    each = {}
    for s, v in r3["rent"].items():
        rate = v["renew"] if v["renew"] is not None else v["rate"]
        w = r3["weekends26"].get(s)
        cls = [sum(u["m"][i] for u in r3["units"] if u["site"] == s) for i in range(12)]
        each[s] = [(c * w["weekends"] / w["classes"] * rate if w and w["classes"] else 0) + (v["storage"] or 0) / 12 for c in cls]
    return each


a, b = rent(json.load(open(OLD, encoding="utf-8"))), rent(json.load(open(NEW, encoding="utf-8")))
assert [s for s in a if any(abs(x - y) > 1e-9 for x, y in zip(a[s], b[s]))] == ["Virginia Beach"]
ta, tb = [sum(v[i] for v in a.values()) for i in range(12)], [sum(v[i] for v in b.values()) for i in range(12)]
assert abs(sum(ta) - 155992.29367917063) < 0.005, sum(ta)
assert abs(sum(tb) - 155429.6369627527) < 0.005, sum(tb)
va, vb = a["Virginia Beach"], b["Virginia Beach"]
rows = [[MON[i], round(va[i], 2), round(vb[i], 2), round(vb[i] - va[i], 2), round(ta[i], 2), round(tb[i], 2), round(tb[i] - ta[i], 2)] for i in range(12)]
rows.append(["Year", round(sum(va), 2), round(sum(vb), 2), round(sum(vb) - sum(va), 2), round(sum(ta), 2), round(sum(tb), 2), round(sum(tb) - sum(ta), 2)])
with open(OUT, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["2027 month", "Virginia Beach rent, 33 weekends", "Virginia Beach rent, 32 weekends", "Change", "Total rent, release 6", "Total rent, release 7", "Change"])
    w.writerows(rows)
for r in rows:
    print(r)
print("rounded months add to", round(sum(r[3] for r in rows[:12]), 2), "| year change", rows[12][3])
