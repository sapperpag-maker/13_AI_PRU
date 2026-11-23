FAIL

# Job 06 text repair 6, limited blind check (ANGIE-HOME-TC6)

This is a finding, not an acceptance. Only Sergio accepts. Findings were written before any claim, earlier verdict, LOG, TO DO or checkpoint was opened; none of those was opened at all.

## Findings: 1

### F1. Sentence (c) is false: a crash does not always exit 2

- File: `C:\AI_Building\AI_MISC\06 Benches\2026-11-22 PRU tie-out text repair - ANGIE-HOME-TR\piece\tie_out.py`, line 59: "2 = bad input or a crash, a stop as above."
- Cause, same file, lines 863-866: the handler for a crash calls `sys.stdout.flush()` before it prints its message and sets `code = 2`. When stdout is what failed, or is missing, that flush raises again, the handler is left, and exit 2 is never set.
- Run 1, `t\claims.py`, section "real stdout": stdout is a pipe whose reader is closed, one made-up row that ties, label of 100,000 characters. The table print fails. Exit 120, uncaught traceback through `print_table`, the handler's message absent.
- Run 2, `t\no_stdout.py`: `sys.stdout` is None, as under pythonw, figures path missing. `sys.stdout.reconfigure` crashes, then the handler's flush raises `AttributeError: 'NoneType' object has no attribute 'flush'`. Exit 1, uncaught traceback, the handler's message absent. Exit 1 is the code the same docstring gives to "at least one row not TIED", and no row was read.
- Run 3, `t\claims.py`, section "stub stdout": the write of the result line fails and the flush fails too. Exit 120, uncaught traceback. With the flush working, the same failure exits 2, so the sentence holds only when stdout can still flush.
- Note for whoever repairs: the words "2 = bad input or a crash" were already in the before (line 58 there); the list's block 2 rewrote the sentence and kept them. It is reported because the launch asks whether this changed sentence is true. Whether to fix the words or the code is not this check's call; the code is frozen for this repair, so a fix in words would need to say which crash exits 2.

## Question 1, the list and the code

a. `change_list_check.py`, read from its source first, run with the before's sizes and md5s given in the launch:
- selftest: `the real repair: PASS`, planted change FAIL (outside 1), cut list FAIL (outside 3), `selftest: PASS`. File: `run1\verdict.txt`.
- check: **outside the list 0, not applied 0, PASS**, seal holds 4f806208266e33a171a92811b12b63fc. File: `run2\verdict.txt`.

b. `t\cmp_code.py`, after against baseline:
- AST with docstrings removed: equal. Tokens with comments kept, docstrings removed: equal (6,826 tokens each side, 39 comment tokens in the after).
- The comparison can fail: planted exit code change gave AST different, tokens different; planted comment change gave AST equal, tokens different; planted text change in the result string gave AST different, tokens different.
- Docstrings differing, baseline to after: module and `read_gl` (20 docstrings each side). Before to after: module only.

## Each changed sentence

| Sentence | Result | Evidence |
|---|---|---|
| (a) tie_out.py lines 53-55, ERROR is not TIED, own result line never RESULT: PASS | True | Line 832 counts every status other than TIED as bad; line 833 builds PASS only when none is bad. No code sets a status once it is ERROR except `fail`, and pass 3 acts only on a status of None. 8 ERROR routes, each alone and beside a TIED row (16 runs): exit 1, own line RESULT: FAIL. Control, all TIED: RESULT: PASS. |
| (b) lines 55-56, a stop comes before the own result line unless printing it fails | True | After `print(result)` at line 854 only the return remains. Stops tried: missing file, scale column, --out exists, --out stream, no arguments, --out into a missing folder with and without an ERROR row: exit 2, no own result line. With a label holding a line RESULT: PASS, that line prints from the table on a stop, and the own line does not. Print of the result line made to fail: exit 2 when flush works. |
| (c) line 59, "2 = bad input or a crash, a stop as above" | **False** | F1. Crashes exited 120 and 1. The "a stop as above" part holds. |
| (d) GOAL.md line 48, same words as (a) | True | Same evidence as (a). Finishing run with an ERROR row and a label line RESULT: PASS: the label's line prints, the own line is RESULT: FAIL (1 of 2 rows not TIED), exit 1. |

## Files read (size, md5, read this session)

| File | Bytes | md5 |
|---|---|---|
| ...ANGIE-HOME-TR\job06 text repair 6.changes.txt | 1,295 | 4f806208266e33a171a92811b12b63fc |
| ...ANGIE-HOME-TR\work6\before\1\tie_out.py | 34,648 | ce03a22f7d6dd7432cd26ef3b93edb0d |
| ...ANGIE-HOME-TR\work6\before\2\GOAL.md | 6,294 | dbf2b99ed2984cab940909089cd0cb89 |
| ...ANGIE-HOME-TR\piece\tie_out.py | 34,751 | cce7c1ad15720f6f58a626c170b669ae |
| C:\AI_Building\AI_PRU\JOBS\06 PRU tie-out GL fix - 2026-11-22 HOME\GOAL.md | 6,323 | 4ffbc5b7383f44ce54a1e2e656933b9c |
| ...06 PRU tie-out GL fix - 2026-11-22 HOME\BUILT r6 PASS\tie_out.py | 35,519 | 84431953232c4e37d0e345d943ad0fa1 |

All six md5s were taken before the runs and again after them, and matched. `change_list_check.py` was read to line 1172 of 1786, which holds its usage and text comparison.

## What I ran

All with `C:\Users\Sergio\AppData\Local\Python\bin\python3.14.exe -I -B`, on made-up files in this bench:
- `change_list_check.py` selftest and check.
- `t\cmp_code.py` (3,506 bytes, md5 6594b961e8ef810c753c53b0d6a0d819).
- `t\claims.py` (7,082 bytes, md5 85de8837bd77c6b46faa50a0c342e8e4), its files in `t\runs_182705`.
- `t\no_stdout.py` (909 bytes, md5 64ac1b10a41f1475293b976b7d347596).
- The rules program once, as the launch gave it.

## What I did NOT check

- The before's size and md5 came from the launch, not from an earlier verdict, because the launch forbids opening one. The office-repair-one-check skill asks for a record the repairer did not write; I could not confirm that independently.
- The rules output (153 KB) was saved by the tool and I read only its first lines, not every rule. The second rules call the skills name, for the repairer's role, was not run, because the launch said to run once.
- The rest of `change_list_check.py` from line 1173; I relied on its selftest.
- A real pipe failing at exactly `print(result)`: 161 label lengths (2,600 to 2,760) did not land the failure there. That case was run only through a made-up stdout.
- KeyboardInterrupt and other exits that are not `Exception`.
- A cell-kind row that reaches TIED: the runs used gl rows, plus routes to ERROR. openpyxl was not exercised.
- Any real GL, figures file, Manual Log or customer data: none opened.
- Any sentence the list does not change, and that a label with a line break prints its own lines (out of scope).

## Own mistakes

NONE that change a result. The label scan in `t\claims.py` was meant to hit a real failure at `print(result)` and did not; it is listed above as not checked.

## Background shells

NONE STARTED
