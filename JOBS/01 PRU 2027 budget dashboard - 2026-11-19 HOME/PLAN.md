# PLAN - job 01, PRU 2027 budget dashboard - DRAFT

Angie, 2026-11-20 HOME. Not checked by LAWYER. Nothing is built until LAWYER has checked this plan and `GOAL.md`, and Sergio has said yes (R-1879, R-1809). His answers 1 to 5 and his message about last year's planner are in `C:\AI_Building\AI_PRU\05 His answers and decisions\His words - the desk opened.md`.

## Bad news first

1. **No source found for 3 of the 6 weekly measures:** coach pass rate, coach profitability, class fill rate. They seem to live in the MSI5 registration system (the website's booking links name book `POWERRIDEU`, https://www.powerrideuniversity.com/schedule-your-class, read 2026-11-20) and in coach pay. Angie has no MSI5 login and makes none. His answer 4: "Build the three found first". These three wait.
2. **For the other three, only sales were found, not costs.** No 2026 file splits coach pay or range rent by class or range. His answer 5: "Ask Rick for costs". Class and range profitability wait on Rick's answer.
3. ~~The weekly student source is a snapshot.~~ Closed 2026-11-20: he named the live log, `H:\Shared drives\Accounting\09-Daily Reports\2026 PRU\2026 PRU Manual Log v.3.xlsx` (662,493 B, saved 2026-11-19 10:41, md5 de908b10884b9b5a6bde8d6b4199da38; the same two sheets as Rick's copy).

4. **The Google Sheet he sent cannot be opened by this desk.** Sheet id 1hTnf1S60SBZRwt8NCQbqkqPyihLIvYA8qBmeJ3Z7tRs: the Drive connector, signed in as the gmail account, answers "Requested entity was not found" (2026-11-20). Per `C:\AI_Building\AI_PRC
 Google Drive map\DRIVE MAP.md`, this means the connector's account cannot see it, not that it is missing. What it holds: unknown. The two `.gsheet` links in `H:\Shared drives\PRU ANALYSIS\Monthly PRU Registrations6 Rems Data Files (From Coko)\` cannot be read from disk either.
5. **His work folder `003 - PRU` holds no 2026 cost file.** Of its 702 files, the 10 changed since 2025-01-01 are licenses, contractor agreements, a Clarksburg lease draft, `08 - Workflow\Workflow.xlsx` and a returns note (listed by name, 2026-11-20). Its coach-pay and by-range files are from 2021 and 2022.

6. **The full log, sent by him 2026-11-20:** `C:\Users\Sergio\Downloads\2026 PRU Manual Log v3.xlsx` (6,464,527 B, md5 ab99689da045431d30dda84f57000c76), 21 sheets, against 2 in the copy on H:. Read by column headers only; it holds student records and is never copied into `C:\AI_Building\AI_PRU` (the folder goes online). Sheet `Master` has one row per registration, with columns Site, Class, Course, WE Dt (the week-ending date), Total Fee, Disc $, the promo columns and Class Date. That gives **students per week, and sales per week by range (Site), by class and by course.** Sheet `26 Rent Schedule` ("Range Rental Schedule", 2026) is **a cost source for range rent.** It has no column for the coach and none for pass or fail, so coach pass rate and coach profit still have no source. Its `Ecourse File` seat columns belong to the e-course link, not the classes, so class fill rate has none either. On reading these headers, 3 student rows from each of `Master` and `Ecourse File` were printed in the session; the mistake form went to the Legislator through the Conductor.

## What the job delivers (his answers 1 to 3)

| piece | what it shows | model | source |
|---|---|---|---|
| A. PRU 2027 P&L page | every line of PRU's P&L, "same as rick"; 2025, 2026 and 2027 side by side (his answer 2) | Rick's store pages, `C:\AI_Building\AI_Financials\04 Budget\2027\reports\Falls Church 2027 Budget - DRAFT.html`, made by the skill fs-budget-store-pages | 2027 and 2026: sheet PRU-pl of `C:\AI_Building\AI_Financials\04 Budget\2027\rolled\02 - Consolidated SGP Budget light.xlsx` (md5 64e3c1ecdf01ee25cae717657952bfbe on 2026-11-20; the 2027 months are in columns D to U, the 2027 total under "2027B", 2026 under "2026", read from row 6). 2025: sheet PRU-Prior of `C:\AI_Building\AI_Financials\04 Budget\2027\raw files\3 Operating statements\02 - Operating Statements 2026-09.xlsx`, as Rick's `fs_budget_pru_2026.py` reads it (its docstring) |
| B. PRU 2027 sales goal planner | the Training sales built up by course and month, 2027 numbers he can change, the totals moving with them; "a better version of the excel planner they used last year" that "can be carrued into 2027" (his answer 1, his message) | Rick's 2027 Goal Setting page, `C:\AI_Building\AI_Financials\04 Budget\2027\2026-11-12 budget table - rick RICK-HOME-1111\GOAL PAGE RULES.md`: changeable boxes, a draggable monthly curve, marks where 2027 is under 2026, saved to a file. He said "same as builder did for sales": Angie takes this page to be the one he means (unverified) | last year's planner, `H:\Shared drives\Accounting\08-Budget\2026 Budget\PRU\2026 PRU Budget v3 final.xlsx` (md5 c06d1386a8568837aed681ec310bf102; sheets `2026 Summary`, `2026 Trend`, Jan to Dec, `25Classes`, `25Rev`, `2025 Sum`, `25 Detail`, `2024 Sum`, `2024 Summary`); the 2027 opening figures from PRU-pl's Training line, so the planner and the P&L page agree |
| C. The weekly school measures | one point per week, coaches by name (his answer 62) | - | table below |

All three are one offline page per piece (or one page with tabs, the simpler on the day), printed by program, "Draft budget, not approved" on until his lock. Readers on ONE VIEW (his answer 3): Sergio, Kim Harrison, Richard Stein, Angel Aerls (PRU manager). Angel Aerls is in no Brain file Angie read (`C:\AI_Building\AI_Brain\wiki\people.md`, searched 2026-11-20): the Brain gets the name for its readers file when the page goes live.

## A source for each weekly measure

File names and sheet names only; no cell of these was opened (no customer data).

| measure | source found | state |
|---|---|---|
| Number of students | the live log, `H:\Shared drives\Accounting\09-Daily Reports\2026 PRU\2026 PRU Manual Log v.3.xlsx` (his message, 2026-11-20; Rick's copy of 2026-11-08 is `C:\AI_Building\AI_Financials\04 Budget\2027\raw files\2 Sales and GP\2026 PRU Manual Log v.3 - saved 2026-11-08.xlsx`), sheet `Copy of WklyConsolidating Wd`, a weekly sheet (`fs_budget_pru_2026.py`, its notes). 2025: `H:\Shared drives\PRU ANALYSIS\Monthly PRU Registrations\2025 Data Files\2025 PRU Registrations by Month.xlsx` (md5 340720a87ba2f2e4dcaaa497de68db4e). 2026 also named: `H:\Shared drives\PRU ANALYSIS\Monthly PRU Registrations\2026 Rems Data Files (From Coko)\Daily Registrations by Month 2026.gsheet` (a Google Sheet link, not read) | FOUND, to confirm: whether the weekly sheet holds a student count, by its row labels only |
| Class profitability | sales: the same log; `H:\Shared drives\PRU ANALYSIS\Conversions Analysis\01 - PRU $ by range by class.xlsx` (md5 5a4bcfaf5f0425b77da9e362552afe8c, to 2025-09). Costs: none found | SALES ONLY, waits on Rick (his answer 5) |
| Range profitability | sales: the same two files. Costs: none found for 2026; a 2022 one-off exists, `C:\Users\Sergio\My Drive (spagnini@wherethepoweris.com)\003 - PRU\03-Financial Models\2022 Performance\08-Aug\PRU Performance By Range Aug-2022.xlsx` | SALES ONLY, waits on Rick (his answer 5) |
| Class fill rate | none (seats offered per class are in MSI5) | NO SOURCE, waits (his answer 4) |
| Coach pass rate | none (pass or fail per class is in MSI5) | NO SOURCE, waits (his answer 4) |
| Coach profitability | none for 2026; 2021-22 coach pay files only, in `C:\Users\Sergio\My Drive (spagnini@wherethepoweris.com)\003 - PRU\04-Coach Counts\` | NO SOURCE, waits (his answer 4) |

## Steps

1. LAWYER checks this plan and the updated `GOAL.md`; Sergio says yes. (R-1809, R-1879)
2. The Conductor relays to Rick: does the general ledger split PRU's coach pay and range rent by range or class? (his answer 5; questions to other desks go through the Conductor)
3. Bench in `C:\AI_Building\AI_MISC\06 Benches\`. Write `CHOICES.json` from his answers 1 to 3.
4. Build A, the P&L page, by program from PRU-pl and PRU-Prior, with its test (GOAL.md item 4).
5. Build B, the planner: read last year's planner's summary sheets (not `25 Detail`, which may hold student rows) to take its course list and method; print the page.
6. Build C for students now; class and range profit when Rick answers; the other three when a source arrives.
7. Own tests, then the blind checker, then LAWYER (R-1875, R-1877); Sergio accepts; the Brain puts it live.
