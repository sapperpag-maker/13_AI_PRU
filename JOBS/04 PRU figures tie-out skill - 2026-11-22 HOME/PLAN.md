# Job 04: finish the pru-figures-tie-out skill (full auto)

Angie, 2026-11-22. Sergio: "ok do full auto". Goal: the skill `C:\AI_Building\AI_PRU\.claude\skills\pru-figures-tie-out\` landed with a program that passed its blind check and LAWYER, run by hand twice, PDF without DRAFT, committed, and `pru-planner-check`'s checker pointed at it. Sergio alone accepts.

Rules asked: `rulebook.py get --who ANGIE --job "full-auto run" --moment "before building"` (1,278 lines, 2026-11-22 00:31). Plan tested against its full-auto entries (R-0028-31, R-0488, R-0514, R-0515, R-1126/27, R-1159/60, R-1170, M-1531, the gap test): 2 passes. Pass 1 found 3 defects (a money figure with no ledger, the pru-planner-check PDF yes would need a mid-run question, irreversible acts not each on their own item), fixed below; pass 2 found none.

## Steps (minutes; who; model; done when)

| # | Step | Min | Who | Model | Done when |
|---|---|---|---|---|---|
| 1 | Read the r4 blind verdict | 5 | Angie (reading her own checker's file) | - | VERDICT.md md5 and first line in LOG.md |
| 2a | PASS: send Piston the PASS line and md5s for LAWYER | 5 | Angie -> Piston | - | message sent; LAWYER verdict path back |
| 2b | FAIL: shape 2 (cell and gl kinds only; sum and ratio refused) per Piston's pick 2731af36 | 15 | builder agent | Opus | tie_out.py md5, TESTS line |
| 2c | Blind check of shape 2 | 15 | checker agent (fresh) | Opus | VERDICT first line |
| 2d | Second FAIL on shape 2: stop, park the program as NOT DONE (path: program, new shape, smaller, stop) | 5 | Angie | - | LOG line, parked in the end report |
| 3 | LAWYER FAIL: repair per the WHO REPAIRS table in `C:\AI_Building\AI_HQ\CLAUDE.md`, re-check | 15/round | builder agent + LAWYER via Piston | Opus | LAWYER PASS |
| 4 | Run the skill by hand on the real case: the planner, release 4 (page 0ca37404), figures listed, sourced, tied | 15 | runner agent | Opus | TIEOUT.md first line, on a bench |
| 5 | Run it by hand on a made-up report with a planted wrong figure, on a trash bench | 10 | runner agent | Opus | TIEOUT.md says FAIL on the planted figure |
| 6 | Each fault from 4-5: fix the SKILL.md line (skill-write-body), redraw the PDF if a step changes | 10 | Angie (skill editing is her desk's) | - | line count <= 50 |
| 7 | DRAFT off, PDF rebuilt (`build.py --only pru-figures-tie-out`) | 5 | Angie | - | WROTE lines, RESULT: BUILT |
| 8 | pru-planner-check: its step 3 checker launch runs pru-figures-tie-out before the LAWYER request; build.py entry and PDF updated | 15 | Angie | - | SKILL.md <= 50 lines, PDF built |
| 9 | Blind check of the two skill texts (rule text only, no data) | 10 | checker agent | Sonnet | VERDICT first line PASS |
| 10 | Names scan, commit AI_PRU by named paths | 5 | Angie | - | commit id |
| 11 | Push and Brain commit requests (build.py, 2 PDFs, README, wiki row) | 5 | Angie -> Piston -> a Brain session | - | commit ids read back |
| 12 | Benches to the trash, checkpoint, end report | 15 | Angie | - | checkpoint path |

Agents: at most 7 new (2 runners, 1 skill-text checker, and on the FAIL path 2 builders + 2 checkers), plus the r4 checker already running. All Opus except step 9 (Sonnet: reads rule text only). LAWYER is Piston's to launch, not counted here.

Critical path with no FAIL: about 2 h. With the FAIL path and one LAWYER repair: about 3.5 h. Ceiling: Sergio's gate answer.

## Never in this run
No question to Sergio after the start word. No email. No customer row or GL line printed. Nothing deleted: benches go to the trash. Pushes are Piston's. Nothing accepted: Sergio accepts.
