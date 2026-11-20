# GOAL - PRU 2027 budget dashboard - DRAFT, repair round 1

**DRAFT.** He accepts the plan when LAWYER passes it ("plan is accepted when the lawyer passes. Piston picks on my behalf."). His words for the job are in `C:\AI_Building\AI_PRU\05 His answers and decisions\His words - the desk opened.md`: his opening words, answers 53 to 62, Angie's answers 1 to 7 and his later messages. Repair round 1 of Angie's blind check: `C:\AI_Building\AI_MISC\06 Benches\2026-11-20 PRU job 01 plan blind check - ANGIE-HOME\FINDINGS.md`.

## Who does what

- Angie builds the page, its program and its test on her bench in `C:\AI_Building\AI_MISC\06 Benches\` (R-0448). [answer 55: "Angie builds, Rick advises (Recommended)"]
- Rick answers Angie's questions and writes nothing in `C:\AI_Building\AI_PRU`. [answer 55]
- Angie's blind checker, then LAWYER, check it (R-1875, R-1877). Sergio accepts, or Piston where he named him ("Piston picks on my behalf"). The Brain puts it live on ONE VIEW. [answer 59: "Angie builds, Brain puts live (Recommended)"]

## Release 1: the page for 9am ("ill need something in ONE VIEW for tomorrow 9am MANDATORY")

**R1-1. One page, `PRU 2027 Budget - DRAFT.html`,** with two tabs, P&L and Weekly. It opens alone with no internet, as Rick's store pages do (skill fs-budget-store-pages: "one file that opens with no internet, light and dark"). It shows "Draft budget, not approved". It names no student.

**R1-2. Tab P&L: PRU's whole P&L, 2025, 2026 and 2027 side by side, by month and by year.** [answer 1: "i want P&L same as rick"; answer 2: "2025, 2026, 2027 side by side"] One row per line of PRU-pl, column B, rows 8 to 103, in PRU-pl's own order. Each figure is read by program; none is typed.
- 2027: `C:\AI_Building\AI_Financials\04 Budget\2027\rolled\02 - Consolidated SGP Budget light.xlsx`, sheet PRU-pl, rows 8-103. Months in columns D, E, F, I, J, K, N, O, P, S, T, U; the year in Y ("2027B").
- 2026: the same sheet, the block headed "2026 - Prior Year". Its rows are 116-211, each the row above plus 108. Months are in the same twelve columns; the year is in Y ("Total").
- 2025: `C:\AI_Building\AI_Financials\04 Budget\2027\raw files\3 Operating statements\02 - Operating Statements 2026-09.xlsx`, sheet PRU-Prior. Its rows are matched to PRU-pl's lines by the label in column B. Months are in the same twelve columns, as Rick's `fs_budget_pru_2026.py` reads them (its MONTHS list).

**R1-3. Tab Weekly: three of the six measures, one point per week, 2026 to the newest week in the source.** [answer 61: "Part of job 01"; answer 4: "Build the three found first"]
- Number of students: registrations counted per week-ending date.
- Sales by class: the sum of fees per week, by course.
- Sales by range: the sum of fees per week, by site.
- Source: `C:\Users\Sergio\Downloads\2026 PRU Manual Log v3.xlsx`, sheet Master. He sent this file on 2026-11-20. Only these columns are read: Site, Course, WE Dt, Total Fee. The program reads no name, email or ID column, and writes only weekly totals. The file is never copied into `C:\AI_Building\AI_PRU`.
- Not in release 1: coach pass rate, coach profitability and class fill rate. They wait on his file (answer 6: "skip for now, ill send it later"). The page says so in one line.

**R1-4. A test, by program, that fails on each of these and passes on none:**
1. a P&L figure differs from its source cell (any year, line or month);
2. a year figure differs from its source's year cell, or from the sum of its twelve months by more than $1;
3. a line of PRU-pl rows 8-103 is missing from the page, or one is added;
4. a year (2025, 2026, 2027) is missing from the page;
5. a week present in the source is missing from a weekly measure;
6. a weekly figure differs from its recount from the source;
7. the page fetches anything from the internet (`http:` or `https:` in a src, href, import or fetch);
8. "Draft budget, not approved" is missing;
9. the md5 of any of the three source files is not on the page.

The test also scans the page for any student's name (case 10). It reads the Master columns Last Name and First NAme, by the test only, never printed, and looks for each student's full name - first and last of the same row, in either order - in the page's words. One match is a failure. Single page words that equal some first or last name (a month such as "May", the site code "WOOD") are listed for information and are not failures. (Full-auto decision G5, flagged: the first test, on every single value, failed on 12 ordinary page words.)

Before the test is believed, it must fail on one planted fault for each of the 10 cases above (case 10 is the name scan). For case 6, one plant goes in each of the three measures.

**R1-5. Pass mark:** the test's whole output shows PASS on the page, with the three source md5s and the page's md5; and each of the 10 plants shows FAIL.

## Release 2 (after 9am)

- **R2-1. Range profit per week:** range sales, less that range's rent, less its share of coach pay.
  - Rent comes from the GL accounts 785xx-30, one per site, in `C:\AI_Building\AI_Financials\00 Raw data\GL\2026 YTD 101E GL History Detail Postings - All Accounts.csv`, Store POW. This is Rick's read (his claim, R-0022).
  - Coach pay is account 72200-30, spread by students. [answer 7: "Spread coach pay by students"]
  - The page labels it an estimate.
- **R2-2. Class profit per week:** class sales less its share of coach pay, by students. Labelled an estimate. [answer 7]
- **R2-3. The 2027 sales goal planner.** [answer 1: "I want a 2027 Goal planner for the sales part, same as builder did for sales. A better version of the excel planner they used last year"; his message: "i need something more user friendly, that can be carrued into 2027"] Its MUSTs, cases and pass mark are written in a goal file of its own before it is built, checked the same way.

Coach pass rate, coach profitability and class fill rate join when his file comes (answer 6).

## Readers on ONE VIEW

His words, answer 3: "me kim richrd and angel aerls, PRU manager". Read as Sergio; Kim Harrison and Richard Stein (surnames from `C:\AI_Building\AI_Brain\wiki\people.md`); and one person, Angel Aerls, PRU manager. That reading is a full-auto decision, flagged (the office-full-auto-plan skill, Phase 4 item 1).
