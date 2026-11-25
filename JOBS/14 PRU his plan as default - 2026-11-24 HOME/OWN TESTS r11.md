# Job 14 r11: Angie's own tests (2026-11-24, HOME). Not a verdict.

- Piece: `job14 410b33df.html`, md5 410b33df16d1928e28fef449a479ca28, 157,857 bytes, in this folder.
- Repairs r10 (f0f6a502), which failed LAWYER round 1: verdict `C:\AI_Building\AI_LAWYER\Office desk\Verdicts\2026-11-24 Angie PRU job 14 page r10 check - 81e59d05.md`, findings F1, F2, F3.
- Built by `fix14.py` on the bench. The only change from r10 is the fill line, which is 1 line; diff r10 to r11 is 2 lines (1 out, 1 in).

## The repair
- F1 and F2: the fill line now reads exactly as Sergio's question 15, which showed the whole line with no quote marks. His answer: "Yes, use this (Recommended)". The line: Fill % is the share of seats filled. Leave a box empty to use the 2026 fill (March to November). A fill typed for one site beats its class type, and a class type beats the box for all classes. Prices come from Class Data, 2027 Projections, M17 to M21.
- F3: `OWN TESTS r10.md` and `BLIND CHECK r10 PASS.md` each carry a correction line at their end.
- The three save lines are as question 14, unchanged from r10. They hold no quote marks.

## Tests, at http://localhost:8814/r11.html, browser storage cleared first
1. PASS. Nothing saved: the download sheets equal his file in all 13 sheets after the job 13 name swap, with the Downloaded lines left out: 0 cells differ.
2. PASS. After typed changes (2,235 cells differ), two clicks of Reset everything: 0 cells differ.
3. PASS. A draft with 3-Wheel price 111, after a reload: the draft shows (price 111).
4. PASS. SELFTEST worst gap 7.28e-12; the console shows no error.
5. PASS. The fill note on the plan tab reads word for word as question 15. The status after Reset reads "Kept on this computer only, not saved yet. Press Save plan to save it.", as question 14.
