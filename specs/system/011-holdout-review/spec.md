---
title: "Feature Specification: Held-out review of Creator - Deals - Saved Deals Shelf"
description: "A source the Product Owner skill had never seen was written by hand and a fresh Sonnet at high effort wrote a Story from it. This packet reviews the artifact and the rules that produced it, reports which traps held, and ranks the changes it recommends from P0 to P3."
trigger_phrases:
  - "held-out review saved deals shelf"
  - "product owner requirements paraphrase"
  - "story drafts export path retired"
  - "holdout fixture benchmark"
  - "format gate prose semicolon"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Held-out review of Creator - Deals - Saved Deals Shelf

<!-- SPECKIT_LEVEL: 1 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 1 |
| **Priority** | P1 |
| **Status** | Complete |
| **Created** | 2026-09-09 |
| **Branch** | Not recorded in this folder. |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
The Requirements rule had been rewritten twice, in `ba2bec3` and `095479a`, but it had never been tested against a source the skill had not already seen. The brief states the case: "A source the skill had never seen was written by hand, and a fresh Sonnet at high effort wrote a Story from it." The findings state the two facts that frame the review. The artifact is the only one of seventeen that fails the format gate. The ReAuth story did not prove the rule generalises, because its Initial Instagram Sheet group is byte-identical to the four-line worked example the rules print.

### Purpose
Judge the artifact and the rules that produced it, and say what should change, ranked P0 to P3 with file, line, current text and replacement.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- The artifact, judged against the rules in `sk-product-owner/references/story-mode.md` sections 1, 3, 4 and 9 and `sk-product-owner/assets/story-template.md`
- The eight trap families the source was written to test, one per rule that changed
- The phrase list proposed in `AI Systems/Product Owner/specs/010-requirements-bloat/findings.md` section 6.2, measured across 328 Requirements bullets
- The output path and the symlink coupling that put the artifact beside its own source
- The rules that are redundant, contradictory or unreachable after the four Requirements changes
- Whether the source is worth keeping as a permanent held-out fixture and where it should live
- The ranked change list, P0 to P3

### Out of Scope
- Any edit outside this folder, any sync compiler run and any commit
- The repairs themselves, which the review ranks but does not apply

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `brief.md` | Created | The review brief, with the reading list, the trap families and the six advisory questions |
| `run.sh` | Created | The CLI runner that dispatched the reviewer and captured `run.log` |
| `run.log` | Created | The printed report plus the closing `exit=0 seconds=842` line |
| `findings.md` | Created | The report, with the trap verdicts, the measurements and the ranked changes |

The review changed nothing outside this folder, so the repairs it recommends are proposals. Section 8 of `findings.md` files them against `sk-product-owner/references/story-mode.md`, `sk-product-owner/assets/story-template.md`, `benchmark/format/validate-output-format.cjs` and the artifact at `export/Story Drafts/Creator - Deals - Saved Deals Shelf/Creator - Deals - Saved Deals Shelf.md`.
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-001 | Read every item on the brief's reading list before advising | The report cites the source, the artifact, `story-mode.md`, `story-template.md`, `ba2bec3`, `095479a` and `specs/010-requirements-bloat/findings.md` |
| REQ-002 | Give one verdict per trap family | Section 1 of the report carries a verdict for each of the eight trap families and names the one that failed |
| REQ-003 | Rank every recommended change P0 to P3 with file, line, current text and replacement | Section 8 of the report carries the ranked list |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-004 | Answer the six advisory questions in the brief | Each question has its own headed answer in the report |
| REQ-005 | Write the report to `findings.md` and also print it | `findings.md` exists and `run.log` holds the printed copy, closing on `exit=0 seconds=842` |
| REQ-006 | Touch nothing outside this folder, run no sync compiler, commit nothing | The run log records a `git status` check against `AI Systems/Product Owner/` with no change outside the folder |
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: `findings.md` holds the report and `run.log` holds the printed copy
- **SC-002**: All eight trap families carry a verdict, seven held and one failed
- **SC-003**: The phrase list is measured on a 328-bullet corpus and named for what it catches, a copy-paraphrase check rather than a description check
- **SC-004**: The report ends on a ranked change list and a recommendation on the fixture, and no file outside the folder changed
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | The held-out source and the artifact are one file | A rerun that reads the export folder sees the answer | Move the source out of the export tree into a tracked holdout folder |
| Risk | The phrase list is a copy-paraphrase check with low recall | A layout inventory passes it | Name the check for what it catches, in the code comment and in the prose rule |
| Risk | The held-out source is untracked | `.gitignore:68` masks `**/export/*`, so the only source the skill has never seen can be lost | Keep it under `benchmark/holdout/`, which `git ls-files` shows is tracked |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:questions -->
## 7. OPEN QUESTIONS

- None
<!-- /ANCHOR:questions -->

---
