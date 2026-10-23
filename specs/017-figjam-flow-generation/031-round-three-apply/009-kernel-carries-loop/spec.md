---
title: "Feature Specification: Phase 9: Carry the loop in the kernel and rebuild the two mirrors by hand"
description: "The Flow row names sources and output with no intake, and a Project cannot hold a state machine or write a file, so turn state survives only in the conversation. This phase applies interactive intake rank 9 so that carry the loop in the kernel and rebuild the two mirrors by hand."
trigger_phrases:
  - "kernel carries loop"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Phase 9: Carry the loop in the kernel and rebuild the two mirrors by hand

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P1 |
| **Status** | Complete |
| **Created** | 2026-10-21 |
| **Branch** | `main` |
| **Parent Spec** | ../spec.md |
| **Phase** | 9 of 32 |
| **Predecessor** | ../../030-figjam-research-three/003-interactive-intake |
| **Successor** | None |
| **Handoff Criteria** | The change is applied, mirrored and every gate passes |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 9** of the round three changes under the Product Owner FigJam flow generation upgrade.

**Scope Boundary**: `claude project/Custom Instructions.md` Flow row and Flow Mode Delivery, plus `claude project/knowledge/Product Owner - Templates - Flow Mode.md` and `Product Owner - System - Interactive Mode.md`.

**Dependencies**:
- Rank 9 in `../../030-figjam-research-three/003-interactive-intake/research/research.md` Section 3.

**Deliverables**:
- The edited sources, their Project mirrors where they have one, and passing gates.

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
The Flow row names sources and output with no intake, and a Project cannot hold a state machine or write a file, so turn state survives only in the conversation.

### Purpose
Carry the loop in the kernel and rebuild the two mirrors by hand.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- `claude project/Custom Instructions.md` Flow row and Flow Mode Delivery, plus `claude project/knowledge/Product Owner - Templates - Flow Mode.md` and `Product Owner - System - Interactive Mode.md`

### Out of Scope
- Any other ranked change, which has its own phase
- Any Barter screenshot, Barter flow or board URL

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `claude project/Custom Instructions.md` Flow row and Flow Mode Delivery, plus `claude project/knowledge/Product Owner - Templates - Flow Mode.md` and `Product Owner - System - Interactive Mode.md` | Modify | Carry the loop in the kernel and rebuild the two mirrors by hand |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | Carry the loop in the kernel and rebuild the two mirrors by hand. |
| REQ-002 | Every gate passes after the change: run_gates.sh, the format gates, the playbook validators and the Sync Loop gates where a mirror changed. |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-003 | The edit was proposed by DeepSeek V4.1 Flash at max through cli-pi and applied and checked by the orchestrator. |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: The change from the interactive intake rank 9 synthesis is in place: two sentences of policy, being that the Brief runs before the type choice and is replayed once before the gate, and that a Quick request gets one proposed Brief instead of rounds. No per-row table and no round counter in the kernel, because they would drift from the skill.
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Risk | Parallel edits collide in a shared file | Med | Edits apply in order and a failed match is redone by hand |
| Risk | A mirror drifts from its source | Med | Mirrors are regenerated or edited with the source and the parity gates run |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Security
- **NFR-S01**: No secrets, board URLs or Barter flows in any edit.

### Reliability
- **NFR-R01**: The pre-change tree is snapshotted, so the change reverts file by file.
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Error Scenarios
- A proposed edit whose old text no longer matches: redone by hand against the current file.

### State Transitions
- Partial completion: the snapshot restores any file.
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 8/25 | A few files |
| Risk | 6/25 | Reversible text edits |
| Research | 4/20 | Done in phase 030 |
| **Total** | **18/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- None.
<!-- /ANCHOR:questions -->
