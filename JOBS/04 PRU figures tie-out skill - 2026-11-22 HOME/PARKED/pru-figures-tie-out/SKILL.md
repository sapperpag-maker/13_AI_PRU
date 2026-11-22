---
name: pru-figures-tie-out
description: Use when the blind checker launched by pru-planner-check reaches its step 3, before the LAWYER request, or when Angie is asked to "verify the numbers", "check the balances", "tie it to the GL", "tie out the report" or "reconcile with the source files" on a PRU report. Covers listing every figure a report shows, naming each one's source file or GL accounts, recomputing every figure and total by one program, tying each GL-based line to its accounts, and reading each figure for anything misleading. Called by pru-planner-check's checker. Invoke before the first figure is checked.
---

# PRU's figures tie-out (a utility)

Called by the blind checker of `pru-planner-check` at its step 3.
Input: the report's path and md5. Output: `TIEOUT.md`'s path and its first line, PASS or FAIL.

## STEP 0: the rules

| Call | Run right before | Meant to return |
|---|---|---|
| `rulebook.py get --who ANGIE --act review --what budget` | step 1 | the review rules and their MISTAKE blocks |

The program: `"C:\AI_Building\AI_LEGISLATOR\Engine room\.venv\Scripts\python.exe" "C:\AI_Building\AI_LEGISLATOR\Engine room\Rules program\rulebook.py"`. Where it refuses the job, stop and tell Sergio.

## Limits

- Never print a GL line or a customer row; read the GL's Account, Journal, Date, Debit, Credit and Store only, as sums; read the Master sheet in columns B to E only.
- Never edit the report or a source file; write only on the checker's bench in `C:\AI_Building\AI_MISC\06 Benches\`.
- Never accept the report. Not for the planner's own tests: those are `pru-planner-check` steps 1 and 2.

## Steps

1. List every figure the report shows, none skipped: each number, total, rate and count, with its label, value as shown, period and unit, one row each in `figures.csv` on the bench.
2. Name each figure's source and scale (as-is, fraction-to-pct, points) in `figures.csv`: a file from `C:\AI_Building\AI_PRU\JOBS\03 PRU source map - 2026-11-21 HOME\SOURCE MAP.md` with its sheet and cell, or GL accounts with store POW, dates and side; a total gets its own cell or GL accounts, never its parts. A figure with no source is marked NO SOURCE, never guessed.
3. Run `python3.14 -I "C:\AI_Building\AI_PRU\.claude\skills\pru-figures-tie-out\test_tie_out.py" --bench <bench>`, then `python3.14 -I "C:\AI_Building\AI_PRU\.claude\skills\pru-figures-tie-out\tie_out.py" <bench>\figures.csv`. It checks each source's md5 and size, recomputes every figure from its cell or its GL accounts (cell and gl rows only). Each OFF, NO SOURCE or ERROR line is a finding, with its difference.
4. Read each figure for anything misleading: the period stated and right, the sign, the unit and $, the label matching what was summed, a part left out of a total without saying so, a plan shown as an actual. Check a low or odd figure again at its source before it is written.
5. Write `TIEOUT.md` on the bench: first line PASS or FAIL, one row per figure (shown, source, recomputed, difference), the GL account table, the misleading findings. FAIL when any finding stands.

## The result

`TIEOUT.md` on the bench, first line PASS or FAIL, beside `figures.csv` and the program's output.

## Known traps

- A figure tied to the report's own other figures proves nothing: tie it to a source file or the GL.
- GL income is credit minus debit; a sign flipped on one line hides inside a right total.

## Examples

- Good: 41 figures listed; Training tied to GL 46xxx-30 and 47700-30, store POW, Jan-Sep; one total off by 1,137, reported with both sums.
- Bad: the totals add up, so every figure is passed without its source being opened.
## Final check

Every figure listed? Every one with a source or NO SOURCE? Program run after its test? Misleading read done? First line PASS or FAIL?

Hand back: give `TIEOUT.md`'s path and first line to the checker that called you and return to `pru-planner-check` step 3. Invoked alone: hand Sergio the path and first line.
