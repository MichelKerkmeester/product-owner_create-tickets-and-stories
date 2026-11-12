---
title: "FJ-050 -- A direct edit writes only after its own yes"
description: "This scenario validates a direct edit writes only after its own yes for `FJ-050`. It checks that a request to insert a column into an existing board ends on a gate with no tool call, and that the yes backs up the page, deletes nothing unasked, renders the changed region and reads back the edits the gate listed."
version: 1.0.0.0
---

# FJ-050 -- A direct edit writes only after its own yes

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-050`.

---

## 1. OVERVIEW

This scenario validates a direct edit writes only after its own yes for `FJ-050`. It checks that a request to insert a column into an existing board ends on a gate with no tool call, and that the yes backs up the page, deletes nothing unasked, renders the changed region and reads back the edits the gate listed.

### Why This Matters

A direct edit changes a board the user already works on, often one they edited by hand. Inserting a column shifts every node to its right, so one wrong move can break a board nobody can rebuild from a model. The backup page, the gate and the read-back are what make that write safe to undo.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-050` and confirm the expected signals without contradictory evidence.

- Objective: Verify that a direct edit is offered behind its own gate with no tool call, and that after the yes it backs up the page, deletes no node it did not create, renders the changed region and reads back the listed edits
- Real user request: `on the Fernhouse return board, add a Refund column between Inspect and Close, with one card "Send the refund" in the Finance lane, and keep my own edits`
- Prompt: `on the Fernhouse return board, add a Refund column between Inspect and Close, with one card "Send the refund" in the Finance lane, and keep my own edits`
- Setup: A FigJam file holding a Fernhouse return board with stage columns, at least one column to the right of Inspect, a key with line samples and one label the operator restyled by hand
- Expected execution process: Recognise a structural change on an existing board and answer as `references/flow-mode.md` Section 9, A direct edit, sets out. Turn 1 is the gate. After the yes, Turn 2 backs up the page, reads the board, inserts the column on the grid `references/style-guide.md` Section 7 sets, places every moved label again, renders the changed region and reads it back
- Expected signals: Turn 1 calls no tool. It names the insert as a change the model cannot carry, names the `Inspect` and `Close` columns by their labels, offers the edit in FigJam or a direct edit, lists the edits, the backup page, what the read-back will count and the rollback, and ends on one question about the write. Turn 2 creates a page with `figma.createPage()` named after the board's page with `(backup <date>)` before any node moves, and deletes no node it did not create. Every node right of Inspect moves by one column pitch, the stage and lane rects and the section widen to match, and the hand-restyled label keeps its weight and casing. The changed region is rendered with `node.screenshot()` inside a `use_figma` call and checked for overlaps, and the reply's read-back counts the column, the card and the moved nodes against the gate's list and names any that differ
- Desired user-visible outcome: A gate first, then a widened board with the new column, a backup page left for the user to delete and a read-back that matches the gate
- Pass/fail: PASS if Turn 1 calls no tool and ends on the gate's one question, and Turn 2 makes the backup page before the first move, deletes nothing unasked, keeps the hand edit and reads back counts that match the gate. FAIL if any Figma write runs before the yes, the backup page is missing or made after a move, a node the edit did not create is deleted, the board is composed again, or the read-back skips a listed edit

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `on the Fernhouse return board, add a Refund column between Inspect and Close, with one card "Send the refund" in the Finance lane, and keep my own edits`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-050 | A direct edit writes only after its own yes | Verify that a direct edit is offered behind its own gate with no tool call, and that after the yes it backs up the page, deletes no node it did not create, renders the changed region and reads back the listed edits | `on the Fernhouse return board, add a Refund column between Inspect and Close, with one card "Send the refund" in the Finance lane, and keep my own edits` | 1. `session: start fresh -> user: submit the prompt exactly` -> 2. `operator: read the reply and the tool calls` -> 3. `user: yes` -> 4. `operator: read the tool calls, the pages in the file and the reply` | Step 2 finds the gate and no tool call. Step 4 finds the backup page made before the first move, no unasked delete, a `node.screenshot()` render and a read-back that matches the gate | The replies, the tool calls, the file's page list and the rendered region | PASS if Turn 1 calls no tool and ends on the gate's one question, and Turn 2 makes the backup page before the first move, deletes nothing unasked, keeps the hand edit and reads back counts that match the gate. FAIL if any Figma write runs before the yes, the backup page is missing or made after a move, a node the edit did not create is deleted, the board is composed again, or the read-back skips a listed edit | 1. Check `references/flow-mode.md` Section 9, A direct edit 2. Check `references/style-guide.md` Section 7, Boards with stage columns 3. Check `ROUTER.md`, the direct edit branch of `route_flow` |

### Commands

1. `session: start fresh -> user: submit the prompt exactly`
2. `operator: read the reply and the tool calls`
3. `user: yes`
4. `operator: read the tool calls, the pages in the file and the reply`

### Expected

Step 2 finds the gate and no tool call. Step 4 finds the backup page made before the first move, no unasked delete, a `node.screenshot()` render and a read-back that matches the gate

### Evidence

The replies, the tool calls, the file's page list and the rendered region

### Pass / Fail

- **Pass**: Turn 1 calls no tool and ends on the gate's one question, and Turn 2 makes the backup page before the first move, deletes nothing unasked, keeps the hand edit and reads back counts that match the gate
- **Fail**: any Figma write runs before the yes, the backup page is missing or made after a move, a node the edit did not create is deleted, the board is composed again, or the read-back skips a listed edit

### Failure Triage

1. Check `references/flow-mode.md` Section 9, A direct edit
2. Check `references/style-guide.md` Section 7, Boards with stage columns
3. Check `ROUTER.md`, the direct edit branch of `route_flow`

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
| [`references/flow-mode.md`](../../references/flow-mode.md) | The direct edit route, its gate, backup page and read-back |
| [`references/style-guide.md`](../../references/style-guide.md) | The column grid of a board with stage columns |
| [`ROUTER.md`](../../ROUTER.md) | The direct edit branch and the resources it loads |

---

## 5. SOURCE METADATA

- Group: Board write
- Playbook ID: FJ-050
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `board-write/direct-edit-after-yes.md`
