---
title: "Feature Specification: Phase 2: Kernel size"
description: "The Project kernel, Custom Instructions.md, is 75 KB and loads on every turn, and its Section 11 Router Code alone is 27 KB of Python a Project never executes. Cut the kernel's per-turn cost without losing a rule, starting with the Router Code and the 13 KB Delivery Protocol."
trigger_phrases:
  - "kernel size"
importance_tier: "normal"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "019-runtime-and-project-optimization/002-kernel-size"
    last_updated_at: "2026-10-21T18:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Cut the kernel and resynced the residency statements"
    next_safe_action: "Start phase 003, knowledge retrieval"
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
# Feature Specification: Phase 2: Kernel size

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
| **Phase** | 2 of 17 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
The Project kernel, Custom Instructions.md, is 75 KB and loads on every turn, and its Section 11 Router Code alone is 27 KB of Python a Project never executes.

### Purpose
Cut the kernel's per-turn cost without losing a rule, starting with the Router Code and the 13 KB Delivery Protocol.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Custom Instructions.md
- The differential gate and the Sync Loop statements that hold kernel text
- SYNC.md review notes

### Out of Scope
- Changing any rule's meaning
- The skill side, except where a gate couples it to the kernel

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| claude project/Custom Instructions.md | Modify | The cuts |
| benchmark/router/differential.py | Modify | Its kernel-side contract |
| z — Claude Project Sync Loop/systems.py | Modify | Resynced statements |
| SYNC.md | Modify | The kernel review note |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | Count every rule in the kernel before and after |
| REQ-002 | Move or replace the Router Code so a Project still routes the same requests |
| REQ-003 | Tighten the Delivery Protocol |
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
| Dependency | Phase 001 | Order of work | Follow tasks.md |
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
