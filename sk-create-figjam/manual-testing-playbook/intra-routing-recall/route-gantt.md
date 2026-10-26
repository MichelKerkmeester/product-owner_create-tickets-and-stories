---
id: FJR-007
category: intra_routing_recall
stage: routing
title: "FJR-007 -- Gantt routing"
description: "This scenario validates gantt routing for `FJR-007`. It checks that a request for a FigJam gantt reaches `sk-create-figjam` at the hub and resolves the Flow pair, the gantt files and the quality rubric as leaves, with the rubric loading before the gate."
expected_intent: sk-create-figjam
expected_resources:
  - sk-create-figjam/references/flow-mode.md
  - sk-create-figjam/assets/flow-templates.md
  - sk-create-figjam/references/types/gantt.md
  - sk-create-figjam/assets/templates/gantt.md
  - sk-create-figjam/references/quality-rubric.md
expected_workflow_mode: sk-create-figjam
expected_leaf_resources:
  - workflow_mode: sk-create-figjam
    leaf_resource_id: references/flow-mode.md
  - workflow_mode: sk-create-figjam
    leaf_resource_id: assets/flow-templates.md
  - workflow_mode: sk-create-figjam
    leaf_resource_id: references/types/gantt.md
  - workflow_mode: sk-create-figjam
    leaf_resource_id: assets/templates/gantt.md
  - workflow_mode: sk-create-figjam
    leaf_resource_id: references/quality-rubric.md
version: 1.0.1.0
---

# FJR-007 -- Gantt routing

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJR-007`.

---

## 1. OVERVIEW

This scenario validates gantt routing for `FJR-007`. It checks that a request for a FigJam gantt reaches `sk-create-figjam` at the hub and resolves the Flow pair, the gantt files and the quality rubric as leaves, with the rubric loading before the gate.

### Why This Matters

Type detection decides which rules the model is held to. A wrong type loads the wrong reference and the check reads the block against the wrong grammar.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJR-007` and confirm the expected signals without contradictory evidence.

- Objective: Verify that a request for a FigJam gantt reaches `sk-create-figjam` at the hub and resolves the Flow pair, the gantt files and the quality rubric as leaves, with the rubric loading before the gate
- Real user request: `put the launch plan on a FigJam gantt chart`
- Prompt: `put the launch plan on a FigJam gantt chart`
- Expected execution process: Hub stage one starts the request in `sk-create-figjam`, the hub `ROUTER.md` FLOW intent maps the Flow pair and `SKILL.md` Section 2 `TYPE_SIGNALS` matches `plan` and `gantt` to `gantt` alone, then adds its files and the quality rubric
- Expected signals: The hub check passes with this prompt among its gold rows, the `TYPE_SIGNALS` row for the type carries a cue the prompt uses and every declared leaf exists in the packet and in `leaf-manifest.json`
- Desired user-visible outcome: The gantt rules load before any model is written
- Pass/fail: PASS if the hub routes the prompt to `sk-create-figjam`, the `TYPE_SIGNALS` row for `gantt` carries the `plan` cue and every leaf resolves. FAIL if the hub routes elsewhere, the `TYPE_SIGNALS` row or its cue is missing or a leaf is missing from the packet or the manifest

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `put the launch plan on a FigJam gantt chart`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJR-007 | Gantt routing | Verify that a request for a FigJam gantt reaches `sk-create-figjam` at the hub and resolves the Flow pair, the gantt files and the quality rubric as leaves, with the rubric loading before the gate | `put the launch plan on a FigJam gantt chart` | 1. `bash: python3 benchmark/gates/check_hub.py` -> 2. `bash: grep -n -e '"gantt": (.*"plan"' sk-create-figjam/SKILL.md` -> 3. `bash: for p in references/flow-mode.md assets/flow-templates.md references/types/gantt.md assets/templates/gantt.md references/quality-rubric.md; do test -e "sk-create-figjam/$p" && grep -q "$p" leaf-manifest.json && echo "OK $p" // echo "MISS $p"; done` -> 4. `bash: node "$SKILLED/skills/sk-doc/sk-create-skill/scripts/validate-playbook-topology.cjs" --skill-dir . --dir sk-create-figjam/manual-testing-playbook` | Step 1 prints `PASSED the hub`. Step 2 prints the `TYPE_SIGNALS` row for `gantt`, which carries the `plan` cue. Step 3 prints `OK` for all 5 leaves. Step 4 prints `PASS  FJR-007` | The four command outputs with their exit status | PASS if the hub routes the prompt to `sk-create-figjam`, the `TYPE_SIGNALS` row for `gantt` carries the `plan` cue and every leaf resolves. FAIL if the hub routes elsewhere, the `TYPE_SIGNALS` row or its cue is missing or a leaf is missing from the packet or the manifest | 1. Check the gold row in `benchmark/hub-routing-cases.json` and the stage one rules in the hub `SKILL.md` 2. Regenerate `leaf-manifest.json` with `generate-leaf-manifest.cjs --write` when a leaf is missing from it |

### Commands

1. `bash: python3 benchmark/gates/check_hub.py`
2. `bash: grep -n -e '"gantt": (.*"plan"' sk-create-figjam/SKILL.md`
3. `bash: for p in references/flow-mode.md assets/flow-templates.md references/types/gantt.md assets/templates/gantt.md references/quality-rubric.md; do test -e "sk-create-figjam/$p" && grep -q "$p" leaf-manifest.json && echo "OK $p" || echo "MISS $p"; done`
4. `bash: node "$SKILLED/skills/sk-doc/sk-create-skill/scripts/validate-playbook-topology.cjs" --skill-dir . --dir sk-create-figjam/manual-testing-playbook`

### Expected

Step 1 prints `PASSED the hub`. Step 2 prints the `TYPE_SIGNALS` row for `gantt`, which carries the `plan` cue. Step 3 prints `OK` for all 5 leaves. Step 4 prints `PASS  FJR-007`

### Evidence

The four command outputs with their exit status

### Pass / Fail

- **Pass**: the hub routes the prompt to `sk-create-figjam`, the `TYPE_SIGNALS` row for `gantt` carries the `plan` cue and every leaf resolves
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
| [`references/types/gantt.md`](../../references/types/gantt.md) | The routed type reference |

---

## 5. SOURCE METADATA

- Group: Intra-routing recall
- Playbook ID: FJR-007
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `intra-routing-recall/route-gantt.md`
