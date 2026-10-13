"""Apply exact, counted substitutions to a file and record them for the residency resync."""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = os.path.join(HERE, "resync-pairs.json")


def apply(path, pairs, record=True):
    s = open(path, encoding="utf-8").read()
    for item in pairs:
        old, new = item[0], item[1]
        want = item[2] if len(item) > 2 else 1
        got = s.count(old)
        if want == "all":
            assert got >= 1, f"{path}: not found: {old[:80]!r}"
        else:
            assert got == want, f"{path}: expected {want}, found {got}: {old[:80]!r}"
        s = s.replace(old, new)
    open(path, "w", encoding="utf-8").write(s)
    if record:
        log = json.load(open(LOG)) if os.path.exists(LOG) else []
        for item in pairs:
            pair = [item[0], item[1]]
            if pair not in log:
                log.append(pair)
        json.dump(log, open(LOG, "w"), indent=1, ensure_ascii=False)
