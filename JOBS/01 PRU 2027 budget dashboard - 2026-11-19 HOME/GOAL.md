# GOAL - PRU 2027 budget dashboard - DRAFT

**DRAFT, waiting on Sergio's yes.** Nothing in this job is built until he says yes to this file (R-1879); it goes to him only after LAWYER's PASS on it (R-1809). His words for the job, his answers 55 to 59, his later words on what Angie tracks and his answers 61 and 62 relayed by the Conductor are in `C:\AI_Building\AI_PRU\05 His answers and decisions\His words - the desk opened.md`.

## Who does what

- Angie builds the page, its program and its tests, in this job folder and its bench in `C:\AI_Building\AI_MISC\06 Benches\` (R-0448). [his answer 55: "Angie builds, Rick advises (Recommended)"]
- Rick answers Angie's questions and shares his method and files, and writes nothing in `C:\AI_Building\AI_PRU`. [his answer 55, the option he picked: "Rick answers Angie's questions and shares his method and files, but writes nothing in PRU. Con: the 11-11 rule gets a PRU exception."]
- Angie's own blind checker, then LAWYER, check it (R-1875, R-1877); only Sergio accepts it (R-0180); only the Brain puts it on ONE VIEW (`C:\AI_Building\AI_Dashboards\DASHBOARD MAP.md`: "Kept by the Brain (ruling 880: the Brain builds, updates and maintains every dashboard)"). For PRU, Angie builds and the Brain puts it live, an exception to ruling 880. [his answer 59: "Angie builds, Brain puts live (Recommended)"]

## What the build MUST deliver (items 1 to 4), and what follows it (items 5 to 8)

1. **One page, `PRU 2027 Budget - DRAFT.html`,** in this job folder, that opens alone with no internet, as Rick's store pages do (the skill fs-budget-store-pages, `C:\AI_Building\AI_Financials\.claude\skills\fs-budget-store-pages\SKILL.md`: "one file that opens with no internet, light and dark").
2. **The 2027 budget, built the way Rick's budget pages are built:**
   - every figure printed by a program from the budget master handed over, never typed or edited by hand on the page (the same skill: "Print only from the master handed over. Never edit a page, PDF or CSV by hand: fix its program");
   - PRU's 2027 figures read from the PRU-pl sheet of Rick's master, `C:\AI_Building\AI_Financials\04 Budget\2027\rolled\02 - Consolidated SGP Budget light.xlsx`, named by its md5 on the day of the build (the sheet: `C:\AI_Building\AI_PRU\ANGIE_SPEC.md`, "PRU in the books");
   - the lines, years and views Sergio picks, written in his words into `CHOICES.json` in this job folder (Open, below);
   - "Draft budget, not approved" on the page until Sergio's final lock (the same skill: "Keep "Draft budget, not approved" on until Sergio's final lock").
3. **The school's measures, each as a trend by week, a condition of this job:** each coach's profitability and pass rate, each coach shown by name; each range's profitability; each class's profitability and fill rate; the number of students. [his words: "coaches profitability, pass rate / Ranges profitability / Classes, profitability and filling ration / Number of students / Trend is by week"; his answer 61, relayed by the Conductor: "Part of job 01"; his answer 62, relayed by the Conductor: "By name (Recommended)"] Each measure names the source file it is counted from (R-0005, R-0006). Their sources are still unknown: a measure with no source stops and goes to Sergio before the build goes on. [his answer 61, relayed by the Conductor: "a measure with no source stops and goes to him"; R-0028]
4. **A test, by program** (R-1879: "the test that says it shows it"), that:
   - every budget figure equals the master's figure for the same line and month, and each year total equals the sum of its months;
   - the page shows exactly the lines, years and views in `CHOICES.json`;
   - each of the six weekly measures in item 3 is on the page, one point per week, and each weekly figure equals its recount from its named source file [his answer 61, relayed by the Conductor: "Part of job 01"];
   - the page loads nothing from the internet (no `http:` or `https:` source or link it fetches) and carries "Draft budget, not approved".
   It names the master's md5 and each measure's source md5, and before it is believed it fails on each of 9 planted faults (10 at most), one per common failure case below and in its order: 1, a planted wrong budget figure; 2, a planted wrong year total; 3, a planted extra line; 4, a planted missing year; 5, a missing week; 6, one planted wrong figure in each of the six weekly measures, run as one plant that must fail on all six; 7, a planted internet link; 8, a removed draft line; 9, a removed master's md5.
5. **Angie's own blind checker** finds the page reaches this goal file, before LAWYER is called (R-1875, R-1877).
6. **LAWYER's PASS** names the page by its md5 (R-1809).
7. **Sergio's acceptance**, in his own words, written into the page's accept record, `PRU 2027 Budget - DRAFT.html.accept.json`, beside it (`C:\AI_Building\AI_Dashboards\DASHBOARD MAP.md`: "no tab goes live without `<page file name>.accept.json` beside the page sent").
8. **Live on ONE VIEW only through the Brain**, which sends a page only with its accept record (same map). Angie writes nothing in `C:\AI_Building\AI_Dashboards` (R-0024).

## The common failure cases (capped at 10)

The test checks these 9 cases and no others [his rule of 2026-11-15, as the rules program words it in M-2819-WB-OLBQ: "the MUSTs, a capped failure list and a pass mark"; the cap of 10: LAWYER's, until he gives a number]:

1. a budget figure differs from the master's figure for its line and month;
2. a year total differs from the sum of its months;
3. the page shows a line, year or view that `CHOICES.json` does not name;
4. a line, year or view in `CHOICES.json` is missing from the page;
5. a weekly measure of item 3, or a week of one, is missing from the page;
6. a weekly figure differs from its recount from its named source file;
7. the page fetches something from the internet;
8. "Draft budget, not approved" is missing from the page;
9. the master's md5 or a measure's source md5 is not named.

A case beyond the list is reported, never a FAIL.

## The pass mark

The build passes when items 1 to 4 are each shown by a file (R-1879): item 1, the page and its md5 with the test's PASS on the offline and draft-line checks; item 2, the program that printed the page with its run output naming the master's md5, and `CHOICES.json`; item 3, the test's PASS line for each of the six weekly measures (coach profitability, coach pass rate, range profitability, class profitability, class fill rate, number of students), each naming its source file's md5; item 4, the test's whole PASS output on the 9 common failure cases and its 9 planted-fault runs, one per case, each FAIL (the case 6 run failing on each of the six measures). Items 5 to 8 are not the build's own steps and are not in the pass mark: they are the checks, his acceptance and the putting live that follow it.

## Open, for Sergio, before the build

These are Angie's questions for him, each to go through the question tool (R-0411, R-1879):

- Which budget lines the page shows (for example PRU's whole P&L, or Training and its gross only).
- Which years and views (for example 2025, 2026 and 2027 side by side, as Rick's store extracts show them in the skill fs-budget-store-pages, or another set).
- Who reads it on ONE VIEW.
- Which files hold the coaches, ranges, classes and students week by week: Angie finds the sources (his words: "she can find good sources of data") and brings him what she finds.
