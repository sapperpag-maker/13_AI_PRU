# Job 15 r3: Angie's own tests (2026-11-25). Not a verdict; only Sergio accepts.

Piece: `C:\AI_Building\AI_PRU\JOBS\15 PRU coach pass rate and fill - 2026-11-25 HOME\job15 4439a32e.html`, md5 4439a32efadb806a45bb7c215696ecc7, 177,939 bytes. It repairs r2 (ac7c092e).
r2's blind check: ANGIE-HOME-J15B, VERDICT.md md5 c8b6afce, first line FAIL. 2 counted FAILs so far.
Bench: `C:\AI_Building\AI_MISC\06 Benches\2026-11-25 PRU weekly dashboard - ANGIE-HOME-W25\`. Programs: pru15_count.py (2ddf794a), pru15_build.py (3a416f77), pru15_page.html (337bdb4e), pru15_tests.py (f7e7cb13). counts.json is f347a45b. The r2 programs are kept as *_r2 copies.

## What changed from r2
- F1, Sergio Q30, "Instructor 1 only": no change to who gets a result. The count now records the rows with two different coaches marked I (6 in 2025, week 22; 0 in 2024 and 2026). The Coaches note names them.
- F2, Sergio Q31, "Show both (Recommended)": a new measure, Students, all rows, for every student row credited to the main coach. The coach table shows Students, all rows, Students tested and Pass rate for each year. The chart can show any of the three.
- F3: a week standing alone now gets a dot in every year, not only in 2026.
- F4: the page had no viewport tag, so a phone drew it 980 px wide and shrank it. The tag is added, and each chart is now drawn at the screen's own width, with every other month label below 520 px.
- R1: the source lines name the three fail statuses.
- R2: 2024 and 2025 end at week 52, the week of their last Sunday, not week 53.
- R4: the coach note no longer repeats the main-coach phrase.

## Tests
1. **Re-count: PASS.** pru15_tests.py re-counts from the workbook and writes 807 year-to-date figures to site/expected.json (bff17204). The new ones are Students, all rows by coach. In the browser, 807 were compared and 0 differ. A planted change (one coach's rows, plus 1) was caught. Of the coach table's 770 cells (77 coaches), 0 differ from expected. The All row for 2026 reads 4,567 rows and 3,744 tested, the same as the r2 checker's figures. An earlier run gave 69 cells off. That was a fault in my test: it showed a dash where expected.json has no key for a coach with no rows in a year. The page was right.
2. **Student data: PASS.** 0 of 13,405 names, 13,449 emails, 13,425 phones, 13,483 licence numbers and 8,775 dates of birth were found.
3. **Same input, same page: PASS.** The page was built twice from counts.json f347a45b, and both builds are 4439a32e. counts.json was re-run from the workbook for r3; the totals are unchanged (pass 3,932, 3,588 and 3,425; fail 375, 341 and 319).
4. **Tabs and console: PASS.** At 375 px, in light and in dark, on Overview, Ranges, Classes and Coaches: the page is 375 px wide with no sideways scroll, and chart text is 11.1 px. Jones, Jeramiah's pass rate shows 8 dots for 2024 and 2025, the 5 and 3 the checker counted. The console shows no error, and the text of all five tabs has 0 quote marks.

## Not tested here
Every chart point one by one; colour contrast measured; the live ONE VIEW host.
