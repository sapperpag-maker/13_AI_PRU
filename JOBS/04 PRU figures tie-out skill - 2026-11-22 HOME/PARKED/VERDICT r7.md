FAIL

# r7 blind check of the PRU figures tie-out program

Checker: job agent launched by Angie (ANGIE-HOME, HOME), round 7. I did not build the piece. I invoked the skill office-review-adversarially before reading anything. OWN_FINDINGS.md was written before any claim; no claim file was opened (no LOG.md, PARKED.md, VERDICT r6.md, no Trash folder). No real data file was opened; every file was made up on this bench. Excel was not started.

Piece checked (md5 and size matched the launch before any test):
- tie_out.py  eab300b2033ac383337b1201f7a558fa  27,493 bytes
- test_tie_out.py  05404aa2d9e5cb094e21d0552d3fcfc0  42,519 bytes

Builder's suite: `python3.14 -I -B test_tie_out.py --bench <bench>\suite2` -> TESTS: PASS (299), exit 0, no __pycache__.

## Failing findings: 2

### A1. A format section that shows no number still decides the scale (F1's class without the @)
The chosen section is read for a %, even when it holds no digit placeholder at all (empty, quoted text only, a bare "-", or a colour only). It has no %, so points and as-is pass, while the format's only numeric section is a percent. A wrong figure comes out TIED, and the right reading is refused.

| Case (made-up cell B2) | Expected | Got |
|---|---|---|
| -0.5, format `0%;"neg"`, scale points, shown `-0.5%` | not TIED (true figure -50%) | TIED, exit 0 |
| -0.5, format `0%;"neg"`, scale fraction-to-pct, shown `-50%` | the right reading | ERROR "fraction-to-pct needs a % format" |
| -0.125, format `0.0%;;0.0%`, scale points, shown `-0.1%` | not TIED (true -12.5%) | TIED, exit 0 |
| -50, format `0%;"neg"` / `0%;` / `0%;[Red]` / `0%;-`, points, shown `-50%` | not TIED (the r6 F1 case with @ swapped out) | TIED, exit 0, all four |
| 50, format `"pos";0%`, points `50%` / as-is `50` | not TIED | TIED, both |

Where: tie_out.py, format_section_for (lines 287-295) picks the section; recompute_cell (lines 338-346) reads "% in that section"; check_format (lines 271-284) refuses only an @, not a section with no number. The class: the scale is decided by reading a section that does not display the value. The fact that settles it: whether the chosen section holds a digit placeholder (0, # or ?, outside quotes, brackets and escapes); without one, refuse. Proof: bench attack2b_out.txt and attack2_out.txt.

### A2. --out that names the figures file or a source is not always refused (goal: exit 2)
The guard compares spellings (same_path, lines 687-688, used in main lines 709-713), not the file.

| --out given | Expected | Got |
|---|---|---|
| `\\?\` + the figures file's full path | exit 2, file unchanged | exit 0, figures file overwritten |
| `\\?\` + a source workbook's full path | exit 2 | exit 0, source overwritten |
| `\\localhost\C$` + the figures path | exit 2 | exit 0, figures file overwritten |
| a hard link to the figures file | exit 2 | exit 0, figures file overwritten |
| figures path + "." / + " " / `\\.\` prefix | exit 2 | exit 2 (refused, good) |

The fact that settles it: file identity (os.path.samefile on an existing --out). Proof: bench attack3_out.txt and attack2_out.txt.

## What passed (counted this session)
- F1 retest: 11 fresh @ shapes (in sections 1, 2, 3, 5, alone, with [Red], quoted, escaped). All refused where they should be, accepted where quoted, escaped or fourth.
- attack.py: 149 cases over formats (quotes, escapes, fill, padding, colours, locale and condition brackets, sections, % counts, thousands commas, scientific, fraction), cell types and float edges, the shown grammar (30 shapes), the GL amount grammar, header, records, accounts, store, dates, journal, side, kinds. 142 matched my expectation; of the 7 that did not: 3 were my own wrong expectations (gl10, r12, r13 are correct behaviour), 1 is correct (r3 ERROR), 3 are notes below (q6, q9, t7).
- Leaks: 149 runs grepped for the planted customer description and Doc #: 0 hits.
- Mutants: 57 written; 2 were my own mistakes (m20 pattern not found, m26 would not compile) and were rewritten as m20b and m26b. Of the 55 valid: 54 caught (53 by a TESTS: FAIL line, 1, m54, by the suite crashing), 1 survived (m53).

## Minor notes (not the verdict)
1. Mutant m53 survived: removing the "md5 must be 8 or 32 hex" check passes the suite (a 1-character md5 prefix would be accepted). Test coverage gap, lines 190-191.
2. Mutant m54 (U+2212 not accepted) crashes the suite instead of failing a named test.
3. Risk, unverified: if Excel reads `!` as an escape (like `\`), format `0!%` holds a literal %, yet the program counts it; cell 50, scale fraction-to-pct, shown 5000% came out TIED (case q9). I could not confirm Excel's reading without Excel. Same for `0 ,` (comma after a space; case t7, accepted as no scaling).
4. An unterminated quote (`"x0%`) hides the rest of the format (q6). Excel would not save such a format.
5. Risk: GL dates are read as M/D/YYYY. A GL written D/M/YYYY with every day 12 or under would be read wrongly without an error. Fact that settles it: the GL export's date setting. Not tested on real data (forbidden).
6. A whole-number cell held as an int above 15 digits is compared exactly; Excel would show it cut to 15 digits.

## What I did NOT check
- Any real GL or workbook (forbidden); the real GL's date order and the real budget workbooks' number formats.
- Excel's own reading of `!`, `0 ,`, and formats Excel itself would refuse.
- Unicode/locale builtin number-format ids beyond what openpyxl maps; workbooks with hand-edited XML (duplicate cell refs, missing r attributes).
- 8.3 short names for --out (my probe crashed on the cmd output, inconclusive).
- Steps 1, 4 and 5 of SKILL.md (the figure listing, the misleading read, TIEOUT.md): not in this check's goal.
- Performance on a large GL.
