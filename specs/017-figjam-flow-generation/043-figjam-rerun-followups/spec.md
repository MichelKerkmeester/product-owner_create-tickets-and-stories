---
title: "Feature Specification: Phase 43: FigJam rerun follow-ups"
description: "The v1.0.8.0 rerun passed 7 of the 14 failures under the operator's two grading rulings. The rest fail on a composite's inner states, a split title spelled two ways, a revision's second glance and numbered title, replies that do not open on the URL, stickies on adjacent rows and a missing-route gate. This phase fixes them as v1.0.9.0 and reruns the 7 failures with two readers per board."
trigger_phrases:
  - "figjam rerun follow-ups"
  - "phase 43 figjam follow-ups"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.3 -->
# Feature Specification: Phase 43: FigJam rerun follow-ups

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
| **Phase** | 43 of 43 |
| **Predecessor** | 042-figjam-glance-and-left-out |
| **Successor** | None |
| **Handoff Criteria** | Every row in acceptance-criteria.md is Met |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 43** of the Product Owner FigJam flow generation upgrade specification.

**Scope Boundary**: the findings and critic gaps of the v1.0.8.0 rerun in `sk-create-figjam`, its examples, the playbook, the check, the Claude Project mirror and kernel, and the run's records, then a rerun of the 7 scenarios that failed. No Barter board is read or written.

**Dependencies**:
- The rerun records in `benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison/` (`grades/sonnet-high-042.*`, README section 8.8).
- `sk-create-figjam` v1.0.8.0 as phase 042 left it.

**Deliverables**:
- The skill, example, check and playbook fixes, released as hub and `sk-create-figjam` v1.0.9.0, with the kernel moved only if its rules change.
- The hand-written Project mirror.
- A graded rerun of the 7 failures with two readers per scored board, its renders and README section 8.9.

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Claude Sonnet 5.5 high reran the 14 failures of v1.0.7.0 on v1.0.8.0 and 7 pass under the operator's rulings. FJ-026 and FJ-032 lose Composition because readers take the states inside a composite before the planned glance, while the state rule plans them last. FJ-029 titles its second board `2. Setup`, the spelling `assets/flow-templates.md` gives, and names no split. FJ-031's plan lets the light blue entry and the decisions compete with the changed end for the second glance, and the gate's numbered-title advice keeps `Start a return 2` so the write-time delete rule never runs. FJ-029, FJ-031 and FJ-036 open a reply on prose above the URL. FJ-017 shifts two stickies on adjacent rows off level. FJ-009 copies the composed-route gate where the missing route belongs, and no example shows that gate. No run printed a `Label:` line, because the check falls silent without node.

### Purpose
Close each gap at its source and in the Project, make the playbook grade lanes, zones and a composite's inner states one way with two readers per board, and prove it by rerunning the 7 failures on the same model.

### Decisions
- **D1**: State boards. With no state named, the first state is planned first, the states inside a composite second with their section and the end states last. With a state named, the focus line marks it first and the first state and the composite's states follow in the second glance.
- **D2**: The style guide's 56 pixel rule holds on the composer's path estimate. FigJam may draw an elbow closer, and graders do not count that as a loss. The composer is not changed.
- **D3**: Each scored board gets two fresh readers. A Composition point is lost only when both read an unplanned part ahead of the planned glance. The playbook row says so.
- **D4**: The rerun covers the 7 failures: FJ-009, FJ-017, FJ-026, FJ-029, FJ-031, FJ-032 and FJ-036.
- **D5**: Lanes and zones read as frame on every type, like the title block, as the operator ruled in phase 042. The playbook row and the rubric say so.
- **D6**: Exact sentence swaps whose wording this phase sets are applied by script and byte-checked in the skill and the mirror alike. DeepSeek V4.1 Flash max on cli-pi through llmgateway makes the code changes, one change per brief. A fresh Opus reviewer verifies the whole diff. GPT 6 Luna max fast on cli-codex is the only fallback.
- **D7**: Every skill change reaches its Project file in the same commit.
- **D8**: Each rerun board scenario writes into a fresh draft file in the Barter team plan with its starting section count recorded, and each run has its own temp folder. No board URL, file key, plan name or email reaches a committed file.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Plan a composite's inner states second per D1 in the state rule, the state example and the playbook Composition row.
- Spell the second split title one way and name the split under `Left out:` even when the file holds both boards.
- Make a revision's changed end the second glance alone, and keep the old title on a revision that deletes the old section.
- Open every delivery reply and the delete reply on the board URL with nothing before it.
- Place a single sticky when two noted nodes sit on adjacent rows.
- Show a missing-route gate in the gantt example.
- Make the `Label:` check say when it skipped, and give the Project a hand rule for labels.
- Reword the elbow rule per D2, and write D3 and D5 into the playbook and the rubric.
- Rerun the 7 failures with two readers per scored board, grade them and write README section 8.9.

