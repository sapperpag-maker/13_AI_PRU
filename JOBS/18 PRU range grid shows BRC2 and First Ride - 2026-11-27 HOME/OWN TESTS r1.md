# Job 18: Angie's own tests, round 1 (not a verdict)

Bench: C:\AI_Building\AI_MISC\06 Benches\2026-11-27 PRU range grid BRC2 First Ride - ANGIE-HOME-J18
Built by j18_build.py: page_before.html (cb1532735ede13ca7ff66ac007aa9015, the accepted job17 page) to page_after.html (eb0dc3fcd05081808963b03d2d7af382, 159,197 bytes). 3 changes: the note on the range tab, a classes-only block for BRC2 and First Ride, and the line that puts that block on each range tab.
Served by the launch config pru-job18-grid (port 8818), browser storage cleared before each run.

| Test | Script | page_after | Red control |
|---|---|---|---|
| T1 grid adds up to "2027B classes", every range, every month | t1.js | 12 ranges, 0 fail | page_before: 3 fail (Clarksburg months 5,8; Manassas Mall 3-11; Woodbridge 3,5-10); plant_clarksburg_off.html: 1 fail (Clarksburg 5,8) |
| T2 a BRC2 class typed on a range tab shows on the ARC tab and moves totals once; then the other way; then emptied | t2.js | Manassas Mall BRC2 Jan: 0 to 1, ARC tab shows 1, classes 610 to 611, sales and P&L $2,011,791 to $2,014,025; typed 2 on the ARC tab, range tab shows 2, 612 and $2,016,259; emptied, back to 610 and $2,011,791, no state kept | - |
| T3 nothing typed: every figure of all 13 download sheets equal to the accepted page | t3.js | 13 sheets, 4,939 cells, hash 77a9416e8eaf9288 on both pages | one class typed on page_before: hash changes to a22cf74ab1b64d81 |
| T4 a planted fault fails T1 | plant_clarksburg_off.html | see T1 | - |

Also: the page's self-test worst difference 7.3e-12; no console errors.
Seen on the bench server only, not a fault of the page: the server sends no character set, so the browser shows "Â·" for "·". ONE VIEW shows "·" (his screenshot of 2026-11-27).
