# GOAL - PRU 2027 budget dashboard - DRAFT, repair round 5 (new shape: P&L alone for 9am)

**DRAFT.** He accepts the plan when LAWYER passes it ("plan is accepted when the lawyer passes. Piston picks on my behalf."). His words for the job are in `C:\AI_Building\AI_PRU\05 His answers and decisions\His words - the desk opened.md`: his opening words, his answers 53 to 59, 61 and 62 at the desk's opening, his answers 1 to 7 to Angie's questions, and his later messages. Angie's blind checks, in order:
- check 1, plan: `C:\AI_Building\AI_MISC\06 Benches\2026-11-20 PRU job 01 plan blind check - ANGIE-HOME\FINDINGS.md`
- check 2, plan: `C:\AI_Building\AI_MISC\06 Benches\2026-11-20 PRU job 01 plan blind check - ANGIE-HOME\FINDINGS round 2.md`
- check 2, page (run beside it): `C:\AI_Building\AI_MISC\06 Benches\2026-11-20 PRU job 01 page blind check - ANGIE-HOME\FINDINGS round 1.md`
- check 3, plan and page: `C:\AI_Building\AI_MISC\06 Benches\2026-11-20 PRU job 01 plan blind check - ANGIE-HOME\FINDINGS round 3.md` (the plan's third FAIL)
- check 4, plan and page in the new shape: `C:\AI_Building\AI_MISC\06 Benches\2026-11-20 PRU job 01 plan blind check - ANGIE-HOME\FINDINGS round 4.md` (page PASS, plan FAIL 11)

## Who does what

- Angie builds the page, its program and its test on her bench in `C:\AI_Building\AI_MISC\06 Benches\` (R-0448). [answer 55: "Angie builds, Rick advises (Recommended)"]
- Rick answers Angie's questions and writes nothing in `C:\AI_Building\AI_PRU`. [answer 55]
- Angie's blind checker, then LAWYER, check it (R-1875, R-1877). Sergio alone accepts the page (R-0180). Piston picks shapes and decisions in his place ("Piston picks on my behalf") but does not accept the page; he asks Sergio for his yes when he is back. The Brain puts it live on ONE VIEW. [answer 59: "Angie builds, Brain puts live (Recommended)"]

## Release 1: the page for 9am ("ill need something in ONE VIEW for tomorrow 9am MANDATORY") - the P&L tab alone

Shape picked by Piston in his place after the third FAIL of Angie's blind check (R-1878; Piston's message to Angie, 2026-11-20 02:05, logged in `C:\AI_Building\AI_PRU\LOG.md`: "If it comes, I'll pick: deliver only the P&L tab for 9am"), his to strike. The Weekly tab moves to release 1b.

**R1-1. One page, `C:\AI_Building\AI_MISC\06 Benches\2026-11-20 PRU job 01 page - ANGIE-HOME\PRU 2027 Budget - DRAFT.html`, holding the P&L alone,** built by `C:\AI_Building\AI_MISC\06 Benches\2026-11-20 PRU job 01 page - ANGIE-HOME\build_page.py --pl-only`. After LAWYER's PASS it is copied, unchanged, into `C:\AI_Building\AI_PRU\JOBS\01 PRU 2027 budget dashboard - 2026-11-19 HOME\`. It opens alone with no internet, light and dark, as Rick's store pages do (`C:\AI_Building\AI_Financials\.claude\skills\fs-budget-store-pages\SKILL.md`: "one file that opens with no internet, light and dark"); it has a light/dark button. It shows "Draft budget, not approved". It holds nothing from the student log: no figure, no md5, no file name. One line says what is not on it yet: "Not on this page yet: the weekly measures (students, sales by class and by range) come after review; coach pass rate, coach profitability and class fill rate wait on the file Sergio will send."

**R1-2. PRU's whole P&L, 2025, 2026 and 2027.** [answer 1: "i want P&L same as rick"; answer 2: "2025, 2026, 2027 side by side"] The year view shows the three years side by side, one column each; the month view shows one year's twelve months at a time, the year picked from a list (G13). Each figure is read by program; none is typed.
- **A line** is a row of PRU-pl from 8 to 103 that has a label in column B or a month figure that is not zero, in PRU-pl's own order. Rows with neither are left out.
- **A heading** is a line whose twelve month cells are empty in all three years (2027 row, 2026 row, 2025 row); it shows no figures.
- **Row 21** has no label and holds ratios from 0.62 to 0.80. In 2026 and 2027 each equals gross profit (row 20) over total sales (row 14). In 2025 one cell does not: PRU-Prior U21 (December) holds 0.7096, which repeats November's T21, where U20/U14 gives 0.7818. The page shows every cell as the source holds it. Row 21 is shown as percents, with no year figure and no gap mark, under "(row 21: a ratio, shown as a percent; no label in the source)" (G11). The program refuses to run if row 21 gains a label or a value above 1.5 (its function `ratio_ok`).
- 2027: `C:\AI_Building\AI_Financials\04 Budget\2027\rolled\02 - Consolidated SGP Budget light.xlsx` (md5 64e3c1ecdf01ee25cae717657952bfbe), sheet PRU-pl. Months in columns D, E, F, I, J, K, N, O, P, S, T, U; the year in Y ("2027B").
- 2026: the same sheet, the block headed "2026 - Prior Year", matched by position: each line's row plus 108 (rows 116-211), the same columns, the year in Y ("Total"). PRU-pl B184 reads "Repairs and Maintenance - Building" where B76 reads "Insurance - Building"; the page shows a note saying so (G6).
- 2025: `C:\AI_Building\AI_Financials\04 Budget\2027\raw files\3 Operating statements\02 - Operating Statements 2026-09.xlsx` (md5 c2b949723c5f30e369b831404a90ce37), sheet PRU-Prior, **the same row** as PRU-pl. Its column B equals PRU-pl's on every line's row; the test checks this before anything else (SOURCE CHECKS) and a difference fails the run. The same twelve month columns, as `C:\AI_Building\AI_Financials\04 Budget\2027\scripts\fs_budget_pru_2026.py` reads them (its MONTHS list); the year in Y ("Total").
- **A year figure is the source's own year cell.** Where a line's twelve months miss that cell by more than $1 in the source (25 lines in 2025, none in 2026 or 2027; row 21 is exempt), the page marks the year with * and shows the month sum in its tooltip (G8).

**R1-3. A test, by program, `C:\AI_Building\AI_MISC\06 Benches\2026-11-20 PRU job 01 page - ANGIE-HOME\test_page_pl.py`, that fails on each of these and passes on none.** Before the cases it runs SOURCE CHECKS: PRU-Prior's column B equals PRU-pl's on every line's row, and row 21 is still an unlabelled row of ratios no higher than 1.5. A figure matches within $0.005 of its source cell (the page carries the cell's full value). The test renders each view of the page in node and compares every shown cell, rounded as the page rounds (half up, whole dollars, negatives in brackets).
1. a month figure differs from its source cell (any year, line or month), in the data or as shown; a month cell carries a * mark or a tooltip;
2. a year figure differs from its source's year cell, in the data or as shown; a gap (R1-2) is not marked, or one is marked that does not exist, or row 21 is marked, in the data or as drawn (the * on the year cell, in the year view and in each month view's year column); a gap's year cell has no tooltip reading "Months add up to" and the month sum recounted from the source, or a year cell that is not a gap has a tooltip;
3. a line is missing or one is added; the lines are not in PRU-pl's order; a label differs from the source's column B (or, where B is empty, from R1-2's stand-in text), in the data or as drawn in any view; a line's heading or ratio flag differs from R1-2's definitions; a heading shows a figure or a tooltip in any view;
4. a year (2025, 2026, 2027) is missing, in the data, as a year-view column, or as an option of the view list (the year view and each year by month);
5. the page refers to the internet: `http:`, `https:`, `ws:` or `wss:` anywhere; a `//` address in src, href, action, srcset, data or CSS url(); @import, import(), fetch, XMLHttpRequest, WebSocket, EventSource or sendBeacon;
6. "Draft budget, not approved" is missing;
7. the md5 of either source is not on the page;
8. the B184 note is not shown;
9. the dark-theme CSS (`@media (prefers-color-scheme: dark)` and `:root[data-theme="dark"]`) or the light/dark button is missing;
10. the "Not on this page yet" line is missing or differs by a word from R1-1;
11. anything from the student log is on the page: weekly data, its md5 or its name.

Before the test is believed, it fails on 57 planted faults, one per branch:
- case 1 five (a month in each year, a shown month, a tooltip on every month cell);
- case 2 eight (a year, a shown year, a 2025 mark removed, a false 2027 mark, a mark on row 21, a tooltip sum wrong, the tooltip removed, the * not drawn);
- case 3 eight (a line removed, a line added, two lines out of order, a label changed, a figure line flagged heading, row 21's ratio flag removed, a heading showing figures, labels not drawn);
- case 4 four (each year, and 2025 by month taken off the view list);
- case 5 seventeen (each internet pattern, `ws:` included);
- case 6 one; case 7 two (each md5); case 8 one; case 9 two (the CSS, the button); case 10 two (the line removed, its middle words changed); case 11 three (weekly data, the log's md5, its name);
- SOURCE CHECKS two (a PRU-Prior label changed, row 21 given a label);
- the program's refusal two: `ratio_ok` in `C:\AI_Building\AI_MISC\06 Benches\2026-11-20 PRU job 01 page - ANGIE-HOME\build_page.py` refuses row 21 with a label and with a value above 1.5, and accepts the real row 21.

**R1-4. Pass mark:** the test's whole output, `C:\AI_Building\AI_MISC\06 Benches\2026-11-20 PRU job 01 page - ANGIE-HOME\TEST_OUTPUT_PL.txt`, shows the following:
- the two source md5s and the page's md5;
- SOURCE CHECKS PASS;
- PASS on all 11 cases;
- "program refusal, real row 21: PASS - accepted";
- each of the 57 plants FAIL - caught.

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
