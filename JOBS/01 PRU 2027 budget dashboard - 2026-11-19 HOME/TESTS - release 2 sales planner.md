# Angie's own tests - planner release 2 (for LAWYER, rule R-1905-HOME-IYKK)

Page tested: `C:\AI_Building\AI_PRU\JOBS\01 PRU 2027 budget dashboard - 2026-11-19 HOME\PRU 2027 Sales Planner - DRAFT.html`. The tests below ran on the first build (md5 4e18d46f…, 2026-11-20). The sandbox wording test ran on a bench build between the two. The live build is md5 49a03ed793ab15fa4e9869e20dfdfb2b. Angie did not re-run the first-build tests on it, except as the last section says. The tests ran in the browser at http://localhost:8766/preview.html through `window.__PRU_TEST__`.

Data tested with:
- `C:\Users\Sergio\Downloads\2026 PRU Manual Log v3.xlsx` (md5 ab99689da045431d30dda84f57000c76): sheet "WklyConsolidating Wd", read by `C:\AI_Building\AI_MISC\06 Benches\2026-11-20 PRU job 01 planner - ANGIE-HOME\extract_weekly.py` into `weekly_by_range.json`.
- `C:\AI_Building\AI_Financials\04 Budget\2027\rolled\02 - Consolidated SGP Budget light.xlsx` (md5 64e3c1ecdf01ee25cae717657952bfbe): sheet PRU-pl, rows 7-103, in `pl2027.json`.
- Classes held in 2026, from sheet Master (class codes only), in `classes2026.json`.

Results:
1. At Rick's own Training, every P&L line equals PRU-pl: the worst difference is $0.0000000000018, every month. PASS.
2. Totals add up line by line at the plan's sales and at twice Rick's sales: 0 faults. PASS.
3. The fixed lines (27, 60, 62, 73, 76, 85-88, 93, 94, 98) equal Rick's at twice his sales: 0 faults. Cost of sales scales: $915,718 against Rick's $457,859. PASS.
4. Planted faults are caught: $5 added to row 69 in April is flagged at 69 and 80; Insurance - Other changed in March is flagged. PASS.
5. Pay per class at $600 gives Salaries $343,800, equal to 316,299 × 600 / 552.005. PASS.
6. A rent typed for one range and month (Chesapeake January, $1,000) changes that one cell only. PASS.
7. An initiative switched on adds its sales to Training ($1,585,828 to $1,655,628) and its classes × pay to Salaries. Switched off, the P&L is identical to before. PASS.
8. All five tabs render, the theme switch works, and there are no console errors. PASS.
9. With browser storage blocked, as on ONE VIEW, the page works and says "Inputs are not saved here; they clear when the page reloads." PASS.

Checked again on the live build (md5 49a03ed7…), after the blind check's round 1: the 2026 totals are 4,540 students and $1,583,953; +10% growth gives 4,994; the self-test's worst difference is $1.8e-12; saving $600 pay per class shows no false banner; --bad is #FF7A2E. PASS.

Blind check verdicts: `C:\AI_Building\AI_MISC\06 Benches\2026-11-20 PRU job 01 planner check - ANGIE-HOME\VERDICT.md` (round 1 FAIL, 5 findings) and `VERDICT-2.md` (round 2 PASS).
