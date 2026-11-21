// Angie's own test 19 (Sergio's Q40, 2026-11-20: "Fix halves, go to LAWYER"): every display formatter rounds halves
// away from zero, as Excel shows them, and an exact half carried with float error (x.4999999) still rounds up.
// The vs and trends Change and Change % cells print through fmtN, fmtD, fmtP and fmtPC; round 18 found 14 such cells.
window.__r19 = function () {
  const F = (window.__PRU_TEST__ || {}).fmt, fails = [];
  if (!F) return { fails: ['t19: the page exposes no formatters'] };
  const eq = (nm, got, want) => { if (got !== want) fails.push('t19 ' + nm + ': shown "' + got + '", want "' + want + '"'); };
  eq('fmtN 2.5', F.fmtN(2.5), '3'); eq('fmtN -2.5', F.fmtN(-2.5), '-3'); eq('fmtN -1234.5', F.fmtN(-1234.5), '-1,235');
  eq('fmtN 0.1+0.2+2.2 (2.5 in float)', F.fmtN(0.1 + 0.2 + 2.2), '3'); eq('fmtN 1.005*1000-0.5', F.fmtN(1.005 * 1000 - 0.5), '1,005');
  eq('fmtN -0.4', F.fmtN(-0.4), '0'); eq('fmtN -0.5', F.fmtN(-0.5), '-1');
  const d = F.fmtD(-2.5); if (!/3/.test(d) || /2/.test(d)) fails.push('t19 fmtD -2.5: shown "' + d + '"');
  eq('fmtP -2.5', F.fmtP(-2.5), '-3%'); eq('fmtP 2.5', F.fmtP(2.5), '+3%');
  eq('F1 0.25', F.F1(0.25), '0.3'); eq('F1 -0.25', F.F1(-0.25), '-0.3'); eq('F1 4.35', F.F1(4.35), '4.4'); eq('F1 1.45', F.F1(1.45), '1.5');
  eq('fmtF 12.25', F.fmtF(12.25), '12.3%');
  eq('fmtPC -2.5,-0.25', F.fmtPC(-2.5, -0.25), '-0.3%'); eq('fmtPC 10,2.5', F.fmtPC(10, 2.5), '+3%');
  // the same rule over a sweep of halves, both signs, against an integer-only reference
  for (let i = -500; i <= 500; i++) { const v = i + 0.5, want = (v < 0 ? -1 : 1) * Math.floor(Math.abs(v) + 0.5);
    if (F.RH(v) !== want) { fails.push('t19 RH(' + v + ') = ' + F.RH(v) + ', want ' + want); break; } }
  for (let i = -500; i <= 500; i++) { const v = (i * 10 + 5) / 100, want = (v < 0 ? -1 : 1) * Math.floor(Math.abs(i * 10 + 5) / 10 + 0.5) / 10;
    if (F.RH(v, 1) !== want) { fails.push('t19 RH(' + v + ',1) = ' + F.RH(v, 1) + ', want ' + want); break; } }
  return { fails };
};
