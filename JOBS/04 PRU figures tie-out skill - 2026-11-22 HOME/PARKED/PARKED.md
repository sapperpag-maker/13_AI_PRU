# PARKED: the pru-figures-tie-out skill (NOT DONE)

Angie, 2026-11-22 02:10 HOME. Sergio's gate answer Q59: "Park the whole skill (Recommended)".

## Why
The program's last blind check, r6, is FAIL: `C:\AI_Building\AI_MISC\06 Benches\2026-11-22 PRU tie-out program check r6 - ANGIE-HOME-TC6\VERDICT.md`, md5 57480f2a. (That bench moves to the trash; the copy is `VERDICT r6.md` beside this file.)
- F1: a number-format section holding @ (text) is read as the negative section. Cell -50, format `0%;@`, scale points, shown -50% comes out TIED. tie_out.py lines 285-293.
- Checker FAILs on the program: 6 (r1-r6). Path spent: program, new shape (Piston's pick 2731af36), shape 1, shape 2, stop.

## What is here
- `pru-figures-tie-out\` : SKILL.md 753eb20d, tie_out.py db36cbd4, test_tie_out.py 32f9079b (285 tests pass). Moved out of `.claude\skills\` so it does not fire.
- `pru-planner-check SKILL.md - changed under Q58, parked` (a6d00721): the step 3 change naming the tie-out. Taken back out of the live skill, which is again the committed text, since it would call a parked skill.
- The two workflow PDFs in `C:\AI_Building\AI_Brain\Deliverables\reports\skills-workflows\` stay DRAFT.

## What it needs from Sergio
A word to restart: fix F1 (refuse any format with @ outside a 4th section) and one more blind check, or leave it parked.
