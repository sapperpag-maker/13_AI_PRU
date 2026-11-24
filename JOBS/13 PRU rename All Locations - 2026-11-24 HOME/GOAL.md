# GOAL - job 13: rename the "All Locations" tab (ACCEPTED: Sergio, question 5, 2026-11-24, in Angie's chat: "Yes")

His words, 2026-11-24, in Angie's chat, question 4: "Rename it". The question was whether to rename the "All Locations" tab so it can't be taken for the total. He asked because the Classes chart there showed 2 classes for 2027B, which is ARC only.

## What the finished page shows

1. The tab now reads **ARC, BRC2, IME and Other** wherever the page shows that name: the tab button, chart titles, table labels, notes, and the Excel download's sheet name and cells.
2. Every figure stays the same as the live page r8 (926ab8a84c26fd7c009e036aab63da28).
3. The page keeps its inside key "All Locations". Edits saved in r8, whether in the browser or in a downloaded edits file, open unchanged.

## The tests that say it shows it

1. Open every tab under each of Students, Sales $ and Classes. The page's visible text contains "All Locations" nowhere. The new name appears on the tab button.
2. Make the Excel download from r8 and from the new page with the same plan. After the old name is swapped for the new one, every sheet and every cell is equal. The only difference allowed is the "Downloaded" time line.
3. Save a draft holding edits in r8, then open the new page in the same browser. The draft loads, and every figure is equal to r8 with that draft.
4. The page's own self-test passes, and the browser console shows no error.
