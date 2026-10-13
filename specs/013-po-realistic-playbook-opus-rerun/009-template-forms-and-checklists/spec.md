---
title: "Feature Specification: Phase 9, template forms and checklists"
description: "The Product Owner templates taught heading levels and checkbox forms the operator no longer writes, and the rules banned the Story requirement checklists the operator now uses. This phase moves every template, rule, gate, mirror, example and export to the operator's ClickUp forms."
trigger_phrases:
  - "template forms"
  - "checklist bracket form"
  - "story requirements checklist"
  - "about heading h2"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core + level2-verify | v2.2 -->
# Feature Specification: Phase 9, template forms and checklists

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P1 |
| **Status** | Complete |
| **Created** | 2026-09-26 |
| **Branch** | `main` |
| **Parent Spec** | ../spec.md |
| **Phase** | 9 of 9 |
| **Predecessor** | 008-cut-exports-and-word-budget |
| **Successor** | None |
| **Handoff Criteria** | Every template, rule, mirror, example and export in the new forms, both gates enforcing them, and the commits made |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 9** of the realistic Product Owner playbook packet.

**Scope Boundary**: The Product Owner skill sources, the Claude Project kernel and knowledge mirrors, the playbook, both format validators with their fixtures, the shared residency declaration and the 78 exports in `export/benchmark/`.

**Dependencies**:
- Phase 008 pushed, Product Owner `bb9210f` and Barter `0b08add1`

**Deliverables**:
- The five template changes the operator asked for, in every Product Owner surface
- Both validators reading `[]` and blocking the retired forms
- Skill 0.17.0, kernel v0.20.0, playbook 2.5.0.0, a changelog and a `SYNC.md` note
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
The operator's newest hand-written ClickUp exports use `## About`, `#### Problem` and `#### Solution`, a bold `**Expected outcomes**` label inside Solution and checkbox items under each Story requirement group. The templates taught H3 openings, an H4 Expected outcomes heading and plain requirement bullets, and 15 or more rules banned a checkbox in Requirements. The format gate blocked the operator's own shape, and most of its checkbox rules could not see a `[]` box at all.

### Purpose
Every Product Owner surface writes and checks the operator's forms, and nothing a reader acts on changes in the exports.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Story and Epic openings at H4, with Expected outcomes and User Story as bold labels inside Solution
- `## About` at H2 in the Task and Bug templates, their other sections staying at H3
- Story requirements as `- []` constraint items, still hard constraints and never build steps
- Every artifact checkbox written `[]`, in templates, examples, rules, kernel, mirrors and exports
- Both validators, their fixtures, the residency declaration and the playbook scenarios

### Out of Scope
- A playbook rerun or a live ClickUp render test of `[]`
- Heading-level checks in the gate, which checks no heading level today
- The shared `z — Knowledge` cards, which state none of these forms
- Other systems' checklists and Deal Templates' `## ABOUT`

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `sk-product-owner/assets/*.md`, `references/*.md`, `SKILL.md`, `AGENTS.md` | Modify | The new forms and rules, each version bumped |
| `claude project/Custom Instructions.md`, `claude project/knowledge/*` | Modify, Rename | Kernel v0.20.0, 11 mirrors renamed, 17 example mirrors converted |
| `sk-product-owner/assets/examples/**` | Modify | 17 examples converted |
| `export/benchmark/**` | Modify | 78 exports checked, the 75 holding an old form converted |
| `z — Claude Project Sync Loop/validate-output-format.cjs`, `systems.cjs`, `systems.py`, `run_fixtures.sh`, `fixtures/` | Modify, Create | Shared gate, checkbox key, resynced statements, fixtures |
| `benchmark/format/*` | Modify, Create | Product Owner's validator copy, runner and fixtures, kept identical |
| `sk-product-owner/manual-testing-playbook/**` | Modify | 42 scenarios and the root at 2.5.0.0 |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | The five forms hold in every template, example and export: H4 Problem, Solution and Goal, the bold Expected outcomes label, `## About`, `- []` Story requirement items and `[]` checkboxes |
| REQ-002 | The conversion changes no word: each changed line differs from its snapshot only by an allowed transform |
| REQ-003 | Both validators accept the new forms, block the retired ones, and give identical output |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-004 | The kernel, mirrors, residency declaration and playbook agree with the skill, with parity, residency and the playbook validator passing |
| REQ-005 | Every version surface, the changelog and a `SYNC.md` note record the change, with the kernel review pending |
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: No old form survives in a template, example or export, and the gate blocks each retired form on the old snapshot
- **SC-002**: The format gate, fixtures, reference parity, parity, residency and the playbook validator pass on the committed state
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Risk | ClickUp may not render `- []` as a checkbox | High | The operator chose the form knowing this; the run README names the check |
| Risk | A mirror keeps an old form that parity cannot see, since parity folds brackets and hashes | Med | A scratch diff of every mirror body against its source |
| Risk | A sibling system's deliverable meets the inverted Requirements rule | Low | The rule fires only on `## Requirements`, and all four fixture suites pass |
<!-- /ANCHOR:risks -->

---


---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Performance
- **NFR-P01**: A reader sees one heading level per opening group, with no heading nested inside an H4

### Security
- **NFR-S01**: No secret or credential enters any file

### Reliability
- **NFR-R01**: The gate reads both checkbox forms, so no rule goes quiet on either
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Data Boundaries
- A refinement of an old-form source keeps its markers unless normalization was asked for
- The Which-means-that lines under a Rule block sit inside Requirements, so they become `- []` items too

### Error Scenarios
- A changed line that is not an allowed transform fails the verify script
- A kernel statement reworded without its declaration fails residency

### State Transitions
- A mirror renamed for a version bump keeps every live reference through the repointer
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 20/25 | About 200 files in two repositories |
| Risk | 12/25 | Gate behavior shared by four systems, an unverified ClickUp form |
| Research | 6/20 | Enforcement surfaces mapped before editing |
| **Total** | **38/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- None. On 2026-09-26 the operator chose the Epic too, all 78 exports converted, `[]` in every artifact checklist, and Story requirements kept as constraints
<!-- /ANCHOR:questions -->

---
