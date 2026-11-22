# PARKED: job 05, the tie-out program rebuilt to read stored numbers (NOT DONE)

Angie, 2026-11-22 HOME. Sergio's Q63: "Yes, rebuild it (Recommended)". Goal: `..\GOAL.md`.

## Why it stopped
The checker-FAIL path (program, new shape, smaller, stop) is spent: 2 FAILs on the new shape (r1, r2), then 2 on the smaller step (r3, r4).
- r4 (`VERDICT r4.md`, 10204c81), F1: float cells are cut to 15 digits half EVEN, not half up (tie_out.py line 214). Cell 1234567890123.125 ties to shown 1,234,567,890,123.12.
- r4, F2: the difference column is computed in a context that rounds without error (line 645). It affects only cells below about 1E-44, and the status is still right.
- Both bite only at the 15th significant digit; a 2-decimal money figure under 13 digits before the point is not reached. The rule still makes them FAILs.

## What is here
- tie_out.py 81e79f40, test_tie_out.py 303a8c10 (TESTS: PASS (430)).
- The verdicts r1-r4.

## What it needs from Sergio
A word to restart: fix r4's F1 (cut the exact float value half up, as ints are) and F2 (the difference in the trapping context), then one more check. Or leave it parked.
