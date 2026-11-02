"""Build [old, new] statement pairs for every Product Owner statement a home lost.

Each edit this phase made stayed on its own line, so line i of a home at HEAD maps to
line i of the edited home. A statement found inside old line i is re-read from new
line i by keeping the unchanged text on either side of it.
"""
import json, subprocess, sys
from pathlib import Path

AIS = Path("/Users/michelkerkmeester/MEGA/Development/AI Systems/AI Systems")
PO = AIS / "Product Owner"
sys.path.insert(0, str(Path(__file__).parent))
import precheck_residency as pr

ns = pr.gate_namespace()
decl = ns["SYSTEMS"]["product-owner"]
fold = lambda t: " ".join(t.split())
KERNEL = PO / "claude project" / "Custom Instructions.md"

def head_text(path):
    rel = path.relative_to(PO).as_posix()
    # a renamed mirror is read at HEAD under its old name
    old = subprocess.run(["git", "-C", str(PO), "diff", "--cached", "--name-status", "-M"], capture_output=True, text=True).stdout
    candidates = [rel]
    for line in old.splitlines():
        parts = line.split("\t")
        if parts[0].startswith("R") and parts[2] == rel:
            candidates.insert(0, parts[1])
    for c in candidates:
        r = subprocess.run(["git", "-C", str(PO), "show", f"HEAD:{c}"], capture_output=True, text=True)
        if r.returncode == 0:
            return r.stdout
    raise SystemExit(f"no HEAD copy for {rel}")

def entries(o):
    if isinstance(o, dict):
        if "statement" in o and "statement_key" in o:
            yield o
        for v in o.values():
            yield from entries(v)
    elif isinstance(o, list):
        for v in o:
            yield from entries(v)

pairs, unresolved = [], []
for e in entries(decl):
    st = e["statement"]
    homes = [KERNEL]
    if e.get("home"):
        homes.insert(0, PO / e["home"])
    live = [h for h in homes if h.exists()]
    texts = {h: h.read_text() for h in live}
    if any(fold(st) in fold(t) for t in texts.values()):
        continue
    new_st = None
    for h in live:
        old_lines = head_text(h).split("\n")
        new_lines = texts[h].split("\n")
        if len(old_lines) != len(new_lines):
            continue
        old_text = "\n".join(old_lines)
        at = old_text.find(st)
        if at >= 0:
            first = old_text.count("\n", 0, at)
            last = old_text.count("\n", 0, at + len(st))
            ol = "\n".join(old_lines[first:last + 1])
            nl = "\n".join(new_lines[first:last + 1])
            start = at - (old_text.rfind("\n", 0, at) + 1)
            pre = ol[:start]
            post = ol[start + len(st):]
            if nl.startswith(pre) and nl.endswith(post):
                new_st = nl[len(pre): len(nl) - len(post) if post else len(nl)]
        if new_st:
            break
    if new_st is None:
        unresolved.append(st[:90])
    else:
        pairs.append([st, new_st])
print(len(pairs), "pairs,", len(unresolved), "unresolved")
for u in unresolved:
    print("  UNRESOLVED", u)
json.dump(pairs, open(Path(__file__).parent / "statement-pairs.json", "w"), indent=1, ensure_ascii=False)
