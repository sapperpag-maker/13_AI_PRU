PASS

# Blind check r5 of tie_out.py (a8f90d60) and test_tie_out.py (c9e6562a) against GOAL.md (c44120a0)

Checker: blind job agent for Angie (ANGIE-HOME, machine HOME), 2026-11-22. I did not build this program.
Skill office-review-adversarially invoked through the Skill tool at 13:57, before any file was read.
Files checked: the three bench files above, md5 re-taken at 13:57 and again at 14:02, unchanged.

## Repairs checked first
- F1 (tie_out.py line 214, to_decimal): float cell 1234567890123.125 against shown 1,234,567,890,123.12 -> OFF, recomputed 1,234,567,890,123.13, difference 0.01; shown ...123.13 -> TIED; -1234567890123.125 against -...123.12 -> OFF. Case probe/c1.py, command `python3.14 -I -B probe/probe.py c1`, rows f1a, f1b, f1c. Repaired.
- F2 (line 645, difference via SUM_CTX with Inexact and Rounded trapped, lines 649-650): cell 1e-70 vs shown 1 -> ERROR "difference too long to compute without rounding", blank difference, exit 1, no crash (row f2a); cell 1e-300 vs shown 0.000001 -> ERROR (row t1). An exact difference still prints (f2b, t2, den: TIED with every digit). Repaired.

## Findings
NONE. 0 findings.

What I tried that could have produced a finding, and what came back (all from probe/c1.py, c2.py, c3.py and shell runs on the bench):
- Cells: 2.675 vs 2.68 TIED; 0.1+0.2 vs 0.3 TIED; 14.499999999999998 vs 15 TIED; int 1234567890123456 vs ...460 TIED, vs ...456 OFF; float 123456789012345678.0 cut to ...346,000 TIED; 5e-324 and 1e-300 vs 0 TIED with full digits printed; -0.0 vs 0 and -0 TIED, printed 0; -0.004 vs 0.00 OFF (sign), vs -0.00 TIED; k suffix 1,234,567,890.1k TIED.
- Rule 2: cell -0.5 with format `0%;"neg"`, shown -0.5% -> OFF (difference -49.5); -50% and (50%) TIED; cell 0.5 shown 50% and 0.5 both TIED.
- Rule 1: datetime cell, 45000 with a date format, boolean, text "12" -> ERROR each.
- GL: credit-debit 985.25 and journal-filtered 990.25 and debit-credit -990.25 recomputed by hand from the lines and matched; a 7-decimal amount on a matched line -> ERROR for every row touching it; unreadable amount, unreadable date, quoted newline (records 1 vs lines 2), 10-field line, unknown key, from after to, 2027-1-1 and 1/1/27 dates -> ERROR; gl shown 1% -> ERROR; dead account pattern -> ERROR; $1.5, -$0.5, ($0.25) amounts sum 0.75 TIED. Description text SECRETCUSTOMER never appears in stdout or stderr (checked by string search).
- --out on existing file spelt `existing.csv.`, `EXISTING.CSV`, `existing.csv ` (trailing space), `./sub/../existing.csv`, and `NUL` -> exit 2, file md5 401b30e3 unchanged. Suite covers `\\localhost\C$`, hard link, `:zz` streams, made-after-check.
- figures.csv with a `Scale` column -> exit 2 with usage line.
- Suite: `python3.14 -I -B test_tie_out.py --bench "<bench>"` -> `TESTS: PASS (438)`, no __pycache__ (find returned none). Its passing is not this verdict.

## Minors (change no status or figure)
1. tie_out.py line 246: the size column drops commas before its whole-number check, so a size written "2,2,2" is read as 222 and accepted (row z1 in probe/fz.csv: TIED). The size still has to equal the file's size, so no status changes; the grammar is looser than "strict".
2. tie_out.py lines 595-599 with 243-259: a gl row's source that cannot be opened (GL locked with msvcrt.locking, as when open in Excel) is not caught per row: the whole run stops with exit 2 and "stopped on an unexpected PermissionError; no result", no table (probe/lock.py with probe/fl.csv). A cell row in the same state becomes a row ERROR (line 591). Exit 2 is the program's stated code for a crash and no wrong status is written, so I file it as a minor; if the Owner counts a locked source as valid input, this is a finding.
3. tie_out.py line 655: the note can read "rounds to -0.00" (row s1, cell -0.004 shown 0.00); the docstring's "-0 prints as 0" covers only the recomputed, difference and sum columns, which do print 0.

## What I did not check
- The old job 04 spec behind GOAL point 5: judged from the code, the tests and plain correctness only.
- `\\?\` spellings on an existing file by my own run (the code refuses any ':' past index 1, line 685-690; the suite covers the stream cases).
- Very large files, memory and speed; files changed between the md5 check and the read (time-of-check window, lines 256-259 vs 307/605).
- Real customer workbooks or GLs (none opened, by the launch).
- Excel's own display of floats beyond the 15-digit half-up cut the goal names.
- The rules program STEP 0 of the skill was not run: the launch forbids opening any file outside the bench, and the rules program reads files outside it.

## My mistakes
- Probe harness indexed the source column wrong on first run (IndexError in my probe.py), fixed and rerun.
- Probe c2 first run crashed printing the ≠ sign to a cp1252 console (my harness, not the program), rerun with UTF-8.
Neither touched the program or any file outside the bench.

## Background shells
NONE STARTED.

## Bench contents written by this check
PROGRESS.md, VERDICT.md, probe\ (probe scripts and made-up workbooks, GLs, figures), test-runs\ (made by the suite).
