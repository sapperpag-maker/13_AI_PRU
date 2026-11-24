FAIL

# PRU job 11 r7 (new shape, Piston's pick 04191917), blind check of piece md5 7cb32885522a6e345865f13507f872a4

Filed by Angie, the builder, from the checker's hand-back; its Write tool refused its own FINDINGS.md. Fresh checker, tag ANGIE-HOME-J11G, 2026-11-24. Bench: `C:\AI_Building\AI_MISC\06 Benches\2026-11-24 PRU job 11 r7 blind check - ANGIE-HOME-J11G\` (gen_plant.py, plant_state.json, plant_draft.json, helpers.js, frame.html, cmp.html). This is a finding, never an acceptance. Second checker FAIL at the new-shape step; the next step is "smaller" (MUST 4 whole lines only).

md5 at start and end: piece 7cb32885522a6e345865f13507f872a4 (156,115 bytes); base c2f6b7ce921e7318fc51c2ef0d9fa097; r6 3820f2bba43de8eaac014cd56c7cf585.

## Finding (MUST 4)
1. A month-named year key ending in " t" or " v" is lost when the year is split into months. piece line 316, plMaterialize's cell(): the key goes in as c[q.k], then c.t=t;c.v=v writes over it. Plant: pl.28 = {"y":{"t":"$","v":1200,"Apr t":5,"Apr v":6,"Jun t":{"k":1}}}; validPlan accepts it and orphans() lists all three. Real UI: Show the 12 months, typed 90 in line 28's Jan box, Tab. The values 5, 6 and {k:1} are gone from getState, editsText() and the draft, and orphans() is []. r6 keeps all three on the same draft, so this round brought the loss in. Reach: all 24 names "<Mon> t" and "<Mon> v", % years too.

## Passed
- The r6 plant: real typing 15000 in the year box gave y {"Apr foo":2,"Jun foo":7}, in state, editsText and draft, listed; back to months each foo returns to its own month as foo.
- Collisions across month pairs and month-named keys: all values kept, nothing overwritten. Year and month cells together on one line cannot be reached (validPlan refuses; setPl never leaves both).
- 187 raw-JSON leaf paths, 12 holding __proto__: 0 missing, 0 changed through draft load, editsText, draft after a real-keyboard edit, loadEdits round trip, reload, and the frame save message ([data-save] on plan, inits, budget).
- No figure moves: 7 scenarios x 26 views (25 page views plus plannerSheets with its stamp stripped), 0 differences against base, the orphan warning line left out (it differs by design).
- Source diff against r6: only the new comment, plHas, plMon, plFree, plMaterialize's cell(), and setPl's year-branch merge.
- Proof the checks can fail: a 1-cent plant caught in 5 views and plannerSheets; planted missing leaves caught; finding 1 itself.

## Reported, not counted
Clears: a year clear deletes the line with its line-level keys; a month clear removes that cell. Risks: (1) a plain year key that happens to be named like "May note" goes only to May, as note; no loss found apart from finding 1. (2) "P&L line 28 Apr foo" and "P&L line 28 year Apr foo" read almost the same. (3) norm passes every fillType/fillUnit value, read or not, through FILLV (rounded, 0-100): an unread fillType.zzT 0.5 became 1; base the same. R3, R4, R5 and validPlan's silent refusal did not come up.

## Not checked
The xlsx contents beyond plannerSheets; the line reset and Reset everything; the window.claude save path; the frame's stale, refused and ack answers; Dirt Bike shapes for R3 and R5, hdN for R4; many steps used the setPl hook rather than the keyboard.

## Checker's mistakes
A first keyboard attempt typed 15000 in line 33's % year box after a scroll; undone, later runs began from a fresh draft. First figure snapshots skipped closed details; caught and all 7 scenarios rerun. Server bps5y1928 stopped, draft key cleared, tab closed.
