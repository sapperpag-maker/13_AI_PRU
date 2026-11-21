"""Tell whether any source of PRU's 2027 planner changed since the last build, by md5.

Only hashes each file's bytes; never parses a file's content.
Usage: python pru_sources_check.py [--class-data P] [--manual-log P] [--gl P]
       [--rick-budget P] [--manifest P] [--record]
Last line: RESULT: CHANGED (exit 0), RESULT: SAME (exit 3), RESULT: STOP (exit 1).
"""
import argparse
import datetime
import hashlib
import json
import os
import re
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_MANIFEST = os.path.join(HERE, "SOURCES.json")
ROLES = ["class_data", "manual_log", "gl", "rick_budget"]


def md5_of(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def stop(msg):
    print(msg)
    print("RESULT: STOP")
    return 1


class Parser(argparse.ArgumentParser):
    def error(self, message):  # a bad argument ends in STOP, exit 1, never argparse's 2
        print("BAD ARGUMENTS: %s" % message)
        print("RESULT: STOP")
        sys.exit(1)


HEX = re.compile(r"^[0-9a-f]+$")


def main(argv=None):
    ap = Parser()
    for role in ROLES:
        ap.add_argument("--" + role.replace("_", "-"), dest=role, default=None)
    ap.add_argument("--manifest", default=DEFAULT_MANIFEST)
    ap.add_argument("--record", action="store_true")
    a = ap.parse_args(argv)

    try:
        with open(a.manifest, "r", encoding="utf-8") as f:
            manifest = json.load(f)
        roles = manifest["roles"]
        for role in ROLES:
            full = roles[role].get("md5_full")
            key = str(full if full else roles[role]["md5"]).lower()
            if not HEX.match(key) or len(key) not in ((32,) if full else (8, 32)):
                raise ValueError(role + " md5 is not 8 or 32 hex characters")
    except Exception as e:  # unreadable or wrong shape
        return stop("MANIFEST UNREADABLE %s (%s: %s)" % (a.manifest, type(e).__name__, e))

    given = [getattr(a, r) for r in ROLES if getattr(a, r) is not None]
    if not given:
        return stop("NO SOURCE GIVEN: nothing to check")
    norm = [os.path.normcase(os.path.abspath(g)) for g in given]
    if len(set(norm)) != len(norm):
        return stop("ONE PATH GIVEN FOR TWO ROLES")

    changed = missing = False
    new = {}
    for role in ROLES:
        path = getattr(a, role)
        if path is None:
            print("%s NOT GIVEN" % role)
            continue
        if not os.path.isfile(path):
            print("%s MISSING %s" % (role, path))
            missing = True
            continue
        try:
            cur = md5_of(path)
        except OSError as e:
            print("%s UNREADABLE %s (%s)" % (role, path, type(e).__name__))
            missing = True
            continue
        new[role] = (cur, os.path.basename(path))
        entry = roles[role]
        full = entry.get("md5_full")
        old = str(full if full else entry["md5"]).lower()
        same = (cur == old) if full else cur.startswith(old)
        if same:
            print("%s SAME %s" % (role, cur))
        else:
            print("%s CHANGED %s -> %s" % (role, old, cur))
            changed = True

    if missing:
        print("RESULT: STOP")
        return 1

    if a.record:
        for role, (cur, name) in new.items():
            roles[role]["md5"] = cur
            roles[role]["md5_full"] = cur
            roles[role]["name"] = name
        manifest["recorded"] = datetime.date.today().isoformat()
        if not os.access(a.manifest, os.W_OK):
            return stop("RECORD FAILED %s (not writable)" % a.manifest)
        folder = os.path.dirname(os.path.abspath(a.manifest))
        tmp = None
        try:  # write a temp file beside it, then swap, so a failure never cuts the manifest short
            fd, tmp = tempfile.mkstemp(dir=folder, suffix=".tmp")
            with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as f:
                json.dump(manifest, f, indent=2)
                f.write("\n")
            os.replace(tmp, a.manifest)
        except OSError as e:
            if tmp and os.path.exists(tmp):  # our own temp file, never the manifest
                try:
                    os.remove(tmp)
                except OSError:
                    pass
            return stop("RECORD FAILED %s (%s)" % (a.manifest, type(e).__name__))
        print("RECORDED %s" % a.manifest)

    if changed:
        print("RESULT: CHANGED")
        return 0
    print("RESULT: SAME")
    return 3


if __name__ == "__main__":
    sys.exit(main())
