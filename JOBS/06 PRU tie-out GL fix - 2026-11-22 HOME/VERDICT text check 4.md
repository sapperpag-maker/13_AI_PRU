FAIL

# Job 06 text repair 4: blind check, ANGIE-HOME-TC4, 2026-11-22 HOME

A finding, not an acceptance. Only Sergio accepts. Three sentences are false. The code is unchanged and its tests and real run pass.

## Findings

**F1. `tie_out.py` module docstring, line 54: "A row with status ERROR is not TIED, and the run ends RESULT: FAIL."**
The second half is false when the run crashes after the rows are worked.
Made-up run: one row with shown `abc`, `--out` into a folder that does not exist. The table prints that row as ERROR, then the run ends exit 2 with no RESULT line; stderr: `bad input: tie_out stopped on an unexpected FileNotFoundError; no result`.
Cause: `main`, line 835, opens `--out` after the rows are worked and before RESULT is printed.
Evidence: `attack output.txt`, line "CRASH after rows: ERROR row, --out in a missing folder".
The next sentence ("A stop prints no RESULT line") describes this run correctly, so the two sentences together claim both outcomes for it.

**F2. `GOAL.md`, section "Two refusals kept", line 48: "A row with status ERROR is not TIED, and the run ends RESULT: FAIL."**
Same sentence, same counterexample as F1. This section has no sentence about a stop after the rows.

**F3. `GOAL.md`, section "Two refusals kept", line 47: "a figures row with a blank id and a no-break space in another column stops the run with exit 2 and no RESULT line; job 05 skipped that row and tied the others."**
The job 05 half is false for a row that also holds text. Job 05 skips the row only when the no-break space is all it holds.
Made-up runs, each with one good row beside it:
- blank id, no-break space in `label`, text in `unit`: job 05 exit 2, no RESULT, `a figures row has no id`.
- blank id, `label` = text plus a no-break space: job 05 exit 2, no RESULT, same message.
This build does the same on both, so for these rows there is no difference from job 05, and the line names one.
Where the no-break space is the row's only content, the sentence is true: 8 of 8 columns tried, this build exit 2, job 05 exit 0 with the good row TIED.
Evidence: `attack output.txt`, section "GOAL finding 2".

## Answers to the four questions

**1. The after is the before with exactly the list's blocks: yes.**
- `change_list_check.py selftest`: real repair PASS; planted change FAIL (outside the list 1); cut list FAIL (outside the list 34, seal passed over: yes); `selftest: PASS`.
- `check`: 3 blocks, outside the list 0, not applied 0, PASS. Filed in `verdict.txt`.
- Own program `code_equal.py`: with docstrings removed, the after and the code baseline are byte-equal (both md5 f3a8643f6cec2c52030a15ea84892d05), their syntax trees are equal, and all 39 comments are equal.
- Of 20 docstrings, exactly 2 differ from the baseline: `<module>` and `read_gl`.
- That program failed as it must on a planted code change and on a planted comment change.

**2. Module docstring from "Every field of figures.csv", and `read_gl`: one false sentence (F1).** At least one attempt per sentence, in `attack output.txt`:

| Sentence | Attempt | Result |
|---|---|---|
| Every figures and 9-field GL field trimmed | spaces and tabs on GL fields, quoted GL fields, figures fields, figures header | true, all TIED |
| The files it reads are never changed | md5 and size of figures and GL before and after a run with `--out` | true |
| A refusal is a row with ERROR or a stop with exit 2 | ERROR rows; 5 kinds of stop | true |
| A row with ERROR is not TIED | every ERROR run | true |
| ...and the run ends RESULT: FAIL | ERROR row plus crash at `--out` | **FALSE, F1** |
| A stop prints no RESULT line | 4 stops before the rows, 2 crashes after them | true |
| Exit 0 = every row TIED, RESULT: PASS | tied runs | true |
| Exit 1 = at least one row not TIED, RESULT: FAIL | ERROR, OFF, NO SOURCE, mixed | true |
| Exit 2 = bad input or a crash, no RESULT line | the same stops and crashes | true |
| read_gl: one streaming pass for every gl row on the path | read of the code; two rows on one path | true |
| read_gl: each field of a 9-field record trimmed | as the first row | true |
| read_gl: RowError or csv.Error, then every row on the path ERROR | bad header, short record, quote closed early, two rows each | true, 2 of 2 ERROR each |
| read_gl: unreadable date, debit or credit makes that row ERROR | bad date, blank date, bad debit, bad credit; with a journal filter that excludes the line; on another store | true; another row on the path stays TIED; another store's line changes nothing |

**3. GOAL "Two refusals kept": two false sentences (F2, F3).**
- Line 46 (no-break space at the end of a gl detail value): this build ERROR, job 05 TIED, for all 6 keys (accounts, store, from, to, side, journal). True. See Minor 1.
- Line 49 ("no change of logic"): true, by question 1.

**4. Tests and real run: yes.**
- `TESTS: PASS (1271)`, exit 0, 0 `__pycache__` folders.
- On `gl_check.csv`, `--out` to a new file: `RESULT: PASS`, exit 0, 9 rows TIED, 0 ERROR, OFF or NO SOURCE. Counted in `real\result.csv`.

