---
title: "Feature Specification: Phase 4: Parent hub conversion"
description: "Convert Product Owner into a parent hub on the Moneybird Accountant pattern, with sk-product-owner as the default packet and the vendored mcp-figma as its only tool packet, without changing how existing requests route."
trigger_phrases:
  - "parent hub conversion"
  - "figjam phase 4"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Phase 4: Parent hub conversion

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P1 |
| **Status** | Complete |
| **Created** | 2026-10-20 |
| **Branch** | `main` |
| **Parent Spec** | ../spec.md |
| **Phase** | 4 of 8 |
| **Predecessor** | After 003, which provides the vendored packet. |
| **Successor** | See the parent Phase Documentation Map |
| **Handoff Criteria** | Every row in acceptance-criteria.md is Met |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 4** of the Product Owner FigJam flow generation upgrade specification. Its scope comes from section 15 of `../001-research/research/research.md`.

**Scope Boundary**: Flow Mode content - phase 005.

**Dependencies**:
- After 003, which provides the vendored packet.

**Deliverables**:
- Root SKILL.md, hub-router.json and mode-registry.json
- sk-product-owner/ROUTER.md with the section 2 pointer
- AGENTS.md read order and its four routing surfaces
- A Product Owner hub check ported from check-route-table.py with the vendored exemption
- differential.py and the other routing readers repointed
- Hub gold rows
- Built in a scratch clone and applied as one patch

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Product Owner is a single skill. Adding the figma packet beside it needs the hub registries, router pointers and checks that Moneybird already proved, and its conversion broke routing readers that were not repointed.

### Purpose
Add the hub layer with every routing reader repointed and with fixture counts and default-request token cost held to a measured baseline.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Root SKILL.md, hub-router.json and mode-registry.json
- sk-product-owner/ROUTER.md with the section 2 pointer
- AGENTS.md read order and its four routing surfaces
- A Product Owner hub check ported from check-route-table.py with the vendored exemption
- differential.py and the other routing readers repointed
- Hub gold rows
- Built in a scratch clone and applied as one patch

### Out of Scope
- Flow Mode content - phase 005
- The Claude Project mirror - phase 007

### Files to Change

Paths are relative to the Product Owner root unless named otherwise.

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| SKILL.md | Create | Hub entry |
| hub-router.json | Create | Hub routing |
| mode-registry.json | Create | Packet registry |
| sk-product-owner/ROUTER.md | Create | Router pointer |
| AGENTS.md | Modify | Read order and routing surfaces |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | Router and format fixtures pass with the same counts as a baseline captured first |
| REQ-002 | The hub check passes and fails on three planted defects |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-003 | Gold rows cover a bare request, the existing figma Task fixture, a figma-ds-cli-only request and a negated Figma mention |
| REQ-004 | The default Task request's token cost rises by no more than the hub SKILL.md plus 286 tokens of hub overhead (amended by the operator on 2026-10-20) |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: Router and format fixtures pass with the same counts as the baseline captured before the change.
- **SC-002**: The hub check passes, and fails on each of three planted defects: an unregistered packet folder, a wrong default and a missing router pointer.
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | After 003, which provides the vendored packet. | Phase cannot start | Check the predecessor's acceptance criteria first |
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
