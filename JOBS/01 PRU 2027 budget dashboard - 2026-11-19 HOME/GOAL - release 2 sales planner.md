# GOAL - job 01 release 2: PRU 2027 Sales Planner, flowing into the 2027 budget

Accepted by Sergio, 2026-11-20, Angie's chat, question 12: "Yes, build it (Recommended)". The goal as put to him: "the planner gets a third tab, '2027 Budget'. It shows the P&L by month: Training = the plan's sales, the other lines moved by the rule in question 11, profit recomputed. Test: at Rick's own sales, every line equals Rick's budget to the dollar; at the plan's sales, totals add up line by line. Light and dark in Piston's colours, then live on ONE VIEW after the checks."

His words behind it (Angie's chat, 2026-11-20): "I need that planner to figure out 2027 sales, THEN you can flow it into the budget"; "I need 1 tab with the monthly trends by RANGE. In the planner look at the WklyConsolidating Wd tab"; "by planner i mean the 2026 PRTU Manual log v3"; "Yes, flow it in"; "make this planner in piston color, ask brain, and load this planner in teh ONE view. make light and dark themes."

## What the finished page shows

1. **Monthly trends by range:** students and sales $ by range and month for 2022-2026 (2022 students only), by class or all. Source: `C:\Users\Sergio\Downloads\2026 PRU Manual Log v3.xlsx`, sheet "WklyConsolidating Wd": each month block's MTD column (Z) for 2026 and its columns AK-AN for 2025-2022.
2. **2027 plan:** for each range and class, 2027 students = the chosen start year (2026, 2025 or the 2024-2026 average) by month x (1 + growth %), or months typed by hand. Price = the line's 2026 sales / 2026 students, else the latest year with sales, else the class average, x (1 + price change %), or typed. 2027 sales by month = the sum of students x price.
3. **2027 Budget:** every line of `C:\AI_Building\AI_Financials\04 Budget\2027\rolled\02 - Consolidated SGP Budget light.xlsx`, sheet PRU-pl, rows 8-103, by month. Training (row 13) = the plan's 2027 sales. The rule, his answer to question 11, "Hold fixed costs": each month every other line moves by that month's plan sales / Rick's Training (so cost of sales keeps each month's margin), **except** Salaries & Wages (33), Training Fleet Depreciation (27), Insurance - Other (60), Depreciation-Other (62), Rent (72), Leasehold Amortz. & Building Depr. (73), Insurance - Building (76), Floor Plan Interest (93), Mortgage & Other Interest (94), Non-Paying Interest Expense (98) and Other Income rows 85-88, which stay in Rick's dollars. Totals are recomputed from their lines. Income tax = before-tax x Rick's own rate for that month (row 101 / row 100).
4. **2027 sales trends** (his words, Angie's chat, 2026-11-20: "Also add a tab for 2027 budget trends (sales). I want to see 2026 lines vs 2027 budget lines, filtering by ranges and classes"): 2026 actual against the 2027 plan, by month, students or sales $, filtered by range and by class; a chart of the two lines and a table by month with the change.
5. Light and dark themes in Piston's colours (ONE VIEW's tokens, from the Brain); a theme switch.
6. **Coach pay and rent on the P&L** (his words, Angie's chat, 2026-11-20: "In the P&L i want to be able to change the avg hourly rate of coaches, and the monthly rent by range"):
   - Pay per class, editable. His answer 13: "just dived it by the number of classes held. Not by student. they get paid by class." His answer 14: "All coach pay (Recommended)": the whole of Salaries & Wages (row 33) is coach pay. Start value = Rick's 2027 Salaries & Wages $316,299 / 573 classes held in 2026 = $552. Source of the 573: the log's sheet Master, distinct class codes by week-ending date, counted (no customer fields read).
   - Classes held in 2027 by month, editable; start = 2026's by month; an option makes them follow 2027 students.
   - Salaries & Wages each month = Rick's month x (pay per class / $552) + (2027 classes - 2026 classes + initiatives' classes) x pay per class.
   - Rent by range by month, editable. His answer 15: "Rick's rent split (Recommended)": start = Rick's Rent (row 72) that month x the range's share of that month's 2027 plan sales. The weekend rate from the log's "26 Rent Schedule" tab shows beside each range as a guide (no contact fields).
7. **New initiatives** (his words, Angie's chat, 2026-11-20: "Then i need an additional tab fro new initiatives: These would a tab i use to represent scenarios where I add a range or i add a new kind class"): each scenario is a new range or a new class, with start month, students by month, price, students per class and (for a range) rent per month, and an on/off switch. When on, its sales add to Training, its classes x pay per class add to Salaries, its rent adds to Rent, and it shows on the 2027 plan and 2027 vs 2026 tabs.

## The test

1. At Rick's own Training (plan sales set equal to row 13), every line of the 2027 Budget tab equals PRU-pl's value within $1, every month.
2. At the plan's sales, each total equals the sum of its lines, each month; Gross Profit = Total Sales - Total Cost of Sales; profit lines follow.
3. A fixed line equals Rick's value at any sales.
4. The trends tab's figures equal the source cells (a node render compared with an independent read).
5. The test fails on planted faults before it is believed.
6. Pay per class at $600 gives Salaries & Wages = $316,299 x 600 / 552.005 (with no class or initiative change).
7. An initiative switched on adds exactly its sales to Training, its rent to Rent and its classes x pay per class to Salaries; switched off, the P&L returns to what it was.
8. A rent typed for one range and month replaces that cell only, and Rent equals the sum of the ranges plus initiatives' rent.

Then: a blind check by an agent that did not build it (R-1875); LAWYER (R-1877); Sergio's accept; the Brain puts it live (R-1900).
