FAIL

# Blind check 5 of job 06's text repair (3 sentences), ANGIE-HOME-TC5, 2026-11-22

A finding, never an acceptance: only Sergio accepts.
Question 1 passes. Question 2 fails on 3 sentences, all from one cause. No build was changed.

## Findings

All three come from one fact. `print_table` (after\tie_out.py line 781) prints a figures row's label as it is, so a label holding a line break prints its own lines.

- **F1. Docstring, lines 53-54: "a run holding one never prints RESULT: PASS" is false.** Made-up file `t\c11.csv`: row E has status ERROR and the label `x`, line break, `RESULT: PASS`, line break, `y`. The run prints a line that is exactly `RESULT: PASS`, then `RESULT: FAIL (1 of 2 rows not TIED)`, exit 1.
- **F2. Docstring, line 55: "A stop prints no RESULT line." is false.** Made-up file `t\x3.csv`, same label, `--out` into a missing folder. The run stops with exit 2, and the only RESULT line on stdout is exactly `RESULT: PASS`. Stderr says "no result".
- **F3. GOAL.md, line 48: "a run holding one never prints RESULT: PASS" is false.** Same run as F1, and F2's run holds an ERROR row too.

How far these reach: the program's own result line is right in every run I made. What is false is the sentence's "never" and "no", because the printed output can hold that text from a label. The fact that settles it: whether the sentence speaks of everything printed, as its words do, or only of the program's own result line. Read the second way, all three would be true, but that is not what they say.

## Question 1: the list and the code

- `change_list_check.py selftest`: the real repair PASS (outside 0, not applied 0); planted change FAIL (outside 1); cut list FAIL (outside 6, seal passed over: yes); `selftest: PASS`.
- `change_list_check.py check`: 3 blocks, outside the list 0, not applied 0, PASS. Saved in `selftest output.txt` and `check output.txt`.
- My own program `code_equal.py`, on the AST with docstrings removed and on the token stream with comments kept:
  - Code baseline against after: AST equal, tokens equal (5,585 each, 39 comments, 20 docstrings each). **Docstrings that differ: the module's and `read_gl`'s.**
  - Before against after: AST equal, tokens equal. Docstring that differs: the module's only.
  - The proof can fail: a planted code change and a planted comment change both came back not equal.

## Question 2: each sentence

| Sentence | Result | Evidence |
|---|---|---|
| (a) Docstring, ERROR row "is not TIED" | True | Code lines 684, 743: a set status is never overwritten; c2, c3 |
| (a) Docstring, "never prints RESULT: PASS" | **FALSE (F1)** | c11. Without such a label, true: c2, c3, x1 |
| (a) Docstring, "A stop prints no RESULT line." | **FALSE (F2)** | x3. Without such a label, true: x1, x2 |
| (b) GOAL, this build, blank id and no-break space: exit 2, no RESULT line | True | c5-c9, e1-e6: all exit 2, no RESULT line |
| (b) GOAL, job 05, no-break space the only content: skipped, others worked | True | c5, c6, e2, e3, e4, e6 (see minor 1 for e1) |
| (b) GOAL, job 05, row also holds text: exit 2 | True | c7, c8, c9, e5 |
| (c) GOAL, ERROR row "is not TIED" | True | As (a) |
| (c) GOAL, "never prints RESULT: PASS" | **FALSE (F3)** | c11, x3 |

Controls: c1 all tied exits 0 with RESULT: PASS; c4 OFF exits 1; c10 blank id with plain text exits 2 on both builds.

## Minors (change no status)

1. e1: when the no-break-space row is the file's only row, job 05 skips it and then stops with exit 2, "figures file has no rows". GOAL's "worked the others" has no others to work there.
2. c12: a label of `RESULT: PASS` on one line also prints inside its table row. It is not a line of its own.

## Risks (change no status)

1. Anything that searches this program's output for `RESULT: PASS` can be misled by such a label. On x3 that text is the only RESULT line. I did not look for any such reader, and no real figures file was opened.

## Files read, md5 before and after (unchanged)

| File | Size | md5 |
|---|---|---|
| Code baseline, job 06 `BUILT r6 PASS\tie_out.py` | 35,519 | 84431953232c4e37d0e345d943ad0fa1 |
| Before `work5\before\1\tie_out.py` | 34,630 | f736508a4d3d14d74d810380e66f65f7 |
| Before `work5\before\2\GOAL.md` | 6,163 | 3677b82389a900ddc365bd4c3dace816 |
| After `piece\tie_out.py` | 34,648 | ce03a22f7d6dd7432cd26ef3b93edb0d |
| After job 06 `GOAL.md` | 6,294 | dbf2b99ed2984cab940909089cd0cb89 |
| Job 05 `BUILT r5 PASS\tie_out.py` | 29,547 | a8f90d601cfd855442b16d39765a9cea |
| `job06 text repair 5.changes.txt` | 1,228 | 3ed61857bed5fbec2426b9de31b9dd08 |
| Its `.seal` (hashed, checked by the tool) | 33 | 0fa1991d9ee7b1b647e0f09a95e6f70e |
| `change_list_check.py` (searched and run, md5 taken once, after the runs) | 79,121 | 4ec1baf3b86243c5ca36c6701d99817b |

The first eight were hashed when copied or at the end of the run, and the values match the launch's where it names them.

## What I ran

`change_list_check.py` selftest and check; `code_equal.py`; `probe.py` (c1-c12, x1-x3, one --out run); `probe2.py` (e1-e6). All on made-up files in `t\`, with `python3.14 -I -B`, on copies of the programs.

## Rules program

Ran `rulebook.py get --who ANGIE --act review --what budget` once, as launched. Output 153.1 KB. I read its first 2 KB and the 40 lines a search for blind, change list, docstring or checker returned. I did not read the rest. I did not make the skill's second call (as the repairer's role), because the launch said to run it once.

## What I did not check

- Any sentence other than the 3 the list changes, and any behaviour of the program beyond them.
- Any real GL, real figures file, customer data or Manual Log: none opened.
- A failure while writing or closing the `--out` file after its RESULT line, or a broken stdout.
- The before's md5 comes from the launch, not from an earlier verdict, because those are closed to this blind check. So the skill's "record the repairer did not write" is met only as far as the launch is such a record.

## My own mistakes

1. My first two runs of the list check passed `--after` twice and used bench copies. The tool refused them (FAIL, "no --after is the full path the list names"). The correct runs are in `run5` and `run6`; `run1` to `run4` hold nothing relied on.

## Background shells

NONE STARTED
