---
title: "SDK-002 -- Doc conflict gate"
description: "Validates the Doc conflict gate that stops drafting behind one consolidated clarification until source authority is resolved."
version: 1.0.0.0
---

# SDK-002 -- Doc conflict gate

This scenario validates source-conflict handling when two supplied notes describe the same behavior and no authority winner is declared.

---

## 1. OVERVIEW

The command fixes Doc Mode. The two notes contradict each other on how a payout pause ends. The runtime must stop composition, export the consolidated question and wait. Drafting a blended document is the primary failure.

### Why this matters

A silently merged conflict turns one source's retired claim into current behavior. The conflict gate is the only thing that prevents it.

---

## 2. SCENARIO CONTRACT

- Objective: Verify conflict detection, the consolidated clarification export and a status-safe behavior reference after resolution
- Real user request: `Can you write a behavior reference for the payout pause feature from these two notes? Note A says the pause holds for 24 hours then releases automatically. Note B says the pause holds until the brand clears it manually.`
- Prompt: `$doc Write a behavior reference for the payout pause feature from these two notes. Note A says the pause holds for 24 hours then releases automatically. Note B says the pause holds until the brand clears it manually.`
- Runtime profile: skill, from `AGENTS.md` with `SKILL.md` and the `sk-product-owner/` resources loaded
- Precondition: `SID-001` identity handover passed in the skill runtime before this scenario starts
- Expected execution process: Start fresh, submit Turn 1, inspect the clarification export, resolve authority in Turn 2 and inspect the next doc export
- Expected signals: Turn 1 lists both conflicting claims, asks one consolidated question, exports `export/[###] - doc-payout-pause-clarification.md`, reads it back, replies with its path, the read-back line and the HVR self-scan line (root section 5, Clarification turns) and creates no draft. Turn 2 labels the losing claim as retired material, saves `export/[###] - doc-payout-pause.md`, reads it back and replies with the Doc quality summary
- Desired user-visible outcome: A clarification export listing the conflict, then one doc export after the user resolves authority
- Pass/fail: PASS if the first turn stops without a draft and the second turn keeps the resolved status visible. FAIL if the runtime picks a winner, blends the two claims or promotes the retired claim into current behavior
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$doc Write a behavior reference for the payout pause feature from these two notes. Note A says the pause holds for 24 hours then releases automatically. Note B says the pause holds until the brand clears it manually.` | Detect the unresolved conflict, stop composition, export one consolidated question that lists both claims, then wait. Create no draft | Both notes are named and neither is promoted ahead of the user's authority decision | Turn 1 reply, clarification export, read-back result and clean draft ledger |
| 2 | `Note A governs. The automatic release after 24 hours is current behavior. Note B is a retired draft.` | Build the behavior reference with Note A as current behavior and Note B labelled retired, apply the ClickUp layout, save the next doc export, read it back and reply with the path and the Doc summary | The authority decision and the retired label remain attached to their claims | Turn 2 reply, exported behavior reference and read-back result |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$doc Write a behavior reference for the payout pause feature from these two notes. Note A says the pause holds for 24 hours then releases automatically. Note B says the pause holds until the brand clears it manually.`

### Commands

1. `sandbox: record the export folder baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `filesystem: open the clarification export -> operator: confirm it lists both claims and holds no draft -> user: submit Turn 2 in the same session`
4. `filesystem: open the new doc export -> operator: check the status labels, the conflict decision and the ClickUp grammar`

### Expected

Step 1 fixes the baseline. Step 2 stops the draft and produces one clarification file. Step 3 proves the question-only file and captures the authority decision. Step 4 finds current behavior for the 24 hour release and a retired label on the manual-clear claim.

### Evidence

Capture both replies, the side-effect ledger, both export paths and read-back results, the conflict list, the authority decision and the status labels in the final document.

### Pass / fail

- **Pass**: The first turn stops with one question-only clarification, and the final document keeps Note A as current, Note B as retired and no blended claim
- **Fail**: The runtime drafts at any point before the decision, chooses a winner itself, merges the two claims or drops the retired label

### Failure triage

1. Check the authority order and conflict gate in `doc-mode.md`
2. Compare the question with the Doc Context and Clarification template in `interactive-response-templates.md`
3. Re-read the final document and restore any status label that the synthesis dropped

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| SDK-002 | Doc conflict gate | Verify the conflict stop and the status-safe behavior reference | `$doc Write a behavior reference for the payout pause feature from these two notes. Note A says the pause holds for 24 hours then releases automatically. Note B says the pause holds until the brand clears it manually.` | 1. Baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the behavior reference | Step 1: baseline known. Step 2: conflict stop and one clarification. Step 3: authority resolved. Step 4: current and retired labels intact | Both replies, ledger, clarification and doc export paths, conflict list and status labels | PASS if the stop, the decision and the labels all match. FAIL otherwise | 1. Check the conflict gate. 2. Check the clarification. 3. Check status labels in the export |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and root summary |
| [`doc-mode.md`](../../references/doc-mode.md) | Source authority order, conflict gate and classification rules |
| [`doc-templates.md`](../../assets/doc-templates.md) | Behavior reference shape |
| [`interactive-response-templates.md`](../../assets/interactive-response-templates.md) | Consolidated clarification wording |
| [`SID-001`](../skill-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Skill document modes
- Playbook ID: SDK-002
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-document-modes/doc-conflict-gate.md`
