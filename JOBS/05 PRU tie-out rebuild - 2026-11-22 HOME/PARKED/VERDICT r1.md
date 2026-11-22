FAIL

# Blind check, job 05: tie_out.py (md5 43e650f7, 25,124 B) and test_tie_out.py (md5 1e591600, 46,141 B)

Checker: a fresh agent launched by Angie (ANGIE-HOME). It did not build the piece. The skill office-review-adversarially was invoked before anything was read. Rules asked: `rulebook.py get --who helper --moment "before checking" --act review --what All` and `--who angie --job All --moment "before building"`. Yardstick: C:\AI_Building\AI_PRU\JOBS\05 PRU tie-out rebuild - 2026-11-22 HOME\GOAL.md, read whole, plus the spec list in the launch. OWN_FINDINGS.md was written before the test file was read and before any claim was opened. PROGRESS.md, mutants.py, mutants\ and suite\ of the builder, LOG.md, the trash and job 04 PARKED were not opened.

## Failing findings: 2

### F1. --out to a new stream of an existing file is accepted, and that file is changed
- Case: `--out <existing file>:zz` (also `:yy:$DATA`). Tried on a made-up victim.csv, on the figures file itself, on the source workbook and on a folder.
- Expected (GOAL.md item 4): "any existing file, whatever path spelling or link reaches it, exits 2 and stays unchanged".
- Got: exit 0. The result CSV is written into a new alternate data stream on the existing file. The file's mtime changes; its main content (md5, size) does not. On the source workbook the md5 stays the same, so the same figures still TIE after the write. Only a second run to the same stream exits 2.
- Where: tie_out.py line 635, `os.path.lexists(out_path)`, which asks only whether the stream exists, and line 648, `open(out_path, "x")`, which creates the stream on the existing file.
- Class: it decides "nothing is there" from the whole path string. What would settle it: check whether the file the path lands on exists (the part before any `:stream` suffix), or refuse any `:` after the drive.
- Evidence: probe.py, sections (b), (b2), (b3), (b4). Also attack.py's two lines "--out ... ADS new stream": rc=0, md5 same, mtime changed.

### F2. A wrong figure comes out TIED, and the right one OFF, once a value passes 28 digits
- Case: one matched GL line, Credit Amount `1234567890123456789012345499.6`, side credit-debit. Shown `1,234,567,890,123,456,789,012,346k` -> TIED. The true half-up value is ...345k (1234567890123456789012345.4996k), and shown `...345k` -> OFF.
- Expected: no wrong figure TIED.
- Got: as above (probe.py section (c), rc 1).
- Where: tie_out.py line 425, `sp["sum"] += amt`, runs in Decimal's default context (28 significant digits, half-even), which rounds without telling anyone. Line 117 then rounds half up again: a double rounding. The amount grammar (lines 79-81, 133-151) has no limit on digits. The same class reaches integer cells with more than 28 digits through line 117 (the division) and line 274 (`v * HUNDRED`).
- What would settle it: an exact context (trap Inexact/Rounded and give ERROR), or a digit cap that is refused as ERROR.
- Weight: made-up input. No real GL here carries an amount near 10^27. It still meets the launch's FAIL condition ("a wrong figure could tie") on an input the strict grammar accepts.

## Minor notes (none of them decides the verdict)
- N1. Date and time number formats still change a result. Stored 45000 gives ERROR with `yyyy-mm-dd`, `m/d/yyyy`, `h:mm`, `[h]:mm` or `mm:ss`, and TIED with General, `0 "d"` or `#,##0 "days"`. The format is read by openpyxl, not by tie_out.py. GOAL item 1 asks for both "never reads a number format" and "date cells are ERROR", and both cannot hold literally. The result always errs on the safe side (ERROR, never a wrong TIED). This clash is the Owner's to settle.
- N2. A shown or label that holds a newline splits the printed table row. The status is still ERROR.
- N3. The builder's suite (295 checks) misses 3 of my non-equivalent mutants:
  - m10: open mode "w", so a file made mid-run is overwritten (no race test);
  - m12: GL header compared without case;
  - m30: GL header text echoed in an error (no header-leak test).
  It has no ADS case either.
