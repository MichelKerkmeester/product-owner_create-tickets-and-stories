---
title: "Feature Specification: Fresh review fixes"
description: "Fixes the verified findings of a fresh Fable review of the whole system, redacts private identifiers from the public repositories and repairs five upstream items in Skilled."
trigger_phrases:
  - "fresh review fixes"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.4 -->
# Feature Specification: Fresh review fixes

<!-- SPECKIT_LEVEL: 1 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 1 |
| **Priority** | P1 |
| **Status** | Complete |
| **Created** | 2026-11-11 |
| **Branch** | `main` |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
A fresh Fable 5.2 review at medium effort read the whole system with no prior context. It found Doc scaffolds that teach an em dash the gate blocks, a gate runner that never runs the source format lint, a Doc spacer rule its own examples break, a feedback ticket path that holds a slash, and private identifiers in tracked files of this public repository. Michel chose through the question tool to fix all four finding groups, to keep spacers in Doc exports, to redact the identifiers and rewrite history, and to fix the five upstream items of packet 031 in Skilled.

### Purpose
Each chosen finding is fixed at its source, the gates catch the next slip, and no private identifier stays in the public repositories.
<!-- /ANCHOR:problem -->

<!-- ANCHOR:measured-behavior -->
### Measured Behavior
```text
doc-templates.md lines 323, 571 and 646: scaffold line with a prose em dash
run_gates.sh: 0 rows run validate-output-format.cjs on the source files
doc-mode.md:97 bans spacer headings in a file export, the Doc examples carry 42
task-mode.md:254: export path holds the kind UI/UX, which contains a slash
vendor-sync.py on a truncated vendor.json: exit 1 with a traceback, the docstring says 2
tracked files: workspace id in 7, work email in 2, Figma team ids in 6, home path in 1,885
```
<!-- /ANCHOR:measured-behavior -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Doc scaffolds, the Doc spacer rule, the feedback ticket path and example, and the stale counts, in the skill and by hand in the Claude Project mirror
- `run_gates.sh` gains the source format lint, the example lint reads scaffolds, and an identifier scan joins the gates
- `vendor-sync.py` exits 2 on a malformed manifest
- The six simplification proposals of the review
- Redaction of the workspace id, work email, Figma team ids and home path, in place and in git history
- The five upstream items of packet 031, fixed in Skilled and pulled

### Out of Scope
- Review findings F6, F7, F9 and F10, which were not chosen
- A live model benchmark of the simplified instruction files
- The private Barter repository's history

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `sk-product-owner/`, `AGENTS.md`, `SKILL.md`, `ROUTER.md`, `README.md` | Modify | Scaffolds, rules, paths, counts, simplifications |
| `claude project/` | Modify | Hand-written mirror of the rule changes |
| `benchmark/gates/`, `benchmark/grader/`, `scripts/` | Modify | Lint gate, scaffold lint, identifier scan, exit code |
| `benchmark/reports/`, `specs/` | Modify | Redaction |
| Skilled `sk-doc` checkers, the alignment command, `mcp-code-mode` playbook, `mcp-click-up` docs | Modify | Upstream items |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-001 | A Doc copied from any scaffold passes the artifact gate | Each scaffold block passes `validate-output-format.cjs` as a target |
| REQ-002 | The gate runner runs the source format lint | A banned word in a skill file turns `run_gates.sh` red |
| REQ-003 | No private identifier stays in tracked files | The identifier scan gate passes on the tree |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-004 | The Doc spacer rule and its examples agree | The rule keeps spacers in the export, in the skill and the mirror |
| REQ-005 | A feedback ticket path holds no slash from its kind | The path uses `logic` and `ui-ux` slugs |
| REQ-006 | A malformed manifest is a setup error | `vendor-sync.py` exits 2 and a test proves it |
| REQ-007 | The five upstream items are fixed in Skilled | Each has a check that fails before and passes after |
| REQ-008 | No gate regresses | `run_gates.sh`, parity and residency pass |
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: `run_gates.sh` reports every gate passing, with the new lint and scan gates in the list
- **SC-002**: `git grep` finds none of the redacted values in either public repository
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Where | Mitigation |
|------|------|--------|--------|------------|
| Risk | A history rewrite changes every commit hash | High | Both public repositories, `vendor.json`, the Sync Loop | Remap pinned hashes, confirm with Michel right before the force push |
| Risk | A simplified instruction file changes agent output | Medium | `AGENTS.md`, `SKILL.md`, `ROUTER.md` | Router fixtures and gates run. A live benchmark stays open |
| Risk | A peer session pushes to Skilled during the rewrite | High | Skilled | Rewrite only after Michel confirms no peer session is active |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:questions -->
## 7. OPEN QUESTIONS

- Should a live model benchmark run on the simplified instruction files before the next release?
<!-- /ANCHOR:questions -->

---
