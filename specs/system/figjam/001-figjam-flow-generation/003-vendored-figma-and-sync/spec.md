---
title: "Feature Specification: Phase 3: Vendored figma skill and sync"
description: "Give Product Owner a byte-identical vendored copy of the mcp-figma skill with a manifest and a vendor-sync.py tool whose status, pull and push keep it in step with .skilled."
trigger_phrases:
  - "vendored figma and sync"
  - "figjam phase 3"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Phase 3: Vendored figma skill and sync

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P0 |
| **Status** | Complete |
| **Created** | 2026-10-20 |
| **Branch** | `main` |
| **Parent Spec** | ../spec.md |
| **Phase** | 3 of 8 |
| **Predecessor** | None. First build phase, runs in parallel with 002. |
| **Successor** | See the parent Phase Documentation Map |
| **Handoff Criteria** | Every row in acceptance-criteria.md is Met |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 3** of the Product Owner FigJam flow generation upgrade specification. Its scope comes from section 15 of `../001-research/research/research.md`.

**Scope Boundary**: Hub registries, routing and Flow Mode - phases 004 and 005.

**Dependencies**:
- None. First build phase, runs in parallel with 002.

**Deliverables**:
- mcp-figma/ copied byte for byte at the Product Owner root
- vendor.json manifest with the upstream path and base commit
- scripts/vendor-sync.py with status, pull and push
- Tests against a scratch git repository standing in for Code_Environment/Public
- A vendor-sync status hook in benchmark/gates/run_gates.sh

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
The figma skill lives only in the shared .skilled repo, which is a different git repo from Product Owner. Without a manifest and a sync tool, an embedded copy drifts silently and optimizations never reach upstream.

### Purpose
Make the embedded copy provably identical at a recorded base commit, detect drift in either direction, and move changes both ways with one command.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- mcp-figma/ copied byte for byte at the Product Owner root
- vendor.json manifest with the upstream path and base commit
- scripts/vendor-sync.py with status, pull and push
- Tests against a scratch git repository standing in for Code_Environment/Public
- A vendor-sync status hook in benchmark/gates/run_gates.sh

### Out of Scope
- Hub registries, routing and Flow Mode - phases 004 and 005
- Any write into Code_Environment/Public - phase 008 does the one real push

### Files to Change

Paths are relative to the Product Owner root unless named otherwise.

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| mcp-figma/ | Create | Vendored copy |
| vendor.json | Create | Manifest |
| scripts/vendor-sync.py | Create | Sync tool |
| benchmark/gates/run_gates.sh | Modify | Add the status gate |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | Copy mcp-figma byte for byte and record the base commit in vendor.json |
| REQ-002 | vendor-sync.py status exits 0 when in step and 1 on any local or upstream drift |
| REQ-003 | pull refuses over local edits and push writes a reviewable diff to the upstream |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-004 | run_gates.sh runs the status check |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: sha256 of every file under mcp-figma/ equals upstream at the base commit in vendor.json.
- **SC-002**: vendor-sync.py status exits 0 right after pull, and exits 1 after a one-byte local edit while pull refuses.
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | None. First build phase, runs in parallel with 002. | Phase cannot start | Check the predecessor's acceptance criteria first |
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
