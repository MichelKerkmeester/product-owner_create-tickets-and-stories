---
title: "FJ-003 -- A kind Flow Mode does not draw"
description: "This scenario validates a kind Flow Mode does not draw for `FJ-003`. It checks that a request for a mindmap is refused plainly with the nearest useful form offered, and no board tool is called."
version: 1.0.1.0
---

# FJ-003 -- A kind Flow Mode does not draw

This document captures the user-testing contract, execution flow, source anchors and metadata for `FJ-003`.

---

## 1. OVERVIEW

This scenario validates a kind Flow Mode does not draw for `FJ-003`. It checks that a request for a mindmap is refused plainly with the nearest useful form offered, and no board tool is called.

### Why This Matters

Flow Mode draws seven types and a mindmap is not one of them. A write that tries anyway either fails or draws a flowchart that only looks like what was asked for.

---

## 2. SCENARIO CONTRACT

Operators run the exact prompt and command sequence for `FJ-003` and confirm the expected signals without contradictory evidence.

- Objective: Verify that a request for a mindmap is refused plainly with the nearest useful form offered, and no board tool is called
- Real user request: `$figjam a mindmap of the Roamstay launch themes: guest trust, partner onboarding, pricing and reviews`
- Prompt: `$figjam a mindmap of the Roamstay launch themes: guest trust, partner onboarding, pricing and reviews`
- Expected execution process: Route to Flow Mode, find mindmap in the list of kinds Flow Mode does not draw, say so and offer a table or a list in a Doc
- Expected signals: The reply says Flow Mode does not draw a mindmap, offers a table or a list in a Doc and calls no Figma tool
- Desired user-visible outcome: A plain refusal with a useful alternative
- Pass/fail: PASS if the reply names the mindmap as undrawable, offers a table or a list and calls no Figma tool. FAIL if a Figma tool is called, a flowchart is drawn in its place, or the reply offers no alternative

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$figjam a mindmap of the Roamstay launch themes: guest trust, partner onboarding, pricing and reviews`

### Recommended Orchestration Process

1. Restate the user request in plain user language
2. Run it locally in one fresh session, because each scenario reads one runtime's replies and tool calls
3. Execute the steps exactly as written
4. Compare the observed output with the desired user-visible outcome
5. Record the verdict with the evidence below

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| FJ-003 | A kind Flow Mode does not draw | Verify that a request for a mindmap is refused plainly with the nearest useful form offered, and no board tool is called | `$figjam a mindmap of the Roamstay launch themes: guest trust, partner onboarding, pricing and reviews` | 1. `session: start fresh -> user: submit the prompt exactly` -> 2. `operator: read the reply and the tool calls` | Step 1 returns the refusal with the offer. Step 2 finds no Figma tool call | The reply and the tool calls | PASS if the reply names the mindmap as undrawable, offers a table or a list and calls no Figma tool. FAIL if a Figma tool is called, a flowchart is drawn in its place, or the reply offers no alternative | 1. Check the undrawable kinds in `references/flow-mode.md` Section 3 2. Check the NEVER rules in `SKILL.md` Section 4 |

### Commands

1. `session: start fresh -> user: submit the prompt exactly`
2. `operator: read the reply and the tool calls`

### Expected

Step 1 returns the refusal with the offer. Step 2 finds no Figma tool call

### Evidence

The reply and the tool calls

### Pass / Fail

- **Pass**: the reply names the mindmap as undrawable, offers a table or a list and calls no Figma tool
- **Fail**: a Figma tool is called, a flowchart is drawn in its place, or the reply offers no alternative

### Failure Triage

1. Check the undrawable kinds in `references/flow-mode.md` Section 3
2. Check the NEVER rules in `SKILL.md` Section 4

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
| [`references/flow-mode.md`](../../references/flow-mode.md) | What Flow Mode does not draw |
| [`SKILL.md`](../../SKILL.md) | Rules |

---

## 5. SOURCE METADATA

- Group: Type choice
- Playbook ID: FJ-003
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `type-choice/unsupported-kind-offers-nearest.md`
