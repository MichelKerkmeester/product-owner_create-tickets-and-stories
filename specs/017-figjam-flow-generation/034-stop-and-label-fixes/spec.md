---
title: "Feature Specification: Phase 34: Flow stop discipline and composer label fixes"
description: "The 2026-10-24 Sonnet run merged the playback and the gate into one stop and wrote on the reading yes in several scenarios, wrote on an answer to a question it never asked, and the composer let a second edge into one target and connectors cross zone titles. Make the playback and the gate two separate stops that no reply can merge, keep composed labels clear of zone titles and of each other, reconcile the notes contract between the skill and the playbook, mirror the change to the Project and rerun the scenarios that failed."
trigger_phrases:
  - "stop and label fixes"
importance_tier: "normal"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "017-figjam-flow-generation/034-stop-and-label-fixes"
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
# Feature Specification: Phase 34: Flow stop discipline and composer label fixes

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
| **Phase** | 34 of 34 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
The 2026-10-24 Sonnet run merged the playback and the gate into one stop and wrote on the reading yes in several scenarios, wrote on an answer to a question it never asked, and the composer let a second edge into one target and connectors cross zone titles.

### Purpose
Make the playback and the gate two separate stops that no reply can merge, keep composed labels clear of zone titles and of each other, reconcile the notes contract between the skill and the playbook, mirror the change to the Project and rerun the scenarios that failed.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- sk-create-figjam flow-mode.md and hybrid-workflow.md
- sk-create-figjam/assets/compose-board.js and scripts/compose_board.py
- The playbook scenarios whose contract changes
- The Claude Project mirrors, SYNC.md and the kernel when it carries the rule
- A rerun of the failed Sonnet scenarios

### Out of Scope
- Commits and pushes
- Composer changes the run did not show a need for

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| sk-create-figjam/ | Modify | Stop rule, composer and notes contract |
| claude project/ | Modify | Mirrors |
| benchmark/reports/ | Modify | Rerun evidence |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | A reply never carries both the playback and the gate, and only a yes to the gate writes |
| REQ-002 | No composed label touches a zone title or another edge label |
| REQ-003 | The skill and the playbook state the same notes contract |

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
| Dependency | Phase 033 | Order of work | Follow tasks.md |
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
