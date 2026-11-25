# Job 15 r1: Angie's own tests (2026-11-25). Not a verdict; only Sergio accepts.

Piece: `C:\AI_Building\AI_PRU\JOBS\15 PRU coach pass rate and fill - 2026-11-25 HOME\job15 608baa5c.html`, md5 608baa5c324cd8dd6f17fee6e86f7d60, 180,701 bytes.
Bench: `C:\AI_Building\AI_MISC\06 Benches\2026-11-25 PRU weekly dashboard - ANGIE-HOME-W25\`.
Source: `Sergio PRU Class Data.xlsx` on the bench, md5 281b22390a296bebefd949fb31c816ba, a copy of his upload of 2026-11-25. Sheets used: 2024 to 2026 Demand Analysis, and Sergio 2024 to Sergio 2026. No Recap tab.
Programs on the bench: pru15_count.py (eaef796c), pru15_build.py (53ea36b9), pru15_page.html (fa869c9c), pru15_tests.py (f3ce1709).
Run: count, then build with as-of Sunday 2026-11-22 (week 47) and built date 2026-11-25. Every year is compared on weeks 1 to 47.

## Tie to the job 12 survey before building
- Demand Analysis students: 4,684 in 2024, 4,330 in 2025 and 4,388 in 2026. These are the survey's figures.
- Classes with no Limit: 49, 128 and 58. These are the survey's figures.
- Fails: 375, 341 and 319. Each is the sum of that year's I-FAILSKILL, I-FAILKNWLDG and I-FAILBOTH status counts, read by pru15_probe.py.

## Tests (the goal's four)
1. **Re-count: PASS.** pru15_tests.py re-counts straight from the workbook, without counts.json. It counts every year-to-date figure for weeks 1 to 47: all, each site, each course and each coach. It counts students, revenue, classes, fill, pass rate and students tested. That gives 730 figures, written to site/expected.json (md5 0e1990ce). The page's own figures, from `window.__PRU_DASH__.total`, were compared in the browser: 730 compared, 0 differ. No site, course or coach in the page has a non-zero figure outside the 730. A planted change (2024 students, plus 1) was caught.
2. **Student data: PASS.** Every student's name pair, email, phone, licence number and date of birth, from the three student sheets, was searched for in the page. 0 were found: 13,405 names, 13,449 emails, 13,425 phones, 13,483 licence numbers and 8,775 dates of birth searched. No value was printed.
3. **Same input, same page: PASS.** Count and build were run again. counts.json is 1b11e193 both times, and the page is 608baa5c both times.
4. **Console and tabs: PASS.** Overview, Students, Ranges, Classes and Coaches each draw, and the browser console shows no error.

## Seen, not a test
- At 375 px the bench page lays out at 980 px. The file carries no viewport line, the same as the planner page; ONE VIEW adds one. Nothing on the page is wider than the screen.
- Ranges and coaches show as the file writes them: site codes (MANMALL, WOOD and others) and instructor names (Sergio question 20).
- The coach table lists every first Instructor of 2024 to 2026.
