# Job 14, plan steps 2 and 3: his plan read out of his file, and proved (2026-11-24, Angie, HOME)

Run on the live r8 as a throwaway base, on the Conductor's word. Own test, not a verdict.

Bench: `C:\AI_Building\AI_MISC\06 Benches\2026-11-24 PRU his final plan - ANGIE-HOME-W24\`
- `r8.html` md5 926ab8a84c26fd7c009e036aab63da28 (the live page)
- `data\his plan.xlsx` md5 78f1ffa44ed0bdd36e76a9926382cf08 (his file)
- `his.json` md5 0ccbbf1f967ce2650990e861824e35c9 (his file's 13 sheets as rows, by tojson.py)
- `his_state.json` md5 461080bfd922002b4cb3a66bcddf07c3, 1,919 bytes: his plan as the page's own saved state

## What his plan changes
Only classes and students per class. Price, fill %, the P&L lines, weekend rate, storage and Dirt Bike are as the page starts.
- Classes by month: 12 units (all nine 2-Wheel sites, Manassas Mall and Newport News 3-Wheel, ARC).
- Students per class by month: 13 units (nine 2-Wheel sites, Woodbridge, Virginia Beach and Clarksburg 3-Wheel, Woodbridge First Ride).

## The proof (goal test 1, on r8)
Loaded `his_state.json` into r8 with `setState`, then compared the page's download sheets with `his.json` cell by cell, all 13 sheets.
- 12 cells differ: row 2 of 12 sheets, the "Downloaded" time line. Nothing else.
- So the read is complete: P&L, Summary and every site sheet equal his file.

## Next
Step 4, the default build, waits on LAWYER's verdict of job 13's r9. The goal waits on Sergio's yes (question 10). Question 9 (rewording) is open.
