# GOAL - PRU 2027 budget dashboard - DRAFT, repair round 2

**DRAFT.** He accepts the plan when LAWYER passes it ("plan is accepted when the lawyer passes. Piston picks on my behalf."). His words for the job are in `C:\AI_Building\AI_PRU\05 His answers and decisions\His words - the desk opened.md`: his opening words, his answers 53 to 59, 61 and 62 at the desk's opening, his answers 1 to 7 to Angie's questions, and his later messages. Blind check rounds 1 and 2: `C:\AI_Building\AI_MISC\06 Benches\2026-11-20 PRU job 01 plan blind check - ANGIE-HOME\FINDINGS.md` and `FINDINGS round 2.md` beside it.

## Who does what

- Angie builds the page, its program and its test on her bench in `C:\AI_Building\AI_MISC\06 Benches\` (R-0448). [answer 55: "Angie builds, Rick advises (Recommended)"]
- Rick answers Angie's questions and writes nothing in `C:\AI_Building\AI_PRU`. [answer 55]
- Angie's blind checker, then LAWYER, check it (R-1875, R-1877). Sergio accepts, or Piston where he named him ("Piston picks on my behalf"). The Brain puts it live on ONE VIEW. [answer 59: "Angie builds, Brain puts live (Recommended)"]

## Release 1: the page for 9am ("ill need something in ONE VIEW for tomorrow 9am MANDATORY")

**R1-1. One page, `PRU 2027 Budget - DRAFT.html`,** with two tabs, P&L and Weekly. It opens alone with no internet, as Rick's store pages do (`C:\AI_Building\AI_Financials\.claude\skills\fs-budget-store-pages\SKILL.md`: "one file that opens with no internet, light and dark"). It shows "Draft budget, not approved". It names no student.

**R1-2. Tab P&L: PRU's whole P&L, 2025, 2026 and 2027 side by side, by month and by year.** [answer 1: "i want P&L same as rick"; answer 2: "2025, 2026, 2027 side by side"] Each figure is read by program; none is typed.
- **A line** is a row of PRU-pl from 8 to 103 that has a label in column B or a month figure that is not zero, in PRU-pl's own order. Row 21 has no label and holds ratios (0.62 to 0.80, gross margin by the round-2 page check); it is shown as percents, with no year figure, under "(row 21: a ratio, shown as a percent; no label in the source)" (G11). Rows with neither a label nor a figure are left out.
- 2027: `C:\AI_Building\AI_Financials\04 Budget\2027\rolled\02 - Consolidated SGP Budget light.xlsx` (md5 64e3c1ecdf01ee25cae717657952bfbe), sheet PRU-pl. Months in columns D, E, F, I, J, K, N, O, P, S, T, U; the year in Y ("2027B").
- 2026: the same sheet, the block headed "2026 - Prior Year", matched by position: each line's row plus 108 (rows 116-211), the same columns, the year in Y ("Total"). PRU-pl B184 reads "Repairs and Maintenance - Building" where B76 reads "Insurance - Building"; the page notes it (G6).
- 2025: `C:\AI_Building\AI_Financials\04 Budget\2027\raw files\3 Operating statements\02 - Operating Statements 2026-09.xlsx` (md5 c2b949723c5f30e369b831404a90ce37), sheet PRU-Prior, **the same row** as PRU-pl (its column B equals PRU-pl's on every row 8-103; a difference is a failure). The same twelve month columns, as `C:\AI_Building\AI_Financials\04 Budget\2027\scripts\fs_budget_pru_2026.py` reads them (its MONTHS list); the year in Y ("Total").
- **A year figure is the source's own year cell.** Where the twelve months miss that cell by more than $1 in the source (25 rows of PRU-Prior), the page marks the year with * and shows the month sum in its tooltip (G8).

**R1-3. Tab Weekly: number of students, and the sales half of range and class profitability, one point per week, every week from the first to the newest week-ending date in the source; a week with no registrations shows 0.** [answer 61: "Part of job 01"; answer 4: "Build the three found first"] Profit comes in release 2 (G1).
- Number of students: registration rows counted per week-ending date. One row is one registration: a student on two courses counts twice. The page says so (G9).
- Sales by class: the sum of Total Fee per week, by course.
- Sales by range: the sum of Total Fee per week, by site.
- Source: `C:\Users\Sergio\Downloads\2026 PRU Manual Log v3.xlsx` (md5 ab99689da045431d30dda84f57000c76, 6,464,527 B), sheet Master. He sent it in Angie's chat, 2026-11-20 00:29: @"C:\Users\Sergio\Downloads\2026 PRU Manual Log v3.xlsx". It is not the live log he named first, `H:\Shared drives\Accounting\09-Daily Reports\2026 PRU\2026 PRU Manual Log v.3.xlsx` (662,493 B, 2 sheets, no sheet Master); the Downloads file is used because it holds Master (G10). Only these columns are read: Site, Course, WE Dt, Total Fee. The program reads no name, email or ID column, and writes only weekly totals. Rows with no week-ending date are not counted; the page gives their number and their Total Fee in dollars. Ranges are shown by the site codes the log uses; no plain names are in a source read here (G12). The file is never copied into `C:\AI_Building\AI_PRU`.
- Not in release 1: coach pass rate, coach profitability and class fill rate. They wait on his file (answer 6: "skip for now, ill send it later"). The page says so in one line.

**R1-4. A test, by program, that fails on each of these and passes on none.** A figure matches when it is within $0.005 of its source cell (the page carries the cell's full value).
1. a P&L month figure differs from its source cell (any year, line or month), in the data or as the page shows it (the test renders each view in node and compares every shown cell, rounded as the page rounds);
2. a year figure differs from its source's year cell, in the data or as shown; or a year whose months miss that cell by more than $1 is not marked, or one is marked that does not;
3. a line (as R1-2 defines it) is missing from the page or one is added, or PRU-Prior's label differs from PRU-pl's on a line's row, or a line's heading or ratio flag differs from its recount;
4. a year (2025, 2026, 2027) is missing from the page;
5. a week present in the source is missing from a weekly measure;
6. a weekly figure differs from its recount from the source (students, total sales, each class, each range);
7. the page refers to the internet anywhere: `http:`, `https:`, `ws:` or `wss:` anywhere in the file; a `//` address in src, href, action, srcset, data or CSS url(); @import, import(), fetch, XMLHttpRequest, WebSocket, EventSource or sendBeacon;
8. "Draft budget, not approved" is missing;
9. the md5 of any of the three source files is not on the page;
10. a student's full name - first and last of the same Master row, in either order - is in the page's words. The test reads the Master columns Last Name and First NAme for this alone and never prints them. Single page words that equal some first or last name ("May", the site code "WOOD") are listed for information and are not failures (G5).

