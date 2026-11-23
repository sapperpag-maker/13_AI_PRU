FAIL

# Job 07 blind check, round r8

- Page: `C:\AI_Building\AI_MISC\06 Benches\2026-11-22 PRU job 07 Trends - ANGIE-HOME-T7\draft-h.html`, md5 2247437a339585a863de28527767f47c
- Goal: `C:\AI_Building\AI_PRU\JOBS\07 PRU Trends classes and years - 2026-11-22 HOME\GOAL.md`, md5 8a9b74d169416f5baa571b92fdbde055
- Baseline: `PRU 2027 Sales Planner - release 5.html`, md5 218637b509804e342cedabb9bc9b8e16
- Source: `C:\Users\Sergio\.claude\uploads\034bc097-973b-403b-8a90-c7678efdb939\eb48a496-2026_PRU_Manual_Log_v3.xlsx`, md5 37c427cf4078f449459b532e4d8e9377, sheet Master, columns B to E and J (J as sums)

Findings: 5. The numbers tie out. All five faults are in what the page says about them.

## Findings

### 1. The rounding explanation is on the one Trends view that does not need it
- Where: Trends, table, Year in table = 2027B, views Students and Sales $.
- Shown: rows that do not add to the printed All ranges total, with no explanation. Students, start state: Jun rows add to 541, total 540; Jul 480 vs 479; Sep 369 vs 370; Nov 255 vs 253. Sales $: 10 of 13 columns differ, for example Jan $24,013 vs $24,012 and Year $1,706,911 vs $1,706,910.
- Should be: the explanation on every view where 2027B rows can miss the printed total (repair item 3).
- Measured: the sentence beginning Rounding is built only in the Classes branch (`meas==="c"`, line 345). On screen: Students no, Sales $ no, Classes yes. Classes has 0 columns that miss. Over All and each class filter, columns that miss: Students 16 of 84, Sales $ 25 of 84, Classes 0 of 60.

### 2. The Sources line leaves out Master as a base of the 2027 budget
- Where: foot of every tab, line 283.
- Shown: tab Master for the 2026 students, sales and classes on Trends and the 2026 student comparison on the plan, by class date; tab WklyConsolidating Wd as the base of the 2027 budget.
- Should be: it also names Master, by week, as part of the 2027 budget base, and Master by class date for the plan's Months panels. GOAL.md names the base as the log's weekly summary, and Master by week.
- Measured: the plan's own note says the start fill is Manual Log, Master sheet, by week, as set for the 2027 budget. `R3.fill26` (start fill, students per class) and `R3.students2W26` come from Master codes. The plan's Months panels read `M26.fill`, Master by class date, and the line does not name them.

### 3. The discount note calls 3,942 students 2-Wheel and HD; 17 of them are neither
- Where: 2027 plan tab, Discounts card, note.
- Shown: 3,942 2026 2-Wheel students, HD included (Manual Log, Master sheet, by week, the 2027 budget base).
- Should be: a description that fits the figure. It also holds the other students of the one December multi-site class code.
- Measured from Master, week rows with a 2026 class date: 2-Wheel 3,877 + HD 48 = 3,925. The December code also holds 8 3-Wheel, 2 BRC2, 4 First Ride and 3 ARC = 17. 3,925 + 17 = 3,942. The same 17 are missing from the base's other types: 3-Wheel 446 vs 454, BRC2 135 vs 137, First Ride 75 vs 79, ARC 8 vs 11.

### 4. The Budget tab prints the 2027 budget base without labeling it
- Where: 2027 Budget (P&L) tab: coach note, rent note, rent table header.
- Shown: ARC: its 2026 students ÷ its 2026 classes on the Master sheet; 2026 (Manual Log), Master; Weekends / classes 2026 (Manual Log).
- Should be: labeled as the 2027 budget base. GOAL.md: Where the page prints that base, it is labeled as the 2027 budget base.
- Measured: ARC's 2026 students in that ratio are 8 (`R3.fill26`), while Trends shows ARC 2026 at 11 students, and Master counts 11. The plan tab labels the same 8 as the budget base; the Budget tab does not.