### Out of Scope
- The composer and its colours.
- Running FJ-018 and FJ-035, which need Figma Desktop and the figma-ds-cli daemon.
- Rerunning the 7 scenarios that passed on v1.0.8.0.

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| sk-create-figjam/SKILL.md, references/, assets/ | Modify | Flow Mode, rubric, style guide, hybrid workflow, state reference, flow templates and examples |
| sk-create-figjam/scripts/ | Modify | The label check's skipped line and its self-test |
| sk-create-figjam/manual-testing-playbook/ | Modify | The Composition row and the scenario rows the fixes touch |
| AGENTS.md, claude project/, SYNC.md, README.md | Modify | Reply contract, mirror, kernel and release notes |
| benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison/ | Modify, Create | The grader brief, the rerun records and README |
| changelog/, sk-create-figjam/changelog/, version files | Create, Modify | v1.0.9.0 |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | The composer self-test, the design check, the flow check self-test, pytest, the 15 repository gates and the output format gate all exit 0 on the committed tree. |
| REQ-002 | The Sync Loop parity and residency checks print PASSED after the last commit, and the Flow Board Composer Knowledge code block equals `compose_board.py --template`. |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-003 | The state rule, the state example and the playbook Composition row plan a composite's inner states second per D1, in the skill and the Project. |
| REQ-004 | No source spells the second split title two ways, and the split reply and gate carry a `Left out:` line naming the second board. |
| REQ-005 | A revision plans its changed end alone in the second glance, and a revision that deletes the old section keeps the old title. |
| REQ-006 | Every delivery reply and the delete reply open on the board URL with nothing before it, in the skill, the Project and the kernel. |
| REQ-007 | The single sticky rule places two stickies whose nodes sit on adjacent rows, and the gantt example shows a missing-route gate. |
| REQ-008 | `flow_check.py` prints a `Label:` line saying the check was skipped and why when node is missing or the trace fails, proved by a self-test case, and the Project's Flow Mode carries a hand rule for labels. |
| REQ-009 | The style guide states D2, and the playbook root states D3 and D5. |
| REQ-010 | The 7 failures run again on Claude Sonnet 5.5 high in fresh files, every board is rendered and read by two readers and each scenario is graded on one line. |
| REQ-011 | `sk-create-figjam` and the hub read 1.0.9.0 with a changelog, and the kernel H1 moves when its rules change. |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: At least 5 of the 7 rerun scenarios pass, and every remaining failure is named with its cause in the run README.
- **SC-002**: No rerun board loses a Composition point that only one of its two readers saw.
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | Draft files in the Barter team plan for every board scenario | High | Files are created before the lanes start and their keys stay in the scratchpad |
| Risk | Disk space on the run machine | Med | Free space is checked before launch, and a lane that stops before its first turn is relaunched |
| Risk | The kernel's character room | Med | The output format gate and the Sync Loop residency check run after every kernel edit |
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
- A state board with no composite: the first state is planned first and the end states second, as before.
- Two noted nodes on adjacent rows with no free side: the second sticky goes below or to the left of its node and the reply names it on a `Finding:` line.

### Error Scenarios
- A lane that stops before its first turn, such as on a full disk: the lane is relaunched and the stop is recorded as a harness fact.
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 14/25 | About 30 files across skill, examples, mirror, kernel, check, playbook and records |
| Risk | 8/25 | The kernel, the reply contract and a live rerun |
| Research | 3/20 | The findings were graded and criticised before this phase |
| **Total** | **25/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- None. The operator settled D1 to D5 on 2026-10-27.
<!-- /ANCHOR:questions -->
