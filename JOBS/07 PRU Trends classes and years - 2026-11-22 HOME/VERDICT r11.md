FAIL

# Blind check r11, PRU job 07, draft-k.html

Target: `C:\AI_Building\AI_MISC\06 Benches\2026-11-22 PRU job 07 Trends - ANGIE-HOME-T7\draft-k.html`, md5 a4fe8bcf6833445a2e83021fc8fde176.
Goal: `C:\AI_Building\AI_PRU\JOBS\07 PRU Trends classes and years - 2026-11-22 HOME\GOAL.md`.
Written before opening any earlier verdict, checkpoint, LOG.md, vb_*.py, apply_q112.py or diff_k.py.

## Finding (1)

**F1. The 2026 Classes view counts classes in the wrong month under the goal's written rule, in 5 months.**
- Rule: GOAL.md line 28: "A class is one class code, counted in the month of its week." Test 2 (line 34): the monthly count equals `classes2026.json`, "or each difference is named".
- Page: draft-k.html, Trends, Classes, All ranges (`classSeries`, line 294, from `master26.fill`) counts by class date: Jan-Dec 5, 20, 60, 60, 78, 60, 54, 58, 52, 45, 29, 52 (573).
- Master, month of the week (column E), my count: 4, 12, 69, 60, 78, 60, 54, 58, 52, 38, 36, 52 (573). This equals the page's own `classes2026` list in every month.
- Off: Jan +1, Feb +8, Mar -9, Oct +7, Nov -7. 17 classes sit in another month. 19 of 97 range-month class figures differ, across 6 ranges.
- The page does not name these differences. It uses `classes2026` only for its year total (line 370).
- GOAL.md line 5 (Q79) moves "students and sales" to the class date. It does not name classes. If Sergio did decide classes go by class date, the repair is to write that into GOAL.md and name the differences; I found no such line in the goal.

## Questions, not findings

- **Q1. 2024 students: 4,952 or 4,991.** The page shows 4,952 (log, sheet 2024, AA1154, sum of the months). The log's year total is 4,991 (sheet 2024, E1254; 2025 Summary, T49). The 39 are the Other row (sheet 2024, E1251), which has no month split. Goal test 1 holds the figure to release 4, so it is not a wrong figure, but the page does not mention the 39.
- **Q2. Q109 and Q112.** Q109 says the 2027 budget does not move. Q112 moves it: Rent falls $562.66, after-tax profit rises $416.37. I applied Q112 as the later and specific decision, as the launch states. GOAL.md line 7 and test 6 do not yet carry that exception.

## Risk, not a FAIL

- **R1.** The page declares no character set. Served by the preview (`text/html`, no charset) it decodes as windows-1252, so dashes, × and · print garbled. Release 4 has the same gap. No figure changes.

## What passed

- **Virginia Beach weekends:** 32 distinct Sundays in 2026, counted from Master (VABEACH, VABEACH2, VABEACH3 as one site; shared code to the site of its first row). Page: 32 weekends, 67 classes. The 2 shared codes add no Sunday. All 9 sites' weekends and classes equal my count.
- **Rent:** 61 classes x 32 / 67 x $618 = $18,005.01 for Virginia Beach. Every site and month equals the formula (largest difference under $0.000001). Total $155,429.64, on P&L row 72, through rows 78, 80, 82, 91, 96, 100, 101, 103.
- **Against release 4:** only those 9 P&L rows move, and only Virginia Beach's rent: -$562.66. Plan students, sales, coach, classes and Dirt Bike are unchanged. `src-data`, `src-pl`, `plan-state` are identical.
- **Tie-out, default view:** 165 figures listed, 165 tied, 0 OFF, 0 NO SOURCE, 0 ERROR (`tieout.csv` rows). tie_out.py md5 a8f90d601cfd855442b16d39765a9cea.
- **2026 from Master:** students 4,606, fees $1,602,640, all 20 lines by month: 0 cells differ. Classes by site, type and month against `master26.fill`: 0 keys differ under the class-date count.
- **Goal 1, 3, 4, 5:** only 2024-2026 plus 2027B; year buttons clicked, the last year stays on, the table's list follows; 2024 and 2025 classes show "not available" in legend and table; each class filter clicked.
- **Goal 2:** smallest pair contrast 1.62 dark, 1.63 light; smallest against the card 3.32 dark, 3.61 light.
- **Goal 6, Dirt Bike:** start $30,816; edits move rows by the formulas; a 0-weekend month has no class or cost; P&L does not move; state restored. Set through the page's state hook, not typed into inputs; the Reset button was not clicked.
- **Goal 7, 2027B:** 480 range-class-month cells, 0 off; totals equal the plan (4,455.29 students, $1,706,910.41, 498 classes); a 50% fill moves it to 2,983 on both.
- **Goal 8:** no "2027 vs 2026" tab.
- **Test 5:** 0 class codes, emails or phone numbers in the page.

## What I did not check

- Figures outside the default view through tie_out.py (Sales $, Classes, plan, New initiatives, P&L). These were checked by the separate recounts above, or against release 4 only.
- P&L lines against GL accounts. The default view has no GL-based line.
- 161 of the 165 tied figures tie to my own `recount.xlsx`, built from the sources, because no single source cell holds them.
- 2024 and 2025 by month against the log, beyond equality with release 4 and the year totals.
- Class Data's 2027 inputs and the 2027 rent table against their sources.
- The 2027B and Dirt Bike screens by eye; the chart's drawn line positions; the light theme's rendering beyond its colors.
- Whether Sergio decided elsewhere that classes go by class date: LOG.md was closed to me.

## My mistakes

- `survey.py` printed Master rows 2 and 3 with their site and course (class code and date masked). That breaks the launch's limit on printing a site-course pair of a single class. It went only to this session's screen, not to any file.
- First tie-out run had 11 rows not TIED from my own inputs; fixed and rerun, first run kept as `tieout-run1-checker-input-faults.csv`.
