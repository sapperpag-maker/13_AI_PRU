> Reader's survey - figures are the reader's claim, not checked.

# GL survey (reader B, Sonnet), saved by Angie from its hand-back, 2026-11-21

File: C:\AI_Building\AI_Financials\00 Raw data\GL\2026 YTD 101E GL History Detail Postings - All Accounts.csv
- md5 94ae1ff9841d3de6bc9903402e32874b, 64,690,471 bytes, modified Oct 28 17:35. UTF-8 no BOM, comma, 874,156 data rows + header, 9 fields every row.
- Header: Account | Journal | Date | Doc # | Description | Debit Amount | Credit Amount | Balance | Store ("Account ", "Journal ", "Store " carry a trailing space).
- 2,498 rows with no Date and no Store (counted, not read).
- Stores (rows): FC1 291,998; WB1 271,708; RPS 197,029; BYP 96,663; POW 10,250; PR1 4,010; blank 2,498.
- Dates m/d/yyyy, 1/1/2026 to 10/28/2026; October partial. No 46xxx sales rows in October.
- POW journals: Payroll 6,374; Repeating 1,644; Accounts 819; GL Batch 720; MANUAL JE 641; Bank 42; Debit Memo 4; Credit Memo 4; blank 2.

## POW, accounts -30 (119 accounts; grand net +288,106.42)
Sales 46xxx (net credit, YTD): 46001 205,340; 46002 178,494; 46006 129,983; 46008 176,389; 46009 79,736; 46011 112,131; 46012 116,910; 46014 78,396; 46018 102,870; 46101 21,424; 46102 16,806; 46106 23,183; 46108 5,563; 46112 16,966; 46114 18,025; 46118 17,461; 46201 21,179; 46202 12,780; 46206 2,073; 46350 6,534; 46400 22,135.50; 46450 8,323.95. Zero all year: 46013, 46016, 46109, 46111, 46113, 46116, 46205, 46209.
- 460xx, 461xx, 462xx look like course-type blocks; last two digits look like the site. Account names are not in the file (needs a chart of accounts).
- 47700 LDW +26,518.37 (mirrors 67700 -6,629.60 and non-suffix 34148 +6,629.60).
Cost of Sales 66/67xxx (debit): 660xx/661xx mirror 460xx/461xx by last two digits, one row a month. 66001 -52,746.25; 66002 -46,477.50; 66006 -31,525; 66008 -40,325; 66009 -19,775; 66012 -26,650; 66013 -30,787.50; 66014 -21,505; 66018 -23,125; 66101 -5,312.50; 66102 -5,100; 66106 -5,550; 66108 -2,550; 66112 -3,875; 66114 -5,587.50; 66118 -4,000; 66201 -580; 66300 -7,023.50; 66400 -6,850; 66450 -2,800; 66600 -8,590; 67700 -6,629.60.
Expenses: largest 72200 -194,947.92 (223 rows, has October); 78000 -53,258.31 (about -5,860 a month, likely rent); 78200 -39,067.56; 71350 -36,075.03; 72500 -37,120.28 (1,599 rows); 785xx block -147,761 approx (78502 -31,450; 78506 -15,071.65; 78508 -23,400; 78511 -21,875; 78512 -17,199; 78513 -9,350; 78514 -8,500; 78518 -15,015; 78521 -2,400; 78545 -3,000); others in the bench output (o.pkl).
POW without -30: 79600 -16,163.00; 79900 -78,740.58; balance-sheet accounts 2xxxx/3xxxx (34146 +9,000 and 34148 +6,629.60 offset 71460-30 and 67700-30).

## What it can and cannot tell PRU
- Can: monthly POW P&L by account, Jan to Oct 2026; sales by account (course type and site, by number); cost of sales paired to sales.
- Cannot: revenue by class or coach; coach pay by coach; students, fill or pass rates; weekly cost (cost of sales posts once a month). Description and Doc # not read (may name people).
- Store PR1 (4,010 rows) not examined.
Reader's mistakes: NONE (no GL line or free text printed).
