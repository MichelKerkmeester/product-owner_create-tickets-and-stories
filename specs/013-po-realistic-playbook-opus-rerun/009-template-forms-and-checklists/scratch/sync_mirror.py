"""Carry line edits from a skill source (HEAD vs working tree) into its Project mirror.

Each replaced line pair is applied to every mirror line equal to the old line. Lines the
mirror words differently are reported as misses for a hand edit.
"""
import difflib, subprocess, sys

PO = "/Users/michelkerkmeester/MEGA/Development/AI Systems/AI Systems/Product Owner"


def sync(skill_rel, mirror_rel):
    old = subprocess.run(["git", "-C", PO, "show", f"HEAD:{skill_rel}"], capture_output=True,
                         text=True, check=True).stdout.splitlines()
    new = open(f"{PO}/{skill_rel}", encoding="utf-8").read().splitlines()
    mpath = f"{PO}/{mirror_rel}"
    mtext = open(mpath, encoding="utf-8").read()
    mlines = mtext.split("\n")
    misses, applied = [], 0
    sm = difflib.SequenceMatcher(a=old, b=new, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        if tag != "replace" or (i2 - i1) != (j2 - j1):
            misses.append((tag, old[i1:i2], new[j1:j2]))
            continue
        for o, n in zip(old[i1:i2], new[j1:j2]):
            if o.startswith(("title:", "version:", "# Product Owner")):
                continue
            hits = [k for k, line in enumerate(mlines) if line == o]
            if not hits:
                misses.append(("line", o, n))
            for k in hits:
                mlines[k] = n
                applied += 1
    open(mpath, "w", encoding="utf-8").write("\n".join(mlines))
    print(f"{mirror_rel.split('/')[-1]}: {applied} lines applied, {len(misses)} misses")
    for m in misses:
        print("  MISS", m[0], repr(m[1])[:160])
    return misses


if __name__ == "__main__":
    sync(sys.argv[1], sys.argv[2])
