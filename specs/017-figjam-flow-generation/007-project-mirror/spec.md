---
title: "Feature Specification: Phase 7: Claude Project mirror"
description: "Bring Flow Mode's Project-applicable rules into the Product Owner Claude Project kernel and knowledge files, with connector-conditional board writing, while every Sync Loop gate stays green."
trigger_phrases:
  - "project mirror"
  - "figjam phase 7"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Phase 7: Claude Project mirror

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P1 |
| **Status** | In Progress |
| **Created** | 2026-10-20 |
| **Branch** | `main` |
| **Parent Spec** | ../spec.md |
| **Phase** | 7 of 8 |
| **Predecessor** | After 005. Runs in parallel with 006. |
| **Successor** | See the parent Phase Documentation Map |
| **Handoff Criteria** | Every row in acceptance-criteria.md is Met |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 7** of the Product Owner FigJam flow generation upgrade specification. Its scope comes from section 15 of `../001-research/research/research.md`.

**Scope Boundary**: Mirroring mcp-figma into the Project.

**Dependencies**:
- After 005. Runs in parallel with 006.

**Deliverables**:
- A Flow Mode knowledge document with the Project-applicable rules
- The kernel command list and router section, with a kernel H1 minor bump
- Connector-conditional write or refusal wording, from the 002 decision note
- Pair and unmirrored_sources entries in systems.py

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
The claude.ai Project cannot run the fj CLI and can write boards only through a Figma connector. Without a mirror, the Project neither knows Flow Mode nor refuses it cleanly.

### Purpose
Hand-write the Flow Mode knowledge and kernel changes per SYNC.md, declare them to the Sync Loop, and keep the parity, receipts, residency and format gates passing.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- A Flow Mode knowledge document with the Project-applicable rules
- The kernel command list and router section, with a kernel H1 minor bump
- Connector-conditional write or refusal wording, from the 002 decision note
- Pair and unmirrored_sources entries in systems.py

### Out of Scope
- Mirroring mcp-figma into the Project
- Any generated mirror - Project files are hand-written

### Files to Change

Paths are relative to the Product Owner root unless named otherwise.

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| claude project/ | Modify | Kernel and knowledge files |
| SYNC.md | Modify | Change record |
| Sync Loop folder systems.py | Modify | Pair entries |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | run_parity.sh, run_receipts.sh, run_residency.sh and run_gates.sh exit 0 |
| REQ-002 | validate-output-format.cjs --system product-owner passes |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-003 | A deliberate rule-span drift fails the parity gate |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: run_parity.sh, run_receipts.sh, run_residency.sh and run_gates.sh each exit 0.
- **SC-002**: validate-output-format.cjs --system product-owner passes.
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | After 005. Runs in parallel with 006. | Phase cannot start | Check the predecessor's acceptance criteria first |
| Risk | Public-repo leak of board URLs or Barter screenshots | High | Keep them out of tracked files, per research section 14 |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Security
- **NFR-S01**: No secrets, tokens or Figma file keys in tracked files.

### Reliability
- **NFR-R01**: Every check in this phase is rerun from the final state before the phase closes.
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Error Scenarios
- External service failure: stop and record the failure in the goal log, never fake a pass.

### State Transitions
- Partial completion: the goal log records what is done and the next step.
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 12/25 | See Files to Change |
| Risk | 10/25 | Public repo, shared gates |
| Research | 6/20 | Done in 001-research |
| **Total** | **28/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- See section 17 of `../001-research/research/research.md` for the operator questions this phase depends on.
<!-- /ANCHOR:questions -->
