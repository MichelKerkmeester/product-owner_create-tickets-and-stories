---
title: "Feature Specification: Phase 46: FigJam gate and accent fixes"
description: "The v1.0.11.0 rerun passed 2 of 4. FJ-017's gate could not see a noted node's sides before the write, FJ-036 put its accent on the goal the composer draws last, and the findings named a gate without its sketch, a stop that ended on a self-scan line, a label trace that missed a lone word and an end-state order the playbook never set. This phase fixes them as v1.0.12.0 with the Claude Project in step, then reruns the affected scenarios."
trigger_phrases:
  - "figjam gate and accent fixes"
  - "phase 46 figjam fixes"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.3 -->
# Feature Specification: Phase 46: FigJam gate and accent fixes

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P1 |
| **Status** | In Progress |
| **Created** | 2026-10-27 |
| **Branch** | `main` |
| **Parent Spec** | ../spec.md |
| **Phase** | 46 of 46 |
| **Predecessor** | 045-figjam-findings-fixes |
| **Successor** | None |
| **Handoff Criteria** | Every row in acceptance-criteria.md is Met |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 46** of the Product Owner FigJam flow generation upgrade specification.

**Scope Boundary**: the two failures and the open findings of the v1.0.11.0 rerun in `sk-create-figjam`, its scripts, its shipped models, the playbook, `AGENTS.md` and the Claude Project mirror, then a rerun of FJ-017 and FJ-036 and of FJ-022 and FJ-023, whose gallery boards accented the goal.

**Dependencies**:
- The rerun records in `benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison/` (`grades/sonnet-high-045.*`, README section 8.11).
- `sk-create-figjam` v1.0.11.0 as phase 045 left it.

**Deliverables**:
- The script, skill, model and playbook fixes, released as hub and `sk-create-figjam` v1.0.12.0.
- The hand-written Project mirror in the same commit.
- The graded rerun and the gallery boards it earns.

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Claude Sonnet 5.5 high reran the 4 failures of v1.0.10.0 on v1.0.11.0 and 2 pass. FJ-017's gate could not know a noted node was boxed in, because nothing traced the board before the write, so the sticky question came too late. FJ-036 put its one accent on the goal, which the composer draws at the far end of the main row, so readers reached the marked node last and Composition scored 0. Nine of the eleven shipped flow models accent their goal the same way. The playback and the gate of FJ-036 and an intake round of FJ-029 ended on an `HVR self-scan:` line after their question, and no rule said whether that line belongs there. Most gates showed no sketch and answered none of the four critique questions, which the skill names only by its first. The label trace missed a lone `tip` FigJam wrapped on FJ-029, and FJ-026's pass rests on end states named as one group carrying no order, which the playbook never states.

### Purpose
Let the gate see where each note lands, keep the accent off the goal, make every stop end on its question, make the gate's sketch and critique required and write the end-state reading into the playbook, in the skill and the Project alike.

### Decisions
- **D1**: Trace sides at the gate. A model whose board carries single stickies names their nodes on a `%% notes:` line, which moves the key down by one sticky and its gap. `flow_check.py --notes` composes the board in memory and prints a `Sides:` line per noted node, and a sticky placed for an earlier node takes its side from the next. The gate names each side or offers pins with a legend or a model change for a boxed-in node (the operator chose this on 2026-10-27).
- **D2**: Accent the entry instead. The goal never takes the accent, because the composer draws it last on the main row. A `%% goal:` line names it, and the one accent goes to a decision, a failure end or the one step in focus (the operator chose this on 2026-10-27).
- **D3**: The rule reaches all nine shipped flows that accent their goal, their Project mirrors and the extension and revision rules (the operator chose this on 2026-10-27).
- **D4**: Nothing after a stop's question. An intake round, the playback and the gate deliver nothing, so none carries the `HVR self-scan:` line (the operator chose this on 2026-10-27).
- **D5**: End states carry no order. A group the request names as one, such as the end states, reads as a set whose member order neither the plan nor a reader scores (the operator chose this on 2026-10-27).
- **D6**: Gate questions required. The gate always shows the sketch with the check's result and answers the four critique questions, now each named, unless the user already settled them (the operator chose this on 2026-10-27).
- **D7**: The label trace reads each label at the normal and the narrow character measure, so a lone last word FigJam wraps prints a `Label:` line.
- **D8**: Exact sentence swaps are applied by script and byte-checked in the skill and the mirror alike, every skill change reaches its Project file in the same commit, and a fresh Opus reviewer reads the whole diff.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Add the `%% notes:` line to the composer and the `--notes` sides check per D1, with self-tests, and rewrite FJ-017 around them.
- Keep the accent off the goal per D2 and re-accent the nine shipped flows per D3, and rewrite FJ-022's goal and accent signals.
- Write the stop rule per D4, the end-state reading per D5 and the gate's sketch and critique per D6.
- Read labels at two measures per D7.
- Rerun FJ-017, FJ-036, FJ-022 and FJ-023 on v1.0.12.0 with Claude Sonnet 5.5 high, each in a fresh draft file in the operator's team drafts, grade them as phase 045 graded its rerun and refresh the gallery boards the passing runs earn.

