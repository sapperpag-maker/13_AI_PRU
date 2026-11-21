// Angie's own tests 15-17 (after blind round 16, Sergio's Q37 "Fix all 9, recheck"):
// 15: every shown total row and every row under it sits within 1 (0.1 for classes) of its exact figure, each month;
//     the six top totals equal the exact figure rounded; start state and 25 edited states
// 16: ARC's coach count reads the students per class shown on the plan tab (its 2026 students / its 2026 classes, Master sheet; after round 17)
// 17: the save line keeps its words after a tab switch (after Save, after an edit)
window.__r16 = async function () {
  const T = window.__PRU_TEST__, D = document, fails = [], wait = () => new Promise(r => setTimeout(r, 80)), s = a => a.reduce((p, q) => p + q, 0);
  const near = (nm, sh, ex, tol) => sh.forEach((q, m) => { if (Math.abs(q - ex[m]) >= tol - 1e-9) fails.push('t15 ' + nm + ' ' + m + ': ' + q + ' vs ' + (+ex[m]).toFixed(2)); });
  const top = (nm, sh, ex, k) => { if (Math.round(s(sh) * k) !== Math.round(Math.round(s(ex) * k * 1e6) / 1e6)) fails.push('t15 top ' + nm + ': ' + s(sh) + ' vs ' + s(ex).toFixed(2)); };
  function one(tag) {
    const b = T.budget(), a = b.agg, SP = T.shownPlan(a);
    const sales = a.core.s.map((q, m) => q + a.gap[m]), sal = a.coach.map((q, m) => q + a.aid[m]);
    near(tag + ' classes', SP.cls, a.cls, 0.1); near(tag + ' students', SP.n, a.core.n, 1); near(tag + ' fees', SP.fees, a.core.s, 1);
    near(tag + ' ldw', SP.ldw, a.ldw, 1); near(tag + ' other', SP.other, a.other, 1); near(tag + ' sales', SP.sales, sales, 1);
    near(tag + ' S&W', SP.sal, sal, 1); near(tag + ' rent', SP.rent, a.rent, 1); near(tag + ' aid', SP.aid, a.aid, 1);
    Object.keys(SP.type).forEach(t => near(tag + ' coach ' + t, SP.type[t].coach, a.byType[t].coach, 1));
    SP.U.forEach(x => { near(tag + ' n ' + x.u.key, x.n, x.p.n, 1); near(tag + ' c ' + x.u.key, x.c, x.p.cls, 0.1); near(tag + ' s ' + x.u.key, x.s, x.p.s, 1); });
    SP.C.forEach(x => { near(tag + ' n ' + x.c.key, x.n, x.p.n, 1); near(tag + ' s ' + x.c.key, x.s, x.p.s, 1); near(tag + ' coach ' + x.c.key, x.coach, x.p.coach, 1); });
    Object.keys(SP.rentBy).forEach(k => near(tag + ' rent ' + k, SP.rentBy[k], a.rentBy[k], 1));
    top(tag + ' classes', SP.cls, a.cls, 10); top(tag + ' students', SP.n, a.core.n, 1); top(tag + ' sales', SP.sales, sales, 1);
    top(tag + ' S&W', SP.sal, sal, 1); top(tag + ' rent', SP.rent, a.rent, 1);
    const P = T.shownPL((r, m) => b.B[r][m], { 13: SP.sales, 33: SP.sal, 72: SP.rent }), DER = [20, 80, 82, 91, 96, 100, 101, 103];
    T.PL.forEach(p => { const r = p.row; if (!P[r] || !b.B[r] || DER.includes(r)) return; near(tag + ' P&L ' + r, P[r], b.B[r], 1); });
    if (T.rfall && T.rfall()) fails.push('t15 ' + tag + ': ' + T.rfall() + ' tables fell back to row-by-row rounding');
  }
  T.setState({}); T.resetRfall && T.resetRfall(); one('start');
  let seed = 7; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
  for (let i = 0; i < 25; i++) {
    const st = { fillType: {}, fillUnit: {}, unitMonths: {}, price: {}, rate: {} };
    if (rnd() < 0.5) st.fillAll = Math.round(30 + rnd() * 70);
    T.UNITS.forEach(u => { if (rnd() < 0.2) st.fillUnit[u.key] = Math.round(rnd() * 100); if (rnd() < 0.15) st.unitMonths[u.key] = u.m0.map(x => Math.round((x + rnd() * 2) * 10) / 10); });
    ['2-Wheel', '3-Wheel', 'BRC2', 'First Ride', 'ARC', 'HD'].forEach(t => { if (rnd() < 0.3) st.price[t] = Math.round(150 + rnd() * 300); });
    T.R3.sites.forEach(x => { if (rnd() < 0.3) st.rate[x] = Math.round(300 + rnd() * 700); });
    T.setState(st); T.resetRfall && T.resetRfall(); one('edit' + i);
  }
  // 16
  T.setState({}); T.setTab('plan'); await wait();
  const arc = T.CARRIED.find(c => c.key === 'ARC'), tr = [...D.querySelectorAll('tr')].find(r => r.cells[0] && /^ARC/.test(r.cells[0].textContent.trim()) && r.cells.length >= 9);
  if (!tr) fails.push('t16: no ARC row on the plan tab'); else {
    const shown = tr.cells[4].textContent.trim(), who = tr.cells[8].textContent.trim(), ms = s(Object.keys(T.R3.fill26).filter(k => k.endsWith('|ARC')).map(k => s(T.R3.fill26[k].s))), want = (ms / s(arc.cls26)).toFixed(1);
    if (shown !== want) fails.push('t16: ARC students per class shown "' + shown + '", want ' + want);
    if (who !== (+shown > 6 ? 'two' : 'one')) fails.push('t16: ARC coach ' + who + ' for shown ' + shown);
    const ap = T.planAgg().car.find(x => x.c.key === 'ARC').p; if (ap.two !== (+want > 6)) fails.push('t16: model ARC two=' + ap.two + ' for ' + want);
  }
  // 17
  try { localStorage.removeItem('pru-planner-draft-v3'); } catch (e) {}
  T.setState({}); T.setTab('plan'); await wait();
  const stat = () => (D.querySelector('[data-status]') || {}).textContent || '';
  const f = D.querySelector('#f-all'); f.value = '45'; f.dispatchEvent(new Event('change')); await wait();
  const afterEdit = stat(); T.setTab('budget'); await wait(); T.setTab('plan'); await wait();
  if (stat() !== afterEdit) fails.push('t17: after an edit "' + afterEdit + '", after a tab switch "' + stat() + '"');
  D.querySelector('[data-save]').click(); await wait(); const afterSave = stat(); T.setTab('inits'); await wait();
  if (stat() !== afterSave) fails.push('t17: after Save "' + afterSave + '", after a tab switch "' + stat() + '"');
  let saved = null; try { saved = JSON.parse(localStorage.getItem('pru-planner-draft-v3')); } catch (e) {}
  if (!saved || !saved.saved) fails.push('t17: the saved draft carries no saved mark, so a reload cannot show "Saved"');
  try { localStorage.removeItem('pru-planner-draft-v3'); } catch (e) {}
  T.setState({}); T.setTab('plan');
  return { fails };
};
