# Job 17 r3, the planner repair: Angie's own tests (2026-11-27, full-auto run). Not a verdict; only Sergio accepts.

Bench: `C:\AI_Building\AI_MISC\06 Benches\2026-11-26 PRU cancelled classes out - ANGIE-HOME-J17\planner\`. Decisions D5 and D6: `DECISIONS.md` there.

## Why a repair
Blind checker r2 (`CHECKER r2\FINDINGS.md`) failed the planner on 4 findings: the weekends and classes per range, the 2026 2-Wheel student count, no left-out count on the page, and the goal check's half-class stop.

## The build
`j17_planner_r3.py` (00567e7d) builds `page_after_r3.html` (0f526ae7, 158,272 bytes) from the live page 410b33df. It makes 14 changes (`build_r3.txt`): the 13 of r2, plus:
- r3.weekends26: Newport News 48/97 to 47/96, Woodbridge 37/81 to 37/80 (`disc_check.py`: Newport News held no other class that weekend; Woodbridge held 2).
- r3.students2W26: 3942 to 3941.
- One note sentence: 9 cancelled 2026 classes in the Demand Analysis, 2 of them taken out here, their fees stay in.
Neither booking has a discount code or amount, so the discount claims are unchanged.

## Tests (`j17_planner_tests_r3.py` 55e164a8, `tests_r3.txt` 5439ac5a): TEST: PASS
- 17 numbers moved, each by -1; no fee moved.
- Outside the data, only the one sentence changed.
- The default download: Woodbridge First Ride April 1 to 0, and the range total 13 to 12.
- SELFTEST worst 7.28e-12. The console shows no errors.

## The goal check (`goal_check_r3.txt` ef051574)
Check 4 PASSES with 0 months over. The RESULT is still STOP, on his 16 half classes (D5, parked).

## 2027, before and after (`sales_gp_r3.csv` 23dbc377)
- Sales and gross profit are the same as in r2: sales -$278.19, gross profit -$203.19.
- Operating profit is +$110.33 and after taxes +$81.65, because the rent per class follows the weekends fix.

## Checker r3 (`CHECKER r3\FINDINGS.md`): FAIL, the second failed check
- F1: the discounts note still reads "3,925 2-Wheel and HD, plus 17", which adds to 3,942. My tests didn't cover that text.
- F2: the half classes.
The planner stopped and went to Piston (R-1917). It does not go to LAWYER, and Rick is not sent the new plan.
