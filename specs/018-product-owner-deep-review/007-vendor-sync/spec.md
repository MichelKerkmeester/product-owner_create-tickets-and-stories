---
title: "Feature Specification: Phase 7: Vendored packet sync"
description: "The mcp-click-up and mcp-figma findings are fixed upstream in the mcp-tooling packet 023, and the vendored copies in Product Owner still carry the old bytes. Pull the fixed mcp-click-up and mcp-figma packets back into Product Owner so vendor.json records the new upstream commit."
trigger_phrases:
  - "vendor sync"
importance_tier: "normal"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "018-product-owner-deep-review/007-vendor-sync"
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
# Feature Specification: Phase 7: Vendored packet sync

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
| **Phase** | 7 of 7 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
The mcp-click-up and mcp-figma findings are fixed upstream in the mcp-tooling packet 023, and the vendored copies in Product Owner still carry the old bytes.

### Purpose
Pull the fixed mcp-click-up and mcp-figma packets back into Product Owner so vendor.json records the new upstream commit.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- scripts/vendor-sync.py pull for mcp-click-up and mcp-figma
- vendor.json and the plugin rebuild that follows

### Out of Scope
- Editing a vendored file in place
- The upstream fixes themselves, which mcp-tooling packet 023 owns

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| mcp-click-up/ | Modify | Pulled from upstream |
| mcp-figma/ | Modify | Pulled from upstream |
| vendor.json | Modify | New base commits and hashes |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | Pull both packets only after the upstream fixes are committed |
| REQ-002 | vendor-sync.py status reports both packets in step at the new commit |
| REQ-003 | The plugin rebuild and its self-test pass after the pull |

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
| Dependency | The upstream fix commit in Code_Environment, which waits on the operator's go-ahead | Order of work | Follow tasks.md |
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
