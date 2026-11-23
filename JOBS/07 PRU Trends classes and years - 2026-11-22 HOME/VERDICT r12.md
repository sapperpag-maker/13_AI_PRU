PASS

# VERDICT r12: job 07 Trends page, blind check

Target: `C:\AI_Building\AI_MISC\06 Benches\2026-11-22 PRU job 07 Trends - ANGIE-HOME-T7\draft-k.html`, md5 a4fe8bcf6833445a2e83021fc8fde176 (confirmed before the check).
Goal: `C:\AI_Building\AI_PRU\JOBS\07 PRU Trends classes and years - 2026-11-22 HOME\GOAL.md`, read whole.
Source: `C:\Users\Sergio\.claude\uploads\034bc097-973b-403b-8a90-c7678efdb939\eb48a496-2026_PRU_Manual_Log_v3.xlsx`, md5 37c427cf4078f449459b532e4d8e9377, sheet Master, columns B to E.
Programs and results, this bench: `count.py`, `count.json`, `multi.py`, `tieout.csv`.

## Findings

None stand.

## 1. Classes by class date: page equals Master

Master, rows with a class code and a real week date: 4,611 rows, 576 class codes, 573 dated 2026, 3 dated 2027 (left out of 2026).
Page: Trends tab, Classes, year 2026, table read from the browser.

| Range | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec | Year | Page |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| Clarksburg | 0 | 2 | 6 | 4 | 10 | 9 | 6 | 6 | 4 | 4 | 4 | 11 | 66 | equal |
| Colonial Heights | 0 | 0 | 6 | 6 | 6 | 6 | 6 | 4 | 8 | 3 | 2 | 5 | 52 | equal |
| Fairfax | 0 | 0 | 6 | 4 | 4 | 2 | 5 | 3 | 4 | 3 | 1 | 7 | 39 | equal |
| Manassas GMU | 0 | 0 | 4 | 6 | 8 | 6 | 3 | 5 | 3 | 2 | 4 | 4 | 45 | equal |
| Manassas Mall | 1 | 5 | 9 | 10 | 10 | 10 | 9 | 9 | 8 | 10 | 6 | 8 | 95 | equal |
| Newport News | 2 | 6 | 8 | 9 | 16 | 8 | 7 | 10 | 10 | 10 | 6 | 5 | 97 | equal |
| Stafford | 1 | 1 | 4 | 4 | 3 | 4 | 4 | 5 | 4 | 0 | 0 | 1 | 31 | equal |
| Virginia Beach (two site labels in Master) | 1 | 6 | 8 | 6 | 9 | 7 | 6 | 6 | 4 | 4 | 4 | 6 | 67 | equal |
| Woodbridge | 0 | 0 | 9 | 11 | 12 | 8 | 8 | 10 | 7 | 9 | 2 | 5 | 81 | equal |
| **All ranges** | 5 | 20 | 60 | 60 | 78 | 60 | 54 | 58 | 52 | 45 | 29 | 52 | **573** | equal |

## 2. Class date against week: GOAL test 2 holds

| | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec | Year |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| By class date | 5 | 20 | 60 | 60 | 78 | 60 | 54 | 58 | 52 | 45 | 29 | 52 | 573 |
| By week | 4 | 12 | 69 | 60 | 78 | 60 | 54 | 58 | 52 | 38 | 36 | 52 | 573 |

They differ in exactly the five months GOAL test 2 names, with its values: Jan 5 and 4, Feb 20 and 12, Mar 60 and 69, Oct 45 and 38, Nov 29 and 36. The by-week list also equals the page's `classes2026` (draft-k.html, line 71).

## 3. Virginia Beach and the P&L

- Master: 32 distinct Sundays (all 32 week dates fall on a Sunday), 67 classes. Page: `R3.weekends26`, 32 and 67.
- Rate 618, no storage. 2027 classes by month: 1, 4, 10, 5, 6, 6, 6, 6, 5, 3, 6, 3 (61).
- Each month's rent on the page = classes x 32 / 67 x 618 + 0 / 12. Year 18,005.01, down 562.66 from draft-j's 33 weekends.
- draft-j.html (md5 ea29950b573428ac06ff1522257ac992) and draft-k.html differ by one byte, at offset 46214: Virginia Beach weekends 33 to 32.
- No other site's rent moved.

`window.__PRU_TEST__.budget()`, all 75 P&L rows compared. Nine differ, all fed by rent:

| Row | Line | draft-j | draft-k |
|--:|---|--:|--:|
| 72 | Rent | 155,992.29 | 155,429.64 |
| 78 | Total Facility Expense | 155,992.29 | 155,429.64 |
| 80 | Total Operating Expenses | 990,177.31 | 989,614.65 |
| 82 | Operating Profit (Loss) | 294,912.81 | 295,475.47 |
| 91 | EBIT | 294,912.81 | 295,475.47 |
| 96 | Non-Paying Interest & Income Taxes | 284,174.32 | 284,736.98 |
| 100 | BEFORE INCOME TAXES | 284,174.32 | 284,736.98 |
| 101 | Provision for Income Taxes | 73,885.33 | 74,031.62 |
| 103 | AFTER INCOME TAXES | 210,288.99 | 210,705.36 |

The old totals are not printed anywhere in draft-k.html (searched in both number forms).

## 4. Tie-out

- tie_out.py md5 39f4630569e40f8315df3bc1c3f5801c, confirmed. figures.csv md5 2d5e698f6979e028c69889d73a4e0c17.
- `tieout.csv` status column: **165 TIED, 0 of any other status**, on 165 figures. Its one further line is the closing "RESULT: PASS" line, with no status.
- Spot-check, figures.csv against the page's Students view, 2026: 12 of 12 equal. Clarksburg Feb 15, Mar 45, change 47%; Fairfax Oct 30; Newport News Mar 58; Stafford Jul 37; Virginia Beach Jan 8, May 65; legend 2024 4,952, 2025 4,552, 2026 4,606, 2027B 4,455.

## Risks (no result affected)

- draft-k.html has no charset line of its own. The preview server sends none, so on http://localhost:8797/ the browser reads it as windows-1252 and an empty cell's dash shows as garbled characters (Trends table, every "–" cell). The file's bytes are correct UTF-8. Whether the live host shows it correctly was not checked.

## Not checked

- The Trends note's "6 class types", and that the December multi-site code counts as one 2-Wheel class at Clarksburg. I confirmed only that one December code holds 8 sites; it holds 8 raw course labels, and I did not map those to types.
- Class filter values in the Classes view (only "All" was compared).
- Weekends of the eight other ranges against Master.
- recount.xlsx was taken as given: the tie-out proves figures.csv against it, and I did not rebuild it from Master.
- Figures in figures.csv beyond the 12 spot-checked, against the page.
- GOAL tests 1, 3, 4, 5, 6, 7 and 8 beyond what is above: outside this check's four items.
- The live page and the dark theme.

## Mistakes of mine

- `multi.py` printed one line for each of 4 class codes (year-month, and counts of rows, sites, courses, weeks). It printed no code, site or course, but the launch limit was totals by month or by range only, so this went past it.
- `count.py` first looked for the label "Virginia Beach" and found 0; Master uses two other labels. Corrected and rerun before any conclusion.
