"""Looks at every multi-line record of one GL and writes the allowed list for that exact file.
It prints line numbers, counts and yes/no answers only: never a GL line, a Description or an amount (the standing limit).
A record is listed only if all its checks hold. Every check of the Description reads all its pieces, the first one too.
Usage: look_multiline.py <gl.csv> <list.json>"""
import csv
import hashlib
import json
import os
import re
import sys
from datetime import datetime

GL, OUT = sys.argv[1:3]
DESC = 4
ANY_DATE = re.compile(r"\d{1,4}[/\-.]\d{1,2}[/\-.]\d{1,4}")
ACCT = re.compile(r"(?<![A-Za-z0-9])(?:[A-Za-z]+\d+(?:-\d{2})?|\d+-\d{2})(?![A-Za-z0-9])")  # any letters plus digits, or any digits with a -NN ending; a bare number counts only if it equals a real Account value
TOKEN = re.compile(r"[A-Za-z0-9][A-Za-z0-9\-]*")
NUMBER = re.compile(r"-?\$?[\d,]*\.?\d+")
AMOUNT = re.compile(r"-?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?|-?\.\d+")
h = hashlib.md5()
state = {"line": 0}


def lines():
    with open(GL, "rb") as f:
        for raw in f:
            h.update(raw)
            state["line"] += 1
            yield raw.decode("utf-8", errors="surrogateescape")


def real_date(text):
    try:
        datetime.strptime(text.strip(), "%m/%d/%Y")
        return True
    except ValueError:
        return False


def amount(text):
    """Blank, or a real number."""
    text = text.strip()
    return not text or bool(AMOUNT.fullmatch(text))


def checks(x, start, end, accounts, journals, stores):
    desc = x[DESC] if len(x) > DESC else ""
    pieces = re.split(r"\r\n|\n", desc)
    parts = [s.strip() for p in pieces for s in p.split(",")]
    nine = len(x) == 9
    return {
        "nine fields": nine,
        "break only in Description": len(x) > DESC and not any(("\n" in v or "\r" in v) for i, v in enumerate(x) if i != DESC),
        "pieces equal file lines": len(pieces) == end - start + 1,
        "no piece holds a date": not any(ANY_DATE.search(p) for p in pieces),
        "no piece holds an account": not any(ACCT.search(p) for p in pieces)
        and not any(t in accounts for p in pieces for t in TOKEN.findall(p)),
        "no later piece holds a comma, no comma part of any piece is a number, store, account or journal":
            not any("," in p for p in pieces[1:])
            and not any(s and (NUMBER.fullmatch(s) or s in stores or s in accounts or s in journals) for s in parts),
        "no quote in Description": '"' not in desc,
        "Account, Journal and Doc filled, Date a real calendar date":
            nine and all(x[i].strip() for i in (0, 1, 3)) and real_date(x[2]),
        "debit and credit are real numbers, at least one filled":
            nine and amount(x[5]) and amount(x[6]) and bool(x[5].strip() or x[6].strip()),
        "no bare carriage return": "\r" not in desc.replace("\r\n", ""),
    }


csv.field_size_limit(10_000_000)
it = lines()
next(it)
prev = 1
records = 0
held = []
accounts, journals, stores = set(), set(), set()
for x in csv.reader(it, strict=True):
    start, end, prev = prev + 1, state["line"], state["line"]
    if not x or (len(x) == 1 and not x[0].strip()):
        continue
    records += 1
    if end > start:
        held.append((start, end, x))
    if len(x) == 9:  # every record, multi-line ones too
        accounts.add(x[0].strip())
        journals.add(x[1].strip())
        stores.add(x[8].strip())
accounts.discard("")
journals.discard("")
stores.discard("")
found = []
for start, end, x in held:  # after the whole file, so the known accounts, journals and stores are complete
    result = checks(x, start, end, accounts, journals, stores)
    ok = all(result.values())
    found.append((start, end, ok))
    print(f"record at file lines {start}-{end}:", "ALL CHECKS HOLD" if ok else "FAILED: " + "; ".join(k for k, v in result.items() if not v))
md5 = h.hexdigest()
print("file md5", md5, "size", os.path.getsize(GL), "records", records, "multi-line", len(found))
if not found or not all(f[2] for f in found):
    sys.exit("STOP: nothing written, a record did not hold every check")
with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    json.dump({md5: {"size": os.path.getsize(GL), "records": [[a, b] for a, b, _ in found]}}, f, indent=1)
print("WROTE", OUT)
