---
title: "Feature Specification: Phase 15: FigJam rebuild"
description: "sk-create-figjam drew user flows only and left most of what sk-design-diagram and the researched FigJam skills teach on the table. It now draws every type Figma's generate_diagram supports, each with a reference, a template, a worked example and a check, mirrored into the Claude Project."
trigger_phrases:
  - "figjam rebuild"
  - "every figjam diagram type"
  - "phase 15 figjam rebuild"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Phase 15: FigJam rebuild

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
| **Phase** | 15 of 15 |
| **Predecessor** | 014-hub-to-root |
| **Successor** | 008-upstream-roundtrip-and-release |
| **Handoff Criteria** | Every diagram type has a reference, a template and a checked example, and every gate passes |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 15** of the Product Owner FigJam flow generation upgrade specification.

**Scope Boundary**: The `sk-create-figjam/` packet, the hub files that route to it, the gates that check it and its Claude Project mirror. Task, Bug, Doc and Story behavior do not change.

**Dependencies**:
- Phase 014's hub at the repository root.
- Phase 009's research corpus on public FigJam diagram skills.
- The shared sk-design-diagram intake, style guide, quality rubric and derivation record, read and translated rather than copied.

**Deliverables**:
- One reference, template and worked example per type, a style guide, a quality rubric and a hybrid workflow.
- `flow_check.py` checking every type, with planted fixtures per rule.
- A packet playbook, hub routing rows and the Project mirror per the SYNC.md parity method.

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
The packet drew one kind of diagram, a user flow, through one reference and one template. Figma's generator draws seven kinds, and the shared diagram skill already holds intake, style and quality rules that a FigJam board needs. The operator called the packet barebones on 2026-10-20.

### Purpose
Draw every type the generator supports to the same standard the user flow already met: a type picked from the reader's question, a model checked before the write, a gate, a read-back and a reply that names what the board leaves out.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- User flow, process, architecture, sequence, state, ER and gantt references, templates and worked examples on fictional companies
- The style guide with a measured palette record, the quality rubric and the hybrid workflow for pins, stickies, tints and legends
- `flow_check.py` with per-type rule modules and a self-test that plants one defect per rule
- The packet SKILL.md routing, README, changelog, the hub router keywords and gold rows, and a packet playbook
- The Claude Project mirror: Knowledge files, kernel Flow sections, resynced statements, router patterns and the parity record

### Out of Scope
- Any edit inside `mcp-figma/`, `mcp-click-up/` or the vendored Mermaid extractor
- Live board writes, which wait for the hosted Figma MCP connection
- A kernel version bump, because v1.2.2 is unreleased

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| sk-create-figjam/references/, assets/, scripts/ | Create, Modify | Types, templates, examples, style, quality, hybrid and the check |
| sk-create-figjam/SKILL.md, README.md, changelog/v1.0.0.0.md, manual-testing-playbook/ | Modify, Create | Routing, orientation, release notes and the playbook |
| SKILL.md, ROUTER.md, AGENTS.md, README.md, description.json, graph-metadata.json, mode-registry.json, leaf-manifest.json, manual-testing-playbook/ | Modify | Hub wording, keywords, the manifest and a routing scenario |
| benchmark/ (gates, router, format, hub-routing-cases.json, reports/) | Modify, Create | Gold rows, fixtures, rule parity homes, the format perimeter and the playbook shell run |
| claude project/ (kernel, README, 25 Knowledge files) | Modify, Create | The Project mirror |
| SYNC.md, sk-product-owner/manual-testing-playbook/ | Modify | The dated record and remapped citations |
| z — Claude Project Sync Loop/systems.py, systems.cjs, validate_parity.py (outer repo) | Modify | Pairs, resynced statements, the format perimeter and a count word |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | Every type the generator draws has a reference, a template where it differs from the user flow, and a worked example that passes `flow_check.py`. |
| REQ-002 | `flow_check.py --self-test` fails every planted defect and passes every template, example and Project mirror. |
| REQ-003 | parent-skill-check, validate_skill_package --strict, run_gates.sh, the format gates, reference parity, the playbook validators and the plugin build pass. |
| REQ-004 | The Project mirror passes the Sync Loop parity and residency gates in a scratch clone. |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-005 | A request for a FigJam sequence, ER or gantt diagram routes to `sk-create-figjam` at the hub and to Flow Mode in the kernel router. |
| REQ-006 | A kind the generator cannot draw is named as such, with the nearest drawable type offered. |
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: A reader asking which statuses a booking passes through gets a state diagram, not a flowchart.
- **SC-002**: No model reaches a board with a construct the generator drops or mangles.
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Risk | The vendored extractor misreads some types | High | The check parses sequence, ER and gantt itself and preprocesses the rest, and the vendored file stays a byte copy |
| Risk | A Project mirror drifts from its source | Med | One transform script writes every mirror, and the check reads the mirrors in its self-test |
| Risk | Kernel line citations shift | Med | Every citation was remapped and verified against the line it named before |
| Dependency | Hosted Figma MCP | Med | Live writes stay in phase 002 and the playbook marks them SKIP until connected |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Maintainability
- **NFR-M01**: One rule module per type under `scripts/figjam_checks/`.

### Reliability
- **NFR-R01**: The check self-test runs inside the built plugin without the Project files.
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Error Scenarios
- A flowchart with no `%% type:` line is a user flow, so a process or an architecture must name itself.
- Two types fit one request, such as an architecture and a sequence, so the workflow asks before drawing.
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 22/25 | About 60 new files and 40 edited across three repositories |
| Risk | 12/25 | Parity-gated mirrors and a shared declaration |
| Research | 10/20 | Phase 009's corpus and the shared diagram skill |
| **Total** | **44/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- None. The operator chose every type, the hybrid workflow and the Project mirror on 2026-10-20.
<!-- /ANCHOR:questions -->
