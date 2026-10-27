---
title: "Feature Specification: Phase 45: FigJam findings fixes"
description: "The v1.0.10.0 rerun passed 2 of 6 and the operator closed testing. Its findings show plans that ignore the board the composer draws, two intake sentences that disagree, a boxed-in sticky with no place, a revision playback that reads nothing and playbook rules the graders applied without the text saying so. This phase fixes them as v1.0.11.0 with the Claude Project in step and no rerun."
trigger_phrases:
  - "figjam findings fixes"
  - "phase 45 figjam fixes"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.3 -->
# Feature Specification: Phase 45: FigJam findings fixes

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P1 |
| **Status** | Complete |
| **Created** | 2026-10-27 |
| **Branch** | `main` |
| **Parent Spec** | ../spec.md |
| **Phase** | 45 of 45 |
| **Predecessor** | 044-figjam-composite-and-path-order |
| **Successor** | None |
| **Handoff Criteria** | Every row in acceptance-criteria.md is Met |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 45** of the Product Owner FigJam flow generation upgrade specification.

**Scope Boundary**: the findings and critic gaps of the v1.0.10.0 rerun in `sk-create-figjam`, its examples, the playbook and the Claude Project mirror, then a rerun of the four scenarios still failing on v1.0.11.0. The operator reopened this phase for that rerun on 2026-10-27.

**Dependencies**:
- The rerun records in `benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison/` (`grades/sonnet-high-044.*`, README section 8.10).
- `sk-create-figjam` v1.0.10.0 as phase 044 left it.

**Deliverables**:
- The skill, example and playbook fixes, released as hub and `sk-create-figjam` v1.0.11.0.
- The hand-written Project mirror in the same commit.

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Claude Sonnet 5.5 high reran the 6 failures of v1.0.9.0 on v1.0.10.0 and 2 pass, FJ-032 by the operator's ruling. The state rule plans a named end state first, but the composer always draws end states on the last ranks, so FJ-026's readers take the first state and the composite before its pink outline. The rubric plans a flow's outlined kinds second and lets two decisions share a line, while readers take the main row the composer draws, entry to goal, then the nodes off it, so FJ-029's plan reads out of order and FJ-036's detour, drawn on the row, reads before the outcomes planned second. `references/flow-mode.md` Section 2 says the reply after accepted answers is the playback, while a later sentence lets a round ask a row left unasked. The single-sticky fallback parked FJ-017's boxed-in note 688 px from its node, and the skill never says a sticky is a fixed 240 px square. A revision playback reads nothing first, the revision reply shape drops the second glance and the read-back assumes `get_figjam` returns connector labels. Board scenarios expect one intake round at most and three grading conventions the graders applied are not in the playbook.

### Purpose
Make every plan follow the board the composer draws, make the intake, sticky, revision and read-back rules agree with themselves, and write the grading conventions into the playbook, in the skill and the Project alike.

### Decisions
- **D1**: State boards. The plan follows the board, whether or not a state is named: the first state first, the states inside a composite second with their section and the end states last, because the composer draws end states on the last ranks. A `%% focus:` line marks the named state, or the most telling member of a named group, where it is drawn, and that state leads its glance line. The composer is unchanged, and the playbook scores 2 when the marked state leads its line and the rest of the order holds (the operator chose this on 2026-10-27).
- **D2**: Flow glance lines. On a user flow or a process the second glance is the main row, the longest path from the entry to the goal, which the composer draws as one row, so a detour on that path is part of it. It is named in path order without the accented node, and every node off that row, such as an error, an exit, a branch or a loop back, goes in the last glance in path order. "Two decisions share a line" is dropped and the process example follows (the operator chose this on 2026-10-27).
- **D3**: Boxed-in sticky. When every side of a noted node is taken, the gate says so before any write and offers the pin and legend form or a recompose with more room. A single sticky never sits more than one sticky width from its node. A FigJam sticky is a fixed 240 pixel square, so a side needs 240 pixels plus the 64 pixel gap, and a size probe runs inside the notes call (the operator chose this on 2026-10-27).
- **D4**: Intake. After accepted answers the next reply is the playback, or one round about a row the last round named as still open or a gap those answers opened, as the operator ruled for FJ-032. Board scenarios allow the rounds the run opens, and each round moves the later turn numbers by one.
- **D5**: A revision playback reads the board with `get_figjam` first, and the revision reply names the changed end as the second glance on its read-back line.
- **D6**: Connector labels are matched from the composing write's return and the overview screenshot, because `get_figjam` returns none, and a labelled count on the read-back line rests on those two. The first draft added a clause to every read-back line, which a fresh review showed every shipped example reply would then lack, so the rule was narrowed on 2026-10-27 and the reply shape stays as it was.
- **D7**: The playbook writes down the conventions the graders applied: the entry and the goal in one line carry no order, content the file held before the write is outside the glance order, and two runs FigJam draws closer than the composer's path estimate keeps them are not a trunk.
- **D8**: Exact sentence swaps are applied by script and byte-checked in the skill and the mirror alike, every skill change reaches its Project file in the same commit, and a fresh Opus reviewer reads the whole diff.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Plan a state board as drawn per D1 in the state reference, the rubric and the playbook Composition row.
- Define the flow glance lines per D2 in the rubric, the playbook and the process and user flow examples.
- Give the boxed-in sticky a gate question and the sticky's size per D3.
- Reconcile the intake sentences per D4 and let every board scenario allow the rounds a run opens.
- Read the board before a revision playback and name the changed end on the revision read-back per D5.
- State how connector labels are read per D6.
- Write the grading conventions per D7 and add the write time to FJ-031's delete signal.
- Rerun FJ-017, FJ-026, FJ-029 and FJ-036 on v1.0.11.0 with Claude Sonnet 5.5 high, each board scenario in a fresh draft file, and grade them as phase 044 graded its rerun.

