PASS

# Blind check: job 06 tie-out GL fix (tie_out.py cc8894e4, test_tie_out.py 0e5e081c, GOAL.md 920fa845)
Checker: ANGIE-HOME-GC, 2026-11-22. Skill office-review-adversarially invoked first, at 15:21 EST, before any file was read.
My findings were written here before I read any builder claim; I read no builder verdict, LOG or JOBS folder.

## Findings (fail the work)
NONE. 0 findings.

## What was checked and how it could have failed
- Diff against the accepted job 05 build (C:\AI_Building\AI_PRU\.claude\skills\pru-figures-tie-out\tie_out.py, a8f90d60): the only code changes are header_ok (lines 426-433, used at 465), '+' in _PLAIN_RE (105), has_sign (128-129, 143), the unsigned-zero rule in sign_agrees (161-162) and the "-0" note fix (680-681). Everything else is byte-identical, so point 4 rests on the accepted build plus the spot checks below.
- Point 1 (header): 12 header lines through header_ok. TRUE: real shape with trailing spaces + CRLF; no trailing spaces; leading and trailing spaces; "\r\r\n". FALSE (ERROR): tab after a name, a 10th empty column, quoted names, lower-case "account", double space inside "Debit  Amount", Debit/Credit swapped, a no-break space after Store, 8 columns. Could fail: yes, any FALSE case returning True.
- Point 2 ('+'): "+8%" vs 7.78 TIED; "+$18,233" vs 18233.4 TIED; "+47" TIED; "+5k", "+1,234.5M" TIED; "+5" vs -5 and vs -4.6 OFF "sign differs"; "+0.4" vs -0.4 OFF. Refused (ERROR "shown not readable"): "+-5", "++5", "5+", "+(5)", "(+5)", "$+5", "+ 5", "+", "+.5", "+05", "-+5", "U+2212 then +5"; "+$5%" refused for $ with %. Real GL: "+$15,553" vs Jan TIED; "+15,553" against the debit-credit sum -15,552.61 OFF.
- Point 3 (unsigned zero): "0" vs -0.4 TIED, vs -0.5 OFF (rounds to -1); "0.0" vs -0.04 TIED, vs -0.05 OFF; "0%" vs -0.4, "$0" vs -0.49, "0k" vs -499, "0M" vs -499999 TIED; "0k" vs -500 OFF. CLI run on a made-up GL with the real header shape (fakegl.csv, figs_fake.csv, fake_out.csv): rows a-j, no "-0" in any note, recomputed or difference cell (grep run; the only "-0" hit is the shown column of row d, the input itself).
- Point 4 spot checks: --out refused on 5 other spellings of an existing file ("x.", "x ", upper case, "./x", "x...") exit 2, file md5 unchanged (f86e4aaf...); "$5%", "-$5%", "($5%)", "+$5%" refused; fmt(-0.000) prints 0.000; to_decimal(14.499999999999998)=14.5, int 1234567890123456 -> 1.23456789012346E+15, 1/3 -> 0.333333333333333.
- Suite: python3.14 -I -B test_tie_out.py --bench <this bench> ended "TESTS: PASS (504)". Not my verdict.

## Real-GL result (sums only, no GL line printed)
GL: size 64690471, md5 94ae1ff9841d3de6bc9903402e32874b; header names 'Account ', 'Journal ', 'Date', 'Doc #', 'Description', 'Debit Amount', 'Credit Amount', 'Balance', 'Store ' (CRLF, no BOM); 874,156 records, all 9 fields.
Accounts worked out by sums/counts per account and store (gl_sums.py): store POW has 34 accounts matching 46xxx-30 plus 47700-30 (one 46xxx-30 account, 46300-30, is store WB1 and is excluded by store=POW).
My own rows (figs_real.csv: accounts=46xxx-30,47700-30; store=POW; month from/to; side=credit-debit; md5 and size) gave:
Jan 15,552.61 TIED | Feb 60,160.28 TIED | Mar 201,004.26 TIED | Apr 200,237.82 TIED | May 246,286.44 TIED | Jun 191,234.34 TIED | Jul 171,425.99 TIED | Aug 180,524.17 TIED | Sep 132,794.91 TIED.
These equal my independent sums from gl_sums.py to the cent. Controls on the same run: "15,552" OFF, "-15,553" OFF (sign), "$15,552.61" TIED, "15.6k" TIED. Output files real_stdout.txt and real_out.csv hold only ids, shown values, sums, account numbers and counts (grep: 479 account rows, no other text).

## The builder's reading on signed zeros
Reading: '-0' and '(0)' never tie +0.4; '+0' never ties -0.4; a signed zero still ties its own sign and exact 0.
Judgement: it meets the goal. Point 3 lists only unsigned zeros (0, 0.0, 0%, $0, 0k); point 2 says '+' on a negative value means the signs differ "as - on a positive one does now", and the accepted build already held "-0" never ties +0.30. A report that shows "-0" or "(0)" is showing a negative that rounds to zero, which still TIES.
Risk 1 (not a finding, not a caveat on the verdict): Sergio's Q69 words "0 ties either sign" do not name signed zeros. If he meant every zero, rows like "+0" vs -0.30 (fake row c) and "-0" vs +0.4 would be OFF where he wants TIED. Only his word settles it.

## Minors (change no status or figure)
1. Note on fake row c reads "rounds to 0; sign differs from shown" for shown "+0" vs -0.30: correct but a reader may find "rounds to 0" next to OFF odd.
2. A header with the same names in quotes ("Account ") is ERROR. The goal says any other header is ERROR, so this is consistent; noted in case a re-export quotes its header.

## What I did not check
- Cell rows against any real workbook (none named for this job); cell logic is unchanged from job 05 and covered only by the suite and the to_decimal spot check.
- The unchanged job 05 code line by line beyond the diff and the spot checks; the test file's content line by line.
- gl_check.csv in the hand-run bench (not opened, per my limits); I used the shown values in my launch.
- The 8.3 short-name spelling of --out: short names are not made on this volume, so "FAKE_OU~1.CSV" was a new file name and could not test the guard (the file it created is on this bench).
- Other machines and other Python versions.

## My mistakes
1. I ran the rules program once (STEP 0 of the skill) before noticing it writes an ask receipt to C:\AI_Building\AI_LEGISLATOR\...\Governance\Rules\Ask receipts\HOME\2026-11-22.txt, outside this bench, against my launch limits. The ask was refused for argument form; I did not ask again.
2. My first figures.csv left commas in detail unquoted; the program rightly refused it (exit 2) and I re-ran with quoting.
3. adv.py first crashed printing U+2212 to a cp1252 console; re-run with ascii().

Background shells: NONE STARTED.
