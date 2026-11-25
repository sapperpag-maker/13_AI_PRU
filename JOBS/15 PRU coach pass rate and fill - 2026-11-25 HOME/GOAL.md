# GOAL - job 15: the PRU weekly dashboard, a new page

ACCEPTED by Sergio, question 23, 2026-11-25, in Angie's chat: "Yes, build it (Recommended)".

Draft 1, a new tab in the planner, was accepted by question 21 ("Yes, build it (Recommended)"). His later words in Angie's chat, 2026-11-25, replaced it with a new page:
- "I think we have to create a new page to explode and divide in multiple tabs the 2027 planner into what it'll become the daily dashboard. And I'd like to see KPI by students, by Range, by Class, By Coaches. YoY comparisons. Trends."
- "updated on a weekly base"
- Question 22, where Actual vs Budget goes: "Its own page". That page is a job of its own, not this one.
His rules, still in force (questions 18 to 20, 2026-11-25):
- Pass rate is passed divided by passed plus failed ("Passed vs tested (Recommended)").
- Only Instructor 1 gets the result ("Instructor 1 only").
- Coach names show as the file has them ("Real names (Recommended)").

## What the finished page shows
1. A new ONE VIEW page, the PRU dashboard, with five tabs: Overview, Students, Ranges, Classes, Coaches. The 2027 planner stays live and unchanged.
2. Each tab shows its KPIs by week for 2024 to 2026, with a trend line and the same week of the year before (YoY).
   - Students: students, and the student count against the year before.
   - Ranges: students, revenue and fill by range.
   - Classes: students, revenue and fill by class type. Fill is students against seats.
   - Coaches: pass rate and students by coach.
   - Overview: the headline figure of each of the other four tabs.
3. It is refreshed weekly from the newest exports in `H:\Shared drives\PRU ANALYSIS\2027 Planner data`.
4. Every figure names its source file and sheet.
5. No student's name, date of birth, licence number, address, email or phone is in the page. The page holds counts and totals only.

## The tests that say it shows it
1. A program re-counts every figure from his files by week, range, class type and coach. Every figure on the page equals that count.
2. A program searches the page for every student name, email, phone, licence number and date of birth in his files, and finds 0.
3. Re-running the weekly refresh on the same files gives the same page.
4. The browser console shows no error, and each tab opens.