## Minors (change no status)

1. GOAL line 46, "job 05 tied it", assumes a row whose shown figure is right. With a wrong shown value, job 05 gives OFF (`attack2 output.txt`). This build still differs from it (ERROR), so the named difference holds.

## Risks (change no status)

1. **The before's record.** The one-check skill wants the before's md5 from a record the repairer did not write. The md5s I had came from the launch, and the verdicts that could hold them were closed to me as blind. Partial anchor: the code baseline equals its committed git blob (e3d25c36), and the before's code equals the baseline. The before's docstrings and the before `GOAL.md` have no independent record: git HEAD's `GOAL.md` is an older version (5,321 bytes, md5 5b89ef53).
2. **Exit code outside 0, 1, 2.** With stdout closed, a tied run ended exit 120 (`attack output.txt`). The docstring does not say these are the only codes, so this is not a false sentence.

## Files read, md5 before and after (unchanged)

| File | Bytes | md5 |
|---|---|---|
| `C:\AI_Building\AI_MISC\06 Benches\2026-11-22 PRU tie-out text repair - ANGIE-HOME-TR\piece\tie_out.py` | 34,630 | f736508a4d3d14d74d810380e66f65f7 |
| `C:\AI_Building\AI_MISC\06 Benches\2026-11-22 PRU tie-out text repair - ANGIE-HOME-TR\piece\test_tie_out.py` | 107,836 | 1ab8b575900ed2a88513cacbb77385f6 |
| `C:\AI_Building\AI_PRU\JOBS\06 PRU tie-out GL fix - 2026-11-22 HOME\GOAL.md` | 6,163 | 3677b82389a900ddc365bd4c3dace816 |
| `C:\AI_Building\AI_PRU\JOBS\06 PRU tie-out GL fix - 2026-11-22 HOME\BUILT r6 PASS\tie_out.py` | 35,519 | 84431953232c4e37d0e345d943ad0fa1 |
| `C:\AI_Building\AI_PRU\JOBS\05 PRU tie-out rebuild - 2026-11-22 HOME\BUILT r5 PASS\tie_out.py` | 29,547 | a8f90d601cfd855442b16d39765a9cea |
| `C:\AI_Building\AI_MISC\06 Benches\2026-11-22 PRU tie-out text repair - ANGIE-HOME-TR\work4\before\1\tie_out.py` | 37,086 | e14f2ecba45274799e3e2f1a2f31d4ad |
| `C:\AI_Building\AI_MISC\06 Benches\2026-11-22 PRU tie-out text repair - ANGIE-HOME-TR\work4\before\2\GOAL.md` | 6,532 | 4f284b6eb7528c92554c0c1f31e65b0a |
| `C:\AI_Building\AI_MISC\06 Benches\2026-11-22 PRU tie-out text repair - ANGIE-HOME-TR\job06 text repair 4.changes.txt` | 6,002 | d2ae1fb3abb996fb5131e99b01e15879 |
| `C:\AI_Building\AI_MISC\06 Benches\2026-11-22 PRU tie-out hand run real - ANGIE-HOME-HR1\gl_check.csv` (run by the program; not opened by me) | 3,168 | f3941c4a5f90478d30008245ce741ac7 |

## What I ran

- Rules program, once: `get --who ANGIE --act review --what budget`. **I read the first 14,000 of its 156,760 characters, not the rest.**
- `change_list_check.py` selftest and check.
- `code_equal.py`, `attack.py`, `attack2.py`, all on made-up files.
- `test_tie_out.py`, and the after on `gl_check.csv`.
- Python 3.14 with `-I -B` throughout. Outputs are saved on this bench.

## What I did not check

- The rest of the rules output (above).
- The two extra rules calls the one-check skill's table names; the launch said to run the program once.
- The sentences of the module docstring before "Every field of figures.csv", and every docstring other than the module's and `read_gl`'s. They are byte-identical to the baseline only for the docstrings that did not change.
- GOAL sections other than "Two refusals kept".
- Whether the tests themselves are sufficient: I ran them and read only their result.
- Cell rows in my own attacks. They ran only through the test suite.
- The history claims in GOAL line 44 and 49 (verdict c7f96db6, Sergio's 76, Piston's pick): those files were closed to me as blind.
- Mistyped codes, outside this check by the launch.

## Blind

Before this file was written I opened no VERDICT file other than my own, no "text check" bench other than mine, nothing in `C:\AI_Building\AI_LAWYER` or `C:\AI_Building\AI_HQ\03 Library`, no checkpoint, no `LOG.md`, no earlier change list, no claims or shapes file, no "apply output.txt". No customer data, Manual Log, GL line or secret was opened or printed.

## My own mistakes

1. My first selftest and check passed `--after` twice, so the program refused them ("no --after is the full path the list names"). I reran both with both paths after one `--after`, in the new folders `run1b` and `run2b`. Folders `run1` and `run2` hold that refused first try.
2. I left a copy of git HEAD's `GOAL.md` on this bench as `head_GOAL.md`. It was used only for Risk 1.

## Background shells

NONE STARTED
