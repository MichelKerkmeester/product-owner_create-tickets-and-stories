---
title: "Feature Specification: Phase 8: Routing, mode links and repository hygiene research"
description: "Routing lives in several copies across the parent hub, both packets, the router contract and the Claude Project kernel, and nobody has checked recently whether the READMEs are current, whether dead code or documents remain or whether the code follows sk-code-skilled. Run ten iterations of deep research with DeepSeek V4.1 Flash max and record ranked, cited recommendations."
trigger_phrases:
  - "routing research"
importance_tier: "normal"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "019-runtime-and-project-optimization/008-routing-research"
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
# Feature Specification: Phase 8: Routing, mode links and repository hygiene research

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
| **Phase** | 8 of 17 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Routing lives in several copies across the parent hub, both packets, the router contract and the Claude Project kernel, and nobody has checked recently whether the READMEs are current, whether dead code or documents remain or whether the code follows sk-code-skilled.

### Purpose
Run ten iterations of deep research with DeepSeek V4.1 Flash max and record ranked, cited recommendations.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Parent hub routing, mode-registry.json, hub-router.json, ROUTER.md and SKILL.md
- How the modes connect: Story with tasks, then-FLOW, Interactive fallback, refinement and ClickUp handoff
- Routing in the Claude Project kernel and Knowledge
- README currency, dead code and dead documents
- Code alignment with sk-code-skilled

### Out of Scope
- Source edits, which a later fix phase makes
- Vendored packets
- AI Systems/Product Context, screenshots and board URLs

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| research/ | Modify | Research state and the synthesis |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | Map every routing copy and recommend the smallest set |
| REQ-002 | Map the mode links and their gaps |
| REQ-003 | List stale README claims with evidence |
| REQ-004 | List dead code and documents with evidence |
| REQ-005 | List code that breaks sk-code-skilled rules |

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
| Dependency | Phase 007 | Order of work | Follow tasks.md |
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