Before the test is believed, it must fail on planted faults, one per branch of each case: case 1 four (a month in each year, a shown month); case 2 four (a year changed, a shown year, a 2025 mark removed, a false 2027 mark); case 3 three (a line removed, a line added, a figure line flagged heading); case 4 three (each year); case 5 one; case 6 four (students, total sales, a class, a range); cases 7, 8 and 10 one each; case 9 three (each md5). 25 plants.

**R1-5. Pass mark:** the test's whole output shows PASS on all 10 cases of the page, with the three source md5s and the page's md5; and each of the 25 plants shows FAIL.

## Release 2 (after 9am)

- **R2-1. Range profit per week:** range sales, less that range's rent, less its share of coach pay.
  - Rent comes from the GL accounts 785xx-30, one per site, in `C:\AI_Building\AI_Financials\00 Raw data\GL\2026 YTD 101E GL History Detail Postings - All Accounts.csv`, Store POW. This is Rick's read (his claim, R-0022).
  - Coach pay is account 72200-30, spread by students. [answer 7: "Spread coach pay by students"]
  - The page labels it an estimate.
- **R2-2. Class profit per week:** class sales less its share of coach pay, by students. Labelled an estimate. [answer 7]
- **R2-3. The 2027 sales goal planner.** [answer 1: "I want a 2027 Goal planner for the sales part, same as builder did for sales. A better version of the excel planner they used last year"; his message: "i need something more user friendly, that can be carrued into 2027"] Its MUSTs, cases and pass mark are written in a goal file of its own before it is built, checked the same way.

Coach pass rate, coach profitability and class fill rate join when his file comes (answer 6).

## Readers on ONE VIEW

His words, answer 3: "me kim richrd and angel aerls, PRU manager". Read as Sergio; Kim Harrison and Richard Stein (surnames from `C:\AI_Building\AI_Brain\wiki\people.md`); and one person, Angel Aerls, PRU manager. That reading is a full-auto decision, flagged (G4). Risk, from the round-2 check: His words also notes "'Angel' is Angie"; who "angel aerls" is stays his to say.
