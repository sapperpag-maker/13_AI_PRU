FAIL

# Blind check 3 of the job 06 words-only repair (tie_out.py docstrings, GOAL.md)

Checker: job agent launched by Angie (ANGIE-HOME), machine HOME, 2026-11-22. This is a finding, not an acceptance: only Sergio accepts.
Target: `piece\tie_out.py` md5 e14f2ecba45274799e3e2f1a2f31d4ad (37,086 bytes); `GOAL.md` md5 4f284b6eb7528c92554c0c1f31e65b0a (6,532 bytes).

## Answers to the four questions

1. **Lists: yes.** Stage B is stage A with exactly list 2; the after is stage B with exactly list 3. Each: selftest PASS (planted change FAIL, cut list FAIL), check PASS, outside the list 0, not applied 0. **Code: yes.** After and baseline have the same 6,057 tokens and comments once docstrings are removed. Of 20 docstrings, exactly 2 differ: `<module>` and `read_gl`. My program caught a planted code change and a planted comment change.
2. **Docstrings: no.** Seven findings (F1 to F7 below): all seven are in the module paragraph, and F6 is also in read_gl. read_gl leaves out no refusal it makes and states none it does not make; its one false sentence is the bare carriage return (F6).
3. **GOAL "Two refusals kept": no.** F1 to F4 are in it. Its other sentences held, including that both refusals are differences from job 05 (run on the job 05 build, md5 a8f90d60).
4. **Tests and real run: yes.** `TESTS: PASS (1271)`, exit 0, no `__pycache__`. On gl_check.csv: `RESULT: PASS`, exit 0, 9 rows, 9 TIED.

## Findings (7)

Line numbers are of the after. Every case is a made-up file, in `cases.py` on this bench.

**F1. "holds anything in another column" is false for a space or a tab.** tie_out.py lines 65-67; GOAL.md line 47.
The sentence predicts exit 2, no RESULT. A row with an empty id and only a space in label (`, ,,,,,,,,`), or only a tab: the row is skipped, exit 0, `RESULT: PASS`. Code: load_figures line 651. List 2 dropped the old words "after the trim" from this clause.

**F2. A no-break-space row does not always end RESULT: FAIL, exit 1.** tie_out.py lines 67-70; GOAL.md line 47.
Two lines that are each one no-break space, or two rows with only a no-break space in the id column: exit 2, no RESULT, stderr "duplicate id". The other rows are not worked. Code: lines 670-671.

**F3. A quoted sheet name is not "taken exactly as written".** tie_out.py lines 73-74; GOAL.md line 46.
`'It''s'!A1` on a workbook holding both sheets `It''s` (A1 = 4) and `It's` (A1 = 3) reads `It's`: shown 4 is OFF "rounds to 3", shown 3 is TIED. Code: line 340, `.replace("''", "'")`.

**F4. A quoted name ending in a no-break space is not always "read as that sheet's name".** tie_out.py lines 73-74; GOAL.md line 46.
`'Master<NBSP>'!F1` on a sheet of that exact name, F1 = 5, shown 5: ERROR "Master past column E". The Master guard strips all whitespace from the name before comparing. Code: line 363.

**F5. "other whitespace at an end is ERROR naming the part" is false at either end of the whole detail field.** tie_out.py lines 71-73.
A no-break space before the first gl key, after the last gl value, before an unquoted sheet name, or after the cell part (4 cases): each is ERROR, but the note says "figures column detail" and names no part. The same space on an inner part names it, such as "gl detail store value". Code: lines 655 and 698-701 fire before parse_gl_detail and split_ref.

**F6. A bare carriage return outside quotes is not always refused.** tie_out.py lines 62-64; read_gl docstring lines 514-516.
A carriage return inside a field is refused. One just before the line end (CR CR LF), or as the last byte of the file: accepted, both rows TIED, exit 0, `RESULT: PASS`.

**F7. "its note names the column" is false when the same GL also has a fault the csv reader refuses.** tie_out.py lines 58-59.
A no-break space at the end of an account on line 1 and a quote closed early on line 2: both rows ERROR, note "GL could not be read (Error)", no column named. The csv error stops the read before the column notes are built (lines 615-625 are not reached).

## Claims tested and true

Exit code, RESULT line, other rows and note content, one case or more each: quote, end whitespace, non-ASCII, bad byte, inner tab and control character in a used field (ERROR for every gl row, note names the column); the same in an unused column (no effect); space inside account or store matching a target (ERROR, no column), not matching (no effect); quote closed early, left open, space after closing quote, CR inside a field; empty file, BOM only, wrong header, tab-padded header, records differing from lines, 8 and 10 fields, a line of one no-break space in the GL; unreadable date, debit, credit on a matched line (that row alone), on another account (nothing); figures field and header whitespace; empty id with text or no-break space (exit 2); single no-break-space id row and line (ERROR, others worked, exit 1); id not first column; inner detail parts; quoted names with inner spaces and a trailing no-break space on a non-Master sheet.

