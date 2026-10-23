---
title: "Feature Specification: Phase 11: FigJam packet split"
description: "Flow Mode lives inside the Product Owner packet, so every Product Owner reader carries FigJam rules it never uses. This phase moves it into its own hub packet, sk-create-figjam, which the hub routes to at stage one."
trigger_phrases:
  - "figjam packet split"
  - "sk-create-figjam"
  - "phase 11 figjam packet split"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Phase 11: FigJam packet split

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
| **Phase** | 11 of 12 |
| **Predecessor** | 010-flow-mode-hardening |
| **Successor** | 012-vendored-clickup |
| **Handoff Criteria** | The hub check, run_gates.sh, the format gate and the Sync Loop parity and residency gates pass |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 11** of the Product Owner FigJam flow generation upgrade specification.

**Scope Boundary**: The Flow Mode files move into a new packet, and every reader of their old paths follows them. Flow behavior does not change, and neither does the Claude Project kernel.

**Dependencies**:
- Flow Mode as hardened in phase 010.
- The operator chose on 2026-10-20: the packet is named `sk-create-figjam`, the hub routes to it at stage one, and it reads the Human Voice cards from `sk-product-owner/` rather than copying them.

**Deliverables**:
- `sk-create-figjam/` with `SKILL.md`, `ROUTER.md`, `README.md`, `changelog/`, `references/flow-mode.md`, `assets/flow-templates.md` and `scripts/flow_check.py` with its vendored extractor.
- The hub registry, stage one router and hub check carrying the packet.

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Flow Mode draws boards, and the other five modes write ClickUp artifacts. Both share one packet, so the Product Owner router, SKILL.md and README all carry FigJam rules, and the FigJam work cannot be read, versioned or shipped on its own.

### Purpose
Give FigJam its own hub packet that the hub picks at stage one, the way `mcp-figma` already sits beside `sk-product-owner`.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Move `flow-mode.md`, `flow-templates.md`, `flow_check.py` and `scripts/vendored/` into `sk-create-figjam/`.
- New packet `SKILL.md`, `ROUTER.md`, `README.md` and `changelog/v1.0.0.0.md`.
- Hub `SKILL.md`, `mode-registry.json`, `hub-router.json` and `benchmark/gates/check_hub.py`: the packet row, the `$flow` and `$figjam` commands, the `figjam` signal and new gold rows.
- `sk-product-owner/` ROUTER.md, SKILL.md and README.md: Flow becomes a handoff to the new packet.
- Path readers: `vendor.json`, `run_gates.sh`, `build-plugin.py`, the router fixtures, AGENTS.md, both READMEs, `claude project/README.md`, SYNC.md, the playbook and `systems.py`.

### Out of Scope
- Any change to Flow behavior, the check rules or the Project Knowledge files.
- The kernel. Its router code stays equal to `router-contract.md` minus comments, so its FLOW lane strings stay as they are.

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| sk-create-figjam/ | Create | The packet, with the moved Flow files |
| SKILL.md, mode-registry.json, hub-router.json | Modify | Third packet and its stage one rules |
| benchmark/gates/check_hub.py | Modify | Packet kinds, router sections per packet, gold rows, command routing |
| sk-product-owner/ROUTER.md, SKILL.md, README.md, references/router-contract.md | Modify | Flow handed off to the packet |
| benchmark/router/route_contract.py, fixtures.json | Modify | Lane comment, three Flow fixtures resolve no Flow file here |
| vendor.json, benchmark/gates/run_gates.sh, scripts/build-plugin.py | Modify | New paths |
| AGENTS.md, README.md, claude project/README.md, SYNC.md | Modify | Paths, layout and counts |
| z — Claude Project Sync Loop/systems.py (outer repo) | Modify | Two Flow pairs point at the packet |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | No Flow file remains in `sk-product-owner/`, and every reader of the old paths names the new ones. |
| REQ-002 | The hub sends `$flow`, `$figjam` and a FigJam request with no other artifact to `sk-create-figjam`, and the hub check replays that. |
| REQ-003 | A Flow route that still reaches the Product Owner router hands off to the packet. |
| REQ-004 | run_gates.sh, the differential gate, the format gate and the Sync Loop parity and residency gates pass. |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-005 | SYNC.md records the move as maintenance, and the plugin ships the packet. |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: A Task, Bug, Doc or Story request loads no FigJam file.
- **SC-002**: A FigJam request loads the packet and the two Human Voice cards, and nothing else from `sk-product-owner/`.
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Risk | The Sync Loop refuses a pair path outside `skill_dir` | High | The parity walk resolves `skill_dir / rel` and checks containment in the systems root, proved in a scratch clone |
| Risk | Kernel parity breaks | High | The router code is untouched, only comments change |
| Risk | Stage one misroutes a Task that names FigJam | Med | Artifact words still win, and the Product Owner router hands any Flow route on |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Maintainability
- **NFR-M01**: The Human Voice cards exist once, in `sk-product-owner/references/`.

### Reliability
- **NFR-R01**: The hub check self-test fails on a planted defect for each new rule.
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Error Scenarios
- `$task $flow` is a command conflict and stays with the Product Owner packet, whose Interactive Mode asks one question.
- "make a FigJam flow from the product doc" names the word doc, so stage one keeps it in Product Owner, whose router reads it as Flow and hands it on.

### State Transitions
- A standalone clone without the outer Sync Loop folder still runs every packet gate.
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 16/25 | About 25 files across both repos |
| Risk | 12/25 | Parity-gated router copies and a shared declaration |
| Research | 2/20 | None beyond reading the gates |
| **Total** | **30/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- None. The operator answered the name and the routing on 2026-10-20.
<!-- /ANCHOR:questions -->
