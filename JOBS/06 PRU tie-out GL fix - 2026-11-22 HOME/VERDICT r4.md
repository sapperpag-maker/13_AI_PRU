FAIL

# Blind check r4 of tie_out.py against GOAL.md (job 06)

Checker: a job agent launched by Angie (ANGIE-HOME), machine HOME, 2026-11-22. I did not build this. This is a finding, never an acceptance: only Sergio accepts.

Done first: the skill `office-review-adversarially` was invoked, then `rulebook.py get --who ANGIE --act review --what budget` was run once. Its output was 153.1 KB; I searched it for the review, checker and verdict lines and did not read all of it.

Files checked, md5 matched before the work and again after it:
- GOAL.md d8b296195fc3cbd13aa4115a0c0a2002
- tie_out.py 6f8b9cccddf2ea12283de81cffcad136
- test_tie_out.py e5dea374875fccbf9daad59e13935372
- gl_check.csv f3941c4a5f90478d30008245ce741ac7

## Findings (2)

### F1. A GL line can leave a sum with no word, and the wrong figure comes out TIED
- **Where:** tie_out.py lines 539-545 (the only checks on a used field), 116-118 (`edge_space`), and the exact compares at 551, 553 and 572.
- **Goal point:** point 5 as made exact after r2 and r3 (GOAL.md lines 23, 28, 29). Line 29 gives the reason: a field that matches nothing makes "the line ... leave the sum without a word". The launch also names this as the first thing to attack.
- **Cause:** the program decides whether a line belongs to a sum by comparing account, store and journal exactly. It refuses only three kinds of bad field: a quote, whitespace at an end, and an invalid byte or U+FFFD. A valid UTF-8 character outside those three makes the field match nothing, so the line drops out and nothing is counted or reported.
- **The case:** a made-up GL of 3 lines of 100.00 (true sum 300.00), with the character planted in line 2, and shown `200`. TIED at 200.00 means the line left the sum and the wrong figure passed.
- **Count:** 93 of 117 planted cases came out TIED at 200.00: 31 each in account, journal and store.
  - 27 per column: U+200B, U+FEFF, U+00AD, U+2060, U+200C, U+200D, NUL, U+0001, U+007F, each at the start, middle and end.
  - 4 per column: U+00A0, U+2003, U+000B, U+3000 in the middle of the field. At the ends these four are ERROR, as the goal asks.
  - The journal cases apply only to a row with a `journal=` filter.
- **Surface reading:** the program decides "this field is clean" by listing bad shapes. Each repair so far (quote, end whitespace, invalid byte) has left the next shape open.
- **The fact that settles it:** what a used field is allowed to hold. On the real GL, all 6 used fields hold only printable ASCII (0x20 to 0x7E) in all 874,156 records, counted by my own reader on the raw bytes after trimming spaces and tabs: 0 lines with any other byte. A rule that a used field holding anything else is ERROR would refuse every shape above and change nothing on today's GL.
- **Fair weight:** no such character is in today's GL, so none of the 9 real figures is wrong. GOAL.md does not name these characters word for word, except that "and the like" on line 23 may reach U+200B and U+FEFF at an end. Whether the goal should say so is Angie's or Sergio's to decide. I file it as a finding because it puts a wrong figure at TIED.

### F2. A cell reference that is not a cell reference is read instead of refused
- **Where:** tie_out.py lines 338-339. `.upper()` runs before the pattern check.
- **Goal point:** point 4 (holds as the accepted build), and the program's own line 6: "every reading is stated in figures.csv or refused".
- **Cause:** Python's `.upper()` turns some non-ASCII letters into ASCII ones, so a bad reference becomes a valid one.
- **The case:** on a made-up workbook, detail `Sheet1!ſ1` (U+017F, long s) with shown `7` reads cell S1 and is TIED. Detail `Sheet1!ı1` (U+0131, dotless i) with shown `9` reads cell I1 and is TIED. Both should be ERROR "cell detail must be Sheet!A1".
- **The fact that settles it:** the reference as written must match `[A-Za-z]{1,3}[1-9][0-9]*` before any change of case.

## Minors (1), no status changes on any file I can call wrong

