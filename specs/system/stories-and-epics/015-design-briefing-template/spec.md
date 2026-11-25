---
title: "Feature Specification: Design briefing template"
description: "Product Owner gains a design briefing task shape for the Product Design team, with a template, three worked examples, Task Mode rules, Project mirrors and a format gate that accepts plain bullets under a Why facet in a briefing."
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
Michel writes briefings for the Product Design team by hand, such as `Briefing - Partner & Creator - Barter Deals - Desired Collab Amount & Reach Pause`. Product Owner had no shape for them. A briefing also carries a `**Why**` facet of plain bullets inside Requirements, which the format gate reports as a plain bullet outside a User flow.

### Purpose
Product Owner writes a design briefing from a template, in the layout Michel approved, and the gate accepts the briefing's one plain-bullet facet and nothing wider.
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
- H2 sections, ALL-CAPS H3 audience headings with a divider, Title Case facet labels and section headings, and `- []` checkboxes
- Task Templates Section 7, three worked examples, a Task Mode entry with checklist lines, and the `AGENTS.md` title and file naming rules
- The Project kernel, three knowledge mirrors, two edited mirrors and the Sync Loop declaration
- A `**Why**` exemption in both validators, scoped to a document whose title starts `Briefing - `

### Out of Scope
- The shared Human Voice card and its copies, because the gate never flags the briefing's own labels
- The router tables and gold rows, because the leaf map parity and hub gates depend on them
- The user's own briefing files, which only a scratch copy converted

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `sk-product-owner/assets/task-templates.md`, `references/task-mode.md`, `assets/examples/task/` | Modify and Create | Section 7, the Task Mode entry and three examples |
| `AGENTS.md`, `sk-product-owner/SKILL.md`, `README.md`, `sk-product-owner/README.md` | Modify | Title rule, file naming, shape lists and versions |
| `benchmark/format/` validator, three fixtures, runner and README | Modify and Create | The Why exemption |
| `../z — Claude Project Sync Loop/` validator, three fixtures, runner, `systems.py`, README | Modify and Create | The shared copy, the new mirror pairs and the resynced statements |
| `claude project/` kernel, knowledge files, README and `SYNC.md` | Modify and Create | Hand-written mirrors and the parity note |
| `leaf-manifest.json`, `sk-product-owner/changelog/v1.2.22.0.md` | Modify and Create | Regenerated manifest and the release note |
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
| Risk | A bare briefing request routes to the interactive fallback, not Task | Medium | Reported, with the router left alone |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:questions -->
## 7. OPEN QUESTIONS

- Should the router tables gain a briefing signal and a gold row, so a bare briefing request reaches Task Mode?
<!-- /ANCHOR:questions -->

---
