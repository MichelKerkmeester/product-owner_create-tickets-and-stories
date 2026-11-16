---
title: "Feature Specification: Story criteria and checklist layout"
description: "The house Story layout changes in four places: no divider under a Mark-as-done line, a Checklist label over each requirement section's checks, user flows split into bullets and screenshots in columns. New Stories and Epics now default to that layout."
trigger_phrases:
  - "story criteria and checklist layout"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.4 -->
# Feature Specification: Story criteria and checklist layout

<!-- SPECKIT_LEVEL: 1 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 1 |
| **Priority** | P1 |
| **Status** | Complete |
| **Created** | 2026-11-16 |
| **Branch** | `main` |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Michel chose a new house layout for Stories that differs from the current rules in four places. Story Mode puts a divider under every Mark-as-done line, bans a `**Checklist**` label inside Requirements, writes a section's user flow as one line and says a Story never carries an image. The new layout drops the lower divider, labels each section's checks, splits the user flow into one bullet per step and sets screenshots side by side in ClickUp columns. The format gate enforces the old rules, so a Story written in the new layout fails it.

### Purpose
New Stories and Epics use the new layout by default, in the skill, its Claude Project package and both copies of the format gate.
<!-- /ANCHOR:problem -->

<!-- ANCHOR:measured-behavior -->
### Measured Behavior
```text
$ node benchmark/format/validate-output-format.cjs <a Story in the new layout>
reports a missing divider below each of the six Mark-as-done lines before the change
```
<!-- /ANCHOR:measured-behavior -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Acceptance criteria: no divider under a Mark-as-done line, one empty line before the next criterion, and the last criterion ends on its Mark-as-done line with no divider and no spacer after it
- A `**Checklist**` label with a `* * *` divider under it above the checks of every requirement section
- `**User flow:**` alone on its line, then one `*   ` bullet per step
- Screenshots of a section set side by side in ClickUp columns on a push, one image left and two right for three
- Both format validators, their fixtures and the source contract pins, kept output-identical
- The Claude Project mirrors, the Sync Loop declaration and a patch release

### Out of Scope
- The vendored `mcp-click-up` page writer, which pastes over the whole task editor. The fix goes upstream through `scripts/vendor-sync.py push`
- Old exports and delivered Stories, which are refined only on request

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `AGENTS.md`, `sk-product-owner/SKILL.md` | Modify | Prohibited bullet and NEVER rule on Mark-as-done dividers, task columns note |
| `sk-product-owner/references/story-mode.md`, `doc-mode.md` | Modify | The four layout rules |
| `sk-product-owner/assets/story-template.md`, `epic-template.md`, `assets/examples/story/` | Modify | Templates and worked examples in the new layout |
| `sk-product-owner/manual-testing-playbook/` story scenarios | Modify | Expected results that state the rule |
| `benchmark/format/` validator, fixtures, runner, README and `benchmark/gates/rule_parity.py` | Modify | Gate enforces the new layout |
| `../z — Claude Project Sync Loop/` validator, fixtures, runner, `systems.py`, `systems.cjs` | Modify | Shared gate and declaration, in the parent repository |
| `claude project/` kernel and knowledge files, `SYNC.md` | Modify | Hand-written mirrors and the parity note |
| Version files and changelogs | Modify and Create | Hub v1.0.36.0, `sk-product-owner` v1.2.20.0 |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-001 | The gate accepts the new layout | A Story written in the new layout passes `validate-output-format.cjs` in artifact mode |
| REQ-002 | The gate refuses a divider under a Mark-as-done line | The flipped `markasdone-divider-violation.md` fixture reports it and exits 1 |
| REQ-003 | Both validators agree | `reference-parity.cjs` prints `shared core is byte-identical to the reference implementation` |
| REQ-004 | No source still states the old rules | `rg 'sits between two dividers'` finds nothing in sources or mirrors |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-005 | The mirrors carry the same rules | `bash benchmark/parity/run_residency.sh` prints `PASSED` |
| REQ-006 | The gates hold against the baseline | `run_gates.sh` fails no gate beyond the vendor sync gate that failed before the change |
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: A Story written from the template passes the gate with no divider under any Mark-as-done line
- **SC-002**: Gate, fixture, parity and residency results match the baseline apart from the intended fixture changes
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | The shared validator and declaration live in the parent repository | Two repositories change together | Run the parity check and residency from the final state of both |
| Risk | A ClickUp task with columns rewritten through `markdown_description` loses its columns | High | SKILL.md forbids that write on a task with columns |
| Assumption | The new layout does not show what follows the last criterion when `## Delivery` is present | Low | The `##   ` spacer still opens Delivery, with no divider above it |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:questions -->
## 7. OPEN QUESTIONS

- None. Michel confirmed the last criterion and the Checklist divider.
<!-- /ANCHOR:questions -->

---
