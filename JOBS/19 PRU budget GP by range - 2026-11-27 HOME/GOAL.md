# Job 19: a 2027 Budget GP tab by range, the P&L out, the class counts the same on every tab

His words, Angie's chat, 2026-11-27: "i also need "monthly trends by range" and "2027 plan" to be linked. 2027 budget P&L is useless. make it a 2027 budget GP, which is where i can edit coaches and rent cost by range. It linked to monthly and 2027 plan." His answers: 76, "i see different number of classes between the two. right now i have 566 in monthly and 558 in 2027 plan"; 77, "Yes, by range and month (Recommended)"; 78, "Drop it everywhere".

Built on job 18's page (page_after.html eb0dc3fc, blind checker r1 PASS), so job 18 goes to LAWYER inside this job.

## What the finished page shows

1. A tab "2027 Budget GP" in place of "2027 Budget (P&L)". At the top, a total block; under it, one block per range. Each block has months across and a year column, with 4 lines: Sales, Coach cost, Rent, Gross profit (sales less coach cost less rent).
2. In each range block, 2 boxes to type: coach cost per class and rent per weekend. Each starts at the value the page uses today. A typed value moves that range's lines and the total block. Emptying a box goes back to its start value.
3. A range's sales are the class fees of its sites, BRC2 and First Ride included, at their real site. ARC, Loss Damage Waiver and other parts, which belong to no range, sit in one block of their own. The total block's sales equal the 2027 plan tab's sales.
4. Linked: a class, a fill or a price typed on "Monthly trends by range" or "2027 plan" moves the GP tab, and a typed coach cost or rent moves nothing but GP.
5. The 2027 class count is one number on every tab. Wherever 2026 and 2027 class counts stand side by side, each is labelled with its year.
6. The P&L is gone: no P&L tab, and no "2027 P&L" sheet in the Excel download.
7. With nothing typed, every class, student and sales figure is the same as the accepted page (job17 cb153273): 610 classes, 5,093 students, sales $2,011,791.21.

## The tests that say it shows it

- T1: job 18's test (each range tab's grid adds up to its "2027B classes" row), still passing.
- T2: for every range and month, GP = sales − coach cost − rent; the blocks add up to the total block; the total block's sales = the 2027 plan tab's sales, to the cent.
- T3: type a class on the trends tab, then a fill on the 2027 plan tab, then a price: the GP tab moves by the same sales amount as the 2027 plan tab, once. Type a coach cost and a rent: only GP moves.
- T4: the 2027 class count read from every tab that shows one is the same number, nothing typed and with a class typed.
- T5: nothing typed: classes, students and sales on every tab and in the download equal the accepted page's.
- T6: no "P&L" tab, and no "2027 P&L" sheet in the download.
- Each test is run once on a page with a planted fault, to show it can fail.

## Your 76: the 566 and the 558

- In the accepted plan, "Monthly trends by range", Summary, Classes, shows 2026 classes 566 and 2027B classes 610. The 2027 plan tab shows 610 for 2027, with "566 held or booked in 2026" under it.
- So in the accepted plan, 566 is the 2026 count and 610 the 2027 count, on both tabs. I have not seen your screen. If your 566 is the trends tab's 2026 line, the 558 is your 2027 figure on ONE VIEW, from the plan saved there, which is not the accepted plan (your 72). If both are 2027 figures on your screen, T4 is the test that catches it, and I trace it in this job.
- Point 5 makes the labels say the year, so a 2026 count can't be read as a 2027 one.

## Not in this job

- Clearing the plan saved on ONE VIEW: his step on the page (Reset everything, then Save plan).
- The "DRAFT - not accepted" label at the top of the page.
