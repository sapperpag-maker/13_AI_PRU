# Own tests, job 13 r9 (2026-11-24, Angie, HOME). Not a verdict.

Page: `job13 6ded25cb.html` (6ded25cb0d85d55d4e893bb14b824897, 155,849 bytes). Built from r8 926ab8a84c26fd7c009e036aab63da28 by `C:\AI_Building\AI_MISC\06 Benches\2026-11-24 PRU rename All Locations - ANGIE-HOME-W24\fix.py`. The program holds 16 exact replacements, each made to match exactly once, or nothing is written.

Start word: Piston, 2026-11-24, steps 1 to 3 only. Step 4 (the blind checker) waits on Sergio's yes to GOAL.md.

How it was run: r8 and r9 were served from the bench at http://localhost:8813, in the built-in browser.

1. **No "All Locations" shown: PASS.**
   - Visible text and aria-label, title and placeholder attributes were swept on all 4 top tabs.
   - On Monthly trends, every range tab was swept under Students, Sales $ and Classes: 46 views.
   - Then Summary, the renamed tab and Fairfax were swept under every Class filter option: 72 views.
   - 0 hits. The tab button reads "ARC, BRC2, IME and Other".
   - The first build failed this test: the Summary table's row label still showed the old name. It was fixed, rebuilt and rerun.
2. **Excel download equal: PASS.**
   - A plan was saved in r8, then opened in r9. The two pages' `plannerSheets()` were compared with the "Downloaded" line taken out.
   - After the name swap they are equal, and r9 holds "All Locations" nowhere.
   - The sheet is named "ARC, BRC2, IME and Other". `xlsxBytes` builds a 236,297-byte zip.
3. **Saved draft opens unchanged: PASS.**
   - The test plan in r8: Fairfax GMU 2-Wheel March = 9, ARC June = 3, saved with Save plan.
   - In r9 the plan state is equal, the P&L figures (`budget().B`) are equal, and the edits file text is equal apart from its time stamp.
4. **Self-test and console: PASS.** SELFTEST worst gap is 7.3e-12. The console shows no error.

Not tested: opening the downloaded .xlsx in Excel itself.

Left in the code on purpose: "All Locations" stays as the key in 22 places (data, sorting, comparisons, two comments).
