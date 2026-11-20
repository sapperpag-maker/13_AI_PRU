# PLAN - job 01, PRU 2027 budget dashboard - DRAFT, repair round 1

Angie, 2026-11-20 HOME. The goal is `GOAL.md`, beside this file. His words are in `C:\AI_Building\AI_PRU\05 His answers and decisions\His words - the desk opened.md`. The run is full auto on his word: "im going to sleep, go ahead full auto. plan is accepted when the lawyer passes. Piston picks on my behalf. ill need something in ONE VIEW for tomorrow 9am MANDATORY."

## Bad news first

1. Coach pass rate, coach profitability and class fill rate have no source. His answer 6: "skip for now, ill send it later". They are not in release 1.
2. The GL does not split coach pay by range or class: account 72200-30 names employees. That is Rick's read of `C:\AI_Building\AI_Financials\00 Raw data\GL\2026 YTD 101E GL History Detail Postings - All Accounts.csv` (his claim, R-0022). So range and class profit spread coach pay by students, his answer 7 ("Spread coach pay by students"). It is an estimate, labelled as one, in release 2.
3. The Google Sheet he sent (id 1hTnf1S60SBZRwt8NCQbqkqPyihLIvYA8qBmeJ3Z7tRs) is not visible to the Drive connector, which answers "Requested entity was not found". The file he then downloaded, `C:\Users\Sergio\Downloads\2026 PRU Manual Log v3.xlsx`, has the same name. Whether it is the same sheet: unverified.

## One source per measure

| measure | file | sheet, columns | state |
|---|---|---|---|
| P&L 2027 | `C:\AI_Building\AI_Financials\04 Budget\2027\rolled\02 - Consolidated SGP Budget light.xlsx` (md5 64e3c1ecdf01ee25cae717657952bfbe) | PRU-pl rows 8-103; months D, E, F, I, J, K, N, O, P, S, T, U; year Y. Columns G, L, Q, V are quarter totals and H, M, R are percents, never read as months | release 1 |
| P&L 2026 | the same file | PRU-pl rows 116-211 ("2026 - Prior Year"), the same columns | release 1 |
| P&L 2025 | `C:\AI_Building\AI_Financials\04 Budget\2027\raw files\3 Operating statements\02 - Operating Statements 2026-09.xlsx` | PRU-Prior, rows matched by the column B label, the same twelve month columns | release 1 |
| Number of students | `C:\Users\Sergio\Downloads\2026 PRU Manual Log v3.xlsx` (md5 ab99689da045431d30dda84f57000c76) | Master: WE Dt, a count of rows | release 1 |
| Class sales (profit in release 2) | the same file | Master: WE Dt, Course, Total Fee | release 1 |
| Range sales (profit in release 2) | the same file | Master: WE Dt, Site, Total Fee | release 1 |
| Range rent | the GL CSV above, accounts 785xx-30, Store POW (Rick's claim); also the log's sheet `26 Rent Schedule` | | release 2 |
| Coach pay | the GL CSV, account 72200-30 (Rick's claim) | | release 2 |
| Coach pass rate, coach profit, class fill rate | none | | waits on his file (answer 6) |

The student rows stay out of `C:\AI_Building\AI_PRU`. The program reads Master in place, reads only the columns named, and writes weekly totals. The test reads the two name columns only to prove no name is on the page.

## Full-auto decisions made in his place, flagged (to Piston, 2026-11-20 01:16)

- G1. Release 1 is one page with two tabs. Range and class profit, then the planner, come after 9am.
- G2. The page is built on the bench while LAWYER checks this plan, because of the 9am deadline. Nothing goes live without LAWYER's PASS on the page.
- G3. "same as builder did for sales" is read as Rick's 2027 Goal Setting page, `C:\AI_Building\AI_Financials\04 Budget\2027\2026-11-12 budget table - rick RICK-HOME-1111\GOAL PAGE RULES.md`.
- G4. Readers: "me kim richrd and angel aerls, PRU manager" is read as four people.
- G5. The name scan (case 10) looks for full names, first and last of one row; single words that equal some name are listed, not failed. Why: the scan on every single value failed on 12 ordinary page words ("may", "cash", "wood", "sergio" in a file path...).
- G6. PRU-pl B184 reads "Repairs and Maintenance - Building" where its 2027 row B76 reads "Insurance - Building". The 2026 row is kept by position (row + 108) and the page says so in a note.
- G7. "Training" is used twice in PRU-pl (rows 13 and 54). The nth use of a label takes the nth PRU-Prior row with that label.
- Whether Piston accepts the page in his place so it can go live by 9am is Piston's decision, asked of Piston.

## Steps, agents and models

The run launches 4 agents, all on Opus unless named: 2 blind checkers (round 2 of this plan, and the page), and the re-checks a repair needs, at most 2 more. LAWYER is a desk of its own. The Brain puts the page live.

| # | step | who | done when | minutes |
|---|---|---|---|---|
| 1 | Repair this plan and GOAL.md (round 1, 20 findings) | Angie | both files rewritten | 15 |
| 2 | Blind re-check of the plan | checker agent (Opus) | PASS | 20 |
| 3 | Build the page program and the page on the bench `C:\AI_Building\AI_MISC\06 Benches\2026-11-20 PRU job 01 page - ANGIE-HOME\` | Angie (Angie builds, answer 55) | the page and program exist | 45 |
| 4 | The test and its 10 plants | Angie | PASS, with every plant FAIL | 30 |
| 5 | Plan to LAWYER (session local_5fb2d9ed-2bc2-4e00-8229-4baba6e00ef6) | Angie sends | LAWYER's verdict | - |
| 6 | Blind check of the page | checker agent (Opus) | PASS | 20 |
| 7 | Page to LAWYER | Angie sends | LAWYER's PASS | - |
| 8 | Page into the job folder; accept record by whoever accepts; the Brain puts it live | Piston / the Brain | live on ONE VIEW | - |
| 9 | Release 2 | Angie, then the same checks | - | - |

Each check lists every fail it finds. There are two FAILs per repair step (R-1876, R-1880).
