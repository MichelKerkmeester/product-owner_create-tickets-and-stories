---
title: "Feature Specification: Phase 36: FigJam design system research"
description: "Composed FigJam boards vary in design quality and consistency across diagram types, and a repo user cannot restyle them. This phase runs 7 deep-research iterations across three lineages on sk-create-figjam and ends in ranked design changes and a recommendation on a user-editable design spec file."
trigger_phrases:
  - "figjam design system research"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Phase 36: FigJam design system research

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P1 |
| **Status** | Complete |
| **Created** | 2026-10-25 |
| **Branch** | `main` |
| **Parent Spec** | ../spec.md |
| **Phase** | 36 of 37 |
| **Predecessor** | 035-first-glance-and-routing |
| **Successor** | 037-figjam-design-spec |
| **Handoff Criteria** | research/research.md exists with at least 10 ranked design changes and a design spec file recommendation, and the operator has chosen what to apply |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 36** of the Product Owner FigJam flow generation upgrade specification.

**Scope Boundary**: Research and synthesis only. No Product Owner source file changes.

**Dependencies**:
- sk-create-figjam as it stands after phase 035: the composer, the templates, the examples, the nine rendered board screenshots, the style guide, the quality rubric, the type references and compose_board.py.
- The DESIGN.md Style Reference idea that the sk-design-md-generator mode of the sk-design skill produces, read as a model for a user-editable design spec file.

**Deliverables**:
- Iteration files and a deep-research state log per lineage under `research/lineages/`: 3 from claude-opus-5-5, 2 from swe-2-max and 2 from gpt-6-luna.
- `research/research.md`, the synthesis written by a fresh Opus 5.5 medium agent, with the merged registry in `research/findings-registry.json` and the lineage attribution in `research/fanout-attribution.md`.

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Boards composed by sk-create-figjam follow a style guide and a rubric, yet their visual quality and consistency still vary from one diagram type to the next. The colours, type, spacing, shapes and connectors live in the composer and the references, so a repo user who wants boards in their own style has no single place to change them.

### Purpose
Produce evidence-cited findings, a ranked list of design changes and a recommendation on a user-editable design spec file that agents read before composing a board.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- The design quality of composed boards: colour, type, spacing, shapes, connectors, zones, the key and the title, read from the sources and the nine rendered screenshots.
- Consistency across diagram types: the same element drawn the same way in every type reference, template and example.
- A user-editable design spec file in the spirit of a DESIGN.md Style Reference: where it lives, its schema, how compose_board.py and the Project read it, how defaults stay safe and how the rubric checks against it.
- The inputs: `sk-create-figjam/assets/compose-board.js`, `assets/flow-templates.md`, `assets/templates/`, `assets/examples/`, `assets/screenshots/`, `references/style-guide.md`, `references/quality-rubric.md`, `references/types/` and `scripts/compose_board.py`.

### Out of Scope
- Editing the packet, its Project mirror or the kernel. This phase proposes, a later phase applies.
- Any Barter screenshot, Barter flow, board URL or Figma file key.

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| research/ | Create | Lineages, iterations, state logs and the synthesis, made by the workflow |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | Run 7 deep-research iterations as a fan-out with one lineage per executor and convergence stopping disabled: claude-opus-5-5 at medium effort through cli-claude-code for 3, swe-2-max through cli-devin for 2 and gpt-6-luna at max effort on the fast service tier through cli-codex for 2. The workflow then merges the lineages and writes `research/research.md`. |
| REQ-002 | Each iteration cites files as [SOURCE: path:line] and names the image file for any screenshot it draws on. |
| REQ-003 | The synthesis ranks at least 10 design changes, each naming the file it changes and the evidence, with at least 3 on consistency across diagram types. |
| REQ-004 | The synthesis recommends a design spec file: its location, its schema with tokens for colour, type, spacing, shapes, connectors, zones, key and title, how compose_board.py and the Project read it, how defaults stay safe when a user edits it and how the quality rubric checks against it. |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-005 | The orchestrator posts a one-line status about every 3 minutes while lineages run. |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: 7 iteration records exist across the three lineages and none ends its lineage early.
- **SC-002**: The operator can choose what to apply from `research/research.md` alone.
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | cli-claude-code, cli-devin and cli-codex | A lineage stalls | Rerun the iteration on the same executor and log it |
| Risk | Model claims drift from the cited lines | High | The synthesis opens every cited line it uses |
| Risk | A screenshot read without vision support | Med | Iterations name the image file so a claim can be checked by eye |
| Risk | A spec file that breaks boards when a user edits it badly | Med | REQ-004 asks how defaults stay safe |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Security
- **NFR-S01**: No secrets or tokens in research files or logs.
- **NFR-S02**: No Barter screenshot, Barter flow, board URL or Figma file key enters a prompt or an output.

### Reliability
- **NFR-R01**: A failed iteration is rerun, never skipped, so the count stays at 7.
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Error Scenarios
- Empty model output at exit 0: treat as a miss and rerun the iteration.
- A cited line that does not say what the iteration claims: the synthesis drops or corrects the claim and lists it.

### State Transitions
- Partial completion: resume each lineage from the last iteration record in its state log.
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 8/25 | Research files only |
| Risk | 6/25 | External models, no source edits |
| Research | 16/20 | 7 iterations across three lineages plus a design spec recommendation |
| **Total** | **30/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- Which of the ranked design changes should the next sk-create-figjam revision apply, and should it ship the design spec file? The operator decides.
<!-- /ANCHOR:questions -->
