// Angie's own test of release 4 (coach cost in Cost of Sales; release 3 tests kept), run in the page: goal tests 1-7 against rel3/expected.json, then test 8 (each fails on a planted fault)
(async()=>{
const E=await fetch('/rel4/expected.json?'+Date.now()).then(r=>r.json());const SRC=JSON.parse(document.getElementById('src-pl').textContent);
const s=a=>a.reduce((p,q)=>p+q,0);const CLS=498;
function run(T){const b=T.budget(),a=b.agg,B=b.B,res={};
 let f1=[];if(Math.abs(s(a.cls)-CLS)>1e-6)f1.push('total');a.ups.forEach(({u,p})=>{const e=E.units[u.key];if(!e){f1.push('nokey '+u.key);return;}p.cls.forEach((c,m)=>{if(Math.abs(c-e.cls[m])>1e-9)f1.push(u.key+m);});});if(Object.keys(E.units).length!==a.ups.length)f1.push('count');res.t1=f1;
 res.t2=a.ups.filter(({u,p})=>Math.abs(s(p.s)-s(E.units[u.key].s))>0.5).map(x=>x.u.key);
 let f3=[];a.ups.forEach(({u,p})=>p.coach.forEach((c,m)=>{if(Math.abs(c-E.units[u.key].coach[m])>1e-6)f3.push(u.key+m);}));res.t3=f3;
 res.t4=a.rent.map((q,m)=>Math.abs(q-E.rent[m])>0.01?m:null).filter(x=>x!=null);
 res.t5=a.ldw.map((q,m)=>Math.abs(q-a.core.s[m]*E.ldw_rate)>0.01?m:null).filter(x=>x!=null);
 const st=T.getState();const p1=JSON.stringify(T.budget().B);T.setState(Object.assign({},st,{showDirt:!st.showDirt}));const p2=JSON.stringify(T.budget().B);T.setState(st);res.t6=p1===p2?[]:['x'];
 const SUMS={14:[8,9,10,11,12,13],38:[33,34,35,36,37],78:[72,73,74,75,76,77],89:[85,86,87,88]};let f7=[];
 for(let m=0;m<12;m++){Object.keys(SUMS).forEach(k=>{const t=SUMS[k].reduce((x,r)=>x+((B[r]||[])[m]||0),0);if(Math.abs(t-B[k][m])>0.01)f7.push(k+'/'+m);});
  if(Math.abs(B[82][m]-(B[14][m]-B[18][m]-B[30][m]-B[38][m]-B[69][m]-B[78][m]))>0.01)f7.push('82/'+m);
  T.FIXED.forEach(r=>{const p=SRC.find(x=>x.row===r);if(Math.abs((B[r][m]||0)-((p&&p.m[m])||0))>0.01)f7.push('f'+r);});
  if(Math.abs(B[72][m]-a.rent[m])>0.01||Math.abs(B[16][m]-(a.coach[m]+a.aid[m]))>0.01||Math.abs(B[13][m]-(a.core.s[m]+a.gap[m]))>0.01)f7.push('line/'+m);}
 res.t7=f7;
 // release 4 test 1: at start every line equals Rick's r5 PRU-pl within $1 a month (only when the plan is at its start state)
 if(START){let f8=[];SRC.forEach(p=>{if(p.row===21||p.m.every(x=>x==null))return;p.m.forEach((x,m)=>{if(Math.abs(((B[p.row]||[])[m]||0)-(x||0))>1)f8.push(p.row+'/'+m);});});res.t8=f8;}else res.t8=[];
 // release 4 test 3: Salaries = Rick's row 33 every month, under a changed plan
 {const st=T.getState();T.setState(Object.assign({},st,{price:{'2-Wheel':420}}));const B2=T.budget().B;T.setState(st);const r33=SRC.find(x=>x.row===33);res.t9=B2[33].map((q,m)=>Math.abs(q-(r33.m[m]||0))>0.01?m:null).filter(x=>x!=null);}
 return res;}
let START=true;const T=window.__PRU_TEST__;const n=r=>{const o={};for(const k in r)o[k]=r[k].length;return o;};const clean=n(run(T));
const R3=T.R3,pl={},st=T.getState();
let u=T.UNITS[0];const m0=u.m0[3];u.m0[3]=m0+1;pl.t1=run(T).t1.length>0;u.m0[3]=m0;
T.setState(Object.assign({},st,{price:{'3-Wheel':390}}));pl.t2=run(T).t2.length>0;T.setState(st);
const cc=R3.coach['3-Wheel'][1];R3.coach['3-Wheel'][1]=cc+1;pl.t3=run(T).t3.length>0;R3.coach['3-Wheel'][1]=cc;
const w=R3.weekends26.Stafford.weekends;R3.weekends26.Stafford.weekends=w+1;pl.t4=run(T).t4.length>0;R3.weekends26.Stafford.weekends=w;
const lr=E.ldw_rate;E.ldw_rate=lr*1.01;pl.t5=run(T).t5.length>0;E.ldw_rate=lr;
pl.t6=(()=>{const d=T.dirtCalc(),b=T.budget();return JSON.stringify(b.B)!==JSON.stringify(T.budget(b.sales.map((q,m)=>q+d.s[m])).B);})();
const fx=T.PL.find(p=>p.row===60);const f0=fx.m[4];fx.m[4]=f0+5;pl.t7=run(T).t7.length>0;fx.m[4]=f0;
const fy=T.PL.find(p=>p.row===24);const g0=fy.m[4];fy.m[4]=g0+5;pl.t8=run(T).t8.length>0;fy.m[4]=g0;
T.FIXED.delete(33);pl.t9=run(T).t9.length>0;T.FIXED.add(33);
const after=n(run(T));const b=T.budget(),a=b.agg;
window.__selftest={clean,pl,after,st:T.SELFTEST.worst,cls:s(a.cls),n:Math.round(s(a.core.n)),fees:Math.round(s(a.core.s)),sales:Math.round(s(b.B[13])),cos:Math.round(s(b.B[16])),sal:Math.round(s(b.B[33])),coach:Math.round(s(a.coach)+s(a.aid)),at:Math.round(s(b.B[103])),rent:Math.round(s(b.B[72])),op:Math.round(s(b.B[82])),warn:(document.querySelector('.warn')||{}).innerText||''};
})();
