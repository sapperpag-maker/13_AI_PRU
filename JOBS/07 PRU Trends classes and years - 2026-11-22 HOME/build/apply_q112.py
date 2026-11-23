"""Job 07, Sergio's Q112 "Once: 32 weekends": Virginia Beach's 2026 weekends in r3.json go from 33 to 32; its 67 classes stay.
Keeps r3.before-q112.json first and changes that one number."""
import hashlib
import json
import pathlib
import re

here = pathlib.Path(__file__).parent
src = here / "r3.json"
keep = here / "r3.before-q112.json"
raw = src.read_bytes()
assert hashlib.md5(raw).hexdigest() == "b449a52f75a744038c8a6721373cc1f3"
assert not keep.exists()
keep.write_bytes(raw)
assert keep.read_bytes() == raw
new, n = re.subn(rb'("Virginia Beach"\s*:\s*\{\s*"weekends"\s*:\s*)33(\s*,\s*"classes"\s*:\s*67)', rb"\g<1>32\g<2>", raw)
assert n == 1, n
a, b = json.loads(raw), json.loads(new)
assert b["weekends26"]["Virginia Beach"] == {"weekends": 32, "classes": 67}
a["weekends26"]["Virginia Beach"]["weekends"] = 32
assert a == b
src.write_bytes(new)
print("r3.json", len(new), hashlib.md5(src.read_bytes()).hexdigest(), "| kept", keep.name, hashlib.md5(keep.read_bytes()).hexdigest())
