# PLAN - job 14: his plan as the PRU planner's default (2026-11-24, Angie, HOME)

Goal: `GOAL.md` in this folder (DRAFT, waits on Sergio's yes).

1. **Base.** Build on job 13's r9 (6ded25cb) if LAWYER passes it, so the live page gets both changes. If LAWYER fails r9, build on the live r8 (926ab8a8).
2. **Read his plan out of his file** with a program on the bench `C:\AI_Building\AI_MISC\06 Benches\2026-11-24 PRU his final plan - ANGIE-HOME-W24\`. It reads each site's classes, fill %, students per class and price by month, the P&L lines he typed, and Dirt Bike. Where a value differs from the page's start, it becomes a saved edit, in the same shape the page already saves.
3. **Prove the plan read is complete.** Load that plan into the base page. Its Excel download must equal his file cell for cell (goal test 1). If any cell differs, fix the reading, never the page.
4. **Put his plan in the page as its default.** It goes in the page's plan-state block, which is already there and empty. Two lines change: Reset everything, and ONE VIEW's "nothing saved yet" answer, both go back to that plan instead of an empty one. No other code changes.
5. Run my own tests 1 to 4 and fix every fault they find.
6. A fresh blind checker, then LAWYER, then Sergio's yes, then the Brain puts it live.
7. The live page stays as it is until then.

Not in scope:
- The Save plan fault on ONE VIEW: sent to the Conductor for the Brain, 2026-11-24.
- The rewording of the save and fill lines: Sergio's question 9 is open. It goes in only on his word.
- Dirt Bike in the P&L: his question 6, "not for now".