### Out of Scope
- The composer's layout and geometry beyond the key's gap.
- A rerun of scenarios that passed on v1.0.11.0 and are untouched by these rules.

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| sk-create-figjam/scripts/, assets/compose-board.js | Modify | The notes line, the sides check, the goal line and the two-measure label trace |
| sk-create-figjam/references/, assets/ | Modify | Flow Mode, rubric, style guide, hybrid workflow, flow types and the re-accented models |
| sk-create-figjam/manual-testing-playbook/ | Modify | The Composition, Signal and acceptance rules, FJ-017 and FJ-022 |
| AGENTS.md, claude project/, SYNC.md, README.md | Modify | The stop rule, the mirror and the release notes |
| changelog/, sk-create-figjam/changelog/, version files | Create, Modify | v1.0.12.0 |
| benchmark/reports/.../, sk-create-figjam/assets/screenshots/ | Create, Modify | The rerun records and the gallery |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | The composer self-test, the design check, the flow check self-test, pytest, the 15 repository gates and the output format gate all exit 0 on the committed tree. |
| REQ-002 | The Sync Loop parity, residency and divergence checks print PASSED after the last commit. |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-003 | The composer accepts a `%% notes:` line and refuses one naming a missing node, `flow_check.py --notes` prints a `Sides:` line per noted node, and the hybrid workflow and FJ-017 state the gate's use of it per D1. |
| REQ-004 | No source lets the goal take the accent, a `%% goal:` line names it per D2, and every shipped flow model accents a decision, a failure end or a step per D3. |
| REQ-005 | Flow Mode, `AGENTS.md` and the playbook state the stop rule per D4. |
| REQ-006 | The playbook states the end-state reading per D5. |
| REQ-007 | Flow Mode names all four critique questions and makes the gate's sketch and critique required per D6, and the rubric and the playbook check it. |
| REQ-008 | The label trace reads at two measures per D7, with a self-test for the lone word. |
| REQ-009 | `sk-create-figjam` and the hub read 1.0.12.0 with a changelog, and the kernel H1 moves only when its rules change. |
| REQ-010 | FJ-017, FJ-036, FJ-022 and FJ-023 are rerun on v1.0.12.0, graded by one Opus grader with two readers per board and recorded in the run README as section 8.12, and the gallery takes each passing board. |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: Each finding of README section 8.11 that names a skill, script, playbook or mirror cause has a change in this phase or a recorded reason it needs none.
- **SC-002**: The skill and the Project state each changed rule in the same words, as the Sync Loop parity and divergence checks show.
- **SC-003**: FJ-017 and FJ-036 pass on v1.0.12.0.
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Risk | The Project composer's 50,000 character budget | Med | The notes gap costs 13 characters, and the composer test names the room left |
| Risk | Rules no rerun has tested | Med | A fresh Opus reviewer reads the whole diff before the commit, and the rerun follows |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Security
- **NFR-S01**: No board URL, Figma file key, plan name or email in any committed file. PO is a public repository.
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Data Boundaries
- Two noted nodes on adjacent rows: the first sticky takes the right, so the second takes below or left.
- A flow whose only decision is the goal's gate: the accent goes to that decision and the goal line names the end.

### Error Scenarios
- A node that shows boxed in only after the compose: no notes call runs and the reply asks the gate's question.
- A `%% goal:` line naming a step: the composer refuses it.
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 15/25 | About 35 files across the scripts, skill, models, playbook and mirror, plus a four-scenario rerun |
| Risk | 8/25 | A composer gap change and a new check mode, each self-tested |
| Research | 2/20 | The findings were graded and criticised before this phase |
| **Total** | **25/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- None. The operator settled D1 to D6 on 2026-10-27.
<!-- /ANCHOR:questions -->
