# GOAL - job 01 release 3: the PRU 2027 Sales Planner on Sergio's Class Data

DRAFT, Angie, 2026-11-20. Put to Sergio for his yes (R-1879). It replaces release 2's goal, which stays in this folder for the record. Every input is his file or his words in Angie's chat on 2026-11-20 (logged in `C:\AI_Building\AI_PRU\LOG.md`). Lines marked **my pick** are Angie's choices where he has not ruled; each is his to strike.

## Sources
- **Manual Log:** the file he attached, `2026_PRU_Manual_Log_v3.xlsx`, md5 37c427cf. His words: "we only have 1 version,,attached". Sheets "WklyConsolidating Wd" (students and $ by range, class and month) and "Master" (class codes, sites and courses only; no customer fields).
- **Class Data:** `Class_Data.xlsx`, md5 19acfe24, tab "2027 Projections". His words: "tab 2027 projection has the target number"; Q24: "498 table is the correct one".
- **Rick's workbook:** `C:\AI_Building\AI_Financials\04 Budget\2027\rolled\02 - Consolidated SGP Budget light.xlsx`, sheet PRU-pl.

## What the finished page shows
1. **Trends** as in release 2: 2022-2026 by range, class and month, read from the attached log.
2. **2027 classes:** his 498, by site and class type (2027 Projections A1-F11), by month (rows 31-39 for 2-Wheel, 44-52 for 3-Wheel, 57-65 for BRC2, and E15-E26 for First Ride). There is no Waldorf ("Waldorf range is out for 2027 at the moment"). Each cell can be edited.
3. **2027 students = 2027 classes × students per class.** Students per class = each site and type's 2026 students (log) / its 2026 classes (Master), editable. A fill-rate change % replaces the growth %. **My pick** (Q28 was not answered).
4. **2027 prices:** 2-Wheel $389, 3-Wheel $389 (his Q25: "Typo, use $389"), BRC2 $249, ARC $199, First Ride $99 (2027 Projections M17-M21), each editable. **My pick:** First Ride = the log's IME class ($99). HD and ARC, which have no classes in his table, are carried at their 2026 students × price.
5. **Discounts:** Military $36 and VIP $50 on 2-Wheel BRC, with 393 and 177 claims in 2026 ("these are the discounts we applied through the year"). **My pick:** shown at the 2026 claim rate for information only, and not subtracted again, because the log's 2026 2-Wheel average of $358.14 is below the $369 list price (Q29 was not answered).
6. **Rick's 2026 as the 2026 base** and the five gap rows, named as in Q23 (Q27: "no need to rename"). In 2027, Loss Damage Waiver = 1.9436% of class fees (his words: "LDW just figure a % to sales ad keep it"; $26,518.37 / $1,364,378.50, Jan-Sep 2026, Rick's table). **My pick:** the other four parts are carried at their 2026 amounts. Oct-Dec 2026 stay Rick's estimate, and October becomes actual once its books are final (his answer 4).
7. **Coach cost (Salaries & Wages, row 33)** = each 2027 class × its type's cost (2027 Projections H15-J22): one coach (column J) where students per class are 6 or fewer, two coaches (column I) where more. His Q26: "Cost varies by student, up to 6 and more than six." Range aid is $250 a class; **my pick:** 15 classes, as in 2026 (Q31 was not answered).
8. **Rent (row 72)** = each range's 2027 classes × its weekend rate, using the 2027 renewal where one is given (Woodbridge $950, Clarksburg $725), plus annual storage / 12 (Woodbridge $2,500, Manassas Mall $7,800, Clarksburg $1,800). His words: "thhis are going to be rent rates for next year". Each rate can be edited.
9. **2027 Budget P&L** as in release 2: Training = 2027 sales + the gap parts; every other line follows release 2's rule (his answer 11, "Hold fixed costs"); totals are recomputed.
10. **2027 vs 2026** as in release 2.
11. **New initiatives:** Dirt Bike classes, 24 classes × 6 students × $289 = $41,616 in sales, rent $500 and coach $200 (2027 Projections N2-O8). Shown on its own and **never flowing into the P&L** (his words: "keep it separate for now, we need to present to Richard, don't make these numbers flow into P&L").
12. Light and dark themes in Piston's colours. Every Manual Log figure is labelled Manual Log.

## The test
1. 2027 classes on the page = 498, and each site and type cell equals 2027 Projections.
2. With every input at its start value, 2027 sales = the sum over site, type and month of classes × students per class × price, to the dollar.
3. Coach cost = the sum over classes of the right column-I or column-J cost, recomputed independently.
4. Rent = the sum of classes × rate + storage / 12, each month.
5. LDW 2027 = 1.9436% × 2027 class fees.
6. Dirt Bike changes no P&L cell: the P&L is the same with it shown or hidden.
7. The P&L totals equal the sums of their lines; fixed lines equal Rick's.
8. Each test fails on a planted fault before it is believed.

Then: my own test, one blind check by an agent that did not build it (R-1875), LAWYER (R-1877), Sergio's accept, and the Brain puts it live.
