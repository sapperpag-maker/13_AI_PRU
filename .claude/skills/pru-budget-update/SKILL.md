---
name: pru-budget-update
description: Use when Angie is asked to update, remake or refresh PRU's budget or the 2027 Sales Planner, when Sergio says "update the budget", "new class data" or "updated quantities", or when a new Class Data file, Manual Log, GL or Rick budget lands. Covers finding which source changed by program, the extract and diff, the GL sales utility, checking each changed figure at its source, the build, the planner check and landing. Invoke before the first source file is read.
---

# Angie remakes PRU's budget (an orchestrator)

Calls: `pru-sales-from-gl` at step 3 · `pru-planner-check` at step 6.

## STEP 0: the rules

| Call | Run right before | Meant to return |
|---|---|---|
| `rulebook.py get --who All --job All --moment "before replying"` | the first reply to Sergio | the office rules and their MISTAKE blocks |

The program: `"C:\AI_Building\AI_LEGISLATOR\Engine room\.venv\Scripts\python.exe" "C:\AI_Building\AI_LEGISLATOR\Engine room\Rules program\rulebook.py"`. Where it refuses the job, stop and tell Sergio.

## Limits

- Never open or print a customer row; read the Master sheet in columns B to E only.
- Write only in `C:\AI_Building\AI_PRU` and a bench in `C:\AI_Building\AI_MISC\06 Benches\`.
- Never accept the page, push, or put it live. Delete nothing.
- Not for a fix LAWYER failed: that is the WHO REPAIRS table in `C:\AI_Building\AI_HQ\CLAUDE.md`.

## Steps

1. Run `python3.14 "C:\AI_Building\AI_PRU\.claude\skills\pru-budget-update\pru_sources_check.py" --class-data <p> --manual-log <p> --gl <p> --rick-budget <p>` with each new file's path. `RESULT: SAME`: stop, nothing to do. `RESULT: STOP`: stop and ask Sergio. `RESULT: CHANGED`: go on.
2. Make `C:\AI_Building\AI_PRU\JOBS\NN PRU budget update - <date> <machine>\` and a bench `C:\AI_Building\AI_MISC\06 Benches\<date> PRU budget update - <tag>\`; copy the last build's programs to it. Run `extract_r3.py`, `extract_r4.py` and the old-against-new diff.
3. The GL changed: invoke `pru-sales-from-gl`; hand it the GL CSV and the Operating Statements file; it returns a CSV of sales by category and month, its md5, and the LDW (47700) and other training (46450) totals. Check that shape, then carry on at step 4. A missing or wrong output stops the job and goes to Sergio. Put LDW and other training into `build.py`'s gap parts and LDW rate, and recount the log's other gap parts (January, fees above the log, Oct-Dec). Never run Rick's `pru_nonlog_streams.py` for PRU: it counts them twice.
4. Check every changed figure at its file, sheet and row; a low figure is checked before anyone hears it. A rule or value the files do not give goes to Sergio through the question tool, one decision a question.
5. Run `build.py` on the bench; it writes the planner page and prints its md5.
6. Invoke `pru-planner-check`; hand it the page path and md5; it returns LAWYER's verdict path and first line. Check that shape, then carry on at step 7. A missing or wrong output stops the job and goes to Sergio.
7. On LAWYER's PASS: put the page in the job folder, write the LOG line, run step 1's command again with `--record`, commit by named paths and ask Piston to push. Ask Sergio to accept; the Brain puts it live; send Piston, for Rick, the figures file, its md5 and sources.

## The result

A planner page whose md5 is in `C:\AI_Building\AI_PRU\LOG.md` and `SOURCES.json`, with LAWYER's PASS on file, and Sergio asked to accept.

## Known traps

- Rick's non-log program on top of the planner counts LDW and the gap parts twice.

## Examples

- Good: Class Data changed; the diff shows 12 classes moved; each checked in Class Data; build, check, LAWYER.
- Bad: rebuild straight from the new file and send Sergio the page before LAWYER.

## Final check

Sources check run first? Every changed figure sourced? LDW and gap parts carried? LAWYER's PASS before `--record`? Nothing live before Sergio?
