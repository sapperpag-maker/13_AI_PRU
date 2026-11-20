# GOAL - PRU 2027 budget dashboard - DRAFT, repair round 3 (new shape: P&L alone for 9am)

**DRAFT.** He accepts the plan when LAWYER passes it ("plan is accepted when the lawyer passes. Piston picks on my behalf."). His words for the job are in `C:\AI_Building\AI_PRU\05 His answers and decisions\His words - the desk opened.md`: his opening words, his answers 53 to 59, 61 and 62 at the desk's opening, his answers 1 to 7 to Angie's questions, and his later messages. Blind check rounds 1 and 2: `C:\AI_Building\AI_MISC\06 Benches\2026-11-20 PRU job 01 plan blind check - ANGIE-HOME\FINDINGS.md` and `FINDINGS round 2.md` beside it.

## Who does what

- Angie builds the page, its program and its test on her bench in `C:\AI_Building\AI_MISC\06 Benches\` (R-0448). [answer 55: "Angie builds, Rick advises (Recommended)"]
- Rick answers Angie's questions and writes nothing in `C:\AI_Building\AI_PRU`. [answer 55]
- Angie's blind checker, then LAWYER, check it (R-1875, R-1877). Sergio accepts, or Piston where he named him ("Piston picks on my behalf"). The Brain puts it live on ONE VIEW. [answer 59: "Angie builds, Brain puts live (Recommended)"]

## Release 1: the page for 9am ("ill need something in ONE VIEW for tomorrow 9am MANDATORY") - the P&L tab alone

Shape picked by Piston in his place after the third FAIL of Angie's blind check (R-1878; Piston, 2026-11-20 ~02:15: "If it comes, I'll pick: deliver only the P&L tab for 9am"), his to strike. The Weekly tab moves to release 1b.

**R1-1. One page, `PRU 2027 Budget - DRAFT.html`, holding the P&L alone.** It opens alone with no internet, light and dark, as Rick's store pages do (`C:\AI_Building\AI_Financials\.claude\skills\fs-budget-store-pages\SKILL.md`: "one file that opens with no internet, light and dark"); it has a light/dark button. It shows "Draft budget, not approved". It holds nothing from the student log: no figure, no md5, no file name. One line says what is not on it yet: "Not on this page yet: the weekly measures (students, sales by class and by range) come after review; coach pass rate, coach profitability and class fill rate wait on the file Sergio will send."

**R1-2. PRU's whole P&L, 2025, 2026 and 2027.** [answer 1: "i want P&L same as rick"; answer 2: "2025, 2026, 2027 side by side"] The year view shows the three years side by side, one column each; the month view shows one year's twelve months at a time, the year picked from a list (G13). Each figure is read by program; none is typed.
- **A line** is a row of PRU-pl from 8 to 103 that has a label in column B or a month figure that is not zero, in PRU-pl's own order. Rows with neither are left out.
- **A heading** is a line whose twelve month cells are empty in all three years (2027 row, 2026 row, 2025 row); it shows no figures.
- **Row 21** has no label and holds ratios (gross profit, row 20, over total sales, row 14; 0.62 to 0.80). It is shown as percents, with no year figure and no gap mark, under "(row 21: a ratio, shown as a percent; no label in the source)" (G11). The program refuses to run if row 21 gains a label or a value above 1.5.
- 2027: `C:\AI_Building\AI_Financials\04 Budget\2027\rolled\02 - Consolidated SGP Budget light.xlsx` (md5 64e3c1ecdf01ee25cae717657952bfbe), sheet PRU-pl. Months in columns D, E, F, I, J, K, N, O, P, S, T, U; the year in Y ("2027B").
- 2026: the same sheet, the block headed "2026 - Prior Year", matched by position: each line's row plus 108 (rows 116-211), the same columns, the year in Y ("Total"). PRU-pl B184 reads "Repairs and Maintenance - Building" where B76 reads "Insurance - Building"; the page shows a note saying so (G6).
- 2025: `C:\AI_Building\AI_Financials\04 Budget\2027\raw files\3 Operating statements\02 - Operating Statements 2026-09.xlsx` (md5 c2b949723c5f30e369b831404a90ce37), sheet PRU-Prior, **the same row** as PRU-pl. Its column B equals PRU-pl's on every line's row; the test checks this before anything else (SOURCE CHECKS) and a difference fails the run. The same twelve month columns, as `C:\AI_Building\AI_Financials\04 Budget\2027\scripts\fs_budget_pru_2026.py` reads them (its MONTHS list); the year in Y ("Total").
- **A year figure is the source's own year cell.** Where a line's twelve months miss that cell by more than $1 in the source (25 lines in 2025, none in 2026 or 2027; row 21 is exempt), the page marks the year with * and shows the month sum in its tooltip (G8).

**R1-3. A test, by program, that fails on each of these and passes on none.** A figure matches within $0.005 of its source cell (the page carries the cell's full value). The test renders each view of the page in node and compares every shown cell, rounded as the page rounds (half up, whole dollars, negatives in brackets).
1. a month figure differs from its source cell (any year, line or month), in the data or as shown;
2. a year figure differs from its source's year cell, in the data or as shown; a gap (R1-2) is not marked, or one is marked that does not exist, or row 21 is marked;
3. a line is missing or one is added; a line's heading or ratio flag differs from R1-2's definitions;
4. a year (2025, 2026, 2027) is missing;
5. the page refers to the internet: `http:`, `https:`, `ws:` or `wss:` anywhere; a `//` address in src, href, action, srcset, data or CSS url(); @import, import(), fetch, XMLHttpRequest, WebSocket, EventSource or sendBeacon;
6. "Draft budget, not approved" is missing;
7. the md5 of either source is not on the page;
8. the B184 note is not shown;
9. the dark-theme CSS (`@media (prefers-color-scheme: dark)` and `:root[data-theme="dark"]`) or the light/dark button is missing;
10. the "Not on this page yet" line is missing;
11. anything from the student log is on the page: weekly data, its md5 or its name.