## Minors (change no status)

None.

## Risks (change no status)

R1. read_gl's refusal "a GL sum too long to add without rounding" exists and fires when I forced a 5-digit context, but with amounts capped at 24 digits and a 60-digit context I could not reach it from a real file.

## Files read, md5 before and after (unchanged)

| File | Bytes | md5 |
|---|---|---|
| Baseline `BUILT r6 PASS\tie_out.py` | 35,519 | 84431953232c4e37d0e345d943ad0fa1 |
| Stage A `work2\before\1\tie_out.py` | 36,299 | f12b2b176ab1510264fe1a013b944131 |
| Stage A `work2\before\2\GOAL.md` | 6,116 | 1b98e1ae8d3e2ef5d2dfbe3da91fc030 |
| Stage B `work3\before\1\tie_out.py` | 36,951 | c3a289ca4e776699e770b0bdde84666a |
| Stage B `work3\before\2\GOAL.md` | 6,394 | 20336d980f70817d42da09901f4cdb3e |
| `job06 text repair 2.changes.txt` | 4,394 | 67d800997d95e6b6f5fbe6eae7cc0818 |
| `job06 text repair 3.changes.txt` | 1,351 | da731cfc9aef63dd3ce64860615338ce |
| After `piece\tie_out.py` | 37,086 | e14f2ecba45274799e3e2f1a2f31d4ad |
| After `GOAL.md` | 6,532 | 4f284b6eb7528c92554c0c1f31e65b0a |
| `piece\test_tie_out.py` (run, not read) | 107,836 | 1ab8b575900ed2a88513cacbb77385f6 |
| `gl_check.csv` (run, not opened) | 3,168 | f3941c4a5f90478d30008245ce741ac7 |
| Job 05 `BUILT r5 PASS\tie_out.py` (copied, run, header lines read) | 29,547 | a8f90d601cfd855442b16d39765a9cea |
| `change_list_check.py` (run) | 79,121 | 4ec1baf3b86243c5ca36c6701d99817b |

## What I ran

All with `python3.14.exe -I -B`, on copies on this bench unless named:
- `change_list_check.py` selftest and check, both lists. List 3 used the sealed list and the real after, read only. List 2 names the after's final paths, so it ran on a copy of the list with only those two paths changed to my stage B copies, resealed here; `extra.py` proved the copy equals the sealed list once the paths are put back.
- `code_same.py`, `cases.py`, `extra.py`, `j5_notes.py`.
- `test_tie_out.py --bench testbench`; `tie_out.py gl_check.csv --out real_result.csv`. Only the RESULT line and status counts were printed. `real_result.csv` holds sums per account and no GL line.
- Rules program, once, as launched: 156,760 characters, 2,147 lines. I read the first 25,000 characters and the first 60 lines matching blind, checker, docstring, change list or verdict. The rest was not read.

## What I did not check

- The stage A, stage B and baseline md5s come from the launch, written by the repairer's desk; I had no record the repairer did not write. The code proof ties the after to the baseline directly, but the baseline's own md5 is taken from the launch.
- The first change list (blind), so stage A's making from the baseline is proved only for code and comments, not for its words.
- The rest of the program's docstrings (the two changed ones were read in full for the named paragraph and read_gl; the module docstring outside that paragraph was not tested).
- GOAL.md outside "Two refusals kept". In that section, the quoted verdict md5, Sergio's 76 and 77 and Piston's relay were not traced (LAWYER's folder is closed to this check).
- Mistyped codes: outside this check.
- The rules program's second call for the repairer's role, which the one-check skill names: the launch said to run the program once.

## Blind

No file named VERDICT*, no "text check" bench but my own, no AI_LAWYER, no checkpoint, no LOG.md, no first change list, no shapes, no "apply output.txt" was opened before these findings were written. Lists 2 and 3 carry first lines and block labels naming earlier findings by number; I saw them and did not use them.

## My own mistakes

1. The first list-check runs failed because I had not copied the seals. 2. The next failed because I passed `--after` twice, and the tool keeps only the last. Both refused before reading any after; the runs above are the good ones. 3. `cases.py` crashed once printing a character to the console; fixed and rerun. 4. My first job 05 comparison used a header job 05 refuses, so it proved nothing; rerun on job 05's own header.

## Background shells

NONE STARTED.
