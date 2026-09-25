---
title: "PDK-001 -- Doc guide delivery"
description: "Validates a no-token documentation request through the Project source gate to a ClickUp-formatted guide Deliverable Block."
version: 1.0.0.0
---

# PDK-001 -- Doc guide delivery

This scenario validates natural-language Doc routing, the consolidated source question and the new-document layout in a Claude Project.

---

## 1. OVERVIEW

The request carries no command token. The Project should route by documentation framing, reach the Doc context gate and ask one consolidated question covering at least the source set, authority, status, shape and scope, the minimum that `Product Owner - Templates - Doc Mode` line 174 and `Custom Instructions.md` line 130 set. The request states the audience, and purpose sits outside that minimum, so the question may ask either but need not. It must not draft until the user answers, and the final guide renders as a Canvas Artifact with an export-equivalent label and no file claim.

### Why this matters

Doc Mode is the source-safety lane. A guide drafted from an unseen source set or an unstated status turns unknown material into current fact.

---

## 2. SCENARIO CONTRACT

- Objective: Verify Doc routing, the consolidated context question and the ClickUp layout contract on a rendered guide
- Real user request: `Document how the notification retry pipeline works for the support team. I will paste the engineering notes.`
- Prompt: `Document how the notification retry pipeline works for the support team. I will paste the engineering notes.`
- Runtime profile: project, from `Custom Instructions.md` with the full `claude project/knowledge/` set attached
- Precondition: `PID-001` identity handover passed in the Project runtime before this scenario starts
- Expected execution process: Start a fresh Project conversation, submit Turn 1, capture the consolidated question and its clarification block, answer in Turn 2 and inspect the rendered guide
- Expected signals: Turn 1 asks one question covering the unresolved Doc fields, renders it as its own clarification block with `Export-equivalent path: export/[NNN] - doc-notification-retry-clarification.md` and the HVR self-scan line (root section 5, Clarification turns) and claims no file. Turn 2 renders the guide with `* * *` dividers, `*   ` bullets and sentence-case headings under `Export-equivalent path: export/[NNN] - doc-notification-retry.md`, then replies with the HVR self-scan line and the one-line-per-dimension Doc summary
- Desired user-visible outcome: One consolidated source question followed by a ClickUp-formatted doc block
- Pass/fail: PASS if turn 1 asks one consolidated question covering every unresolved Doc field, the promised notes together with authority, status, shape and scope rather than the notes alone, rendered as a clarification block, the runtime then waits, the guide uses the ClickUp grammar and every claim traces to the supplied notes, with no file claim. FAIL if turn 1 asks only for the notes or leaves any of those five fields out of the question, whether it drops the field or defers it until the notes arrive, drafts before the notes arrive, merges statuses or prints `Path:` and claims a save
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `Document how the notification retry pipeline works for the support team. I will paste the engineering notes.` | Route to Doc Mode, run the context gate, ask one consolidated question for the source set, authority, status, shape and scope, plus any other field the request left open, render it as a clarification block and wait. Create no draft | Doc Mode is selected and no source is assumed beyond the promised notes | Turn 1 reply, rendered clarification block and the no-file-write statement |
| 2 | `Guide for support agents. Purpose: diagnose and requeue a failed notification retry. Status: current behavior. The notes are authoritative. Notes: a retry runs on a 30 second backoff for five attempts. Attempt six moves the notification to the failed queue. Support can requeue from the failed queue with the Requeue action. A requeued notification restarts the backoff.` | Render the guide from the notes with the ClickUp layout, then reply with the export-equivalent label, the HVR self-scan line and the one-line-per-dimension Doc summary | Every supplied value survives in its own units and no behavior beyond the notes is claimed | Turn 2 reply, rendered guide block and its labels |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `Document how the notification retry pipeline works for the support team. I will paste the engineering notes.`

### Commands

1. `canvas: record the Canvas panel baseline`
2. `session: start a fresh Project conversation -> user: submit Turn 1 exactly`
3. `canvas: inspect the clarification block -> operator: confirm it holds only the question -> user: submit Turn 2 in the same conversation`
4. `canvas: inspect the rendered guide -> operator: check the ClickUp grammar, the supplied values and the export-equivalent label`

### Expected

Step 1 fixes the panel baseline. Step 2 returns one consolidated question as its own clarification block. Step 3 proves the wait state and that no draft exists. Step 4 finds a guide with `* * *` dividers directly under each content heading, `*   ` bullets, sentence-case headings and the 30 second backoff, five attempts and failed queue values intact, and a reply carrying one summary line each for Source safety, Shape fit, ClickUp layout, Readability and Voice (`Product Owner - Templates - Doc Mode` line 388, `Custom Instructions.md` line 217). Spacer headings are not graded here. The skill twin fails them because a file export never carries one, and `Product Owner - Templates - Doc Mode` line 73 allows them in ClickUp-bound content, which the kernel does not say a rendered block is. The rule's silence on a rendered block is logged as a follow-up finding.

### Evidence

Capture both replies, both rendered blocks, the two export-equivalent labels, the guide headings with divider adjacency, the bullet markers and the Doc quality summary.

### Pass / fail

- **Pass**: Turn 1 asks one consolidated question covering every unresolved Doc field, the promised notes together with authority, status, shape and scope rather than the notes alone, rendered as a clarification block, with no early draft, and one rendered guide that passes the ClickUp layout gate with source-backed claims and no file claim
- **Fail**: Turn 1 asks only for the notes or leaves one of the five fields out, whether dropped or deferred until the notes arrive, or the runtime drafts early, invents behavior, promotes the notes beyond their supplied scope, writes `---` dividers and hyphen bullets into the new document, or claims a local save

### Failure triage

1. Check the Doc context gate and ClickUp contract in `Product Owner - Templates - Doc Mode`
2. Compare the question with the Doc Context and Clarification Question in `Product Owner - Assets - Interactive Response Templates`
3. Re-read the rendered guide against the supplied notes and restore any source value that was generalized

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| PDK-001 | Doc guide delivery | Verify no-token Doc routing, the source gate and ClickUp guide delivery in a Project | `Document how the notification retry pipeline works for the support team. I will paste the engineering notes.` | 1. Canvas baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the guide block | Step 1: baseline known. Step 2: one consolidated question. Step 3: source set and status settled. Step 4: ClickUp guide with supplied values and label | Both replies, rendered blocks, labels, layout checks and artifact excerpts | PASS if turn 1 asks one consolidated question for every unresolved Doc field, not the notes alone, and the layout and the source fidelity all match. FAIL otherwise | 1. Check Doc Mode knowledge. 2. Check the context question. 3. Check layout and source values |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and root summary |
| [`Custom Instructions.md`](../../../claude%20project/Custom%20Instructions.md) | Project routing, Canvas Artifact and export-equivalent contract |
| [`Product Owner - Templates - Doc Mode - v0.110.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Doc%20Mode%20-%20v0.110.md) | Project Doc context gate and ClickUp contract |
| [`Product Owner - Assets - Doc Templates - v0.107.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Doc%20Templates%20-%20v0.107.md) | Project guide shape and layout rules |
| [`PID-001`](../project-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Project document modes
- Playbook ID: PDK-001
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-document-modes/doc-guide-delivery.md`
