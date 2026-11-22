FAIL

# Blind check r3 of tie_out.py (job 06), ANGIE-HOME-GC3, 2026-11-22

Checked: GOAL.md 51bfc499, tie_out.py eb71e1a8, test_tie_out.py ff2b9326 (md5 read this session, matching the launch).
Skill office-review-adversarially was invoked first, before anything was read. Its STEP 0 rules call was run once, right after, as `rulebook.py get --who ANGIE --act review --what budget`.

## Findings: 1

### F1. A no-break space in a non-UTF-8 GL is not seen, and the line drops out of the sum, so a wrong figure shows TIED
- File and line: tie_out.py line 508, `raw.decode("utf-8", errors="replace")`, with the check at lines 116-118 and 533.
- Goal point: GOAL.md line 23. A used field that still starts or ends with other whitespace, no-break space named first, is "ERROR, never silently cleaned and never silently dropped".
- Cause: the program decides "is this whitespace" by reading the text after a lossy decode. In a Windows-1252 file a no-break space is the single byte A0. That byte is not valid UTF-8, so it becomes U+FFFD, which `isspace()` calls not whitespace. The field then fails the store or account match and the line leaves the sum with no word.
- The fact that settles it: whether the used field's bytes decode as UTF-8. A used field holding an undecodable byte (U+FFFD after the decode, or a strict decode failing) should be ERROR.
- Cases, all on a made-up GL with the real header shape. Good line: POW credit 100. Second line: credit 50 with the fault shown. Shown 100. Command: `python3.14 -I -B attack.py` (output in attack-output.txt). Expected ERROR each time.

| Case | Second line's fault | Exit | Status | Recomputed |
|---|---|---|---|---|
| c016 | store `POW` + byte A0 | 0 | TIED | 100 |
| c017 | account `46000-30` + byte A0 | 0 | TIED | 100 |
| c018 | byte A0 + store `POW` | 0 | TIED | 100 |
| c019 | journal `SJ` + byte A0, row filters journal=SJ | 0 | TIED | 100 |
| c020 | store `POW` + byte 85 (also not UTF-8) | 0 | TIED | 100 |

The true total of the two lines is 150. The same no-break space written in UTF-8 is caught (c004, c005: ERROR).
On today's real GL this does not occur: 0 of 874,157 lines hold invalid UTF-8, and 0 hold byte A0. It is a wrong status on a plausible file, a Windows export saved in its usual encoding.

## Minors: 1 (change no status on a file I could call plausible)
M1. tie_out.py line 516 and 531. The csv reader removes some stray quotes before the quote check sees them, so these fields hold no `"` and raise no ERROR. `"5"0` in credit reads 50 (c021). `"POW"X` in store reads POWX and is not POW (c022); the same line written POWX with no quote is also left out, so the quote is not what drops it. An unclosed `"POW` on the very last line with no line end reads POW and is counted (c023). No line was lost to a quote in these cases. The goal's wording, "still holds a quote after it is read", is met.

## Repairs asked to be checked first
- Stray quote: launch case (POW 100, then ` "POW"` credit 50, shown 100) gives ERROR (c001). Quote inside credit and account: ERROR (c002, c003). Unclosed quote mid file: ERROR (c025). Held.
- Other whitespace: NBSP, em space, FF, VT, NEL and US, written in UTF-8, before account and after store: ERROR, 12 of 12 (c004-c015). Not held for the non-UTF-8 byte form (F1).
- figures.csv: NBSP in shown, and in the sheet and cell parts of a reference: ERROR.

## Other points run
- Point 1 header: real shape ties; tab, swapped order, 10 names, quoted name and NBSP all ERROR (c058-c063).
- Point 2 plus sign: 15 shown forms against 100, all as the goal says (c029-c043).
- Point 3 zero: 14 cases on -0.30, +0.30, -499.99 and -500 (c044-c057). All correct. No note printed -0.
- Point 4: 18 cell cases, 0 wrong (15-digit cut half up, big int, text, boolean, $ with %, Master column guard). --out refused 8 spellings of an existing file (exact, upper case, trailing dot, trailing space, forward slashes, `::$DATA`, `:zz`, `\\?\`), figures file unchanged.
- Suite: `TESTS: PASS (890)`. That is not this verdict.

## Real GL (sums only)
File: `C:\AI_Building\AI_Financials\00 Raw data\GL\2026 YTD 101E GL History Detail Postings - All Accounts.csv`, md5 94ae1ff9841d3de6bc9903402e32874b, size 64,690,471, 874,157 physical lines. Store POW, accounts 46xxx-30 and 47700-30, credit minus debit. "Own sum" is my separate reader, not tie_out.py.

| Month | Shown | tie_out | Own sum | Lines | Status |
|---|---|---|---|---|---|
| Jan | 15,553 | 15,552.61 | 15,552.61 | 95 | TIED |
| Feb | 60,160 | 60,160.28 | 60,160.28 | 31 | TIED |
| Mar | 201,004 | 201,004.26 | 201,004.26 | 32 | TIED |
| Apr | 200,238 | 200,237.82 | 200,237.82 | 34 | TIED |
| May | 246,286 | 246,286.44 | 246,286.44 | 34 | TIED |
| Jun | 191,234 | 191,234.34 | 191,234.34 | 34 | TIED |
| Jul | 171,426 | 171,425.99 | 171,425.99 | 34 | TIED |
| Aug | 180,524 | 180,524.17 | 180,524.17 | 33 | TIED |
| Sep | 132,795 | 132,794.91 | 132,794.91 | 33 | TIED |

9 of 9 TIED. No GL line, description or single posting was printed.

## What I did not check
- The goal's `gl_check.csv` on the other bench (the launch barred other benches); I used the nine figures in the launch.
- The accepted job 05 build, so "nothing else changed" was tested by behaviour on point 4's list, not by a diff.
- --out into a missing folder or a read-only place; Windows device names as --out; a locked source file.
- The size column's handling of odd comma placement; very long numbers beyond the cases above.
- Every test inside test_tie_out.py was run but not read.
- Whether the real GL's exporter can ever write Windows-1252. Today's file has no such byte.

## My mistakes
- c045 expected TIED for shown `0.0` against -0.30. That was my error: -0.30 rounds to -0.3 at one decimal, so OFF is right. Not a finding.
- My first attack run stopped on a print encoding fault in my own script at case 25. I fixed the script and reran all cases into `attack-runs2`. The partial `attack-runs` folder stays on the bench, since I delete nothing.
- cells.py itself ran with `-B` only, because it imports openpyxl to make the test workbook. The tie_out.py runs it launched used `-I -B`.

Background shells: NONE STARTED.