- **M1. A quote closed early is joined and used.** tie_out.py line 540 looks for a quote after the csv reader has removed it. Store `"101"E`, account `"40"00`, credit `"10"0.00` and date `"1/15"/2026` each read as the joined value and came out TIED at 300.00. GOAL.md line 24 covers a field that "still holds" a quote, and these do not, so the goal is met as written. I cannot say from anything written that the joined value is wrong. The real GL has 0 quote marks left in a used field and 0 open quotes. `csv.reader(..., strict=True)` would refuse this shape, if that is wanted.

## What I ran

| Check | Cases | As expected |
|---|---|---|
| A. Invalid byte or U+FFFD in a used field: 6 columns, 8 byte shapes, start, middle, end, inside quotes | 192 | 192 ERROR |
| B. The same bytes in an unused field (Doc #, Description, Balance) | 96 | 96 TIED at 300.00 |
| C. Valid invisible, control or inner-space characters in account, journal, store | 117 | 24; 93 leaks (F1) |
| D. Structure: line ends, blank lines, field counts, quotes, headers, BOM | 27 | 27 |
| E. Points 2 and 3: `+`, refused signs, shown zero, rounding edges, no "-0" note | 28 | 28 (see my mistake 1) |
| Second set: point 5 pads on every GL and figures.csv field, other whitespace, detail parts, cells | 91 | 89; 2 are F2 |
| Second set: early-closed quotes, observed only | 4 | M1 |
| **Total planted** | **555** | |

- `python3.14 -I -B test_tie_out.py --bench <bench>\t1` ended `TESTS: PASS (967)`. No `__pycache__` anywhere under the bench.
- `tie_out.py` on gl_check.csv with `--out real_out.csv`: 9 of 9 TIED, last line `RESULT: PASS`.
- Name scan, counts only, for sean|kim\b|richard|spagnini|angel|oneal, case-insensitive: tie_out.py 0, test_tie_out.py 0, GOAL.md 0.

## The 9 months, real GL

Source: `C:\AI_Building\AI_Financials\00 Raw data\GL\2026 YTD 101E GL History Detail Postings - All Accounts.csv`, 874,156 records, 0 of wrong width, 0 open quotes. My reader (`chk_real.py`) does not import tie_out and splits the raw bytes itself.

| Row | Shown | tie_out | My own sum | Lines (both) | Status |
|---|---|---|---|---|---|
| G01 | $15,553 | 15,552.61 | 15,552.61 | 95 | TIED |
| G02 | $60,160 | 60,160.28 | 60,160.28 | 31 | TIED |
| G03 | $201,004 | 201,004.26 | 201,004.26 | 32 | TIED |
| G04 | $200,238 | 200,237.82 | 200,237.82 | 34 | TIED |
| G05 | $246,286 | 246,286.44 | 246,286.44 | 34 | TIED |
| G06 | $191,234 | 191,234.34 | 191,234.34 | 34 | TIED |
| G07 | $171,426 | 171,425.99 | 171,425.99 | 34 | TIED |
| G08 | $180,524 | 180,524.17 | 180,524.17 | 33 | TIED |
| G09 | $132,795 | 132,794.91 | 132,794.91 | 33 | TIED |

All 9 agree to the cent. Differences between shown and sum, each under one dollar and from rounding to whole dollars: G01 -0.39, G02 +0.28, G03 +0.26, G04 -0.18, G05 +0.44, G06 +0.34, G07 -0.01, G08 +0.17, G09 -0.09. G07 is the only difference of one cent or less.

## What I did not check

- Point 4 against the job 05 build itself: I was told not to open it. I relied on the 967 tests and my own cases.
- test_tie_out.py was run and scanned, not read line by line, so I do not say each of its tests is sound.
- Whether the accounts, dates and sides in gl_check.csv are the right ones for the business, or whether the shown figures are the right ones to show. A tie proves the two agree, not that either is right.
- No real workbook was opened. Cell cases ran on one made-up workbook.
- Other non-ASCII letters that `.upper()` maps to ASCII (for example ß) were not run; I ran the two in F2.
- The whole of the rulebook output (see the top).

## My own mistakes

1. My E-set check marked `0.0` against -0.05 as BAD because it searched for the text "rounds to -0", which also matches the correct note "rounds to -0.1". The status (OFF) and the note are right. Not a finding; counted as expected in the table.
2. I first ran the test suite on a folder that did not exist yet. It exited 2 with its usage line. I made the folder and ran it again.
3. My name-scan control word "decimal" has 0 hits in GOAL.md, so it proves nothing for that file. I read GOAL.md whole and saw none of the names.

## Background shells

NONE STARTED
