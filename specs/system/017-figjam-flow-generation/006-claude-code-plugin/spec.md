---
title: "Feature Specification: Phase 6: Claude Code plugin"
description: "Package the Product Owner hub as a skills-only Claude Code plugin on the Media Editor build pattern, with no bin folder and no MCP server entry."
trigger_phrases:
  - "claude code plugin"
  - "figjam phase 6"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Phase 6: Claude Code plugin

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P1 |
| **Status** | Draft |
| **Created** | 2026-10-20 |
| **Branch** | `main` |
| **Parent Spec** | ../spec.md |
| **Phase** | 6 of 8 |
| **Predecessor** | After 005. Runs in parallel with 007. |
| **Successor** | See the parent Phase Documentation Map |
| **Handoff Criteria** | Every row in acceptance-criteria.md is Met |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 6** of the Product Owner FigJam flow generation upgrade specification. Its scope comes from section 15 of `../001-research/research/research.md`.

**Scope Boundary**: An MCP server entry.

**Dependencies**:
- After 005. Runs in parallel with 007.

**Deliverables**:
- claude-plugin/ with .claude-plugin/plugin.json, marketplace.json and a README
- A build script that copies the hub, sk-product-owner and mcp-figma into an untracked skills/ folder with Media Editor's refusals
- .gitignore entries

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Product Owner reaches Claude Code only through this repo. A plugin makes the hub, sk-product-owner and the vendored figma skill installable, but a plugin build that copies sources loosely can ship drifted or linked files.

### Purpose
Build a reproducible, hash-checked skills-only plugin that refuses divergence and links, the way Media Editor's build does.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- claude-plugin/ with .claude-plugin/plugin.json, marketplace.json and a README
- A build script that copies the hub, sk-product-owner and mcp-figma into an untracked skills/ folder with Media Editor's refusals
- .gitignore entries

### Out of Scope
- An MCP server entry
- A bundled figma-ds-cli or bin shim - skills only first (operator, 2026-10-20)

### Files to Change

Paths are relative to the Product Owner root unless named otherwise.

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| claude-plugin/ | Create | Plugin shell |
| scripts/build-plugin | Create | Build script |
| .gitignore | Modify | Ignore built skills/ |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | claude plugin validate exits 0 |
| REQ-002 | Two builds produce identical hash trees, and a planted divergence or link fails the build |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-003 | A claude --plugin-dir session lists the skill and routes the Flow command to Flow Mode |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: claude plugin validate exits 0 on the built plugin.
- **SC-002**: Two consecutive builds produce identical hash trees.
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | After 005. Runs in parallel with 007. | Phase cannot start | Check the predecessor's acceptance criteria first |
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
