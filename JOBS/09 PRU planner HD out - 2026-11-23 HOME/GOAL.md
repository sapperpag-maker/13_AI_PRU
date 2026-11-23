# Job 09 goal: the passed planner page with HD out, and nothing else

His words: 150, "HD is off. the range for ARC look in the website"; 151, "Take HD out (Recommended)" (both in Piston's chat, relayed by Piston, 2026-11-23).

Piston's order, 2026-11-23: a separate small piece, page dc320827 with HD out and nothing else, on its own bench, with this goal. One blind check; PASS goes to Piston, then LAWYER. Rick's Books use the new page's figures. Nothing goes live.

Base: `C:\AI_Building\AI_MISC\06 Benches\2026-11-23 PRU figure fix - ANGIE-HOME-FX\build\planner.html`, md5 dc320827a5f0f9b4c3803156ba2ce8f0.
Bench: `C:\AI_Building\AI_MISC\06 Benches\2026-11-23 PRU HD out - ANGIE-HOME-HD\`.

## It MUST deliver

1. 2027B carries no HD students, no HD sales and no HD price box.
2. 2027 sales $1,740,120.89, operating profit $264,213.17, net after taxes $187,571.25.
3. Everything that does not follow from HD stays as on dc320827: classes 498 on this page, rent $155,429.64, coach cost $494,505, and all of 2025 and 2026, HD's 2026 history included.
4. The plan tab says in one sentence that HD is not offered in 2027, and the P&L tab's note on why the page differs from the Workbook names HD as a third reason, with its amounts.

The job changes four places in `template.html`, and no others: the carried list, the price boxes, the plan tab's carried note, and the P&L tab's Workbook note.

## The common failures the blind check tests

1. A P&L cell differs from dc320827 with HD's price set to 0, the independent route to the same answer.
2. Sales, operating profit or net differ from item 2.
3. 2027B students moved anywhere except by HD's 48, in the Manassas - GMU range and the HD class.
4. Classes, rent or coach cost moved, in any month.
5. A 2026 figure moved, HD's included.
6. An HD row, price box or HD amount is still shown for 2027.
7. A sentence on the page is no longer true with HD out.
8. The page shows an error on any tab.
9. A saved state from the old page, holding an HD price, breaks the page or brings HD back.
10. The template differs from the base's in any place other than the four named.

## Pass mark

All 4 delivered and none of the 10 failures found. Anything else the check sees is reported, never a FAIL.
