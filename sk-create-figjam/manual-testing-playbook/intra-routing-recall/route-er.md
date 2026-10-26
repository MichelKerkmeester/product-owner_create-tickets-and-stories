---
id: FJR-006
category: intra_routing_recall
stage: routing
title: "FJR-006 -- ER routing"
description: "This scenario validates ER routing for `FJR-006`. It checks that a request for a FigJam ER diagram reaches `sk-create-figjam` at the hub and resolves the Flow pair, the ER files and the quality rubric as leaves, with the rubric loading before the gate."
expected_intent: sk-create-figjam
expected_resources:
  - sk-create-figjam/references/flow-mode.md
  - sk-create-figjam/assets/flow-templates.md
  - sk-create-figjam/references/types/er.md
  - sk-create-figjam/assets/templates/er.md
  - sk-create-figjam/references/quality-rubric.md
expected_workflow_mode: sk-create-figjam
expected_leaf_resources:
  - workflow_mode: sk-create-figjam
    leaf_resource_id: references/flow-mode.md
  - workflow_mode: sk-create-figjam
    leaf_resource_id: assets/flow-templates.md
  - workflow_mode: sk-create-figjam
    leaf_resource_id: references/types/er.md
  - workflow_mode: sk-create-figjam
    leaf_resource_id: assets/templates/er.md
  - workflow_mode: sk-create-figjam
    leaf_resource_id: references/quality-rubric.md
version: 1.0.1.0
---

# FJR-006 -- ER routing

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJR-006`.

---

## 1. OVERVIEW

This scenario validates ER routing for `FJR-006`. It checks that a request for a FigJam ER diagram reaches `sk-create-figjam` at the hub and resolves the Flow pair, the ER files and the quality rubric as leaves, with the rubric loading before the gate.

### Why This Matters

Type detection decides which rules the model is held to. A wrong type loads the wrong reference and the check reads the block against the wrong grammar.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJR-006` and confirm the expected signals without contradictory evidence.

- Objective: Verify that a request for a FigJam ER diagram reaches `sk-create-figjam` at the hub and resolves the Flow pair, the ER files and the quality rubric as leaves, with the rubric loading before the gate
- Real user request: `make a FigJam ER diagram of the stays model from the schema note`
- Prompt: `make a FigJam ER diagram of the stays model from the schema note`
- Expected execution process: Hub stage one starts the request in `sk-create-figjam`, the hub `ROUTER.md` FLOW intent maps the Flow pair and `SKILL.md` Section 2 `TYPE_SIGNALS` matches `schema` and `er diagram` to `er` alone, then adds its files and the quality rubric
- Expected signals: The hub check passes with this prompt among its gold rows, the `TYPE_SIGNALS` row for the type carries a cue the prompt uses and every declared leaf exists in the packet and in `leaf-manifest.json`
- Desired user-visible outcome: The er rules load before any model is written
- Pass/fail: PASS if the hub routes the prompt to `sk-create-figjam`, the `TYPE_SIGNALS` row for `er` carries the `schema` cue and every leaf resolves. FAIL if the hub routes elsewhere, the `TYPE_SIGNALS` row or its cue is missing or a leaf is missing from the packet or the manifest

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `make a FigJam ER diagram of the stays model from the schema note`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJR-006 | ER routing | Verify that a request for a FigJam ER diagram reaches `sk-create-figjam` at the hub and resolves the Flow pair, the ER files and the quality rubric as leaves, with the rubric loading before the gate | `make a FigJam ER diagram of the stays model from the schema note` | 1. `bash: python3 benchmark/gates/check_hub.py` -> 2. `bash: grep -n -e '"er": (.*"schema"' sk-create-figjam/SKILL.md` -> 3. `bash: for p in references/flow-mode.md assets/flow-templates.md references/types/er.md assets/templates/er.md references/quality-rubric.md; do test -e "sk-create-figjam/$p" && grep -q "$p" leaf-manifest.json && echo "OK $p" // echo "MISS $p"; done` -> 4. `bash: node "$SKILLED/skills/sk-doc/sk-create-skill/scripts/validate-playbook-topology.cjs" --skill-dir . --dir sk-create-figjam/manual-testing-playbook` | Step 1 prints `PASSED the hub`. Step 2 prints the `TYPE_SIGNALS` row for `er`, which carries the `schema` cue. Step 3 prints `OK` for all 5 leaves. Step 4 prints `PASS  FJR-006` | The four command outputs with their exit status | PASS if the hub routes the prompt to `sk-create-figjam`, the `TYPE_SIGNALS` row for `er` carries the `schema` cue and every leaf resolves. FAIL if the hub routes elsewhere, the `TYPE_SIGNALS` row or its cue is missing or a leaf is missing from the packet or the manifest | 1. Check the gold row in `benchmark/hub-routing-cases.json` and the stage one rules in the hub `SKILL.md` 2. Regenerate `leaf-manifest.json` with `generate-leaf-manifest.cjs --write` when a leaf is missing from it |

### Commands

1. `bash: python3 benchmark/gates/check_hub.py`
2. `bash: grep -n -e '"er": (.*"schema"' sk-create-figjam/SKILL.md`
3. `bash: for p in references/flow-mode.md assets/flow-templates.md references/types/er.md assets/templates/er.md references/quality-rubric.md; do test -e "sk-create-figjam/$p" && grep -q "$p" leaf-manifest.json && echo "OK $p" || echo "MISS $p"; done`
4. `bash: node "$SKILLED/skills/sk-doc/sk-create-skill/scripts/validate-playbook-topology.cjs" --skill-dir . --dir sk-create-figjam/manual-testing-playbook`

### Expected

Step 1 prints `PASSED the hub`. Step 2 prints the `TYPE_SIGNALS` row for `er`, which carries the `schema` cue. Step 3 prints `OK` for all 5 leaves. Step 4 prints `PASS  FJR-006`

### Evidence

The four command outputs with their exit status

### Pass / Fail

- **Pass**: the hub routes the prompt to `sk-create-figjam`, the `TYPE_SIGNALS` row for `er` carries the `schema` cue and every leaf resolves
- **Fail**: the hub routes elsewhere, the `TYPE_SIGNALS` row or its cue is missing or a leaf is missing from the packet or the manifest

### Failure Triage

1. Check the gold row in `benchmark/hub-routing-cases.json` and the stage one rules in the hub `SKILL.md`
2. Regenerate `leaf-manifest.json` with `generate-leaf-manifest.cjs --write` when a leaf is missing from it

---

## 4. SOURCE FILES

### Playbook Sources

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and scenario summary |
| Feature catalog | No dedicated catalog entry: the packet has no feature catalog, so `SKILL.md` and the references below are the contract |

### Implementation And Test Anchors

| File | Role |
|---|---|
| [`SKILL.md`](../../SKILL.md) | Type detection and resource loading |
| [`references/types/er.md`](../../references/types/er.md) | The routed type reference |

---

## 5. SOURCE METADATA

- Group: Intra-routing recall
- Playbook ID: FJR-006
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `intra-routing-recall/route-er.md`
