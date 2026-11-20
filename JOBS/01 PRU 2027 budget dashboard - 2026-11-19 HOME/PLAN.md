# PLAN - job 01, PRU 2027 budget dashboard - DRAFT, repair round 4 (P&L alone for 9am)

Angie, 2026-11-20 HOME. The goal is `C:\AI_Building\AI_PRU\JOBS\01 PRU 2027 budget dashboard - 2026-11-19 HOME\GOAL.md`. His words are in `C:\AI_Building\AI_PRU\05 His answers and decisions\His words - the desk opened.md`. The run is full auto on his word: "im going to sleep, go ahead full auto. plan is accepted when the lawyer passes. Piston picks on my behalf. ill need something in ONE VIEW for tomorrow 9am MANDATORY."

## Bad news first

1. Coach pass rate, coach profitability and class fill rate have no source. His answer 6: "skip for now, ill send it later". They are not in release 1.
2. The GL does not split coach pay by range or class: account 72200-30 names employees. That is Rick's read of `C:\AI_Building\AI_Financials\00 Raw data\GL\2026 YTD 101E GL History Detail Postings - All Accounts.csv` (his claim, R-0022). So range and class profit spread coach pay by students, his answer 7 ("Spread coach pay by students"). It is an estimate, labelled as one, in release 2.
3. The Google Sheet he sent (id 1hTnf1S60SBZRwt8NCQbqkqPyihLIvYA8qBmeJ3Z7tRs) is not visible to the Drive connector, which answers "Requested entity was not found". The file he then downloaded, `C:\Users\Sergio\Downloads\2026 PRU Manual Log v3.xlsx`, has the same name. Whether it is the same sheet: unverified.

## One source per measure

