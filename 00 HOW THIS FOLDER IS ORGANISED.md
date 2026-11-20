# How the Angie folder is organised

Angie is the PRU desk (PowerRide University), opened on his word of 2026-11-19 at HOME. Its own online copy is `sapperpag-maker/13_AI_PRU`, which he creates himself (his answer 53); whether it is made yet is kept in `C:\AI_Building\AI_PRU\TO DO.md`. **Start with `C:\AI_Building\AI_PRU\CLAUDE.md`, then `C:\AI_Building\AI_PRU\ANGIE_SPEC.md`.**

## Every file and folder

| path | what it is for | who writes it |
|---|---|---|
| `C:\AI_Building\AI_PRU\00 HOW THIS FOLDER IS ORGANISED.md` | this page: the folder's map, and where PRU's budget sources live | Angie, in the same act that adds, moves or retires a file here |
| `C:\AI_Building\AI_PRU\CLAUDE.md` | who Angie is, her law, how she works, what she never does; each line with its source | Piston at the opening; after that only on his word |
| `C:\AI_Building\AI_PRU\ANGIE_SPEC.md` | what is known about PRU, each fact with its source | Angie, facts only; the Brain wins where they disagree |
| `C:\AI_Building\AI_PRU\DESK_SETTINGS.md` | the desk's five places for wake-up and goodnight, read by `C:\AI_Building\AI_HQ\04 Tools\Tools\desk_settings.py` | Piston at the opening |
| `C:\AI_Building\AI_PRU\LOG.md` | the desk's log: the only file for notes, quotes and history lines (R-0804) | Angie; the opening line waits for LAWYER's PASS on the desk's files |
| `C:\AI_Building\AI_PRU\TO DO.md` | his jobs waiting their turn, and what each waits on | Angie |
| `C:\AI_Building\AI_PRU\.gitignore` | what the online copy leaves out: Python's cache, this computer's own permissions file | Piston at the opening |
| `C:\AI_Building\AI_PRU\01 Raw data\` | PRU's raw files as they arrive, never edited; `README.md` inside | whoever delivers the file; Angie logs it |
| `C:\AI_Building\AI_PRU\05 His answers and decisions\` | his words and answers for this desk; `C:\AI_Building\AI_PRU\05 His answers and decisions\His words - the desk opened.md` holds his opening words, answers 53 to 59, his later words on what Angie tracks, and answers 61 and 62 relayed by the Conductor | Angie, his words word for word |
| `C:\AI_Building\AI_PRU\JOBS\` | one folder per job, `NN <what> - <date> <machine>`, numbered from 01, each with its goal file, plan and finished builds | Angie |
| `C:\AI_Building\AI_PRU\JOBS\01 PRU 2027 budget dashboard - 2026-11-19 HOME\GOAL.md` | the first job's goal file, a DRAFT for his yes | Angie (written by Piston at the opening) |
| `C:\AI_Building\AI_PRU\.claude\settings.json` | lets Angie's sessions read and write her checkpoints folder | Piston at the opening |
| `C:\AI_Building\AI_PRU\.claude\skills\angie-wake-settings\SKILL.md` | Angie's wake settings, called by `wake-up` and `goodnight` at their step 1 (his answer 54, "PRU folder only") | the Conductor, through `create-a-skill` |

Outside this folder, Angie's own places:

| path | what it is for | who writes it |
|---|---|---|
| `C:\AI_Building\AI_MISC\05 Checkpoints\Angie Checkpoint\` | Angie's checkpoints; `README.md` inside | Angie; saved with `C:\AI_Building`'s own copy |
| `C:\AI_Building\AI_MISC\06 Benches\` | one bench folder per job while it is in use, named with date, job and tag (R-0448, R-0449) | Angie |
| `C:\AI_Building\AI_MISC\07 Trash - agents empty their own\` | where a bench goes when its job ends, and junk (R-1892, R-0833) | Angie moves; nobody deletes another's |
| `C:\AI_Building\AI_MISC\08 Archive\` | the waiting folder of the one archive, for superseded or closed material (R-0832) | Angie moves |

There is no archive or trash in this folder (R-0834). The numbers leave gaps so a folder can be put between two without renumbering.

## Where PRU's budget sources live

Searched read-only on 2026-11-19, file names matched with `PRU`, `powerride` and `univers` (any case) under `C:\AI_Building\AI_Financials` and `C:\AI_Building\AI_Dashboards`, plus the folders named below listed by hand. These are Rick's and the Brain's files: Angie reads them in place and writes nothing there.

### Rick's budget method

| file | what it holds |
|---|---|
| `C:\AI_Building\AI_Financials\04 Budget\README.md` | the budget job's own page: where the old office's budget material is, the skill, the learning phase, the 2027 folder |
| `C:\AI_Building\AI_Financials\.claude\skills\fs-budget-build\SKILL.md` | Rick's orchestrator for next year's budget; it names the University among the lines to draft |
| `C:\AI_Building\AI_Financials\.claude\skills\fs-budget-store-pages\SKILL.md` | how a store's budget page is made: extract, target lines, the page that opens alone, its read-through |
| `C:\AI_Building\AI_Financials\.claude\skills\fs-budget\SKILL.md` | the budget during the year: budget against actual, re-forecast |
| `C:\AI_Building\AI_Financials\04 Budget\2027\LEDGER.md` | the 2027 budget's ledger; its frame rule "the University = its 2026 budget x 1.05", later replaced (next row) |
| `C:\AI_Building\AI_Financials\04 Budget\2027\scripts\fs_budget_pru_2026.py` | how the PRU-pl sheet's 720 cells are made: 2026 actual x Plus27 for January to September, a trend for October to December, October Training from the PRU log (its docstring) |
| `C:\AI_Building\AI_Financials\04 Budget\2027\scripts\fs_budget_standalone_html.py` | the program that makes a budget page that opens alone |
| `C:\AI_Building\AI_Financials\04 Budget\2027\scripts\fs_budget_store_extract.py` | the program that prints a store's extract (PDF and workbook) from the master |
| `C:\AI_Building\AI_Financials\04 Budget\2027\scripts\fs_budget_print.py` | the program that prints the 2027 Budget Book |
| `C:\AI_Building\AI_Financials\04 Budget\2027\2026-11-08 Sergio's dashboard tabs - for BUILDER.md` | his words on the budget dashboard tabs, for BUILDER |
| `C:\AI_Building\AI_Financials\04 Budget\2027\2026-11-09 OPS25 PRUAct heads - Rick\ACCEPTED by Sergio.md` | his acceptance of the PRUAct heading change in the 2025 operating statements copy |
| `C:\AI_Building\AI_Financials\04 Budget\2027\LOCKED\LOCK.md` | what is locked in the 2027 budget; PRU is among what is not locked |
| `C:\AI_Building\AI_Financials\04 Budget\2027\raw files\RAW FILES - list.md` | the list of the 2027 budget's raw files with size and md5, PRU's among them |
| `C:\AI_Building\AI_Financials\04 Budget\01 Learning and testing\README.md` | the budget's learning phase: what was rebuilt and tested before 2027 |
| `C:\AI_Building\AI_Financials\04 Budget\01 Learning and testing\ROLL SPEC - 2026 to 2027 (draft).md` | what the roll changes 2026 to 2027, the PRU budget workbook's tabs included |
| `C:\AI_Building\AI_Financials\04 Budget\01 Learning and testing\meeting 2026-01-28 budget handover\NOTES - what the meeting teaches for the 2027 budget.md` | the old budget owner's walk-through, Rick's notes |
| `C:\AI_Building\AI_Financials\04 Budget\out\from the old office\21 Budget\05 Records\THE BUDGET BOOK - what it is and where each page comes from.md` | what each page of the Budget Book is and where it comes from |

