---
title: "Feature Specification: Requirements bloat in Story Mode"
description: "The owner reports that Requirements carries unneeded bloat, pointing at the Initial Instagram Sheet group in the ReAuth story where four of five bullets describe the screen. The carry-through rule at story-mode.md:79 orders every source line into the draft while the hard-constraint rule at :116 excludes only a Checklist and a user outcome. The review measures the bloat at 28 of 221 bullets, gives a build-can-fail test, sixteen proposed edits and one narrow gate check."
trigger_phrases:
  - "requirements bloat"
  - "story requirements description"
  - "requirements bullet a build can fail"
  - "instagram reauth sheet requirements"
  - "story mode requirements rule"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Requirements bloat in Story Mode

<!-- SPECKIT_LEVEL: 1 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 1 |
| **Priority** | Not recorded in this folder. |
| **Status** | Complete |
| **Created** | Not recorded in this folder. |
| **Branch** | Not recorded in this folder. |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Four of the five bullets under `Initial Instagram Sheet` in `Highlights - Onboarding - Instagram ReAuth.md` describe the screen rather than state a constraint. The source gives the sheet one prose line, `Compeltely new sheet that explains the situation`, and `Screenshots/2 No Instagram ReAuth/` holds the screen itself. Two rules then collide. The carry-through rule at `story-mode.md:79` orders every source line into the draft and names an omitted line a defect, while the hard-constraint rule at `story-mode.md:116` excludes exactly two shapes, a `**Checklist**` and a user outcome. Narrative UI description is neither, so the instruction with a consequence attached beat the adjective with no exclusion behind it. No check anywhere reconciles in the other direction, from a Requirements bullet back to the source, so a bullet that traces to no supplied value is not a finding in any gate.

### Purpose
Name the rule conflict, measure how widespread the bloat is, give a one-sentence test a model can apply without judgement, propose the exact edits file by file, and answer honestly whether a format gate can check this mechanically.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- The rule sources: `story-template.md`, `story-mode.md`, `SKILL.md`, `quality-scoring.md` and the Claude Project `Custom Instructions.md`
- The corpus: sixteen exported stories, 221 Requirements bullets across the fifteen that carry the section, plus 93 bullets in the five worked examples, the exports and the knowledge mirrors
- The format gate and its fixtures as a candidate home for a mechanical check
- `findings.md`, the one deliverable, written inside this folder

### Out of Scope
- Any edit to a skill or Claude Project file, since the brief demanded a review and proposals only
- Running the sync compiler, which the brief forbade
- The three derived knowledge files, which a resync would carry
- Commits, which the brief forbade

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `sk-product-owner/assets/story-template.md` | Proposed Modify | The build-can-fail rule, the screenshot copy rule and the no-padding rule, edits A to C |
| `sk-product-owner/references/story-mode.md` | Proposed Modify | House grammar, verbatim copy, grouping, accounting, intake, validation and checklist entries, edits D to M |
| `sk-product-owner/SKILL.md` | Proposed Modify | ALWAYS rule 9, one line for one line, so the file stays 405 lines, edit N |
| `claude project/Custom Instructions.md` | Proposed Modify | Rule 10 takes the same insertion, edit O |
| `sk-product-owner/references/quality-scoring.md` | Proposed Modify | Relevance scored per bullet rather than per section, edit P |
| `claude project/knowledge/Product Owner - Assets - Story Template - v0.100.md` and two peers | Proposed Resync | Derived copies carrying edits A to C, D to M and P |
| `benchmark/format/validate-output-format.cjs`, `benchmark/format/run_fixtures.sh` and two new fixtures | Proposed Add | The narration check and its fixture pair, measured at zero false positives |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-001 | Each bloated bullet is traced to the rule it obeyed | All four bullets name a rule from `story-mode.md` with the sentence that permitted it |
| REQ-002 | The scale of the bloat is measured, not estimated | Per-file classification of all 221 bullets, with description and rider counts and five worst examples quoted |
| REQ-003 | One test separates a constraint from a description | The rule keeps the five value bullets, strikes the four bloated bullets and states where the borderline case lands |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-004 | Every proposed edit quotes its current text | Each edit names a file, a line, the current sentence and the replacement |
| REQ-005 | The gate answer is honest | The narrow check ships with measured precision and the general description check is named as not mechanically separable |
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: `findings.md` answers all seven items the brief lists, each in its own section
- **SC-002**: The narration check was built and run before it was proposed, with its precision and recall stated
- **SC-003**: The format gate and its fixtures pass at baseline, recorded in `run.log`
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | The brief scopes a read-only review | No file outside this folder changes, so the bloat reproduces until a follow-up pass | Apply the proposed edits in that pass |
| Dependency | The sync compiler is forbidden | The three derived knowledge files stay stale | Resync them in the follow-up pass |
| Risk | A broad description check misfires | Two candidates measured 0.15 and 0.38 precision on the corpus | Only the narrow narration check is proposed |
| Risk | The gate roster stays narrower than the proposed rule | `SKILL.md:388` and `Custom Instructions.md:214` still list no screen description | A second edit to each file, awaiting authorization |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:questions -->
## 7. OPEN QUESTIONS

- Whether a second edit to `SKILL.md` and `Custom Instructions.md` is authorized so their gate rosters match the new rule
<!-- /ANCHOR:questions -->

---
