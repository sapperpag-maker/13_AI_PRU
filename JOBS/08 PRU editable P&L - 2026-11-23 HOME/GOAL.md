# Job 08 goal: a planner whose 2027 budget Sergio can edit

His yes, Q123, 2026-11-23: "Yes, build it (Recommended)".

His words, 2026-11-23: "PRU P&L is very badly formatted. And I need to be able to set my own 2027 b values myself. I want to see for every year I want see teh balances and % compared to sales. I want to be able to change 2027b values (balances and or %) Then a final 2 columns with the 2027 end values that automatically change with my edits.", "the PLANNER, I NEED TO BE ABLE TO EDIT 2027 BUDGET VALUES, havent I asked for this 4 times already??", "and why December would spike like that ! Ask builder how he did the 2027 sales goals page." and "YOUR GOAL NOW: MAKE A PLANNER THAT WORKS BVASED ON MY REQUESTS."

Base: the figure-fix page, built alone from repaired page bc5b00d4c6c64b3b0075c842a50ab4a7 with its own blind check and LAWYER check (Piston's order, 2026-11-23). Job 08 is rebuilt on it once it passes.

## What the finished page shows

1. **One clean P&L table:** line | 2025 $ | 2025 % | 2026 $ | 2026 % | 2027B $ | 2027B % | 2027 End $ | 2027 End %. Q114.
2. **% is always % of sales** for that year. Number format, frozen line names and header, clear section and total rows.
   - The page says on its face that 2025 operating profit is $69,183.40 by the year-end statements and $106,290.74 by the GL, a $37,107.34 gap not explained, unless the gap is traced first.
3. **2027B $ and % can both be typed, on every line that is not a total, except the six sales lines (rows 8 to 13), which take $ only and show their %** (Q126, 2026-11-23: "Sales lines: $ only (Recommended)"). Typing one fills the other. **The 2027B total rows follow the typed values, so the column always adds up** (Q125, 2026-11-23: "Totals follow my edits (Recommended)").
4. **Year and each month can be typed** (Q115). A switch opens the 12 months of 2027B.
   - Typing a year spreads it over the months by that line's current monthly shape, and replaces month values typed earlier on that line.
   - Typing a month changes that month, and the year becomes the sum of the months.
5. **A typed $ stays that dollar amount. A typed % stays that % and its dollars move with sales. Lines not touched keep following the plan** (Q116).
6. **2027 End $ and % update at once** after any edit, here or on the classes, students, rent and coach inputs. Totals, gross profit, operating profit, tax and net recalculate.
7. **Each edited line is marked and has its own reset.** Reset everything clears them, after a second click.
   - A line with no 2027 monthly shape spreads by its 2026 shape, else equally (the method of the store P&L Goals pages, BUILDER's report of 2026-11-23).
   - Percent keeps 4 decimals, dollars 2.
8. **Sales corrected:** January $14,469 and the proved Feb-Sep $4,013 come out by lowering the carried total, same monthly spread (his 128, Q117). Start values: sales $1,761,113.12, operating profit $280,838.33, net after taxes $199,873.87. The other $10,077 stays as a named unknown.

## Sales planner: classes and students (his Q119 answer, 2026-11-23)

His words: "As I said already, the sales planner for 2027, I want to be able to change the number of classes per month, the number of students for each individual type of class, and then the line that represents the trend should adjust accordingly."

Measured on the base page bc5b00d4, 2026-11-23, in the browser:

- The 2027B line already moves: one more March 2-Wheel class took March from 57 to 58 classes and 532.65 to 543.34 students.
- Classes can be typed only site by site, across 20 rows, each behind a Months button.
- No box takes a number of students. Only fill % can be typed.
- HD and ARC have no class or student box at all.

His answers: Q120 "Students per class (Recommended)"; Q121 "Type every site myself"; Q122 "Under the trend chart (Recommended)".

The finished page has one grid under the trend chart on the Monthly trends page:

1. **One block per site and class type (the 20 rows), Jan to Dec:** classes and students per class, both typed directly. No automatic split across sites.
2. **Total students = classes x students per class,** shown per month and year. Changing classes moves students.
3. **ARC and HD get their own rows.** ARC: classes and students per class. HD: the plan holds no HD class count, so HD takes students by month until a class count is given.
4. **The 2027B line, sales, rent, coach cost and the P&L follow at once,** with the class and year filters still working.
5. **A typed students per class wins over fill %.** Coaches follow it month by month: one at 6 or fewer, two above. A figure above the class's seats (12; 4 for First Ride) is marked, not blocked.
6. **Each typed cell is marked, has a reset, and is saved** the way the section below says.

His words, 2026-11-23: "I want a tab per range", "take 2024 out", "and then a summary tab as well". So the Monthly trends page has a Summary tab (all ranges, with the table of ranges), then one tab per range holding that range's chart, year table and grid. 2024 is not shown.

Test: every range tab opens with no page error, the ranges add up to the Summary in each year, and every grid row is reachable from a tab.

Test: for every grid row and month, type classes, then students per class. The 2027B line for that site, class and month, total students, sales, rent, coaches and net each recompute correctly, and no other row moves.

## How his edits are saved, so a rebuild or a fix cannot wipe them

Today (template.html lines 106, 112, 529-544): edits sit in this browser under one key, or inside the page when the page can publish itself. `build.py` writes an empty state, so a rebuild drops any edits saved inside the page.

1. **Only what he typed is saved:** line, month or year, $ or %. Results are never saved, so a corrected sales figure flows through his edits.
2. **The saved key stays the same across releases,** and a new release loads the old edits. Today's class, fill, price and rent edits carry over too.
3. **Download my edits / Load my edits buttons** keep a copy in a file he owns.
4. **A line that no longer exists is never dropped silently:** the page lists it.
5. **Open, his call:** whether edits are shared between people. The store pages keep them in one browser only. Whether ONE VIEW can save for everyone is not checked.

## Plan

1. His changes to this goal, then his yes. Nothing is built before it.
2. On a bench from bc5b00d4: the January and $4,013 sales fix, tied to the start values.
3. 2026 lines from the workbook, PRU-pl, column AB. 2025 lines from `C:\AI_Building\AI_Financials\04 Budget\2027\raw files\3 Operating statements\Operating Statements.xlsx` (md5 b7c1ab1cc26251b08bb389b51d36bfe6), tab PRUAct, the 12 months, by a program (his Q124 "2025 year-end statements"). The workbook has no 2025: its column labelled 2025 holds Q4 2026. This 2025 does not tie to the GL: operating profit $69,183.40 against $106,290.74.
4. The new P&L table, the edit logic, the saving.
5. My own tests below, then a fresh blind checker, then LAWYER through Piston.
6. Sergio accepts. The Brain puts it live on ONE VIEW.

## Tests that say it shows it

1. With no edits, 2027B equals 2027 End on every line and month, and sales, operating profit and net equal the start values in item 8.
2. 2026 $ ties to the budget workbook (md5 3717f2bb), PRU-pl, and 2025 $ to Operating Statements.xlsx (md5 b7c1ab1c), PRUAct, every line, by the tie-out program; each % recomputes from them.
3. For a sample-free sweep of every editable line: type a $, type a %, type a month. Each time the line, its totals, profit, tax and net recompute correctly, and untouched lines do not move except by sales.
4. A typed $ does not move when classes change. A typed % does move, by the sales change.
5. Save, reload and reset each keep or clear every edit correctly. Edits made on one build load on a rebuilt page with changed sales, and the file download and load restores them exactly.
6. No page error, readable at desktop and phone width.
7. Blind check by a fresh agent, then LAWYER, before it reaches him or ONE VIEW.

## His 149 and 150 (his answers in Piston's chat, relayed by Piston, 2026-11-23)

- **149, "500, with ARC (Recommended)":** 2027B shows 500 classes, worded as 498 on the sites plus 2 ARC. ARC stands under All Locations in both years. 2026 stays 573. No dollar moves.
- **150, typed by him: "HD is off. the range for ARC look in the website".** Open until his answer on the two questions sent through Piston: whether HD's $20,592 comes out of the start values, and where ARC stands, as the website names no single place for it. Until then HD and ARC rent stay as they are.

## The capped goal (his 11-15 order)

**It MUST deliver:**

1. One calculation: every tab reads classes, students, coaches, sales and rent from it. No tab keeps its own sum.
2. Every 2027B value on the P&L can be typed as the goal above says, with the 2027 End columns following at once.
3. Classes and students per class can be typed by month for every grid row, and the trend line follows.
4. A Summary tab and one tab per range, 2025, 2026 and 2027B only.
5. Saved edits survive a save, a reload and a rebuild.

**The 10 common failure cases the blind check tests:**

1. With no edits, a P&L cell differs from page dc320827.
2. With no edits, sales, operating profit or net differ from the start values, unless his answer on HD changes them.
3. 2027B classes are not 500, or are not worded 498 on the sites plus 2 ARC. 2026 is not 573.
4. The ranges do not add to the Summary in any year, for classes, students or sales.
5. ARC stands in different places in 2026 and 2027B.
6. A typed ARC class or students per class does not reach the plan tab, the coach label, the trends and the P&L.
7. ARC coach cost breaks the printed rule: two April classes cost $780.
8. A typed $ or % on a P&L line gives a wrong line, total, profit, tax or net.
9. A save or a rebuild loses a typed edit without stopping or listing it. A % on a sales line is not listed.
10. A sentence on the page says something the page's numbers do not do.

**Pass mark:** all 5 delivered and none of the 10 cases found. Anything else the check sees is reported, never a FAIL.

## Not in this job

- The 42 December classes: kept, on his answer "ok so them keep them" (job 06 session's report, 2026-11-23). 2026 stays at 573 classes.
- What the $10,077 is.
- Years before 2025.
