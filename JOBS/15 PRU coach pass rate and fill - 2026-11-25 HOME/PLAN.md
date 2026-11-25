# PLAN - job 15: the PRU weekly dashboard (draft 2, 2026-11-25, Angie, HOME)

Goal: `GOAL.md` in this folder, accepted by his question 23 ("Yes, build it (Recommended)"). Draft 1, a tab in the planner, was replaced by his words of 2026-11-25 quoted there.
Sources: his two files, copied read-only to `C:\AI_Building\AI_MISC\06 Benches\2026-11-24 PRU planner data survey - ANGIE-HOME-W24\data\` (survey: job 12, `SURVEY.md`):
- `PRU Student_Class Data 2024 to 11-24-26.xlsx`, sheets 2024, 2025 and 2026: one row per student.
- `Sergio PRU Class Data.xlsx`, sheets 2024, 2025 and 2026 Demand Analysis: one row per class. The Recap tabs are not used (his order, 2026-11-24).

1. **Count on the bench, never in the page.** A refresh program in a new bench `C:\AI_Building\AI_MISC\06 Benches\2026-11-25 PRU weekly dashboard - ANGIE-HOME-W25\` reads only the columns it needs, and no name or contact column. It writes one small data file of counts and totals by week, range, class type and coach.
2. **Tie the counts before building.** Students and fees by year are tied to the survey's counts. Where the two files disagree, the page uses one source per measure and says which.
3. **Build the page:** five tabs, each with weekly trend and YoY. It is styled like the planner.
4. **Weekly refresh:** one program run reads the newest exports and rebuilds the data file.
5. My own tests 1 to 4. Then a fresh blind checker, LAWYER, his yes, and the Brain puts it live as a new ONE VIEW tab.

The weekly refresh skill, pru-weekly-dashboard: Sergio, 2026-11-25. His words: "Draft the skill of Job 15 while yo build". Q24 "Yes, orchestrator"; Q25 "PRU only (Recommended)"; Q26, on the DRAFT workflow PDF `C:\AI_Building\AI_Brain\Deliverables\reports\skills-workflows\pru-weekly-dashboard.pdf`: "Yes, it makes sense (Recommended)". SKILL.md is written after this job's first full run. Only Sergio PRU Class Data is needed: its student sheets match the Student Class Data file row for row on every column used (bench `pru15_same.py`).
r1 blind check (ANGIE-HOME-J15A, `C:\AI_Building\AI_MISC\06 Benches\2026-11-25 PRU job 15 r1 blind check - ANGIE-HOME-J15A\VERDICT.md`, md5 771c630f, first line FAIL): F1, 11 tiles name no source; F2, the Overview shows Fill and Pass rate with no weekly line. His answers to its questions, 2026-11-25:
- Q27, coach name endings: "show me that. Every range has a main coach, a helper, sometimes 2 helpers." Shown: the ending I sits in Instructor 1 in 13,576 rows; I2 sits in Instructor 2 in 7,672 rows.
- Q29: "Main coach (I), merged (Recommended)". One row per person, with the ending dropped. A result goes to the coach marked I, wherever that name sits on the row. This replaces Q19's Instructor 1 column.
- Q28, Demand Analysis rows with no Limit, no # Stud and no Fees: "Leave them out (Recommended)".
r2 blind check (ANGIE-HOME-J15B, `C:\AI_Building\AI_MISC\06 Benches\2026-11-25 PRU job 15 r2 blind check - ANGIE-HOME-J15B\VERDICT.md`, md5 c8b6afce, first line FAIL; 2 counted FAILs): F1, 6 rows in Sergio 2025, week 22, have two different coaches marked I; F2, the goal's students by coach showed students tested only; F3, a lone week drew no mark in 2024 and 2025; F4, chart text about 4 px at 375 px. His answers, 2026-11-25:
- Q30, two coaches marked I on one row: "Instructor 1 only". The first Instructor column holding an I gets the result; the page names the rows (6 in 2025).
- Q31, students by coach: "Show both (Recommended)". The coach table shows students (all rows), students tested and pass rate side by side.
r3 blind check (ANGIE-HOME-J15C, `C:\AI_Building\AI_MISC\06 Benches\2026-11-25 PRU job 15 r3 blind check - ANGIE-HOME-J15C\VERDICT.md`, md5 7e271c92, first line FAIL; 3 counted FAILs, so Piston picks the shape): F1, the source lines said every figure goes to the main coach, but rows with no coach marked I were counted too (649, 61 and 66 in weeks 1 to 47). The checker found every number right and the shape sound. His answers, 2026-11-25:
- Q32, rows with no coach marked I: "get the coach from the first coach column". Such a row goes to the coach in Instructor 1, ending dropped (446, 24 and 22 rows in weeks 1 to 47). Rows with all three Instructor columns blank stay (no main coach): 203, 37 and 44.
- Q33, page theme on first open: "Always dark first". No change.
r4 blind check (ANGIE-HOME-J15D, `C:\AI_Building\AI_MISC\06 Benches\2026-11-25 PRU job 15 r4 blind check - ANGIE-HOME-J15D\VERDICT.md`, md5 f16f1141, first line FAIL; TIEOUT.md c42581ae PASS, 214,603 figures, 0 off): F1, the short coach line in 6 places left out Q30 and Q32's blank rows. Piston picked shape A after the third FAIL. Sergio's answers in Piston's chat, relayed by Piston, 2026-11-25:
- 38: "Fix the line, then LAWYER (Recommended)". The full line in the 6 places; no more blind rounds.
- 39: "Remember their choice (Recommended)". Dark first, then the viewer's pick.
- 40, 7 student rows sharing a coach's name: "Fine as is (Recommended)".
r5 is `job15 66fa1545.html`; own tests in `OWN TESTS r5.md`.
Sources per measure: students, revenue and fill come from Demand Analysis, one row per class. Pass rate and coaches come from the student sheets.

Not in scope, each on TO DO:
- Actual vs Budget, its own page (his question 22).
- Coach profitability. These files hold no coach pay.
- A source that updates on its own instead of exports.
- The 14 unexplained students in Trends.
