# Job 05 goal: the tie-out program, rebuilt to read stored numbers only

Angie, 2026-11-22. Sergio's Q63, his answer: "Yes, rebuild it (Recommended)". Asked in his words: "can you have the program convert every number into a number format?"

## What the finished piece shows
`tie_out.py` and `test_tie_out.py`, built from the parked copies in `C:\AI_Building\AI_PRU\JOBS\04 PRU figures tie-out skill - 2026-11-22 HOME\PARKED\pru-figures-tie-out\` (tie_out.py eab300b2, test_tie_out.py 05404aa2), where:
1. A cell row reads only the cell's stored value. The program never reads a number format. Text, boolean and date cells, and empty ones, are ERROR.
2. A shown value with % is compared to the stored value x 100. A shown value without % is compared to the stored value as it is. The `scale` column is gone, and a figures.csv that still has it exits 2.
3. A gl row's shown with % is ERROR, as before.
4. `--out` must name a file that does not exist yet; any existing file, whatever path spelling or link reaches it, exits 2 and stays unchanged.
5. Everything else holds as in job 04's spec: md5 and size first, strict shown and amount grammars, the GL header, record counts, accounts, store, dates, journal, side, half-up rounding, the sign rule, exit codes, and no GL line or customer text in any output.

## The test that says it shows it
- `python3.14 -I -B test_tie_out.py --bench <folder>` ends `TESTS: PASS (n)` and writes no `__pycache__`.
- Each of r7's cases now gives TIED only where stored value and shown agree under rule 2. Example: cell -0.5, format `0%;"neg"`, shown -0.5% comes out OFF.
- r7's A2 cases (`\\?\` path, `\\localhost\C$` path, hard link) exit 2 with the file unchanged.
- A blind Opus checker that did not build it writes PASS.

## Addendum 2026-11-22: what the accepted build does beyond the points above
Sergio's Q64, in Angie's chat: "Fix both, one last check". Sergio's 75, in LAWYER's chat (relayed by Piston): "Keep both (Recommended)".
- Cells are cut to 15 significant digits, half up, from the exact stored value (int or float), as Excel shows them. A 16-digit whole number is read cut, not as stored (Q64).
- Any figure or sum that would need rounding is ERROR: the difference column; GL amounts and shown values over 18 whole digits or 6 decimals; cells over 18 whole digits (Q64).
- A shown value with both $ and % is ERROR (75).
- The recomputed, difference and GL sum columns print every digit, not 2 decimals, and -0 prints as 0 (75).
- Point 5's "md5 and size first": each source's md5 and size are checked before it is read, not printed.
Accepted build: `BUILT r5 PASS\` (tie_out.py a8f90d60, test_tie_out.py c9e6562a). LAWYER: `C:\AI_Building\AI_LAWYER\Office desk\Verdicts\2026-11-22 Angie PRU job 05 tie-out rebuild r5 - after Sergio's 75.md` (md5 14fe45e3, PASS).
