PASS

# PRU job 14 r10 (his plan as the default, plus the save and fill wording): blind check of piece md5 f0f6a502cb09187caa92c5dcb0e70310

Angie, the builder, filed this from the checker's hand-back. This is a finding, never an acceptance; only Sergio accepts.
- Checker: a fresh job agent, tag ANGIE-HOME-J14A, 2026-11-24, about 21:43 to 22:13 EST. It used 155,371 tokens (the app's own count).
- Bench: `C:\AI_Building\AI_MISC\06 Benches\2026-11-24 PRU job 14 blind check - ANGIE-HOME-J14A\`. The verdict is in PROGRESS.md (md5 795468424a57dfd57ad9ad6c7ed64c3c, Angie read it). Its line reads "# VERDICT: PASS". The harness refused FINDINGS.md.
- The checker invoked office-review-adversarially at the start, just before 21:43:05. It asked the rules program twice, as All and as Angie with review / budget. Its own head limit cut the second printout at R-0117.
- md5 at the start and the end:
  - piece: f0f6a502cb09187caa92c5dcb0e70310
  - base r9: 6ded25cb0d85d55d4e893bb14b824897
  - goal: 363ced900d2703de4b74ec4a5a6ce437
  - his file: 78f1ffa44ed0bdd36e76a9926382cf08

## Failing findings
NONE.

## Passed (the goal's tests)
1. With nothing saved, the download equals his file in all 18 xlsx parts. The checker compared 3,914 cells. The only differences are the Downloaded lines and the job 13 name swap. Its planted change was caught.
   - His file's figures: 609 classes; 5,091.42 students; $2,011,581.60 sales; $238,565.12 after taxes (Summary N5, N6, N10, N17).
   - In a stand-in for the ONE VIEW frame with no saved plan, the page opens on his plan and its download also equals his file.
2. After typed changes and two clicks of Reset everything, the download equals his file again.
3. A browser draft, an edits file and a saved plan in the stand-in frame each open over his plan.
4. SELFTEST worst gap 7.28e-12. The console shows no error, and a planted error was read back.
5. The four approved lines appear word for word. Line a was checked in the code only, because it shows only when storage is blocked.
6. Nothing else changed. The diff has 7 spots, each one a goal item. The frame messages are unchanged, and so are the comparison columns. 11 boxes on the plan tab show as typed.

## Risks (no wrong value shown)
- R1: two status lines this job did not touch still say "browser" where the new ones say "this computer".
- R2: a draft or edits file made before job 14 opens over his plan (goal item 4).
- R3: on a plain local server the "·" and "×" signs show garbled. r9 is the same.
- R4: Reset on a page that carries its own saved plan goes back to his plan (goal item 2).

## Not checked
- The live ONE VIEW frame and the Brain's real save.
- The window.claude republish.
- Line a on screen.
- Phone layout, and other browsers.

## Checker's own mistakes
- One click missed and was redone by element.
- One oversized result was saved by the harness to the session's tool-results folder. It holds planner workbook text only.

CORRECTION (2026-11-24, after LAWYER FAIL 81e59d05, finding F3): the claim above that the fill line is word for word is wrong. r10 printed double quote marks where question 14 showed single ones, and it kept a Prices sentence that question 14 did not show. Repaired in r11 (410b33df) on question 15.
