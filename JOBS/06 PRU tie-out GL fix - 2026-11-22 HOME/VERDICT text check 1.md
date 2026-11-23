FAIL

# Blind check of the job 06 text repair (two docstrings of tie_out.py)

Checker: job agent launched by Angie (ANGIE-HOME), HOME, 2026-11-22. This is a finding, not an acceptance: only Sergio accepts. I did not build this piece.

## Answers

| Question | Answer |
|---|---|
| 1. After = before + exactly the list's blocks; code identical | YES |
| 2. Every claim in the two passages true of the code | NO: findings F1, F3, F4, F5 |
| 3. Last GOAL section describes the two kept refusals | NO: findings F1, F2 |
| 4. Tests and real run | YES: `TESTS: PASS (1271)`, 0 __pycache__; real run `RESULT: PASS`, 9 of 9 TIED |

## Findings (5)

**F1. A figures row holding only a no-break space does not always stop the run.**
- Where: `tie_out.py` header lines 63-64 ("A figures row that holds anything after the trim and has no id, a no-break space alone included, stops the whole run (exit 2)"); GOAL.md line 47, which says the same.
- Evidence: with the no-break space in the id column (`\u00a0,,,,,,,,,`), and with a line that is one no-break space and nothing else, the run does NOT stop. It exits 1, the row is ERROR with a blank-looking id, and r1 and r2 are still worked and TIED. Cases "NBSP alone IN the id column" and "the line is one NBSP and nothing else" in `cases output.txt`.
- Why: `load_figures` (lines 657-659) tests `not r["id"]`, and the id after the trim is the no-break space, which is not empty. Only a no-break space in another column, with the id truly blank, gives exit 2 (2 cases, both exit 2).
- id is the first column, so the plain one-character line is the shape that fails. The row is still loud (ERROR, RESULT: FAIL), so no figure passes wrongly: the fault is that the text and the goal state a stop the program does not make.

**F2. The GOAL's first kept refusal leaves out the quoted sheet name.**
- Where: GOAL.md line 46: whitespace other than a space or tab at an end of "a sheet or cell part" is ERROR for its row.
- Evidence: a made-up workbook with a sheet named `S` + no-break space, detail `'S\u00a0'!A1`, shown 5: the row is TIED, exit 0. Case "NBSP at end of QUOTED sheet part".
- The program's header (lines 68-69) does state this exception ("A quoted sheet name is taken exactly as written"), so the code and header agree; the GOAL's sentence, as written, does not. The other 6 detail shapes (gl key, value, accounts item, journal item, unquoted sheet, cell part) are ERROR for their row, as it says.

**F3. "The note names the column" is false for refusals the repair added to that passage.**
- Where: `tie_out.py` header lines 64-65, closing the passage that now lists them.
- Evidence, the notes as printed:
  - strict csv refusal: `GL could not be read (Error)`: no column;
  - figures row with no id: `bad input: a figures row has no id`: no column;
  - figures header: `bad input: figures header has whitespace other than space or tab at the end of a name`: no column named;
  - space inside account or store: `1 GL lines whose account or store equals a target once inner spaces are removed`: does not say which of the two.
- The second half is true: no note printed the content (a marker planted in the bad field of the 42 used-column cases appeared in the output of none).

**F4. read_gl's docstring leaves out refusals the reader makes.**
- Where: `tie_out.py` lines 503-509, the list of what read_gl raises on.
- Left out, each run: an empty GL (`GL file is empty`, line 528, ERROR for every row on the path); an unreadable Date or Debit/Credit on a matched line (counted in read_gl, lines 579-582, and ERROR for that row only, with other rows on the path still TIED).
- Also left out, read in the code and not triggered: `GL sum too long to add without rounding` (lines 255, 590-592).

**F5. Both passages give quotes as the csv refusal; the reader also refuses a bare carriage return.**
- Where: header lines 60-61 ("a GL the csv reader refuses under strict=True (a quote closed early or left open, in any column)"); read_gl docstring lines 508-509.
- Evidence: a bare CR inside the unused Description column gives `GL could not be read (Error)` for every row on the path. Case "bare CR inside unused Description".

## Claims tested and true

