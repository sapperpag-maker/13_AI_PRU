// Angie's own test 18 (Sergio's Q38, 2026-11-20: "Each figure on its own"): every printed figure equals its own exact figure rounded,
// read off the screen: the plan tab's "2027 by month" table, the budget tab's coach and rent tables, and the P&L in all three views
// (Rick's view against his PRU-pl rows, the Difference view against plan minus Rick); start state and 6 edited states.
// It replaces test 9 (rows add up to their totals), which Q38 retired.
window.__r17 = async function () {
  const T = window.__PRU_TEST__, D = document, fails = [], wait = () => new Promise(r => setTimeout(r, 80)), s = a => a.reduce((p, q) => p + q, 0);
  let cells = 0;
  // Sergio's Q40: halves round away from zero (-2.5 shows -3), after the float error of an exact half is removed
  const hz = (e, k) => { const a = Math.round(Math.abs(e) * k * 1e6) / 1e6, r = Math.floor(a + 0.5) / k; return e < 0 ? -r : r; };
  const num = td => { let t = td.textContent.trim(); if (t === '–' || t === '') return 0; const neg = /^-/.test(t); t = t.replace(/[-+$,]/g, ''); const v = parseFloat(t); return neg ? -v : v; };
  const rowOf = (card, label) => [...card.querySelectorAll('tr')].find(r => r.cells[0] && r.cells[0].textContent.trim().startsWith(label));
  function cmp(tag, tr, ex, k, off) { if (!tr) { fails.push('t18 ' + tag + ': row not found'); return; }
    const c = [...tr.cells].slice(off || 1); const want = ex.concat([s(ex)]);
    want.forEach((e, i) => { cells++; const got = num(c[i]), w = hz(e, k); if (Math.abs(got - w) > 1e-6) fails.push('t18 ' + tag + ' ' + (i < 12 ? i : 'year') + ': shown ' + got + ', exact ' + e.toFixed(2)); }); }
  async function one(tag) {
    const b = T.budget(), a = b.agg, sales = a.core.s.map((q, m) => q + a.gap[m]);
    T.setTab('plan'); await wait();
    const fc = [...D.querySelectorAll('.card')].find(c => /2027 by month/.test(c.textContent));
    cmp(tag + ' classes', rowOf(fc, '2027 classes'), a.cls, 10); cmp(tag + ' students', rowOf(fc, '2027 students'), a.core.n, 1);
    cmp(tag + ' fees', rowOf(fc, '2027 class fees'), a.core.s, 1); cmp(tag + ' LDW', rowOf(fc, 'Loss Damage Waiver'), a.ldw, 1);
    cmp(tag + ' other', rowOf(fc, 'Other four parts'), a.other, 1); cmp(tag + ' sales', rowOf(fc, '2027 sales'), sales, 1);
    T.setTab('budget'); await wait();
    const cc = [...D.querySelectorAll('.card')].find(c => /Coach cost/.test(c.textContent));
    Object.keys(a.byType).forEach(t => cmp(tag + ' coach ' + t, [...cc.querySelectorAll('tr')].find(r => r.cells[0] && r.cells[0].textContent.trim().startsWith((t === 'First Ride' ? 'First Ride (IME)' : t) + ':')), a.byType[t].coach, 1));
    cmp(tag + ' COS', rowOf(cc, 'Cost of Sales'), a.coach.map((q, m) => q + a.aid[m]), 1);
    const rc = [...D.querySelectorAll('.card')].find(c => /Rent by range/.test(c.textContent));
    T.R3.sites.forEach(st => { const tr = rc.querySelector('tr[data-s="' + st + '"]'); if (tr) cmp(tag + ' rent ' + st, tr, a.rentBy[st], 1, 4); });
    cmp(tag + ' rent total', rowOf(rc, 'Rent'), a.rent, 1, 4);
    const pc = () => [...D.querySelectorAll('.card')].find(c => /P&L by month/.test(c.textContent));
    const views = [['plan', '2027 with the plan', r => b.B[r]], ['rick', "Rick's budget", r => T.PL.find(p => p.row === r).m.map(x => x || 0)], ['diff', 'Difference', r => b.B[r].map((q, m) => q - (T.PL.find(p => p.row === r).m[m] || 0))]];
    for (const [v, lab, ex] of views) {
      const btn = [...pc().querySelectorAll('[data-v]')].find(x => x.textContent.trim() === lab); btn.click(); await wait();
      const trs = [...pc().querySelectorAll('tr')].filter(r => r.cells.length >= 14);
      // P&L rows in page order, matched in order to the PL rows that are shown (non-head rows)
      const rows = T.PL.filter(p => b.B[p.row]); let i = 0, hit = 0;
      trs.forEach(tr => { const lab0 = tr.cells[0].textContent.trim(); if (lab0 === 'Line' || /margin %/.test(lab0)) return;
        let j = i; while (j < rows.length && !lab0.startsWith(rows[j].label)) j++;
        if (j < rows.length) { cmp(tag + ' P&L ' + v + ' ' + rows[j].label, tr, ex(rows[j].row), 1); i = j + 1; hit++; } else fails.push('t18 ' + tag + ' P&L ' + v + ': no P&L row for "' + lab0 + '"'); });
      if (hit < 20) fails.push('t18 ' + tag + ' P&L ' + v + ': only ' + hit + ' rows matched');
    }
    const btn = [...pc().querySelectorAll('[data-v]')].find(x => x.textContent.trim() === '2027 with the plan'); btn.click(); await wait();
  }
  T.setState({}); await one('start');
  for (let i = 0; i < 6; i++) { T.setState({ fillAll: [7, 20, 40, 63, 88, 100][i], price: i % 2 ? { '2-Wheel': 401 + i } : {}, rate: i % 3 ? { Stafford: 611 + i } : {} }); await one('fill' + [7, 20, 40, 63, 88, 100][i]); }
  T.setState({}); T.setTab('plan');
  return { cells, fails };
};
