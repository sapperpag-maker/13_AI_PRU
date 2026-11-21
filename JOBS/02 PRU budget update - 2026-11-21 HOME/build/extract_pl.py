"""PRU-pl rows 7-103 by month (cols D-F, I-K, N-P, S-U) -> pl2027.json. A row is kept when it has a label in B or any month value."""
import openpyxl, sys, json
SRC, OUT = sys.argv[1], sys.argv[2]
ws = openpyxl.load_workbook(SRC, read_only=True, data_only=True)['PRU-pl']
rows = list(ws.iter_rows(min_row=1, max_row=103, values_only=True))
MC = (3,4,5,8,9,10,13,14,15,18,19,20)
assert [rows[5][i] for i in MC] == ['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec'] and rows[5][24] == '2027B'
out = []
for r in range(7, 104):
    v = list(rows[r-1]) + [None]*30
    m = [v[i] for i in MC]
    if v[1] is not None or any(x not in (None, 0) for x in m):
        out.append({'row': r, 'label': str(v[1]).strip() if v[1] is not None else '', 'm': m})
json.dump(out, open(OUT, 'w'))
print('rows', len(out))
