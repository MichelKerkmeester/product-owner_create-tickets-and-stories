---
title: "Feature Specification: Phase 14: Hub to root"
description: "Phase 13 moved the hub into product-owner/ to pass the skilled checkers. The operator wants it back at the repository root, as Moneybird Accountant keeps it, so the hub declares its repository entries through the new repo-root-hub extension."
trigger_phrases:
  - "hub to root"
  - "repo-root-hub product owner"
  - "phase 14 hub to root"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Phase 14: Hub to root

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
| **Phase** | 14 of 15 |
| **Predecessor** | 013-skilled-hub-alignment |
| **Successor** | 015-figjam-rebuild |
| **Handoff Criteria** | parent-skill-check.cjs on the repository root reports 0 failures, validate_skill_package.py --strict passes on the root and its packets, and every gate 013 passed still passes |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 14** of the Product Owner FigJam flow generation upgrade specification.

**Scope Boundary**: The hub's location and every reader of its paths. Routing, mode behavior, templates and the Claude Project kernel do not change.

**Dependencies**:
- Phase 013's hub on the skilled contract.
- The `repo-root-hub` extension added to the shared skilled checkers in the Code_Environment packet `specs/sk-doc/068-hub-repo-folder-exemption`.
- The operator asked on 2026-10-20 for the hub at the repository root, as Moneybird Accountant keeps it.

**Deliverables**:
- The hub files and the four packets at the repository root, with `repo-root-hub` declared in `mode-registry.json`.
- Every gate, script, doc and the outer Sync Loop declaration pointed at the root.

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
The skilled checkers read a whole folder as the skill, so phase 013 had to put the hub in `product-owner/` to pass. That adds a folder level every reader has to know about, and Moneybird Accountant keeps its hub at its root.

### Purpose
Put the hub back at the repository root with no checker exemption beyond the entries the hub itself declares.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Move every file in `product-owner/` to the repository root, and the hub benchmark files into the system `benchmark/`
- Declare `repo-root-hub` in `mode-registry.json` with the repository's own entries
- Point the gates, the plugin build, the format validators, the docs and the outer Sync Loop declaration at the root

### Out of Scope
- The shared checker change itself, which is the Code_Environment packet's
- Any edit inside `mcp-figma/` or `mcp-click-up/`
- The Claude Project kernel and Knowledge files

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| product-owner/ | Delete | Its files move to the root |
| SKILL.md, ROUTER.md, mode-registry.json, hub-router.json, description.json, graph-metadata.json, leaf-manifest.json, changelog/, manual-testing-playbook/ | Create | The hub at the root |
| benchmark/README.md, benchmark/hub-routing-cases.json, benchmark/gates/check_hub.py | Modify | The hub benchmark beside the system gates |
| benchmark/gates/run_gates.sh, rule_parity.py, benchmark/router/*.py, benchmark/format/validate-output-format.cjs, scripts/build-plugin.py | Modify | Root paths |
| AGENTS.md, README.md, SYNC.md, packet READMEs and SKILL.md files | Modify | Root paths and layout |
| z — Claude Project Sync Loop/systems.py, systems.cjs (outer repo) | Modify | The skill folders at the root |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | `parent-skill-check.cjs` on the repository root reports 0 failures and 0 warnings. |
| REQ-002 | `validate_skill_package.py --strict` passes on the root and its four packets. |
| REQ-003 | run_gates.sh, the format gates, reference parity, the playbook validators, the plugin build and the Sync Loop parity and residency gates pass. |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-004 | No file outside `specs/` and the dated SYNC.md record names the `product-owner/` folder. |
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: A reader finds `SKILL.md` at the repository root.
- **SC-002**: The plugin still installs the hub as `skills/product-owner/`.
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Risk | A rewritten link points at the wrong depth | Med | Links were recomputed from the old and new file locations, then a link check ran |
| Risk | A repository folder ships in the plugin | Med | The plugin build copies the registry's packets only, and a self-test proves a repository folder never ships |
| Dependency | The shared checker change | High | Both checkers were rerun on the root after it landed |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Maintainability
- **NFR-M01**: One list of repository entries, in `mode-registry.json`.

### Reliability
- **NFR-R01**: A clone without `export/` passes the same checks.
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Error Scenarios
- `benchmark/` holds snake_case gate scripts, so it is declared a repository entry rather than read as a hub folder.
- `AGENTS.md` is both a repository bootstrap and a file the plugin ships, so the plugin build names it explicitly.
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 18/25 | 68 files rewritten plus the move |
| Risk | 12/25 | Parity-gated files and a shared declaration |
| Research | 4/20 | A probe copy named every blocker |
| **Total** | **34/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- None. The operator chose the repository root and a hub-declared list on 2026-10-20.
<!-- /ANCHOR:questions -->
