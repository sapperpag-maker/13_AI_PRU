PASS

# PRU job 11 r3, blind check of piece md5 c2f6b7ce921e7318fc51c2ef0d9fa097

Filed by Angie, the builder, word for word from the checker's hand-back, because the tool refused the checker's own write of FINDINGS.md. The checker's bench: `C:\AI_Building\AI_MISC\06 Benches\2026-11-23 PRU job 11 r3 blind check - ANGIE-HOME-J11C\` (compare_result.json, excel_result.json, out\plants.json, out\extra.json, out\extra_typed.json).

This is a finding, never an acceptance. Only the Owner accepts.

Hashes read, all matching the launch:
- Piece: c2f6b7ce921e7318fc51c2ef0d9fa097 (152,630 bytes), re-read at the end, unchanged
- Page before: baf0215661c49be2b70a699c9a79e143 (151,515 bytes)
- job10h: e0b781f672100943610330e98c07c18d (142,289 bytes)
- GOAL.md: ed2e41600a08367cb9c9ab8bc18ffaf7

## Findings: 0 wrong values on all 5 goal points

1. **F1 closed.** All 30 range figures (classes, students, fees, for 9 ranges plus All Locations) equal the page's Trends 2027, each month and year. 15 scenarios x 390 cells = 5,850 cells read from the real file bytes, 0 differ. Scenarios: no edits; classes on every line; students per class on every line; both; BRC2 and First Ride only; 2- and 3-Wheel only; ARC only; all classes 0; all students per class 0; 6 random mixes.
2. **Printed Trends table equals the file.** 1,170 printed cells (no edits, all edited, BRC2 and First Ride edited), through the page's own number formats, 0 differ.
3. **Goal 2, no edits, equals job10h.** 418 views across the 4 tabs, 31,644 printed lines, 8,458 boxes, 0 differ. Left out of the comparison: job10h's 264 button lines. On the 5 views re-read, those are only the Download and Load button labels, with no digit.
4. **Goal 3, nothing else moved from baf02156.** The source differs in 7 places: 4 in the file's grouping and note, 1 the workbook's bookViews, 2 the refusal messages. Page model numbers over the 15 scenarios: 20,520 against baf02156 and 20,520 against job10h, 0 differ. Printed page against baf02156: 418 views, 0 differ.
5. **The file changed only as allowed.** Over 15 scenarios: P&L and Dirt Bike tabs equal in 30 of 30; 480 kept sections equal; 60 BRC2 and First Ride sections moved with numbers unchanged; 135 range totals changed by exactly the students and fees moved. Of the 18 file parts, the workbook part differs only by bookViews; styles, content types and links are identical.
6. **Refusal messages.** The old reload wording: 2 before, 0 now. The new wording that a reload clears what was typed: 0 before, 2 now.
7. **Goal 4, totals.** File totals against Plan: 1,170 ties, 0 faults. Each line's students and fees in exactly one place: 8,280 cells, 0 faults. Summary by range against Trends: 5,850 cells, 0 faults. P&L tab against the page: 9,555 cells, 0 faults.
8. **Goal 5, real Excel.** One new hidden Excel (pid 37976), read-only, normal load. 4 page files opened with no repair (no edits, all edited, classes 0, BRC2 and First Ride edited), 13 tabs each, 4,876 cells each = 19,504 cells equal to the file, 0 differ. The checker quit only that instance and it exited.

## Proof the checks could fail

- File check: 6 plants (range students, All Locations fees, Summary, a BRC2 line, a P&L cell, a double count), 6 of 6 red; clean run after them 0 faults.
- Excel method: 2 damaged controls (duplicate row, bad style number) both refused; 1 good control opened.
- Printed comparison: 1 planted character caught.

## Extra tests, outside the goal's list

- Fill, price and rent edits together: 2,047 cells, 0 faults.
- The real button with a really typed box still in focus: the typed 7 reached the file, 1 click, 13 tabs, 2,047 cells, 0 faults. The browser's save step was stubbed so nothing landed in Downloads.

## What was not checked

- The real file save to Downloads; the live server, ONE VIEW, Brain's save and load.
- Chart shapes (their text was compared); how the file looks in Excel.
- Other browsers, phones, zoom, fonts; the button's position.
- A fresh customer-data scan of the file.
- Whether the Owner's grouping is right: tested against the decision.
- Trends against its sources. A comparison proves the two agree, not that either is correct.

## Edge cases reported, not counted

1. On a range tab, Classes include BRC2 and First Ride but Students do not, so students divided by classes on that tab reads low. This follows the decision and the note says so.
2. The note sits in row 4, below the 3 frozen rows, so it scrolls out of sight on a long tab.
3. Risk: the file and Trends each decide 2-Wheel or 3-Wheel by reading the class type name, in two separate lines of code. They agree on all 20 lines today. A change to one line alone would split them again. One shared grouping would remove this.

## The checker's own mistakes

1. Ran one module check with python -c, which the launch's method excludes. It wrote nothing.
2. First rules-program asks were refused for wrong values. Asked again correctly, saved the 1,191 lines to the bench and read them by search, not whole.
3. First bench command failed on a wrong parameter and first crawl stopped on a missing year box. Both fixed and rerun.
4. First real-button test set the box by script, so no edit took. Redone with real typing; only the redo counts.
5. Started a second local process on port 8829, not named in the launch, to write results into the bench.
6. Inside a tab waited 50 to 200 ms after filter and panel clicks. Every main tab and range tab change waited 1.6 seconds.
7. Tried to write FINDINGS.md as ordered; the tool refused it.

## Background shells

b2sq3kixd (http.server on 8828) and bozrvpz8s (receiver on 8829), both stopped; 0 listeners on either port. Browser tab closed. Nothing committed, pushed, sent or deleted by the checker.