Each on made-up files; 76 cases, 73 as I predicted, the other 3 are F1 (2) and F2 (1). Full list: `cases output.txt`.
- In each of the 6 used GL columns: a quote; no-break space at an end; VT at a start; a non-ASCII character; a bad byte; a control character; DEL. All ERROR for both gl rows, including the row the line does not belong to (42 cases).
- A space inside account or store hiding a target: ERROR for every row (2). The same in a non-target account: no refusal (control).
- A quote closed early and one left open, used and unused column: csv.Error, ERROR for every row on the path (4).
- Wrong header, 8-field record, records differing from lines: ERROR for every row (3).
- A figures field with other whitespace at an end: ERROR for its row only (2). The same in the figures header: exit 2.
- A figures row with no id and a no-break space or text in another column: exit 2 (3).

## Minors (change no status)

1. A quote that does not open a field (mid-field, or after a leading space) in the unused Description is not refused and the figures tie. This matches the words "closed early or left open" as the csv reader means them, but a reader could take ` "desc` as "left open".
2. A NUL inside the unused Description is not refused and the figures tie. No passage claims otherwise.

## Risks (change no status)

1. Surface reading: `load_figures` decides "has no id" by whether the trimmed text is empty. The shape in F1 beats it. The fact that would settle it is whether the id holds anything other than whitespace.

## What I ran

- `change_list_check.py selftest`: the real repair PASS (outside the list 0, not applied 0); (a) planted change FAIL, (b) cut list FAIL, seal passed over: yes; `selftest: PASS`. Output in `st\`.
- `change_list_check.py check`: PASS, outside the list 0, not applied 0, 2 blocks, seal holds the list's md5. Output in `ck\`.
- `code_same.py` (mine): syntax tree identical with docstrings removed; 6,846 tokens and comments identical; 20 docstrings each side; changed: exactly the module's and read_gl's. It failed on a planted code change and, on tokens, on a planted comment change.
- `cases.py` (mine): the 76 cases, in `case_runs3\`; earlier partial runs in `case_runs\` and `case_runs2\`.
- `test_tie_out.py --bench tests`: `TESTS: PASS (1271)`, 0 __pycache__ on my bench.
- `tie_out.py gl_check.csv --out real_result.csv`: `RESULT: PASS`, exit 0, 9 rows, 9 TIED, counted from the output file. No GL line printed or opened by me.

## Files read, md5 before and after

| File | Size | md5 before | md5 after |
|---|---|---|---|
| `C:\AI_Building\AI_PRU\JOBS\06 PRU tie-out GL fix - 2026-11-22 HOME\BUILT r6 PASS\tie_out.py` | 35,519 | 84431953232c4e37d0e345d943ad0fa1 | same |
| `C:\AI_Building\AI_MISC\06 Benches\2026-11-22 PRU tie-out text repair - ANGIE-HOME-TR\piece\tie_out.py` | 36,299 | f12b2b176ab1510264fe1a013b944131 | same |
| `...TR\piece\test_tie_out.py` (run, not read) | 107,836 | 1ab8b575900ed2a88513cacbb77385f6 | same |
| `...TR\job06 text repair.changes.txt` | 2,461 | 4dc374898c030b7cd5fce4c1f294e7dc | same |
| `...TR\job06 text repair.changes.txt.seal` (read by the tool) | 33 | 50e74f9c896a84e521f1847a2c74e079 | same |
| `C:\AI_Building\AI_MISC\06 Benches\2026-11-22 PRU tie-out hand run real - ANGIE-HOME-HR1\gl_check.csv` (run, not opened) | 3,168 | f3941c4a5f90478d30008245ce741ac7 | same |
| `C:\AI_Building\AI_PRU\JOBS\06 PRU tie-out GL fix - 2026-11-22 HOME\GOAL.md` | 6,116 | 1b98e1ae8d3e2ef5d2dfbe3da91fc030 | same |

## What I did not check

- Rules program: run once as told (`--who ANGIE --act review --what budget`), 156,760 characters of output. I read about the first 2 KB (R-0001 to R-0023) and searched the first 14,000 characters for "blind", "checker" and "change list" (1 hit, R-0112). The rest I did NOT read. I did not make the skill's second call, for the repairer's role.
- The before's size and md5 come from your launch, which says LAWYER recorded them. I did not open LAWYER's folder, being blind, so I did not see that record myself.
- The code outside the two passages, except where a claim led to it. The test file's content. Mistyped codes (outside this check).
- The real GL's lines. Whether any real figures.csv holds the F1 shape.
- I did not open any VERDICT file of the job, the LAWYER folder, a checkpoint, LOG.md or `work\apply output.txt`.

## My own mistakes

1. My first `cases.py` run had a wrong control: it added a third matching line, so r1 was OFF for my reason, not the program's. It also crashed printing a character to the console. I fixed both and reran; no result here comes from that run.

## Background shells

NONE STARTED
