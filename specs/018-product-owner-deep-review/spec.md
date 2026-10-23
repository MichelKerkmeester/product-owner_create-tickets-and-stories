---
title: "Feature Specification: Product Owner deep review"
description: "Five-iteration DeepSeek deep reviews of each Product Owner mode and of the whole repository, with findings the operator can choose to fix."
trigger_phrases:
  - "product owner deep review phase parent spec"
importance_tier: "important"
contextType: "review"
_memory:
  continuity:
    packet_pointer: "018-product-owner-deep-review"
    last_updated_at: "2026-10-21T12:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Opened the deep review packet"
    next_safe_action: "Run the five review lineages"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "1004bf13-7863-4447-a63e-6ad2f5fcfd86"
      parent_session_id: null
    completion_pct: 70
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: phase-parent-spec | v2.2 -->

<!-- SPECKIT_LEVEL: 2 -->

# Feature Specification: Product Owner deep review

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
| **Parent Spec** | None |
| **Parent Packet** | product-owner |
| **Predecessor** | 017-figjam-flow-generation |
| **Successor** | None |
| **Handoff Criteria** | Each child holds a review report and the operator has chosen which findings to fix |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Product Owner grew from one skill into a hub of four packets with a Project mirror, a plugin and a set of gates across 32 phases of work. No review has looked at each packet on its own and at the repository as a whole since then.

### Purpose
Run a five-iteration DeepSeek deep review of each mode and one of the whole repository, so the operator can choose which findings to fix.

> **Phase-parent note:** This spec.md and goal.md are the only authored documents at this level. Plans, tasks, checklists and decisions live in the child phase folders listed below.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- One review child per mode and one for the whole repository
- Two fix children, chosen by the operator on 2026-10-21

### Out of Scope
- Commits and pushes without the operator's go-ahead

### Files to Change

| File Path | Change Type | Phase | Description |
|-----------|-------------|-------|-------------|
| Each child's review/ | Create | 001 to 005 | Iterations, state log and review report |
| Product Owner files named in 006 | Modify | 006 | The own fixes |
| mcp-click-up/, mcp-figma/, vendor.json | Modify | 007 | The vendor pull |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:phase-map -->
## PHASE DOCUMENTATION MAP

> Each phase is an independently executable child spec folder.

| Phase | Folder | Focus | Status |
|-------|--------|-------|--------|
| 1 | 001-sk-product-owner/ | Review the sk-product-owner packet for correctness, contract drift, routing gaps, template and example defects and stale references | Complete |
| 2 | 002-sk-create-figjam/ | Review the sk-create-figjam packet for correctness, check-script bugs, contract drift between references, templates and examples, and stale references | Complete |
| 3 | 003-mcp-click-up/ | Review the vendored mcp-click-up packet for correctness, contract drift and stale references, and how the hub uses it | Complete |
| 4 | 004-mcp-figma/ | Review the vendored mcp-figma packet for correctness, contract drift and stale references, and how the hub uses it | Complete |
| 5 | 005-whole-repo/ | Review the whole Product Owner repository for cross-packet drift, hub routing, mirror and kernel parity, gate and script defects and stale documentation | Complete |
| 6 | 006-own-fixes/ | Fix every review finding whose fix site is a Product Owner file, with its mirrors | Complete |
| 7 | 007-vendor-sync/ | Pull the upstream-fixed mcp-click-up and mcp-figma packets back | Complete |

### Phase Transition Rules

- Each phase MUST pass `validate.sh` independently
- The five runs are independent and run in parallel
- Phase 006 runs after the reviews, and phase 007 runs after the upstream fixes in mcp-tooling packet 023 are committed

### Phase Handoff Criteria

| From | To | Criteria | Verification |
|------|-----|----------|--------------|
| 017-figjam-flow-generation | 001 to 005 | The operator asked for the five reviews on 2026-10-21 | This spec |
<!-- /ANCHOR:phase-map -->

---

<!-- ANCHOR:questions -->
## 4. OPEN QUESTIONS

- None.
<!-- /ANCHOR:questions -->

---

## RELATED DOCUMENTS

- **Phase children**: See sub-folders `[0-9][0-9][0-9]-*/`
