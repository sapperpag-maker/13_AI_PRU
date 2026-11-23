# GOAL: job 07, the planner's Trends tab shows classes and clear years

Angie, 2026-11-22 HOME. Sergio's yes (R-1879): Q73 "Yes, build now (Recommended)" for points 1-5; Q80 "Yes, approve points 6-8 (Recommended)".

**Source of 2026 students and sales (Q79, "Master, by class date (Recommended)"):** both the plan and Trends use the v3 log's Master sheet (md5 37c427cf), each student in the month of the class date held in the class code, for rows with a week. Master's fee column J is read as sums only, by his Q79; no other column beyond B to E. Test 1's 2026 figures change accordingly: 2026 students are 4,606 on both tabs, January 37. Trends then no longer equals the budget book's Prior column, and the page says so.

**The 2027 budget does not move (Q109, "Keep 2027 as is (Recommended)"):** only the shown 2026 figures change. The 2027 plan, its start fill, its five parts and the P&L stay on the base they were built on (the log's weekly summary, and Master by week), so test 6 stands. Where the page prints that base, it is labeled as the 2027 budget base.

**One exception, Virginia Beach rent (Q112, "Once: 32 weekends (Recommended)"):** Virginia Beach's 2026 weekends base is 32, the distinct Sundays in Master, with its 67 classes. Rent and the P&L lines it feeds move by that change alone; every other figure in test 6 stands.

His words: "I need to see classes here as well, and use different colors with high contrast from each other for the years. i also want to be able to filter by year." Q71: "Number of classes (Recommended)". Q72: "do 2024-2025-2026. remove 2022 and 2023".

Starts from: `C:\AI_Building\AI_PRU\JOBS\02 PRU budget update - 2026-11-21 HOME\PRU 2027 Sales Planner - release 4.html`, with its build folder beside it. Other tabs do not change.

## What the finished page shows

1. **Years.** The Trends tab shows 2024, 2025 and 2026 only. 2022 and 2023 are gone from its chart, legend, table and year list.
2. **Colors.** Each year has its own color, in both themes: 2024 blue, 2025 pink, 2026 amber. Each pair of year colors differs by a contrast ratio of at least 1.5, and each color has at least 3:1 against the chart's background.
3. **Year filter.** One on/off button per year. Turning a year off takes it out of the chart and legend. At least one year stays on. The table's year list offers only the years that are on.
4. **Classes.** A third button beside Students and Sales $: the number of classes per month, by range, with the Class filter working on it.
5. **A year with no class source** shows "not available", never 0, in the chart legend and the table.

6. **Dirt Bike plan, New initiatives tab** (his words: "I need to be able to change number of classes, students, held through the year, rent and coach cost per weekend"; Q74: "By weekend, month by month (Recommended)"). He edits weekends held and classes per weekend for each month, and one students per class, rent per weekend and coach cost per weekend. Classes = weekends x classes per weekend; students = classes x students per class; coach and rent = weekends x their weekend cost. Start values: 1 weekend, 2 classes, 6 students, $500 rent, $400 coach, which give today's $30,816. It stays out of the P&L.

7. **2027B on Trends** (his words: "in here I want to see the 2027B trend as well"). 2027B is a fourth year button, with its own color and a dashed line, in the chart, legend and table, for Students, Sales $ and Classes, by range and class. It follows the 2027 plan tab's inputs. Students equal the plan tab's 2027 students. Classes equal its 2027 classes. Sales $ are class fees, like the log's registrations; the P&L's sales also hold the five parts. A class with no 2027 figure shows "not available".
8. **The "2027 vs 2026" tab is gone** (his words: "this page can be deleted"). The other tabs stay.

## Sources for classes

- 2026: Master sheet of the v3 log (md5 37c427cf), columns B to E only. A class is one class code, counted in the month of the class date held in the code (Q113, "Class date (Recommended)").
- 2024 and 2025: NO SOURCE YET. The v3 log's sheets 2024, "2025 " and 2025 Summary carry no class label (counted 2026-11-22). No full-year 2024 or 2025 log was found in the PRU Drive folder, Downloads, AI_Financials or the other folders searched; the newest 2024 file there was saved in August 2024.

## Tests

1. Students and Sales $ for 2024, 2025 and 2026 equal release 4's, for every range, class and month.
2. The 2026 class count per month, over all ranges, equals Master by class date. It differs from the week-based list (`classes2026.json`) in five months, class date against week: Jan 5 and 4, Feb 20 and 12, Mar 60 and 69, Oct 45 and 38, Nov 29 and 36. The year is 573 on both.
3. A program measures the contrast of every color pair, in both themes.
4. Each filter button is clicked in a browser: the chart, legend and table follow, and the last year on cannot be turned off.
5. No customer data, in the page or in the build's output.
6. The plan, New initiatives and Budget tabs' figures equal release 4's, apart from the Dirt Bike inputs above. No "2027 vs 2026" tab remains.
7. Dirt Bike: untouched, every row equals release 4's. Each input changed in a browser moves the rows by the formulas above; a month at 0 weekends shows no class and no cost; Reset restores the start; the P&L does not move.
8. 2027B: for every range and class, students and class fees by month equal the plan's lines; all ranges equal the plan tab's students, class fees and classes. A changed fill % moves the 2027B line.
