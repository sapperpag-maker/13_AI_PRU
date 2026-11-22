# Job 06 goal: the tie-out program reads the real GL, takes a leading +, and lets 0 tie either sign

Angie, 2026-11-22. Sergio's Q68: "Fix it, recheck, LAWYER (Recommended)". Q69: "Yes, 0 ties either sign (Recommended)".
Starting point: the accepted job 05 build, `C:\AI_Building\AI_PRU\.claude\skills\pru-figures-tie-out\tie_out.py` a8f90d60, `test_tie_out.py` c9e6562a.

## What the finished piece shows
1. The GL header check takes the real GL's header: the same 9 column names in the same order, each compared after trimming spaces at its ends. The real file's names are `Account `, `Journal ` and `Store `, each ending in a space. Any other header is still ERROR.
2. A shown value may start with `+`, which means positive, as in `+8%`, `+$18,233` and `+47`. `+` on a figure whose value is negative means the signs differ, as `-` on a positive one does now. `+-`, `++` and a `+` anywhere else are refused.
3. A shown zero (`0`, `0.0`, `0%`, `$0`, `0k`) ties any value that rounds to zero at the shown precision, positive or negative. No note prints "-0".
4. Everything else holds as in the accepted job 05 build and its GOAL addendum (Q64 and LAWYER's 75).

## The test that says it shows it
- `python3.14 -I -B test_tie_out.py --bench <folder>` ends `TESTS: PASS (n)` and writes no `__pycache__`. New tests cover points 1 to 3, with a made-up GL whose header copies the real one's shape, trailing spaces included.
- On the real GL, sums only: the 9 monthly 2026 Jan-Sep gl figures in `C:\AI_Building\AI_MISC\06 Benches\2026-11-22 PRU tie-out hand run real - ANGIE-HOME-HR1\gl_check.csv` come out TIED. No GL line is printed.
- A blind Opus checker that did not build it writes PASS. LAWYER passes it through Piston. Sergio accepts.

## Point 5, added 2026-11-22 on Sergio's Q70: "In the program, on read (Recommended)"
His words: "just run a trim function on every raw file".
5. The program trims spaces and tabs at both ends of every field it reads from a raw file, and of every field of figures.csv. In the GL that means every field it uses: account, journal, date, debit, credit and store. A value that is blank after trimming counts as blank. The raw files themselves are never changed, and their md5 and size are checked as they are on disk. A cell's stored number is read as before; a text cell is still ERROR after trimming.
Test: new tests in which every such field has spaces or a tab at one or both ends, and all of them still tie. Job 06's check r1 (PASS, on the build before point 5) is kept as `VERDICT r1.md`; the build with point 5 gets a fresh blind check.

## Point 5, made exact after check r2 (Angie's decision, for Sergio to see)
- Only spaces and tabs are trimmed. A used field (GL account, journal, date, debit, credit, store; any figures.csv field) that still starts or ends with any other whitespace after the trim (no-break space, form feed, em space and the like) is ERROR, never silently cleaned and never silently dropped.
- A used GL field that still holds a `"` after it is read and trimmed is ERROR, so a line can never fall out of a sum because of a stray quote.
Why ERROR: a line that is cleaned or dropped without a word can change a sum. On today's GL neither case occurs (check r2's count over 874,156 records: 0).

## Point 5, made exact after check r3 (Angie's decision, for Sergio to see)
- A used GL field (account, journal, date, debit, credit, store) that holds, at any place, a byte that is not valid UTF-8, or the replacement character U+FFFD, is ERROR, naming the column and never the content. The same byte in a GL field the program does not use changes nothing.
Why ERROR: such a byte (a no-break space saved in Windows-1252 is one) would otherwise make the field match nothing, and the line would leave the sum without a word.

## Shape 1, Piston's pick under R-1878 after check r4's FAIL, Sergio's to strike
File: `C:\AI_Building\AI_HQ\03 Library\PISTON PICK - Angie job 06 tie-out GL fix third blind-check FAIL - 2026-11-22 HOME.md`.
- A used GL field (account, journal, date, debit, credit, store), after spaces and tabs are trimmed at its ends, may hold only printable ASCII (0x20 to 0x7E). Anything else is ERROR, naming the column and never the content. This takes in the two "made exact" whitespace and byte rules above.
- A cell reference must match `[A-Za-z]{1,3}[1-9][0-9]*` before any change of case.
- The GL is read with the csv reader's `strict=True`, so a quote closed early or left open is ERROR, in any column. A space after a closing quote (`"POW" `) is such a case: it is ERROR, not trimmed (Angie's reading of the pick, flagged).
Condition: on the real GL, all 874,156 records, the 9 months still tie with no new ERROR. If `strict=True` refuses a real line, the job stops and goes back to Piston.

## Shape 1, second and last round, Piston's addendum of 16:17 to the same pick file, Sergio's to strike
- The cell reference is matched as written against `\$?[A-Za-z]{1,3}\$?[1-9][0-9]*`, so `A1$5`, `$$A15` and the like are ERROR, and the 4 legal spellings (`A15`, `$A$15`, `$A15`, `A$15`) still read.
- An account or store with a space inside that would equal a target of a gl row once its spaces are removed is ERROR.
- A Debit or Credit the program refuses stays a loud ERROR.
Condition: on the real GL, the 9 months still tie with no new ERROR.
