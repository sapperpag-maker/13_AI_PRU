FAIL

# PRU job 11 r5, blind check of piece md5 ace4f5ec00c7179b6d0a2d3e900a264f

Filed by Angie, the builder, from the checker's hand-back; its Write tool refused its own FINDINGS.md. Fresh checker, tag ANGIE-HOME-J11E. Bench: `C:\AI_Building\AI_MISC\06 Benches\2026-11-23 PRU job 11 r5 blind check - ANGIE-HOME-J11E\` (cmp.html, plants.js, ui.js, base.html, new.html). This is a finding, never an acceptance. Second checker FAIL on this repair step.

md5 at start and end: piece ace4f5ec00c7179b6d0a2d3e900a264f (154,110 bytes); base c2f6b7ce921e7318fc51c2ef0d9fa097 (152,630 bytes).

## Findings, goal point 1 (MUST 4)
1. A saved fill % for ARC is not read and not listed. orphans() treats "ARC" as known for unitMonths, fillUnit and spc (piece line 314). The page reads unitMonths.ARC and spc.ARC (lines 203-206), but it never reads fillUnit.ARC, because fillPct() (line 187) runs for units only. With `{"fillUnit":{"ARC":50}}`, orphans() is [] and every figure and view equals no edits. The base page has the same gap.
2. Typing on a P&L line drops the unknown keys saved inside that line. Plants: pl.24.y.note, pl.24.extra, pl.25.m.3.foo, pl.25.bar. Typing in line 24's year box, line 25's Apr box and line 25's year box removed them from getState, editsText() and the draft, and the warning stopped naming them. Cause: setPl (line 310) rebuilds the line or cell as {t,v}. The base page has the same fault. This counts only if keys inside a line are saved edits under MUST 4; the launch's plant list said they are.

## Passed
- 60 raw-JSON plants, 9 of them __proto__ keys, all listed (52 labels; the same name in 3 unit maps shares one label). After an edit elsewhere, every one is kept in getState, editsText, the draft, loadEdits(editsText()), a reload and the frame save message.
- No orphans from the page's own edits: real UI on all tabs, setPl, setClassCell, setSpcCell, and clearing boxes.
- Point 2, no figure moves: the diff is 6 hunks (norm, orphans, withAt, the server save text). 7 scenarios over 26 views, up to 1,992 inputs each: 0 differences in figures, text and inputs. Only the stored state differs, where the piece keeps the 3 __proto__ keys the base loses. Only the server and unknown save errors carry the new text.
- Proof the checks can fail: a planted price, a one-digit text change, an input change and a renamed plant were each caught; the base page fails the orphan test.

## Risks, not counted
R1: unit-map orphans are listed by bare key, merged across maps. R2: validPlan refuses a wrongly shaped draft whole and silently. R3: dirt wk or cpw saved as a number makes a weekend edit go nowhere (same on base).

## Not checked
The 20-second ack timeout path; the artifactApi save path; xlsxBytes bytes; every Months panel; Trends filters other than the defaults; the dark theme; console errors inside frames.

## Checker's mistakes
Started python once with a heredoc (bkocd2oay); it ran nothing and was stopped. The first S0 run used a cached harness and was rerun. Server bpth8fbpj stopped, draft key cleared, tab closed.
