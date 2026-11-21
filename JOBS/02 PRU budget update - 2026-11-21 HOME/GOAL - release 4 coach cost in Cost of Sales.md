# GOAL - job 02 release 4: coach cost moves to Cost of Sales

Drafted by Angie (R-1879), for Sergio's yes before the build. Everything not named here stays as in release 3's goal, `C:\AI_Building\AI_PRU\JOBS\01 PRU 2027 budget dashboard - 2026-11-19 HOME\GOAL - release 3 sales planner.md`, accepted 2026-11-20.

## Why
- His Q49, 2026-11-21: "Yes, match the books (Recommended)".
- The GL puts PRU coach pay in Cost of Sales, not Salaries: `C:\AI_Building\AI_Financials\00 Raw data\GL\2026 YTD 101E GL History Detail Postings - All Accounts.csv` (md5 94ae1ff9), store POW, accounts ending -30. Cost of Sales 66xxx/67xxx = $357,364.35, of which the per-class coach accounts 660xx and 661xx = $324,891.25. Counted by Angie on 2026-11-21; Rick counted the same.

## What changes
1. **Rick's workbook** becomes `C:\AI_Building\AI_Financials\04 Budget\2027\2026-11-21 PRU and Consolidated Books from the planner - rick RICK-HOME-2bd93960\work\04 PRU GP rebuilt.xlsx` (md5 3717f2bb, LAWYER PASS round 5), sheet PRU-pl. It replaces the light file (64e3c1ec). The 2026 base (column AB, row 13 and row 121) reads the same $1,651,117.18.
2. **Cost of Sales (row 16)** = coach cost + range aid, each month, computed as release 3's item 7 says. Total Cost of Sales (row 18) and Gross Profit (row 20) are recomputed from it.
3. **Salaries & Wages (row 33)** = Rick's own figure ($316,298.88), held fixed like the other fixed lines.
4. Rent (row 72) stays the planner's, as in release 3.
5. Every other line keeps release 3's rule ("Hold fixed costs"; variable lines move by plan sales / Rick's Training).

## The test
1. With every input at its start value, every line of the 2027 Budget tab equals the new PRU-pl, column by month, within $1. That includes Training $1,779,595.12, Cost of Sales $494,505, Salaries $316,298.88, Rent $155,992.29 and after-tax $210,288.99.
2. Cost of Sales = coach cost + range aid, each month, recomputed independently.
3. Salaries equals Rick's row 33 in every month, whatever the plan does.
4. Release 3's tests 1-6 still pass. Test 7's line check now reads row 16, not row 33, for coach cost.
5. Each test fails on a planted fault before it is believed.

Then: my own test, one blind check by an agent that did not build it (R-1875), LAWYER (R-1877), Sergio's accept, and the Brain puts it live.
