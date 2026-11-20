# PRU 2026 sales: source, categories by month, and rebuild steps (for Angie)
From Rick HOME (RICK-HOME-2bd93960), 2026-11-20. Found by Rick's read-only agent; these are the agent's figures, not re-derived by Rick. The Jan-Sep totals agree with LAWYER's FINDINGS.md (C:\AI_Building\AI_MISC\06 Benches\2026-11-20 PRU sales why differ - LAWYER-HOME-1118\).

**Bottom line.** 02 PRU-pl AB13 = $1,651,117.18. It is Jan-Sep actuals of $1,399,220.82 plus an Oct-Dec forecast of $251,896.36, and all of it sits in row 121 (Training).
- Rows 116-120 (Major Units, Parts, Accessories, Service, F&I) are typed zeros.
- Each month Jan-Sep ties to the cent across three places: the GL, Operating Statements PRUAct row 13, and PRU-pl row 121.

## Files
- 02 workbook: C:\AI_Building\AI_Financials\04 Budget\2027\rolled\02 - Consolidated SGP Budget light.xlsx, sheet PRU-pl.
- Operating statements 2026-09: C:\AI_Building\AI_Financials\04 Budget\2027\raw files\3 Operating statements\02 - Operating Statements 2026-09.xlsx, sheets PRUAct and PRU-Prior (md5 c2b94972).
- 2025 statement: ...\raw files\3 Operating statements\Operating Statements.xlsx, sheet PRUAct.
- GL: C:\AI_Building\AI_Financials\00 Raw data\GL\2026 YTD 101E GL History Detail Postings - All Accounts.csv (94ae1ff9). Last date 2026-10-28; no POW 46xxx or 47700 lines from October on.
- GL account names: C:\AI_Building\AI_Financials\01 Financial Statements\out\inputs\2026-07\00 - LS CSV Reports\PL PRU 07.26.csv.

## By category and month, store POW, net = credit minus debit
| Category | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Jan-Sep |
|---|---|---|---|---|---|---|---|---|---|---|
| 2-Wheel 460xx | $14,469.00 | $56,399.00 | $169,675.00 | $160,793.00 | $207,857.00 | $161,107.00 | $145,307.00 | $151,760.00 | $112,882.00 | $1,180,249.00 |
| 3-Wheel 461xx | $0.00 | $1,723.00 | $13,202.00 | $11,368.00 | $15,516.00 | $21,430.00 | $18,471.00 | $20,409.00 | $17,309.00 | $119,428.00 |
| Advance Rider/BRC2 462xx | $0.00 | $0.00 | $3,585.00 | $9,852.00 | $7,205.00 | $5,883.00 | $3,468.00 | $6,039.00 | $0.00 | $36,032.00 |
| IME 46350 | $0.00 | $0.00 | $0.00 | $1,386.00 | $1,683.00 | $396.00 | $891.00 | $792.00 | $1,386.00 | $6,534.00 |
| HD Academy 46400 | $0.00 | $0.00 | $6,864.00 | $6,864.00 | $7,293.00 | $0.00 | $1,114.50 | $0.00 | $0.00 | $22,135.50 |
| Other training 46450 | $285.00 | $90.00 | $905.00 | $1,455.00 | $1,278.95 | $1,360.00 | $1,280.00 | $995.00 | $675.00 | $8,323.95 |
| LDW 47700 | $798.61 | $1,948.28 | $6,773.26 | $8,519.82 | $5,453.49 | $1,058.34 | $894.49 | $529.17 | $542.91 | $26,518.37 |
| **Total** | $15,552.61 | $60,160.28 | $201,004.26 | $200,237.82 | $246,286.44 | $191,234.34 | $171,425.99 | $180,524.17 | $132,794.91 | $1,399,220.82 |

## Accounts, Jan-Sep
- **2-Wheel BRC:**
  - 46001 Manassas $205,340.00
  - 46002 Woodbridge $178,494.00
  - 46006 Colonial Heights $129,983.00
  - 46008 Newport News $176,389.00
  - 46009 Manassas GMU $79,736.00
  - 46011 Waldorf (the log calls it Fairfax) $112,131.00
  - 46012 Virginia Beach $116,910.00
  - 46014 Stafford $78,396.00
  - 46018 Clarksburg $102,870.00
