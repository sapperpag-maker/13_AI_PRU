PASS

# PRU job 13 r9 (rename "All Locations" to "ARC, BRC2, IME and Other"): blind check of piece md5 6ded25cb0d85d55d4e893bb14b824897

Filed by Angie, the builder, from the checker's hand-back. The checker had no findings file: the harness refused its FINDINGS.md, so its verdict line is in its PROGRESS.md.
- Fresh checker, tag ANGIE-HOME-J13A, 2026-11-24 about 17:15 to 17:47 EST. It used about 178,322 tokens (the app's own count).
- Bench: `C:\AI_Building\AI_MISC\06 Benches\2026-11-24 PRU job 13 blind check - ANGIE-HOME-J13A\`.
- Angie read the md5s of piece.html, base.html, diff.txt, PROGRESS.md and compare_out.txt; all are equal to the hand-back.
- This is a finding, never an acceptance; only Sergio accepts.
- Goal: `GOAL.md`, md5 b8bd2ba39a77c1f3d565ae0a7c59d030, accepted by Sergio, question 5.

md5 at the start and the end: piece 6ded25cb0d85d55d4e893bb14b824897; base (live r8) 926ab8a84c26fd7c009e036aab63da28; goal b8bd2ba39a77c1f3d565ae0a7c59d030.

The checker invoked office-review-adversarially at about 17:15 EST, before reading anything else.

The rules program refused the launch's two asks as written ("--job is given beside --act or --what", then "PRU planner page is not on what.txt"). The checker asked again with `--act review --what budget`, as All and as Angie, and got 764 lines each. That refusal is a mistake of the launch.

## Failing findings
NONE.

## Risks (not failing findings: no wrong value shown)
1. R1, piece line 476: the grid block "ARC (All Locations)" now reads "ARC". The name is dropped there, not renamed. Its aria-labels change the same way.
2. R2, piece line 449: the Trends note's "it holds ARC, BRC2, IME and Other" now reads "it holds those classes".
3. R3, piece line 725, Excel Summary cells A40 and A51: "ARC, BRC2, IME and Other (BRC2, First Ride, ARC)". This is the plain swap the goal asks for. The label repeats the name and says First Ride where the name says IME.

## Passed
1. Test 1: 384 views per page, covering every measure, range tab and class filter, the Summary row click, the plan, New initiatives and the Budget tab. The piece shows "All Locations" in 0 views: clean, with a draft, and with loaded edits. The base shows it in 379. The only attributes still holding it are the keys data-range and data-r.
2. Test 2: the xlsx was opened with openpyxl: 13 sheets, 4,876 cells. After the name swap, with the Downloaded line masked, 0 cells differ in all 3 pairs. The sheet "ARC, BRC2, IME and Other" opens cleanly.
3. Test 3: a draft typed in the base (fill %, price, ARC classes, students per class, a BRC2 class, a P&L year figure) loads in the piece with 0 differences. That covers 1,296 trend series, the budget grids and every sheet. The base's edits file also loads through loadEdits with 0 differences.
4. Test 4: SELFTEST worst gap is 7.28e-12. No console error appeared; the checker proved its console reader works with a planted error.
5. Key lookups still work: the Summary row click, inRange and elsewhere, RANGES, RTABS, CARRIED, and the Download button.
6. The diff from the base is 52 lines: the RNAME helper plus label-only changes. No logic changed.

## Not checked
- The ONE VIEW frame save and load path, and the plan-state embed.
- Microsoft Excel itself.
- Light theme and mobile width.
- One draft only.
- Two early piece sessions were not read for console errors.

## Checker's own mistakes
- It clicked the real Download button, which may have written a file to the browser pane's download folder (location UNRESOLVED).
- It served the pages with its own serve.py (http.server plus a POST into out/) instead of plain http.server.
