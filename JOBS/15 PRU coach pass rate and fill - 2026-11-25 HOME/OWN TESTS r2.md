# Job 15 r2: Angie's own tests (2026-11-25). Not a verdict; only Sergio accepts.

Piece: `C:\AI_Building\AI_PRU\JOBS\15 PRU coach pass rate and fill - 2026-11-25 HOME\job15 ac7c092e.html`, md5 ac7c092e374a593af43507e6990f6b60, 174,918 bytes. It repairs r1 (608baa5c).
r1's blind check: ANGIE-HOME-J15A, VERDICT.md md5 771c630f, first line FAIL. 1 counted FAIL so far.
Bench: `C:\AI_Building\AI_MISC\06 Benches\2026-11-25 PRU weekly dashboard - ANGIE-HOME-W25\`. Programs: pru15_count.py (b70d37df), pru15_build.py (31bfbab6), pru15_page.html (f170de1c), pru15_tests.py (b4a4abe6). counts.json is 2d91de06.

## What changed from r1
- F1: every tile now ends with its source: the file, the sheets (Demand Analysis sheets 2024 to 2026, or sheets Sergio 2024, Sergio 2025 and Sergio 2026) and the column or rule. Before, 11 tiles had none.
- F2: the Overview now has four weekly charts: Students, Revenue, Fill and Pass rate. Before, it had two.
- Sergio Q29, "Main coach (I), merged (Recommended)": a result goes to the coach whose name ends in I, in any Instructor column, with the ending dropped. That leaves 77 coach rows in the data.
- Sergio Q28, "Leave them out (Recommended)": Demand Analysis rows with no Limit, no # Stud and no Fees are not classes. That is 38, 116 and 53 rows over the full years 2024, 2025 and 2026. Students and fees are unchanged.
- The checker's notes:
  - O1: no "(no zone)" bracket in the Range list.
  - O2: the label is now "Class type".
  - O3: "retest, retake".
  - R3: the Fill note now names the classes left out with no Limit for every year.
  - The Classes note names the empty rows left out for every year.
- The page is now pure ASCII, with 0 bytes over 127. The en dash is written as a JavaScript escape, so a server that sends no character set no longer garbles it.

## Tests
1. **Re-count: PASS.** pru15_tests.py, updated for Q28 and Q29, re-counts from the workbook. It gives 642 year-to-date figures in site/expected.json (md5 874190d1). In the browser, 642 were compared and 0 differ, and no page figure falls outside the 642. A planted change (revenue, plus 1) was caught.
2. **Student data: PASS.** 0 of 13,405 names, 13,449 emails, 13,425 phones, 13,483 licence numbers and 8,775 dates of birth were found. This search uses the "First Last" form. The r1 checker also found 5 names in "Last, First" form, all inside coach names, which Sergio question 20 allows.
3. **Same input, same page: PASS.** The page was built twice from counts.json 2d91de06, and both builds are ac7c092e.
4. **Tabs and console: PASS.** All five tabs draw, and every tile names its source: 4/4, 5/5, 4/4, 4/4 and 2/2. The Overview has 4 charts. The browser console shows no error, and the page text has 0 quote marks.

## Not tested here
Light theme and phone width; the 2024 and 2025 chart points one by one; the live ONE VIEW host.
