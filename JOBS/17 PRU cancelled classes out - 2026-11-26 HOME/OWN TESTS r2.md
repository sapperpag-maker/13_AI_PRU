# Job 17 r2, the planner: Angie's own tests (2026-11-27, full-auto run). Not a verdict; only Sergio accepts.

Bench: `C:\AI_Building\AI_MISC\06 Benches\2026-11-26 PRU cancelled classes out - ANGIE-HOME-J17\planner\`. Decisions made in his place: `DECISIONS.md` there (D1 to D4).

## The build
- Base: the live planner, job 14, `job14 410b33df.html`, copied to the bench as `page_before.html`. The job 17 plan named 926ab8a8, which is wrong: the live page is 410b33df (DASHBOARD MAP, row pru-planner).
- `j17_planner.py` (624e6e02) builds `page_after.html`, bc617b5e, 157,940 bytes. It changes 13 numbers in the page's data and adds 1 key to the default plan:
  - The 2 classes in cancelled-only 2026 classes (Newport News 2-Wheel, January; Woodbridge First Ride, April; 1 booking each) leave master26.fill and r3.fill26 (1 class and 1 student each), classes2026 (January and April, 1 each), master26.lines (1 student each) and src-data (IME, All Locations, April, 1 student).
  - No fee moved anywhere (his 55).
  - The default plan gets Woodbridge First Ride April 2027 = 0 (his words, 2026-11-26).
- step1.txt: the v3 log and the page agree on Newport News January (2 classes, 7 students). On Woodbridge First Ride April they don't: the page has 4 classes, v3 has 3, both with 7 students. See D1.

## Tests (`j17_planner_tests.py` 48090cc7, `tests.txt` 73ead662): TEST: PASS
- The page's code and text outside the data are byte-equal to 410b33df.
- Exactly the 13 intended numbers moved, each by 1, and no fee moved.
- The default plan has only the one key added.
- The download with nothing saved, at http://localhost:8817 with browser storage cleared: Woodbridge First Ride April 1 to 0, and Woodbridge's April range total 13 to 12. Class rows moved only on the Woodbridge tab and the Summary.
- SELFTEST worst 7.28e-12, before and after. The console shows no error after a fresh load and all 4 tabs.
- Plants (`plants.txt`), each FAIL: one class left in; April at 1 in the default plan; the before download given as the after.

## The goal check on the new default plan (`goal_check.txt` ef051574)
- Check 4, the month test: 0 months over, PASS. On his own goal file it was 1 over, Woodbridge April 13 > 12.
- RESULT: still STOP, on check 1: 16 cells are half classes (First Ride 0.5 in March and October, Manassas Mall and Woodbridge, and the totals that carry them). His own goal file has the same 16. See D4 and the mistake form of 2026-11-27.

## 2027, before and after (`sales_gp.csv` 941ed6a6, from the Summary sheet of each download)
- Classes 609 to 608. Students 5,091.42 to 5,088.66.
- Total sales $2,011,581.60 to $2,011,303.41 (-$278.19).
- Gross profit $1,404,211.60 to $1,404,008.41 (-$203.19).
- After income taxes $238,565.12 to $238,778.71 (+$213.59).
- March, September and October rise by a few dollars: the 2026 fill for First Ride, which 2027 reads, went up when the 1-student class left.
