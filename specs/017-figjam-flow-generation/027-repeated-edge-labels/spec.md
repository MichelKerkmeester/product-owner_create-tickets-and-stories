---
title: "Feature Specification: Phase 27: Repeated edge labels"
description: "The rubric says nothing about the same label on every connector. This phase applies the phase 016 change so that four or more identical labels on non-decision edges become none or one, with decision exits and sequence messages exempt."
trigger_phrases:
  - "repeated edge labels"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Phase 27: Repeated edge labels

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P1 |
| **Status** | Complete |
| **Created** | 2026-10-20 |
| **Branch** | `main` |
| **Parent Spec** | ../spec.md |
| **Phase** | 27 of 28 |
| **Predecessor** | 016-figjam-improvement-research |
| **Successor** | None |
| **Handoff Criteria** | The change is applied, mirrored and every gate passes |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 27** of the Product Owner FigJam flow generation upgrade specification.

**Scope Boundary**: sk-create-figjam/references/quality-rubric.md Section 2 and the process and architecture type references.

**Dependencies**:
- The ranked change in `../016-figjam-improvement-research/research/research.md` Section 4.

**Deliverables**:
- The edited sources, their Project mirrors where they have one, and passing gates.

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
The rubric says nothing about the same label on every connector.

### Purpose
Four or more identical labels on non-decision edges become none or one, with decision exits and sequence messages exempt.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Sk-create-figjam/references/quality-rubric.md Section 2 and the process and architecture type references

### Out of Scope
- Any other ranked change, which has its own phase
- Any Barter screenshot, Barter flow or board URL

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| sk-create-figjam/references/quality-rubric.md Section 2 and the process and architecture type references | Modify | Four or more identical labels on non-decision edges become none or one, with decision exits and sequence messages exempt |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | Four or more identical labels on non-decision edges become none or one, with decision exits and sequence messages exempt. |
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

- **SC-001**: The rubric and both type references carry the rule with its exemptions.
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
| Research | 4/20 | Done in phase 016 |
| **Total** | **18/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- None.
<!-- /ANCHOR:questions -->
