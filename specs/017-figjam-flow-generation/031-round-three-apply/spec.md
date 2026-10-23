---
title: "Feature Specification: Phase 31: Round three apply"
description: "The 32 ranked changes of phase 030 applied as 32 child phases: an interactive intake for both packets, input-to-model logic and FigJam design output."
trigger_phrases:
  - "round three apply phase parent spec"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "017-figjam-flow-generation/031-round-three-apply"
    last_updated_at: "2026-10-21T11:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Opened the round three apply phase parent"
    next_safe_action: "Run the intake wave"
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

# Feature Specification: Phase 31: Round three apply

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
| **Predecessor** | 030-figjam-research-three |
| **Successor** | None |
| **Handoff Criteria** | Every child applies its change and validates alone |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Both packets ask one round of questions and then draw, the AI reads screenshots and product logic into a model with no stated order of inference, and nothing governs how a finished board composes. Phase 030 ranked 32 changes across those three questions.

### Purpose
Apply all 32, one child phase per change, in three waves: the intake first, then the input logic, then the design output, each wave built on the text the one before left.

> **Phase-parent note:** This spec.md and goal.md are the only authored documents at this level. Plans, tasks, checklists and decisions live in the child phase folders listed below.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- sk-create-figjam, the sk-product-owner intake files, the hub router prose, the kernel, the Claude Project mirrors, the check script and the playbook generator

### Out of Scope
- Any change phase 030 did not rank
- Commits and pushes without the operator's go-ahead

### Files to Change

| File Path | Change Type | Phase | Description |
|-----------|-------------|-------|-------------|
| See each child's spec.md | Modify | 001 to 032 | One ranked change per child |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:phase-map -->
## PHASE DOCUMENTATION MAP

> Each phase is an independently executable child spec folder. 001 to 011 are the intake, 012 to 023 the input logic and 024 to 032 the design output.

| Phase | Folder | Focus | Status |
|-------|--------|-------|--------|
| 1 | 001-intake-brief/ | Add the nine-row Brief with a status per row to Flow Mode intake | Complete |
| 2 | 002-draw-ready-stop-rule/ | Add the draw-ready threshold, the ordered stop rule and the energy cap | Complete |
| 3 | 003-question-bank/ | Add the question bank with a recommended answer per question | Complete |
| 4 | 004-sparring-outline-pass/ | Add the sparring step and the outline pass | Complete |
| 5 | 005-playback-and-gate-line/ | Add the per-round replay, the single playback and the gate line | Complete |
| 6 | 006-challenge-ladder/ | Add the challenge ladder and the type-first sequencing | Complete |
| 7 | 007-po-lane-board-block/ | Give the Product Owner lane a board block and one named exception | Complete |
| 8 | 008-quick-and-just-do-it/ | Add the Quick and just-do-it rules for board facts | Complete |
| 9 | 009-kernel-carries-loop/ | Carry the loop in the kernel and rebuild the two mirrors by hand | Complete |
| 10 | 010-intake-in-always-and-router/ | Name the intake in the packet's ALWAYS list and the ROUTER FLOW row | Complete |
| 11 | 011-intake-test-contract/ | Carve out the test contract and add four scenarios | Complete |
| 12 | 012-reaction-graph-first/ | Read the reaction graph before any frame content | Complete |
| 13 | 013-intake-record-per-item/ | Keep one intake record per item, with a class and a confidence | Complete |
| 14 | 014-verify-image-labels/ | Verify an image-derived label before it becomes a node | Complete |
| 15 | 015-inference-ladder/ | State the inference ladder | Complete |
| 16 | 016-screen-or-state/ | Decide screen against state by the action that reaches it | Complete |
| 17 | 017-criterion-as-triple/ | Read an acceptance criterion as a triple | Complete |
| 18 | 018-edge-actor/ | Give an edge an actor | Complete |
| 19 | 019-source-evidence-limits/ | Name what each source can and cannot evidence | Complete |
| 20 | 020-type-against-needs-row/ | Test the chosen type against its needs row | Complete |
| 21 | 021-contradicted-item-surface/ | Give a contradicted item a surface the reply already has | Complete |
| 22 | 022-chunk-allocation/ | Allocate the chunks from the source list before drawing | Complete |
| 23 | 023-pre-gate-reread/ | Re-read only the rows that fail silently, before the gate | Complete |
| 24 | 024-first-glance/ | Write the first glance down before modelling | Complete |
| 25 | 025-visible-titles/ | Put a visible title on every diagram, not only when asked | Complete |
| 26 | 026-spacing-scale/ | Give the board a spacing scale and a proximity ratio | Complete |
| 27 | 027-multi-diagram-board/ | Compose a multi-diagram board instead of appending to it | Complete |
| 28 | 028-better-mermaid-lane-order/ | Define what 'better Mermaid' means, and verify lane order | Complete |
| 29 | 029-legend-as-key/ | Make the legend the board's key, and give tints a second channel | Complete |
| 30 | 030-reading-distance-dial/ | Add reading distance as the third dial | Complete |
| 31 | 031-pre-write-layout-check/ | Measure the graph before the write, not after | Complete |
| 32 | 032-composition-scorecard/ | Rebuild the scorecard around composition, at two zooms | Complete |

### Phase Transition Rules

- Each phase MUST pass `validate.sh` independently
- The three waves run in order, and the phases inside a wave run in parallel

### Phase Handoff Criteria

| From | To | Criteria | Verification |
|------|-----|----------|--------------|
| 030-figjam-research-three | 001 to 032 | The operator adopted all 32 ranked changes on 2026-10-21 | 030 syntheses |
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
