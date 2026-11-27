# Job 17 r4, the planner after his answer to 65: Angie's own tests (2026-11-27). Not a verdict; only Sergio accepts.

Bench: `C:\AI_Building\AI_MISC\06 Benches\2026-11-26 PRU cancelled classes out - ANGIE-HOME-J17\planner\`.

## Why r4
His answer to 65, Angie's chat, 2026-11-27: "Round the half classes up". It settles checker r3's F2. r4 also fixes checker r3's F1.

## The build
`j17_planner_r4.py` (aff26fa7) builds `page_after_r4.html` (cb153273, 158,349 bytes) from `page_after_r3.html` (0f526ae7). It makes 5 changes (`build_r4.txt`):
- The default plan opens the 4 First Ride half classes as 1: Manassas Mall and Woodbridge, March and October. The start values from Class Data stay as they are.
- The discounts note reads "3,924 2-Wheel and HD, plus 17". Its parts now add to the 3,941 it shows.

## Tests (`j17_planner_tests_r4.py` febbd4f8, `tests_r4.txt` 17a80bdc): TEST: PASS
- The 4 data blocks are byte-equal to r3. Outside them, only the one note number changed.
- In the default plan, only those 4 cells moved, and Woodbridge First Ride April stays 0.
- In the download, 5 class rows moved. The 2 First Ride rows and the 2 range totals rose 0.5 in March and October. The Summary plan total rose 1.
- No class cell is a half.
- A red control (r3 against itself) fails 6 tests.
- SELFTEST is worst 7.28e-12, the same as before.

## The goal check (`goal_check_r4.txt` 7ada147e)
RESULT: PASS. Check 1: 600 cells, 0 not whole. Check 4: 0 months over.

## 2027 Summary, the live page's default plan against r4 (`sales_gp_r4.csv` 0bcb65b8)
| Year line | Before | After | Change |
|---|---|---|---|
| Total Sales | 2,011,581.60 | 2,011,791.21 | +209.61 |
| Gross Profit | 1,404,211.60 | 1,404,346.21 | +134.61 |
| Operating Profit (Loss) | 333,123.77 | 332,861.32 | -262.46 |
| After income taxes | 238,565.12 | 238,370.91 | -194.22 |

r3 against r4 alone (`sales_gp_r3_to_r4.csv`): sales +487.80, gross profit +337.80, March and October only.
