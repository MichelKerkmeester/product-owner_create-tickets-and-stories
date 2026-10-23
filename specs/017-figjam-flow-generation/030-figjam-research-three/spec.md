---
title: "Feature Specification: Phase 30: FigJam research round three"
description: "Three five-iteration DeepSeek research runs: FigJam design output, turning screenshots and product logic into a model, and an interactive intake that asks until confident and spars on what the board conveys."
trigger_phrases:
  - "figjam research round three phase parent spec"
importance_tier: "important"
contextType: "research"
_memory:
  continuity:
    packet_pointer: "017-figjam-flow-generation/030-figjam-research-three"
    last_updated_at: "2026-10-21T10:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Opened the third research round"
    next_safe_action: "Run the three lineages"
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

# Feature Specification: Phase 30: FigJam research round three

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
| **Predecessor** | 029-extension-fixes |
| **Successor** | None |
| **Handoff Criteria** | Each child holds a checked synthesis and the operator has chosen which changes to apply |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
The FigJam packet checks a model's structure, but three questions are still open: how a finished board can look and read better, how the AI should read screenshots and product logic into a correct model, and how both packets should keep asking, and push back, until they know enough to draw the right board.

### Purpose
Answer each question with a five-iteration DeepSeek research run and a checked, ranked synthesis the operator can choose from.

> **Phase-parent note:** This spec.md and goal.md are the only authored documents at this level. Plans, tasks, checklists and decisions live in the child phase folders listed below.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Research and synthesis only, one child per question

### Out of Scope
- Any Product Owner source change, which follows only after the operator chooses
- Commits and pushes without the operator's go-ahead

### Files to Change

| File Path | Change Type | Phase | Description |
|-----------|-------------|-------|-------------|
| Each child's research/ | Create | 001 to 003 | Iterations, state log and synthesis |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:phase-map -->
## PHASE DOCUMENTATION MAP

> Each phase is an independently executable child spec folder.

| Phase | Folder | Focus | Status |
|-------|--------|-------|--------|
| 1 | 001-design-output/ | Find how sk-create-figjam's FigJam diagrams can look and read better: layout, hierarchy, colour, density, labels, annotation and the board as a whole | Complete |
| 2 | 002-input-to-model-logic/ | Find how the AI can most reliably turn screenshots, Figma flows and product logic into a correct FigJam model: extraction, inference, ordering, gaps and checks | Complete |
| 3 | 003-interactive-intake/ | Design an intake for sk-product-owner and sk-create-figjam that keeps asking until it is confident it understands the feature, and spars with the user on what the board conveys and how it looks | Complete |

### Phase Transition Rules

- Each phase MUST pass `validate.sh` independently
- The three runs are independent and run in parallel

### Phase Handoff Criteria

| From | To | Criteria | Verification |
|------|-----|----------|--------------|
| 029-extension-fixes | 001 to 003 | The operator asked for the three runs on 2026-10-21 | This spec |
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