- N4. Unknown extra columns in figures.csv (for example a `format` or `multiplier` column) are accepted with no warning.
- N5. `--out NUL` exits 2.

## What passed
attack.py ran 387 of my own cases against the original. 5 came back BAD: 2 are F1, and 3 were mistakes in my harness, re-checked by hand (listed in OWN_FINDINGS.md). They cover:
- **The % rule:** fractions, whole numbers, negatives, 0 and -0, tiny values against 0% and -0%, half up at the half (+ and -), 15-digit cuts (0.145 -> 15%, 0.285 -> 29%, 1.005 -> 101%, -0.145 -> -15%), many decimals, k and M with % refused, k and M rounding.
- **Formats:** the same results across 9 number formats, including `0%;"neg"`, `@` and `"x"0`. The goal's own example (-0.5, `0%;"neg"`, shown -0.5%) comes out OFF.
- **Cell types:** text, a number stored as text, TRUE, FALSE, a formula with no cached value, #DIV/0!, #N/A, #REF!, empty, date, datetime and time all give ERROR, with exit 1.
- **Shown grammar:** 44 bad forms refused, 14 good forms read right.
- **md5, size, kind and NO SOURCE rows.**
- **Scale column:** refused in 4 spellings (exit 2, no table).
- **Exit codes:** 0, 1 and 2 checked.
- **GL:**
  - 23 detail cases: x patterns, a dead account, store exact, journal, dates inclusive or unreadable, side, %, unknown and repeated keys;
  - 22 amount forms and 7 date forms;
  - 6 header forms, plus BOM and LF line ends;
  - 6 record shapes;
  - an empty GL, blank lines, non-UTF-8 text, a quoted thousands amount.
- **Leaks:** a customer marker placed in Description, Doc #, a broken quoted field and the GL header never reached stdout, stderr or --out.
- **--out:** every one of these ended exit 2 with the victim's md5 and mtime unchanged:
  - spellings: plain, upper case, forward slashes, trailing dots, a trailing space, a trailing space and dot, `\\?\`, `\\.\`, `\\?\UNC\localhost\C$`, `\\localhost\C$`, `\\127.0.0.1\C$`, relative, `..`, `::$DATA`, the 8.3 short name;
  - links and folders: a hard link, a path through a junction, the junction itself, a folder, a missing folder, the figures file, the source workbook;
  - a file made mid-run (race).
  - A new path writes the file and ends RESULT: PASS.
- **The goal's own test:** the builder's suite run on my bench gives `TESTS: PASS (295)`, with no `__pycache__` beside either program or on my bench.

## Mutants
I wrote 34 mutants of my own (my_mutants\, made by mk_mutants.py). m31 (abs compare) is equivalent, because sign_agrees still guards it.
- The builder's suite caught 30 of 34. It missed m10, m12, m30 and m31.
- My attack.py caught 31 of 34. It missed m11 (lexists removed; open "x" still refuses, so it is equivalent for my checks), m17 (store compared without case: a gap in my cases) and m31.
- Together they caught 33 of 34. The one left is m31, the equivalent.

## What I did NOT check
- Symlinks: not allowed on this machine (OSError), so the symlink and dangling-symlink --out cases did not run.
- A real Excel-saved workbook (Excel was not started) and any real GL or workbook (not opened, by the launch).
- r7's own case list: r7's verdict was not opened. I only covered the cases the goal names (the -0.5 `0%;"neg"` example, `\\?\`, `\\localhost\C$`, hard link).
- The Master sheet column rule, beyond reading it.
- The middle of test_tie_out.py (lines 331-699), line by line. It was run, and its mutant kills were measured.
- The md5-check-to-read window in time (a change to the GL between check_source and read_gl).
- Very large files and performance.
