import json, hashlib, sys
RICK_WB, PL_JSON, OUT_HTML = sys.argv[1], sys.argv[2], sys.argv[3]   # Rick's workbook, its PRU-pl extract, the page to write
d = json.load(open('weekly_by_range.json'))
for e in d:
    for k in ('n','d'):
        e[k] = {y: [round(v) for v in e[k][y]] for y in ('2026','2025','2024','2023','2022')}
pl = json.load(open(PL_JSON))
extra = json.load(open('classes2026.json'))
# release 3 (goal accepted 2026-11-20): Class Data '2027 Projections' and 2026 fill from the attached log's Master, made by extract_r3.py
import re
r3=json.load(open('r3.json'))
for k in ('classes','spc','hours'): r3['dirt'][k]=int(re.match(r'\d+',r3['dirt'][k]).group())
extra['r3']=r3
extra['master26']=json.load(open('master26.json',encoding='utf-8'))   # Q79, Q109: shown 2026, Master by class date
# Rick's 2026 figure for reference (his answer 18): 02 workbook, PRU-pl, row 13 Training, column AB (header '2026')
import openpyxl
_ws=openpyxl.load_workbook(RICK_WB,read_only=True,data_only=True)['PRU-pl']
assert str(_ws['AB6'].value).strip()=='2026' and _ws['B13'].value=='Training'
extra['rick2026']=round(_ws['AB13'].value,2)
# Rick's 2026 by month: PRU-pl row 121 (block '2026 - Prior Year', B112), columns D-F, I-K, N-P, S-U; Oct-Dec are his forecast
_r=[c.value for c in next(_ws.iter_rows(min_row=121,max_row=121))]
assert _r[1]=='Training'
extra['rick2026m']=[round(_r[i],2) for i in (3,4,5,8,9,10,13,14,15,18,19,20)]
assert abs(sum(extra['rick2026m'])-extra['rick2026'])<0.01
# his answer 23, 'Five named rows': the parts of Rick's 2026 less the Manual Log, from LAWYER's FINDINGS.md
# (C:/AI_Building/AI_MISC/06 Benches/2026-11-20 PRU sales why differ - LAWYER-HOME-1118/FINDINGS.md) and Rick's message of 2026-11-20
extra['gapParts']=[
 ['Loss Damage Waiver (GL 47700-30), not in the Manual Log',26518.37],
 ['Other training income (GL 46450-30), not in the Manual Log',8323.95],
 ['January classes missing from the Manual Log',14469.00],
 ['Class fees above the Manual Log, Feb–Sep (not reconciled)',15204.50],
 ["Oct–Dec: the workbook's forecast less the Manual Log's bookings",None]]
_log=sum(sum(e['d']['2026']) for e in d)
# Oct-Dec part = Rick's Oct-Dec less the log's Oct-Dec (it moves as December bookings come in)
extra['gapParts'][4][1]=round(sum(extra['rick2026m'][9:12])-sum(sum(e['d']['2026'][9:12]) for e in d),2)
assert abs(sum(v for _,v in extra['gapParts'])-(extra['rick2026']-_log))<1, (sum(v for _,v in extra['gapParts']), extra['rick2026']-_log)
J = lambda o: json.dumps(o, separators=(',',':')).replace('<','\u003c')
t = open('template.html', encoding='utf-8').read()
theme = open('theme.css', encoding='utf-8').read().strip()
init = {"fillAll":None,"fillType":{},"fillUnit":{},"unitMonths":{},"price":{},"rate":{},"showDirt":True,"savedAt":None}
out = (t.replace('__THEME__', theme).replace('__STATE__', J(init)).replace('__DATA__', J(d))
        .replace('__PL__', J(pl)).replace('__EXTRA__', J(extra)))
assert '__' + 'STATE' not in out and '__PL__' not in out and '__EXTRA__' not in out and '__THEME__' not in out
p = OUT_HTML
open(p,'w',encoding='utf-8',newline='\n').write(out)
open('preview.html','w',encoding='utf-8',newline='\n').write('<meta charset="utf-8">'+out)
print(len(out.encode()), hashlib.md5(out.encode()).hexdigest())
