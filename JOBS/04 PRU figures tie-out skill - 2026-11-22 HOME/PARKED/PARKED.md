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

## ADDENDUM 2026-11-22 09:49 HOME: the last check failed; parked for good
Sergio's answer to Piston's question 90: "Fix F1, one last check (Recommended)". F1 was fixed (tie_out.py eab300b2, test_tie_out.py 05404aa2, TESTS: PASS (299)). The last blind check, r7, is FAIL: `VERDICT r7.md` beside this file, md5 a5aa8d99.
- A1: a format section that shows no number (empty, only quoted text, a bare "-" or only a colour) still sets the scale. Cell -0.5, format `0%;"neg"`, scale points, shown -0.5% comes out TIED.
- A2: the --out guard compares how a path is written, not the file, so `\?\` paths and hard links can overwrite the figures file or a source.
Under Sergio's answer, no further round. The skill stays parked; a restart needs a new word from him.
