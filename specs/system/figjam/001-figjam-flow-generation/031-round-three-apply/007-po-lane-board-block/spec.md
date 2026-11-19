---
title: "Feature Specification: Phase 7: Give the Product Owner lane a board block and one named exception"
description: "A FigJam request that reaches the Product Owner lane inherits questions about deliverable type, scope and sources, and the packet's own escalation still says one question. This is the half of the brief that Flow Mode's own file cannot reach. This phase applies interactive intake rank 7 so that give the Product Owner lane a board block and one named exception."
trigger_phrases:
  - "po lane board block"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Phase 7: Give the Product Owner lane a board block and one named exception

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
| **Phase** | 7 of 32 |
| **Predecessor** | ../../030-figjam-research-three/003-interactive-intake |
| **Successor** | None |
| **Handoff Criteria** | The change is applied, mirrored and every gate passes |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 7** of the round three changes under the Product Owner FigJam flow generation upgrade.

**Scope Boundary**: `sk-product-owner/assets/interactive-response-templates.md`, a board block in the comprehensive question, and `sk-product-owner/references/interactive-mode.md` core rule 1 with the MUST NOT list.

**Dependencies**:
- Rank 7 in `../../030-figjam-research-three/003-interactive-intake/research/research.md` Section 3.

**Deliverables**:
- The edited sources, their Project mirrors where they have one, and passing gates.

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
A FigJam request that reaches the Product Owner lane inherits questions about deliverable type, scope and sources, and the packet's own escalation still says one question. This is the half of the brief that Flow Mode's own file cannot reach.

### Purpose
Give the Product Owner lane a board block and one named exception.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- `sk-product-owner/assets/interactive-response-templates.md`, a board block in the comprehensive question, and `sk-product-owner/references/interactive-mode.md` core rule 1 with the MUST NOT list

### Out of Scope
- Any other ranked change, which has its own phase
- Any Barter screenshot, Barter flow or board URL

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `sk-product-owner/assets/interactive-response-templates.md`, a board block in the comprehensive question, and `sk-product-owner/references/interactive-mode.md` core rule 1 with the MUST NOT list | Modify | Give the Product Owner lane a board block and one named exception |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | Give the Product Owner lane a board block and one named exception. |
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

- **SC-001**: The change from the interactive intake rank 7 synthesis is in place: when FLOW is detected, the comprehensive question gains one block naming the reader, the question the board answers and what the reader should decide. Core rule 1 names a board intake as a legal second round, bounded by Rank 2's stop rule, so the ban on a second round keeps its force everywhere else.
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
