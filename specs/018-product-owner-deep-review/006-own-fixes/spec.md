---
title: "Feature Specification: Phase 6: Product Owner own fixes"
description: "The five reviews found 5 P1 and 39 P2 defects in files Product Owner owns, among them a skill rubric that asks for Project-only delivery proof, a private-doc recipe that omits a required parameter and a plugin build that ships a playbook its own rule excludes. Fix every review finding whose fix site is a Product Owner file, and bring the Project mirrors, kernel and playbooks in line."
trigger_phrases:
  - "own fixes"
importance_tier: "normal"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "018-product-owner-deep-review/006-own-fixes"
    last_updated_at: "2026-10-21T14:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Opened the fix phase"
    next_safe_action: "Apply the fixes"
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
# Feature Specification: Phase 6: Product Owner own fixes

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
| **Phase** | 6 of 7 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
The five reviews found 5 P1 and 39 P2 defects in files Product Owner owns, among them a skill rubric that asks for Project-only delivery proof, a private-doc recipe that omits a required parameter and a plugin build that ships a playbook its own rule excludes.

### Purpose
Fix every review finding whose fix site is a Product Owner file, and bring the Project mirrors, kernel and playbooks in line.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- The P1 and P2 findings of phases 001, 002 and 005, and the Product Owner fix sites named in phases 003 and 004
- The Claude Project mirrors and kernel lines that copy a changed source

### Out of Scope
- Files inside the vendored mcp-click-up/ and mcp-figma/ packets, which phase 007 pulls from upstream
- Commits and pushes

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| sk-product-owner/ | Modify | Rubric, router contract, routing, examples, modes and playbook |
| sk-create-figjam/ | Modify | Check scripts, flow-mode.md, SKILL.md and README.md |
| AGENTS.md, ROUTER.md, SYNC.md, README.md | Modify | Hub documents |
| scripts/vendor-sync.py, scripts/build-plugin.py | Modify | Vendor and plugin tooling |
| benchmark/ | Modify | Gate floors, the example lint and READMEs |
| claude project/ | Modify | Mirrors and kernel lines that copy a changed source |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | Fix every in-scope P1 finding at its named site |
| REQ-002 | Fix every in-scope P2 finding, or record why it does not hold |
| REQ-003 | Keep each Claude Project mirror in step with its changed source |
| REQ-004 | Rerun run_gates.sh, the format gate, the playbook validators and the plugin self-test from the final state |

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
| Dependency | None inside Product Owner | Order of work | Follow tasks.md |
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
