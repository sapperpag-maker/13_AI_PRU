PASS

# Blind check r6, PRU job 07, release 5 draft f

Checker: job agent launched by ANGIE-HOME-T7, machine HOME, 2026-11-22. This is a builder's blind check, not an acceptance. Only the owner accepts.

## Files read (md5, read before the check and again after it, unchanged)

- `release 5 draft f.html` 218637b509804e342cedabb9bc9b8e16 (piece under check)
- `release 5 draft e.html` 70c6857484caf486313a561e1cb77115 (yardstick for B)
- `baseline.html` 0ca374047992a7f42583b5ea9f17a6af (release 4)
- `GOAL.md` 1fedf1bb8dcdded858d0223da6b1c694

Served from this bench by `serve.py` on 127.0.0.1:8799 with `text/html; charset=utf-8`. Driven in the built-in browser by `harness.html` and `harness.js`. The draft key was cleared before each page load.

## A. GOAL points and tests, on draft f

| Test | What ran | Counted result |
|---|---|---|
| 1 Students and Sales $ = release 4 | Data: 39 lines x 2 measures x 3 years x 12 months. Screen: 2 measures x 8 class choices x 3 years | 2,808 data cells, 0 differences. 48 views, 3,796 table cells, 0 differences. 0 baseline rows with figures missing from f |
| Point 1 years | Year list and all Trends text, 3 measures x 4 years | List is 2024, 2025, 2026, 2027B. 0 mentions of 2022 or 2023 |
| 2 2026 classes = `classes2026` | All-ranges row against the page's list | 12 months, 0 differences (4, 12, 69, 60, 78, 60, 54, 58, 52, 38, 36, 52) |
| Point 4 class filter | Classes by range and class, recounted from the page's class data | 6 class choices with a figure, 492 cells, 0 differences. HD and Other show not available |
| 3 contrast | Program over all 6 year pairs and each color against the card, both themes | Dark: lowest pair 1.617, lowest against card 3.319. Light: lowest pair 1.628, lowest against card 3.607. Limits 1.5 and 3.0 met |
| 4 filter buttons | All 15 year combinations x 3 measures x 8 classes x each table year, through the page's buttons and lists. Real mouse clicks on Classes and on the year buttons for one off-and-on path | 768 states, 768 checks of lines, legend, year list, pressed and disabled state, message and table: 0 failures. The last year on stayed on when clicked (by script and by real mouse) |
| Point 5 not available | Same 768 states | 0 legends or tables show 0 for a year or class with no source |
| 5 no customer data | All 1,350 strings in the page's data blocks (214 distinct) | 0 scan words, 0 email shapes, 0 phone shapes |
| 6 other tabs = release 4 | Plan, Budget in 3 views, Dirt Bike rows | Plan 536 cells, Budget 1,028 + 1,028 + 1,014 cells: 0 differences. Dirt Bike 6 rows equal (Rent row is labeled "Rent (one day a month)" in release 4). The 2027 vs 2026 tab is gone |
| 7 Dirt Bike | 27 input edits, emptied boxes, Reset | 2,690 formula checks, 0 failures. 0-weekend months show no class and no cost. Start $30,816 net. Reset restores every row. P&L unchanged at every step |
| 8 2027B | Every range and class, students and class fees, at start and at 85% fill | 16 views and 888 cells each run, 0 differences. All ranges = plan tab for students (4,455), class fees ($1,706,910) and classes (498). 85% fill moved students from 4,455 to 5,030 |
| Point 7 line | Chart read in the browser | 2027B has its own color and a dashed line |
| Point 8 | Tab list | Four tabs remain |

## B. Every figure, draft f against draft e

| Run | States | Items compared | Same | Differ |
|---|---:|---:|---:|---:|
| Trends: 3 measures x 8 classes x each year x each range row | 542 | 191,524 | 190,982 | 542 |
| Trends: all 15 year combinations | 768 | 164,567 | 163,799 | 768 |
| Plan (with 20 Months panels and edits), Budget 3 views, Dirt Bike inputs, Reset, hide, Save | 59 | 25,114 | 24,749 | 365 |
| Total | 1,369 | 381,205 | 379,530 | 1,675 |

All 1,675 differing items were read as 36 distinct text pairs. Item counts matched in every state. 35 pairs have the same figures. The other pair is the footer, whose only lost number is the "round 5" in the removed wording. No figure changed.

## C. Shown text

Scanned: every text node, title, aria-label and placeholder in all 1,369 states, all data strings, and in source the messages that cannot be reached here (failed self-check, save errors, read-only, conflict).

- Quotation marks: 0
- his, him, he, or first-person wording: 0
- Rick, Angie, Sergio, Piston, LAWYER, Ben, Brain: 0
- Six scan words: 0 in draft f, in source and on screen
- Possessive apostrophes (such as workbook's) are not quotation marks and are not counted

Control: the same kind of scan on draft e's four tabs found 33 name nodes and 11 pronoun nodes; draft f's found 0 and 0. The baseline's plan tab showed 3 nodes with curly quotes. A wrong figure planted in a live draft f cell was caught by the comparison.

## D. Replaced notes

All 36 changed text pairs were read. Each states what the old note stated, without the person's name, and none is cut off. Every tab that says workbook also shows the full name Budget workbook, and the footer names the file, 04 PRU GP rebuilt.xlsx, tab PRU-pl.

Trends, Classes view:
- Years on with no class source: "No class source for the years on." 32 states, all correct.
- A year with a source on, but no figure for the class: "not available for this class." 66 states, all correct.

## Findings

NONE.

## Risks, separate from the verdict (none is a wrong value)

1. Bare "workbook" on the plan tab is read beside Manual Log and Class Data, which are also workbooks. Shapes tried: every bare use on the Plan and Budget tabs. None pointed to another file, and the full name is on both tabs. Naming it Budget workbook at every use would remove the risk.
2. The footer's "2027 rent table of 2026-11-20" names the table and its date but no file. The statement is true. A file name, if one exists, would remove the risk.
3. The message "not available for this class." starts with a small letter. It carries the wording the order asks for and is unchanged from draft e.

## What I did NOT check

- Any figure against its Excel source or GL. This check is page against page, so it proves sameness, not correctness of the underlying numbers.
- The whole 15-year-combination run with real mouse clicks. Real mouse covered one path; the rest used each control's own click and change events.
- Save against the real artifact service, and the failed self-check, read-only, conflict and save-error states on screen. Those messages were read in source.
- A visual review of the light theme. Its colors were measured by program.
- Phone width and browsers other than the built-in one.

## My mistakes

NONE that affect a result. My first browser click lookup for the year buttons returned no match, so I read their positions and clicked by coordinates. Each click was confirmed by the page's state.
