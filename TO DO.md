# TO DO - Angie

His jobs, waiting their turn. Nothing here starts until he says so.

| # | job | waits on |
|---|---|---|
| 1 | **PRU's 2027 budget dashboard** (his words, 2026-11-19: "the first task is to build the 2027 budget dashboard for PRU"; answer 55, "Angie builds, Rick advises (Recommended)"). Job folder `C:\AI_Building\AI_PRU\JOBS\01 PRU 2027 budget dashboard - 2026-11-19 HOME\`; its goal file `GOAL.md` is a DRAFT | his yes to `GOAL.md` (still DRAFT, its line 3, read 2026-11-19). The desk's opening is COMPLETED 2026-11-19: `git ls-remote origin main` on `sapperpag-maker/13_AI_PRU` returns c589acc41eac, the desk's opening commit |
- Planner page title says "PRU 2027 Sales Planner", ONE VIEW button says "PRU 2027 Planner"; make them match at the next rebuild if Sergio wants (Brain HOME, 2026-11-20).
- Write a program that rebuilds PRU's 2026 sales from the GL by Rick's 11 steps (`JOBS/01 PRU 2027 budget dashboard - 2026-11-19 HOME/PRU 2026 SALES - source, categories, rebuild steps (from Rick).md`), so Angie makes the figure herself each month (Sergio, 2026-11-20: "from now on you have to be able to do it all").
- Once the planner passes LAWYER: send Piston, for Rick, the file holding the 2027 figures by month, its md5, and each figure's source. Sergio told Rick, in Rick's chat, relayed by Piston 2026-11-20: "You take Angie's numbers from the Planner and you integrate those number with revenue streams that are not included in the log."
- pru-budget-update: add the step that runs Rick's pru_nonlog_streams.py (Sergio Q44 "One step, run by path") only after LAWYER passes it (Piston, 2026-11-20: blind r4 passed, queued at LAWYER). Risks to build into the step (Piston relaying Rick's checker): --out on its own path, never onto an input; an accept record saved with a BOM gives STOP; on the real GL it STOPs until Sergio rules on the accept-record fingerprints. Also split the skill (56 lines, limit 50).
- LAWYER's three wording risks on the planner notes (verdict md5 fd1413c3), Sergio Q45 "Accept it as it is": plan note's "above or beside" misses site rows above their unit rows; vs note does not cover the Change row; P&L note says "adding" where 5 profit lines subtract. Fix at the next update.
- HOLD (Piston relaying Rick, 2026-11-21): the step that runs pru_nonlog_streams.py waits on Sergio's pick in Rick's chat: (a) Angie's sales_2027 as accepted, Rick's program not used for PRU (Rick's pick); (b) class_fees_2027 + Rick's program. Under (a) the step and Q44's step are not needed.
