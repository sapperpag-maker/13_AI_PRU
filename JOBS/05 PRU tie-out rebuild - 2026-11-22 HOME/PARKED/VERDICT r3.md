FAIL

# Blind check r3 (smaller shape) of the job 05 tie-out program

Checker: a job agent launched by Angie (ANGIE-HOME, HOME), 2026-11-22. I did not build the piece. I invoked the skill office-review-adversarially before reading anything, and asked the rules program (`--who Angie --act review --what budget --moment "before checking"`; "tie-out program" is not on what.txt and was refused).

Piece, md5 checked first, both match:
- `C:\AI_Building\AI_MISC\06 Benches\2026-11-22 PRU tie-out rebuild - ANGIE-HOME-RB\tie_out.py` f94eb1f30b566da6ddaffb2e497a0984, 28,689 bytes
- `...\test_tie_out.py` 8caa1d343d8f50398b82c166067f91c6, 65,665 bytes

Goal: `C:\AI_Building\AI_PRU\JOBS\05 PRU tie-out rebuild - 2026-11-22 HOME\GOAL.md`, plus the smaller shape and the core test in the launch brief.
My findings were written to `OWN_FINDINGS.md` on this bench before test_tie_out.py was opened. No claim file was opened (PROGRESS.md, mutants*, suite*, LOG.md, PARKED, rebuild-check folders, the trash).

## Failing findings: 1

F1. Integer cells are not cut to 15 significant digits, so a figure Excel never shows comes out TIED.
- File and line: tie_out.py lines 202-205, `to_decimal`: `if isinstance(value, int): return Decimal(value)`. Only floats go through `format(value, ".15g")`.
- Case: a made-up xlsx (`work\c1.xlsx`) whose cell A21 holds `<v>1234567890123456</v>` (16 digits, no point; openpyxl returns a Python int, and a workbook written by openpyxl from a Python int is stored this way). Excel holds it as a double and shows 1,234,567,890,123,460.
- Expected, under the smaller shape ("Cells: at most 18 digits before the point, cut to 15 significant digits") and the program's own docstring (cut "as Excel does"): shown 1,234,567,890,123,456 is OFF; shown 1,234,567,890,123,460 is TIED.
- Got: `a21_int16_exact` (shown 1,234,567,890,123,456) TIED; `a21_int16_excel` (shown 1,234,567,890,123,460) OFF, difference -4.00.
- The same with an 18-digit int 123456789012345678 (cell A5): `a5_int18_exact` TIED; `a5_int18_excel` (123,456,789,012,346,000) OFF, difference -322.00.
- The builder's suite does not test this: its only big integer cell is 999999999999999000 (15 significant digits, test_tie_out.py line 161).
- Weight: this needs a whole number of 16 to 18 digits, far above any PRU money figure. It still breaks the stated shape and lets a wrong figure tie, which the brief makes a FAIL.

## Minor notes (not a wrong TIED; not counted)

- M1. The recomputed, difference and GL sum columns always show 2 decimals (`fmt`, line 212). Three examples:
  - A 0.0145% cell shows recomputed 0.01.
  - A difference of 0.000001 shows 0.00 or -0.00.
  - A GL sum of 1,999,999,999,999,999,999,999.997999 shows as 2,000,000,000,000,000,000,000.00 beside a TIED 2,000,000,000,000,000M.

  The status is right in each case, but the columns can mislead.
- M2. A stored -0.0 shows recomputed -0.00 and difference -0.00.
- M3. A shown value of `$12.5%` (dollar and percent together) is accepted and compared as 12.5%.
- M4. md5 accepts an 8-hex prefix (line 243), which is weaker than the full 32.
- M5. openpyxl turns a number with a date format into a date, so that cell is ERROR. The library reads the format even though the program does not. This is the safe direction, and goal item 1 calls date cells ERROR.
- M6. An --out inside a folder that does not exist prints the tables, then says "stopped on an unexpected FileNotFoundError; no result" and exits 2. No file is written, but the message does not say the folder is missing.

## What held (each counted this session, all on made-up files in work\)

My cases are in `attack.py`: 98 checks plus a 36-value shown grammar table, and a race case.

