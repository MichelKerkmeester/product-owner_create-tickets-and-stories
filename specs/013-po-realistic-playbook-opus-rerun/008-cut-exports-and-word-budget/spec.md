---
title: "Feature Specification: Phase 8, cut the exports and set a word budget"
description: "The first conciseness pass met the length caps by splitting lines and cut 2% of the words, so the exports still read long. This phase cuts them about 30% and puts a per-artifact word budget into the rules."
trigger_phrases:
  - "cut exports word budget"
  - "second conciseness pass"
  - "per-artifact word budget"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core + level2-verify | v2.2 -->
# Feature Specification: Phase 8, cut the exports and set a word budget

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
| **Phase** | 8 of 8 |
| **Predecessor** | 007-drop-clarification-exports |
| **Successor** | None |
| **Handoff Criteria** | The 78 exports cut about 30% with every protected fact kept, and the budget on both entry-point lines and the playbook root |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 8** of the realistic Product Owner playbook packet.

**Scope Boundary**: The 78 exports in `export/benchmark/`, the run README's edit record, and the budget on `SKILL.md` line 276, kernel line 90 and the playbook's Size band row, with their versions.

**Dependencies**:
- Phase 007 pushed, Product Owner `e042272` and Barter `c6493c1b`

**Deliverables**:
- 78 exports cut 22.7% in two rounds, checked by a script and by fact reviewers
- A word budget per artifact kind, taken from the cut exports' own counts
- Skill 0.16.0, kernel v0.19.0, playbook 2.4.0.0, a changelog and a `SYNC.md` note
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
The operator read the exports after phase 006 and found them still bloated. That pass kept every fact and split long lines, so words fell 2% on the skill side and 1.7% on the Project side. The caps bound a line, never a whole artifact, so a new run can write the same length again.

### Purpose
The exports read about 30% shorter with nothing a reader acts on lost, and the rules name how long each artifact kind should run.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Cut the 78 exports: restatement, background nobody acts on, explanation past the first reason
- Keep every supplied value, name, number, owner, decision, requirement and open question
- Set a word budget per artifact kind from the cut exports, on both entry-point lines and the playbook's Size band row
- Record the second edit in the run README

### Out of Scope
- A rerun, because the operator has ruled one out since phase 006
- The format gate, since the operator chose the rules and the playbook row only
- The shared Conciseness card, which three other systems read, as decided in phase 006
- Grading verdicts, which still cite the graded originals

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `AI Systems/Product Owner/export/benchmark/**` | Modify | 78 exports cut |
| `sk-product-owner/SKILL.md`, `claude project/Custom Instructions.md` | Modify | The budget on line 276 and line 90, skill 0.16.0 and kernel v0.19.0 |
| `sk-product-owner/manual-testing-playbook/manual-testing-playbook.md` | Modify | The budget in the Size band row, root 2.4.0.0 |
| `sk-product-owner/changelog/v0.16.0.0.md`, `SYNC.md`, both READMEs, `description.json` | Create, Modify | Versions and the pending kernel review |
| The run's `README.md` | Modify | The second edit recorded |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | The exports lose words to the depth the operator chose after round one showed 14.9%: 22 to 25% overall, measured by `scratch/verify_cut.py` against `scratch/before-cut/`. The first aim was about 30% |
| REQ-002 | No protected fact is lost: every backticked value, number and link survives the script, and fact reviewers find no dropped, changed or added fact left unrepaired |
| REQ-003 | Every export still passes the format gate and the length caps |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-004 | A word budget per artifact kind is on `SKILL.md` line 276, kernel line 90 and the playbook's Size band row, with every version surface bumped and parity passing |
| REQ-005 | The run README records the second edit, its word counts and that the budget is unmeasured on the runtimes |
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: Words across the 78 exports fall by 22% or more, the depth the operator chose after round one
- **SC-002**: The format gate, parity, residency and the playbook validator pass on the committed state
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Risk | A cut drops a fact carried in plain words, which no script sees | High | Fact reviewers read every file against its snapshot, and each finding is repaired |
| Risk | A hedge becomes a claim | Med | The brief forbids it and the reviewers check for it |
| Dependency | The kernel review goes stale at v0.19.0 | Low | Recorded in `SYNC.md` as pending until the operator confirms it |
<!-- /ANCHOR:risks -->

---


---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Performance
- **NFR-P01**: A reader finds each artifact's decisions and values without reading a restated paragraph twice

### Security
- **NFR-S01**: No secret or credential enters any file

### Reliability
- **NFR-R01**: The collector's edit guard keeps the cut files on the next collection
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Data Boundaries
- A short, value-dense export: cut less and say why, rather than dropping a value
- An About that still runs past two paragraphs: kept only where a fact would go

### Error Scenarios
- A writer's file fails the script: it goes back once, then to me
- A reviewer finds a lost fact: repaired in place and rechecked

### State Transitions
- Two turn copies of one Project artifact: cut each, keeping shared wording aligned
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 16/25 | 78 exports, two rule lines, one playbook row, version surfaces |
| Risk | 12/25 | Fact loss in plain words, a stale kernel review |
| Research | 4/20 | Budget taken from measured counts |
| **Total** | **32/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- None. The operator chose about 30%, all 78 files and a word budget in the rules on 2026-09-26
<!-- /ANCHOR:questions -->

---
