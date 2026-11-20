# PLAN - job 01, PRU 2027 budget dashboard - DRAFT, repair round 7 (smaller shape: P&L alone, its figures proved, for 9am)

Angie, 2026-11-20 HOME. The goal is `C:\AI_Building\AI_PRU\JOBS\01 PRU 2027 budget dashboard - 2026-11-19 HOME\GOAL.md`. His words are in `C:\AI_Building\AI_PRU\05 His answers and decisions\His words - the desk opened.md`. The run is full auto on his word: "im going to sleep, go ahead full auto. plan is accepted when the lawyer passes. Piston picks on my behalf. ill need something in ONE VIEW for tomorrow 9am MANDATORY."

## Bad news first

1. How the page draws is not proved for 9am: the * gap marks, tooltips, labels as drawn, the year list and the not-yet line's exact words. Only its figures and data are. This is Piston's pick after check 5 (GOAL, "NOT PROVED FOR 9AM").
2. Six of Angie's blind checks have failed. A FAIL of check 7 (agent 8) is the seventh and stops the job (R-1876); the 9am call then goes to Sergio himself.
3. Nothing goes live at 9am without Sergio's own yes (R-0180). If he does not answer, ONE VIEW has nothing new at 9am.
4. 2025: 25 lines of PRU-Prior do not add up to their own Total by more than $1 (G8). `C:\AI_Building\AI_Financials\04 Budget\2027\scripts\fs_budget_pru_2026.py` lines 72-79 say PRU-Prior's December cost and expense cells carry year-end entries booked after January. The page shows the source's Total. Which figure is right is his to say.
5. Coach pass rate, coach profitability and class fill rate have no source. His answer 6: "skip for now, ill send it later". They are not in release 1.
6. The GL does not split coach pay by range or class: account 72200-30 names employees. That is Rick's read of `C:\AI_Building\AI_Financials\00 Raw data\GL\2026 YTD 101E GL History Detail Postings - All Accounts.csv` (his claim, R-0022). So range and class profit spread coach pay by students (his answer 7, "Spread coach pay by students"): an estimate, labelled as one, in release 2.
7. The Google Sheet he sent (id 1hTnf1S60SBZRwt8NCQbqkqPyihLIvYA8qBmeJ3Z7tRs) is not visible to the Drive connector, which answers "Requested entity was not found". The file he then downloaded, `C:\Users\Sergio\Downloads\2026 PRU Manual Log v3.xlsx`, has the same name. Whether it is the same sheet: unverified.

## One source per measure

