---
title: "Feature Specification: Phase 9: Routing research P1 and P2 fixes"
description: "The 008 research found gates that miss what they describe, a stale plugin build, no link check, an oversized kernel, stale README counts, unread config entries and small deviations from sk-code-skilled. Fix every P1 and P2 finding of the 008 research through cli-codex GPT 6 Luna max on the fast tier, and verify each fix here."
trigger_phrases:
  - "routing research fixes"
importance_tier: "normal"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "019-runtime-and-project-optimization/009-routing-research-fixes"
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
# Feature Specification: Phase 9: Routing research P1 and P2 fixes

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
| **Phase** | 9 of 17 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
The 008 research found gates that miss what they describe, a stale plugin build, no link check, an oversized kernel, stale README counts, unread config entries and small deviations from sk-code-skilled.

### Purpose
Fix every P1 and P2 finding of the 008 research through cli-codex GPT 6 Luna max on the fast tier, and verify each fix here.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- The gates and READMEs under benchmark/, the plugin build, the kernel trim, root and packet READMEs, config entries and the script standards fixes

### Out of Scope
- The P0 routing contract findings
- Vendored packets
- AI Systems/Product Context, screenshots and board URLs

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| benchmark/ | Modify | Gates and READMEs |
| claude-plugin/ | Modify | Rebuilt copy |
| claude project/ | Modify | Kernel trim |
| README.md, sk-product-owner/, sk-create-figjam/, scripts/ | Modify | Counts, config and standards |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | Fix every P1 finding |
| REQ-002 | Fix every P2 finding |
| REQ-003 | Keep every gate green |

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
| Dependency | Phase 008 | Order of work | Follow tasks.md |
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
