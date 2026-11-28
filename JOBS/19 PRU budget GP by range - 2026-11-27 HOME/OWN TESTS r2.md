# Job 19: Angie's own tests, round 2 (not a verdict)

Page: C:\AI_Building\AI_MISC\06 Benches\2026-11-27 PRU budget GP by range - ANGIE-HOME-J19\page_after.html, md5 3b69e1ed47e36f586715d9801fc86523, 153,910 bytes, built by j19_build.py from the accepted page cb1532735ede13ca7ff66ac007aa9015. Served by pru-job19-gp (port 8819), browser storage cleared.

Changed since round 1 (582fa2cc), for blind checker r1's FAIL (CHECKER r1\FINDINGS.md):
- F1: the Prices tab groups units by range, 2-Wheel and 3-Wheel only; BRC2, First Ride, ARC and HD units go in an "ARC, BRC2, IME and Other" group.
- F2: a saved P&L edit is dropped when a plan loads (his 78).
- F3, F4: the stale notes are rewritten; no "2027 plan" wording is left on the page.
- F5: notes on 2027 Goals say each shown dollar is rounded on its own; totals stay exact so they equal the Prices tab.
- F6: HD counts under ARC, BRC2, IME and Other in 2026 (his 85: "ARC, BRC2, IME and Other (Recommended)").
- Minor: the parts block's line reads "Range aid"; typing the shown coach value back removes the edit.

| Test | Result |
|---|---|
| T1 grid = "2027B classes", each month | 13 tabs, 0 fail |
| T2 totals | sales $2,011,791.21; GP 2027B $1,215,350.72 |
| T3 links | coach cost typed (Colonial Heights $300): GP moves, sales and classes unchanged (run on an empty saved plan, so the dollar move is not the default plan's) |
| T4 one class count | 2027B 610 |
| T5 nothing typed | 610 classes, 5,093 students, $2,011,791.21 |
| T6 no P&L | no "P&L" in any tab's text; old saved P&L edit: no warning, dropped; sheets: Summary, 9 ranges, ARC, BRC2, IME and Other, 2027 Goals, Dirt Bike |
| T8 2026 | classes 566; sales by range add to $1,651,117.18; GP $1,058,439.84. Manassas GMU 2026: 35 classes, $97,081 (HD out). ARC, BRC2, IME and Other 2026: 63 classes, $68,484 (HD in) |
| Prices groups | Manassas Mall 84 / $321,845, Woodbridge 80 / $289,115, Clarksburg 71 / $215,091 (= the other tabs); ARC, BRC2, IME and Other group 27 classes / $26,137 (BRC2 and First Ride), plus ARC in the "Carried at 2026 students" group, 3 classes / $2,985: together 30 / $29,122, the 2027 Goals figure |

Seen, for him: ARC, BRC2, IME and Other has 63 classes and $68,484 in 2026 against 30 classes and $29,122 in 2027B.