- **3-Wheel BRC:**
  - 46101 Manassas $21,424.00
  - 46102 Woodbridge $16,806.00
  - 46106 Colonial Heights $23,183.00
  - 46108 Newport News $5,563.00
  - 46112 Virginia Beach $16,966.00
  - 46114 Stafford Airport $18,025.00
  - 46118 Clarksburg $17,461.00
- **Advance Rider:**
  - 46201 Manassas $21,179.00
  - 46202 Woodbridge $12,780.00 (it posts $3,585 in both March and April)
  - 46206 Colonial Heights $2,073.00
- **Accounts that net to $0 every month:** 46013, 46016, 46109, 46111, 46113, 46116, 46205, 46209. 46300 has no postings.

## Oct-Dec forecast (row 121)
Each month is the 2025 month x 1.012974452, rounded to the cent. The factor = 2026 Jan-Sep $1,399,220.82 / 2025 Jan-Sep $1,381,299.22 (PRU-Prior G13 + L13 + Q13).

| Month | Cell | 2025 source | Forecast |
|---|---|---|---|
| Oct | S121 | PRU-Prior S13 $115,539.03 | $117,038.09 |
| Nov | T121 | T13 $90,177.08 | $91,347.08 |
| Dec | U121 | U13 $42,953.89 | $43,511.19 |
| Q4 | V121 | | $251,896.36 |

The forecast is on the total only, never by category.

## Who wrote row 121
- **Program:** C:\AI_Building\AI_Financials\04 Budget\2027\scripts\fs_budget_targets.py, function build_plan, section "1. prior blocks", lines 216-315.
  - Months 1-9: from PRUAct.
  - Months 10-12: 2025 x factor.
  - Values are written as round(val, 2).
- **Run:** LEDGER.md line 50, on 2026-11-03.
- **Rule:** TARGETS PLAN - plus 5 percent.md, lines 74-76.
- **Note:** 2027 October (PRU-pl S13) is built from the log's October 2025 $112,470 x 1.05. That is a different source from row 121's October, and a fix is pending with Sergio.

## Steps to rebuild it yourself
1. Open the GL CSV. Keep Store = POW, accounts 46xxx-30 and 47700-30. Use only Account, Journal, Date, Debit and Credit.
2. For each line, net = Credit - Debit. Put it in the month of its Date.
3. Group the accounts: 460xx 2-Wheel, 461xx 3-Wheel, 462xx Advance Rider/BRC2, 46350 IME, 46400 HD, 46450 Other, 47700 LDW.
4. Sum by category and month for Jan-Sep. The totals should match the table above (Jan-Sep $1,399,220.82).
5. Tie each month to 02 - Operating Statements 2026-09.xlsx, sheet PRUAct, row 13 (Y13 $1,399,220.82). Any difference means a missed account or the wrong store; stop and find it.
6. Take 2025 from PRU-Prior row 13:
   - Jan-Sep = G13 + L13 + Q13 = $1,381,299.22.
   - Oct, Nov and Dec are S13, T13 and U13.
7. Factor = step 4's Jan-Sep / step 6's Jan-Sep = 1.012974452.
8. Forecast = each 2025 month x the factor, rounded to the cent. Q4 = $251,896.36.
9. Year = $1,399,220.82 + $251,896.36 = $1,651,117.18.
10. Tie check:
    - Each month equals PRU-pl D121..U121.
    - The quarters equal G/L/Q/V121: $276,717.15, $637,758.60, $484,745.07, $251,896.36.
    - The year equals Y121 and AB13.
11. Once October books, and Sergio decides it should be actual, the October GL replaces the forecast.

## "Not in the Manual Log", Jan-Sep (LAWYER's split)
- Truly missing from the log: LDW $26,518.37 + Other $8,323.95 = $34,842.32.
- The log's empty January (classes): $14,469.00.
- Class fees above the log, Feb-Sep: $15,204.50. See C:\AI_Building\AI_MISC\07 Trash - agents empty their own\2026-11-20 PRU classes log vs GL - RICK-HOME-2bd93960\REPORT.md.
- Oct-Dec: the forecast against the log's bookings.
