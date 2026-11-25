---
title: "PBR-004 -- Task lookalike stays Task"
description: "Validates that a task whose subject is a briefing stays in Task Mode and asks the Task question."
version: 1.0.0.0
---

# PBR-004 -- Task lookalike stays Task

This scenario sends a Roamstay request for a task about writing a design briefing and checks that the noun does not change the route.

---

## 1. OVERVIEW

A Search squad PM asks for a task whose work is writing a design briefing. The briefing noun is the subject of the ticket, so the artifact is a task, and the request names no building team. The runtime should keep Task Mode, ask the one Task question with the team gap and wait, never routing to Briefing Mode on the noun.

### Why this matters

The route follows the artifact the requester names. A runtime that reads the briefing noun and writes the design briefing itself hands over a document nobody asked for, and a task stays unwritten.

---

## 2. SCENARIO CONTRACT

- Objective: Verify that a task about writing a briefing routes to Task Mode, asks one Task question and renders it in the task lane
- Real user request: `Create a task to write a design briefing for the date picker stay limits, from Ines's notes in context/roamstay-date-picker-design-notes.md. Company background is in context/roamstay-context.md.`
- Prompt: `Create a task to write a design briefing for the date picker stay limits, from Ines's notes in context/roamstay-date-picker-design-notes.md. Company background is in context/roamstay-context.md.`
- Attachments: [roamstay-context.md](../../../benchmark/fixtures/companies/roamstay/roamstay-context.md), [roamstay-date-picker-design-notes.md](../../../benchmark/fixtures/companies/roamstay/roamstay-date-picker-design-notes.md)
- Runtime profile: project, from `Custom Instructions.md` with the full `claude project/knowledge/` set attached
- Precondition: `PID-001` identity handover passed in the project runtime before this scenario starts, and both attachments sit at `context/<basename>` before the Canvas panel baseline is recorded
- Expected execution process: Start a fresh Project conversation, submit Turn 1 and inspect the rendered clarification block
- Expected signals: The request frames a task, so it routes to Task Mode (`Custom Instructions.md` line 92). A request for a build task stays an ordinary task (`Product Owner - Templates - Briefing Mode.md` line 63). The question renders as its own block, labelled as a task-lane clarification (`Custom Instructions.md` line 259). The briefing is only the task's subject. The question asks which team builds the work, because the notes name no team and a task title leads with the team. It asks for nothing the notes already give. It holds the question and nothing else, with no draft task and no briefing
- Desired user-visible outcome: One Task question rendered under a task-lane label, with no briefing drafted and no briefing-lane label
- Size band (advisory): Not applicable, the delivery is one question
- Pass/fail: PASS if the request routes to Task Mode, asks one consolidated Task question that includes the team, renders it as its own block with a task-lane `Export-equivalent path:` and the `HVR self-scan:` line, and drafts neither a task nor a briefing. FAIL if it routes to Briefing Mode, drafts a briefing, labels a block in the `briefing` lane, writes a `Briefing - ` title or drafts the task in Turn 1. A claim of a local save also fails
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `Create a task to write a design briefing for the date picker stay limits, from Ines's notes in context/roamstay-date-picker-design-notes.md. Company background is in context/roamstay-context.md.` | Route to Task Mode on the task framing, read both attachments, ask one consolidated Task question that includes the team, render it as a task-lane clarification block and wait. Create no draft and no briefing | Task intent stays selected, the stay limits subject is retained and the team is still owed | Rendered clarification block, its label and the no-file-write statement |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `Create a task to write a design briefing for the date picker stay limits, from Ines's notes in context/roamstay-date-picker-design-notes.md. Company background is in context/roamstay-context.md.`

### Commands

1. `sandbox: stage both attachments at context/ -> canvas: record the Canvas panel baseline`
2. `session: start a fresh Project conversation -> user: submit Turn 1 exactly`
3. `canvas: inspect the clarification block -> operator: confirm it holds only the question, carries a task-lane label and has no briefing beside it`

### Expected

Step 1 fixes the baseline with `context/` holding the two attachments. Step 2 returns one Task question. Step 3 finds a question in the task lane, with no briefing, no draft task and no briefing-lane label.

### Evidence

Capture the reply, the rendered block and its export-equivalent label, and the lane word in its label.

### Pass / fail

- **Pass**: One Task question in the task lane with the team asked for, and no briefing, and no file claim
- **Fail**: The runtime routes to Briefing Mode, drafts a briefing or saves in the briefing lane, or claims a local save

### Failure triage

1. Check the framing rule that keeps a task about a briefing in Task Mode in `Custom Instructions.md`
2. Check the lane word rule for a clarification in `Custom Instructions.md` and `Product Owner - System - Interactive Mode`
3. Check the framing rule that keeps a task whose subject is a briefing in Task Mode

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| PBR-004 | Task lookalike stays Task | Verify a task about writing a briefing routes to Task Mode, asks one Task question and renders it in the task lane | `Create a task to write a design briefing for the date picker stay limits, from Ines's notes in context/roamstay-date-picker-design-notes.md. Company background is in context/roamstay-context.md.` | 1. Stage and baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification | Step 2: one Task question in the task lane. Step 3: no briefing and no draft | the reply, the rendered block and its export-equivalent label, and the lane word in its label | PASS if the request stays Task and the question sits in the task lane. FAIL otherwise | 1. Check the framing rule that keeps a task about a briefing. 2. Check the lane word rule for a clarification. 3. Check the framing rule that keeps a task whose subject is a briefing in Task Mode |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`Custom Instructions.md`](../../../claude%20project/Custom%20Instructions.md) | Line 92 briefing route, line 83 explicit commands ask first, line 69 title rule, line 259 clarification label, line 253 briefing label |
| [`Product Owner - Templates - Briefing Mode.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Briefing%20Mode.md) | Line 34 critical rules, line 82 title, lines 85 and 86 audiences and facets, line 89 source wording, line 95 spacing, line 63 build work stays Task |
| [`Product Owner - Assets - Design Briefing Template.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Design%20Briefing%20Template.md) | Lines 27 to 96 briefing scaffold and its notes for use |
| [`Product Owner - System - Interactive Mode.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20System%20-%20Interactive%20Mode.md) | Line 276 Briefing Mode entry and flow |
| [`Product Owner - Assets - Interactive Response Templates.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Interactive%20Response%20Templates.md) | Line 87 briefing context question |
| [roamstay-context.md](../../../benchmark/fixtures/companies/roamstay/roamstay-context.md) | Company context |
| [roamstay-date-picker-design-notes.md](../../../benchmark/fixtures/companies/roamstay/roamstay-date-picker-design-notes.md) | The source the request names |
| [`PID-001`](../project-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Project backlog modes
- Playbook ID: PBR-004
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-backlog-modes/task-lookalike-stays-task.md`
