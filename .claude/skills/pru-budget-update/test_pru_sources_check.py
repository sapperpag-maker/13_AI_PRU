"""Test pru_sources_check.py on a bench copy of SOURCES.json with made-up files.

Never writes the real manifest; checks it is unchanged byte for byte at the end.
Prints RESULT: PASS when every case holds, else RESULT: FAIL.
"""
import hashlib
import json
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROG = os.path.join(HERE, "pru_sources_check.py")
REAL = os.path.join(HERE, "SOURCES.json")
BENCH = r"C:\AI_Building\AI_MISC\06 Benches\2026-11-21 PRU budget skill - ANGIE-HOME\src\test"

fails = []


def check(name, cond):
    print(("ok   " if cond else "FAIL ") + name)
    if not cond:
        fails.append(name)


def run(*args):
    p = subprocess.run([sys.executable, PROG, *args], capture_output=True, text=True)
    return p.returncode, p.stdout.strip().splitlines()


def write(path, data):
    with open(path, "wb") as f:
        f.write(data)


def main():
    with open(REAL, "rb") as f:
        real_before = f.read()
    os.makedirs(BENCH, exist_ok=True)
    man = os.path.join(BENCH, "SOURCES.json")
    a, b, c = (os.path.join(BENCH, n) for n in ("a.bin", "b.bin", "c.bin"))
    write(a, b"made-up file A")
    write(b, b"made-up file B")
    write(c, b"made-up file C")
    ma, mb, mc = (hashlib.md5(open(p, "rb").read()).hexdigest() for p in (a, b, c))
    bench = {
        "roles": {
            "class_data": {"md5": mc[:8], "md5_full": None, "name": "c.bin"},
            "manual_log": {"md5": ma, "md5_full": ma, "name": "a.bin"},
            "gl": {"md5": mb, "md5_full": mb, "name": "b.bin"},
            "rick_budget": {"md5": "0" * 32, "md5_full": "0" * 32, "name": "x"},
        },
        "page_md5": "test",
        "recorded": "2000-01-01",
    }
    with open(man, "w", encoding="utf-8") as f:
        json.dump(bench, f, indent=2)
    with open(man, "rb") as f:
        bench_before = f.read()

    # SAME: full match, prefix match, a role not given
    rc, out = run("--manifest", man, "--manual-log", a, "--gl", b, "--class-data", c)
    check("SAME exit 3", rc == 3)
    check("SAME last line", out[-1] == "RESULT: SAME")
    check("prefix match SAME", ("class_data SAME " + mc) in out)
    check("NOT GIVEN line", "rick_budget NOT GIVEN" in out)

    # CHANGED
    rc, out = run("--manifest", man, "--manual-log", b)
    check("CHANGED exit 0", rc == 0)
    check("CHANGED last line", out[-1] == "RESULT: CHANGED")
    check("CHANGED line", ("manual_log CHANGED %s -> %s" % (ma, mb)) in out)

    # MISSING -> STOP
    gone = os.path.join(BENCH, "no-such-file.bin")
    rc, out = run("--manifest", man, "--gl", gone, "--manual-log", a)
    check("STOP exit 1", rc == 1)
    check("STOP last line", out[-1] == "RESULT: STOP")
    check("MISSING line", ("gl MISSING " + gone) in out)

    # unreadable manifest -> STOP
    bad = os.path.join(BENCH, "bad.json")
    write(bad, b"{not json")
    rc, out = run("--manifest", bad, "--gl", b)
    check("bad manifest STOP", rc == 1 and out[-1] == "RESULT: STOP")

    # no --record writes nothing
    with open(man, "rb") as f:
        check("no write without --record", f.read() == bench_before)

    # --record writes only the bench copy
    rc, out = run("--manifest", man, "--rick-budget", c, "--record")
    check("record run CHANGED", rc == 0 and out[-1] == "RESULT: CHANGED")
    with open(man, "r", encoding="utf-8") as f:
        after = json.load(f)
    check("record md5 full", after["roles"]["rick_budget"]["md5_full"] == mc)
    check("record date not old", after["recorded"] != "2000-01-01")
    check("record kept other roles", after["roles"]["manual_log"]["md5_full"] == ma)
    rc, out = run("--manifest", man, "--rick-budget", c)
    check("after record SAME", rc == 3)

    # repairs of the blind check (2026-11-21): short prefix, bad argument, no source, one path twice, read-only record
    for pre in ("", "f", "0cc175"):
        short = os.path.join(BENCH, "short.json")
        bad2 = json.loads(json.dumps(bench)); bad2["roles"]["class_data"]["md5"] = pre
        with open(short, "w", encoding="utf-8") as f:
            json.dump(bad2, f)
        rc, out = run("--manifest", short, "--class-data", c)
        check("prefix %r STOP" % pre, rc == 1 and out[-1] == "RESULT: STOP")
    rc, out = run("--manifest", man, "--classdata", c)
    check("bad argument STOP exit 1", rc == 1 and out[-1] == "RESULT: STOP")
    rc, out = run("--manifest", man)
    check("no source STOP", rc == 1 and out[-1] == "RESULT: STOP")
    rc, out = run("--manifest", man, "--manual-log", a, "--gl", a)
    check("one path two roles STOP", rc == 1 and out[-1] == "RESULT: STOP")
    up = json.loads(json.dumps(bench)); up["roles"]["gl"]["md5_full"] = mb.upper()
    upm = os.path.join(BENCH, "upper.json")
    with open(upm, "w", encoding="utf-8") as f:
        json.dump(up, f)
    rc, out = run("--manifest", upm, "--gl", b)
    check("uppercase md5_full SAME", rc == 3)
    ro = os.path.join(BENCH, "ro")
    os.makedirs(ro, exist_ok=True)
    rom = os.path.join(ro, "SOURCES.json")
    shutil.copy(man, rom)
    with open(rom, "rb") as f:
        ro_before = f.read()
    os.chmod(rom, 0o444)
    rc, out = run("--manifest", rom, "--gl", a, "--record")
    os.chmod(rom, 0o666)
    with open(rom, "rb") as f:
        check("read-only record STOP, manifest whole", rc == 1 and out[-1] == "RESULT: STOP" and f.read() == ro_before)

    # a failed swap leaves no temp file beside the manifest (recheck finding, 2026-11-21)
    sw = os.path.join(BENCH, "swap")
    os.makedirs(sw, exist_ok=True)
    swm = os.path.join(sw, "SOURCES.json")
    shutil.copy(man, swm)
    code = ("import os,sys,runpy;os.replace=lambda *x:(_ for _ in ()).throw(PermissionError());"
            "sys.argv=[%r,'--manifest',%r,'--gl',%r,'--record'];runpy.run_path(%r,run_name='__main__')" % (PROG, swm, a, PROG))
    p = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True)
    check("failed swap STOP, no temp left", p.returncode == 1 and p.stdout.strip().splitlines()[-1] == "RESULT: STOP"
          and sorted(os.listdir(sw)) == ["SOURCES.json"])

    with open(REAL, "rb") as f:
        check("real manifest unchanged byte for byte", f.read() == real_before)

    print("RESULT: PASS" if not fails else "RESULT: FAIL (%d)" % len(fails))
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
