---
title: "FJ-037 -- An artifact and its board as an ordered pair"
description: "This scenario validates an artifact and its board as an ordered pair for `FJ-037`. It checks that a Story asked for beside a FigJam flow is written and exported first, then Flow Mode runs from it with its own gate, and after a matched read-back the board link lands in the re-saved Story before ClickUp is offered."
version: 1.0.0.0
---

# FJ-037 -- An artifact and its board as an ordered pair

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-037`.

---

## 1. OVERVIEW

This scenario validates an artifact and its board as an ordered pair for `FJ-037`. It checks that a Story asked for beside a FigJam flow is written and exported first, then Flow Mode runs from it with its own gate, and after a matched read-back the board link lands in the re-saved Story before ClickUp is offered.

### Why This Matters

A board named beside an artifact used to be read as the artifact's subject, so the board was dropped. The reader asked for both, and the diagram has to follow the document rather than replace it.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-037` and confirm the expected signals without contradictory evidence.

- Objective: Verify that a Story asked for beside a FigJam flow is written and exported first, then Flow Mode runs from it with its own gate, and after a matched read-back the board link lands in the re-saved Story before ClickUp is offered
- Real user request: `write a story for the Fernhouse return flow and make a FigJam flow of its screens`
- Prompt: `write a story for the Fernhouse return flow and make a FigJam flow of its screens`
- Expected execution process: Hub stage one keeps the request in the Product Owner packet, whose router returns `STORY` with `then: "FLOW"`. The Story is written, exported and read back first, then the request hands off to this packet with the Story as its product-doc source
- Expected signals: The first reply delivers a Story with its export and read-back line, then starts Flow Mode from that Story and ends on Flow Mode's own gate with no ClickUp offer. No Figma write tool is called before that yes. After the yes and a matched read-back, the board URL sits in the Story's `Flows` group, the Story is saved again at its export path and the read-back line ends with its file name
- Desired user-visible outcome: A Story, a gate for a FigJam board drawn from its screens, then the Story re-saved with the board link
- Pass/fail: PASS if the Story is exported and read back first, Flow Mode starts from it, its gate waits for a yes with no ClickUp offer before it, and a matched board link lands in the re-saved Story. FAIL if a board is written before the Story is read back, the board is dropped, the Story is replaced by a board, ClickUp is offered before the link is in, or the saved Story lacks the matched link

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `write a story for the Fernhouse return flow and make a FigJam flow of its screens`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-037 | An artifact and its board as an ordered pair | Verify that a Story asked for beside a FigJam flow is written and exported first, then Flow Mode runs from it with its own gate, and after a matched read-back the board link lands in the re-saved Story before ClickUp is offered | `write a story for the Fernhouse return flow and make a FigJam flow of its screens` | 1. `session: start fresh -> user: submit the prompt exactly` -> 2. `operator: read the reply, export/ and the tool calls` -> 3. `user: reply yes at the gate, with a Figma connection that writes diagrams` -> 4. `operator: read the reply and the Story in export/` | Step 1 returns the Story's delivery and then a Flow Mode gate with no ClickUp offer. Step 2 finds the Story in `export/` and no Figma write before a yes. Step 3 returns the board URL and a read-back line ending with the Story's file name. Step 4 finds the board URL in the Story's `Flows` group. Without a Figma connection steps 3 and 4 are skipped and recorded as such | The reply, the `export/` listing and the tool calls | PASS if the Story is exported and read back first, Flow Mode starts from it, its gate waits for a yes with no ClickUp offer before it, and a matched board link lands in the re-saved Story. FAIL if a board is written before the Story is read back, the board is dropped, the Story is replaced by a board, ClickUp is offered before the link is in, or the saved Story lacks the matched link | 1. Check the gold row `a story with a FigJam flow beside it` with `python3 benchmark/gates/check_hub.py` 2. Check `python3 benchmark/router/route_contract.py` for the `then` field and the ordered pair rule in `../sk-product-owner/references/routing.md` step 5 |

### Commands

1. `session: start fresh -> user: submit the prompt exactly`
2. `operator: read the reply, export/ and the tool calls`
3. `user: reply yes at the gate, with a Figma connection that writes diagrams`
4. `operator: read the reply and the Story in export/`

### Expected

Step 1 returns the Story's delivery and then a Flow Mode gate with no ClickUp offer. Step 2 finds the Story in `export/` and no Figma write before a yes. Step 3 returns the board URL and a read-back line ending with the Story's file name. Step 4 finds the board URL in the Story's `Flows` group. Without a Figma connection steps 3 and 4 are skipped and recorded as such

### Evidence

The reply, the `export/` listing and the tool calls

### Pass / Fail

- **Pass**: the Story is exported and read back first, Flow Mode starts from it, its gate waits for a yes with no ClickUp offer before it, and a matched board link lands in the re-saved Story
- **Fail**: a board is written before the Story is read back, the board is dropped, the Story is replaced by a board, ClickUp is offered before the link is in, or the saved Story lacks the matched link

### Failure Triage

1. Check the gold row `a story with a FigJam flow beside it` with `python3 benchmark/gates/check_hub.py`
2. Check `python3 benchmark/router/route_contract.py` for the `then` field and the ordered pair rule in `../sk-product-owner/references/routing.md` step 5

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
| [`SKILL.md`](../../SKILL.md) | Primary detection signal |
| [`../sk-product-owner/references/routing.md`](../../../sk-product-owner/references/routing.md) | The ordered pair |
| [`references/flow-mode.md`](../../references/flow-mode.md) | The `Flows` group and the re-save in delivery |
| [`../sk-product-owner/assets/interactive-response-templates.md`](../../../sk-product-owner/assets/interactive-response-templates.md) | The closing line of a pair reply |

---

## 5. SOURCE METADATA

- Group: Boundaries
- Playbook ID: FJ-037
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `boundaries/artifact-plus-board-pair.md`
