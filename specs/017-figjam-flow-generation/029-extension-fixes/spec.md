---
title: "Feature Specification: Phase 29: Extension fixes"
description: "The thirteen findings of phase 016 Section 9, applied as twelve child phases: eight follow-ups to shipped changes and five new changes to sk-create-figjam and its integration."
trigger_phrases:
  - "extension fixes phase parent spec"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "017-figjam-flow-generation/029-extension-fixes"
    last_updated_at: "2026-10-21T08:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Opened the extension fixes phase parent"
    next_safe_action: "Work the child phases"
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
<!-- SPECKIT_TEMPLATE_SOURCE: phase-parent-spec | v2.2 -->

<!-- SPECKIT_LEVEL: 2 -->

# Feature Specification: Phase 29: Extension fixes

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
| **Parent Spec** | `../spec.md` |
| **Parent Packet** | product-owner/017-figjam-flow-generation |
| **Predecessor** | 016-figjam-improvement-research |
| **Successor** | None |
| **Handoff Criteria** | Every child applies its finding and validates alone |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Five more research iterations found that eight of the twelve shipped FigJam changes stop short and ranked five new ones. The worst is in routing: a Doc or Bug asked for beside a FigJam board loses the artifact, and seven common phrasings lose the board.

### Purpose
Apply all thirteen findings of `../016-figjam-improvement-research/research/research.md` Section 9, one child phase per finding, with the two router findings in one child.

> **Phase-parent note:** This spec.md is the only authored document at this level besides goal.md. Plans, tasks, checklists and decisions live in the child phase folders listed below.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- The sk-create-figjam sources, the sk-product-owner sources the findings name, the router copies and their fixtures, the Claude Project mirrors and the playbook scenarios that test them

### Out of Scope
- Any change no Section 9 finding names
- Commits and pushes without the operator's go-ahead

### Files to Change

| File Path | Change Type | Phase | Description |
|-----------|-------------|-------|-------------|
| See each child's spec.md | Modify | 001 to 012 | One finding per child |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:phase-map -->
## PHASE DOCUMENTATION MAP

> Each phase is an independently executable child spec folder.

| Phase | Folder | Focus | Status |
|-------|--------|-------|--------|
| 1 | 001-board-link-resave/ | After a matched read-back the artifact gets the link, is saved again at its export path and read back, and a Doc takes the link under Related references | Complete |
| 2 | 002-pair-phrasing-and-framing/ | Sequencing words keep the board in an artifact pair, and write a doc or write a bug frames its artifact | Complete |
| 3 | 003-hosted-route-facts/ | The packet gives the true reason the hosted call skips Code Mode and says a desktop-only session has no generate_diagram | Complete |
| 4 | 004-critic-pass-source/ | The critic pass takes its screenshot from get_figjam first, checks cut labels and checks that the accent node reads first | Complete |
| 5 | 005-tag-key-and-set/ | The tag names its namespace and key, takes the created set from returned ids or new page-level nodes with sections, and carries no source text | Complete |
| 6 | 006-delivery-pointer-lines/ | The sk-product-owner delivery pointer names every line the Flow reply carries | Complete |
| 7 | 007-revision-plan/ | On a revision the gate names the board and states its plan only when the user supplied it | Complete |
| 8 | 008-dangling-connectors/ | A connector with a missing or canvas-pinned end is a read-back mismatch named as dangling | Complete |
| 9 | 009-pair-reply-ending/ | When the route carries then FLOW, the artifact reply ends on the Flow gate and the ClickUp offer waits until the link is written back | Complete |
| 10 | 010-repeated-label-check/ | The user-flow and process check fails four or more identical labels on non-decision edges | Complete |
| 11 | 011-read-call-allowance/ | The gate states the read calls the write spends, and a read refused for the plan limit gives Read-back not possible with the limit named | Complete |
| 12 | 012-er-cardinality-caps/ | An ER read-back compares each end's cap with the model's cardinality and the arrow rule does not apply to ER markers | Complete |

### Phase Transition Rules

- Each phase MUST pass `validate.sh` independently
- Run `validate.sh --recursive` on the top parent to validate all phases as one unit

### Phase Handoff Criteria

| From | To | Criteria | Verification |
|------|-----|----------|--------------|
| 016-figjam-improvement-research | 001 to 012 | The operator adopted all thirteen findings on 2026-10-21 | 016 goal log |
<!-- /ANCHOR:phase-map -->

---

<!-- ANCHOR:questions -->
## 4. OPEN QUESTIONS

- None.
<!-- /ANCHOR:questions -->

---

## RELATED DOCUMENTS

- **Phase children**: See sub-folders `[0-9][0-9][0-9]-*/`
- **Parent Spec**: See `../spec.md`
