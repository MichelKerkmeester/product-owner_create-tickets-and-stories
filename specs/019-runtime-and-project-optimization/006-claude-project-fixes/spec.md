---
title: "Feature Specification: Phase 6: Claude Project review fixes and user guide"
description: "The 005 review found that a Claude Desktop user is never told how to connect ClickUp and Figma to this Project, that the private ClickUp doc recipe is one call where two are needed, that just do it misses the Quick route, and seven smaller defects. Write a user guide for Claude Desktop in Media Editor's shape and fix every finding at its source."
trigger_phrases:
  - "claude project fixes"
importance_tier: "normal"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "019-runtime-and-project-optimization/006-claude-project-fixes"
    last_updated_at: "2026-10-21T18:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Wrote USER-GUIDE.md and fixed the review findings"
    next_safe_action: "The operator reviews the kernel and approves the commit"
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
# Feature Specification: Phase 6: Claude Project review fixes and user guide

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
| **Phase** | 6 of 17 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
The 005 review found that a Claude Desktop user is never told how to connect ClickUp and Figma to this Project, that the private ClickUp doc recipe is one call where two are needed, that just do it misses the Quick route, and seven smaller defects.

### Purpose
Write a user guide for Claude Desktop in Media Editor's shape and fix every finding at its source.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- A root USER-GUIDE.md and links to it
- The kernel, the Knowledge mirrors and their skill sources
- The router contract, its executable copy and the differential corpus
- Residency statements and SYNC.md notes the edits require

### Out of Scope
- Vendored packets, whose findings are fixed upstream or recorded
- AI Systems/Product Context, screenshots and board URLs

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| USER-GUIDE.md | Modify | The Claude Desktop guide |
| claude project/ | Modify | Kernel and mirror fixes |
| sk-product-owner/, sk-create-figjam/ | Modify | Source fixes |
| benchmark/router/ | Modify | Router copy and corpus |
| README.md, SYNC.md | Modify | Links and notes |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | Write a Claude Desktop user guide that adds both connectors, opens the Project, enables them per chat, checks they work and troubleshoots |
| REQ-002 | Make the private doc two calls with name and parent |
| REQ-003 | Route just do it to Quick in every router copy |
| REQ-004 | Fix or record every P2 finding |

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
| Dependency | Phase 005 | Order of work | Follow tasks.md |
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
