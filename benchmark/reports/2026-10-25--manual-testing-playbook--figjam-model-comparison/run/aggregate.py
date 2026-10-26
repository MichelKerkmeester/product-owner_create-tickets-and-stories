"""Merge the seven grader files into the run's results.jsonl and print the per-model and per-type tables.

Each row keeps the grader's own score and verdict, and adds the reconciled score where two graders read one
rubric line two ways, the strict verdict the root playbook's acceptance rule gives (any missing expected signal
fails) and whether the row is its type's gallery board under the gallery rule.

Usage: python3 run/aggregate.py <run folder>
"""
import collections, json, os, sys

RUN = sys.argv[1]
HERE = os.path.join(RUN, "run")
IDS = ["FJ-022", "FJ-023", "FJ-024", "FJ-025", "FJ-026", "FJ-027", "FJ-028"]
TYPES = {"FJ-022": "user flow", "FJ-023": "process", "FJ-024": "architecture", "FJ-025": "sequence",
         "FJ-026": "state", "FJ-027": "ER", "FJ-028": "gantt"}
FINALS = json.load(open(os.path.join(HERE, "finals.json")))
PREFIX = "AI Systems/Product Owner/benchmark/reports/" + os.path.basename(RUN.rstrip("/")) + "/"
FULL = ("composition", "fidelity", "reply", "hygiene_no_node_touched", "hygiene_no_label_covered",
        "hygiene_nothing_else_changed", "hygiene_nothing_exported")
# Two graders read "every count true" two ways for a Finding that undercounts earlier same-title boards.
# The brief counts those boards against no model, so the reconciled score reads the rule as the measured
# Read-back counts only, the reading the FJ-023 grader applied to two runs.
RECONCILE = {("FJ-022", "swe"): ("reply", 2, "The Finding undercounts the earlier same-title boards. The brief "
                                 "counts those boards against no model and the FJ-023 grader scored the same "
                                 "undercount as no loss on two runs, so Reply is reconciled to 2")}


def scorecard_pass(s):
    return s["total"] >= 18 and all(s[k] == (2 if k in ("composition", "fidelity", "reply") else 1) for k in FULL) \
        and all(v != 0 for k, v in s.items() if k != "total")


def rel(p):
    p = p.replace(PREFIX, "")
    if p.startswith("r038/shots/ov/"):
        return "renders/" + p.split("/")[-1]
    if p.startswith("r038/grades/"):
        return "grades/" + p.split("/")[-1]
    return p


rows = []
for sid in IDS:
    for line in open(os.path.join(RUN, "grades", f"{sid}.jsonl"), encoding="utf-8"):
        d = json.loads(line)
        s = dict(d["scorecard"])
        row = {"id": sid, "type": TYPES[sid], "model": d["model"], "board": d["board"],
               "renders": [f"renders/{d['model']}-{sid}-{n}.png" for n in FINALS[sid][d["model"]]],
               "graded": {"verdict": d["verdict"], "total": s["total"]}}
        note = RECONCILE.get((sid, d["model"]))
        if note:
            key, value, why = note
            s[key] = value
            s["total"] = sum(v for k, v in s.items() if k != "total")
            row["reconciled"] = {"item": key, "score": value, "why": why}
        row["total"] = s["total"]
        # A write before the gate fails a run whatever its scorecard, so only a reconciled row is recomputed
        row["verdict"] = ("PASS" if scorecard_pass(s) else "FAIL") if note else d["verdict"]
        if not note and (scorecard_pass(s) != (d["verdict"] == "PASS")):
            print("verdict differs from scorecard:", sid, d["model"], d["verdict"], s["total"])
        missing = [x["signal"] for x in d["signals"] if not x["met"] and not x["signal"].startswith(("Scorecard", "Extra"))]
        row["strict_verdict"] = "PASS" if row["verdict"] == "PASS" and not missing else "FAIL"
        row["missing_signals"] = missing
        row.update({"rank": d["rank"], "reason": d["reason"], "scorecard": s, "losses": d["losses"],
                    "signals": d["signals"], "turns": d["turns"],
                    "evidence": sorted({rel(p) for p in d["evidence"] if not p.startswith(("/var/", "r038/shots/full",
                                                                                          "r038/shots/grey"))})})
        rows.append(row)

# The gallery rule: the most of the 16 board points a viewer sees, then the highest total, then a pass under
# the current playbook, which needs every expected signal, then fewer supplementary and adaptive turns. Every
# run used the three scripted turns, so a tie that survives those falls to the grader's rank.
BOARD = ("composition", "crossings", "shared_trunks", "label_collisions", "fidelity", "legibility", "signal", "clarity")
for sid in IDS:
    group = [r for r in rows if r["id"] == sid]
    best = min(group, key=lambda r: (-sum(r["scorecard"][k] for k in BOARD), -r["total"], r["strict_verdict"] != "PASS",
                                     r["turns"]["supplementary"], r["turns"]["adaptive"], r["rank"]))
    for r in group:
        r["gallery"] = r is best

# Rows of models this script does not aggregate stay, because a rerun rebuilds only the three below.
path = os.path.join(RUN, "results.jsonl")
kept = []
if os.path.exists(path):
    with open(path, encoding="utf-8") as fh:
        kept = [line for line in fh if line.strip() and json.loads(line).get("model") not in ("deepseek", "glm", "swe")]
with open(path, "w", encoding="utf-8") as fh:
    for r in rows:
        fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    fh.writelines(kept)

by = collections.defaultdict(list)
for r in rows:
    by[r["model"]].append(r)
for m in ("deepseek", "glm", "swe"):
    rs = by[m]
    print(m, "total", sum(r["total"] for r in rs), "pass", sum(r["verdict"] == "PASS" for r in rs),
          "strict", sum(r["strict_verdict"] == "PASS" for r in rs), "rank sum", sum(r["rank"] for r in rs),
          "firsts", sum(r["rank"] == 1 for r in rs), "gallery", sum(r["gallery"] for r in rs))
for r in rows:
    print(r["id"], r["model"], r["total"], r["verdict"], r["strict_verdict"], "rank", r["rank"], "GALLERY" if r["gallery"] else "")
