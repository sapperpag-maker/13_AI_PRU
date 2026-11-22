FAIL

# Blind check r2, job 06 tie-out, build with point 5

Checked: `tie_out.py` 10ab6b96c49e8a13fc12dd1010047e33, `test_tie_out.py` c52f89ffbc0df1515b3226a5fdfb10fb, against `GOAL.md` d0fcbe036700720bb01b3764ca57207d.
Skill `office-review-adversarially` invoked first, before any file was read; the clock read 15:33:13 on the first command after it, 2026-11-22.
Suite: `python3.14 -I -B test_tie_out.py --bench <this bench>` ended `TESTS: PASS (516)`. That is not this verdict.
Cases: `attack.py` and `attack2.py` on this bench, made-up data in `attack\` and `attack2\`. Run with `python3.14 -B attack.py` and `python3.14 -I -B attack2.py`.

## Findings: 2

### 1. A padded field that opens with a quote drops its GL line, and the row says TIED
- File: `tie_out.py` lines 479 and 490-498 (line 517 for the journal).
- Class: the csv reader treats a quote as a quote only when it is the field's first character. With a space or tab before it, the quote marks stay in the value, and the trim leaves `"POW"`. That does not equal `POW`, so the line is left out with no count and no error.
- Goal point 5: spaces or a tab at either end of every field, and "all of them still tie".
- Case: GL lines `46000-30 ... credit 100.00, POW` and `46000-30 ... credit 50.00,  "POW"`. True total 150. Shown 100.
- Command: `python3.14 -B attack.py`, cases A1 to A5.

| Case | Padded field | Shown | Output |
|---|---|---|---|
| A1 | store, space then quoted | 100 | exit 0, TIED, recomputed 100.00, 1 GL line |
| A2 | store, tab then quoted | 100 | exit 0, TIED, recomputed 100.00, 1 GL line |
| A3 | account, space then quoted | 100 | exit 0, TIED, recomputed 100.00, 1 GL line |
| A4 | account, tab then quoted | 100 | exit 0, TIED, recomputed 100.00, 1 GL line |
| A5 | journal, space then quoted, journal filter | 100 | exit 0, TIED, recomputed 100.00, 1 GL line |

- Controls: the pad after the closing quote (A6) and inside the quotes (A7) both give 150, TIED. The same shape on the date (A8) or the amount (A9, A10) gives ERROR. Only the three matching keys fail silently.
- The fact that settles it: after the trim, does a key still hold a quote mark? Such a line needs reading as quoted, or ERROR. It must never be left out.

### 2. Account, store, journal, date and kind are trimmed of more than spaces and tabs
- File: `tie_out.py` lines 369, 491-493, 568 and 602.
- Class: after the goal's trim, a plain `.strip()` also removes every other whitespace character, such as NBSP, VT, FF, US (0x1F) and EM SPACE. Goal point 5 names spaces and tabs only, and line 95 sets `TRIM = " \t"`. Amounts and shown refuse the same characters, so one line is treated two ways.
- Case: GL lines `46000-30 ... 100.00, POW` and `46000-30 ... 50.00, POW<NBSP>`. Under the goal's trim, the second store is not `POW`, so the sum is 100.
- Command: `python3.14 -B attack.py`, section B.

| Case | Shown | Output |
|---|---|---|
| store `POW` + NBSP, VT, FF, US or EM SPACE (5 cases) | 100 | OFF, recomputed 150.00, 2 GL lines |
| account + NBSP, VT, FF, US or EM SPACE (5 cases) | 100 | OFF, recomputed 150.00, 2 GL lines |
| journal `GJ` + NBSP, journal filter | 100 | OFF, recomputed 150.00, 2 GL lines |
| date `1/5/2026` + NBSP | 150 | TIED, recomputed 150.00 |
| figures.csv kind `gl` + NBSP (F6) | 100 | TIED |
| credit `50.00` + NBSP (contrast) | 150 | ERROR, unreadable amount |

- I could not tell whether the accepted job 05 build already did this, because I did not open it. If it did, Angie or Sergio may rule on it under point 4. As written, point 5 names two characters and the program removes more.

## Minors: 2
1. Risk, no written rule to judge it by: `split_ref` (line 304) trims the sheet name before `!`. In a book with sheets `Sales` and `Sales `, the unquoted `Sales !A3` read `Sales` (7.78, shown 50%, OFF). The quoted `'Sales '!A3` read the right sheet (50.0, TIED). Excel needs quotes on a name with a space, so the unquoted spelling is not a valid reference.
2. The note column prints the rounded value with no commas (`rounds to 18233`). The recomputed column is right (18,233.00). No status or figure changes.

## Held, each run this session
- Point 1: the real header shape passes. Tab in a name, renamed, 10 names and swapped columns are all ERROR.
- Point 2: `+47`, `+$18,233`, `+8%` TIED; `+` on a negative OFF; `+-5`, `++5`, `5+`, `$+5`, `(+5)` ERROR.
- Point 3: `0`, `0.0`, `$0`, `0k`, `0%` tie small negatives; `0` against -0.50 is OFF (rounds to -1); no note printed -0.
- Point 4: `$` with % refused; 14.499999999999998 shows as 15; a -0 sum prints 0.00; 7 decimals ERROR; `--out` refused on an existing file by plain, upper case, trailing dot, trailing space, `::$DATA` and forward-slash spellings, file kept each time; a made-up marker in the GL text never reached the output in 3 error cases.
- Point 5, other shapes: all used fields padded ties (C7); padded `POW 2`, `P OW`, `46000 -30` and a February date stay out (C1-C4); blank date after trim ERROR; blank debit after trim counts as blank; text cells ` 5 ` and tab-5 ERROR; all figures.csv fields padded ties (F1); padded ids count as duplicates (F9).

## Real GL, sums only
File: `2026 YTD 101E GL History Detail Postings - All Accounts.csv`, md5 94ae1ff9841d3de6bc9903402e32874b, size 64,690,471, unchanged after the runs. Rows: store POW, accounts 46xxx-30 and 47700-30, credit minus debit. My own separate sum agrees with the program in all 9 months.

| 2026 | Shown | Recomputed | Lines | Status |
|---|---:|---:|---:|---|
| Jan | 15,553 | 15,552.61 | 95 | TIED |
| Feb | 60,160 | 60,160.28 | 31 | TIED |
| Mar | 201,004 | 201,004.26 | 32 | TIED |
| Apr | 200,238 | 200,237.82 | 34 | TIED |
| May | 246,286 | 246,286.44 | 34 | TIED |
| Jun | 191,234 | 191,234.34 | 34 | TIED |
| Jul | 171,426 | 171,425.99 | 34 | TIED |
| Aug | 180,524 | 180,524.17 | 33 | TIED |
| Sep | 132,795 | 132,794.91 | 33 | TIED |

Counted over the real GL's 874,156 records, in the 6 used fields of its 9-field records: 103,431 fields have a space or tab at an end; 0 open with a quote after padding; 0 have another whitespace character at an end. So neither finding changes a figure on today's GL. Both can on a later file.

## What I did not check
- The accepted job 05 build, so "nothing else changed" was tested by behaviour, not by a diff.
- The test file line by line; I ran it and read its tail only.
- Real workbooks; cell cases used one made-up workbook.
- Races on `--out` beyond what the suite covers; hard links and `\\localhost` spellings rest on the suite's own passing tests.
- The rules program's answer: my one allowed call was refused (see below), so no rules list was read.

## My mistakes
1. My one rules call passed `--job` beside `--act` and was REFUSED, serving no rule. I did not repeat it, because the launch allows one call.
2. My first `+$18,233` case wrote an unquoted comma in the GL amount and came back ERROR (malformed). That was my test's fault; redone quoted in `attack2.py`, TIED.

## Background shells
NONE STARTED
