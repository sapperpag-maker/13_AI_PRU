# Job 15 r4: Angie's own tests (2026-11-25). Not a verdict; only Sergio accepts.

Piece: `C:\AI_Building\AI_PRU\JOBS\15 PRU coach pass rate and fill - 2026-11-25 HOME\job15 8f785eb9.html`, md5 8f785eb9a641931206505d3a1b7c8833, 178,961 bytes. It repairs r3 (4439a32e).
r3's blind check: ANGIE-HOME-J15C, VERDICT.md md5 7e271c92, first line FAIL. 3 counted FAILs: Piston picks the shape before r4 goes to a blind check.
Bench: `C:\AI_Building\AI_MISC\06 Benches\2026-11-25 PRU weekly dashboard - ANGIE-HOME-W25\`. Programs: pru15_count.py (16d75431), pru15_build.py (cd4f4f87), pru15_page.html (8cb7bfd2), pru15_tests.py (727e365a). counts.json is cca3be7b. The r3 programs are kept as *_r3 copies.

## What changed from r3
- F1, Sergio Q32, "get the coach from the first coach column": a row with no coach marked I now goes to the coach in Instructor 1, with the ending (I2, I3) dropped. In weeks 1 to 47 that is 446 rows in 2024, 24 in 2025 and 22 in 2026. Rows with all three Instructor columns blank stay as (no main coach): 203, 37 and 44. The source lines and the Coaches notes say this, with the counts.
- School totals do not move: every row was and is counted. Pass rate stays 91.3%, 91.3% and 91.5%.
- Sergio Q33, "Always dark first": no change.

## Tests
1. **Re-count: PASS.** pru15_tests.py, with the Q32 rule, writes 810 figures to site/expected.json (4ad3c926). In the browser, 810 were compared and 0 differ. Of the coach table's 780 cells (78 coach rows), 0 differ. The (no main coach) row reads 203, 37 and 44.
2. **Student data: PASS.** 0 of 13,405 names, 13,449 emails, 13,425 phones, 13,483 licence numbers and 8,775 dates of birth were found. The r3 checker notes that a plain search finds 7 full names, all of them coach names, which Sergio Q20 allows. My lists are the rows holding both a first and a last name, and holding a date of birth.
3. **Same input, same page: PASS.** The page was built twice from counts.json cca3be7b, and both builds are 8f785eb9.
4. **Console and words: PASS.** No console error, and 0 quote marks on all five tabs. The layout code did not change from r3, which the r3 checker measured at 11.07 px chart text at 375 px.

## Not tested here
Every chart point one by one; phone width again (the layout code is unchanged from r3).
