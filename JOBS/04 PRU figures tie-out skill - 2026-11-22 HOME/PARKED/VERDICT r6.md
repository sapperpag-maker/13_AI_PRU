FAIL

# r6 blind check of the PRU figures tie-out program (shape 2, last round)

Checker: blind agent ANGIE-HOME-TC6. I invoked the skill office-review-adversarially before reading anything. OWN_FINDINGS.md was written before any claim was opened. I did not open the build bench, any "tie-out program check" bench, or LOG.md. I opened no real data file and did not start Excel.

Piece checked, md5 and size matched the launch:
- tie_out.py md5 db36cbd4, 27,372 bytes
- test_tie_out.py md5 32f9079b, 41,519 bytes

The builder's test: `python3.14 -I -B test_tie_out.py --bench <this bench>` gave exit 0 and `TESTS: PASS (285)`, and wrote no new __pycache__.

## Failing findings (1)

**F1. A text section (@) is read as the negative-number section, so a figure 100 times off can tie.**
- Where: tie_out.py `format_section_for`, lines 285-293. `check_format` (lines 271-282) does not refuse a format that holds @.
- Case t01 (extra.py, extra-out/EXTRA.txt): cell value -50, format `0%;@`, scale points, shown `-50%`.
- Expected: ERROR. The text-section rule says a section holding @ is the text section, it is the last section, and it applies to text only. Numbers, negatives included, then use section 1 (`0%`). So the cell shows -5000%, and "points needs a format without %" should refuse it.
- Got: TIED, "rounds to -50". The program picked section 2 (`@`), which has no %.
- Same result for t04 (`0.0%;@`, shown -50.0%) and t05 (`[Red]0%;@`, shown -50%).
- The right reading is refused instead. t02 (-0.5, fraction-to-pct, shown -50%) gives ERROR "fraction-to-pct needs a % format".
- The class: the program picks a section by its position and never asks whether that section is a text section. The fact that settles it is whether the section holds @: refuse such a format, or apply the text-section rule.
- Weight: I did not confirm in Excel what it displays for -50 in `0%;@`, because Excel was not allowed. I have not counted whether any real PRU workbook uses a format with @ outside a fourth section. Angie can count that from the real files as shapes only. Even if Excel does use the @ section for negatives, the program has still read a format it does not understand instead of refusing it. That breaks the rule "guesses nothing", which is why I mark this FAIL.
- The builder's test has no case with @ outside a fourth section (test_tie_out.py lines 322 and 345 only).

## Earlier findings retested with fresh cases (all hold)

**r5 F1, conditional formats:** all ERROR.
- c01 `[<1]0%;0` with value 5 shown 500%
- c02, c03 `[>=1]0;0%`
- c04 `[=0]`
- c76 `[>1]0;[<=1]0%`
- c77 `[ <1]0%`

**r5 test gaps:** all hold.
- Amount `$$5`: gb07 ERROR.
- Shown `$$900` and `$ 900`: s01, s02 and s39 ERROR.
- `[$%-409]` is not read as %: c11 points TIED, c12 fraction-to-pct ERROR.
- GL header with a trailing space or a tab: gb01 and gb02 ERROR.

**r5 minor findings:** all hold.
- Zero section: c16, c17, c18 and c19 are right.
- `%%`: c06 ERROR.
- Thousands-scaling commas: c07, c08, c09, c10, c78 and c79 ERROR.
- Dead account: g08 ERROR.
- Duplicate figures column: exits 2.

## Fresh attack: what passed

My harness has 85 cell cases, 42 shown cases, 5 Master cases, 36 GL rows on one GL, 40 single-row bad GL files, 17 exit and kind cases, and a leak scan. Results are in attack-out/real/SUMMARY.txt. Only one expectation missed, c65, which is minor note M1 below.

**Formats**
- Quotes and quoted `;`: c13, c14, c53, c62.
- Escapes: c15, c85.
- Fill and spacing characters: c50, c51, c52.
- Colours and locale brackets: c26, c59, c60, c80.
- Scientific format: c22 TIED, c23 OFF.
- Fraction format: c24 TIED, c25 OFF.
- `@` alone: c38. Four sections: c74.
- Accounting formats: c82, c83, t08, t09.