### PRU's budget figures

| file | what it holds |
|---|---|
| `C:\AI_Building\AI_Financials\04 Budget\2027\rolled\02 - Consolidated SGP Budget light.xlsx` | the 2027 budget master; PRU's P&L is its sheet PRU-pl |
| `C:\AI_Building\AI_Financials\04 Budget\2027\rolled\2027 PRU Budget.xlsx` | the PRU budget workbook rolled from 2026 to 2027 |
| `C:\AI_Building\AI_Financials\04 Budget\2027\rolled\University 2026 base - changed cells.csv` | every PRU-pl cell `fs_budget_pru_2026.py` changed |
| `C:\AI_Building\AI_Financials\04 Budget\2027\raw files\1 2026 Budget workbooks\2026 PRU Budget v3 final.xlsx` | the 2026 PRU budget workbook, the roll's source |
| `C:\AI_Building\AI_Financials\04 Budget\2027\raw files\2 Sales and GP\2026 PRU Manual Log v.3 - saved 2026-11-08.xlsx` | Bonnie Lopez's 2026 PRU log, source of October's Training |
| `C:\AI_Building\AI_Financials\04 Budget\2027\raw files\3 Operating statements\02 - Operating Statements 2026-09.xlsx` | September 2026 operating statements; its sheets PRUAct and PRU-Prior feed PRU-pl |
| `C:\AI_Building\AI_Financials\04 Budget\2027\reports\2027 Budget Book - DRAFT.pdf` | the DRAFT 2027 Budget Book, PRU's pages inside |
| `C:\AI_Building\AI_Financials\04 Budget\2027\reports\parts\09 PRU-pl.pdf` | the Book's PRU P&L part |
| `C:\AI_Building\AI_Financials\04 Budget\2027\reports\parts\18 Vs Prior-pru.pdf` | the Book's PRU against prior year part |
| `C:\AI_Building\AI_Financials\04 Budget\2027\reports\parts\28 PRU GP.pdf` | the Book's PRU gross profit part |
| `C:\AI_Building\AI_Financials\04 Budget\2027\reports\parts\32 PRU.pdf` | the Book's PRU part (its content not read) |
| `C:\AI_Building\AI_Financials\04 Budget\01 Learning and testing\bench 2026\inputs\PRU\2026 PRU Budget v3 final.xlsx` | a read-only bench copy of the 2026 PRU budget |
| `C:\AI_Building\AI_Financials\04 Budget\01 Learning and testing\bench 2026\roll test 2\2027 PRU Budget.xlsx` | the PRU workbook from the second roll test |
| `C:\AI_Building\AI_Financials\04 Budget\out\from the old office\21 Budget\01 Drop files here\2026 Budget\PRU\` | the old office's 2026 PRU budget files: v3 final, v10 and v10 macro |
| `C:\AI_Building\AI_Financials\04 Budget\out\from the old office\21 Budget\01 Drop files here\2026 Budget\Cap Exp\1-2026 Cap Ex Falls Church, Woodbridge and Pru.xlsx` | the 2026 capital spending list, PRU's included |

### PRU's columns in the financial statements

| file | what it holds |
|---|---|
| `C:\AI_Building\AI_Financials\01 Financial Statements\MAP.md` | the statements' map; its rule on reporting units names PRU (codes PR/PRU) among seven |
| `C:\AI_Building\AI_Financials\01 Financial Statements\README.md` | the statements job's page; units FC, WB, ROS, BAY, PRU, CORP and Reinsurance |
| `C:\AI_Building\AI_Financials\01 Financial Statements\reports\2026-09\000 - Final reports\03 - Operating Statements 2026-09 vs Trend.pdf` | PRU's month-by-month on pages 11 and 12 |
| `C:\AI_Building\AI_Financials\01 Financial Statements\reports\2026-09\000 - Final reports\04 - Operating Statements 2026-09 vs Prior.pdf` | PRU against 2025 on pages 11 and 12 |
| `C:\AI_Building\AI_Financials\01 Financial Statements\reports\2026-09\000 - Final reports\05 - Operating Statements 2026-09 vs Budget.pdf` | PRU against the 2026 budget on pages 11 and 12 |
| `C:\AI_Building\AI_Financials\01 Financial Statements\reports\2026-09\FS 2026-09.pdf` | the whole September Book (79 pages); "University" found on pages 3, 5 to 8, 19, 20, 35, 36, 51, 52, 57 to 59 and 65, "PRU" on 60 to 62 |
| `C:\AI_Building\AI_Financials\01 Financial Statements\reports\2026-09\02-05 Operating Statement\02 - Operating Statements 2026-09.xlsx` | the September operating statements workbook, PRU's sheets inside |
| `C:\AI_Building\AI_Financials\01 Financial Statements\out\inputs\2026-06\00 - LS CSV Reports\` | June 2026 PRU exports: `BS PRU 6.26.csv`, `PL PRU 06.26 1.csv`, the May prelims, `C:\AI_Building\AI_Financials\01 Financial Statements\out\inputs\2026-06\00 - LS CSV Reports\Reinsurance\PRU Reinsurance June.pdf` |
| `C:\AI_Building\AI_Financials\01 Financial Statements\out\inputs\2026-07\00 - LS CSV Reports\` | July 2026 PRU exports: `2026-07 BS PRU.csv`, `PL PRU 07.26.csv` |

### Rick's raw data

| file | what it holds |
|---|---|
| `C:\AI_Building\AI_Financials\00 Raw data\GL\` | the general ledger, all accounts, 2020 to 2026 year to date, one CSV a year, with a Store column; whether PRU's postings are in it, and under which store code: not checked |
| PRU's monthly exports for August 2026 and later | NOT FOUND under `C:\AI_Building\AI_Financials\00 Raw data` or `C:\AI_Building\AI_Financials\01 Financial Statements\out\inputs`; the statements' map says the exports are read from Accounting's shared drive, not listed by this desk |

### ONE VIEW: Rick's budget pages and the sender

| file | what it holds |
|---|---|
| `C:\AI_Building\AI_Dashboards\DASHBOARD MAP.md` | every dashboard, its data owner and build owner, its readers and status; the accept record rule |
| `C:\AI_Building\AI_Dashboards\README.md` | readers, tests and the deploy of the dashboards |
| `C:\AI_Building\AI_Dashboards\sales command center\send_pages.py` | sends each ONE VIEW tab's page with its accept record; budget tabs `budget-fc`, `budget-wb`, `budget-rosenau`, `budget-all`, read from Rick's reports folder |
| `C:\AI_Building\AI_Dashboards\sales command center\accept_record.py` | checks each page's accept record before anything is sent |
| `C:\AI_Building\AI_Dashboards\sales command center\build_command_center.py` | builds the ONE VIEW shell and its tabs (the Brain's) |
| `C:\AI_Building\AI_Financials\04 Budget\2027\reports\Falls Church 2027 Budget - DRAFT.html`, `Woodbridge 2027 Budget - DRAFT.html`, `Rosenau 2027 Budget - DRAFT.html`, `Consolidated 2027 Budget - DRAFT.html` | Rick's live budget pages, each with its `.accept.json` beside it: the model for PRU's page |
| `C:\AI_Building\AI_Financials\04 Budget\2027\reports\<store> 2027 P&L Goals - DRAFT.html` (Falls Church, Woodbridge, Rosenau, Consolidated) | Rick's P&L Goals pages, each with its accept record |
| a PRU budget page, or a PRU tab in `send_pages.py` | NOT FOUND: none exists on 2026-11-19 |

### From the Brain

| file | what it holds |
|---|---|
| `C:\AI_Building\AI_Brain\wiki\group-companies\powerride-university\true-now.md` | what is true now about PRU |
| `C:\AI_Building\AI_Brain\wiki\group-companies\powerride-university\decisions.md` | PRU's decisions, newest first |
| `C:\AI_Building\AI_Brain\wiki\business.md` | PRU among the group's companies, part of the financial statements; PRU's website is on Wix |

### The school's own data: coaches, ranges, classes, students

Named by him on 2026-11-19 (`C:\AI_Building\AI_PRU\05 His answers and decisions\His words - the desk opened.md`). Listed by name only on 2026-11-19; nothing was opened, and no customer data was read. Angie reads these in place and writes nothing there.

| place | what it is | who writes it |
|---|---|---|
| `H:\Shared drives\PRU ANALYSIS\` | the school's shared folder (his words: "this is our shared folder") | the school's team, not this desk |
| `H:\Shared drives\PRU ANALYSIS\Conversions Analysis\` | a folder; contents not listed | the school's team |
| `H:\Shared drives\PRU ANALYSIS\Monthly PRU Registrations\` | a folder; contents not listed | the school's team |
| `H:\Shared drives\PRU ANALYSIS\PRU returns.xlsx` | a workbook; not opened | the school's team |
| https://www.powerrideuniversity.com/ | the school's website (his words: "this is tehir website"), on Wix (`C:\AI_Building\AI_Brain\wiki\business.md`) | not this desk |
| `C:\Users\Sergio\My Drive (spagnini@wherethepoweris.com)\003 - PRU\` | his work Drive folder for PRU, named in `C:\AI_Building\AI_PRC\15 Google Drive map\DRIVE MAP.md`, "Where things are (top level)"; listed by path only, not read | Sergio |