| measure | file | sheet, columns | release |
|---|---|---|---|
| P&L 2027 | `C:\AI_Building\AI_Financials\04 Budget\2027\rolled\02 - Consolidated SGP Budget light.xlsx` (md5 64e3c1ecdf01ee25cae717657952bfbe) | PRU-pl rows 8-103; months D, E, F, I, J, K, N, O, P, S, T, U; year Y. Columns G, L, Q, V are quarter totals and H, M, R are percents, never read as months | 1 |
| P&L 2026 | the same file | PRU-pl rows 116-211 ("2026 - Prior Year"), the same columns | 1 |
| P&L 2025 | `C:\AI_Building\AI_Financials\04 Budget\2027\raw files\3 Operating statements\02 - Operating Statements 2026-09.xlsx` (md5 c2b949723c5f30e369b831404a90ce37) | PRU-Prior, the same rows (labels equal on every row), the same twelve month columns, year Y | 1 |
| Number of students | `C:\Users\Sergio\Downloads\2026 PRU Manual Log v3.xlsx` (md5 ab99689da045431d30dda84f57000c76; he sent it 00:29; not the H: live log, G10) | Master: WE Dt, a count of rows | 1b |
| Class sales (profit in release 2) | the same file | Master: WE Dt, Course, Total Fee | 1b |
| Range sales (profit in release 2) | the same file | Master: WE Dt, Site, Total Fee | 1b |
| Range rent | the GL CSV above, accounts 785xx-30, Store POW (Rick's claim); also the log's sheet `26 Rent Schedule` | | 2 |
| Coach pay | the GL CSV, account 72200-30 (Rick's claim) | | 2 |
| Coach pass rate, coach profit, class fill rate | none | | waits on his file (answer 6) |

Release 1 reads nothing from the log; its test reads the file's bytes only for the md5 that must not be on the page. Release 1b: the student rows stay out of `C:\AI_Building\AI_PRU`; the program reads Master in place, reads only the columns named, and writes weekly totals.

## Full-auto decisions

Made in his place and flagged. Each is his to strike.
- G1. Release 1 was one page with two tabs. The new shape replaced that: release 1 is the P&L tab alone, and the Weekly tab is release 1b. Range and class profit, then the planner, come after 9am.
- G2. The page was built on the bench while the plan was still being checked, because of the 9am deadline. Nothing goes live without LAWYER's PASS on the page. Piston: "build on the bench while LAWYER checks the plan, not after. Nothing goes live without LAWYER's PASS on the page itself." (2026-11-20 ~02:15, in Angie's session transcript 034bc097-973b-403b-8a90-c7678efdb939).
- G3. "same as builder did for sales" is read as Rick's 2027 Goal Setting page, `C:\AI_Building\AI_Financials\04 Budget\2027\2026-11-12 budget table - rick RICK-HOME-1111\GOAL PAGE RULES.md`.
- G4. Readers: "me kim richrd and angel aerls, PRU manager" is read as four people. Who "angel aerls" is stays his to say.
- G5. Release 1b only, since release 1 has no name scan: the name scan looks for full names, first and last of one row; single words that equal some name are listed, not failed. Why: a scan of every single value failed on 12 ordinary page words.
- G6. PRU-pl B184 reads "Repairs and Maintenance - Building" where its 2027 row B76 reads "Insurance - Building". The 2026 row is kept by position (row + 108), and the page says so in a note.
- G7. Withdrawn: 2025 is read from the same row, so the duplicate "Training" needs no rule.
- G8. A year figure is the source's own year cell. The 25 PRU-Prior gaps are listed in the page's data; which figure is right is his to say.
- G9. One registration row is one student (release 1b).
- G10. The weekly source is the Downloads file he sent at 00:29: 21 sheets, Master among them. It is not the H: live log he named first, which has 2 sheets and no Master. Both counts were read from sheet names alone by openpyxl, 2026-11-20 about 03:01.
- G11. PRU-pl row 21 (no label, ratios 0.62-0.80) is carried as percents with no year.
- G12. Ranges are shown by their site codes (release 1b).
- G13. "side by side": the year view shows the three years side by side; a month view shows one year at a time.
- G14. The page has a light/dark button: no word of his or Rick's asks for it; it follows Rick's "light and dark".
- G15. The page prints the two source md5s, so a reader can tie it to its sources: no word of his asks for it; Rick's skill hands back each file "with its md5" (`C:\AI_Building\AI_Financials\.claude\skills\fs-budget-store-pages\SKILL.md` line 10).
- G16. The page carries a line starting "Not on this page yet", naming the weekly measures and the coach and class measures, so no reader takes the page for the whole of release 1: no word of his asks for it; his answer 6 ("skip for now, ill send it later") left those measures out.

## Piston's picks, in his place, each his to strike

- 02:05: the P&L alone if a third FAIL came. His words are in `C:\AI_Building\AI_PRU\LOG.md`.
- ~02:15: G1 to G7 stand. G1 has since been replaced by the new shape, G5 moved to release 1b, and G7 withdrawn. He does NOT accept the page in Sergio's place; he asks Sergio when Sergio is back.
- Between 02:28 and 02:42: "my pick in his place, his to strike: yes to agent 6, a blind check of the repaired GOAL/PLAN/test only, then LAWYER." The message is in Angie's session transcript 034bc097-973b-403b-8a90-c7678efdb939, between her 02:28 and 02:42 clock readings.
- ~02:44: the smaller shape, on disk with his words, session, time and his flag to Sergio: `C:\AI_Building\AI_HQ\03 Library\PISTON PICK - PRU job 01 third blind-check FAIL - 2026-11-20 HOME.md` (cited by path alone: the file is still being added to). Its "No 7th agent" was corrected there at 02:59.
- 03:04 and 03:09-03:12: his 03:04 pick (the LAWYER desk repairs) crossed my repair; at 03:12, "FINAL, his to strike, and LAWYER agrees", the round-6 repair stands and check 6 runs. Record: 04_AI_HQ cdf0ea9.
- After check 6's FAIL: "my pick in his place, his to strike: yes to your plan. Repair all 7 ... Then one last blind check (agent 8). LAWYER round 2 only on its PASS. If agent 8 FAILs, the job stops (R-1876)." In Angie's session transcript 034bc097-973b-403b-8a90-c7678efdb939.
- 03:00, after LAWYER's plan FAIL: "Repair all 12, then run one blind check (agent 7) of the repaired GOAL, PLAN and test against the frozen page. Only on its PASS does it go back to LAWYER." Also: "The 9am go-live question goes to Sergio himself, with your pick first and the cons." Both are in the same transcript.

## His 9am question

Asked of Sergio himself; Piston relays it if he is back first. Only he accepts.

Question 8: "Put the PRU 2027 budget page (the P&L, 2025-2027) live on ONE VIEW now?"
1. **Yes, put it live as is (Recommended).** Every figure is proved against the source files by Angie's test and her blind checks, and LAWYER checks it. Con: how it draws (* marks, tooltips, labels, the year list) is not proved yet; a drawing fault could show until release 1b.
2. **Not yet, wait for release 1b.** Con: nothing new on ONE VIEW at 9am, against his "MANDATORY".
3. **Show it to me first.** He opens the page file. Con: it goes live only after he looks.

## Steps, agents and models

Agents launched: 7 Opus blind checkers (checks 1 to 6; check 2 ran as two). Piston's word after check 6 allows an 8th: check 7. LAWYER is a desk of its own. The Brain puts the page live.

| # | step | who | done when | minutes | state |
|---|---|---|---|---|---|
| 1 | Checks 1 to 3 (check 1 of the plan alone), repairs | Angie; checker agents (Opus) | - | - | done; FAIL 1 to 3; new shape (Piston) |
| 2 | The P&L-only page, `C:\AI_Building\AI_MISC\06 Benches\2026-11-20 PRU job 01 page - ANGIE-HOME\build_page.py --pl-only`, and its test `C:\AI_Building\AI_MISC\06 Benches\2026-11-20 PRU job 01 page - ANGIE-HOME\test_page_pl.py` | Angie | page frozen at 3fbc0758 | - | done |
| 3 | Check 4, then check 5 (agent 6), each repaired | checker agents (Opus); Angie | - | - | done; FAIL 4 and 5; smaller shape (Piston) |
| 4 | LAWYER round 1 on GOAL and PLAN (verdict `C:\AI_Building\AI_LAWYER\Office desk\Verdicts\2026-11-20 Angie PRU job 01 release 1 plan check - ccc6409e.md`) | LAWYER | - | - | FAIL 12; the page check still runs |
| 5 | Repair of LAWYER's 12 findings: GOAL and PLAN rewritten; the test's cases merged to 10 (the cap); the page unchanged | Angie | own test: 10/10 PASS, 57 of 57 caught | 25 | done (own test, not a verdict) |
| 6 | Check 6, of the repaired GOAL, PLAN and test against the frozen page | checker agent 7 (Opus) | - | - | done; FAIL 6 (A 5, C 2) |
| 6b | Repair of check 6's 7 findings by change list `C:\AI_Building\AI_MISC\06 Benches\2026-11-20 PRU job 01 repair 7 - ANGIE-HOME\change_list_round7.py`; two test checks added (headers as drawn, rows drawn); the page unchanged | Angie | own test: 10/10 PASS, 60 of 60 caught | 15 | done (own test, not a verdict) |
| 6c | Check 7, the last: GOAL, PLAN and test against the frozen page; a FAIL stops the job | checker agent 8 (Opus) | PASS | 25 | next |
| 7 | GOAL, PLAN and test back to LAWYER, round 2 (session local_5fb2d9ed-2bc2-4e00-8229-4baba6e00ef6) | Angie sends | LAWYER's PASS on plan and page | - | |
| 8 | Path, md5 and verdict to Piston by 07:30; page copied into the job folder; his 9am question; the Brain puts it live on his yes | Angie / Piston / Sergio / the Brain | R1-5's pass mark | - | |
| 9 | Release 1b (the drawing, then the Weekly tab), then release 2 | Angie, then the same checks | - | - | after 9am |

Each check lists every fail it finds. There are two FAILs per repair step (R-1876, R-1880); a seventh FAIL of Angie's checker stops the job.
