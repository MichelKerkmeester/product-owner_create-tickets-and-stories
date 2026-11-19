---
title: "Feature Specification: Phase 2: Write-route spike"
description: "Prove which FigJam write routes work from Claude Code and a claude.ai Project by building one scratch board through the hosted generate_diagram tool and one through figma-ds-cli fj, and record each route's tools, schema and limits."
trigger_phrases:
  - "write route spike"
  - "figjam phase 2"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Phase 2: Write-route spike

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P0 |
| **Status** | Draft |
| **Created** | 2026-10-20 |
| **Branch** | `main` |
| **Parent Spec** | ../spec.md |
| **Phase** | 2 of 8 |
| **Predecessor** | None. Runs in parallel with 003. |
| **Successor** | See the parent Phase Documentation Map |
| **Handoff Criteria** | Every row in acceptance-criteria.md is Met |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 2** of the Product Owner FigJam flow generation upgrade specification. Its scope comes from section 15 of `../001-research/research/research.md`.

**Scope Boundary**: Any Product Owner source edit - this phase only proves routes.

**Dependencies**:
- None. Runs in parallel with 003.

**Deliverables**:
- Tool discovery for the hosted Figma MCP in Claude Code and in a claude.ai Project with the Figma connector: tool names, the generate_diagram schema, file and plan selection, read-back tools
- One scratch board through generate_diagram from the Change Location model, checking stadium, rhombus, circle, edge labels, linkStyle and TD direction
- One scratch board through fj, recording whether create verbs print ids, whether connectors follow moved nodes and how label text nodes place
- Tool discovery against the desktop-local Dev Mode MCP
- A dated capture file per route and a one-page decision note

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
The hosted Figma MCP has one recorded board in this repo and no recorded schema, and the fj route has help output but has never written a node. Flow Mode cannot be designed on an unproven write path.

### Purpose
Confirm the operator's chosen route (hosted generate_diagram primary, fj fallback) with real scratch boards and capture the exact tool surface Flow Mode will call.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Tool discovery for the hosted Figma MCP in Claude Code and in a claude.ai Project with the Figma connector: tool names, the generate_diagram schema, file and plan selection, read-back tools
- One scratch board through generate_diagram from the Change Location model, checking stadium, rhombus, circle, edge labels, linkStyle and TD direction
- One scratch board through fj, recording whether create verbs print ids, whether connectors follow moved nodes and how label text nodes place
- Tool discovery against the desktop-local Dev Mode MCP
- A dated capture file per route and a one-page decision note

### Out of Scope
- Any Product Owner source edit - this phase only proves routes
- Any write to a non-scratch Figma file - boards stay in scratch files

### Files to Change

Paths are relative to the Product Owner root unless named otherwise.

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| scratch/captures/ | Create | Dated tool lists, schemas and help output per route |
| decision-note.md | Create | Primary route and the claude.ai Project answer |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | Build one scratch board through generate_diagram and read back node and connector counts equal to the model |
| REQ-002 | Build one scratch board through fj and read back node and connector counts equal to the model |
| REQ-003 | Capture each route's raw tool list, schema or help output with dates |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-004 | Write a decision note naming the primary route and whether a claude.ai Project can write boards through the Figma connector |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: A scratch FigJam board built through generate_diagram reads back node and connector counts equal to the Change Location model.
- **SC-002**: A scratch FigJam board built through fj reads back node and connector counts equal to the same model.
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | None. Runs in parallel with 003. | Phase cannot start | Check the predecessor's acceptance criteria first |
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
