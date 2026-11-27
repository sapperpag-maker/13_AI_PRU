# Job 17 goal: cancelled classes out

His words, Angie's chat, 2026-11-26: "can you exclude from actual 2026 cancelled classes?"
His question 48: "No students = cancelled (Recommended)". His question 49: "Check and weekly dashboard". His question 50: "All three years (Recommended)".
His answer to question 51: "from everywhere in ONE VIEW, i don't want to see cancelled classes in any stats". Then: "Always remove cancelled classes. add to your skill".

A cancelled class: a row of a Demand Analysis sheet in Sergio PRU Class Data.xlsx that is counted as a class today (it has a Course and a Limit, # Stud or Fees) and has 0 or blank # Stud.

## What the finished pieces show

1. The goal-classes check (pru_goal_classes.py): each range's busiest 2026 week counts no cancelled class. It prints how many cancelled rows it left out.
2. The PRU Dashboard page (pru-dashboard, job 15, 66fa1545): in 2024, 2025 and 2026, no cancelled class counts in any figure.
3. The PRU 2027 Planner page (pru-planner, live 926ab8a8): no cancelled class counts in any figure drawn from the class data.
4. Each PRU skill that counts classes says cancelled classes are always left out.

## The tests that say so

1. Counted today: 2024 has 21 cancelled rows, 2025 has 21, 2026 has 9. Each piece's left-out count for a year it reads matches.
2. A test file with one planted cancelled class in a range's busiest week: the check's limit for that range drops by one. The same row with 1 student: the limit stays.
3. Each page's class figures equal a fresh count from the sheets with the cancelled rows out, for every year, range and class.
4. Every figure not drawn from class rows is unchanged from the live page.
5. Fees (revenue) are unchanged from the live page in every year, range and class: a cancelled class keeps its fees.

## Added on his later answers, 2026-11-26

His question 55: "Keep their fees": a cancelled class leaves classes, seats and fill, and its fees stay in the fees (test 5).
His question 58: "Take them out (Recommended)": a student-sheet row in a week, range and course where every class was cancelled leaves every figure too (test 4 then reads: every other figure is unchanged, and the student rows left out equal a fresh count of them).
His words, 2026-11-26, after hearing the 2 planner classes (Newport News 2-Wheel January, Woodbridge First Ride April, 1 booking each): "ok also take the class out the 2027 goal for April". Read as: the Woodbridge First Ride class of April 2027 in his plan goes from 1 to 0, so Woodbridge April is 12 classes (2-Wheel 11, 3-Wheel 1), within its limit of 3 x 4 weekends; the planner's default plan carries it, and the goal check on a goal file with that change gives no stop (test 6). The planner is rebuilt from the live job 14 page, 410b33df, not 926ab8a8.
His answer to question 54: "the v3 in google drive, what file do you need?": the planner's 2026 class figures come from the Google Sheet "2026 PRU Manual Log v3", sheet Master, one row per student booking.
