---
title: "SDK-001 -- Doc guide delivery"
description: "Validates a no-token documentation request through the source gate to a ClickUp-formatted guide export."
version: 1.0.0.0
---

# SDK-001 -- Doc guide delivery

This scenario validates natural-language Doc routing, the consolidated source question and the new-document export.

---

## 1. OVERVIEW

The request carries no command token. The runtime should route by documentation framing, reach the Doc context gate and ask one consolidated question covering at least the source set, authority, status, shape and scope, the minimum that `doc-mode.md` line 198 sets. The request states the audience, and purpose sits outside that minimum, so the question may ask either but need not. It must not draft until the user answers.

### Why this matters

Doc Mode is the source-safety lane. A doc drafted from an unseen source set or an unstated status turns unknown material into current fact.

---

## 2. SCENARIO CONTRACT

- Objective: Verify Doc routing, the consolidated context question and the ClickUp layout contract on a new guide
- Real user request: `Document how the notification retry pipeline works for the support team. I will paste the engineering notes.`
- Prompt: `Document how the notification retry pipeline works for the support team. I will paste the engineering notes.`
- Runtime profile: skill, from `AGENTS.md` with `SKILL.md` and the `sk-product-owner/` resources loaded
- Precondition: `SID-001` identity handover passed in the skill runtime before this scenario starts
- Expected execution process: Start fresh, submit Turn 1, capture the consolidated question and its clarification export, answer in Turn 2 and inspect the next doc export
- Expected signals: Turn 1 asks one question covering the unresolved Doc fields, exports `export/[###] - doc-notification-retry-clarification.md`, reads it back, replies with its path, the read-back line and the HVR self-scan line (root section 5, Clarification turns) and creates no draft. Turn 2 uses only the supplied notes, saves `export/[###] - doc-notification-retry.md`, reads it back and replies with the Doc quality summary
- Desired user-visible outcome: One consolidated source question followed by a ClickUp-formatted guide export
- Pass/fail: PASS if turn 1 asks one consolidated question covering every unresolved Doc field, the promised notes together with authority, status, shape and scope rather than the notes alone, exports it as a clarification and reads it back, the runtime then waits, the guide uses `* * *` dividers and `*   ` bullets, and every claim traces to the supplied notes. FAIL if turn 1 asks only for the notes or leaves any of those five fields out of the question, whether it drops the field or defers it until the notes arrive, drafts before the notes arrive, merges statuses or emits `---` dividers and hyphen bullets in the new document
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `Document how the notification retry pipeline works for the support team. I will paste the engineering notes.` | Route to Doc Mode, run the context gate, ask one consolidated question for the source set, authority, status, shape and scope, plus any other field the request left open, export it as a clarification and wait. Create no draft | Doc Mode is selected and no source is assumed beyond the promised notes | Turn 1 reply, clarification export, read-back result and clean draft ledger |
| 2 | `Guide for support agents. Purpose: diagnose and requeue a failed notification retry. Status: current behavior. The notes are authoritative. Notes: a retry runs on a 30 second backoff for five attempts. Attempt six moves the notification to the failed queue. Support can requeue from the failed queue with the Requeue action. A requeued notification restarts the backoff.` | Build the guide from the notes, apply the ClickUp layout, save the next doc export, read it back and reply with the path, the HVR self-scan line and the one-line-per-dimension Doc summary | Every supplied value survives in its own units and no behavior beyond the notes is claimed | Turn 2 reply, exported guide and read-back result |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `Document how the notification retry pipeline works for the support team. I will paste the engineering notes.`

### Commands

1. `sandbox: record the export folder baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `filesystem: open the clarification export -> operator: confirm it holds only the question -> user: submit Turn 2 in the same session`
4. `filesystem: open the new doc export -> operator: check the ClickUp grammar and the supplied values`

### Expected

Step 1 fixes the baseline. Step 2 returns one consolidated question and one clarification file. Step 3 proves the wait state and that no draft exists. Step 4 finds a guide with `* * *` dividers directly under each content heading, `*   ` bullets, sentence-case headings, no empty spacer heading, since a file export never carries one (`doc-mode.md` line 97), and the 30 second backoff, five attempts and failed queue values intact.

### Evidence

Capture both replies, the side-effect ledger, both export paths and read-back results, the guide headings with divider adjacency, the bullet markers and the Doc quality summary.

### Pass / fail

- **Pass**: Turn 1 asks one consolidated question covering every unresolved Doc field, the promised notes together with authority, status, shape and scope rather than the notes alone, exported as a clarification and read back, with no early draft, and one readable guide that passes the ClickUp layout gate with source-backed claims
- **Fail**: Turn 1 asks only for the notes or leaves one of the five fields out, whether dropped or deferred until the notes arrive, or the runtime drafts early, invents behavior, promotes the notes beyond their supplied scope, or writes `---` dividers, hyphen bullets or empty spacer headings into the new document

### Failure triage

1. Check the Doc context gate and ClickUp contract in `doc-mode.md`
2. Compare the question with the Doc Context and Clarification template in `interactive-response-templates.md`
3. Re-read the exported guide against the supplied notes and restore any source value that was generalized

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| SDK-001 | Doc guide delivery | Verify no-token Doc routing, the source gate and ClickUp guide delivery | `Document how the notification retry pipeline works for the support team. I will paste the engineering notes.` | 1. Baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the doc export | Step 1: baseline known. Step 2: one consolidated question. Step 3: source set and status settled. Step 4: ClickUp guide with supplied values | Both replies, ledger, clarification and doc export paths, layout checks and artifact excerpts | PASS if turn 1 asks one consolidated question for every unresolved Doc field, not the notes alone, and the layout and the source fidelity all match. FAIL otherwise | 1. Check Doc Mode. 2. Check the context question. 3. Check layout and source values |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and root summary |
| [`doc-mode.md`](../../references/doc-mode.md) | Doc context gate, source classification and ClickUp contract |
| [`doc-templates.md`](../../assets/doc-templates.md) | Guide shape and layout rules |
| [`interactive-response-templates.md`](../../assets/interactive-response-templates.md) | Consolidated Doc question wording |
| [`SID-001`](../skill-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Skill document modes
- Playbook ID: SDK-001
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-document-modes/doc-guide-delivery.md`
