---
title: "FJ-013 -- A timeline offered as a gantt chart"
description: "This scenario validates a timeline offered as a gantt chart for `FJ-013`. It checks that a request for a timeline, which the generator cannot draw, is named as such and offered as a gantt chart with each event as a milestone."
version: 1.0.0.0
---

# FJ-013 -- A timeline offered as a gantt chart

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-013`.

---

## 1. OVERVIEW

This scenario validates a timeline offered as a gantt chart for `FJ-013`. It checks that a request for a timeline, which the generator cannot draw, is named as such and offered as a gantt chart with each event as a milestone.

### Why This Matters

A timeline is the most common undrawable request with a close drawable answer. Offering the gantt chart keeps the user moving instead of ending on a refusal.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-013` and confirm the expected signals without contradictory evidence.

- Objective: Verify that a request for a timeline, which the generator cannot draw, is named as such and offered as a gantt chart with each event as a milestone
- Real user request: `$figjam a timeline of the Loomlist offline mode milestones: design done 16 November, beta on 7 December, release on 21 December`
- Prompt: `$figjam a timeline of the Loomlist offline mode milestones: design done 16 November, beta on 7 December, release on 21 December`
- Expected execution process: Find timeline in the undrawable list, say so, offer a gantt chart with the three events as milestones and wait for a yes before modelling
- Expected signals: The reply names the timeline as a kind the generator cannot draw, offers a gantt chart with milestones and calls no Figma tool
- Desired user-visible outcome: A clear offer of the nearest drawable type
- Pass/fail: PASS if the reply names the timeline as undrawable and offers a gantt chart with milestones, with no Figma tool call. FAIL if a Figma tool is called with a timeline block, or the reply refuses with no offer

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$figjam a timeline of the Loomlist offline mode milestones: design done 16 November, beta on 7 December, release on 21 December`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-013 | A timeline offered as a gantt chart | Verify that a request for a timeline, which the generator cannot draw, is named as such and offered as a gantt chart with each event as a milestone | `$figjam a timeline of the Loomlist offline mode milestones: design done 16 November, beta on 7 December, release on 21 December` | 1. `session: start fresh -> user: submit the prompt exactly` -> 2. `operator: read the reply and the tool calls` | Step 1 returns the offer. Step 2 finds no Figma tool call | The reply and the tool calls | PASS if the reply names the timeline as undrawable and offers a gantt chart with milestones, with no Figma tool call. FAIL if a Figma tool is called with a timeline block, or the reply refuses with no offer | 1. Check the nearest-type table in `references/flow-mode.md` Section 3 2. Check `references/types/gantt.md` Section 1 |

### Commands

1. `session: start fresh -> user: submit the prompt exactly`
2. `operator: read the reply and the tool calls`

### Expected

Step 1 returns the offer. Step 2 finds no Figma tool call

### Evidence

The reply and the tool calls

### Pass / Fail

- **Pass**: the reply names the timeline as undrawable and offers a gantt chart with milestones, with no Figma tool call
- **Fail**: a Figma tool is called with a timeline block, or the reply refuses with no offer

### Failure Triage

1. Check the nearest-type table in `references/flow-mode.md` Section 3
2. Check `references/types/gantt.md` Section 1

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
| [`references/flow-mode.md`](../../references/flow-mode.md) | Nearest drawable types |
| [`references/types/gantt.md`](../../references/types/gantt.md) | Gantt use |

---

## 5. SOURCE METADATA

- Group: Type choice
- Playbook ID: FJ-013
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `type-choice/timeline-offers-gantt.md`
