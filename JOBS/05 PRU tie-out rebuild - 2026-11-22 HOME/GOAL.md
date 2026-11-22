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
