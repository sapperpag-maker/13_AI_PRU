FAIL

# Job 05 tie-out rebuild - blind last check r4 (ANGIE-HOME-RC4)

Checker: a job agent launched by Angie; did not build the piece. Skill office-review-adversarially invoked before anything was read. Rules program asked twice (helper / before checking / review; angie / before building).
Piece: tie_out.py md5 81e79f404b3b38444893ad0b68401b50 (29,322 B), test_tie_out.py md5 303a8c10326f6536fdf971b393d89000 (72,275 B); both matched the launch before any check.
Goal: C:\AI_Building\AI_PRU\JOBS\05 PRU tie-out rebuild - 2026-11-22 HOME\GOAL.md, plus the smaller shape in the launch.
Builder's suite: `python3.14 -I -B test_tie_out.py --bench <this bench>\suite_run` ends `TESTS: PASS (430)`, exit 0, no __pycache__ written.
Not opened: PROGRESS.md, mutants*, suite*, mutants.py on the builder's bench; LOG.md; any check folder but this one; the trash; job 04 PARKED; any real data.

## Failing findings: 2

### F1 - a float cell is cut to 15 digits half EVEN, not half up: a wrong figure ties
- Where: tie_out.py line 214, `return Decimal(format(value, ".15g"))`. Python's format() rounds the exact binary value half-even; the int path (line 213) uses CUT15 half up.
- Cases (each its own raw-XML workbook, cells\<id>.xlsx, run from cells\fig.csv by t_cells.py):
  - fhalf4: cell `<v>1234567890123.125</v>`, shown `1,234,567,890,123.12`. Expected OFF (half up to 15 digits is ...123.13). Got TIED, recomputed 1,234,567,890,123.12.
  - fhalf3: same cell, shown `1,234,567,890,123.13`. Expected TIED. Got OFF.
  - fhalf7: cell `<v>-1234567890123.125</v>`, shown `-1,234,567,890,123.12`. Expected OFF. Got TIED.
  - fhalf2: cell `<v>1234567890123445.0</v>`, shown `1,234,567,890,123,440`. Expected OFF. Got TIED. The same number spelled `<v>1234567890123445</v>` (i16a/i16b) gives ...450 and OFF: one stored number, two answers.
  - fhalf1: that float cell, shown `1,234,567,890,123,450`. Expected TIED. Got OFF.
- The class: any float holding an exact half at its 16th significant digit (values like x.5, x.25, x.125 with 16 significant digits). The fact that settles it: cut the exact binary value (`Decimal(value)`, exact for a float) with CUT15 half up, as the int path does.

### F2 - the difference subtraction is rounded silently
- Where: tie_out.py line 645, `diff = res["value"] - shown_value(sh)`, done in the 60-digit WIDE context, which does not trap Inexact or Rounded.
- Case tinyd: cell `<v>1.23456789012345E-50</v>`, shown `1`. Status OFF (right). Difference printed `-0.999999999999999999999999999999999999999999999999987654321099` (60 digits, rounded). Exact: `-0.99999999999999999999999999999999999999999999999998765432109876550`.
- Against the smaller shape: "every sum, negation, subtraction and x100 is exact or ERROR" and the difference column "never rounded". Reach: only cells below about 1E-44; no status changes.

## Minor notes (not failing)
- N1 cell texts `<v> 12</v>` and `<v>1_000</v>` read as 12 and 1000 (openpyxl's int() cast). Excel never writes these.
- N2 the GL accounts table prints partial sums for a row that is ERROR (gl\date_bad.csv: sum 5, 1 line; the row says ERROR).
- N3 cell `<v>-0.0</v>`, shown `0`: TIED (right), but the note says "rounds to -0" (line 653).
- N4 --out naming an existing file with a trailing backslash: exit 2, file unchanged, but the FIGURES table is already on stdout with no RESULT line (the open is at line 730, after the print).
- R1 (risk; no wrong value against the brief) an int text of 16-18 digits is cut exactly, as the brief orders. Excel would first take the nearest double (`123456789012344501` would show as ...344,000 in Excel; the program gives ...345,000). Excel itself never writes such a text.

## What held (counted this session)
- Cells, 45 cases: ints cut at 15, 16, 17 and 18 digits, the half, negatives, -0, bool 0 and 1 (ERROR), exponent ints `1E+17` and `1.5E2`, `1E+18` and 19 digits (ERROR), NaN and inf (ERROR), text, error and str cells (ERROR), x100 for % (r7's example: cell -0.5, shown -0.5% is OFF), k and M, $ with % (ERROR), tiny and huge printing. 39 as the rule says; 5 are F1; 1 is F2.
- GL, 55 cases: header (BOM, space, case), records against lines (embedded newline, a lone CR, a NBSP line, blank lines, no final newline, LF only, CR only, NUL, 10 fields), both grammars, 18 digits + 6 decimals, negatives, accounts exact and x patterns (dead pattern, length, Arabic digit), store, dates inclusive and bad dates, journal, side, %, sign rule and -0, half up. All as the rule says. No description text or doc # in stdout, stderr or the --out file.
- --out, 24 spellings onto an existing file or folder: plain, case, forward slashes, trailing dot, space and ". .", `:zz`, `::$DATA`, `\\?\`, `\\localhost\C$`, `\\127.0.0.1\C$`, `\\?\UNC\localhost\C$`, `\\<hostname>\C$`, 8.3 short name, hard link, `..`, folder, folder with backslash, relative, drive-relative, trailing backslash, `\\.\`, `\\?\GLOBALROOT`. All exit 2; the file unchanged, no stream added. A new path is written ending RESULT: PASS; a second run onto it exits 2.
- md5 wrong, size wrong, md5 blank, md5 of 7 characters: ERROR. Scale column: exit 2. Exit 0 all tied, 1 any not tied, 2 no arguments.
- Earlier findings retested with fresh cases: r1 F1 (stream) holds; r1 F2 (a 25-digit sum of four lines prints exactly 2,999,999,999,999,999,999.999996) holds; r2 N1 (negated 24-digit amount exact) holds; r3 F1 (16-18 digit ints) holds; r3 M1 (columns print every digit) holds; r3 M3 ($ with %) holds.

## Mutants: 34 caught of 37 (mut.py, mut\m01..m37.py)
Survivors: m27 (lexists check off) and m29 (open mode "a"): each guard is backed by the other; with both changed (m36) it is caught. m32 (sum context stops trapping Inexact): no sum of capped amounts can reach 60 digits, so it cannot change an output.

## What I did NOT check
- Excel's own display: no Excel was started; "half up as Excel shows" is taken from the brief and the program's docstring.
- Symbolic links (this account may not make them), junctions, network shares other than this machine, other drives.
- openpyxl turning a numeric cell with a date-like format into a date (it would be ERROR, not a tie); the Master sheet column limits; GL files of real size or speed.
- The builder's 430 tests one by one: only their end line was read.
- Non-Windows systems.
