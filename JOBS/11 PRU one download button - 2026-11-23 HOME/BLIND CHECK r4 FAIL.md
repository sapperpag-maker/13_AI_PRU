FAIL

# PRU job 11 r4, blind check of piece md5 16db28895c5e4b9b3c422f0d16655898

Filed by Angie, the builder. The checker's Write tool refused its own FINDINGS.md, so this is the checker's hand-back, cut down to its findings and evidence. Checker tag ANGIE-HOME-J11D. Bench: `C:\AI_Building\AI_MISC\06 Benches\2026-11-23 PRU job 11 r4 blind check - ANGIE-HOME-J11D\`. This is a finding, never an acceptance. First checker FAIL on this repair.

md5 of the piece, start and end: 16db28895c5e4b9b3c422f0d16655898 (153,196 bytes). Base page: c2f6b7ce921e7318fc51c2ef0d9fa097 (152,630 bytes).

## Findings, goal point 1 (MUST 4)
1. A top-level `__proto__` key in the saved state is dropped at load and never listed (draft S5). Cause: norm() copies the state with Object.assign({},DEF,s), and Object.assign runs the `__proto__` setter instead of copying the key.
2. A `__proto__` key in fillType is dropped and not listed. Cause: norm(), s[k]=Object.assign({},s[k]).
3. A `__proto__` key in fillUnit is dropped and not listed. Same cause as finding 2. Findings 1 to 3 also hold on the base page. By reading the code, the checker says loadEdits() has the same Object.assign copy; it did not run it.
4. Extra keys inside a P&L line (pl.16.z, pl.41.m.0.note, pl.72.y.q) are kept but not listed (draft S6). This counts only under the goal's literal wording, "every saved edit whose key path the page does not read".

## Passed
- Draft S4 listed all 36 orphan entries: unknown sections; Dirt Bike fields, month lists and wrong shapes; constructor, toString, hasOwnProperty and `__proto__` in price, rate, unit, P&L and Dirt Bike; unknown unit, type and site keys. The base page lists 19.
- Nothing is listed for a clean state, for the drafts holding only the page's own edits, for 139 real UI edits, or for setClassCell and setSpcCell on all 21 keys.
- Never dropped after an edit: all 53 planted paths survive in editsText() and the saved draft; after a reload the 36 orphans are still listed.
- Goal point 2, no figure moves: no finding. The source diff is only orphans() and the server save-error text. In 9 of 9 drafts, the budget, plan, Dirt Bike, download sheets, saved state, all 4 tabs' text and every input are equal; only the orphan warning differs.
- Proof the checks can fail: a planted 2-Wheel price of 390 was flagged in 5 outputs.

## Not checked
xlsxBytes() bytes; the live server and frame; loadEdits() run from a file; drafts that validPlan refuses whole.

## Checker's mistakes
Bench copies made with Bash cp; refused rules-program asks before one was served; its first comparison included script text, so it fixed that and reran all 18 loads; its FINDINGS.md write was refused. Server blmbwkz75 stopped, tab closed.
