---
title: "Feature Specification: Phase 1: sk-product-owner deep review"
description: "Review the sk-product-owner packet for correctness, contract drift, routing gaps, template and example defects and stale references. This phase reviews it in five DeepSeek iterations and records findings."
trigger_phrases:
  - "sk product owner deep review"
importance_tier: "normal"
contextType: "review"
_memory:
  continuity:
    packet_pointer: "018-product-owner-deep-review/001-sk-product-owner"
    last_updated_at: "2026-10-21T12:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Opened the review phase"
    next_safe_action: "Run the review lineage"
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
# Feature Specification: Phase 1: sk-product-owner deep review

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
| **Phase** | 1 of 5 |
| **Predecessor** | None |
| **Successor** | None. The findings feed a later fix the operator chooses |
| **Handoff Criteria** | review/review-report.md exists and the operator has chosen which findings to fix |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 1** of the Product Owner deep review.

**Scope Boundary**: Review only. No Product Owner source file changes.

**Dependencies**:
- Product Owner as packet 017 left it, uncommitted work included.

**Deliverables**:
- 5 DeepSeek iteration files and a deep-review state log under `review/lineages/deepseek/`.
- `review/review-report.md`, the lineage's report, with each P0 and P1 finding spot-checked by the orchestrator.

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Nothing has reviewed `sk-product-owner/`, the default workflow packet that writes tasks, bugs, Stories, Epics and docs on its own since packet 017 reshaped it.

### Purpose
Review the sk-product-owner packet for correctness, contract drift, routing gaps, template and example defects and stale references.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- `sk-product-owner/`, the default workflow packet that writes tasks, bugs, Stories, Epics and docs
- Findings name the Product Owner file to change

### Out of Scope
- Editing any reviewed file. This phase finds, a later change fixes
- `AI Systems/Product Context`, screenshots and board URLs, which no prompt or output may carry

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| review/ | Create | Iterations, state log and the review report |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | Run 5 deep-review iterations on DeepSeek V4.1 Flash at max through cli-pi and llmgateway, with convergence stopping disabled. |
| REQ-002 | Each finding carries a P0, P1 or P2 severity and cites the reviewed file as [SOURCE: path:line]. |
| REQ-003 | The orchestrator opens the cited line of every P0 and P1 finding and records whether it holds. |
| REQ-004 | Findings name the Product Owner file to change. |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-005 | The orchestrator posts a one-line status about every 3 minutes while agents run. |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: 5 iteration records exist and none ends the run early.
- **SC-002**: The operator can choose which findings to fix from `review/review-report.md` and the checked list in `implementation-summary.md`.
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | DeepSeek through llmgateway | Run stalls | Rerun the iteration |
| Risk | A finding misreads the cited line | High | The orchestrator opens every P0 and P1 citation |
| Risk | A worker writes outside its lineage | Med | Read-only steer file and a scoped diff check after the run |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Security
- **NFR-S01**: No secrets, board URLs or Barter flows in any prompt or output.

### Reliability
- **NFR-R01**: The run is staged outside Product Owner and copied in, so a failed run leaves the packet as it was.
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Error Scenarios
- A gateway failure: the iteration is rerun and logged.

### State Transitions
- Partial run: the state log shows where it stopped, and the run resumes.
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 8/25 | One packet or the repository |
| Risk | 4/25 | No source change |
| Research | 12/20 | Five iterations |
| **Total** | **24/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- None.
<!-- /ANCHOR:questions -->