- **Arithmetic.** No wrong TIED anywhere in these cases:
  - negated and bracketed GL amounts at 18+6 digits and just past (7 decimals, 19 digits);
  - a 61-digit amount;
  - a 2,001-line sum of 999,999,999,999,999,999.999999 shown in M at 0 and 6 decimals;
  - cells of 1E-300, 4.94E-324 x 100, 1.23456789012345E+17 (shown plain, in M, and with % past the cap), 16-significant floats, -0.0 and 1E400;
  - k and M at 6 decimals, and k with % (refused).
- **The three earlier findings, retested with fresh cases.**
  - r1 F1 (`file:zz`, `::$DATA`, `:zz:$DATA`): exit 2, file unchanged.
  - r1 F2 (19 to 22-digit sums): ERROR where shown cannot hold them, exact otherwise.
  - r2 N1 (a 61-digit negated amount, and an 18+6 negated amount on both sides): ERROR or exact.
- **--out.** 22 spellings and links of one existing file all exit 2, with bytes and mtime unchanged:
  - the plain path and 3 stream forms;
  - `\\?\`, `\\?\UNC\localhost\C$`, `\\localhost\C$`, `\\127.0.0.1\C$` and `\\.\`;
  - upper case, trailing dot, trailing space, `. .`, forward slashes and `..`;
  - a folder, the 8.3 short name, a hard link, a junction and NUL.

  A race also held: a file planted 1 s into a 400,000-line run was kept byte-identical, with exit 2.
- **GL header.** Exact (7 variants refused, BOM allowed).
- **Records against lines.** A multi-line quote, CR-only lines and an NBSP line are ERROR. A stray quote swallowing a line plus a `""` line cannot equalise the counts, because both lower the record count.
- **GL fields.**
  - 8 and 10 fields are ERROR.
  - Store is exact (case kept, spaces trimmed).
  - Accounts: exact, x/X, overlap counted once, a dead account is ERROR, an Arabic-Indic digit does not match x.
  - Journal is exact.
  - Dates are inclusive. A bad date on a matched line is ERROR even outside the range. Feb 30 and 2-digit years are ERROR.
  - Both sides work.
  - The amount grammar refused all 17 bad variants.
- **figures.csv.**
  - A scale column in 3 spellings exits 2.
  - These also exit 2: a duplicate column, a missing column, a duplicate or blank id, an extra field, no rows, a latin-1 file, a missing file, a wrong arg count, and --out with no path.
  - A wrong md5 or size is ERROR, and so is a 7-hex md5.
  - Exit codes are 0, 1 and 2 as specified.
- **Leaks.** Description text planted in every GL line never appeared in stdout, stderr or the --out file.
- **The builder's suite.** `python3.14 -I -B test_tie_out.py --bench <this bench>` gave `TESTS: PASS (391)`, exit 0. It wrote no `__pycache__`, and the builder's bench listing was unchanged.

## My mutants: 30 caught of 32

`my_mutants.py`, with copies in `mut\`.
- **m06** (SUM_CTX traps removed) was missed. I judge it equivalent: under the 18+6 caps, no input can need more than 60 digits.
- **m09** (the lexists check removed) was missed. Mode "x" still refuses every existing file; only NUL changes, from exit 2 to exit 0, and no file is written.
- **m10** (mode "w") was caught only by the race case, run separately.

## What I did NOT check

- Symbolic links, dangling or not: this account could not create one, so the --out symlink cases were not run.
- Job 04's full spec text. It sits in PARKED, which I was told not to open. "Everything else holds as in job 04's spec" was checked against the brief's list and the program's docstring, not against that spec.
- Real data and real Excel files, as the brief said. Every workbook was hand-made XML, not saved by Excel.
- GL files in encodings other than UTF-8, beyond an invalid-byte description.
- GL files over 400,000 lines, and timing or memory.
- The Master sheet rule (columns B to E): I did not test it.
- The md5 being checked in pass 1 and the GL being read in pass 2, so a file swapped between the two would not be seen. I did not try that.
- Network paths other than localhost.
- The NUL, CON and COM device names beyond NUL.
