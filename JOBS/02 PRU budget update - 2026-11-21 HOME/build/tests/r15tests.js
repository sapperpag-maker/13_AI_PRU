// Angie's own tests 13-14 (after blind round 15):
// 13: "Reset everything" brings back the start figures every time, not only the first: three rounds of price, rate,
//     month and fill edits, each followed by a reset (two clicks), and DEF must stay empty
// 14: no word runs into a number in any tab's text (the "start498" class), e.g. a letter straight before a digit or "$"
window.__r15 = async function () {
  const T = window.__PRU_TEST__, D = document, fails = [], wait = () => new Promise(r => setTimeout(r, 80));
  const sales = () => Math.round(T.budget().B[13].reduce((a, b) => a + b, 0));
  T.setState({}); await wait(); const s0 = sales();
  const reset = async () => { T.setTab('plan'); await wait(); const b = D.querySelector('[data-reset]'); b.click(); await wait();
    const b2 = D.querySelector('[data-reset]'); b2.click(); await wait(); };
  for (let round = 1; round <= 3; round++) {
    T.setTab('plan'); await wait();
    const p = D.querySelector('[data-price]'); p.value = String(399 + round * 10); p.dispatchEvent(new Event('change')); await wait();
    const f = D.querySelector('#f-all'); f.value = String(60 + round); f.dispatchEvent(new Event('change')); await wait();
    const st = T.getState(); const k = T.UNITS[0].key; st.unitMonths[k] = T.UNITS[0].m0.map(x => x + round); T.setState(st); await wait();
    T.setTab('budget'); await wait(); const r = D.querySelector('.in-rate'); if (r) { r.value = String(700 + round); r.dispatchEvent(new Event('change')); await wait(); }
    if (sales() === s0) fails.push('t13 round ' + round + ': edits did not move sales');
    await reset();
    const g = T.getState();
    const left = ['price', 'rate', 'unitMonths', 'fillType', 'fillUnit'].filter(x => Object.keys(g[x]).length);
    if (left.length || g.fillAll != null) fails.push('t13 round ' + round + ': after reset still edited: ' + left.join(',') + (g.fillAll != null ? ' fillAll' : ''));
    if (sales() !== s0) fails.push('t13 round ' + round + ': sales after reset ' + sales() + ' vs start ' + s0);
  }
  const IDS = ['trends', 'plan', 'vs', 'inits', 'budget'];
  for (const id of IDS) { T.setTab(id); await wait();
    const txt = D.body.innerText; const re = /[A-Za-z][0-9$]/g; let m;
    while ((m = re.exec(txt))) { const ctx = txt.slice(Math.max(0, m.index - 12), m.index + 12);
      let a = m.index, z = m.index; while (a > 0 && /\S/.test(txt[a - 1])) a--; while (z < txt.length && /\S/.test(txt[z])) z++;
      const tok = txt.slice(a, z).replace(/[(),.;:]+$/, '').replace(/^[(]+/, '');
      if (/^[0-9a-f]{8}$/.test(tok) || /^md5$/i.test(tok) || /_v\d\.xlsx$/.test(tok)) continue;
      if (/\b(?:[A-Z]{1,4}\d|20\d\d|Q\d|R-\d|[A-Z]\d{1,3}\b|md5|H\d|N\d|O\d|M\d|E\d|J\d|I\d|L\d|K\d|Y\d|AB\d|BRC2|BRCE|3WBR|IME|v3|x\d)/.test(ctx.slice(8, 20)) || /[A-Z]{2,}\d|BRC2|[A-Z]\d+[-–:]/.test(ctx)) continue;
      fails.push('t14 ' + id + ': "' + ctx.replace(/\s+/g, ' ') + '"'); } }
  T.setTab('plan'); T.setState({});
  try { localStorage.removeItem('pru-planner-draft-v3'); } catch (e) {}
  return { s0, fails };
};
