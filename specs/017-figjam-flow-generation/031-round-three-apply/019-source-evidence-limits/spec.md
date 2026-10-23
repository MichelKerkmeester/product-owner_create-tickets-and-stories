---
title: "Feature Specification: Phase 19: Name what each source can and cannot evidence"
description: "The intake has four input types and no ticket row,, and nothing says which item kinds a source may contribute, so a reported error invites an invented trigger. This phase applies input to model logic rank 8 so that name what each source can and cannot evidence."
trigger_phrases:
  - "source evidence limits"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Phase 19: Name what each source can and cannot evidence

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
| **Phase** | 19 of 32 |
| **Predecessor** | ../../030-figjam-research-three/002-input-to-model-logic |
| **Successor** | None |
| **Handoff Criteria** | The change is applied, mirrored and every gate passes |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 19** of the round three changes under the Product Owner FigJam flow generation upgrade.

**Scope Boundary**: `sk-create-figjam/references/flow-mode.md` Section 4, a ticket row beside the four input types, and the 'Never invent' rule.

**Dependencies**:
- Rank 8 in `../../030-figjam-research-three/002-input-to-model-logic/research/research.md` Section 3.

**Deliverables**:
- The edited sources, their Project mirrors where they have one, and passing gates.

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
The intake has four input types and no ticket row,, and nothing says which item kinds a source may contribute, so a reported error invites an invented trigger.

### Purpose
Name what each source can and cannot evidence.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- `sk-create-figjam/references/flow-mode.md` Section 4, a ticket row beside the four input types, and the 'Never invent' rule

### Out of Scope
- Any other ranked change, which has its own phase
- Any Barter screenshot, Barter flow or board URL

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `sk-create-figjam/references/flow-mode.md` Section 4, a ticket row beside the four input types, and the 'Never invent' rule | Modify | Name what each source can and cannot evidence |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | Name what each source can and cannot evidence. |
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

- **SC-001**: The change from the input to model logic rank 8 synthesis is in place: one line per input type names the item kinds it can evidence. A ticket evidences an error or exit node and not the move into it, a criterion's When evidences an edge, a reaction evidences an edge. A trigger with no evidence becomes an unknown trigger.
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
