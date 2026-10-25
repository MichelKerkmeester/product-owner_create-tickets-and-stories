---
title: "Feature Specification: Phase 35: First glance, routing and reply fixes"
description: "The 2026-10-25 rerun held stop discipline in all 18 scenarios but passed only 2: on most boards the planned first glance does not read first because the accent is optional, shares a hue with a kind fill and loses to the start pill, architecture and ER edges run along zone borders and share stubs and corridors, replies carry text after the HVR line, and four model misses trace to skill wording. Tie the accent to the planned first glance and give it a hue no kind uses, route edges clear of zone borders with no shared stub or corridor, keep the HVR line last, close the skill wording behind the model misses, mirror the change to the Project and rerun the failed scenarios."
trigger_phrases:
  - "first glance and routing"
importance_tier: "normal"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "017-figjam-flow-generation/035-first-glance-and-routing"
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
# Feature Specification: Phase 35: First glance, routing and reply fixes

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P1 |
| **Status** | In Progress |
| **Created** | 2026-10-21 |
| **Branch** | `main` |
| **Parent Spec** | ../spec.md |
| **Phase** | 35 of 35 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
The 2026-10-25 rerun held stop discipline in all 18 scenarios but passed only 2: on most boards the planned first glance does not read first because the accent is optional, shares a hue with a kind fill and loses to the start pill, architecture and ER edges run along zone borders and share stubs and corridors, replies carry text after the HVR line, and four model misses trace to skill wording.

### Purpose
Tie the accent to the planned first glance and give it a hue no kind uses, route edges clear of zone borders with no shared stub or corridor, keep the HVR line last, close the skill wording behind the model misses, mirror the change to the Project and rerun the failed scenarios.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- sk-create-figjam/assets/compose-board.js, scripts/compose_board.py and their geometry and fixtures
- sk-create-figjam/scripts/flow_check.py and the type checks
- sk-create-figjam references: flow-mode.md, style-guide.md, quality-rubric.md and the type files
- The playbook scorecard and the scenarios whose contract changes
- The Claude Project mirrors, SYNC.md and the kernel when it carries the rule
- A rerun of the failed scenarios with the adaptive runner

### Out of Scope
- Commits and pushes
- Router changes
- A redesign of the composer beyond what the rerun findings need

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| sk-create-figjam/ | Modify | Accent, routing, check and reply rules |
| claude project/ | Modify | Mirrors |
| benchmark/reports/ | Modify | Rerun evidence |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | The board's one accent sits on the node the gate names as first glance, in a hue no kind fill uses, and nothing else outweighs it |
| REQ-002 | No edge runs along a zone border, no two edges share a stub and no two edges share a corridor the model draws apart |
| REQ-003 | A Flow delivery reply ends on the HVR self-scan line |
| REQ-004 | The skill wording closes the gateway, type mismatch, team colour and revision playback misses |

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
| Dependency | Phase 034 | Order of work | Follow tasks.md |
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
