---
title: "Feature Specification: Story Drafts two-pass rewrite"
description: "Sixteen Story Drafts under AI Systems/Product Owner/export/Story Drafts were rewritten in place as full Stories with DeepSeek V4 Flash at max thinking on llmgateway, routed through /agent-router product owner $story with three lanes running in parallel because each rewrite takes several minutes and the folders are independent. The first pass exported 16 of 16 and left 15 of 16 gate-clean, so three stories whose acceptance criteria described UI mechanics went through a second pass with one extra sentence of steer; the second pass, after the hardened Story shape landed, passed the gate 16 of 16 with no hand fixes. A separate one-request benchmark ran the same request against three models."
trigger_phrases:
  - "story drafts rewrite"
  - "deepseek v4 flash story rewrite"
  - "three-lane draft rewrite"
  - "per-surface acceptance criteria ceiling"
  - "story format gate two-pass"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Story Drafts two-pass rewrite

<!-- SPECKIT_LEVEL: 1 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 1 |
| **Priority** | Not recorded in this folder. |
| **Status** | Complete |
| **Created** | 2026-09-08 |
| **Branch** | Not recorded in this folder. |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Sixteen Story Drafts under `AI Systems/Product Owner/export/Story Drafts/` had to be rewritten in place as full Stories in the current house format, each one from its own draft and the `context.md` beside it, with no numbered export and no reference to the screenshots in that folder, because those get embedded in ClickUp later. Each rewrite takes several minutes, and the three lanes exist because the folders are independent. The 16 files in `results.tsv` were written before the Delivery-opt-in and hard-value rules landed, so three of them had UI mechanics written as acceptance criteria instead of requirements or prose.

### Purpose
Every one of the sixteen drafts reads as a finished Story in the hardened house shape: criteria limited to the few outcomes a user relies on per surface, fixed mechanics carried into Requirements as hard constraints, and no design values leaking into acceptance criteria.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Rewriting all sixteen Story Drafts in place as full Stories, one router call per draft, three lanes at once (`run.sh`, `results.tsv`)
- A second pass over the three stories whose first pass wrote UI mechanics as acceptance criteria (`rerun3.sh`, `rerun3.tsv`)
- A separate, one-request benchmark of the hardened Story shape across three models (`story-benchmark-results.tsv`)
- `README.md`, the reading guide that covers what the tsv files record and how to read them

### Out of Scope
- Numbered exports; both prompts overwrite the exact draft path instead
- References to the screenshots in each draft folder, which get embedded in ClickUp later
- The drafts themselves and the pre-rewrite backup, which live outside this folder
- The per-surface acceptance-criteria ceiling, which stays with `Specs/030-system-hardening/spec.md` section 6

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `AI Systems/Product Owner/export/Story Drafts/*/*.md` | Modified | All sixteen drafts overwritten in place as full Stories |
| `run.sh` | Added | First-pass script: reads `files.txt`, splits it three ways round-robin |
| `results.tsv` | Added | First-pass lane, seconds, exit and path for every draft |
| `rerun3.sh` | Added | Second-pass script for the three flagged stories |
| `rerun3.tsv` | Added | Second-pass seconds, exit and path for those three |
| `story-benchmark-results.tsv` | Added | Separate one-request benchmark across three models |
| `README.md` | Added | Reading guide, last updated 2026-10-13 |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-001 | Every draft is rewritten in place as a full Story from its own draft and the `context.md` beside it | `results.tsv` holds 16 rows, one per draft, every exit 0 |
| REQ-002 | No rewrite writes a numbered export or references the folder's screenshots | Both prompts ask for an in-place overwrite and bar screenshot references |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-003 | Criteria stay to the few outcomes a user relies on per surface, and any fixed mechanic moves into Requirements as a hard constraint | Second-pass counts drop to 8, 5 and 6 for the three flagged stories |
| REQ-004 | The hardened Story shape holds when the same drafts are rewritten again from the original source | The second pass, run from the original drafts and context files only, passes the gate 16 of 16 with no hand fixes |
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: First pass exports 16 of 16 in place, every row exit 0, from 187.7s to 648.7s
- **SC-002**: Second pass passes the gate 16 of 16 with no hand fixes
- **SC-003**: No Delivery sections written unasked, no image or screenshot references, no design values (pixel sizes, heading levels, button order) in acceptance criteria, no source hedges copied verbatim into Story prose
- **SC-004**: All five context files' hard values carry into per-screen Requirements groups
- **SC-005**: The benchmark records two valid runs and one invalid run, with the earlier discarded attempt marked as not a comparison point
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | DeepSeek V4 Flash at max thinking on the llmgateway provider, through the agent router | Every rewrite takes minutes | Three lanes run at once, one draft at a time per lane |
| Dependency | `files.txt`, the first pass's draft list | The README states it is not committed | The first pass cannot be re-run from this folder alone |
| Risk | A run answers from a previous export instead of writing one | One GLM 5.3 Flash max attempt did exactly that | The row is kept in the benchmark file for the record and is not counted as a valid comparison point |
| Risk | Shared gateway load during skill edits | The GLM 5.3 Flash max rerun took 5,762.2s and came back invalid | Recorded as invalid rather than compared |
| Risk | UI mechanics written as acceptance criteria | Three stories were not gate-clean on the first pass | A second pass moves each fixed mechanic into Requirements as a hard constraint |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:questions -->
## 7. OPEN QUESTIONS

- The per-surface acceptance-criteria ceiling stays open. Content Gallery - Highlights - Edit Reel UX still returns a high criteria count, at 13 criteria on a four-surface draft, and is the case behind the ceiling recorded in `Specs/030-system-hardening/spec.md` section 6.
- The folder's own record is not reconciled on that count: `README.md` states the second-pass counts dropped to 8, 5 and 6, and also names Edit Reel UX as the one story that still returns a high criteria count after the second pass.
<!-- /ANCHOR:questions -->

---
