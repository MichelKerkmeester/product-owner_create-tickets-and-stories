---
title: "Feature Specification: Phase 7, drop clarification exports"
description: "The published benchmark exports hold 20 clarification files, which are questions asked before drafting rather than deliverables. This phase removes them and stops the collector from writing them back."
trigger_phrases:
  - "drop clarification exports"
  - "clarification files export benchmark"
  - "collector skips clarifications"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Phase 7, drop clarification exports

<!-- SPECKIT_LEVEL: 1 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 1 |
| **Priority** | P1 |
| **Status** | Complete |
| **Created** | 2026-09-26 |
| **Branch** | `main` |
| **Parent Spec** | ../spec.md |
| **Phase** | 7 of 7 |
| **Predecessor** | 006-concise-writing |
| **Successor** | None |
| **Handoff Criteria** | `export/benchmark/` holds no clarification file, and a collector run cannot write one back |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 7** of the realistic Product Owner playbook packet.

**Scope Boundary**: The published exports, the collector, its selftest and the run README. Grading evidence is untouched.

**Dependencies**:
- Phase 006 closed and pushed, Product Owner `1fc3657` and Barter `e324ecdf`

**Deliverables**:
- 20 clarification files removed from `export/benchmark/`
- `run/collect_exports.py` skipping any `*-clarification.md`, with a selftest check that fails without it
- The run README's counts, collection table and next steps brought up to date
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
`export/benchmark/` is where a reader goes to see the run's tickets, and 20 of its 98 files are clarifications: the one question a scenario asked before drafting. The operator does not want them published. The collector would write them back on its next run, since it copies every file a scenario saved.

### Purpose
The published exports hold deliverables only, and the collector keeps it that way.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Remove the 10 skill and 10 Project `*-clarification.md` files from `export/benchmark/`
- Make the collector skip a clarification on both sides and print a skip line for it
- Update the README: the file counts, the Project extraction table, the collector hash and the stale kernel review line
- Delete the 46 git-ignored clarification copies under the run folders' `exports/`, added by the operator later on 2026-09-26

### Out of Scope
- `replies/`, transcripts, `turn-<n>.md`, `grading-notes.md` and `results.csv`, because the verdicts cite them
- The skill and Project rules that save a clarification to `export/`, because the operator asked about the benchmark only

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `AI Systems/Product Owner/export/benchmark/**/*-clarification.md` | Delete | The 20 clarification files |
| `AI Systems/Product Owner/benchmark/reports/2026-09-25--manual-testing-playbook--claude-opus-5-5-medium/run/collect_exports.py` | Modify | Skip clarifications |
| `.../run/selftest.py` | Modify | The collector check expects no clarification and a skip line |
| `.../README.md` | Modify | Counts, table, hashes, next steps |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-001 | No clarification file is published | `find export/benchmark -name '*-clarification.md'` prints nothing, and 78 files remain |
| REQ-002 | A collector run cannot restore one | A dry run over the real run folder lists no clarification write and prints 20 skip lines |
| REQ-003 | The selftest proves the skip | The collector check fails against the previous collector and passes against the new one |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-004 | The README states the current state | Counts read 78, the Project table lists 47 files, the hashes match the files, and the kernel review line matches `SYNC.md` |
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: `export/benchmark/` holds 78 files: 31 skill and 47 Project
- **SC-002**: The selftest passes 7 of 7, and the format gate, parity and residency stay green on the commit
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Risk | A deliverable whose name ends in `-clarification` is skipped | Low | The Product Owner naming rule reserves that suffix for clarifications, and the skip line names every file it drops |
| Dependency | Git history keeps the removed files | Low | Graded originals at Product Owner `e9edb95` and Barter `7652158c`, edited copies at `1fc3657` and `e324ecdf` |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:questions -->
## 7. OPEN QUESTIONS

- None. The operator chose the published files only on 2026-09-26
<!-- /ANCHOR:questions -->

---
