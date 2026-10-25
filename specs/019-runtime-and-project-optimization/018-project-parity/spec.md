---
title: "Feature Specification: Phase 18: Claude Project parity"
description: "The Claude Project package was mirrored by hand across many phases, the parity gate still reports quality-scoring.md as changed after its mirror, and the composed-board route has not been checked end to end for a Project reader with no Python. Audit the kernel and every Knowledge file against the skill sources, fix every finding so a Project behaves as the skill does wherever a Project can, and bring the parity gate to zero findings."
trigger_phrases:
  - "project parity"
importance_tier: "normal"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "019-runtime-and-project-optimization/018-project-parity"
    last_updated_at: "2026-10-21T18:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Opened the phase"
    next_safe_action: "Start the phase"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "1004bf13-7863-4447-a63e-6ad2f5fcfd86"
      parent_session_id: null
    completion_pct: 100
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Phase 18: Claude Project parity

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
| **Phase** | 18 of 19 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
The Claude Project package was mirrored by hand across many phases, the parity gate still reports quality-scoring.md as changed after its mirror, and the composed-board route has not been checked end to end for a Project reader with no Python.

### Purpose
Audit the kernel and every Knowledge file against the skill sources, fix every finding so a Project behaves as the skill does wherever a Project can, and bring the parity gate to zero findings.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- claude project/Custom Instructions.md
- claude project/knowledge/
- claude project/README.md and SYNC.md

### Out of Scope
- Skill behavior changes the audit does not require
- Live deployment of the Project, which the operator does

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| claude project/ | Modify | Kernel and Knowledge fixes |
| SYNC.md | Modify | Dated review note |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | Every Knowledge file carries what a Project reader needs from its skill source and nothing a Project cannot run |
| REQ-002 | The kernel routes every mode to the Knowledge files that hold it |
| REQ-003 | The parity gate reports zero findings |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: Every finding in scope is fixed or recorded with the reason it was not.
- **SC-002**: The gates that own the changed files pass from the final state.
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | Phase 017 | Order of work | Follow tasks.md |
| Risk | A fix changes behaviour a gate or mirror relies on | Med | Rerun the owning gates after each batch |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Security
- **NFR-S01**: No secrets, board URLs or Barter flows in any changed file.

### Reliability
- **NFR-R01**: Each fix is a working-tree edit to a tracked file, reverted with `git checkout -- <path>`.
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Error Scenarios
- A finding does not hold when its fix site is opened: it is recorded as not fixed, with the reason.

### State Transitions
- Partial batch: tasks.md shows which findings are fixed.
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 14/25 | Many small fixes across one packet tree |
| Risk | 8/25 | Docs and scripts, reversible |
| Research | 4/20 | Findings already checked |
| **Total** | **26/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- None.
<!-- /ANCHOR:questions -->
