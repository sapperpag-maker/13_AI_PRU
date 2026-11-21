// Angie's own tests 10-12 (Piston's R-1876 pick, after round 13):
// 10: every fill box takes whole numbers 0-100 only (typed -20, 150, 72.46, 50.5; unit box -5)
// 11: coach count follows the students per class AS SHOWN (one decimal), every unit, fills 0, 100,
//     every whole fill near 6 students, and fill 50.1 typed in a unit box
// 12: P&L tags show only in the plan view
window.__r13 = function () {
  const T = window.__PRU_TEST__, D = document, fails = [];
  T.setTab('plan');
  const fa = D.querySelector('#f-all');
  const want10 = { '-20': 0, '150': 100, '72.46': 72, '50.5': 51 };
  for (const v in want10) { fa.value = v; fa.dispatchEvent(new Event('change'));
    const got = T.getState().fillAll; if (got !== want10[v]) fails.push('t10 all ' + v + ' kept ' + got); }
  T.setState({});
  const ub = D.querySelector('.in-f'); ub.value = '-5'; ub.dispatchEvent(new Event('change'));
  const uv = Object.values(T.getState().fillUnit)[0]; if (uv !== 0) fails.push('t10 unit -5 kept ' + uv);
  T.setState({});
  let n = 0;
  const row = k => D.querySelector('tr[data-k="' + CSS.escape(k) + '"]');
  const look = (u, label) => { const tr = row(u.key); if (!tr) { fails.push('t11 no row ' + u.key); return; }
    const sp = tr.querySelector('.in-f').closest('td').nextElementSibling.textContent.trim();
    const who = [...tr.children].map(c => c.textContent.trim()).find(x => x === 'one' || x === 'two');
    n++; if (who !== (+sp > 6 ? 'two' : 'one')) fails.push('t11 ' + u.key + ' ' + label + ' shown ' + sp + ' coach ' + who); };
  for (const u of T.UNITS) { const cap = T.R3.cap[u.type], fs = [0, 100];
    for (let f = 0; f <= 100; f++) { const s = cap * f / 100; if (s > 5.4 && s < 6.6) fs.push(f); }
    for (const f of fs) { T.setState({ fillUnit: { [u.key]: f } }); look(u, 'f' + f); }
    T.setState({}); const b = row(u.key).querySelector('.in-f'); b.value = '50.1'; b.dispatchEvent(new Event('change')); look(u, 'typed 50.1'); T.setState({}); }
  T.setTab('budget');
  const views = ['plan', 'rick', 'diff'], tags = {};
  for (const v of views) { const b = D.querySelector('[data-v="' + v + '"]'); if (b) b.click(); tags[v] = D.querySelectorAll('.tag').length; }
  if (!tags.plan) fails.push('t12 plan view shows no tags');
  if (tags.rick || tags.diff) fails.push('t12 tags in rick ' + tags.rick + ', diff ' + tags.diff);
  const b0 = D.querySelector('[data-v="plan"]'); if (b0) b0.click();
  T.setTab('plan'); T.setState({});
  try { localStorage.removeItem('pru-planner-draft-v3'); } catch (e) {}
  return { checked11: n, tags, fails };
};
