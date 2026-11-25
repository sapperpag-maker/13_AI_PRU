---
name: pru-planner-check
description: Use when pru-budget-update calls it at step 6, or when Angie is asked to "check the planner", "recheck the planner" or "send it to LAWYER" after a fix, or to "check my goal file" or "check the classes against the weekends". Covers checking the classes in Sergio's goal file against 2027's weekends, running the planner's own tests in the browser, proving they can fail on a planted copy, the blind Opus checker, and the LAWYER request through Piston. Invoke before the first test runs.
---

# Checking PRU's planner page (a utility)

Called by `pru-budget-update` at step 6.
Input: the planner page's path and md5, and Sergio's goal file (the planner's Excel download of his plan). Output: LAWYER's verdict path and its first line.

## STEP 0: the rules

| Call | Run right before | Meant to return |
|---|---|---|
| `rulebook.py get --who Angie --job "launching agents" --moment "before building"` | step 4 | the launch rules |

The program: `"C:\AI_Building\AI_LEGISLATOR\Engine room\.venv\Scripts\python.exe" "C:\AI_Building\AI_LEGISLATOR\Engine room\Rules program\rulebook.py"`. Where it refuses the job, stop and tell Sergio.

## Limits

- Never take own tests or the checker as the verdict; only Sergio accepts.
- Write only on the bench; the checker writes in its own bench folder.

## Steps

1. Run `python3.14 -I pru_goal_classes.py --goal <his goal xlsx> --classes <Sergio PRU Class Data xlsx>` from this skill's folder. It checks each Classes cell is whole, then each range's month against its busiest 2026 week times the month's 2027 weekends, holiday weekends out. Not `RESULT: PASS`: send Sergio the cells and months it names and stop; he decides the fix.
2. Serve the bench on 127.0.0.1 and open the page in the built-in browser; run the `rel3` test files (selftest, r13, r15, r16, r17, r19) through `window.__PRU_TEST__`. Any fail: hand back to the builder to fix and rebuild.
3. Run the same tests on a planted copy carrying the fault the newest test guards. The planted fault must fail; if it passes, the test cannot fail, so fix the test first.
4. Launch a blind Opus checker that did not build the page: the goal file and the page only; its launch names `pru-figures-tie-out`, which it invokes on the page; its findings and `TIEOUT.md` on disk before it reads any claim. A FAIL in either is a FAIL: repair and check again; two FAILs on a step move to the next (program, new shape, smaller, stop); the third goes to Piston.
5. Only when the checker's verdict and `TIEOUT.md` both read PASS, send Piston the LAWYER request: page path and md5, goal file, Sergio's words that bear on it, the checker's verdict, `TIEOUT.md`'s path and first line.
6. Wait for LAWYER's verdict; a FAIL goes back to the builder as one list.

## The result

LAWYER's verdict file path and its first line (PASS or FAIL).

## Known traps

- A test that passes on the planted copy proves nothing.
- `window.__selftest` is an object: read `.clean`, `.after` and `.pl`, don't call it.

## Examples

- Good: tests pass, planted copy fails 10, checker PASS on disk, then the LAWYER request.
- Bad: ask LAWYER while the checker's FAIL is still open.

## Final check

Goal classes PASS, or the STOP sent to Sergio? Tests passed on the page? Planted fault failed? Checker's findings on disk first? Tie-out run, first line PASS? LAWYER asked through Piston?

Hand back: give LAWYER's verdict path and first line to the orchestrator that called you and return to its step 7. Invoked alone: hand them to Sergio.
