---
title: "SBR-004 -- Task lookalike stays Task"
description: "Validates that a task whose subject is a briefing stays in Task Mode and asks the Task question."
version: 1.0.0.0
---

# SBR-004 -- Task lookalike stays Task

This scenario sends a Roamstay request for a task about writing a design briefing and checks that the noun does not change the route.

---

## 1. OVERVIEW

A Search squad PM asks for a task whose work is writing a design briefing. The briefing noun is the subject of the ticket, so the artifact is a task, and the request names no building team. The runtime should keep Task Mode, ask the one Task question with the team gap and wait, never routing to Briefing Mode on the noun.

### Why this matters

The route follows the artifact the requester names. A runtime that reads the briefing noun and writes the design briefing itself hands over a document nobody asked for, and a task stays unwritten.

---

## 2. SCENARIO CONTRACT

- Objective: Verify that a task about writing a briefing routes to Task Mode, asks one Task question and saves it in the task lane
- Real user request: `Create a task to write a design briefing for the date picker stay limits, from Ines's notes in context/roamstay-date-picker-design-notes.md. Company background is in context/roamstay-context.md.`
- Prompt: `Create a task to write a design briefing for the date picker stay limits, from Ines's notes in context/roamstay-date-picker-design-notes.md. Company background is in context/roamstay-context.md.`
- Attachments: [roamstay-context.md](../../../benchmark/fixtures/companies/roamstay/roamstay-context.md), [roamstay-date-picker-design-notes.md](../../../benchmark/fixtures/companies/roamstay/roamstay-date-picker-design-notes.md)
- Runtime profile: skill, from `AGENTS.md` with `SKILL.md` and the `sk-product-owner/` resources loaded
- Precondition: `SID-001` identity handover passed in the skill runtime before this scenario starts, and both attachments sit at `context/<basename>` before the export baseline is recorded
- Expected execution process: Start fresh, submit Turn 1 and inspect the clarification export
- Expected signals: The request frames a task, so it routes to Task Mode (`AGENTS.md` line 244, `references/routing.md` line 34). A request for a build task stays an ordinary task (`references/briefing-mode.md` line 83). The question is saved as `export/[###] - task-[description]-clarification.md` in the task lane (`AGENTS.md` line 84). The briefing is only the task's subject. The question asks which team builds the work, because the notes name no team and a task title leads with the team. It asks for nothing the notes already give. It holds the question and nothing else, with no draft task and no briefing
- Desired user-visible outcome: One Task question saved in the task lane, with no briefing drafted and no briefing-lane file
- Size band (advisory): Not applicable, the delivery is one question
- Pass/fail: PASS if the request routes to Task Mode, asks one consolidated Task question that includes the team, saves it as a task-lane `-clarification` export reported with its path, its `Verified:` line and the `HVR self-scan:` line, and drafts neither a task nor a briefing. FAIL if it routes to Briefing Mode, drafts a briefing, saves a file in the `briefing` lane, writes a `Briefing - ` title or drafts the task in Turn 1
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `Create a task to write a design briefing for the date picker stay limits, from Ines's notes in context/roamstay-date-picker-design-notes.md. Company background is in context/roamstay-context.md.` | Route to Task Mode on the task framing, read both attachments, ask one consolidated Task question that includes the team, export it as a task-lane clarification, read it back and wait. Create no draft and no briefing | Task intent stays selected, the stay limits subject is retained and the team is still owed | Clarification export, read-back line and a ledger holding only the clarification |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `Create a task to write a design briefing for the date picker stay limits, from Ines's notes in context/roamstay-date-picker-design-notes.md. Company background is in context/roamstay-context.md.`

### Commands

1. `sandbox: stage both attachments at context/ -> filesystem: record the export folder baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `filesystem: open the clarification export -> operator: confirm it holds only the question, sits in the task lane and has no briefing beside it`

### Expected

Step 1 fixes the baseline with `context/` holding the two attachments. Step 2 returns one Task question. Step 3 finds a question in the task lane, with no briefing, no draft task and no file in the briefing lane.

### Evidence

Capture the reply, the side-effect ledger, the clarification export path and its read-back line, and the lane word in its file name.

### Pass / fail

- **Pass**: One Task question in the task lane with the team asked for, and no briefing
- **Fail**: The runtime routes to Briefing Mode, drafts a briefing or saves in the briefing lane

### Failure triage

1. Check the framing rule that keeps a task about a briefing in Task Mode in `routing.md`
2. Check the lane word rule for a clarification in `AGENTS.md` and `interactive-mode.md`
3. Check the framing rule that keeps a task whose subject is a briefing in Task Mode

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| SBR-004 | Task lookalike stays Task | Verify a task about writing a briefing routes to Task Mode, asks one Task question and saves it in the task lane | `Create a task to write a design briefing for the date picker stay limits, from Ines's notes in context/roamstay-date-picker-design-notes.md. Company background is in context/roamstay-context.md.` | 1. Stage and baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification | Step 2: one Task question in the task lane. Step 3: no briefing and no draft | the reply, the side-effect ledger, the clarification export path and its read-back line, and the lane word in its file name | PASS if the request stays Task and the question sits in the task lane. FAIL otherwise | 1. Check the framing rule that keeps a task about a briefing. 2. Check the lane word rule for a clarification. 3. Check the framing rule that keeps a task whose subject is a briefing in Task Mode |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Line 84 clarification export, line 98 briefing file name, line 129 briefing title, line 340 explicit commands ask first |
| [`briefing-mode.md`](../../references/briefing-mode.md) | Line 54 critical rules, line 102 title, lines 103 to 106 sections, audiences and facets, line 109 source wording, line 115 spacing, line 83 build work stays Task |
| [`design-briefing-template.md`](../../assets/design-briefing-template.md) | Lines 46 to 115 briefing scaffold and its notes for use |
| [`interactive-mode.md`](../../references/interactive-mode.md) | Line 299 Briefing Mode entry and flow |
| [`interactive-response-templates.md`](../../assets/interactive-response-templates.md) | Line 111 briefing context question |
| [`routing.md`](../../references/routing.md) | Line 34 artifact framing without a command |
| [roamstay-context.md](../../../benchmark/fixtures/companies/roamstay/roamstay-context.md) | Company context |
| [roamstay-date-picker-design-notes.md](../../../benchmark/fixtures/companies/roamstay/roamstay-date-picker-design-notes.md) | The source the request names |
| [`SID-001`](../skill-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Skill backlog modes
- Playbook ID: SBR-004
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-backlog-modes/task-lookalike-stays-task.md`
