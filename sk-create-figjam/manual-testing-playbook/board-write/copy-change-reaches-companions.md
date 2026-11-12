---
title: "FJ-052 -- A copy change reaches every companion"
description: "This scenario validates a copy change reaches every companion for `FJ-052`. It checks that a wording change on a board is carried into its exported .md doc and its A4 pages in the same turn, that no old wording is left and that the A4 blocks below a grown line move down."
version: 1.0.0.0
---

# FJ-052 -- A copy change reaches every companion

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-052`.

---

## 1. OVERVIEW

This scenario validates a copy change reaches every companion for `FJ-052`. It checks that a wording change on a board is carried into its exported .md doc and its A4 pages in the same turn, that no old wording is left and that the A4 blocks below a grown line move down.

### Why This Matters

A board and its docs say the same thing in two forms. When only one of them changes, a reader who opens the doc sees a different rule from the one on the board, and nobody notices until it causes a wrong decision. One change that reaches every companion keeps them one source.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-052` and confirm the expected signals without contradictory evidence.

- Objective: Verify that a copy change on a board is carried into every companion in the same turn, with a search for the old wording, the user's own wording kept and the A4 page reflowed
- Real user request: `on the Fernhouse return board, change the card bullet "Michel assists" to "Michel supports and approves the refund", and keep the docs in line`
- Prompt: `on the Fernhouse return board, change the card bullet "Michel assists" to "Michel supports and approves the refund", and keep the docs in line`
- Setup: A FigJam file holding a Fernhouse return board with a card bullet `Michel assists`, the same doc laid out as A4 pages in that file, and an exported `.md` copy of that doc that says `Michel assists` in one paragraph. One A4 paragraph carries a line break the user forced by hand
- Expected execution process: Answer as a direct edit, as `references/flow-mode.md` Section 9 sets out, and carry the change into the companions as Section 8 sets out under Companion documents
- Expected signals: The gate lists every companion before the first edit: the board card, the `.md` file and each A4 page that holds the wording. After the yes, the board, the `.md` file and the A4 text all read `Michel supports and approves the refund` in the same turn. The reply names a search of each companion for `Michel assists` and either finds no hit or names the hit in a `Finding:` line. Where the A4 paragraph grew a line, every block below it moves down and keeps the page's own gaps, and the last block still clears the footer. The forced line break stays where the user put it
- Desired user-visible outcome: The board and both docs saying the same thing, with no stale wording left
- Pass/fail: PASS if the gate lists every companion, all three read the new wording after one turn, the search for the old wording is named and the A4 blocks keep their gaps. FAIL if a companion keeps `Michel assists` with no `Finding:` line, a block below the grown paragraph overlaps it or its gap shrinks, the forced line break is removed, or a companion is changed in a later turn only

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `on the Fernhouse return board, change the card bullet "Michel assists" to "Michel supports and approves the refund", and keep the docs in line`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-052 | A copy change reaches every companion | Verify that a copy change on a board is carried into every companion in the same turn, with a search for the old wording, the user's own wording kept and the A4 page reflowed | `on the Fernhouse return board, change the card bullet "Michel assists" to "Michel supports and approves the refund", and keep the docs in line` | 1. `session: start fresh -> user: submit the prompt exactly` -> 2. `operator: read the gate` -> 3. `user: yes` -> 4. `bash: grep -n "Michel assists" <the .md companion>` -> 5. `operator: read the board, the A4 pages and the reply` | Step 2 lists every companion. Step 4 finds no hit. Step 5 finds the new wording in all three, the A4 gaps kept and the forced break in place | The replies, the tool calls, the `.md` file, the A4 render and the board text | PASS if the gate lists every companion, all three read the new wording after one turn, the search for the old wording is named and the A4 blocks keep their gaps. FAIL if a companion keeps `Michel assists` with no `Finding:` line, a block below the grown paragraph overlaps it or its gap shrinks, the forced line break is removed, or a companion is changed in a later turn only | 1. Check `references/flow-mode.md` Section 8, Companion documents 2. Check `references/flow-mode.md` Section 9, A direct edit |

### Commands

1. `session: start fresh -> user: submit the prompt exactly`
2. `operator: read the gate`
3. `user: yes`
4. `bash: grep -n "Michel assists" <the .md companion>`
5. `operator: read the board, the A4 pages and the reply`

### Expected

Step 2 lists every companion. Step 4 finds no hit. Step 5 finds the new wording in all three, the A4 gaps kept and the forced break in place

### Evidence

The replies, the tool calls, the `.md` file, the A4 render and the board text

### Pass / Fail

- **Pass**: the gate lists every companion, all three read the new wording after one turn, the search for the old wording is named and the A4 blocks keep their gaps
- **Fail**: a companion keeps `Michel assists` with no `Finding:` line, a block below the grown paragraph overlaps it or its gap shrinks, the forced line break is removed, or a companion is changed in a later turn only

### Failure Triage

1. Check `references/flow-mode.md` Section 8, Companion documents
2. Check `references/flow-mode.md` Section 9, A direct edit

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
| [`references/flow-mode.md`](../../references/flow-mode.md) | Companion documents and the direct edit |

---

## 5. SOURCE METADATA

- Group: Board write
- Playbook ID: FJ-052
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `board-write/copy-change-reaches-companions.md`
