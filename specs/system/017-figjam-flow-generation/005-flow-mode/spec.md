---
title: "Feature Specification: Phase 5: Flow Mode"
description: "Add Flow Mode to sk-product-owner so a request turns screenshots, Figma flows or product docs into a checked Mermaid model and a FigJam board, delivered as the board URL with a read-back line and the HVR self-scan line."
trigger_phrases:
  - "flow mode"
  - "figjam phase 5"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Phase 5: Flow Mode

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P1 |
| **Status** | In Progress |
| **Created** | 2026-10-20 |
| **Branch** | `main` |
| **Parent Spec** | ../spec.md |
| **Phase** | 5 of 8 |
| **Predecessor** | After 002 (confirmed route and schema) and 004 (hub routing). |
| **Successor** | See the parent Phase Documentation Map |
| **Handoff Criteria** | Every row in acceptance-criteria.md is Met |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 5** of the Product Owner FigJam flow generation upgrade specification. Its scope comes from section 15 of `../001-research/research/research.md`.

**Scope Boundary**: Plugin packaging - phase 006.

**Dependencies**:
- After 002 (confirmed route and schema) and 004 (hub routing).

**Deliverables**:
- references/flow-mode.md and assets/flow-templates.md with Mermaid patterns
- The Flow command and routing rows
- A pre-write check built on mermaid_extract.py
- The write procedure for the hosted route with the fj fallback
- The delivery rule: board URL, a read-back line and the HVR self-scan line, with Flow Mode exempt from the export file step in AGENTS.md

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Product Owner has no mode that produces diagrams, and its export protocol blocks every reply until a markdown file is saved, which does not fit a board delivered in Figma.

### Purpose
Ship the end-to-end flow path: input to Mermaid model, a pre-write check built on sk-design-diagram rules, the write through the route 002 confirmed, and URL delivery exempt from the export file rule.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- references/flow-mode.md and assets/flow-templates.md with Mermaid patterns
- The Flow command and routing rows
- A pre-write check built on mermaid_extract.py
- The write procedure for the hosted route with the fj fallback
- The delivery rule: board URL, a read-back line and the HVR self-scan line, with Flow Mode exempt from the export file step in AGENTS.md

### Out of Scope
- Plugin packaging - phase 006
- The Claude Project mirror - phase 007

### Files to Change

Paths are relative to the Product Owner root unless named otherwise.

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| sk-product-owner/references/flow-mode.md | Create | Flow Mode rules |
| sk-product-owner/assets/flow-templates.md | Create | Mermaid patterns |
| AGENTS.md | Modify | Flow Mode export exemption |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | The pre-write check fails bad models and passes the Change Location model |
| REQ-002 | One end-to-end board from the 7 Change Location screenshots reads back counts equal to the model |
| REQ-003 | Flow Mode replies with the board URL, a read-back line and the HVR self-scan line and writes no file to export/ |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-004 | Router fixtures pass for the Flow command and a plain FigJam request |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: The pre-write check fails a four-exit decision, an unlabelled decision exit, an unknown shape and a 10-node diagram, and passes the Change Location model.
- **SC-002**: Router fixtures pass for the Flow command and for "make a FigJam flow from these screenshots".
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | After 002 (confirmed route and schema) and 004 (hub routing). | Phase cannot start | Check the predecessor's acceptance criteria first |
| Risk | Public-repo leak of board URLs or Barter screenshots | High | Keep them out of tracked files, per research section 14 |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Security
- **NFR-S01**: No secrets, tokens or Figma file keys in tracked files.

### Reliability
- **NFR-R01**: Every check in this phase is rerun from the final state before the phase closes.
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Error Scenarios
- External service failure: stop and record the failure in the goal log, never fake a pass.

### State Transitions
- Partial completion: the goal log records what is done and the next step.
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 12/25 | See Files to Change |
| Risk | 10/25 | Public repo, shared gates |
| Research | 6/20 | Done in 001-research |
| **Total** | **28/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- See section 17 of `../001-research/research/research.md` for the operator questions this phase depends on.
<!-- /ANCHOR:questions -->
