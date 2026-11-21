> Reader's survey - figures are the reader's claim, not checked.

# Class Data survey (reader E, Sonnet), saved by Angie from its hand-back, 2026-11-21

## Files (C:\Users\Sergio\.claude\uploads\034bc097-973b-403b-8a90-c7678efdb939\)
- f32ce509-Class_Data.xlsx (in use): md5 542d634b60f1ae711f43206c20ba6503, 86,979 bytes; lastModifiedBy a person's surname, modified 2026-11-20 23:07Z, saved in desktop Excel; 107 formulas, all on 2027 Projections.
- 57ae51b4-Class_Data.xlsx: md5 bcb6c1112062c59610c693c7d4b44f41, 88,852 bytes, zip time 2026-11-20 11:36 (oldest).
- 8c4e186b-Class_Data.xlsx: md5 19acfe248019ef0cd6be7c2754933020, 89,113 bytes, zip time 2026-11-20 12:16.
- The two older ones look like a Google Sheets export (reader's inference). Only 2027 Projections differs between versions (41 cells v1->v2, 72 cells v2->v3): typed totals became formulas, numbers corrected (e.g. 3-wheel 2027 price typo 689 -> 389; 2027 total 485 -> 498 -> 498 with a different split).

## How it was made (clues)
- 14 of 15 sheets are typed values only (pasted, origin unknown); no external links.
- Nine raw sheets titled "Demand Analysis", one row per class, with registration-system fields: WE Date, Course, Home Zone, Site, Loc Id, A/P, Class Days, Limit, # Stud, Fees, Avail Seats, Cap %, Days to Sell, Class Create Dt, Sold Out Date. They look like exports of the school's registration system (likely REMS; not stated). No names.
- 2027 Projections G90:L108: a pasted system report, "Course Summary Report for Dates: 01/01/26 - 12/20/26", by course code: classes, incomplete, failed, passed, total (BRCE 345 classes, 322 incomplete, 271 failed, 2,564 passed, 3,157 total; total 4,121 students, 496 classes). G72:L84 the same for 2025 (4,248 students).

## Sheets
- Raw (Demand Analysis): Manassas 64 classes / 637 students / fees 237,370; Fairfax 34/338/125,584; Woodbridge 57/542/199,933; MM & WB Additional 31/245/79,350; Manassas GMU 33/239/90,961; Colonial Heights 47/474/172,539; Stafford 31/256/95,281; Virginia Beach 60/412/153,275; Clarksburg 65/415/144,727. Total 422 classes, 3,558 students, 1,299,020. Newport News has no raw sheet. Each sheet's own typed Totals and YTD blocks disagree somewhat with its rows; possible typos (VB YTD revenue 13,598; Woodbridge variance 593,932).
- Northern Sites, Central Sites, Stafford Sites, Newport News, Virginia Beach Site: 2027 scenario plans by site and month (classes, students, tuition, coach, rent, contribution), typed.
- 2027 Projections: classes by site and course (2W 417, 3W 55, BRC2 10, First Ride 16 = 498, check cell O28 = 0); monthly grid; 2026 range rent per weekend and storage; coach cost per class (2W 525x2 / 625; 3W 425x2 / 525; BRC2 and ARC 290x2 / 390; First Ride 75; range aid 250, "15 classes in 2026"); prices 2026 -> 2027 (2W and 3W 369 -> 389; BRC2 249; ARC 199; First Ride 99); promotions; Dirt Bike block; note "Keep the 431-class schedule as the baseline" (does not match 498); "Classes For Each Site as of 11/20/26": 448 classes / 3,745 students (Clarksburg not listed).

## 2026 class counts inside the file disagree
- Raw rows: 422 classes, 3,558 students. "Classes For Each Site": 448 / 3,745. Course Summary Report: 496 classes / 4,121 students. Northern Sites 2026 columns: 203 / 2,001 for 4 sites. None reconciled in the file. (v3 log: 573 class codes, 4,606 students.)
- 2026 by month (raw rows, classes/students): Jan 5/29; Feb 18/59; Mar 55/514; Apr 45/422; May 54/526; Jun 53/447; Jul 46/401; Aug 45/393; Sep 35/297; Oct 31/221; Nov 28/221; Dec 7/28.

## 2027 projection by month (2W/3W/BRC2/First Ride = all)
Jan 7/0/0/0=7; Feb 15/2/0/0=17; Mar 51/5/0/1=57; Apr 48/5/1/2=56; May 56/6/3/2=67; Jun 51/8/1/2=62; Jul 44/6/1/4=55; Aug 45/8/2/2=57; Sep 35/5/0/2=42; Oct 30/6/1/1=38; Nov 25/3/1/0=29; Dec 10/1/0/0=11; year 417/55/10/16 = 498.

Names: none (no student, staff or coach names). Reader's mistakes: first pass read openpyxl default properties as real (corrected); one column pair in Northern Sites does not add (199 vs 200), not investigated.
