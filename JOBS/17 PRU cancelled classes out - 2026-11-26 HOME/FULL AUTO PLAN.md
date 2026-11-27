# Job 17, full-auto plan for the rest (written 2026-11-27 01:14 EST, clock read by `date`)

His words, Angie's chat: "do it full auto"; then "also give Rick the new plan", "with the new salesa and GP numbers".
Goal file: `C:\AI_Building\AI_PRU\JOBS\17 PRU cancelled classes out - 2026-11-26 HOME\GOAL.md`.
Bench: `C:\AI_Building\AI_MISC\06 Benches\2026-11-26 PRU cancelled classes out - ANGIE-HOME-J17\` (below: BENCH).
Rules asked: `rulebook.py get --who Angie --job "full-auto run" --moment All`, 710 lines, 2026-11-27 01:13:58 EST.

## Agents: 1 planned, at most 3

- One blind checker, launched by Angie, on Opus 5.5: step 6. If it fails the build, one repair and one fresh checker (2 more, on Opus 5.5). A second failed check stops the piece and hands it to Piston for grill-me (R-1917).
- LAWYER's check is LAWYER's own session and its own agents (step 7). Angie launches none of them.
- Steps 1 to 5, 8 and 9: Angie herself. They are small edits on her own bench and a message, and a builder agent would have to read everything again.

## Steps, each with its proof on disk

1. (10 min) Check the 2 cancelled classes are in the live planner's 2026 figures. Recount Woodbridge First Ride April and Newport News 2-Wheel January from `BENCH\manual log\2026 PRU Manual Log v3.xlsx` the way job 07's `extract_master26.py` counts, and compare with `C:\AI_Building\AI_PRU\JOBS\14 PRU his plan as default - 2026-11-24 HOME\job14 410b33df.html`. Proof: `BENCH\planner\step1.txt`.
2. (15 min) Build `BENCH\planner\j17_planner.py`. It copies 410b33df and takes the 2 classes and their 2 students out of every 2026 figure the page draws from the Manual Log (classes, students, fill). It keeps their fees (his 55). It sets Woodbridge First Ride April 2027 to 0 in the default plan (his "take the class out the 2027 goal for April"). Proof: the new page in `BENCH\planner\` and its md5.
3. (15 min) Own tests in `BENCH\planner\j17_planner_tests.py`:
   - Only the intended figures moved (a diff of the page data).
   - The page runs with no console error and SELFTEST passes, in the browser pane through a local server.
   - The downloaded sheets, with nothing saved: Woodbridge April shows 12 classes.
   - Plants: one class left in, FAIL; April not 0, FAIL.
   Proof: `BENCH\planner\tests.txt`.
4. (10 min) Rerun the goal check, `BENCH\pru_goal_classes.py`, on the new page's downloaded plan. Expected: no stop. Proof: `BENCH\planner\goal_check.txt`.
5. (10 min) Read the new 2027 sales and gross profit, by month and for the year, from the new page's P&L. Put them beside the live page's. Proof: `BENCH\planner\sales_gp.csv` and the downloaded plan workbook.
6. (30 min) One blind checker (Opus 5.5) checks the dashboard build (`BENCH\dashboard\page_after.html`, 0fcfb06e) and the new planner page against GOAL.md. It writes its findings before it reads my claims (R-1875). Proof: `BENCH\CHECKER r2\FINDINGS.md`.
7. (wait) On PASS: ask LAWYER for its check of both pages and the goal check (R-1877). On FAIL: repair (Phase 4 item 2), then step 6 again. Proof: LAWYER's verdict file.
8. (5 min) On LAWYER PASS, per gate question 60: send Rick, in one session message, the new plan workbook's path and the new 2027 sales and gross profit, beside the old.
9. (10 min) Write OWN TESTS r2.md, update TO DO.md and the checkpoint, and commit by named paths after the names scan. The push program pushes (R-1930).

## What this run never does

- It never puts a page live: that waits for his yes, then a numbered Brain session (his 59).
- It never accepts anything.
- It never edits Rick's files, or anything outside AI_PRU and the bench.
- It never prints a class code (M-2880).

## Ceilings: from gate question 61. Spend is written to `BENCH\planner\LEDGER.md` as each call returns (M-0045, M-1526).

## Decisions made in his place: written to `BENCH\planner\DECISIONS.md` before the work each one shapes (M-2849).
