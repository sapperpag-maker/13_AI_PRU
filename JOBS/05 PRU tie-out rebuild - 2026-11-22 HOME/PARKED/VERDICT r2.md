FAIL

# Verdict - job 05, tie-out rebuild, blind check round 2

**Checker:** a blind checker launched by Angie (ANGIE-HOME, HOME). I did not build the piece. I invoked the skill office-review-adversarially before reading anything, and asked the rules program before starting.

**The piece:**

| File | md5 | Size | Matches the launch |
|---|---|---|---|
| tie_out.py | b257dfdd | 27,534 bytes | yes, checked first |
| test_tie_out.py | 6fe80c36 | 54,824 bytes | yes, checked first |

**The yardstick:** `C:\AI_Building\AI_PRU\JOBS\05 PRU tie-out rebuild - 2026-11-22 HOME\GOAL.md`, read whole.

**Blind order:** OWN_FINDINGS.md was written before test_tie_out.py was opened. I opened none of the forbidden paths.

## Failing findings: 1

### N1. A wrong figure comes out TIED, and the right one comes out OFF. A GL amount with more than 60 significant digits is rounded silently when it is negated.

This is round 1's F2 class, still open.

**Case.** All files are under `<bench>\work\`.
- The GL is `neg61.csv`: the exact header, then one line, `4000,J,1/5/2026,1,d,1.<57 zeros>449,,0,S1`.
- The figures file is `f001.csv`:
  - detail: `store=S1;from=2026-01-01;to=2026-12-31;side=credit-debit;accounts=4000`;
  - shown: `-1.<57 zeros>5` (58 decimals).

**Expected.** The true sum is -1.(57 zeros)449. Rounded half up to 58 decimals, that is -1.(57 zeros)4. I confirmed this with a 200-digit context. So shown ...5 is OFF.

**Got.**
- Status TIED, `RESULT: PASS`, exit 0, note "rounds to -1.(57 zeros)5".
- With the right shown, -1.(57 zeros)4 (f002.csv), the status is OFF and the result is `RESULT: FAIL`.

**The same TIED came from three more cases:**
- a credit `(1.<57 zeros>449)` in parentheses, under credit-debit;
- a credit `-1.<57 zeros>449`;
- a two-line case on accounts 400x: debit 1.<57 zeros>449 plus credit 1, where shown -0.(57 zeros)5 TIED.

**Where.**
- tie_out.py line 517: `run()` executes in `localcontext(WIDE)`.
- Line 66: WIDE traps only InvalidOperation, DivisionByZero and Overflow, so Inexact and Rounded pass silently.
- Unary minus runs in WIDE, not in SUM_CTX, at three places:
  - line 171: `return -d if neg else d`;
  - line 452: `exact_sum(cr, -dr)`;
  - line 454: `exact_sum(dr, -cr)`.
- The negated amount is rounded to 60 digits, to ...45. The rounding is then repeated to shown's 58 decimals, giving ...5. exact_sum only sees the already-rounded value.
- The 18-digit cap (lines 168-169) limits digits before the point only. The amount grammar (line 93) allows unlimited decimals.

**Controls.**
- The same 61-digit amount as a plain, not negated, credit gives ERROR ("GL sum too long to add without rounding").
- A negated 60-digit amount ties right and is OFF when wrong.
- So the hole is exactly the negation.

**The fact that would settle it.** Every operation on a GL value must run where rounding raises, the negation included: `SUM_CTX.minus(...)`, or SUM_CTX set as the run's context. The other way is a cap on total significant digits when the amount is read.

**Why it is a FAIL.**
- The core test says "No wrong figure comes out TIED".
- The docstring (lines 25-28) claims "No number is ever rounded silently". It is false.
- The data is absurd (61 significant digits). Round 1's F2, with 28 digits, was the same kind of absurd input and was failed on it.

**The builder's test does not cover it.** test_tie_out.py gives `TESTS: PASS (346)` on this piece. The 60-digit tests in it do not negate a long amount.

## Minor notes (not verdict-deciding)

- **M1.** figures.csv accepts unknown columns silently, so `scales`, or `scale` followed by a zero-width space (U+200B), runs with exit 0. The goal names only `scale`. Plain, space-padded, upper-case and NBSP-padded `scale` exit 2, which is correct. No wrong TIED results, since rule 2 compares unscaled. (load_figures, lines 480-487.)
- **M2.** Notes can show Decimal's scientific notation, for example "rounds to -5E-58" and "-1E-12%" (line 621).
- **M3.** Device-name `--out` on Windows 11:
  - `nul.csv` and `aux.csv` are made as ordinary new files, exit 0;
  - `NUL`, `CON` and `<bench>\NUL` exit 2, "already exists";
  - `COM9` exits 2 on FileNotFoundError.
  - No existing file was changed.
- **M4.** The 15-digit cut (line 185) applies to float cells only, so an int-typed cell keeps 16 to 18 digits. Not reproduced: openpyxl gave me back a float.
- **M5. Test gaps.** Two of my 40 mutants survive the builder's test:
  - m35: a crash exits 1 instead of 2;
  - m37: the duplicate-id check is removed.

## Retest of round 1

**F1 held.** 31 fresh `--out` spellings each exit 2, with no file changed and no stream written:
- streams: `:zz`, `::$DATA` and `:zz:$DATA`, on the target, on the figures file, on a GL source and on a folder;
- path spellings: trailing `.`, ` ` and `. .`; upper case; forward slashes; `\\?\`; `\\localhost\C$`; `\\?\UNC\localhost\C$`; `\\127.0.0.1\C$`; `\\.\C:`; no drive letter; `.\`; `dir\..`;
- links: a hard link; and a junction (the junction itself, a file through it, a stream through it, and `.\` through it);
- arguments: `--out` given twice, and `--out=` given as one argument.

The file is opened with mode "x" (line 698).

**F2 held for digits before the point.** It did not hold for negated long tails (see N1):
- amounts of 19 and 28 digits are ERROR;
- an 18-digit amount ties when right and is OFF by 1;
- a 61-digit sum is ERROR;
- a 60-digit sum is exact;
- three 18-digit lines summing to 19 digits tie in M.

## What was checked, and its shape

- **attack.py:** 217 result lines. **attack2.py:** 27 result lines. Each case is a fresh file of my own.
- The cases cover:
  - the shown grammar: 38 forms;
  - the GL amount grammar: 18 bad forms;
  - the header: 8 cases;
  - records against lines: 5;
  - accounts, store, dates, journal and side: about 30;
  - md5 and size: 5;
  - the sign rule and rounding: 9;
  - cells: 40 in one book and 13 at the % cap;
  - the figures header and scale: 6;
  - exit codes: 6;
  - leaks: 4 runs (stdout, stderr and --out searched for a secret placed in each GL field, in the header, in a multi-line record and in a text cell);
  - `--out`: 31 spellings, 6 device names and 4 through a junction.
- **Could fail:** yes. It did fail on N1, and 38 of my 40 mutants were caught by the builder's suite.
- **The builder's test:** `python3.14 -I -B test_tie_out.py --bench <bench>` was run in place and on a copy. Both gave `TESTS: PASS (346)`, exit 0, and no `__pycache__` on either bench.
- **Mutants:** 40 written (my_mutants.py, my_mutants_results.tsv). 38 caught, 2 survived (m35, m37).

## What I did NOT check

- Symlinks and dangling symlinks: there was no privilege to make them. `TARGET~1.CSV`: 8.3 names are off on this volume. Both rest on mode "x" untested by me.
- A real race between the exists check and open, which I did not drive.
- Workbooks saved by Excel: mine were made with openpyxl only. Shared strings, inline strings, error cells and cached formula values from Excel, beyond what openpyxl writes.
- Real data of any kind (not allowed).
- Job 04's spec in PARKED (not allowed). The goal's item 5 was judged against the launch's summary of it.
- r7's own cases: I do not hold them. I made the goal's named example (-0.5, `0%;"neg"`, -0.5%: OFF) and A2-style paths.
- Non-NTFS volumes, mapped network drives, and very long paths over 260 characters.
- test_tie_out.py read line by line: I read its head and main only, and judged it by running it and by mutants.
- Memory and time on a very large GL.
