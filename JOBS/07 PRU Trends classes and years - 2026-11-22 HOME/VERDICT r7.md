FAIL

# Blind check r7, PRU job 07, Trends page

Page checked: draft-g.html, md5 01fef319117066605679acf3b3d92972
Goal: md5 8a9b74d169416f5baa571b92fdbde055. Release 5: md5 218637b509804e342cedabb9bc9b8e16. Source: v3 log, md5 37c427cf4078f449459b532e4d8e9377, sheet Master.
Measured in the built-in browser, page served as UTF-8 from 127.0.0.1:8811. No console errors.

## Findings: 4

### 1. The source line at the foot of every tab names the wrong source for 2026
- Where: the "Sources:" line, all four tabs.
- Shown: "tabs WklyConsolidating Wd (students and sales) and Master (classes and students per class, by class code only)".
- Should be: 2026 students and sales shown on Trends and in the plan's 2026 student comparison come from Master by class date, with fee column J as sums. The weekly summary is only the 2027 budget base.
- Measured: Trends prints 2026 sales $1,602,640 and 4,606 students, equal to my Master count. The weekly-summary figure is $1,585,090 (plan tab, 2026 registrations $ row). The line also contradicts the Trends note, which says 2026 is Master.

### 2. Six HD classes are counted as 2-Wheel, and HD says "not available"
- Where: Trends, Classes, class filter 2-Wheel, row Manassas - GMU; and class filter HD. The same 45 is in the plan's Months panel for Manassas GMU 2-Wheel.
- Shown: 2-Wheel classes at Manassas - GMU 45 (Mar 4, Apr 6, May 8) beside 2-Wheel students 267. HD shows "2026 classes: not available". The note says HD has no class count of its own.
- Should be: 2-Wheel 39 at that range (Mar 2, Apr 4, May 6), with HD's 6 classes shown as HD, or the page must say plainly that 2-Wheel classes include HD while 2-Wheel students do not.
- Measured: Master at MANGMU has 39 codes with only course BRCE (267 students) and 6 codes with only course BRCR (47 students; Mar, Apr, May, 2 each). The page's HD students are the BRCR rows (48, the 48th in the December code of finding 4). Read as shown, 267 / 45 = 5.9 students a class; on matching classes, 267 / 39 = 6.8. All-range 2-Wheel 462 carries the same 6. Master is a class source for HD, so "not available" is not true for 2026.

### 3. 2027B range rows do not add to the printed total, and Trends does not say why
- Where: Trends, 2027B, Students and Sales $, class filters All, 2-Wheel and 3-Wheel (6 views).
- Shown: 43 month or year cells where the printed rows differ from the printed All ranges figure. Largest: Students, All, Nov, rows add to 255, total 253; Students, 2-Wheel, Nov, 224 against 222; Sales $, All, Mar, $207,045 against $207,047.
- Should be: either the figures add, or Trends carries the rounding sentence the plan and Budget tabs already carry. Trends has no such sentence.
- Measured: every printed row added up in all 73 table views. Classes views and all 2024, 2025 and 2026 views add exactly.

### 4. One December class code spread over 8 sites is shown as one Clarksburg class
- Where: Trends, Classes, 2026, December, 2-Wheel, Clarksburg (MD), printed 8; Colonial Heights printed 5. The note says "Classes stand at their real site".
- Shown: the code counts as 1 class at Clarksburg.
- Should be: that sentence is not true for this code. It needs a named treatment, or a line on the page.
- Measured: the code dated 261227 has 45 rows, 8 sites and 8 course codes, all in December. Clarksburg holds 8 of the rows and Colonial 14. The next largest class in Master has 16 rows. Effect on the printed count: one class, in one month. All-range December (52) is not affected.

## What passed
- B1, 2026 students and classes: 468 Months-panel cells opened on screen for all 20 site and class rows, against Trends for the same range, class and month: 0 differences in classes or 2-Wheel and 3-Wheel students. BRC2 and First Ride students sit under All Locations on Trends; their site figures add to it (137 and 79).
- B2: January prints 37. Students by month 37, 166, 551, 534, 691, 543, 484, 506, 379, 352, 237, 126 = 4,606 on Trends, equal to my Master count; the plan prints 4,606.
- B3: First Ride at Manassas Mall and Woodbridge, March and October, prints 0.5 on both tabs. Every 2027 class cell by range, class and month matches. Classes rows add to the total in every view.
- C: 9 scenarios (start, fill all, fill by type, fill by site, price, rent, months, Dirt Bike, mixed) on the plan, New initiatives and Budget tabs, all three P&L views. New initiatives and Budget: 0 lines differ from release 5. Plan: 8 lines differ in each scenario, all acceptable: the 2026 student comparison (4,606 and its %), and labels naming the base.
- Goal tests: 2024 and 2025 equal release 5 (1,872 values). 2026 classes by month equal Master (573); the existing list has the same total, with five months differing, list against class date (Jan 4/5, Feb 12/20, Mar 69/60, Oct 38/45, Nov 36/29). The page prints only that list's year total, 573. Year buttons, legend, year list, last year locked, dashed 2027B all work. Contrast: lowest year pair 1.62, lowest against background 3.32 dark, 3.61 light. Dirt Bike: $30,816 at start, formulas, 0 weekends, Reset, P&L unmoved. 2027B equals the plan's lines (3,024 values) and moves with fill (4,455 to 4,445 at 75%, same on both tabs). The 2027 vs 2026 tab is gone.
- D: 1,708 distinct shown strings, tooltips and labels included: no quotation marks, his/him/he, my pick or the listed names. No emails, phone numbers or class codes in the page's data.
- E: not available shows for 2024, 2025, HD, Other and 2027 ARC. The sentence on the budget book's Prior column is present.

## Risks that are not faults
- The plan prints 2026 registrations $0 for January and $1,585,090 for the year; Trends prints $12,943 and $1,602,640. The plan's row is labeled as the weekly summary and 2027 budget base, so it is allowed, but a reader will see two 2026 sales figures.
- The Change column on Trends compares 2026 by class date with 2025 from the weekly summary, so the two years are on different bases.
- 2026 classes (573) include ARC and HD; 2027B classes (498) have no ARC row. The note discloses ARC.
- 138 rows have a week in the month after the class date, and 2 rows sit 6 or 7 months later.

## What I could not check
- Release 4 was not opened. Comparisons are against release 5.
- Price and rent scenarios were set through the page's state function, not typed. Fill and Dirt Bike inputs were typed into the real boxes.
- Phone width, and saving to a hosted artifact, were not tested.
- The customer-data scan is by pattern and by reading the short strings.

## My own mistakes
- My first two Master scripts asked openpyxl for columns B to J in one range, so columns F to I were loaded in memory, against the limit. Their values were never used, printed or saved. I recounted with B to E and J only: students, fees and classes are identical.
- A first browser run reported false differences for Manassas Mall because of a double space in its name. I fixed my comparison and reran it.