**Cell types and float edges**
- Text, boolean, date and empty cells: all ERROR.
- 15-digit cut: c46, c84.
- Half up: c29, c45, c48 TIED; c30, c45b, c49 OFF.
- Too large: c68 ERROR.
- Signs: c42, c43, c44, c57, c66b all OFF.

**Shown grammar**
- All 42 cases as specified.
- That includes U+2212, parentheses, NBSP, tab, full-width and Arabic-Indic digits, a zero-width space, `+`, `--`, `(-900)`, `$(900)`, `900K` and `.9k`.

**GL**
- Account x-patterns, length and literal X: g06, g21, g24.
- Store is exact: g10, g11.
- from and to are inclusive: g04, g05, g33.
- Journal filter: g07, g26, g27.
- side: g03, g03b and g32 are right; g19 ERROR.
- A repeated key, including one that differs only in case: ERROR (g12, g13).
- Unknown key and bad dates: ERROR.
- md5 and size are checked before the source is read: g28, g29, g30, and the md5-first note.
- Header variants: gb01, gb02, gb03, gb38, gb39 ERROR; gb04 with a BOM is TIED.
- A quoted newline (gb05), a 10-field line (gb06), an unterminated quote (gb34) and a NEL line (gb25): ERROR.
- A bare CR in an unquoted field: ERROR.
- Every amount-grammar break is ERROR (gb07-13, gb21, gb28-30, gb32, gb35, gb36, gb40), including a bad amount outside the date range (gb15).
- Bad dates are ERROR (gb16, gb17, gb33).

**Exit codes:** all as specified. That includes an --out naming the source in another spelling, two --out flags, a non-UTF-8 figures file and a duplicate id. An --out into a missing folder exits 2 with no RESULT line.

**Result line:** `RESULT: PASS`, and `RESULT: FAIL (1 of 2 rows not TIED)`, as specified.

**Leaks:** none. The scan covered every stdout, stderr and --out file of every run (real program and all mutants) for the GL description, doc, journal and account secrets I planted. It found 0.

## Mutants: 41 of 43 valid mutants caught (44 written)

The list is in MUTANTS.txt; the mutants are in mutants\.
- m22 broke the program's syntax (removing the body leaves an empty `if`). It is invalid and not counted.
- m30 (zero-line check off) was missed. It behaves the same as the real program: with zero lines matched, every listed account is dead, so the dead-account check still gives ERROR.
- m35 (gl % in shown allowed) was missed. It also behaves the same: the next check, % with as-is, still gives ERROR.

## Minor notes (not part of the verdict)

- **M1.** An unterminated quote or bracket in a format is not refused (format_scan, lines 232-264). Case c65, format `"0%` with value 0.5 as-is: TIED. Excel does not write such a format, and the value shown is not wrong.
- **M2.** GL account and store are compared after Python `str.strip()`, which also strips NBSP and other Unicode spaces (lines 463-465). Case gb23, account ` 46100`, was counted as 46100. The spec says exact.
- **M3.** The GL header check `rstrip(b"\r\n")` (line 450) accepts any run of CR and LF at the end of the header, for example `Store\r\r\n`.
- **M4.** A stale `__pycache__\tie_out.cpython-314.pyc` dated 2026-11-21 21:01 sits beside the programs. The test passes because it only checks that the file is unchanged.
- **M5.** The tie_out.py docstring lists the columns as `..., scale, md5, size`, while the spec says `..., md5, size, scale`. Columns are read by name, so this has no effect.
- **R1 (risk).** A comma after % or after a literal (`0%,` in t06, `0 ,` in t07) is not treated as thousands scaling: both came out OFF, not refused. Whether Excel scales these, I could not check.

## What I did NOT check

- What Excel actually displays for any format, F1 included. Excel was not allowed.
- Real PRU data, and how often real formats contain @.
- The r1-r4 findings one by one. I was not given them; my cases cover the same areas.
- Workbooks with shared formulas, external links, .xlsm files or very large sheets.
- Speed on a full-size GL.
- SKILL.md steps 1, 4 and 5. They are human steps.
- Concurrency, and files that change during a run.

## My mistakes

- I saved the builder's test output to test_run.txt with a shell redirect; the launch says to use the file tool only.
- I then tried to delete that file. The delete was refused, so test_run.txt is still on the bench.
