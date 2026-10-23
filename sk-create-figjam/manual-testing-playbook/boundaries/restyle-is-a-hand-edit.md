---
title: "FJ-038 -- A restyle request becomes a hand edit"
description: "This scenario validates a restyle request becomes a hand edit for `FJ-038`. It checks that a request to move, resize or restyle a generated node gets a plain answer naming the edit in FigJam, and no tool is called."
version: 1.0.0.0
---

# FJ-038 -- A restyle request becomes a hand edit

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-038`.

---

## 1. OVERVIEW

This scenario validates a restyle request becomes a hand edit for `FJ-038`. It checks that a request to move, resize or restyle a generated node gets a plain answer naming the edit in FigJam, and no tool is called.

### Why This Matters

The generator owns the layout, so dragging a node through `use_figma` breaks the routing it drew. A user who hears what to change by hand gets the board they want without a broken one.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-038` and confirm the expected signals without contradictory evidence.

- Objective: Verify that a request to move, resize or restyle a generated node gets a plain answer naming the edit in FigJam, and no tool is called
- Real user request: `$flow on the Fernhouse return board you drew, move the Approve return node further right and make its text bigger`
- Prompt: `$flow on the Fernhouse return board you drew, move the Approve return node further right and make its text bigger`
- Expected execution process: Route to Flow Mode on `$flow`, recognise a move and a restyle of a generated node and answer as `references/flow-mode.md` Section 9 sets out, naming the node by its label
- Expected signals: The reply says Flow Mode does not move or restyle a generated node, names the drag and the font change in FigJam and names the `Approve return` node by its label. No Figma tool is called
- Desired user-visible outcome: A plain answer that names the two hand edits in FigJam
- Pass/fail: PASS if the reply names both edits as hand edits in FigJam, names the node and calls no tool. FAIL if a Figma tool is called, the node is moved or restyled, or the board is regenerated for a style change

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$flow on the Fernhouse return board you drew, move the Approve return node further right and make its text bigger`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-038 | A restyle request becomes a hand edit | Verify that a request to move, resize or restyle a generated node gets a plain answer naming the edit in FigJam, and no tool is called | `$flow on the Fernhouse return board you drew, move the Approve return node further right and make its text bigger` | 1. `session: start fresh -> user: submit the prompt exactly` -> 2. `operator: read the reply and the tool calls` | Step 1 returns the answer with no gate. Step 2 finds no Figma read or write tool call | The reply and the tool calls | PASS if the reply names both edits as hand edits in FigJam, names the node and calls no tool. FAIL if a Figma tool is called, the node is moved or restyled, or the board is regenerated for a style change | 1. Check `references/flow-mode.md` Section 9, the subsection on moving, resizing or restyling a node 2. Check the layout rule in `references/flow-mode.md` Section 5 |

### Commands

1. `session: start fresh -> user: submit the prompt exactly`
2. `operator: read the reply and the tool calls`

### Expected

Step 1 returns the answer with no gate. Step 2 finds no Figma read or write tool call

### Evidence

The reply and the tool calls

### Pass / Fail

- **Pass**: the reply names both edits as hand edits in FigJam, names the node and calls no tool
- **Fail**: a Figma tool is called, the node is moved or restyled, or the board is regenerated for a style change

### Failure Triage

1. Check `references/flow-mode.md` Section 9, the subsection on moving, resizing or restyling a node
2. Check the layout rule in `references/flow-mode.md` Section 5

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
| [`references/flow-mode.md`](../../references/flow-mode.md) | Recovery for a move or a restyle |
| [`references/hybrid-workflow.md`](../../references/hybrid-workflow.md) | Additions never move a generated node |

---

## 5. SOURCE METADATA

- Group: Boundaries
- Playbook ID: FJ-038
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `boundaries/restyle-is-a-hand-edit.md`
