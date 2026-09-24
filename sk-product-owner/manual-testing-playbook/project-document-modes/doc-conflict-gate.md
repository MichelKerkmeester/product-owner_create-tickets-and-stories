---
title: "PDK-002 -- Doc conflict gate"
description: "Validates the Project Doc conflict gate that stops drafting behind one consolidated clarification until source authority is resolved."
version: 1.0.0.0
---

# PDK-002 -- Doc conflict gate

This scenario validates source-conflict handling when two supplied notes describe the same behavior and no authority winner is declared.

---

## 1. OVERVIEW

The command fixes Doc Mode. The two notes contradict each other on how a payout pause ends. The Project must stop composition, render the consolidated question as a clarification block and wait. A blended document is the primary failure.

### Why this matters

A silently merged conflict turns one source's retired claim into current behavior. The conflict gate is the only thing that prevents it.

---

## 2. SCENARIO CONTRACT

- Objective: Verify conflict detection, the consolidated clarification block and a status-safe behavior reference after resolution
- Real user request: `Can you write a behavior reference for the payout pause feature from these two notes? Note A says the pause holds for 24 hours then releases automatically. Note B says the pause holds until the brand clears it manually.`
- Prompt: `$doc Write a behavior reference for the payout pause feature from these two notes. Note A says the pause holds for 24 hours then releases automatically. Note B says the pause holds until the brand clears it manually.`
- Runtime profile: project, from `Custom Instructions.md` with the full `claude project/knowledge/` set attached
- Precondition: `PID-001` identity handover passed in the Project runtime before this scenario starts
- Expected execution process: Start a fresh Project conversation, submit Turn 1, inspect the clarification block, resolve authority in Turn 2 and inspect the rendered behavior reference
- Expected signals: Turn 1 lists both conflicting claims, asks one consolidated question, renders it with `Export-equivalent path: export/[NNN] - doc-payout-pause-clarification.md` and creates no draft. Turn 2 labels the losing claim as retired material, renders the reference under `Export-equivalent path: export/[NNN] - doc-payout-pause.md` and claims no file
- Desired user-visible outcome: A clarification block listing the conflict, then one doc block after the user resolves authority
- Pass/fail: PASS if the first turn stops without a draft and the second turn keeps the resolved status visible with no file claim. FAIL if the runtime picks a winner, blends the two claims, promotes the retired claim or claims a local save
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$doc Write a behavior reference for the payout pause feature from these two notes. Note A says the pause holds for 24 hours then releases automatically. Note B says the pause holds until the brand clears it manually.` | Detect the unresolved conflict, stop composition, render one consolidated question that lists both claims with an export-equivalent label, then wait. Create no draft | Both notes are named and neither is promoted ahead of the user's authority decision | Turn 1 reply, rendered clarification block and the no-file-write statement |
| 2 | `Note A governs. The automatic release after 24 hours is current behavior. Note B is a retired draft.` | Render the behavior reference with Note A as current behavior and Note B labelled retired, keep the export-equivalent label and claim no file | The authority decision and the retired label remain attached to their claims | Turn 2 reply, rendered reference block and its labels |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$doc Write a behavior reference for the payout pause feature from these two notes. Note A says the pause holds for 24 hours then releases automatically. Note B says the pause holds until the brand clears it manually.`

### Commands

1. `canvas: record the Canvas panel baseline`
2. `session: start a fresh Project conversation -> user: submit Turn 1 exactly`
3. `canvas: inspect the clarification block -> operator: confirm it lists both claims and holds no draft -> user: submit Turn 2 in the same conversation`
4. `canvas: inspect the rendered reference -> operator: check the status labels, the conflict decision, the layout and the label`

### Expected

Step 1 fixes the panel baseline. Step 2 stops the draft and renders one clarification block. Step 3 proves the question-only block and captures the authority decision. Step 4 finds current behavior for the 24 hour release and a retired label on the manual-clear claim.

### Evidence

Capture both replies, both rendered blocks, the two export-equivalent labels, the conflict list, the authority decision and the status labels in the final document.

### Pass / fail

- **Pass**: The first turn stops with one question-only clarification block, and the final document keeps Note A as current, Note B as retired and no blended claim, with no file claim
- **Fail**: The runtime drafts at any point before the decision, chooses a winner itself, merges the two claims, drops the retired label or claims a local save

### Failure triage

1. Check the authority order and conflict gate in the Templates - Doc Mode knowledge document
2. Compare the block with the Doc Context and Clarification template in the Interactive Response Templates knowledge document
3. Re-read the final document and restore any status label that the synthesis dropped

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| PDK-002 | Doc conflict gate | Verify the Project conflict stop and the status-safe behavior reference | `$doc Write a behavior reference for the payout pause feature from these two notes. Note A says the pause holds for 24 hours then releases automatically. Note B says the pause holds until the brand clears it manually.` | 1. Canvas baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the reference block | Step 1: baseline known. Step 2: conflict stop and one clarification. Step 3: authority resolved. Step 4: current and retired labels intact | Both replies, rendered blocks, labels, conflict list and status labels | PASS if the stop, the decision and the labels all match. FAIL otherwise | 1. Check the conflict gate. 2. Check the clarification block. 3. Check status labels in the rendered reference |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and root summary |
| [`Custom Instructions.md`](../../../claude%20project/Custom%20Instructions.md) | Project routing, Canvas Artifact and export-equivalent contract |
| [`Product Owner - Templates - Doc Mode - v0.109.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Doc%20Mode%20-%20v0.109.md) | Project source authority order and conflict gate |
| [`Product Owner - Assets - Doc Templates - v0.107.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Doc%20Templates%20-%20v0.107.md) | Project behavior reference shape |
| [`PID-001`](../project-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Project document modes
- Playbook ID: PDK-002
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-document-modes/doc-conflict-gate.md`
