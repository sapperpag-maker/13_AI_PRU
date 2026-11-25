# Job 14 r10: Angie's own tests (2026-11-24, HOME). Not a verdict.

- Piece: `job14 f0f6a502.html`, md5 f0f6a502cb09187caa92c5dcb0e70310, 157,843 bytes, in this folder.
- Base: job 13's r9, md5 6ded25cb0d85d55d4e893bb14b824897 (LAWYER PASS 1701ac0c, accepted by Sergio's question 13).
- Built by `fix14.py` on the bench `C:\AI_Building\AI_MISC\06 Benches\2026-11-24 PRU his final plan - ANGIE-HOME-W24\`, with his plan from `his_state.json` (md5 461080bf, proved in `STEPS 2-3 PROOF.md`). The diff from r9 is 13 lines (6 out, 7 in).
- Goal: `GOAL.md`, accepted by Sergio's question 10.

## What changed
1. His plan is held in the code as `PLAN0`. A page whose embedded plan was never saved (no savedAt) opens on it. This differs from PLAN step 4, which put it in the plan-state block: ONE VIEW's own save writes plan-state over, so a plan kept there would be lost. Held in the code, it survives every save.
2. Reset everything goes back to his plan.
3. ONE VIEW's "nothing saved yet" answer opens his plan. The frame messages are unchanged.
4. The save line's words (question 9):
   - not saving at all: "Not saved. What you type is lost when this page closes or reloads. To keep it, press Download my edits."
   - a draft on this computer: "Kept on this computer only, not saved yet. Press Save plan to save it."
   - saved in this browser: "Saved on this computer only. Others do not see it."
5. The fill line's words (question 9): "Fill % is the share of seats filled. Leave a box empty to use the 2026 fill (March to November). A fill typed for one site beats its class type; a class type beats "all classes". Prices come from Class Data, 2027 Projections, M17 to M21."

## Tests, run at http://localhost:8814/r10.html, browser storage cleared first
1. PASS. Nothing saved: the page's download sheets equal his file (`his.json`, from md5 78f1ffa4) in all 13 sheets, after the job 13 name swap, with the Downloaded lines left out: 0 cells differ.
2. PASS. Typed a 2-Wheel price and a fill % (2,235 cells then differ), pressed Reset everything twice: 0 cells differ.
3. PASS. Saved a different draft (3-Wheel price 111, Stafford 2-Wheel classes 5 a month) and reloaded: the draft shows, not his plan; his other edits in the draft are kept.
4. PASS. SELFTEST worst gap 7.28e-12. The console shows no error.
5. WAITS on Sergio's yes to the words in 4 and 5 above.

## Not tested
- ONE VIEW's frame itself: its save service is not live (the Brain's r4 is at LAWYER). The "nothing saved yet" line is read from the code only.
- Microsoft Excel itself, light theme, phone width.
