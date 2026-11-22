FAIL

# Blind check r5 of tie_out.py against GOAL.md (job 06), ANGIE-HOME-GC5, 2026-11-22 HOME

Done first: the skill `office-review-adversarially` was invoked, then the rules program was run once with `--who ANGIE --act review --what budget`. Its output is 153.1 KB; I read its first 2 KB and searched it for the checker rules, and did not read it whole.

Checked: GOAL.md 09296337, tie_out.py 0bdf676c, test_tie_out.py 973ef50c, gl_check.csv f3941c4a. All four md5s were the same at the start and at the end. The GL's md5 at the end is 94ae1ff9841d3de6bc9903402e32874b, the one gl_check.csv names.

## Findings (1)

### F1. A cell reference that is not one is read as another cell
- **File and line:** tie_out.py line 335 `cell = cell.replace("$", "")`, before the match on line 336.
- **Goal point:** "Shape 1", second bullet: a cell reference must match `[A-Za-z]{1,3}[1-9][0-9]*`.
- **Cause:** every `$`, at any place, is removed before the match. So the program decides on the text left after the removal, not on the reference as written.
- **The case:** made-up workbook `attack\case_book.xlsx`, Sheet1, A1 = 7, A15 = 42. The detail `Sheet1!A1$5` with shown `42` comes out **TIED**: it read A15. A figure pointing at a broken reference ties to a cell nobody named.
- **All 7 shapes that were read (each should be ERROR):** `A1$5`, `A$B1`, `$$A15`, `A15$`, `A$$15`, `$A$1$5`, `A$1$5`.
- **The fact that settles it:** a real reference has at most one `$` before the letters and at most one before the digits. Match the text as written against `\$?[A-Za-z]{1,3}\$?[1-9][0-9]*`, then take the letters and digits. The 4 legal spellings (`A15`, `$A$15`, `$A15`, `A$15`) all still read today and must keep reading.

## Minors and risks (change no status on today's GL)

- **M1 (numbered risk, surface reading).** A space inside a used field is printable ASCII, so the goal allows it (0x20). A line whose account or store has a space inside (planted `461 00-30`, `P OW`) matches nothing and leaves the sum without a word: on my made-up GL a figure that left out that line came out TIED. This is the goal as written, so it is not a finding. Real GL: 1,675 lines have a space inside Account, and 0 of them become a target account (46xxx-30 or 47700-30) when the space is removed; 0 lines have a space inside Store. The fact that would remove the risk: a list of the GL's valid accounts and stores.
- **M2.** 823 real GL lines have a Debit or Credit that parse_amount refuses (each holds a space inside). 0 are at store POW and 0 are on a target account, so the 9 figures are not touched. A future gl row whose store and account match one of them will be ERROR, loudly, not wrong.

## What I ran, with counts

| Run | Result |
|---|---|
| `python3.14 -I -B test_tie_out.py --bench run_tests_1` | `TESTS: PASS (1247)`, no `__pycache__` |
| attack\attack.py: every non-printable byte plus space, quote and comma, at start, middle and end of all 9 fields; multi-byte characters; quote and line shapes; blank-looking lines; field counts; headers; shown grammar and signs (points 1, 2, 3, 5, Shape 1) | 13,387 checks, 2 flagged, both M1 |
| attack\attack.py: cell references | 24 that are not valid: 17 ERROR, **7 read (F1)**; 11 good: 11 TIED |
| attack\attack2.py: point 5 on every figures.csv field, detail parts, text cell | 311 checks, 0 wrong |
| tie_out.py on gl_check.csv, `--out real\result.csv` | RESULT: PASS, 9 of 9 TIED |
| real\own_sum.py: own byte-level reader, no csv module | 874,156 records, 0 blank lines, 0 quote faults, 0 wrong field counts, 0 used fields outside printable ASCII or holding a quote |
| csv reader with strict=True over the whole GL | 874,156 records, 0 refused, 0 not 9 fields |
| Name scan of tie_out.py, test_tie_out.py, GOAL.md | 0 matches in each |

The checks could fail: the control with the line removed tied at 150 and went OFF at 175, and the planted shapes above came back ERROR.

## The 9 months (real GL, store POW, accounts 46xxx-30 and 47700-30, credit minus debit)

| Month | Shown | tie_out | Own sum | Lines (both) | Status |
|---|---|---|---|---|---|
| 2026 Jan | $15,553 | 15,552.61 | 15,552.61 | 95 | TIED |
| 2026 Feb | $60,160 | 60,160.28 | 60,160.28 | 31 | TIED |
| 2026 Mar | $201,004 | 201,004.26 | 201,004.26 | 32 | TIED |
| 2026 Apr | $200,238 | 200,237.82 | 200,237.82 | 34 | TIED |
| 2026 May | $246,286 | 246,286.44 | 246,286.44 | 34 | TIED |
| 2026 Jun | $191,234 | 191,234.34 | 191,234.34 | 34 | TIED |
| 2026 Jul | $171,426 | 171,425.99 | 171,425.99 | 34 | TIED |
| 2026 Aug | $180,524 | 180,524.17 | 180,524.17 | 33 | TIED |
| 2026 Sep | $132,795 | 132,794.91 | 132,794.91 | 33 | TIED |

Difference to the cent in all 9: 0.00. Source: the GL named in gl_check.csv, all its records.

## What I did not check

- Goal point 4 against the job 05 build itself: I was told not to open earlier work, so "everything else holds" rests on the build's own 1,247 tests and my planted cases, not on a comparison of the two programs.
- Any real workbook: cell rows were tried only on my made-up books.
- `--out` path attacks beyond what the build's own tests cover.
- What the 823 lines of M2 hold: I counted them and did not look at their content.
- The rules program's output in full (see the top).

## My own mistakes

1. My first test run failed with a usage line because I had not made the `--bench` folder. I made it and ran again.
2. My attack script expected a space in the middle of a field to be refused. The goal allows it, so its 2 flags are M1, not findings.

## Background shells

NONE STARTED
