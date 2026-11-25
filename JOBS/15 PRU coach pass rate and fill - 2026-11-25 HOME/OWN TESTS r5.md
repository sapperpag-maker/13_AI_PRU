# Job 15 r5: Angie's own tests (2026-11-25). Not a verdict; only Sergio accepts.

Piece: `C:\AI_Building\AI_PRU\JOBS\15 PRU coach pass rate and fill - 2026-11-25 HOME\job15 66fa1545.html`, md5 66fa1545e7f5e09f7f9c6b06d86f9b0a, 179,233 bytes. It repairs r4 (8f785eb9).
r4's blind check: ANGIE-HOME-J15D, `C:\AI_Building\AI_MISC\06 Benches\2026-11-25 PRU job 15 r4 blind check - ANGIE-HOME-J15D\VERDICT.md`, md5 f16f1141, first line FAIL, one wording finding. Its TIEOUT.md, md5 c42581ae, first line PASS: 214,603 figures, 0 off.
Sergio's answers, relayed by Piston from Piston's chat, 2026-11-25:
- 38, "Fix the line, then LAWYER (Recommended)": the full coach line in the 6 places, no more blind rounds, straight to LAWYER.
- 39, "Remember their choice (Recommended)": dark the first time, then whatever the viewer picked.
- 40, the 7 student rows sharing a coach's name: "Fine as is (Recommended)".
Bench: `C:\AI_Building\AI_MISC\06 Benches\2026-11-25 PRU weekly dashboard - ANGIE-HOME-W25\`. pru15_page.html is now c728ad47, made by pru15_r5_edit.py; r4's copy is pru15_page_r4.html. counts.json is unchanged, cca3be7b.

## What changed from r4
- The two source strings behind the 6 places now read: credited to the main coach, the one marked I; where two coaches are marked I, the one in the first Instructor column; where none is marked I, the coach in Instructor 1; rows with no coach in any Instructor column show as (no main coach).
- Theme (his 39): no change needed. r4 already kept the viewer's pick in the browser and opened dark when there was none. Tested below.

## Tests
1. **Only the line changed: PASS.** pru15_r5_diff.py takes r4 (8f785eb9), puts the new line in place of the old, and the result equals r5 byte for byte. The old line is in r4 twice and in r5 0 times; the new line is in r5 twice. So every figure is r4's, which the r4 checker tied out at 0 off.
2. **The 6 places: PASS.** In the browser, with nothing picked, the new line shows 2 times on Overview, once on Students and 3 times on Coaches: 6 in all. The old line shows 0 times. Each tab has 0 quote marks.
3. **Theme: PASS.** With nothing stored, the page opens dark. After a click on Light, it reloads light. After a click on Dark, the stored pick is dark again.
4. **Re-count and student data: PASS.** pru15_tests.py re-counts 810 figures from the workbook, and 0 differ from site/expected.json. 0 of 13,405 names, 13,449 emails, 13,425 phones, 13,483 licence numbers and 8,775 dates of birth are in r5. Correction after LAWYER's note (748c9cf8): the name test searches my list of student name pairs; a plain search does find a few students whose full name is also a coach's name shown on the page. Those are coach names, allowed by his Q20 and by his answer 40, "Fine as is (Recommended)".
5. **Same input, same page: PASS.** Two builds from counts.json cca3be7b both give 66fa1545. The page is pure ASCII (0 other characters). The console shows no error.

## Not tested here
No fifth blind round, on his answer 38. Phone width was not checked again: the layout code is the same as r4's, which the r4 checker read at a true 375 px.