| measure | file | sheet, columns | state |
|---|---|---|---|
| P&L 2027 | `C:\AI_Building\AI_Financials\04 Budget\2027\rolled\02 - Consolidated SGP Budget light.xlsx` (md5 64e3c1ecdf01ee25cae717657952bfbe) | PRU-pl rows 8-103; months D, E, F, I, J, K, N, O, P, S, T, U; year Y. Columns G, L, Q, V are quarter totals and H, M, R are percents, never read as months | release 1 |
| P&L 2026 | the same file | PRU-pl rows 116-211 ("2026 - Prior Year"), the same columns | release 1 |
| P&L 2025 | `C:\AI_Building\AI_Financials\04 Budget\2027\raw files\3 Operating statements\02 - Operating Statements 2026-09.xlsx` | md5 c2b949723c5f30e369b831404a90ce37; PRU-Prior, the same rows (labels equal on every row), the same twelve month columns, year Y | release 1 |
| Number of students | `C:\Users\Sergio\Downloads\2026 PRU Manual Log v3.xlsx` (md5 ab99689da045431d30dda84f57000c76; he sent it 00:29; not the H: live log, G10) | Master: WE Dt, a count of rows | release 1b (after 9am) |
| Class sales (profit in release 2) | the same file | Master: WE Dt, Course, Total Fee | release 1b (after 9am) |
| Range sales (profit in release 2) | the same file | Master: WE Dt, Site, Total Fee | release 1b (after 9am) |
| Range rent | the GL CSV above, accounts 785xx-30, Store POW (Rick's claim); also the log's sheet `26 Rent Schedule` | | release 2 |
| Coach pay | the GL CSV, account 72200-30 (Rick's claim) | | release 2 |
| Coach pass rate, coach profit, class fill rate | none | | waits on his file (answer 6) |

Release 1b only: the student rows stay out of `C:\AI_Building\AI_PRU`. The program reads Master in place, reads only the columns named, and writes weekly totals. Release 1 reads nothing from the log; its test reads the file's bytes only for the md5 that must not be on the page.

## Full-auto decisions made in his place, flagged (to Piston, 2026-11-20 01:16)

- G1. Release 1 was one page with two tabs; the new shape (below) replaced that: release 1 is the P&L tab alone, the Weekly tab is release 1b. Range and class profit, then the planner, come after 9am.
- G2. The page is built on the bench while LAWYER checks this plan, because of the 9am deadline. Nothing goes live without LAWYER's PASS on the page.
- G3. "same as builder did for sales" is read as Rick's 2027 Goal Setting page, `C:\AI_Building\AI_Financials\04 Budget\2027\2026-11-12 budget table - rick RICK-HOME-1111\GOAL PAGE RULES.md`.
- G4. Readers: "me kim richrd and angel aerls, PRU manager" is read as four people.
- G5. Release 1b only (release 1 has no name scan; its case 11 proves nothing from the log is on the page): the name scan looks for full names, first and last of one row; single words that equal some name are listed, not failed. Why: the scan on every single value failed on 12 ordinary page words ("may", "cash", "wood", "sergio" in a file path...).
- G6. PRU-pl B184 reads "Repairs and Maintenance - Building" where its 2027 row B76 reads "Insurance - Building". The 2026 row is kept by position (row + 108) and the page says so in a note.
- G7. Withdrawn in repair round 2: 2025 is read from the same row (labels equal on every row), so the duplicate "Training" needs no rule.
- G8. A year figure is the source's own year cell. 25 rows of PRU-Prior miss their Total by more than $1 against their twelve months; the page marks each with * and shows the month sum. Which is right is his to say.
- G9. One registration row is one student; a student on two courses counts twice. The page says so.
- G10. The weekly source is the Downloads file he sent at 00:29 (21 sheets, holds Master), not the H: live log he named first (2 sheets: "Copy of 2026 Summary", "Copy of WklyConsolidating Wd"; no Master).
- G11. PRU-pl row 21 (no label, ratios 0.62-0.80) is shown as percents with no year.
- G12. Ranges are shown by their site codes; no plain names are in a source read here.
- G13. "side by side": the year view shows the three years side by side; the month view shows one year at a time, picked from a list.
- New shape after the third checker FAIL (R-1878), Piston's pick: release 1 is the P&L tab alone; the Weekly tab is release 1b, after 9am.
- G2 is put to Piston for his pick (round-2 finding 15): the page was built before LAWYER's PASS on the plan.
- Piston's picks in his place, 2026-11-20 ~02:15, each his to strike: G1 to G7 stand (G1 since replaced by the new shape, G5 since moved to release 1b, G7 withdrawn); G2 is fine ("build on the bench while LAWYER checks the plan. Nothing goes live without LAWYER's PASS on the page itself").
- The acceptance: Piston does NOT accept the page in his place ("accepting work is his alone"). The page goes to Piston with LAWYER's verdict by 07:30 at the latest; Piston puts a one-tap question to him when he is back; the Brain puts it live on his yes. If LAWYER fails the page, the part that passes goes (the P&L tab alone is enough).

## Steps, agents and models

Agents launched so far: 5, all Opus blind checkers, numbered as in the list of checks in `C:\AI_Building\AI_PRU\JOBS\01 PRU 2027 budget dashboard - 2026-11-19 HOME\GOAL.md`: checks 1 to 4 (check 2 ran as two agents). The cap was 5. Check 4 passed the page and failed the plan with 11 findings. Piston said yes to one more agent (step 7): check 5, of the repaired GOAL, PLAN and test, with the page unchanged. The cap is now 6, and all 6 are used. Check 5 failed with 7 findings, none of them on the page: `C:\AI_Building\AI_MISC\06 Benches\2026-11-20 PRU job 01 blind check 5 - ANGIE-HOME\FINDINGS check 5.md`. That is the step's third FAIL, so the smaller shape is Piston's pick (R-1878). LAWYER is a desk of its own. The Brain puts the page live.

| # | step | who | done when | minutes | state |
|---|---|---|---|---|---|
| 1 | Plan repair rounds 1 and 2 (20, then 19 findings) | Angie | both files rewritten | 15 | done |
| 2 | Blind checks 1 to 3 | checker agents (Opus) | PASS | 20 | FAIL each; the plan's third FAIL went to Piston |
| 3 | The page program and the page on the bench `C:\AI_Building\AI_MISC\06 Benches\2026-11-20 PRU job 01 page - ANGIE-HOME\` | Angie (answer 55) | the page exists | 45 | done |
| 4 | New shape (Piston's pick): the P&L tab alone, `C:\AI_Building\AI_MISC\06 Benches\2026-11-20 PRU job 01 page - ANGIE-HOME\build_page.py --pl-only`; its test `C:\AI_Building\AI_MISC\06 Benches\2026-11-20 PRU job 01 page - ANGIE-HOME\test_page_pl.py` | Angie | PASS, every plant FAIL | 30 | done (own test, not a verdict) |
| 5 | Plan repair round 3 for the new shape (8 + 2 findings) | Angie | GOAL and PLAN rewritten | 15 | done |
| 6 | Blind check 4, plan and P&L page together | checker agent (Opus) | PASS | 20 | page PASS; plan FAIL 11 |
| 6b | Repair of check 4's 11 findings: text in GOAL and PLAN; 10 new plants in the test (52 in all); the row-21 refusal moved into `ratio_ok`, the page's output unchanged | Angie | own test PASS, 52 of 52 caught | 20 | done (own test, not a verdict) |
| 7 | Blind check 5, of the repaired GOAL, PLAN and test (the page unchanged) | checker agent (Opus); Piston's yes in his place, 2026-11-20 between 02:28 and 02:42, his to strike ("yes to agent 6, a blind check of the repaired GOAL/PLAN/test only, then LAWYER"); the page stays frozen at 3fbc0758; a FAIL here is the step's third, and Piston picks the smaller shape (R-1878) | PASS | 20 | FAIL (A 2, C 5); smaller shape to Piston |
| 8 | Plan and page to LAWYER (session local_5fb2d9ed-2bc2-4e00-8229-4baba6e00ef6) | Angie sends | LAWYER's PASS on both | - | |
| 9 | Path, md5 and verdict to Piston by 07:30; his yes asked by Piston when he is back; page into the job folder; the Brain puts it live | Angie / Piston / the Brain | live on ONE VIEW | - | |
| 10 | Release 1b (the Weekly tab), then release 2 | Angie, then the same checks | - | - | after 9am |

Each check lists every fail it finds. There are two FAILs per repair step (R-1876, R-1880).
