FAIL (1 finding)

# Blind check r9, PRU job 07, words-only repair

- Page: draft-i.html, md5 2598de94e387c5f3ba64f8be5116770c
- Before: draft-h.html, md5 2247437a339585a863de28527767f47c
- Goal: GOAL.md, md5 8a9b74d169416f5baa571b92fdbde055
- Source: 2026_PRU_Manual_Log_v3.xlsx (upload eb48a496), md5 37c427cf4078f449459b532e4d8e9377, sheet Master, columns B to E, and J as sums

## Findings

### 1. Trends explains only half of how a 2027B row misses a printed total (point B1)

- **Where:** draft-i.html line 345, Trends foot note, Students and Sales $, table year 2027B.
- **Shown:** "so a total can differ from adding the rounded rows above it". That covers a column against the All ranges row. It says nothing about a row's own twelve months against that row's printed year total.
- **Should be:** the note also covers the months beside the total. The plan and Budget notes on the same page already say "above or beside". This wording is a suggestion; the fault is the missing explanation.
- **Measured:** start inputs, class All, table year 2027B, all rows including All ranges, adding the printed months and comparing to the printed year cell. Students: 7 of 11 rows miss. Sales $: 8 of 11 rows miss. Classes: 0 of 10 rows miss.
- **Reading used:** I read "the printed total" in point 1 as including each row's year column. If the desk means only the All ranges row, this finding falls away and every other check below passed. That call belongs to the desk, not to this checker.

## What passed

**A. Figure equality: PASS.** My program drove h and i side by side in the built-in browser.
- 1,820 views, 573,793 shown items compared (text, tooltips, input values, placeholders, labels, chart points), 0 differences in item count.
- 7 input scenarios: start; fill all 73; type fills and prices; unit fills with fractional months; rent and Dirt Bike; fill 0 with Dirt Bike hidden; fill 100 mixed.
- Trends: 3 measures, 8 class filters (All and 7), 4 table years, and each range row selected. Plan: closed and each of the 20 Months panels open in turn. New initiatives. Budget in 3 P&L views.
- Exactly 10 distinct lines differ, all reworded sentences or labels, none a figure:
  1. Trends note, Students
  2. Trends note, Sales $
  3. Trends note, Classes
  4. Sources line
  5. Plan footnote
  6. Discount note
  7. Budget coach row, ARC
  8. Coach note
  9. Rent note
  10. Rent table header
- Program fires: a copy with one planted number (classes2026 January 4 to 5, md5 2853d160ee8251cb8f23624d91f44f96) gave exactly 1 distinct difference, 573 against 574, in 147 views.
- Evidence: out_h_vs_i.json (md5 20afed04d90baf75004f15cebf17a679), out_i_vs_plant.json (md5 84b21b69921dc3a9ac103c2fe2cee82a).

**B1, rows against the All ranges row: PASS.** The sentence shows on all 224 Students and all 224 Sales $ views. Rows miss the All ranges row only on 2027B (15 of 49 views each for Students and Sales $). Classes cannot miss: 0 misses in 84 views, all 240 start month cells have at most one decimal, and edits round to 0.1.

**B2, Sources line: PASS.** It shows on all 1,820 views, so on every tab.
- Master by class date: rebuilt from Master, 4,606 students, fees 1,602,640. 72 class-by-month cells (students and fees) with 0 differences. Months panel data, 27 site and type keys, 0 differences.
- 2027 base: Master by week rebuilt, 26 keys, 0 student and 0 class cells differ. Weekly summary: the page's 4,543 students and 1,585,090 sales both appear on tab WklyConsolidating Wd, row 1254.

**B3, discount note: PASS.** Counted from Master, 2026 weeks: 3,925 2-Wheel and HD, plus 17 others in the spread code (3-Wheel 8, First Ride 4, ARC 3, BRC2 2), total 3,942.

**B4, Budget labels: PASS.** Coach note, rent note, rent table header and the one coach row printing a base figure (ARC, 2 classes) all carry the label, in every scenario. Eight of nine sites tie to Master on weekends and all nine on classes; for Virginia Beach weekends see Risk 1.

**B5, the December code: PASS.** Counted rows: 45 students, 8 sites, 6 class types, first listed at Clarksburg as 2-Wheel. Six site and type cells show December students with 0 classes (11 students), and all 11 belong to this code. No other month has such a cell. Of 48 HD students, 47 are in the 6 HD-only classes and 1 is in this code.

**C, changed sentences: PASS.** 16 changed sentences: 0 quotation marks, 0 his/him/he, 0 my pick, 0 of the seven names. Each scan was shown to fire on a control string. Each claim was checked in A or B, apart from the wording in finding 1.

## Risks that are not faults

1. Virginia Beach weekends print 33. Master holds 32 distinct Sundays across its three site codes, and 34 when counted per site code. No rule I read says which count is right, so this is a question and not a finding. The figure is the same in h and i and feeds rent.
2. The Sources line lists sales for the Months panels and the student comparison, which show no sales. The list reads as a group and no figure is wrong.
3. The plan's 573 classes held or booked is a year total. The list behind it differs from Master by class date in 5 of 12 months, but the months are not printed and the totals are equal (573).

## What I could not check

- Input scenarios beyond the 7 above.
- Row-beside-total misses were measured on the start inputs only, one view per measure.
- Whether the 3 Virginia Beach site codes are one range or several.
- The non-Master sources (Class_Data, the rent table, the budget workbook). Out of scope; A proves their figures did not move between h and i.

## My own mistakes

1. My first harness named its function run and then assigned window.run, so it recursed and crashed before comparing anything. Renamed and rerun; no result came from the crashed run.
2. My first sentence-scan control did not exercise the single-quote pattern. I added a control and it fired.
3. Two of my Master programs printed the site and course of the first row of a class code, and one printed the digits of the class codes spread across sites. No person field was read or printed, but this came closer to the order never to print a row than it should have.
