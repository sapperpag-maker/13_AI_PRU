# Job 19: Angie's own tests, round 1 (not a verdict)

Goals: GOAL.md, GOAL r2.md, and his 84 (Angie's chat, 2026-11-27): "you have ARC BRC2 IME and other in their separate tab, but then you also count them in each range recap, that's where i get confused and should change." So a range counts its 2-Wheel and 3-Wheel only; BRC2, First Ride and ARC are counted only on the ARC, BRC2, IME and Other tab, in both years. This replaces job 18 (its change is not used) and GOAL.md point 3.

Bench: C:\AI_Building\AI_MISC\06 Benches\2026-11-27 PRU budget GP by range - ANGIE-HOME-J19
Built by j19_build.py from the accepted page (job17 cb1532735ede13ca7ff66ac007aa9015) to page_after.html (582fa2cca5f36c8fe424cde81e00d323, 152,988 bytes). Served by launch config pru-job19-gp (port 8819), browser storage cleared.

| Test | Result on page_after |
|---|---|
| T1 every range tab's grid adds up to its "2027B classes" row, each month | 13 tabs (12 ranges and ARC, BRC2, IME and Other), 0 fail. ARC tab: grid 30, year row 30 (his screenshot showed 3 and 2 before) |
| T2 GP = sales − coach − rent; blocks add to the total; total sales = Prices tab sales | total sales $2,011,791.21 = plan sales; coach $607,445 (= the accepted page's Cost of Sales); rent $188,995.49 (= the page's rent); GP 2027B $1,215,350.72 |
| T3 links | class typed on tab 1: classes, sales, trends line and GP move together. Price, fill: sales and GP move. Coach cost typed (Colonial Heights $300): coach and GP move, classes 609 and sales unchanged. Rent typed ($900): rent and GP move, sales unchanged |
| T4 one 2027 class count | 610 on the trends Summary, Prices KPI, 2027 Goals KPI and table, download Summary |
| T5 nothing typed | 610 classes, 5,093 students, $2,011,791.21 sales; self-test worst difference 7.3e-12 |
| T6 no P&L | no tab, no "P&L" in the page text, no P&L sheet; sheets: Summary, 9 ranges, ARC, BRC2, IME and Other, 2027 Goals, Dirt Bike |
| T7 tabs | Students and Classes, Prices, 2027 Goals, New initiatives; no fill, class or reset box on Prices; fill boxes on tab 1 (all, by type, and one per site and class in the grid) |
| T8 2026 by range | 2026 classes by range add to 566, 2027B to 610; 2026 sales by range + the workbook line add to $1,651,117.18 (the workbook's 2026); 2026 gross profit $1,058,439.84 = workbook sales − Cost of Sales $427,937.70 − Rent $164,739.64 |

Planted faults: T1 on the accepted page fails (job 18 r1: 3 ranges). Other plants not yet run: left to the blind checker.

Seen, for him: ARC, BRC2, IME and Other has 56 classes and $47,892 in 2026 against 30 classes and $29,122 in 2027B.
Seen on the bench server only: no character set sent, so "·" shows as "Â·".
