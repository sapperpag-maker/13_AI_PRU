PASS

# Blind limited check 7: one-line text repair of tie_out.py (job 06)

Checker: job agent for Angie, tag ANGIE-HOME-TC7, machine HOME, 2026-11-22. I did not make this repair.
This is a finding, not an acceptance. Only Sergio accepts.

## Findings

Number of findings: 0.

## Risks, numbered, not findings (they do not decide the verdict)

R1. "A crash" cannot cover a process killed from outside or a hard crash of Python itself: no except line runs then.
Tried: 3 made-up broken workbooks (q2_native.py), 300,000 levels of nesting in two of them. None caused a hard crash. Each gave a row ERROR and exit 1, the documented code for a row not TIED, because the run was not stopped.
What would settle it: a made-up file that kills the interpreter. I found none.

R2. Ctrl+C is not caught by "except Exception" (tie_out.py line 863). A planted KeyboardInterrupt exited 3221225786 (0xC000013A). I read a user's interrupt as neither bad input nor a crash, so it is not a finding. If Sergio reads it as a crash, the sentence would be false for that one case.

## Question 1: the list and the code

a. change_list_check.py, run from its own path, writing only to this bench:
- selftest: "the real repair: PASS (outside the list 0, not applied 0)"; (a) planted change FAIL, outside 1; (b) cut list FAIL, outside 4; "selftest: PASS - both runs failed as they must". Exit 0. Work folder: run_selftest.
- check: seal holds a56312fdea891efae7d9be1d712eb50d; blocks 1; **outside the list: 0; not applied: 0**; PASS. Exit 0. Work folder: run_check, verdict.txt first line PASS.

b. code_eq.py, after against the code baseline (BUILT r6 PASS):
- AST equal with docstrings blanked: True.
- Tokens equal, comments kept, docstrings blanked: True. 6,866 tokens each side. 20 docstrings each side.
- Docstrings that differ from the baseline: 2, the module docstring and read_gl.
- The comparison can fail. 5 planted changes, 5 caught: exit code 2 to 3 (AST and tokens); except Exception to except ValueError (AST and tokens); GL_WIDTH 9 to 8 (AST and tokens); a comment only (tokens); a non-docstring string (AST and tokens).

## Question 2: the sentence

tie_out.py line 59, module docstring: "2 = bad input or a crash, while the screen output still works."
Read as: while stdout and stderr work, a run stopped by bad input or by a crash exits with code 2.

**TRUE** on everything tried.

Code read: every BadInput and argument stop in main returns 2 (lines 804-805, 809-810, 814-815, 819-820, 825-826, 839-840). Any other Exception reaches lines 863-866, which set code 2. Line 867 exits with that code.

Runs on made-up files, screen output working:
- q2_runs.py: 25 kinds of bad input, all exit 2, no traceback. They cover arguments, missing or wrong figures file, encodings, binary junk, header faults, row faults, and --out existing, a folder, a stream or holding a colon.
- q2_runs.py: 8 crashes, all exit 2, no traceback. They cover --out into a missing folder (with a tied row and with an OFF row), bad characters ? * |, a reserved name under a missing folder, a path too long, and a path under a file.
- Total 33 of 33 exit 2. Controls: all tied exit 0, row OFF exit 1.
- q2_inject.py: 7 exception kinds planted at 4 points of a bench copy, 28 runs, 28 exit 2, no traceback.

Pipe whose reader is closed (outside the sentence's condition; not findings):

| Pipe closed | All tied | Row OFF | Bad input, file missing | Crash, --out missing folder |
|---|---|---|---|---|
| stdout | 120 | 120 | 2 | 120 |
| stderr | 0 | 1 | 120 | 120 |

## Files read

| File | Bytes | md5 |
|---|---|---|
| C:\AI_Building\AI_MISC\06 Benches\2026-11-22 PRU tie-out text repair - ANGIE-HOME-TR\job06 text repair 7.changes.txt | 541 | a56312fdea891efae7d9be1d712eb50d |
| same folder, job06 text repair 7.changes.txt.seal | 33 | holds a56312fdea891efae7d9be1d712eb50d |
| same folder, work7\before\1\tie_out.py | 34,751 | cce7c1ad15720f6f58a626c170b669ae |
| same folder, piece\tie_out.py | 34,771 | 39f4630569e40f8315df3bc1c3f5801c |
| C:\AI_Building\AI_PRU\JOBS\06 PRU tie-out GL fix - 2026-11-22 HOME\BUILT r6 PASS\tie_out.py | 35,519 | 84431953232c4e37d0e345d943ad0fa1 |
| C:\AI_Building\AI_HQ\04 Tools\Tools\change_list_check.py | 79,121 | 4ec1baf3b86243c5ca36c6701d99817b |

All md5s were taken by me, and read again after the runs: unchanged.

## What I ran

Python: C:\Users\Sergio\AppData\Local\Python\bin\python3.14.exe -I -B, on: change_list_check.py selftest and check; code_eq.py (md5 89ded1cc06fd00877a754bd6ec2de137); q2_runs.py (6de171b57a5336ff8cff39fc0f88f4fe); q2_inject.py (f96361a7d4677b2a14382e19cc02a2e0); q2_native.py (7a453a10600349e72530ae16e90298d7). The tie_out runs used bench copies only, on made-up files in q2.

## What I did NOT check

- The before's md5 against a record the repairer did not write. The skill asks for the last check's verdict, but this launch forbids opening any earlier verdict, so the record is the launch brief. If the brief's before is wrong, the list check does not show it. The AST and token comparison to the baseline does not depend on that record.
- Any sentence the list does not change, and any other behaviour of the program.
- The two known separate jobs: a label with a line break, and the exit code when screen output is broken.
- A real GL, figures file, Manual Log or customer data: none opened.
- Linux or Mac. Runs were on Windows, HOME only.
- A hard crash of Python or a process killed from outside (see R1). A real Ctrl+C from a console: only a planted KeyboardInterrupt.
- Lines 1173-1786 of change_list_check.py were not read. I relied on its documented usage, its selftest and its output.

## My own mistakes

1. I cut the rules program's output to its first 60 lines, so I read only those rules. The launch said to run the call once, so I did not run it again.
2. The skill office-repair-one-check asks for a second rules call, for the repairer's role. The launch said to run one call, so I did not make it.
3. q2_native.py probes the openpyxl version with one sub-run of python -I -c, not the -I -B <script> form. It wrote no file.

## Background shells

NONE STARTED.
