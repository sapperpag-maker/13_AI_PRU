PASS

# PRU job 07, blind check r10: the Trends rounding sentence

- TARGET: `C:\AI_Building\AI_MISC\06 Benches\2026-11-22 PRU job 07 Trends - ANGIE-HOME-T7\draft-j.html`, md5 ea29950b573428ac06ff1522257ac992, 106,671 bytes
- BEFORE: `draft-i.html`, same folder, md5 2598de94e387c5f3ba64f8be5116770c, 106,661 bytes
- Measured on bench copies with the same md5s, served as UTF-8 on 127.0.0.1:59440, in the built-in browser, own tab.

## Findings

NONE.

## What passed

1. **Byte diff.** Common prefix 78,006 bytes, common suffix 28,655 bytes. i has 0 bytes between them; j has 10: `or beside `. One line of 560 differs (line 345). The sentence in j reads: Rounding: each 2027B figure is rounded on its own from its exact value, so a total can differ from adding the rounded rows above or beside it.

2. **Where it shows.** 96 views driven through the page's own controls: 3 measures x 8 class filters x 4 table years.
   - Students: on 32 of 32 views, once each.
   - Sales $: on 32 of 32 views, once each.
   - Classes: on 0 of 32 views.

3. **It is true.** Start inputs (no saved state), table year 2027B, every class filter that draws a table. Bound: half a unit per non-zero figure added.

   | Measure | Views with table | Row tests | Rows that miss | Largest | Column tests | Columns that miss | Largest | Over the bound |
   |---|---|---|---|---|---|---|---|---|
   | Students | 7 | 37 | 24 | 3 | 91 | 16 | 2 | 0 |
   | Sales $ | 7 | 37 | 25 | $4 | 91 | 27 | $2 | 0 |
   | Classes | 5 | 39 | 0 | 0 | 65 | 0 | 0 | 0 |

   - Row test: the 12 printed months against the printed year, including the All ranges row. Column test: the printed range rows against All ranges, for each month and the year.
   - Each printed Students and Sales $ figure equals the page's own rounding of its exact value from `trendSeries`: 0 differences on the range rows, 0 of 91 on the All ranges rows of each measure.
   - The exact range rows add to the exact All ranges row in every month: 0 differences.
   - Example, Students, All classes: Virginia Beach months add to 465, year prints 462, miss 3, bound 6. Sales $, All classes: Clarksburg (MD) months add to $194,576, year prints $194,578, miss $2, bound $6.
   - No table to test, the page says no figure instead: Other on Students and Sales $; HD, ARC and Other on Classes.

4. **Words.** No quotation mark or apostrophe; no his, him, he; none of Rick, Angie, Sergio, Piston, LAWYER, Ben, Brain (whole-word, any case).

## Proof the checks could fail

- Sum test: a planted +50 on Clarksburg (MD) January gave a miss of 51 against a bound of 6 and was flagged. The cell was put back.
- Presence test: finds the sentence 0 times in draft-i and once in draft-j.
- Words test: flagged a planted line naming Rick and him.

## Risks that are not faults

1. Rule R-0802-HOME-VCMQ, served to this check, reads: "Every agent MUST NOT do blind check on a disclaimer/annotation/comemt/quote/note/log/history line." This job is a blind check of a note line. I ran it because the launch ordered it by name. Whether that rule covers this check is for the desk to settle with the Owner or the Legislator.
2. The sentence speaks of 2027B and still shows when 2027B is switched off or another table year is picked. The order asks for it on all 4 table years, so this is as ordered.
3. The bound used counts the figures added, as ordered. The total's own rounding could add a further half unit; no miss needed it.

## What I could not check

- Any inputs other than the start inputs.
- Whether the exact 2027B values are right against their sources: out of scope, no source workbook opened.
- Anything else on the page: out of scope.

## My own mistakes

1. My first shell line held a stray `cat > /dev/null` that waited on input until the 120-second limit. I stopped that shell. It changed no file; the bench copies had already been made and their md5s matched.
2. My first rules asks used values the program refused (Reviewer, dashboard). I asked again with valid values and got the rules.
