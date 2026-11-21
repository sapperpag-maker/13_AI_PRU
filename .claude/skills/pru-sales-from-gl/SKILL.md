---
name: pru-sales-from-gl
description: Use when pru-budget-update calls it at step 3 because the GL changed, or when Angie is asked to "rebuild 2026 sales from the GL", get "PRU sales from the GL" or "tie PRU to the GL". Covers running the GL sales program and its test, sales by category and month tied to the Operating Statements PRUAct row 13, finding a missed account when it stops, and handing back LDW and other training. Invoke before the GL is read.
---

# PRU's 2026 sales from the GL (a utility)

Called by `pru-budget-update` at step 3.
Input: the GL CSV path, the Operating Statements file, the last closed month. Output: the sales CSV path, its md5, the LDW (47700) and other training (46450) totals.

## STEP 0: the rules

| Call | Run right before | Meant to return |
|---|---|---|
| `rulebook.py get --who All --job All --moment "before replying"` | the first reply to Sergio, unless already run this session | the office rules |

The program: `"C:\AI_Building\AI_LEGISLATOR\Engine room\.venv\Scripts\python.exe" "C:\AI_Building\AI_LEGISLATOR\Engine room\Rules program\rulebook.py"`. Where it refuses the job, stop and tell Sergio.

## Limits

- Never print or copy a GL line; read only Account, Journal, Date, Debit, Credit and Store, as sums.
- Write the CSV only on the bench; never over the GL or the statements.
- Write nothing about the job's state: the orchestrator does.

## Steps

1. Run `python3.14 "C:\AI_Building\AI_PRU\.claude\skills\pru-sales-from-gl\test_gl_sales_2026.py"`. Not `RESULT: PASS`: stop and tell Sergio the program no longer makes the checked figures.
2. Run `python3.14 "C:\AI_Building\AI_PRU\.claude\skills\pru-sales-from-gl\gl_sales_2026.py" --gl <csv> --opstmt <xlsx> --out <bench>\gl_sales_2026.csv --through <month>`. `RESULT: PASS`: go to step 4.
3. On `STOP`, read the month or account it names; find the missed account or the wrong store against the Operating Statements. A fact the files do not give goes to Sergio.
4. Take the CSV's md5 and read the LDW and Other training rows.

## The result

A CSV of sales by category and month, Jan to the last closed month, each month tied to PRUAct row 13; its md5; LDW and other training totals.

## Known traps

- The GL headers carry trailing spaces ("Account ").
- PRUAct repeats the months in a copy block and quarter columns; the program takes the first header row naming every month.

## Final check

Test passed first? `RESULT: PASS`? CSV on the bench with its md5? LDW and other training read from it?

Hand back: give the CSV path, its md5 and the LDW and other training totals to the orchestrator that called you and return to its step 3. Invoked alone: hand them to Sergio.
