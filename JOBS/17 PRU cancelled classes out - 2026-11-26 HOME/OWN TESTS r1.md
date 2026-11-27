# Job 17 r1: Angie's own tests (2026-11-26). Not a verdict; only Sergio accepts.

Bench: `C:\AI_Building\AI_MISC\06 Benches\2026-11-26 PRU cancelled classes out - ANGIE-HOME-J17\`. Class data: Sergio PRU Class Data.xlsx, md5 281b2239, as on the job 15 bench.

## The goal-classes check
- Program 76547112 to 836a8ed8 (15,206 bytes); test b42c01c6 to 2b3c6147 (25,102 bytes), on the bench; the skill folder still holds 76547112.
- TEST: PASS, 64 ok (`test_run1.txt`). The new test run on the old program 76547112: TEST: FAIL on exactly its 3 new asserts (`old program\test_on_old.txt`).
- His 2027 file: rows counted 530 to 521; 9 cancelled left out; every range's limit unchanged; RESULT: STOP, Woodbridge April 13 > 12, as before.

## The PRU Dashboard (job 15 page)
- The bench copies rebuild the live page byte for byte: 66fa1545 (`dashboard\page_before.html`).
- Changed, after his 55 "Keep their fees": pru15_count.py 16d75431 to ecf4687d, pru15_build.py cd4f4f87 to b999cf4a, pru15_page.html c728ad47 to dbe575dc (j17_page_edit.py, then the Fees source line), pru15_tests.py 727e365a to 30f6c17e, j17_tests.py to 890a2bf0. New page `dashboard\page_after.html`, a59e5742, 179,153 bytes, built 2026-11-26, as of week 47 (counts_after.json f2b8bcb1).
- Classes 616, 623, 531 to 595, 602, 522 (21, 21, 9 out). Students and every student-sheet figure unchanged. Fees, whole year, unchanged: $1,532,390, $1,535,475, $1,588,136 (pru15_count.py's print).
- One 2024 range and one 2024 class type had only cancelled classes with fees: they show 0 students, 0 classes and their fees.
- j17_tests.py: TEST: PASS. 282 class figures equal pru15_tests.py's own count from the workbook (cancelled out, their fees kept), 0 off; every class row's fees unchanged. Planted: same counts twice, FAIL (stops on the missing cancelled count); fees taken off the fee-only rows, FAIL (19 rows, 30 figures off).
- Superseded: the first build a5594b7a, which dropped cancelled fees (before his 55); and a59e5742 (fees kept, blind check r1 PASS), kept on the bench as `*_r1fees.*`, before his 58.

### After his 58, student rows of cancelled-only slots out (2026-11-26)
- pru15_count.py to c8f43289, pru15_tests.py to 3e655c25, pru15_page.html to b40cca78 (the student-sheet source line says these rows are left out), j17_tests.py to 85f27fbf. Page `dashboard\page_after.html` 0fcfb06e, 177,750 bytes; counts_after.json c76bfcf3.
- Student rows left out: 26, 17, 8 (2024, 2025, 2026), equal to the blind checker's own count. Pass and fail counts unchanged (pru15_count.py's print). Classes and fees as above.
- j17_tests.py: TEST: PASS. 809 figures (class figures plus student rows, tested and pass rate by coach and range) equal pru15_tests.py's own count from the workbook, 0 off. Student rows only taken away. "No coach marked I" and "two coaches marked I" counts only fall, by no more than the rows left out. Planted: one left-out row put back in the count, FAIL; the r1 counts as after, FAIL (16 off); same counts twice, FAIL (stops).
- pru15_tests.py: 0 student names, emails, phones, licences or dates of birth on the page.
- The page's code passes node --check; its two data blocks are JSON, not code.
- Not done: the page was not opened in a browser (the pane does not run local files).

## The PRU 2027 Planner
- Its 2026 class figures come from the Manual Log's Master, one row per student booking (job 03 survey A). The Downloads copy is gone; read instead: the Google Sheet "2026 PRU Manual Log v3" (his 54), Master, header row only. No status or cancel column. My first claim, "a class with no students has no booking row, so it is already out", is WITHDRAWN: the blind checker found the Sergio sheets keep booking rows for cancelled classes, so Master may too. Tested after his 59: the Google Sheet exported to the bench (`manual log\2026 PRU Manual Log v3.xlsx`, md5 76f72b92), counted by `master_cancelled.py`, matching Master's 2026 class codes to 2026 Demand Analysis by week ending, site, course, D and A/P. Master 2026: 574 classes, 4,618 bookings. 2 classes (2 bookings) sit in a cancelled class only, so the planner counts them: it needs a change. 511 classes (4,421 bookings) match a live class exactly, 13 (93) match a live class by week, site and course, and 48 (102) have no Demand Analysis row, so I cannot tell if they were cancelled.
