PASS

# PRU job 11 r8 (one-line fix on r6, Sergio's question 1 of 2026-11-24), blind check of piece md5 926ab8a84c26fd7c009e036aab63da28

Filed by Angie, the builder, from the checker's hand-back (no findings file; its Write tool refuses report files). Fresh checker, tag ANGIE-HOME-J11I, 2026-11-24 10:48 to 10:56 EST. Bench: `C:\AI_Building\AI_MISC\06 Benches\2026-11-24 PRU job 11 r8 blind check - ANGIE-HOME-J11I\`; Angie read the md5s of piece, r6, base, plant.json, compare.html, frame.html and both xlsx outputs, equal to the hand-back, and `diff r6.html piece.html` (one changed line). This is a finding, never an acceptance; only Sergio accepts. Scope: Piston's word, MUST 4 covers whole saved lines and top-level keys only.

md5 at start and end: piece 926ab8a84c26fd7c009e036aab63da28 (155,589 bytes); r6 3820f2bba43de8eaac014cd56c7cf585; base c2f6b7ce921e7318fc51c2ef0d9fa097.

## Findings (counting)
NONE.

## Passed
1. Only piece line 125 differs from r6: FILLV only for keys in sets built from EXTRA.r3.types and EXTRA.r3.units (site|type), the same source as READS.fillType and READS.fillUnit; nothing mutates R3.
2. No early error: EXTRA (line 92) is defined before norm's first run (line 126); five load paths (no draft, embedded plan-state, draft, both, stand-in frame) with no console error; console capture proven with a planted error.
3. MUST 4: 26 unread keys (fill keys 12.5, 150, 101, 200, 0.5, constructor, __proto__, toString, hasOwnProperty, unitMonths, spc, price, rate, dirt, pl, top-level sections) listed and kept exactly through getState, editsText(), the draft after real typing, reload, loadEdits and the frame save message; read keys still rounded as in r6. The same harness on r6 shows the old rounding, so the test can fail.
4. No figure moves: 2,671 lines per snapshot, 0 differences with no edits and with edits that moved 1,007 lines; a planted 1-cent difference gave 14 differences.
5. Job 11 tests 1-4: valid zip, 13 tabs, 4,287 of 4,287 numbers equal plannerSheets(); Summary adds from the range tabs; P&L tab equals the page; piece's xlsx byte-identical to base's (c915e659); one centred button on 4 tabs, top and scrolled; 0 Load my edits.

## Reported, not counted
1. A non-map section (fillUnit:5) through embedded plan-state or setState is kept but not listed; draft, loadEdits and frame refuse it whole; not from this change. 2. A negative unread fill value makes validPlan refuse the whole plan, by design. 3. Bench page lacks charset/viewport meta; real phone width NOT CHECKED. 4. Keys inside a P&L cell out of scope.

## Not checked
Real Excel; a true phone viewport; the ONE VIEW server and real frame; job 10 tests 1-4 and 6, test_server.py; pru-figures-tie-out (excluded); two browsers and republish.

## Checker's mistakes
A first compare used P&L rows that do not exist (rerun on rows 16, 17, 24); a first Summary check read the wrong row (corrected); two rules-program asks refused for wrong arguments, so no review-specific rule list (UNRESOLVED). Shells b9aobdd1v and bqacxdw9a stopped by TaskStop; storage cleared; tab closed. Tokens 162,625 (app's report).
