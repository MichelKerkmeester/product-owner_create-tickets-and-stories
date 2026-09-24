---
title: "PID-001 -- Project identity handover"
description: "Validates the Project runtime identity and Deliverable Block contract through the Canvas Artifact and the no-file-write claim."
version: 1.0.0.0
---

# PID-001 -- Project identity handover

This scenario validates the Project runtime before any other Project-side scenario runs. It passes only when the reply proves the Canvas Artifact delivery contract that the skill runtime will not emit.

---

## 1. OVERVIEW

The runtime runs from `claude project/Custom Instructions.md` with the full Project Knowledge set attached. A routine Quick task request must render a task as a Canvas Artifact, report an export-equivalent label and claim no file was written. The skill runtime has a real filesystem contract, so a reply carrying a real path or a read-back claim fails this scenario.

### Why this matters

Every later Project scenario assumes the runtime renders a Deliverable Block and never claims a local save. An identity mistake here invalidates the whole Project set.

---

## 2. SCENARIO CONTRACT

- Objective: Verify Project identity through the Canvas Artifact, the export-equivalent label and the no-file-write claim
- Real user request: `Can you write up a quick task for the payout pause toggle? Brands pause a pending payout for 24 hours with a required reason, and QA needs checklist items for the toggle, the reason field and the creator banner.`
- Prompt: `$quick $task Create a task for the payout pause toggle. Brands pause a pending payout for 24 hours with a required reason, and QA needs checklist items for the toggle, the reason field and the creator banner.`
- Runtime profile: project, from `Custom Instructions.md` with the full `claude project/knowledge/` set attached
- Expected execution process: Start a fresh Project conversation, submit Turn 1, capture the rendered block and the labels beside it, then submit Turn 2 and compare both replies
- Expected signals: Turn 1 renders the task as a Canvas Artifact, reports `Export-equivalent path: export/[NNN] - task-payout-pause-toggle.md`, claims no file was written and carries the HVR self-scan line. Turn 2 states the same delivery boundary without naming a real saved file
- Desired user-visible outcome: A Canvas Artifact, an export-equivalent label and no file claim
- Pass/fail: PASS if the reply carries `Canvas Artifact`, reports `Export-equivalent path:` and claims no local file was written. FAIL if it prints `Path:`, `Saved:`, `Verified: read-back succeeded`, or claims any local save
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$quick $task Create a task for the payout pause toggle. Brands pause a pending payout for 24 hours with a required reason, and QA needs checklist items for the toggle, the reason field and the creator banner.` | Route to Task Mode with Quick energy, render the task as a Canvas Artifact, then report the export-equivalent label and the HVR self-scan line outside the block | The artifact renders in the side Canvas panel and no file path is claimed | Turn 1 reply, rendered block and the labels beside it |
| 2 | `Confirm whether you wrote any file to disk, and tell me how a reviewer would open this artifact.` | State that the Project cannot write or read local files, that the Canvas Artifact is the delivery evidence, and repeat the export-equivalent label | The no-file-write boundary holds and the label stays a naming convention | Turn 2 reply |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$quick $task Create a task for the payout pause toggle. Brands pause a pending payout for 24 hours with a required reason, and QA needs checklist items for the toggle, the reason field and the creator banner.`

### Commands

1. `canvas: record the Canvas panel baseline`
2. `session: start a fresh Project conversation -> user: submit Turn 1 exactly`
3. `canvas: inspect the rendered Deliverable Block -> operator: confirm it is a Canvas Artifact and not a pasted file body`
4. `user: submit Turn 2 in the same conversation -> operator: confirm no file was claimed`

### Expected

Step 1 fixes the panel baseline. Step 2 produces one rendered task block. Step 3 proves the block arrived as a Canvas Artifact. Step 4 proves the runtime keeps the no-file-write boundary.

### Evidence

Capture both replies, the rendered block, the export-equivalent label, the HVR self-scan line and the absence of any real path claim.

Identity split proof from the worktree root:

- `grep -c "read-back succeeded" "AI Systems/Product Owner/AGENTS.md"` -> `1`, exit `0`
- `grep -c "read-back succeeded" "AI Systems/Product Owner/claude project/Custom Instructions.md"` -> `0`, exit `1`
- `grep -c "Canvas Artifact" "AI Systems/Product Owner/AGENTS.md"` -> `0`, exit `1`
- `grep -c "Canvas Artifact" "AI Systems/Product Owner/claude project/Custom Instructions.md"` -> `4`, exit `0`

The Project identity string `Canvas Artifact` is absent from the skill identity file. The skill identity string `read-back succeeded` is absent from the Project kernel. A reply that could have come from either runtime, or that carries the other runtime's string, is a FAIL.

### Pass / fail

- **Pass**: The reply carries `Canvas Artifact`, reports `Export-equivalent path:` and claims no local file was written
- **Fail**: The reply prints `Path:`, `Saved:` or `Verified: read-back succeeded`, names a readable file, or omits the export-equivalent label

### Failure triage

1. Re-run Turn 1 in a fresh Project and inspect where the block rendered
2. Compare the delivery wording with the Deliverable Block and export-equivalent rules in `Custom Instructions.md` Section 9
3. If the runtime claims a local file, stop the Project set and report the identity failure

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| PID-001 | Project identity handover | Verify the Project runtime through the Canvas Artifact and the no-file-write claim | `$quick $task Create a task for the payout pause toggle. Brands pause a pending payout for 24 hours with a required reason, and QA needs checklist items for the toggle, the reason field and the creator banner.` | 1. Canvas baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the rendered block -> 4. Submit Turn 2 and confirm the boundary | Step 1: panel baseline known. Step 2: one rendered block. Step 3: Canvas Artifact confirmed. Step 4: no file claim | Both replies, rendered block, export-equivalent label and the no-file-write evidence | PASS if the Project string and the label both appear. FAIL on any real path or save claim | 1. Re-run in a fresh Project. 2. Compare with the Deliverable Block rules. 3. Stop the set on identity drift |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and root summary |
| [`Custom Instructions.md`](../../../claude%20project/Custom%20Instructions.md) | Project identity, Canvas Artifact and export-equivalent contract |
| [`Product Owner - System - Router Contract - v0.100.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20System%20-%20Router%20Contract%20-%20v0.100.md) | Project routing authority |
| [`Product Owner - Rules - Human Voice Core - v0.100.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Rules%20-%20Human%20Voice%20Core%20-%20v0.100.md) | HVR self-scan source |

---

## 5. SOURCE METADATA

- Group: Project identity
- Playbook ID: PID-001
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-identity/identity-handover.md`
