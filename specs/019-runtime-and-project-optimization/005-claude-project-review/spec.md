---
title: "Feature Specification: Phase 5: Claude Project deep review"
description: "Nothing has reviewed the Claude Project packaging since the 019 kernel cuts, and no document tells a Claude Desktop user how to connect the ClickUp and Figma connectors to this Project, as Media Editor's user guide does for its extension. Review the kernel, the knowledge set and the upload list in three DeepSeek iterations for correctness, rule loss, end-user connector setup and the connector tool names the Project assumes."
trigger_phrases:
  - "claude project review"
importance_tier: "normal"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "019-runtime-and-project-optimization/005-claude-project-review"
    last_updated_at: "2026-10-21T18:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Ran the review and spot-checked every P1"
    next_safe_action: "The operator chooses which findings to fix"
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
# Feature Specification: Phase 5: Claude Project deep review

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
| **Phase** | 5 of 17 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Nothing has reviewed the Claude Project packaging since the 019 kernel cuts, and no document tells a Claude Desktop user how to connect the ClickUp and Figma connectors to this Project, as Media Editor's user guide does for its extension.

### Purpose
Review the kernel, the knowledge set and the upload list in three DeepSeek iterations for correctness, rule loss, end-user connector setup and the connector tool names the Project assumes.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- claude project/Custom Instructions.md, claude project/knowledge/ and claude project/README.md
- What README.md and SYNC.md tell a Project user
- The connector tool names the kernel assumes and the evidence for each

### Out of Scope
- Editing any reviewed file. This phase finds, a later change fixes
- AI Systems/Product Context, screenshots and board URLs, which no prompt or output may carry

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| review/ | Modify | Iterations, state log and the review report |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | Run 3 deep-review iterations on DeepSeek V4.1 Flash at max through cli-pi and llmgateway, with convergence stopping disabled |
| REQ-002 | Each finding carries a P0, P1 or P2 severity and cites the reviewed file as [SOURCE: path:line] |
| REQ-003 | The orchestrator opens the cited line of every P0 and P1 finding and records whether it holds |
| REQ-004 | The connector setup and tool-name questions get an answer or an open question each |

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
| Dependency | Phases 001 to 004 | Order of work | Follow tasks.md |
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
