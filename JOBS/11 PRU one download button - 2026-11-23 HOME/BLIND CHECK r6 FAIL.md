FAIL

# PRU job 11 r6 (new shape), blind check of piece md5 3820f2bba43de8eaac014cd56c7cf585

Filed by Angie, the builder, from the checker's hand-back; its Write tool refused its own FINDINGS.md. Fresh checker, tag ANGIE-HOME-J11F. Bench: `C:\AI_Building\AI_MISC\06 Benches\2026-11-23 PRU job 11 r6 blind check - ANGIE-HOME-J11F\` (piece.html, base.html, harness.html, lib.js, scen.js). This is a finding, never an acceptance. First checker FAIL at the new-shape step.

md5 at start and end: piece 3820f2bba43de8eaac014cd56c7cf585 (155,489 bytes); base c2f6b7ce921e7318fc51c2ef0d9fa097 (152,630 bytes).

## Finding (MUST 4)
1. Typing a year box drops a month cell's unknown key when two months hold the same key with different values. setPl's year branch merges every month cell's extras into the year cell, and the first value wins. Real keyboard typing: pl.28 = {"m":{"3":{"t":"$","v":10,"foo":2},"5":{"t":"$","v":20,"foo":7}}}. Typing 500 in the year box gave {"y":{"foo":2,"t":"$","v":500}}, so foo=7 is gone from state, editsText(), the draft and every later save, and nothing lists it. Reproduced through loadEdits and setPl.

## Passed
- F1: fillUnit.ARC is listed as "Fill % of ARC" and moves no figure.
- F2: typing in line 24's year box and line 25's Apr and year boxes kept every unknown key in getState, editsText() and the draft, and they stayed listed. A year-to-months conversion copied the year note into all 12 months.
- 187 raw-JSON leaf paths, 12 of them __proto__: 56 listings cover every unknown path; 0 missing at load. After draft and plan edits, and after a frame load with P&L edits and a frame save, every path survived in state, editsText, draft, loadEdits round trip, reload and the frame save message, apart from keys typed over and the moved copies of converted lines, each of which was present.
- Clean states S0 to S3 (UI typing on all 4 tabs and the 3 hooks): 0 orphans.
- No figure moves: 7 scenarios by 26 views, 0 differences in figures, text and inputs. getState differs only by keys the piece keeps (5 paths in S4 and S5, 38 in S6) and by key order inside P&L lines; 0 keys only in the base, 0 differing values.
- Source diff (96 lines) only in the allowed parts.
- Proof the checks can fail: 3 of 3 planted differences caught; a live price edit gave 23 differing keys.

## Risks, not counted
R1 labels per map, merged when equal. R2 not exercised. R3 confirmed: a weekend edit throws when dirt wk is saved as a number (dirtArr). R4 new: an hdN holding only empty values is not listed. R5 new, also in the base: dirt spc, rent or coach saved as an array is listed as a shape the page does not read, but dirtIn() still reads it, and the Dirt Bike figures go null. O1 by design: clearing the only month cell, or a reset, removes the line with its line-level extras.

## Not checked
The window.claude publish save; Reset everything, per-unit resets, theme; xlsxBytes as a file; most UI edits other than F2 and finding 1 were set by value plus change event; loads validPlan refuses; other browsers.

## Checker's mistakes
First scenario script looked in the wrong places and used too short a wait; each stopped with "no input", was fixed and fully rerun. One harness reload kept an old script for one run, and the harness was reloaded fresh before the counted runs. Server b6yxl6ai3 stopped, draft key cleared, tab closed.