Before the test is believed, it fails on 42 planted faults, one per branch: case 1 four (a month in each year, a shown month); case 2 five (a year, a shown year, a 2025 mark removed, a false 2027 mark, a mark on row 21); case 3 four (a line removed, a line added, a figure line flagged heading, row 21's ratio flag removed); case 4 three (each year); case 5 sixteen (each internet pattern); case 6 one; case 7 two (each md5); case 8 one; case 9 two (the CSS, the button); case 10 one; case 11 three (weekly data, the log's md5, its name).

**R1-4. Pass mark:** the test's whole output shows SOURCE CHECKS PASS and PASS on all 11 cases, with the two source md5s and the page's md5; and each of the 42 plants shows FAIL.

## Release 1b (after 9am): the Weekly tab

Built and checked as release 1 is, with a goal section of its own before it goes on the page. Two faults the blind check found are repaired first: course names typed in the program (no source) come off or get a source; and "weeks after today are bookings ahead" is said only with a source.

**R1b-1. Tab Weekly: number of students, and the sales half of range and class profitability, one point per week, every week from the first to the newest week-ending date in the source; a week with no registrations shows 0.** [answer 61: "Part of job 01"; answer 4: "Build the three found first"] Profit comes in release 2 (G1).
- Number of students: registration rows counted per week-ending date. One row is one registration: a student on two courses counts twice. The page says so (G9).
- Sales by class: the sum of Total Fee per week, by course.
- Sales by range: the sum of Total Fee per week, by site.
- Source: `C:\Users\Sergio\Downloads\2026 PRU Manual Log v3.xlsx` (md5 ab99689da045431d30dda84f57000c76, 6,464,527 B), sheet Master. He sent it in Angie's chat, 2026-11-20 00:29: @"C:\Users\Sergio\Downloads\2026 PRU Manual Log v3.xlsx". It is not the live log he named first, `H:\Shared drives\Accounting\09-Daily Reports\2026 PRU\2026 PRU Manual Log v.3.xlsx` (662,493 B, 2 sheets, no sheet Master); the Downloads file is used because it holds Master (G10). Only these columns are read: Site, Course, WE Dt, Total Fee. The program reads no name, email or ID column, and writes only weekly totals. Rows with no week-ending date are not counted; the page gives their number and their Total Fee in dollars. Ranges are shown by the site codes the log uses; no plain names are in a source read here (G12). The file is never copied into `C:\AI_Building\AI_PRU`.
- Not in release 1: coach pass rate, coach profitability and class fill rate. They wait on his file (answer 6: "skip for now, ill send it later"). The page says so in one line.

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
