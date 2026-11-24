FAIL

# PRU job 11, step "smaller" (piece r6 unchanged), blind check of piece md5 3820f2bba43de8eaac014cd56c7cf585

Filed by Angie, the builder, from the checker's hand-back; its Write tool refused its own FINDINGS.md. Fresh checker, tag ANGIE-HOME-J11H, 2026-11-24 10:02 to 10:12 EST. Bench: `C:\AI_Building\AI_MISC\06 Benches\2026-11-24 PRU job 11 smaller blind check - ANGIE-HOME-J11H\` (harness.html, compare.html, plant.json, serve.py, xlsx_check.py, download.xlsx, download_edits.xlsx; md5s read by Angie 2026-11-24, equal to the hand-back). This is a finding, never an acceptance. Scope: Piston's word, MUST 4 covers whole saved lines and top-level keys only. First FAIL at the "smaller" step; by Piston's word a FAIL here ends the ladder and goes to Sergio.

md5 at start and end: piece 3820f2bba43de8eaac014cd56c7cf585; base c2f6b7ce921e7318fc51c2ef0d9fa097.

## Finding (MUST 4, "kept, unchanged")
1. A saved fill key the page does not read is listed, but its value is rounded and clamped to 0-100 on every load. Piece line 125, norm(): FILLV runs on every key of fillType and fillUnit, read or not (Angie read the line: `["fillType","fillUnit"].forEach(k=>{Object.keys(s[k]).forEach(q=>{if(s[k][q]!=null)s[k][q]=FILLV(s[k][q]);});})`). Plant: fillType {"Zzz":12.5,"Yyy":150}, fillUnit {"Gone|2-Wheel":70.4} became 13, 100, 70 in getState, editsText(), the draft, a reload, the loadEdits round trip and the frame save message, after real typing of fill 60 and Save plan. The page writes only whole numbers 0-100 itself, so only a hand-made or foreign plan has this shape. Fix named by the checker: normalise only the keys in READS.fillType and READS.fillUnit.

## Passed
- LAWYER's three shapes (dirt field and month list, whole sections of 7 kinds, price key "constructor"), __proto__ and constructor keys, own shapes: 21 orphans listed and kept through every path, with real typing. Base given the same 8 shapes listed only "__proto__".
- Reverse probe: 0 keys neither read nor listed, 0 both; the probe's self-test returned BAD.
- No figure moves: 43, 47 and 43 views in 3 states, 0 differences; plannerSheets and budget().E equal; two planted 1-cent differences caught.
- Job 11 tests 1-4: 13 tabs, zip and 18 XML parts well-formed; 4,269 of 4,269 cells equal the model (plant gave 2,478 mismatches); focused box taken in; Summary 41 of 41 add-ups; P&L tab equals the page; one centred fixed button on 4 tabs, at 375 px; 0 Load my edits.

## Reported, not counted
R1 dirt wk as a number throws on a weekend edit (line 603, base same). R2 empty hdN kept, not listed. R3 Reset everything drops orphans (code read, base same). R4 a bad shape refuses the whole plan (validPlan). R5 keys inside P&L cells not probed, out of scope. R6 Excel range tabs are the 9 R3.sites, Trends shows a different list (base same). R7 garbled characters from the bench server's missing charset.

## Not checked
Excel itself; MUST 6 names search; job 10 tests against the real server and ONE VIEW frame; Piston's job 10 pick; test_server.py; the live CSP; Trends option combinations; the GL tie-out (excluded by the launch).

## Checker's mistakes
A wrong tab key once (reloaded, no result taken); a missed click from a scaled screenshot (redone); one string-search "kept" check wrong and not used. Shells bw9gbam5x and bpgg9won3 stopped by TaskStop; draft keys cleared; tabs closed. Tokens 193,658 (app's report).
