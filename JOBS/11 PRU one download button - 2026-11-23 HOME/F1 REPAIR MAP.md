# Job 11: what changes under each answer to LAWYER's F1

Prepared only. Nothing is built. The answer is the Owner's, asked by Piston as 178.

Verdict: `C:\AI_Building\AI_LAWYER\Office desk\Verdicts\2026-11-23 PRU job 11 check - 53220a69.md`, md5 f3994950644957e3290bfcae206ac822.
Line numbers are of `C:\AI_Building\AI_MISC\06 Benches\2026-11-23 PRU class rule site course date - ANGIE-HOME-CT\trial\template.html`, the source of page baf0215661c49be2b70a699c9a79e143.

## The fact the answer turns on

The page's past-year lines hold BRC2 and First Ride under All Locations only, with none under a named range. Counted from the page's own data by `brc_by_range.py` on the bench:

| Year | Source in the page | BRC2 students | First Ride (IME) students |
|---|---|---:|---:|
| 2025 | src-data lines | 114 | 7 |
| 2026 | src-extra master26.lines | 137 | 79 |

Trends already splits one way and the other: its class counts put these two types under their site (lines 221 and 377), and its students and fees put them under All Locations (lines 226 and 442).

## If the answer is All Locations, as Trends does

- Trends does not change. Only the Excel file changes.
- Lines 703 to 705, Summary by range: students and fees of BRC2 and First Ride move to All Locations. Classes stay by site, to equal the Trends class count.
- The line building each range tab (`SP.U.filter`): students, fees and range totals carry 2-Wheel and 3-Wheel only.
- Line 711, All Locations tab: gains the BRC2 and First Ride blocks, each named with its site, beside ARC.
- Rent stays by site, because rent follows classes at the site.
- What it leaves: a range tab's classes include BRC2 and First Ride while its students do not, exactly as Trends shows today. The file must say so in a note.

## If the answer is under their site, as the file does

- The file does not change. Trends changes, so the page's figures on those tabs move.
- Line 226, `plan27Lines`: BRC2 and First Ride go to their site's range.
- Lines 441 to 443: their typing rows move to the site tab, and the sentence pointing to All Locations goes.
- Line 455 and the Plan text that says where these rows live are reworded.
- What it leaves: on 4 range tabs, the 2027 line would include students that the 2025 and 2026 lines hold under All Locations, so those tabs would show a false jump.
- 2026 could be moved by site from the Manual Log's site column, in a new build with its own check. 2025 has no site in the page's data and would wait for the final 2025 log.

## Under either answer

1. Lines 743 and 753: the two messages saying to download and then reload are reworded, because the file cannot be loaded back and a reload loses what was typed.
2. `xlsxBytes`: add the missing `bookViews` part to the workbook. The risk: each sheet's view points at workbook view 0, and the workbook names none. Excel opened the file read-only in two runs with alerts off, so a repair prompt was not ruled out. Test it with alerts on.
3. Then one blind check, PASS or FAIL to Piston first.
