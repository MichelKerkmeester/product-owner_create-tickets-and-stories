#!/usr/bin/env python3
"""Compare two skill-side playbook runs scenario by scenario, mechanically.

Usage: compare_runs.py <playbook dir> <run A> <run B> [--csv out.csv]

For each scenario both runs carry, this reads what each turn saved, whether turn 1
saved a clarification and nothing else, whether every reply carries the
`Verified: read-back succeeded` and `HVR self-scan:` lines, how many of the
backticked values the scenario's Expected signals name appear in the final
deliverables, and what the shared output-format gate says about each deliverable.
It judges nothing a reader has to judge. A row where the runs differ is the list a
reader opens.
"""
import csv, glob, json, os, re, subprocess, sys

PLAYBOOK, RUN_A, RUN_B = sys.argv[1:4]
OUT = sys.argv[sys.argv.index("--csv") + 1] if "--csv" in sys.argv else None
GATE = os.path.join(os.path.dirname(os.path.abspath(__file__)), *[".."] * 5,
                    "z — Claude Project Sync Loop", "validate-output-format.cjs")


def scenario_values(sid):
    for path in glob.glob(os.path.join(PLAYBOOK, "skill-*", "*.md")):
        text = open(path, encoding="utf-8").read()
        if re.search(rf"\b{sid}\b", text[:600]):
            m = re.search(r"^- Expected signals:(.+)$", text, re.M)
            vals = re.findall(r"`([^`]{2,60})`", m.group(1)) if m else []
            # file paths, rule citations and line labels are about the run, not the artifact
            return sorted({v for v in vals if not re.search(r"\.md$|^export/|^references/|^assets/|^AGENTS|^SKILL|HVR self-scan|Verified|\[###\]", v)})
    return []


def run_row(run, sid):
    dirs = glob.glob(os.path.join(run, "skill", f"{sid} - *"))
    if not dirs:
        return None
    d = dirs[0]
    meta = json.load(open(os.path.join(d, "meta.json")))
    turns = []
    for t in meta["turns"]:
        reply = open(os.path.join(d, f"turn-{t['turn']}.md"), encoding="utf-8").read()
        created = [p for p in t.get("ledger", {}).get("created", []) if p.startswith("export/")]
        turns.append({
            "created": created,
            "verified": "Verified: read-back succeeded" in reply,
            "selfscan": "HVR self-scan:" in reply,
        })
    exports = sorted(glob.glob(os.path.join(d, "exports", "export", "**", "*.md"), recursive=True))
    finals = [p for p in exports if "-clarification" not in os.path.basename(p)]
    body = "\n".join(open(p, encoding="utf-8").read() for p in finals)
    vals = scenario_values(sid)
    kept = [v for v in vals if v in body]
    first = turns[0]["created"] if turns else []
    return {
        "completed": meta["completed"],
        "turns": len(turns),
        "t1_asks": bool(first) and all("-clarification" in p for p in first),
        "t1_drafts": any("-clarification" not in p for p in first),
        "files": len(exports),
        "verified_all": all(t["verified"] for t in turns),
        "selfscan_all": all(t["selfscan"] for t in turns),
        "values": f"{len(kept)}/{len(vals)}",
        "missing": "; ".join(v for v in vals if v not in kept)[:300],
        "gate_failed_files": sum(1 for p in finals if subprocess.run(["node", GATE, "--system", "product-owner", p], capture_output=True).returncode),
    }


ids = sorted({os.path.basename(p).split(" - ")[0] for p in glob.glob(os.path.join(RUN_A, "skill", "*"))}
             | {os.path.basename(p).split(" - ")[0] for p in glob.glob(os.path.join(RUN_B, "skill", "*"))})
rows = []
for sid in ids:
    a, b = run_row(RUN_A, sid), run_row(RUN_B, sid)
    keys = ("completed", "turns", "t1_asks", "t1_drafts", "files", "verified_all", "selfscan_all", "values", "gate_failed_files")
    diff = [k for k in keys if (a or {}).get(k) != (b or {}).get(k)]
    rows.append({"id": sid, **{f"A_{k}": (a or {}).get(k) for k in keys + ("missing",)},
                 **{f"B_{k}": (b or {}).get(k) for k in keys + ("missing",)}, "differs": ",".join(diff)})
    print(f"{sid:8} A t1ask={a and a['t1_asks']!s:5} vals={a and a['values']!s:6} gate={a and a['gate_failed_files']!s:2} ver={a and a['verified_all']!s:5} scan={a and a['selfscan_all']!s:5} | "
          f"B t1ask={b and b['t1_asks']!s:5} vals={b and b['values']!s:6} gate={b and b['gate_failed_files']!s:2} ver={b and b['verified_all']!s:5} scan={b and b['selfscan_all']!s:5} | {','.join(diff)}")
if OUT:
    with open(OUT, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