### 5. The page does not say the December class is counted as a 2-Wheel class
- Where: Trends, Classes view, with the Class filter; plan table note; plan Months panels.
- Shown: One December class code holds students at 8 sites; it counts as one class, at Clarksburg. Only the HD student in it is mentioned.
- Should be: the page also says the class counts under 2-Wheel, so its other class types show students with no class (repair item 4).
- Measured: the code holds 2-Wheel 27, 3-Wheel 8, ARC 3, BRC2 2, First Ride 4, HD 1 (45 students). My count matches the page only when the class is put under 2-Wheel at Clarksburg. With the filter on BRC2, December shows 2 students and 0 classes. Months panels with students and 0 classes in December: Stafford 3-Wheel 1, Woodbridge 3-Wheel 1.

## What passed

- A. 2026 students, fees and classes on Trends against my own Master count: 4,356 cells (every range and class, plus totals, by month), 0 differences. Totals 4,606 students, $1,602,640 fees, 573 classes.
- Plan Months panels against my count, 19 of 20 site and class rows: 228 month cells, 0 differences. The 20th, Clarksburg BRC2, has no 2026 row and my count is 0.
- Repair item 2: HD-only classes are 6, all at Manassas GMU, and are out of 2-Wheel (456 2-Wheel classes). Matches Master by range and month.
- C. 2027 unchanged: 11 scenarios (start, fill all, by type, by site, price, rent, months, Dirt Bike, Dirt Bike off, mixed, fill 0) on plan, New initiatives, and Budget in all three P&L views. Each scenario differs from release 5 on the same 14 lines, all labels or 2026 comparison lines:
  1. plan KPI 2027 students (2026 comparison 4,543 to 4,606, and its percent)
  2. plan fill note
  3. plan table fill header
  4. ARC carried row label
  5. five-parts row label
  6. plan table note
  7. discount note
  8. 2026 registrations row label
  9. 2026 gap row label
  10 to 14. Sources line on plan, New initiatives and the three P&L views
- 2024 and 2025 equal release 5: 6,912 cells, 0 differences.
- D. Shown text, tooltips included, over every tab, view, class and year: 3,380 strings. No quotation marks, his/him/he, my pick or office names. No email, phone or class code in the page file. The scan was shown to fire on planted text.
- E. Year buttons, legend, table list, last year cannot go off, not available for 2024, 2025 and classes with no figure, dashed 2027B, class filter, deleted tab: pass.
- Contrast: lowest pair 1.62 dark, 1.63 light; lowest against chart background 3.32 dark, 3.61 light.
- 2027B ties to the plan: 2,448 cells at the start and 2,448 at fill 90, 0 differences. Totals 4,455 students, $1,706,910 fees, 498 classes.
- Dirt Bike: start $30,816 (41,616 − 4,800 − 6,000); each input moves the rows by the formula; 0 weekends gives no class or cost; reset restores; Budget tables do not move.

## Risks that are not faults

1. The Trends note says All Locations holds classes the log's summary does not split by range. 2026 now comes from Master, which does hold a site for them. The sentence is true of the summary only.
2. The Class filter says IME and the notes say First Ride for the same classes.
3. Code comments in the page file carry the names Sergio and Rick and the word his. They are not shown on screen, but anyone viewing the source sees them.

## What I could not check

- That 2026 differs from the budget workbook's Prior column was not measured: I did not open that workbook.
- The Class_Data, rent table and PRU-pl sources behind the 2027 figures: compared only to release 5.
- The WklyConsolidating Wd tab was not read; 4,543 and $1,585,090 are the page's own figures.
- Phone width and print were not tested.
- Customer names were not searched by a name list; the page data holds no person-name field that I saw, and no email, phone or class code.

## My own mistakes

1. The Browser pane was at its tab cap, so I navigated an existing tab (tab-3, which held 127.0.0.1:8798) to my page.
2. I read the rules list's first 436 lines in full, and from the rest only each mistake's title and test line.
3. A first browser script failed because I called `PL` as a function without reading its shape. It left a hidden iframe, which I removed before the next run.
