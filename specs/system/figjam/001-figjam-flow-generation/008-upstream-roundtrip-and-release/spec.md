---
title: "Feature Specification: Phase 8: Upstream round-trip and release"
description: "Prove the sync path end to end by pushing one real optimization from Product Owner's vendored copy to .skilled, re-baselining, and releasing the upgrade with a clean-clone test."
trigger_phrases:
  - "upstream roundtrip and release"
  - "figjam phase 8"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Phase 8: Upstream round-trip and release

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
| **Phase** | 8 of 8 |
| **Predecessor** | Last, after 003 to 007. |
| **Successor** | See the parent Phase Documentation Map |
| **Handoff Criteria** | Every row in acceptance-criteria.md is Met |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 8** of the Product Owner FigJam flow generation upgrade specification. Its scope comes from section 15 of `../001-research/research/research.md`.

**Scope Boundary**: Pushes to any git remote without the operator's go-ahead.

**Dependencies**:
- Last, after 003 to 007.

**Deliverables**:
- One real optimization pushed upstream through vendor-sync.py push, such as the confirmed fj flags from 002
- Operator commit in Code_Environment/Public
- pull to re-baseline
- Version bumps, changelog, README
- A clean-clone test

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
The sync tool is only tested against a scratch upstream until a real change crosses into Code_Environment/Public and comes back in step.

### Purpose
Close the loop: one real push, an operator commit upstream, a pull that re-baselines, version bumps, changelog and a clean clone that passes every gate.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- One real optimization pushed upstream through vendor-sync.py push, such as the confirmed fj flags from 002
- Operator commit in Code_Environment/Public
- pull to re-baseline
- Version bumps, changelog, README
- A clean-clone test

### Out of Scope
- Pushes to any git remote without the operator's go-ahead

### Files to Change

Paths are relative to the Product Owner root unless named otherwise.

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| vendor.json | Modify | New base commit |
| changelog/ | Create | Release notes |
| README.md | Modify | Flow Mode and plugin |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | The manifest base commit equals Code_Environment/Public HEAD for the vendored path and status exits 0 |
| REQ-002 | A fresh clone of Product Owner has no dangling links and passes run_gates.sh |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-003 | Every gate from 003 to 007 is rerun from the final state |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: vendor.json's base commit equals Code_Environment/Public HEAD for the mcp-figma path, and vendor-sync.py status exits 0.
- **SC-002**: A fresh git clone of Product Owner into a scratch folder has no dangling links and run_gates.sh exits 0 there.
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | Last, after 003 to 007. | Phase cannot start | Check the predecessor's acceptance criteria first |
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
