---
title: "FJ-009 -- A gantt chart with no route"
description: "This scenario validates a gantt chart with no route for `FJ-009`. It checks that a yes on a gantt chart with no hosted Figma MCP names the missing route, says the `fj` route cannot draw a gantt chart, offers the checked model and claims no board."
version: 1.0.2.0
---

# FJ-009 -- A gantt chart with no route

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-009`.

---

## 1. OVERVIEW

This scenario validates a gantt chart with no route for `FJ-009`. It checks that a yes on a gantt chart with no hosted Figma MCP names the missing route, says the `fj` route cannot draw a gantt chart, offers the checked model and claims no board.

### Why This Matters

The `fj` fallback draws only user flows and simple processes. Falling back to it for a gantt chart would draw the wrong thing or nothing.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-009` and confirm the expected signals without contradictory evidence.

- Objective: Verify that a yes on a gantt chart with no hosted Figma MCP names the missing route, says the `fj` route cannot draw a gantt chart, offers the checked model and claims no board
- Real user request: `put the Loomlist offline mode launch plan on a FigJam gantt chart in a new board in our Loomlist Product plan. Design starts 2 November for two weeks, the sync engine takes three weeks from the same day, the conflict screen build follows design for two weeks, integration starts when both are done for one week, then a two-week beta and the release.`
- Prompt: `put the Loomlist offline mode launch plan on a FigJam gantt chart in a new board in our Loomlist Product plan. Design starts 2 November for two weeks, the sync engine takes three weeks from the same day, the conflict screen build follows design for two weeks, integration starts when both are done for one week, then a two-week beta and the release.`
- Expected execution process: Open with the playback, which waits for its own yes and comes after an intake round only when the run opens one. Then pick the gantt type, model and check it, stop at the gate, then on the gate's yes find no hosted route, say the `fj` route does not draw a gantt chart, offer the checked model and write nothing
- Expected signals: Turn 1 ends on the playback and writes nothing. Turn 2 ends on the gate, which names the missing route in place of the plan and the calls, and writes nothing. Turn 3 names the hosted Figma MCP as not connected and what it needs, says the `fj` route cannot draw a gantt chart, offers the checked model and prints no board URL or `Read-back:` line
- Desired user-visible outcome: A plain account of the missing route with the checked model to keep
- Pass/fail: PASS if nothing is written, the missing route and the `fj` limit are named, and the checked model is offered. FAIL if a reply claims a board, the `fj` route is tried for the gantt chart, or an image, HTML page or Mermaid file stands in for the board. Record SKIP only when a Figma route is reachable, naming that as the sandbox blocker

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `put the Loomlist offline mode launch plan on a FigJam gantt chart in a new board in our Loomlist Product plan. Design starts 2 November for two weeks, the sync engine takes three weeks from the same day, the conflict screen build follows design for two weeks, integration starts when both are done for one week, then a two-week beta and the release.`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-009 | A gantt chart with no route | Verify that a yes on a gantt chart with no hosted Figma MCP names the missing route, says the `fj` route cannot draw a gantt chart, offers the checked model and claims no board | `put the Loomlist offline mode launch plan on a FigJam gantt chart in a new board in our Loomlist Product plan. Design starts 2 November for two weeks, the sync engine takes three weeks from the same day, the conflict screen build follows design for two weeks, integration starts when both are done for one week, then a two-week beta and the release.` | 1. `sandbox: confirm no Figma route is reachable and record the tool list -> session: start fresh` -> 2. `user: submit the prompt exactly -> operator: confirm the reply is the playback with the question, the outcome, what each source settled and every assumed row. Confirm nothing is written. If the run opens an intake round first, answer it with the recommended answers and confirm the playback follows` -> 3. `user: Yes, that reading is right. -> operator: confirm the passing check and no write` -> 4. `user: Yes, go ahead. -> operator: read the reply and tool calls` | Step 2 finds the playback and no write. Step 3 finds a passing check and no write. Step 4 finds the missing-route reply, the `fj` limit named and no board claimed | All three replies, the tool calls and the offered model | PASS if nothing is written, the missing route and the `fj` limit are named, and the checked model is offered. FAIL if a reply claims a board, the `fj` route is tried for the gantt chart, or an image, HTML page or Mermaid file stands in for the board. Record SKIP only when a Figma route is reachable, naming that as the sandbox blocker | 1. Check the `fj` route limits and the no-route reply in `references/flow-mode.md` Section 6 2. Check `references/types/gantt.md` Section 6 |

### Commands

1. `sandbox: confirm no Figma route is reachable and record the tool list -> session: start fresh`
2. `user: submit the prompt exactly -> operator: confirm the reply is the playback with the question, the outcome, what each source settled and every assumed row. Confirm nothing is written. If the run opens an intake round first, answer it with the recommended answers and confirm the playback follows`
3. `user: Yes, that reading is right. -> operator: confirm the passing check and no write`
4. `user: Yes, go ahead. -> operator: read the reply and tool calls`

### Expected

Step 2 finds the playback and no write. Step 3 finds a passing check and no write. Step 4 finds the missing-route reply, the `fj` limit named and no board claimed

### Evidence

All three replies, the tool calls and the offered model

### Pass / Fail

- **Pass**: nothing is written, the missing route and the `fj` limit are named, and the checked model is offered
- **Fail**: a reply claims a board, the `fj` route is tried for the gantt chart, or an image, HTML page or Mermaid file stands in for the board. Record SKIP only when a Figma route is reachable, naming that as the sandbox blocker

### Failure Triage

1. Check the `fj` route limits and the no-route reply in `references/flow-mode.md` Section 6
2. Check `references/types/gantt.md` Section 6

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
| [`references/flow-mode.md`](../../references/flow-mode.md) | Write routes and the no-route reply |
| [`references/types/gantt.md`](../../references/types/gantt.md) | Writing the board |

---

## 5. SOURCE METADATA

- Group: Board write
- Playbook ID: FJ-009
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `board-write/gantt-with-no-route.md`
