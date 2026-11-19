---
title: "Feature Specification: Phase 13: Skilled hub alignment"
description: "The Product Owner hub was modelled on Moneybird Accountant, so the skilled parent-hub checker fails it 39 times. This phase moves the hub into a product-owner/ folder and rebuilds it on the sk-create-skill parent-hub contract."
trigger_phrases:
  - "skilled hub alignment"
  - "product-owner hub folder"
  - "phase 13 skilled hub alignment"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Phase 13: Skilled hub alignment

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
| **Phase** | 13 of 15 |
| **Predecessor** | 012-vendored-clickup |
| **Successor** | 014-hub-to-root |
| **Handoff Criteria** | parent-skill-check.cjs reports 0 failures, validate_skill_package.py --strict passes on the hub and both workflow packets, and every existing gate still passes |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 13** of the Product Owner FigJam flow generation upgrade specification.

**Scope Boundary**: The hub's location, its metadata files, its stage one and stage two routing documents, the two workflow packets' `SKILL.md` routing sections, and every reader of the moved paths. Mode behavior, templates, the Flow check rules and the Claude Project kernel do not change.

**Dependencies**:
- The four-packet hub from phases 004, 011 and 012.
- The skilled parent-hub contract in `.skilled/skills/sk-doc/sk-create-skill/`, its validator `validate_skill_package.py` and the checker `.skilled/commands/doctor/scripts/parent-skill-check.cjs`.
- The operator asked on 2026-10-20 for perfect sk-create-skill alignment and routing like every skilled parent hub, and chose to move the hub into a `product-owner/` folder.

**Deliverables**:
- `product-owner/` holding `SKILL.md`, `ROUTER.md`, `mode-registry.json`, `hub-router.json`, `description.json`, `graph-metadata.json`, `leaf-manifest.json`, `changelog/`, `manual-testing-playbook/`, `benchmark/` and the four packets.
- Packet routing in each workflow packet's `SKILL.md` Section 2, with the packet `ROUTER.md` files retired.

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
The hub copies Moneybird Accountant's shape: the repository root is the hub, each workflow packet keeps its router in a `ROUTER.md`, and `hub-router.json` holds a schema no skilled tool reads. Run against the skilled contract it fails 39 invariants. The folder name `Product Owner` is not the skill name, compiled routing refuses it as an unsafe path, and `specs/`, `export/`, `claude project/` and `claude-plugin/` count as stray packets and second identities.

### Purpose
Make the hub pass the skilled parent-hub checker and the skill package validator with no exemption, routed the way `mcp-tooling`, `sk-doc` and `sk-code` route.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Move `SKILL.md`, `mode-registry.json`, `hub-router.json` and the four packets into `product-owner/`. `AGENTS.md`, `README.md`, `SYNC.md`, `vendor.json`, `specs/`, `export/`, `claude project/`, `claude-plugin/`, the system `benchmark/` and `scripts/` stay at the repository root.
- Registry and hub router in the canonical schema, with the Product Owner stage one rules kept as a declared policy extension.
- A root `ROUTER.md` in the active state, `description.json`, the one `graph-metadata.json`, a generated `leaf-manifest.json`, a hub changelog, a hub playbook and a hub benchmark baseline.
- Packet routing moved into each workflow packet's `SKILL.md` Section 2 with the canonical resource discovery, and the packet-level identity files removed.
- Every reader of a moved path: the gates, the router oracle and fixtures, the format validators, the plugin build, the vendor sync, the playbook, the docs and the outer Sync Loop declaration.

### Out of Scope
- Any edit inside `mcp-figma/` or `mcp-click-up/`, which stay upstream-owned.
- The Claude Project kernel and Knowledge files. The kernel's router code stays equal to `router-contract.md`.
- Compiled-routing activation. The hub carries the directive, which returns the legacy sentinel until a manifest exists.

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| product-owner/ | Create | The hub folder, holding the moved hub files and packets |
| product-owner/ROUTER.md, description.json, graph-metadata.json, leaf-manifest.json | Create | Hub stage two and metadata |
| product-owner/changelog/, manual-testing-playbook/, benchmark/ | Create | Hub companions |
| product-owner/mode-registry.json, hub-router.json, SKILL.md | Modify | Canonical schema and thin hub |
| product-owner/sk-product-owner/SKILL.md, sk-create-figjam/SKILL.md | Modify | Packet routing in Section 2 |
| benchmark/, scripts/, vendor.json | Modify | Readers of the moved paths |
| AGENTS.md, README.md, SYNC.md, claude project/README.md | Modify | Paths and layout |
| z — Claude Project Sync Loop/systems.py, systems.cjs, validate-output-format.cjs (outer repo) | Modify | The moved skill folders |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | `parent-skill-check.cjs product-owner` reports 0 failures and 0 warnings. |
| REQ-002 | `validate_skill_package.py --strict` passes on the hub, `sk-product-owner` and `sk-create-figjam`. |
| REQ-003 | Stage one still routes every hub gold row as before, and stage two still routes every router fixture and differential row. |
| REQ-004 | run_gates.sh, the format gate, the playbook validator, the plugin build and the Sync Loop parity and residency gates pass. |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-005 | No packet carries a `ROUTER.md`, `graph-metadata.json` or leaf-manifest file, and no doc names a retired path. |
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: A skilled tool reads the Product Owner hub the way it reads `mcp-tooling`.
- **SC-002**: A Task, Bug, Doc or Story request still loads exactly the resources it loaded before the move.
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Risk | A moved path breaks a reader nobody runs | High | Every gate, the plugin build and the Sync Loop gates run from the final tree, and a grep for retired paths runs last |
| Risk | Kernel parity breaks | High | `router-contract.md` keeps its router code byte for byte |
| Risk | Stage one changes behavior | Med | The hub gold rows replay unchanged against the new schema |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Maintainability
- **NFR-M01**: One stage two router at the hub root and one routing section per packet.

### Reliability
- **NFR-R01**: The hub check self-test fails on a planted defect for each rule it enforces.
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Error Scenarios
- A clone without the outer Sync Loop folder still runs every Product Owner gate.
- The plugin installs the hub as `skills/product-owner/`, whose folder name now equals its skill name.
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 20/25 | The hub move touches most path readers in two repositories |
| Risk | 14/25 | Parity-gated files and a shared declaration |
| Research | 4/20 | The skilled contract is read, not designed |
| **Total** | **38/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- None. The operator chose the `product-owner/` folder on 2026-10-20.
<!-- /ANCHOR:questions -->
