"""Job 07 test 3: contrast of the Trends year colors, read from theme.css, in both themes."""
import itertools
import re
import sys
from pathlib import Path

css = (Path(__file__).parent / "theme.css").read_text(encoding="utf-8")
dark, light = css.split(':root[data-theme="light"]')


def lum(h):
    ch = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    r, g, b = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in ch]
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(a, b):
    x, y = sorted((lum(a), lum(b)), reverse=True)
    return (x + 0.05) / (y + 0.05)


bad = 0
for name, block in (("dark", dark), ("light", light)):
    card = re.search(r"--card:(#[0-9A-Fa-f]{6})", block).group(1)
    cols = {y: re.search(rf"--t{y}:(#[0-9A-Fa-f]{{6}})", block).group(1) for y in ("2024", "2025", "2026", "2027")}
    for y, c in cols.items():
        r = ratio(c, card)
        bad += r < 3
        print(name, y, c, "vs card", round(r, 2))
    for (a, ca), (b, cb) in itertools.combinations(cols.items(), 2):
        r = ratio(ca, cb)
        bad += r < 1.5
        print(name, a, "vs", b, round(r, 2))
print("RESULT:", "PASS" if not bad else f"FAIL ({bad})")
sys.exit(1 if bad else 0)
