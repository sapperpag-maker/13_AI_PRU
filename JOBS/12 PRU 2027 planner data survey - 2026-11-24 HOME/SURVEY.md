# Survey of `H:\Shared drives\PRU ANALYSIS\2027 Planner data` (2026-11-24, Angie, HOME)

His words, 2026-11-24, in Angie's chat: "survey this data now: \Shared drives\PRU ANALYSIS\2027 Planner data".

Read-only. Both files copied to the bench `C:\AI_Building\AI_MISC\06 Benches\2026-11-24 PRU planner data survey - ANGIE-HOME-W24\data\` and read there with openpyxl (survey.py, check2.py, check3.py; outputs survey_out.txt, check2_out.txt). Every count below was counted by those programs this session. No student value is written here.

## The folder

2 files, 0 subfolders, both saved 2026-11-24 about 12:58:

| File | Bytes | md5 | Sheets |
|---|---|---|---|
| PRU Student_Class Data 2024 to 11-24-26.xlsx | 3,452,750 | 88a3caea | 2024, 2025, 2026 |
| Sergio PRU Class Data.xlsx | 4,600,993 | 281b2239 | Sergio 2024/2025/2026, 2024/2025/2026 Demand Analysis, 2024/2025/2026 Recap |

The three student sheets are the same in both files: 2025 and 2026 equal cell for cell; 2024 differs only by trailing empty cells (5,123 rows longer in Sergio's copy), no value differs. So Sergio's file = the student file + 6 more sheets.

## Kind 1: one row per student registration (sheets 2024, 2025, 2026)

Title row: "Student Info: For All Courses, For All Sites, For All Statuses, For All Discount Codes" (a REMS-style export). 37 columns.

| Year | Rows | Classes (Class Code) | First Date range | Fee total | I-PASS | I-FAILSKILL | I-DROPX | N-NOSHOW | N-CANCEL | no status |
|---|---|---|---|---|---|---|---|---|---|---|
| 2024 | 5,146 | 621 | 2024-01-13..2024-12-21 | $1,532,440.00 | 3,932 | 299 | 351 | 194 | 195 | 0 |
| 2025 | 4,687 | 641 | 2025-01-11..2025-12-20 | $1,536,036.00 | 3,588 | 316 | 355 | 152 | 135 | 0 |
| 2026 | 4,705 | 552 | 2026-01-10..2026-12-27 | $1,590,224.00 | 3,425 | 280 | 404 | 175 | 132 | 155 |

Useful columns: Class Code, Course Code (BRCE, BRCEM, 3WBRE, 3WBRM, BRC2W, BRCR, ARC, SKRT, IME, ...), First Date, Site (11 to 14 codes: MANMALL, WOOD, COLONIAL, NEWPORT, MANGMU, VABEACH2, FAIRFAX, CLARKSBG, WALDORF, ...), Status (I-PASS, I-FAIL*, I-DROPX, N-*), WS and SS (scores), Fee, Disc Code, Promo Code, Heard About Us, Experience, Instructor 1, 2 and 3.

**Personal data:** the same rows carry first and last name, date of birth, driver's licence number and state, address, email and phone. These must not leave the sheets into any page, report or agent prompt.

2026 holds classes into December (dates to 2026-12-27), so its last weeks are registrations, not results: 155 rows have no status.

## Kind 2: one row per class (2024, 2025, 2026 Demand Analysis)

21 columns: week-ending date, Course, Home Zone (NORTHERN, EASTERN, MARYLAND, CENTRAL, WESTERN), Site, weekend or weekday, Class Days, First Day of Class, Limit (seats), # Stud, Fees, Avail Seats, Cap %, Class Create Dt, Sold Out Date, Sold Out Days. Each sheet ends with one total row (no course).

| Year | Class rows | Seats (Limit) | Students | Fees | Class rows with no Limit | Sold out (rows with a date) |
|---|---|---|---|---|---|---|
| 2024 | 654 | 5,971 | 4,684 | $1,532,390.00 | 49 | 193 |
| 2025 | 739 | 5,898 | 4,330 | $1,535,475.00 | 128 | 185 |
| 2026 | 584 | 4,985 | 4,388 | $1,588,136.00 | 58 | 227 |

The total row equals the sum of the class rows in all 3 years (seats, students, fees).

## Kind 3: one row per class reported (2024, 2025, 2026 Recap)

14 columns: transaction number and date, Return Id, Class Code, Start and End Date (stored as numbers like 1132024, not dates), Course, Site No (a number, 1 to 25, not the site code), # Students, Instructor 1 and 2. RA 1 and RA2 are empty.

| Year | Rows | Students | Transaction dates |
|---|---|---|---|
| 2024 | 566 | 4,541 | 2024-01-05..2024-12-30 |
| 2025 | 552 | 4,236 | 2025-01-02..2025-12-30 |
| 2026 | 207 | 1,742 | 2026-01-07..2026-11-23 |

2026 Recap is far short of 2026 Demand (207 against 584 classes). A Recap row is a class reported to the state: Sergio, question 3, 2026-11-24, "Classes reported to the state". Why 2026 has so few reported by 11-23 is not known.

## What it can feed (his weekly trends)

- **Coach pass rate:** students by Instructor with Status I-PASS against I-FAIL*: yes, 2024 to 2026.
- **Class fill rate:** Limit against # Stud per class, by week: yes (Demand Analysis); 49, 128 and 58 class rows have no Limit.
- **Class and range revenue:** Fees per class and Site: yes. Not profit: no coach pay, rent or cost in these files.
- **Number of students by week:** yes, from either kind.
- This looks like the per-class REMS report on TO DO (asked of [A.] on 2026-11-21). Whether it is that report is NOT KNOWN.

## Gaps and things that do not match (not checked further)

1. Fees: the student rows and the Demand total differ by $50.00 (2024), $561.00 (2025) and $2,088.00 (2026).
2. Students: Demand # Stud (4,684 / 4,330 / 4,388) differs from Recap (4,541 / 4,236 / 1,742) and from the student rows (5,146 / 4,687 / 4,705, every status counted).
3. Recap's Site No is a number; no table here maps it to the site codes.
4. Course codes grow over the years (8, 11, 12 in the student rows); new ones in 2026 are IME, REPLC, RESCH, BRCES, BRCSA, BRC2P.
5. None of this was tied to the GL or to the v3 Manual Log the planner uses today.
