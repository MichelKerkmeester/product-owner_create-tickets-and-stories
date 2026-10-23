---
title: "Feature Specification: Phase 3: Knowledge retrieval"
description: "The Project's 62 knowledge files total 700 KB, with 28 examples and four Templates files of 36 to 48 KB, so retrieval can pull overlapping text for one request. Cut duplicated text across the knowledge files so retrieval returns each rule once, without losing a rule or an example's teaching."
trigger_phrases:
  - "knowledge retrieval"
importance_tier: "normal"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "019-runtime-and-project-optimization/003-knowledge-retrieval"
    last_updated_at: "2026-10-21T18:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Mapped duplication and kept every repeat"
    next_safe_action: "Start phase 004, behavior check"
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
# Feature Specification: Phase 3: Knowledge retrieval

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
| **Phase** | 3 of 16 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
The Project's 62 knowledge files total 700 KB, with 28 examples and four Templates files of 36 to 48 KB, so retrieval can pull overlapping text for one request.

### Purpose
Cut duplicated text across the knowledge files so retrieval returns each rule once, without losing a rule or an example's teaching.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- claude project/knowledge/
- The kernel's knowledge consultation section

### Out of Scope
- The skill sources, except a mirror edit that follows them
- Deleting an example a playbook scenario relies on

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| claude project/knowledge/ | Modify | Merged or trimmed files |
| claude project/Custom Instructions.md | Modify | Section 8 knowledge map |
| claude project/README.md | Modify | Upload list |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | Map duplicated passages across the knowledge files |
| REQ-002 | Remove each duplicate from all but its owning file |
| REQ-003 | Keep the upload list and the kernel map in step |
| REQ-004 | Keep every gate green |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: Every requirement in scope is met or recorded with the reason it was not.
- **SC-002**: The gates that own the changed files pass from the final state.
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | Phase 002 | Order of work | Follow tasks.md |
| Risk | A change alters behaviour a gate or mirror relies on | Med | Rerun the owning gates after each batch |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Security
- **NFR-S01**: No secrets, board URLs or Barter flows in any changed file.

### Reliability
- **NFR-R01**: Each change is a working-tree edit to a tracked file, reverted with `git checkout -- <path>`.
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Error Scenarios
- A requirement turns out not to fit when its site is opened: it is recorded as not met, with the reason.

### State Transitions
- Partial batch: tasks.md shows which tasks are done.
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 14/25 | Several files across one packet tree |
| Risk | 8/25 | Docs and scripts, reversible |
| Research | 4/20 | Measured before the phase opened |
| **Total** | **26/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- None.
<!-- /ANCHOR:questions -->
