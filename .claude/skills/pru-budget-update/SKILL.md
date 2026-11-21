---
name: pru-budget-update
description: Use when Angie is asked to update, remake or refresh PRU's budget or the 2027 Sales Planner, when Sergio says "new class data" or "updated quantities", or when a new Class Data file, Manual Log, GL or Rick budget lands. Covers testing the last build, finding which source changed, extracting by program, the GL sales utility, checking each changed figure at its source, the build, own tests with a planted fault, the blind check, LAWYER through Piston and landing. Invoke before the first source file is read.
---

# Angie remakes PRU's budget (an orchestrator)

Calls: the 2026-sales-from-the-GL utility (name to be agreed with Rick) at step 4.

## STEP 0: the rules

| Call | Run right before | Meant to return |
|---|---|---|
| `rulebook.py get --who All --job All --moment "before replying"` | the first reply to Sergio | the office rules and their MISTAKE blocks |
| `rulebook.py get --who Angie --job "launching agents" --moment "before building"` | step 8 | the launch rules |

The program: `"C:\AI_Building\AI_LEGISLATOR\Engine room\.venv\Scripts\python.exe" "C:\AI_Building\AI_LEGISLATOR\Engine room\Rules program\rulebook.py"`. Where it refuses the job, stop and tell Sergio.

## Limits

- Never open or print a customer row; read the Master sheet in columns B to E only.
- Write only in `C:\AI_Building\AI_PRU` and a bench in `C:\AI_Building\AI_MISC\06 Benches\`.
- Never take her own tests as the verdict, accept the page, push, or put it live.
- Delete nothing: superseded goes through `C:\AI_Building\AI_MISC\08 Archive\`.
- Not for a fix LAWYER failed: that is the WHO REPAIRS table in `C:\AI_Building\AI_HQ\CLAUDE.md`.

## Steps

1. Run the last build's tests (the `rel3` test files on the bench) on the last planner page. Any FAIL: stop and tell Sergio the build no longer makes the checked page.
2. Take each source's md5 by program and compare it with the last `C:\AI_Building\AI_PRU\LOG.md` line. None changed: stop, nothing to do. A new file name or shape: stop and ask Sergio.
3. Make `C:\AI_Building\AI_PRU\JOBS\NN PRU budget update - <date> <machine>\` and a bench `<date> PRU budget update - <tag>`. Run `extract_r3.py`, `count_classes.py` and the old-against-new diff.
4. The GL changed: invoke the GL utility; hand it the GL CSV path and the Operating Statements file; it returns sales by category and month, Jan-Sep tied to PRUAct row 13; check that shape, then carry on at step 5. A missing or wrong output stops the job and goes to Sergio. Carry its LDW (47700) and other training (46450) into `build.py`'s gap parts and the LDW rate, and recount the log's gap parts (January, fees above the log, Oct-Dec), so the revenue the log misses stays in; Rick's `pru_nonlog_streams.py` is never run for PRU, as it would count them twice.
5. Check every changed figure at its file, sheet and row: a low figure is checked before anyone hears it. A rule or value the files do not give goes to Sergio through the question tool, one decision a question.
6. Run `build.py` on the bench; it writes the planner page and prints its md5.
7. Run own tests on the page and on a planted copy: every test passes on the page and the planted fault fails, so the tests can fail.
8. Launch a blind Opus checker that did not build it; its findings on disk before it reads any claim. Repair a FAIL and check again. Then send Piston the LAWYER request: page path, md5, goal file.
9. On LAWYER's PASS: put the page in the job folder, write the LOG line, commit by named paths, and ask Piston to push. Ask Sergio to accept; the Brain puts it live; send Piston, for Rick, the figures file, its md5 and sources.

## The result

A planner page whose md5 is in LOG.md, with own tests passed, a checker verdict and LAWYER's PASS on file, and Sergio asked to accept.

## Known traps

- Math.round sends -2.5 to -2: round halves away from zero, with a float guard.
- A total is its own exact sum rounded, so it can differ by $1-2 from the shown rows; the page says so.
- A test that cannot fail on the old page proves nothing: plant the fault first.

## Examples

- Good: Class Data changed; diff shows 12 classes moved; each checked in Class Data; build, tests, checker, LAWYER.
- Bad: rebuild straight from the new file and send Sergio the page before LAWYER.

## Final check

Last tests passed? Every changed figure sourced? Planted fault failed? Checker and LAWYER on file? Nothing live before Sergio?
