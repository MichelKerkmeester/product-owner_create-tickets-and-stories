---
title: "FJ-018 -- A user flow through the fj fallback"
description: "This scenario validates a user flow through the fj fallback for `FJ-018`. It checks that with no hosted route but `figma-ds-cli` reachable, a user flow is written node by node into the FigJam file open in Figma Desktop after a gate that names it."
version: 1.0.1.0
driver: operator-only
---

# FJ-018 -- A user flow through the fj fallback

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-018`.

---

## 1. OVERVIEW

This scenario validates a user flow through the fj fallback for `FJ-018`. It checks that with no hosted route but `figma-ds-cli` reachable, a user flow is written node by node into the FigJam file open in Figma Desktop after a gate that names it.

### Why This Matters

The `fj` route is the only write path without the hosted MCP. It has no layout verb, so positions are computed, and it must confirm the open file is a FigJam board first.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-018` and confirm the expected signals without contradictory evidence.

- Objective: Verify that with no hosted route but `figma-ds-cli` reachable, a user flow is written node by node into the FigJam file open in Figma Desktop after a gate that names it
- Real user request: `$flow make a FigJam flow of Fernhouse returns in the board I have open in Figma Desktop. From the returns doc: the customer opens an order, taps Return an item, picks the item and a reason, and if the order is older than 30 days they see a not-eligible screen. Otherwise they choose a refund or store credit, print the label and see a confirmation.`
- Prompt: `$flow make a FigJam flow of Fernhouse returns in the board I have open in Figma Desktop. From the returns doc: the customer opens an order, taps Return an item, picks the item and a reason, and if the order is older than 30 days they see a not-eligible screen. Otherwise they choose a refund or store credit, print the label and see a confirmation.`
- Expected execution process: Open with the playback, which waits for its own yes and comes after an intake round only when the run opens one. Then pick the user flow, model and check it, run the read-only `fj info`, name the open file in the gate, then on the gate's yes write with `fj shape`, `fj connect` and `fj text` and read back with `fj nodes -l`
- Expected signals: Turn 1 ends on the playback and writes nothing. Turn 2 writes nothing and ends on the gate, which names the open FigJam file from `fj info`. Turn 3 uses only create verbs, never `fj delete` or `fj eval`, and replies with a `Read-back:` line counting nodes, connectors and labelled exits
- Desired user-visible outcome: The flow on the open board with counts measured by `fj nodes -l`
- Pass/fail: PASS if the flow lands in the open FigJam file with matching counts and no destructive verb. FAIL if a write precedes `fj info` or the gate's yes, `fj delete` or `fj eval` is called, or the counts do not match. Record SKIP only when Figma Desktop or the figma-ds-cli daemon is unavailable in this environment, naming that blocker

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$flow make a FigJam flow of Fernhouse returns in the board I have open in Figma Desktop. From the returns doc: the customer opens an order, taps Return an item, picks the item and a reason, and if the order is older than 30 days they see a not-eligible screen. Otherwise they choose a refund or store credit, print the label and see a confirmation.`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-018 | A user flow through the fj fallback | Verify that with no hosted route but `figma-ds-cli` reachable, a user flow is written node by node into the FigJam file open in Figma Desktop after a gate that names it | `$flow make a FigJam flow of Fernhouse returns in the board I have open in Figma Desktop. From the returns doc: the customer opens an order, taps Return an item, picks the item and a reason, and if the order is older than 30 days they see a not-eligible screen. Otherwise they choose a refund or store credit, print the label and see a confirmation.` | 1. `sandbox: confirm Figma Desktop holds a FigJam file and the figma-ds-cli daemon runs, with no hosted MCP -> session: start fresh` -> 2. `user: submit the prompt exactly -> operator: confirm the reply is the playback with the question, the outcome, what each source settled and every assumed row. Confirm nothing is written. If the run opens an intake round first, answer it with the recommended answers and confirm the playback follows` -> 3. `user: Yes, that reading is right. -> operator: confirm fj info ran before the gate and that nothing is written yet` -> 4. `user: Yes, go ahead. -> operator: read the reply and the fj calls, and run fj nodes -l` | Step 2 finds the playback and no write. Step 3 finds `fj info` and a gate naming the file. Step 4 finds create verbs only and read-back counts that match `fj nodes -l` | All three replies, every `fj` command with its output and the operator's `fj nodes -l` output | PASS if the flow lands in the open FigJam file with matching counts and no destructive verb. FAIL if a write precedes `fj info` or the gate's yes, `fj delete` or `fj eval` is called, or the counts do not match. Record SKIP only when Figma Desktop or the figma-ds-cli daemon is unavailable in this environment, naming that blocker | 1. Check the `fj` route in `references/flow-mode.md` Section 6 2. Check the mutating gate in `mcp-figma/SKILL.md` |

### Commands

1. `sandbox: confirm Figma Desktop holds a FigJam file and the figma-ds-cli daemon runs, with no hosted MCP -> session: start fresh`
2. `user: submit the prompt exactly -> operator: confirm the reply is the playback with the question, the outcome, what each source settled and every assumed row. Confirm nothing is written. If the run opens an intake round first, answer it with the recommended answers and confirm the playback follows`
3. `user: Yes, that reading is right. -> operator: confirm fj info ran before the gate and that nothing is written yet`
4. `user: Yes, go ahead. -> operator: read the reply and the fj calls, and run fj nodes -l`

### Expected

Step 2 finds the playback and no write. Step 3 finds `fj info` and a gate naming the file. Step 4 finds create verbs only and read-back counts that match `fj nodes -l`

### Evidence

All three replies, every `fj` command with its output and the operator's `fj nodes -l` output

### Pass / Fail

- **Pass**: the flow lands in the open FigJam file with matching counts and no destructive verb
- **Fail**: a write precedes `fj info` or the gate's yes, `fj delete` or `fj eval` is called, or the counts do not match. Record SKIP only when Figma Desktop or the figma-ds-cli daemon is unavailable in this environment, naming that blocker

### Failure Triage

1. Check the `fj` route in `references/flow-mode.md` Section 6
2. Check the mutating gate in `mcp-figma/SKILL.md`

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
| [`references/flow-mode.md`](../../references/flow-mode.md) | The fj route |
| [`references/types/user-flow.md`](../../references/types/user-flow.md) | User flow rules |

---

## 5. SOURCE METADATA

- Group: Board write
- Playbook ID: FJ-018
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `board-write/fj-route-user-flow.md`
