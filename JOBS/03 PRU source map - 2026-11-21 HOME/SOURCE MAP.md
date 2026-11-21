# PRU source map

Angie, 2026-11-21. For each file Angie reads for PRU: its path, md5 (first 8 characters), size, sheets, and its survey. What each file holds, and any personal data in it, are in its survey, in `C:\AI_Building\AI_PRU\JOBS\03 PRU source map - 2026-11-21 HOME\surveys\`. A reader agent wrote each survey; its figures are the reader's claim, not checked.

## 1. The v3 log (in use)
- **Path:** `C:\Users\Sergio\.claude\uploads\034bc097-973b-403b-8a90-c7678efdb939\eb48a496-2026_PRU_Manual_Log_v3.xlsx`, md5 37c427cf, 7,109,744 bytes.
- **Sheets:** Master; Ecourse File; 2026 Summary; Copy of 2026 Summary; WklyConsolidating Wd and 2 copies; x2025 v Budget; x2025 Budget; 26 Rent Schedule; 2025 Summary; "2025 "; 2024; 2023; Miscellaneous Income Log; GIFT CARDS; Parameters; New Range To Do; hidden: Sean, WklyConsolidating, Copy of Copy of WklyConsolidati, Sheet24 (survey A says 22 sheets, 3 hidden, but names these 4 as hidden).
- **Survey:** `surveys\A_log SURVEY.md`.
- **Other copies, not in use:** Sergio's order of 2026-11-21, "use the v3 log", is logged against md5 37c427cf (`C:\AI_Building\AI_PRU\LOG.md` line 213).
  - `C:\Users\Sergio\Downloads\2026 PRU Manual Log v3.xlsx`, md5 ab99689d, 6,464,527 bytes. Sheets: 21, the in-use file's without "Copy of WklyConsolidating Wd 1". Survey: `surveys\A_log SURVEY.md`.
  - `C:\AI_Building\AI_Financials\04 Budget\2027\raw files\2 Sales and GP\2026 PRU Manual Log v.3 - saved 2026-11-08.xlsx`, md5 86b02898, 661,808 bytes. Sheets: Copy of 2026 Summary; Copy of WklyConsolidating Wd. Survey: `surveys\A_log SURVEY.md`.

## 2. The GL
- **Path:** `C:\AI_Building\AI_Financials\00 Raw data\GL\2026 YTD 101E GL History Detail Postings - All Accounts.csv`, md5 94ae1ff9, 64,690,471 bytes.
- **Sheets:** one CSV; columns Account, Journal, Date, Doc #, Description, Debit Amount, Credit Amount, Balance, Store.
- **Survey:** `surveys\B_gl SURVEY.md`. Its 785xx total disagrees with the sum of the 785xx accounts it lists; the account sum (Angie's sum) agrees with Rick's 785xx figure at `C:\AI_Building\AI_PRU\LOG.md` line 9 (Piston's pick, item 3).

## 3. Rick's r5 workbook (2027 budget)
- **Path:** `C:\AI_Building\AI_Financials\04 Budget\2027\04 PowerRide University\2026-11-21 PRU and Consolidated Books from the planner - rick RICK-HOME-2bd93960\work\04 PRU GP rebuilt.xlsx`, md5 3717f2bb, 11,705,242 bytes.
- **Sheets:** 61, whole company. PRU's: PRU-pl, PRU GP, PRU (capex), Vs Prior-pru, PRU's row on Master, PRU's column on Consolidating.
- **Survey:** `surveys\C_rick SURVEY.md`.

## 4. Operating Statements 2026-09
- **Path:** `C:\AI_Building\AI_Financials\04 Budget\2027\raw files\3 Operating statements\02 - Operating Statements 2026-09.xlsx`, md5 c2b94972, 4,444,109 bytes.
- **Sheets:** 52, for the group companies named in survey D. PRU's: PRUAct, PRU-Prior, PRUb, PriorYrPRU, CompPRU, PriorQtrPRU, PRU-Detail (hidden).
- **Survey:** `surveys\D_books SURVEY.md`.
- **Also in that folder, not opened:** `C:\AI_Building\AI_Financials\04 Budget\2027\raw files\3 Operating statements\Operating Statements.xlsx`, md5 b7c1ab1c, 4,532,872 bytes. Sheets: not read. No survey of its own; survey D names it.

## 5. 2026 PRU Budget v3 final
- **Path:** `C:\AI_Building\AI_Financials\04 Budget\2027\raw files\1 2026 Budget workbooks\2026 PRU Budget v3 final.xlsx`, md5 c06d1386, 5,294,023 bytes.
- **Sheets:** 22 per survey D, which names 21: Notes; 2026 Summary; 2026 Trend; Jan to Dec; 25Classes; 25Rev; 2025 Sum; 25 Detail; 2024 Sum; 2024 Summary.
- **Survey:** `surveys\D_books SURVEY.md`.

## 6. 2027 PRU Budget (rolled)
- **Path:** `C:\AI_Building\AI_Financials\04 Budget\2027\rolled\2027 PRU Budget.xlsx`, md5 b80e18c8, 5,126,027 bytes.
- **Sheets:** 21: Notes; 2027 Summary; 2027 Trend; Jan to Dec; 26Classes; 26Rev; 2026 Sum; 26 Detail; 2024 Sum; 2024 Summary.
- **Survey:** `surveys\D_books SURVEY.md`.

## 7. Class Data: not a source (low priority)
Sergio, 2026-11-21: Class Data "is not a source file, Angel produced that ... it looks not accurate" (`C:\AI_Building\AI_PRU\LOG.md` line 213).
- **Paths:** in `C:\Users\Sergio\.claude\uploads\034bc097-973b-403b-8a90-c7678efdb939\`:
  - `f32ce509-Class_Data.xlsx`, md5 542d634b, 86,979 bytes.
  - `57ae51b4-Class_Data.xlsx`, md5 bcb6c111, 88,852 bytes.
  - `8c4e186b-Class_Data.xlsx`, md5 19acfe24, 89,113 bytes.
- **Sheets:** 15: nine raw "Demand Analysis" sheets, named in survey E; Northern Sites; Central Sites; Stafford Sites; Newport News; Virginia Beach Site; 2027 Projections.
- **Survey:** `surveys\E_classdata SURVEY.md`.

## 8. Waiting: the REMS custom report
Asked of Angel, one row per class (`C:\AI_Building\AI_PRU\LOG.md` line 210). Not in hand yet.
