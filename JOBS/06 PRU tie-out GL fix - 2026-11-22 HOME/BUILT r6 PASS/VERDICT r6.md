PASS

# Blind check r6: tie_out.py against GOAL.md (job 06)

Checker: job agent launched by Angie (ANGIE-HOME), machine HOME, 2026-11-22. I did not build this. This is a finding, not an acceptance: only Sergio accepts.

Done first: the skill `office-review-adversarially` was invoked, then the rules program was run once (`get --who ANGIE --act review --what budget`). Its output was 153.1 KB. I read its opening lines and a search of it for blind, checker, verdict, review and tie-out (first 60 hits), not all of it.

Files checked, md5 the same before and after:
- GOAL.md 5b89ef53cb8a73477220482ccac65db9
- tie_out.py 84431953232c4e37d0e345d943ad0fa1
- test_tie_out.py 1ab8b575900ed2a88513cacbb77385f6
- gl_check.csv f3941c4a5f90478d30008245ce741ac7

## Findings

0 findings.

## Minors (change no status)

- M1. tie_out.py lines 55-59, the header text, still describes the older rule (a quote or edge whitespace is ERROR). The code at lines 536-542 applies the wider Shape 1 rule, printable ASCII only. The code is right and the text is behind it.
- M2. tie_out.py lines 492-498, the read_gl text, names neither `strict=True` nor the inner-space refusal. Both are in the code (lines 520 and 546-550) and both worked in my cases.

## Risks (surface readings, separate from the verdict)

Neither one is beaten by the real GL. Both were beaten only on made-up files, by values the goal does not cover.

- R1. Store, account and journal match exactly (tie_out.py lines 553, 555, 574). A planted $1,000 line with store `pow`, account `46100-3O`, or, under a journal filter, journal `G J` or `gj` left the sum and the row showed TIED. The goal's inner-space rule names account and store only, so journal is outside it. The fact that settles it: the GL's distinct values. Over all 874,156 records, 0 groups of account (2,527 distinct), journal (31) or store (7) differ only by case or inner space.
- R2. The inner-space guard (lines 546-550) removes spaces from the GL value only. If a target itself holds a space (store `P OW`), a line spelled `PO W` leaves the sum and the row showed TIED. This meets the goal's words. The real GL has 0 store values with a space. 1,675 lines have an account with an inner space, and 0 lines equal a target of the 9 rows once spaces are removed.

## What I ran

1. `python3.14 -I -B test_tie_out.py --bench t_bench`: ended `TESTS: PASS (1271)`. 0 `__pycache__` folders on the bench.
2. `attack.py` run2, made-up files: 590 GL cases and 78 cell or shown rows, 668 in all. 667 came out as expected. The 1 other was my own case (see my mistakes); redone in `extra.py`, it gave ERROR as it should.
   - Used GL fields (account, journal, date, debit, credit, store): 24 kinds of byte or character at start, middle and end. They include NBSP in UTF-8 and in Windows-1252, VT, FF, FS to US, NUL, DEL, U+FFFD, em space, zero-width space, BOM, fullwidth digit, NEL, LS, stray bytes, quote, CR, inner tab and inner space.
   - Spaces and tabs at the ends of every used field, and quoted with spaces inside: still tie. Space after a closing quote and before an opening quote: ERROR.
   - Unused columns (Doc #, Description, Balance): the same bytes change nothing.
   - Line ends (LF, CRLF, CRCRLF, bare CR, none at the end), blank and blank-looking lines, quotes left open or swallowing the next line, 8 and 10 fields, BOMs, 9 kinds of wrong header, inner spaces, bad amounts and dates.
   - Shown grammar for points 2 and 3: 48 cases, including `+-`, `++`, misplaced `+`, zero forms of either sign. No note printed "-0".
   - Cell references: 6 legal spellings read; 24 false ones ERROR, including `A1$5`, `$$A15`, Kelvin sign, long s, dotless i, Arabic and fullwidth digits. The cells those would wrongly reach held the value that would have tied, so the check could fail.
3. `extra.py`: 3 inner-space guard cases gave ERROR; 2 target-with-a-space cases are R2; counts on the real GL.
4. tie_out.py on gl_check.csv, `--out real/result.csv`: `RESULT: PASS`, 9 of 9 TIED.
5. `own_sum.py`, my own byte-level reader (no csv module, no tie_out code), over the real GL: 874,156 physical lines, 874,156 records, 0 lines continued, 0 blank, 0 records without 9 fields, 0 used fields with a quote or a byte outside printable ASCII. So no real line is refused for the 9 rows. 360 target lines in all, all of them inside Jan-Sep.
6. Name scan of tie_out.py, test_tie_out.py and GOAL.md: 0, 0 and 0 matches. The same search with one word known to be in GOAL.md added found 7, so the search can hit.

## The 9 months

Source: `C:\AI_Building\AI_Financials\00 Raw data\GL\2026 YTD 101E GL History Detail Postings - All Accounts.csv`, accounts 46xxx-30 and 47700-30, store POW, credit minus debit.

| Row | Month | Shown | tie_out | My own sum | Lines | Status |
|---|---|---:|---:|---:|---:|---|
| G01 | Jan | $15,553 | 15,552.61 | 15,552.61 | 95 | TIED |
| G02 | Feb | $60,160 | 60,160.28 | 60,160.28 | 31 | TIED |
| G03 | Mar | $201,004 | 201,004.26 | 201,004.26 | 32 | TIED |
| G04 | Apr | $200,238 | 200,237.82 | 200,237.82 | 34 | TIED |
| G05 | May | $246,286 | 246,286.44 | 246,286.44 | 34 | TIED |
| G06 | Jun | $191,234 | 191,234.34 | 191,234.34 | 34 | TIED |
| G07 | Jul | $171,426 | 171,425.99 | 171,425.99 | 34 | TIED |
| G08 | Aug | $180,524 | 180,524.17 | 180,524.17 | 33 | TIED |
| G09 | Sep | $132,795 | 132,794.91 | 132,794.91 | 33 | TIED |

Differences that round to one cent or less (R-1874): between tie_out and my own sum, none; all 9 are equal to the cent. Between shown and the sum, each is under 50 cents because shown is in whole dollars: -39, +28, +26, -18, +44, +34, -1, +17 and -9 cents.

## What I did not check

- Whether the 9 shown figures are the right figures for the business. I checked only that they tie to the GL.
- Whether the GL itself is right.
- The accepted job 05 behaviour in point 4 beyond this program's own 1,271 tests and the cases above. I did not compare with the job 05 build, which I was told not to open.
- figures.csv read with odd quoting: it is not read with `strict=True`, and the goal asks that of the GL only. I planted no case there.
- Workbooks other than my made-up one. No workbook of the business was opened.
- The rest of the rules program's 153.1 KB output, beyond what is stated at the top.

## My own mistakes

1. attack.py run1 used a target with `47700-30` and no such line in the made-up GL, so every row came back ERROR and the run proved nothing. I fixed the case and reran it as run2; run1 is not counted.
2. In run2, the case "inner space both" used account `47700 -30`, no longer a target, so TIED was the right answer. Redone in extra.py with `46100 -30`: ERROR.

## Background shells

NONE STARTED
