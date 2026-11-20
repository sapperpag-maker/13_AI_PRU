# GOAL - PRU 2027 budget dashboard - DRAFT, repair round 6 (smaller shape: P&L alone, its figures proved, for 9am)

**DRAFT.** He accepts the plan when LAWYER passes it ("plan is accepted when the lawyer passes. Piston picks on my behalf."). His words for the job are in `C:\AI_Building\AI_PRU\05 His answers and decisions\His words - the desk opened.md`: his opening words, his answers 53 to 59, 61 and 62 at the desk's opening, his answers 1 to 7 to Angie's questions, and his later messages. The flags G1 to G15 cited here are the PLAN's list, section "Full-auto decisions", in `C:\AI_Building\AI_PRU\JOBS\01 PRU 2027 budget dashboard - 2026-11-19 HOME\PLAN.md` (R-0150).

## The checks so far

Angie's blind checks (R-1875), in order. Their FAILs count on a path of their own, two to each step: program, new shape, smaller, stop (R-1876).
- check 1, plan, FAIL 1: `C:\AI_Building\AI_MISC\06 Benches\2026-11-20 PRU job 01 plan blind check - ANGIE-HOME\FINDINGS.md`
- check 2, plan, FAIL 2: `C:\AI_Building\AI_MISC\06 Benches\2026-11-20 PRU job 01 plan blind check - ANGIE-HOME\FINDINGS round 2.md`; with it, the page: `C:\AI_Building\AI_MISC\06 Benches\2026-11-20 PRU job 01 page blind check - ANGIE-HOME\FINDINGS round 1.md`
- check 3, plan and page, FAIL 3: `C:\AI_Building\AI_MISC\06 Benches\2026-11-20 PRU job 01 plan blind check - ANGIE-HOME\FINDINGS round 3.md`. Piston picked the new shape, the P&L alone (R-1878).
- check 4, plan and page in the new shape, FAIL 4 (page PASS, plan 11 findings): `C:\AI_Building\AI_MISC\06 Benches\2026-11-20 PRU job 01 plan blind check - ANGIE-HOME\FINDINGS round 4.md`
- check 5, plan and test, FAIL 5 (plan 2, test 5; none on the page): `C:\AI_Building\AI_MISC\06 Benches\2026-11-20 PRU job 01 blind check 5 - ANGIE-HOME\FINDINGS check 5.md`. Piston picked the smaller shape: `C:\AI_Building\AI_HQ\03 Library\PISTON PICK - PRU job 01 third blind-check FAIL - 2026-11-20 HOME.md` (md5 ca3d554bfef5e49a916a517253c04844). That file records both counts, Angie's "third on the new-shape step" and LAWYER's "fifth overall"; this GOAL counts by LAWYER's.
- **check 6 (agent 7) checks this GOAL before LAWYER sees it again (R-1877).** A FAIL there is FAIL 6, the second on the "smaller" step. **A seventh FAIL stops the job** (R-1876): nothing more is built for release 1, and Piston and Sergio are told.
- These findings files were saved by Angie from each checker's hand-back, in substance and not in the checker's own words (LAWYER's risk 2).

LAWYER round 1 failed this GOAL and the PLAN (12 findings): `C:\AI_Building\AI_LAWYER\Office desk\Verdicts\2026-11-20 Angie PRU job 01 release 1 plan check - ccc6409e.md`. Piston's word, 2026-11-20 03:00: Angie repairs all 12, then agent 7 checks, and LAWYER again only on its PASS.

## Who does what

- Angie builds the page, its program and its test on her bench in `C:\AI_Building\AI_MISC\06 Benches\` (R-0448). [answer 55: "Angie builds, Rick advises (Recommended)"]
- Rick answers Angie's questions and writes nothing in `C:\AI_Building\AI_PRU`. [answer 55]
- Angie's blind checker, then LAWYER, check it (R-1875, R-1877). Sergio alone accepts the page (R-0180). Piston picks shapes and decisions in his place ("Piston picks on my behalf"), but he does not accept the page. The Brain puts it live on ONE VIEW. [answer 59: "Angie builds, Brain puts live (Recommended)"]

## Release 1: the page for 9am - the P&L alone, its figures proved

His words: "ill need something in ONE VIEW for tomorrow 9am MANDATORY." The shape is Piston's, picked in his place and his to strike:
- the P&L alone, after check 3. Piston's message, 2026-11-20 02:05, is logged word for word in `C:\AI_Building\AI_PRU\LOG.md`: "If it comes, I'll pick: deliver only the P&L tab for 9am."
- its figures alone proved, after check 5. See the PISTON PICK file above.

The Weekly tab is release 1b.

**R1-1. One page, `C:\AI_Building\AI_MISC\06 Benches\2026-11-20 PRU job 01 page - ANGIE-HOME\PRU 2027 Budget - DRAFT.html`, frozen at md5 3fbc07586d0a54a78c7224c77b4fe5ad, holding the P&L alone.** It is built by `C:\AI_Building\AI_MISC\06 Benches\2026-11-20 PRU job 01 page - ANGIE-HOME\build_page.py --pl-only`. Its file holds:
- no internet reference;
- light and dark CSS and a light/dark button;
- the text "Draft budget, not approved";
- the two source md5s;
- a line starting "Not on this page yet", saying the weekly measures and the coach and class measures are not on it yet;
- nothing from the student log: no figure, no md5, no file name.

Sources:
- no internet and light and dark: Rick's store pages, `C:\AI_Building\AI_Financials\.claude\skills\fs-budget-store-pages\SKILL.md` line 31: "one file that opens with no internet, light and dark";
- the Draft text: the same file, line 23: Keep "Draft budget, not approved" on until Sergio's final lock;
- nothing from the student log: the Conductor's brief that opened this desk's run, in Angie's session transcript 034bc097-973b-403b-8a90-c7678efdb939: "Open no customer data. Name source files only.";
- the button and the md5s on the page: Angie's full-auto decisions, G14 and G15.

**R1-2. PRU's whole P&L, 2025, 2026 and 2027, in the page's data and as figure cells.** [answer 1: "i want P&L same as rick"; answer 2: "2025, 2026, 2027 side by side"] The year view shows the three years side by side, one column each. Each month view shows one year's twelve months and its year (G13). Each figure is read by program; none is typed.
- **A line** is a row of PRU-pl from 8 to 103 that has a label in column B or a month figure that is not zero, in PRU-pl's own order. Rows with neither are left out.
- **A heading** is a line whose twelve month cells are empty in all three years (2027 row, 2026 row, 2025 row). It shows no figures. (The program decides it from the 2027 row alone; on these sources both give the same 9 headings. LAWYER's risk 3.)
- **Row 21** has no label and holds ratios from 0.62 to 0.80:
  - in 2026 and 2027 each equals gross profit (row 20) over total sales (row 14);
  - in 2025 one cell does not: PRU-Prior U21 (December) holds 0.7096, which repeats November's T21, where U20/U14 gives 0.7818;
  - the page carries every cell as the source holds it, as percents, with no year figure and no gap;
  - its label in the page's data is "(row 21: a ratio, shown as a percent; no label in the source)" (G11);
  - the program refuses to run if row 21 gains a label or a value above 1.5 (its function `ratio_ok`).
- 2027: `C:\AI_Building\AI_Financials\04 Budget\2027\rolled\02 - Consolidated SGP Budget light.xlsx` (md5 64e3c1ecdf01ee25cae717657952bfbe), sheet PRU-pl. Months in columns D, E, F, I, J, K, N, O, P, S, T, U; the year in Y ("2027B").
- 2026: the same sheet, the block headed "2026 - Prior Year", matched by position: each line's row plus 108 (rows 116-211), the same columns, the year in Y ("Total"). PRU-pl B184 reads "Repairs and Maintenance - Building" where B76 reads "Insurance - Building"; the page shows a note saying so (G6).
- 2025: `C:\AI_Building\AI_Financials\04 Budget\2027\raw files\3 Operating statements\02 - Operating Statements 2026-09.xlsx` (md5 c2b949723c5f30e369b831404a90ce37), sheet PRU-Prior, **the same row** as PRU-pl. Its column B equals PRU-pl's on every line's row; the test checks this first (SOURCE CHECKS). It uses the same twelve month columns as `C:\AI_Building\AI_Financials\04 Budget\2027\scripts\fs_budget_pru_2026.py` reads (its MONTHS list); the year is in Y ("Total").
- **A year figure is the source's own year cell.** Where a line's twelve months miss that cell by more than $1 (25 lines in 2025, none in 2026 or 2027; row 21 exempt), the page's data lists the line as a gap (G8). How the gap is drawn (a * and a tooltip) is not claimed for 9am.

**R1-3. A test, by program, `C:\AI_Building\AI_MISC\06 Benches\2026-11-20 PRU job 01 page - ANGIE-HOME\test_page_pl.py`, that fails on each of these 10 cases and passes on none.**
- Before the cases it runs SOURCE CHECKS: PRU-Prior's column B equals PRU-pl's on every line's row, and row 21 is still an unlabelled row of ratios no higher than 1.5.
- A figure matches within $0.005 of its source cell; the page carries the cell's full value.
- The test renders each view of the page in node and compares every figure cell, rounded as the page rounds: half up, whole dollars, negatives in brackets.

The cases:
1. a month figure differs from its source cell (any year, line or month), in the data or as a figure cell;
2. a year figure differs from its source's year cell, in the data or as a figure cell; a gap (R1-2) is missing from the page's data, or one is listed that does not exist, or row 21 is listed;
3. a line is missing or one is added; the lines are not in PRU-pl's order; a label in the page's data differs from the source's column B (or, where B is empty, from R1-2's stand-in text); a line's heading or ratio flag differs from R1-2's definitions; a heading shows a figure in any view;
4. a year (2025, 2026, 2027) is missing from the data or as a year-view column;
5. the page's file refers to the internet: `http:`, `https:`, `ws:` or `wss:` anywhere; a `//` address in src, href, action, srcset, data or CSS url(); @import, import(), fetch, XMLHttpRequest, WebSocket, EventSource or sendBeacon;
6. the text "Draft budget, not approved" or the "Not on this page yet" line is missing from the page's file;
7. the md5 of either source is not in the page's file;
8. the B184 note is not shown;
9. the dark-theme CSS (`@media (prefers-color-scheme: dark)` and `:root[data-theme="dark"]`) or the light/dark button (`id="theme"`) is missing from the page's file;
10. anything from the student log is in the page's file: weekly data, its md5 or its name.

**Known limits of the test, said plainly (LAWYER's finding 5 and risks).**
- Cases 5, 6, 7, 9 and 10 look for text in the page's file; they do not prove what a browser draws.
- Case 9 checks only that the button's id is present, not that it switches the theme.
- Case 10 knows weekly data only by the key "weekly", which is the key the program uses.
- The source md5s are printed but not compared with this GOAL's; the reader compares them.

**NOT PROVED FOR 9AM: how the page draws.** The figures and the page's data are proved. How they are drawn is not:
- the * gap marks;
- the tooltips;
- the labels as drawn;
- the year list's options;
- the exact words of the "Not on this page yet" line.

This is Piston's pick in Sergio's place after check 5 (the PISTON PICK file above), his to strike. Since check 5 the test holds checks and plants for these five, marked "release 1b" below, and they pass. No blind checker has passed them, so they are claimed in release 1b, not here.

Before the test is believed, it fails on 57 planted faults, one per branch. The five marked "release 1b" test the drawing, which is not claimed for 9am:
- case 1 five (a month in each year, a shown month; release 1b: a tooltip on every month cell);
- case 2 eight (a year, a shown year, a 2025 gap removed, a false 2027 gap, a gap on row 21; release 1b: a tooltip sum wrong, the tooltip removed, the * not drawn);
- case 3 eight (a line removed, a line added, two lines out of order, a label changed, a figure line flagged heading, row 21's ratio flag removed, a heading showing figures; release 1b: labels not drawn);
- case 4 four (each year; release 1b: 2025 by month taken off the view list);
- case 5 seventeen (each internet pattern, `ws:` included);
- case 6 three (the Draft text removed, the not-yet line removed; release 1b: its middle words changed);
- case 7 two (each md5); case 8 one; case 9 two (the CSS, the button); case 10 three (weekly data, the log's md5, its name);
- SOURCE CHECKS two (a PRU-Prior label changed, row 21 given a label);
- the program's refusal two: `ratio_ok` in `C:\AI_Building\AI_MISC\06 Benches\2026-11-20 PRU job 01 page - ANGIE-HOME\build_page.py` refuses row 21 with a label and with a value above 1.5, and accepts the real row 21.

**R1-4. Pass mark of the build.** The test's whole output, `C:\AI_Building\AI_MISC\06 Benches\2026-11-20 PRU job 01 page - ANGIE-HOME\TEST_OUTPUT_PL.txt`, shows:
- the two source md5s and the page's md5 3fbc07586d0a54a78c7224c77b4fe5ad;
- SOURCE CHECKS PASS;
- PASS on all 10 cases;
- "program refusal, real row 21: PASS - accepted";
- each of the 57 plants FAIL - caught.

**R1-5. On ONE VIEW for 9am, for his readers, on his yes.** [his words: "ill need something in ONE VIEW for tomorrow 9am MANDATORY"; answer 59; answer 3]
- After LAWYER's PASS, the page is copied unchanged into `C:\AI_Building\AI_PRU\JOBS\01 PRU 2027 budget dashboard - 2026-11-19 HOME\`.
- Sergio is asked the go-live question (PLAN, section "His 9am question").
- On his yes, the Brain puts the page live on ONE VIEW for his readers: Sergio, Kim Harrison, Richard Stein and "angel aerls, PRU manager" (G4; who that is stays his to say).
- **Pass mark:** the Brain reports the page live on ONE VIEW by 9am, 2026-11-20, with the page's md5 equal to 3fbc07586d0a54a78c7224c77b4fe5ad and those readers named.
- Without his yes nothing goes live (LAWYER's risk 1). This pass mark is outside Angie's hands, and only Sergio accepts it.

## Release 1b (after 9am): the drawing, then the Weekly tab

Release 1b is built and checked as release 1 is, with a goal section of its own before it goes on the page.
- First, how the release 1 page draws is claimed and blind-checked: the * marks, the tooltips, the labels as drawn, the year list, and the "Not on this page yet" line word for word. These are check 5's findings C-1 to C-5.
- Two faults the blind check found are repaired before the Weekly tab: course names typed in the program (no source) come off or get a source; and "weeks after today are bookings ahead" is said only with a source.

**R1b-1. Tab Weekly: number of students, and the sales half of range and class profitability, one point per week, every week from the first to the newest week-ending date in the source; a week with no registrations shows 0.** [answer 61: "Part of job 01"; answer 4: "Build the three found first"] Profit comes in release 2 (G1).
- Number of students: registration rows counted per week-ending date. One row is one registration: a student on two courses counts twice. The page says so (G9).
- Sales by class: the sum of Total Fee per week, by course.
- Sales by range: the sum of Total Fee per week, by site.
- Source: `C:\Users\Sergio\Downloads\2026 PRU Manual Log v3.xlsx` (md5 ab99689da045431d30dda84f57000c76, 6,464,527 B, 21 sheets, sheet Master among them). He sent it in Angie's chat, 2026-11-20 00:29: @"C:\Users\Sergio\Downloads\2026 PRU Manual Log v3.xlsx".
  - It is not the live log he named first, `H:\Shared drives\Accounting\09-Daily Reports\2026 PRU\2026 PRU Manual Log v.3.xlsx` (662,493 B, 2 sheets, no sheet Master). Both sheet counts were read by openpyxl from the sheet names alone, 2026-11-20 about 03:01. The Downloads file is used because it holds Master (G10).
  - Only these columns are read: Site, Course, WE Dt, Total Fee. The program reads no name, email or ID column, and writes only weekly totals.
  - Rows with no week-ending date are not counted; the page gives their number and their Total Fee in dollars.
  - Ranges are shown by the site codes the log uses; no plain names are in a source read here (G12).
  - The file is never copied into `C:\AI_Building\AI_PRU`.
- Not in release 1: coach pass rate, coach profitability and class fill rate. They wait on his file (answer 6: "skip for now, ill send it later"). The page says so in one line.

## Release 2 (after 9am)

- **R2-1. Range profit per week:** range sales, less that range's rent, less its share of coach pay.
  - Rent comes from the GL accounts 785xx-30, one per site, in `C:\AI_Building\AI_Financials\00 Raw data\GL\2026 YTD 101E GL History Detail Postings - All Accounts.csv`, Store POW. This is Rick's read (his claim, R-0022).
  - Coach pay is account 72200-30, spread by students. [answer 7: "Spread coach pay by students"]
  - The page labels it an estimate.
- **R2-2. Class profit per week:** class sales less its share of coach pay, by students. Labelled an estimate. [answer 7]
- **R2-3. The 2027 sales goal planner.** [answer 1: "I want a 2027 Goal planner for the sales part, same as builder did for sales. A better version of the excel planner they used last year"; his message: "i need something more user friendly, that can be carrued into 2027"] Its MUSTs, cases and pass mark are written in a goal file of its own before it is built, checked the same way.

Coach pass rate, coach profitability and class fill rate join when his file comes (answer 6).