### Out of Scope
- The composer and its geometry.
- A rerun of FJ-031 and FJ-032, which passed on v1.0.10.0.
- The machine's Homebrew node, which waits for the operator's yes to a reinstall.

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| sk-create-figjam/SKILL.md, references/, assets/examples/ | Modify | Flow Mode, rubric, style guide, state reference, hybrid workflow and the state, user flow and process examples |
| sk-create-figjam/manual-testing-playbook/ | Modify | The Composition and Shared trunks rows, the intake turn rule and the board scenarios' intake wording |
| claude project/, SYNC.md, README.md | Modify | Mirror and release notes |
| changelog/, sk-create-figjam/changelog/, version files | Create, Modify | v1.0.11.0 |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | The composer self-test, the design check, the flow check self-test, pytest, the 15 repository gates and the output format gate all exit 0 on the committed tree. |
| REQ-002 | The Sync Loop parity and residency checks print PASSED after the last commit. |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-003 | The state reference, the rubric and the playbook plan a state board as drawn per D1, in the skill and the Project. |
| REQ-004 | The rubric, the playbook and both flow examples define the glance lines per D2, and no source keeps "two decisions share a line". |
| REQ-005 | The hybrid workflow states the boxed-in gate question and the sticky's size per D3. |
| REQ-006 | No source states the narrower intake rule, and no board scenario expects at most one intake round. |
| REQ-007 | Flow Mode reads the board before a revision playback, names the changed end on the revision read-back and says how connector labels are read, per D5 and D6. |
| REQ-008 | The playbook states the D7 conventions, and FJ-031's delete signal names the write time. |
| REQ-009 | `sk-create-figjam` and the hub read 1.0.11.0 with a changelog, and the kernel H1 moves only when its rules change. |
| REQ-010 | The four scenarios still failing are rerun on v1.0.11.0, graded by one Opus grader with two readers per board, and recorded in the run README as section 8.11. |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: Each finding of README section 8.10 that names a skill, playbook or mirror cause has a change in this phase or a recorded reason it needs none.
- **SC-002**: The skill and the Project state each changed rule in the same words, as the Sync Loop parity check shows.
- **SC-003**: At least three of the four rerun scenarios pass on v1.0.11.0.
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Risk | The kernel's character room | Med | The kernel changes only if a rule it carries changes, and the residency check runs after |
| Risk | Rules no rerun has tested | Med | A fresh Opus reviewer reads the whole diff against the findings before the commit |
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
- A state board with no composite: the first state first and the end states second, with a named end state leading its line.
- A flow whose only path to the goal runs through a detour: the detour is on the main row and planned second.

### Error Scenarios
- A boxed-in node found only after the compose: the notes call writes nothing and the reply asks the gate question.
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 14/25 | About 40 files across the skill, examples, playbook scenarios and mirror |
| Risk | 6/25 | Prose rules only, no composer change |
| Research | 2/20 | The findings were graded and criticised before this phase |
| **Total** | **22/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- None. The operator settled D1 to D4 on 2026-10-27 and reopened the phase for the rerun the same day.
<!-- /ANCHOR:questions -->
