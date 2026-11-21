# Angie's own test, release 3: recompute the goal's figures from Class Data itself (not from the page) -> rel3/expected.json
import json, openpyxl
CD = r'C:\Users\Sergio\.claude\uploads\034bc097-973b-403b-8a90-c7678efdb939\f32ce509-Class_Data.xlsx'   # his updated quantities, 2026-11-20 (md5 542d634b)
ws = openpyxl.load_workbook(CD, data_only=True, read_only=True)['2027 Projections']
g = {}
assert ws.cell(32, 1).value == 'Woodbridge' and ws.cell(66, 1).value == 'ALL SITES'
for row in ws.iter_rows(min_row=1, max_row=26, max_col=13):
    for c in row:
        if c.value is not None: g[c.coordinate] = c.value
r3 = json.load(open('r3.json'))
fails = []
def chk(cond, msg):
    if not cond: fails.append(msg)
# test 1: site x type classes = A1:F11, and 498
TYPES = {'B': '2-Wheel', 'C': '3-Wheel', 'D': 'BRC2', 'E': 'First Ride'}
grid = {}
for r in range(2, 11):
    site = g['A%d' % r]
    for col, t in TYPES.items():
        grid[(site, t)] = float(g.get('%s%d' % (col, r), 0) or 0)
chk(g['F11'] == 498, 'F11 is not 498')
# his updated file carries his answer 34 itself: no class is moved by code
chk(sum(grid.values()) == 498, 'classes are not 498')
units = {(u['site'], u['type']): u['m'] for u in r3['units']}
for k, v in grid.items():
    got = sum(units.get(k, [0] * 12))
    chk(abs(got - v) < 1e-9, 'classes %s: units %s vs Class Data %s' % (k, got, v))
# monthly totals by type = rows 15-26
for i in range(12):
    for col, t in TYPES.items():
        want = float(g.get('%s%d' % (col, 15 + i), 0) or 0)
        got = sum(m[i] for (s, tt), m in units.items() if tt == t)
        chk(abs(got - want) < 1e-6, 'month %d %s: units %s vs Class Data %s' % (i + 1, t, got, want))
# prices M17:M21 (labels in L)
price = {str(g['H%d' % r]).strip().upper(): g['M%d' % r] for r in range(17, 22)}   # M17:M21, rows named in H
# coach H17:J21
coach = {}
for r in range(17, 22):
    coach[str(g['H%d' % r]).strip().upper()] = (g['I%d' % r], g['J%d' % r])
aid = g['J22']
CK = {'2-Wheel': '2 WHEEL', '3-Wheel': '3 WHEEL', 'BRC2': 'BRC2', 'First Ride': 'FIRST RIDE', 'ARC': 'ARC'}
# rent H3:J11
rate = {}
for r in range(3, 12):
    rate[g['H%d' % r]] = g.get('J%d' % r) or g['I%d' % r]
cap = {'2-Wheel': 12, '3-Wheel': 12, 'BRC2': 12, 'First Ride': 4, 'ARC': 12}   # his answer 33
MN = range(2, 11)
def fill(keys, t):
    c = sum(r3['fill26'][k]['c'][m] for k in keys for m in MN); s = sum(r3['fill26'][k]['s'][m] for k in keys for m in MN)
    return s / (c * cap[t]) * 100
out = {'price_read': price, 'coach_read': {k: list(v) for k, v in coach.items()}, 'aid': aid, 'rate_read': rate, 'fails': fails}
exp_units = {}
for (site, t), m in units.items():
    key = site + '|' + t
    f = fill([key], t) if key in r3['fill26'] else fill([k for k in r3['fill26'] if k.endswith('|' + t)], t)
    spc = cap[t] * f / 100
    p = price[CK[t]]
    two, one = coach[CK[t]]
    per = two if round(spc, 1) > 6 else one   # Piston's R-1876 pick: the coach rule reads students per class as shown
    exp_units[key] = {'cls': m, 's': [c * spc * p for c in m], 'coach': [c * per for c in m]}
out['units'] = exp_units
storage = {s: (v['storage'] or 0) for s, v in r3['rent'].items()}
wk = r3['weekends26']   # his answer 36: weekends per class from 2026
out['rent'] = [sum(sum(units[(s, t)][i] for t in TYPES.values() if (s, t) in units) * wk[s]['weekends'] / wk[s]['classes'] * rate[s] + storage.get(s, 0) / 12 for s in rate) for i in range(12)]
out['ldw_rate'] = 26518.37 / 1364378.50
open('rel3/expected.json', 'w').write(json.dumps(out))
print('fails', len(fails), fails[:5]); print('price', price); print('coach', coach, 'aid', aid); print('rent', [round(x) for x in out['rent']], round(sum(out['rent'])))
