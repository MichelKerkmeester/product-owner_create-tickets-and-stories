---
title: "Feature Specification: Phase 10: Routing P0 fixes"
description: "Stage one is stated in prose, in hub-router.json sentences nothing reads and in a hand-coded Python copy, a request that opens with a tool drops the artifact it asks for, the router contract carries a dead DEFAULT_RESOURCE and an unloadable entry, seven mode hand-offs are undefined or contradictory and the two leaf maps are never compared. Make hub-router.json the executed stage-one authority, let an artifact request win over an opening tool word, and give every hand-off and leaf map one checked contract."
trigger_phrases:
  - "routing p0 fixes"
importance_tier: "normal"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "019-runtime-and-project-optimization/010-routing-p0-fixes"
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
    completion_pct: 0
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Phase 10: Routing P0 fixes

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
| **Phase** | 10 of 16 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Stage one is stated in prose, in hub-router.json sentences nothing reads and in a hand-coded Python copy, a request that opens with a tool drops the artifact it asks for, the router contract carries a dead DEFAULT_RESOURCE and an unloadable entry, seven mode hand-offs are undefined or contradictory and the two leaf maps are never compared.

### Purpose
Make hub-router.json the executed stage-one authority, let an artifact request win over an opening tool word, and give every hand-off and leaf map one checked contract.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Hub SKILL.md, hub-router.json, check_hub.py and the gold rows
- The router contract, its program and kernel Section 11 where a route changes
- Mode references, their Knowledge mirrors and playbook scenarios
- A leaf-map parity gate

### Out of Scope
- Vendored packets
- AI Systems/Product Context, screenshots and board URLs

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| SKILL.md, hub-router.json, ROUTER.md, leaf-manifest.json | Modify | Stage one and leaf maps |
| benchmark/ | Modify | Gates, gold rows and corpus |
| sk-product-owner/, sk-create-figjam/ | Modify | Contracts |
| claude project/ | Modify | Mirrors and Section 11 |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | hub-router.json is the stage-one authority the gate executes |
| REQ-002 | An artifact request wins over an opening tool signal |
| REQ-003 | DEFAULT_RESOURCE and the ALWAYS entry are fixed |
| REQ-004 | Each of the seven hand-offs has one contract and one scenario |
| REQ-005 | A gate compares the two leaf maps, FLOW included |

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
| Dependency | Phase 009 | Order of work | Follow tasks.md |
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
