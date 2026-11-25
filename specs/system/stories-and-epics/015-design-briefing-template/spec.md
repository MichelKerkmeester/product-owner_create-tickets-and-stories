---
title: "Feature Specification: Design briefing template"
description: "Product Owner gains a design briefing for the Product Design team as its own artifact kind, with a $briefing command, a Briefing Mode reference, a template, three worked examples, Project mirrors and a format gate that accepts plain bullets under a Why facet in a briefing."
trigger_phrases:
  - "design briefing template"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.4 -->
# Feature Specification: Design briefing template

<!-- SPECKIT_LEVEL: 1 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 1 |
| **Priority** | P1 |
| **Status** | Complete |
| **Created** | 2026-11-25 |
| **Branch** | `main` |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Michel writes briefings for the Product Design team by hand, such as `Briefing - Partner & Creator - Barter Deals - Desired Collab Amount & Reach Pause`. Product Owner had no shape for them. A first pass added the briefing as a sixth task shape, and Michel then decided a briefing is not a task, so it now stands beside Task, Bug, Doc and Story as its own artifact kind. A briefing also carries a `**Why**` facet of plain bullets inside Requirements, which the format gate reports as a plain bullet outside a User flow.

### Purpose
Product Owner writes a design briefing from its own mode and template, in the layout Michel approved, a request for one never routes as a task, and the gate accepts the briefing's one plain-bullet facet and nothing wider.
<!-- /ANCHOR:problem -->

<!-- ANCHOR:measured-behavior -->
### Measured Behavior
```text
$ node "z — Claude Project Sync Loop/validate-output-format.cjs" --system product-owner <example-full>
3 errors, one per Why bullet: a plain bullet inside Requirements outside a User flow
```
<!-- /ANCHOR:measured-behavior -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Title `Briefing - {App or Apps} - {Area} - {Detail}`, with the area named in full, such as `Barter Deals`
- H2 sections, ALL-CAPS H4 audience headings with a divider, Title Case facet labels and section headings, and `- []` checkboxes
- `references/briefing-mode.md`, `assets/design-briefing-template.md`, three worked examples under `assets/examples/briefing/`, and the `AGENTS.md` title, file naming and command rules
- The `BRIEFING` intent in the router contract, the route oracle, the differential gate, the route fixtures, the hub leaf map and its gate
- The `$briefing` command, with no shortcut because `$b` is Bug
- The Project kernel, five new knowledge mirrors, the edited mirrors and the Sync Loop declaration
- A `**Why**` exemption in both validators, scoped to a document whose title starts `Briefing - `

### Out of Scope
- The shared Human Voice card and its copies, because the gate never flags the briefing's own labels
- A semantic topic for briefings, because a briefing is asked for by its noun or by `$briefing`
- Task Mode and Task Templates beyond removing the briefing
- The user's own briefing files, which only a scratch copy converted

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `sk-product-owner/references/briefing-mode.md`, `assets/design-briefing-template.md`, `assets/examples/briefing/` | Create | The mode reference, the scaffold and three examples |
| `sk-product-owner/assets/task-templates.md`, `references/task-mode.md`, `assets/examples/task/` | Modify and Delete | The briefing leaves Task Mode, and the three examples move out |
| `sk-product-owner/references/router-contract.md`, `benchmark/router/`, `benchmark/gates/check_leaf_map_parity.py`, `ROUTER.md`, `leaf-manifest.json` | Modify | The `BRIEFING` intent, its frames, fixtures and leaf lane |
| `AGENTS.md`, `sk-product-owner/SKILL.md`, `README.md`, `sk-product-owner/README.md`, Interactive Mode and its templates, Quality Scoring | Modify | Command registry, token rules, loading order, intake question, kind lists and versions |
| `benchmark/format/` validator, three fixtures, runner and README | Modify and Create | The Why exemption |
| `../z — Claude Project Sync Loop/` validator, three fixtures, runner, `systems.py`, README | Modify and Create | The shared copy, the new mirror pairs and the resynced statements |
| `claude project/` kernel, knowledge files, README and `SYNC.md` | Modify and Create | Hand-written mirrors and the parity note |
| `leaf-manifest.json`, `sk-product-owner/changelog/v1.2.23.0.md`, `changelog/v1.0.39.0.md` | Modify and Create | Regenerated manifest and the release notes |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-001 | The three examples and the scaffold pass the gate | `validate-output-format.cjs --system product-owner <file>` exits 0 on each |
| REQ-002 | A briefing's Why bullets pass and nothing wider does | `briefing-why-silent.md` exits 0, the two violation fixtures exit 1 |
| REQ-003 | Both validators agree | `reference-parity.cjs` prints `shared core is byte-identical to the reference implementation` |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-004 | The Project carries the same shape | Residency and parity pass in a scratch clone with a throwaway commit |
| REQ-005 | The gates hold against the baseline | `run_gates.sh` fails no gate beyond the baseline's identifier scan and the one peer-file gap named in the summary |
| REQ-006 | The real briefing passes in the new layout | A scratch copy converted to the layout exits 0 |
| REQ-007 | A briefing request routes to its own intent | `route_contract.py` routes `$briefing` and `write a design briefing` to `BRIEFING`, and `create a task to write a briefing` stays `TASK` |
| REQ-008 | The router copies agree | `benchmark/router/run_fixtures.sh` passes, with the kernel's Router Code equal to the contract's with its comments removed |
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: A briefing written from the template passes the gate with a Why facet
- **SC-002**: A plain bullet under any other facet, or a Why facet in another document, still fails
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | The shared validator and declaration live in the parent repository | Two repositories change together | Run parity and residency in a scratch clone of both |
| Risk | A briefing paired with a FigJam board has no defined link group in Flow Mode Section 8 | Low | The router carries the pairing, and the link placement is reported for the owner of `sk-create-figjam` |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:questions -->
## 7. OPEN QUESTIONS

- Should Flow Mode Section 8 name a link group for a briefing, as it does for a Task, Bug, Story, Epic and Doc?
<!-- /ANCHOR:questions -->

---
