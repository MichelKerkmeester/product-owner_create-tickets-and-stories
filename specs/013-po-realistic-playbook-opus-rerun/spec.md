---
title: "Feature Specification: Rewrite the Product Owner manual testing playbook around realistic tickets for three fictional companies, rename the Story export prefix, add the Story with nested Tasks bundle, then rerun both packagings on claude-opus-5-5 medium"
description: "The Product Owner benchmark exports look nothing like real engineering tickets: 12 of 14 scenarios are about payout pause, the other two about notification retry, and every Story saves under a PRD- prefix. This packet gives Story exports the Story- word, adds the Story with nested Tasks bundle, sets a rewritten playbook at three fictional companies, and reruns both packagings on claude-opus-5-5 at effort medium once the operator approves the scenario plan."
trigger_phrases:
  - "realistic product owner playbook"
  - "opus 5.5 medium playbook rerun"
  - "story export prefix"
  - "company context fixtures"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "013-po-realistic-playbook-opus-rerun"
    last_updated_at: "2026-09-25T20:40:00Z"
    last_updated_by: "claude-opus-5-5"
    recent_action: "Wrote the phase-parent spec and scoped phase 001"
    next_safe_action: "Execute phase 001 against its child goal"
    blockers: []
    key_files:
      - "AI Systems/Product Owner/sk-product-owner/manual-testing-playbook/manual-testing-playbook.md"
      - "AI Systems/Product Owner/claude project/Custom Instructions.md"
      - "AI Systems/Product Owner/sk-product-owner/SKILL.md"
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "12f293fe-5421-46a0-b1ea-9fdc15ce0f8e"
      parent_session_id: null
    completion_pct: 0
    open_questions:
      - "How phase 003 grades Story and Epic titles, since the H1 rule bans the discipline codes real titles carry"
    answered_questions:
      - "D1 to D5 decided by the operator on 2026-09-25, see goal.md"
---
<!-- SPECKIT_TEMPLATE_SOURCE: phase-parent-spec | v2.2 -->

<!-- SPECKIT_LEVEL: 2 -->
<!-- CONTENT DISCIPLINE: PHASE PARENT
  FORBIDDEN content (do NOT author at phase-parent level):
    - merge/migration/consolidation narratives (consolidate*, merged from, renamed from, collapsed, X→Y, reorganization history)
    - migrated from, ported from, originally in
    - heavy docs: plan.md, tasks.md, decision-record.md, implementation-summary.md: these belong in child phase folders only
  REQUIRED content (MUST author at phase-parent level):
    - Root purpose: what problem does this entire phased decomposition solve?
    - Sub-phase list: which child phase folders exist and what each one does
    - What needs done: the high-level outcome the phases work toward
-->

# Feature Specification: Rewrite the Product Owner manual testing playbook around realistic tickets for three fictional companies, rename the Story export prefix, add the Story with nested Tasks bundle, then rerun both packagings on claude-opus-5-5 medium

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P1 |
| **Status** | Complete |
| **Created** | 2026-09-25 |
| **Branch** | `main` |
| **Parent Spec** | None, this is the phase parent |
| **Parent Packet** | 013-po-realistic-playbook-opus-rerun |
| **Predecessor** | 045-playbook-rerun-sonnet-5-medium, whose Product Owner report stays as the historical record |
| **Successor** | None |
| **Handoff Criteria** | Each phase child closes on its own acceptance criteria before a phase that depends on it starts, and no scenario runs before the operator approves the scenario plan |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
The Product Owner playbook measures whether the system follows its rules, but the tickets it produces look nothing like real engineering work. Twelve of its 14 scenarios ask about one payout pause feature and the other two about notification retry, so every Task, Bug, Story and Doc a run exports is a toy with no product, surface, service or number behind it. The playbook never asks for an Epic, a parent task with subtasks, a refinement or a Story with the tasks that deliver it. Every Story also saves under a `PRD-` prefix while its sibling kind saves under `Epic-`. The 25 Sonnet exports in `export/benchmark/` showed all of this, and a model measured against toy prompts says little about the tickets a team would get.

### Purpose
One measurement of both Product Owner packagings on claude-opus-5-5 at effort medium, taken against 46 scenarios that ask for real-looking Tasks, Bugs, Stories, Epics and Docs at three fictional companies, each backed by its own context documents, with Stories exported under `Story-` and a Story able to ship with its tasks.

> **Phase-parent note:** This spec.md is the ONLY authored document at the parent level. All detailed planning, task breakdowns, checklists, and decisions live in the child phase folders listed in the Phase Documentation Map below. This keeps the parent from drifting stale as phases execute and pivot.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- The `Story-` export word and the `Story` clarification lane in both packagings, keeping the `$prd` and `$p` aliases and the H1 ban on a `PRD -` prefix
- The Story with nested Tasks bundle: one folder holding the Story and its linked task files
- Three fictional companies, Roamstay, Loomlist and Fernhouse, each with a context document and the source attachments the scenarios cite
- A rewritten playbook of 23 skill scenarios and 23 Project twins, with a ticket realism rubric and an extended runner and collector
- The operator's approval of the scenario plan before any scenario runs
- A full run of both packagings on claude-opus-5-5 at effort medium, then grading, a twin comparison, a realism review of every export and a report
- Commits in the Barter repo and the Product Owner public repo, pushed on the operator's go-ahead

### Out of Scope
- Prompt Improver and Deal Templates, per D5
- The live claude.ai Project. The Project packaging runs in the terminal harness, and a kernel reaches claude.ai only after the operator reviews and uploads it
- Any model or effort level other than claude-opus-5-5 at medium
- Repairs after grading that the operator has not decided, per D7

### Files to Change

| File Path | Change Type | Phase | Description |
|-----------|-------------|-------|-------------|
| `AI Systems/Product Owner/export/benchmark/**` | Delete, create | 001, 004 | The 25 Sonnet files out first, the Opus run's deliverables in after the run |
| `AI Systems/Product Owner/` skill sources, kernel, knowledge, READMEs, `SYNC.md` | Modify | 001 | The `Story-` word, the bundle rule and the version bookkeeping |
| The Claude Project Sync Loop declaration `systems.py` | Modify | 001 | Declared kernel statements, through the loop's own tools |
| `AI Systems/Product Owner/benchmark/fixtures/companies/**` | Create | 002 | Three company context documents and their attachments |
| `AI Systems/Product Owner/sk-product-owner/manual-testing-playbook/**` | Modify, delete, create | 003 | The root and 46 scenario files |
| `AI Systems/Product Owner/benchmark/reports/<date>--manual-testing-playbook--claude-opus-5-5-medium/**` | Create | 003, 004, 005 | Runner, checker, collector, run output, grading and report |
| `AI Systems/Product Owner/specs/013-po-realistic-playbook-opus-rerun/**` | Create | all | This packet |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:phase-map -->
## PHASE DOCUMENTATION MAP

> This spec uses phased decomposition. Each phase is an independently executable child spec folder. All implementation details (plan, tasks, checklist, decisions, continuity) live inside the phase children.

| Phase | Folder | Focus | Status |
|-------|--------|-------|--------|
| 1 | 001-story-prefix-and-bundle/ | Give Story exports the `Story-` word in both packagings, add the Story with nested Tasks bundle, and commit the removal of the old Sonnet exports | Complete |
| 2 | 002-company-context-fixtures/ | Write the Roamstay, Loomlist and Fernhouse context documents and every source attachment the scenario catalog cites | Complete |
| 3 | 003-playbook-rewrite/ | Rewrite the playbook root and the 46 scenario files, extend the runner and collector, then stop at the operator's approval gate | Complete |
| 4 | 004-opus-run/ | After approval, run a smoke pair, then all 46 scenarios on claude-opus-5-5 at effort medium, and collect the deliverables | Complete |
| 5 | 005-grading-and-report/ | Grade every turn, compare the twins, review each export's realism, write the report and bring the findings to the operator | Complete |
| 6 | 006-concise-writing/ | Set length caps in the rules, warn on them in the gate and the playbook, and edit the exports and report to them by hand | Complete |
| 7 | 007-drop-clarification-exports/ | Remove the 20 clarification files from the published exports and make the collector skip them | Complete |
| 8 | 008-cut-exports-and-word-budget/ | Cut the exports about 30% and add a per-artifact word budget to the rules | Complete |
| 9 | 009-template-forms-and-checklists/ | Move Story and Epic openings to H4, About to H2 in every template, Story requirements to checklist items and every checklist to `[]`, across rules, gates, playbook, mirrors and the 78 exports | Complete |

### Cross-Phase Dependencies

- 001 and 002 have no dependency on each other and may run side by side
- 003 depends on 001, because its scenarios grade the `Story-` word and the bundle, and on 002, because its scenarios cite the fixtures
- 004 depends on the operator's approval of the scenario plan that 003 presents, not only on 003 closing
- 005 depends on 004's run and collection

### Phase Transition Rules

- Each phase MUST pass `validate.sh` independently before the next phase begins
- Parent spec tracks aggregate progress via this map
- Use `/spec_kit:resume [parent-folder]/[NNN-phase]/` to resume a specific phase
- Run `validate.sh --recursive` on parent to validate all phases as integrated unit

### Phase Handoff Criteria

| From | To | Criteria | Verification |
|------|-----|----------|--------------|
| 001-story-prefix-and-bundle | 002-company-context-fixtures | None. Phase 002 does not wait on 001, and 001 closes on its own criteria | Phase 001 `acceptance-criteria.md` |
| 002-company-context-fixtures | 003-playbook-rewrite | Phase 001 committed with the proof grep empty and parity green, and every fixture file the catalog names present with no em dash | Both phases' `acceptance-criteria.md` read `Closeable: Yes` |
| 003-playbook-rewrite | 004-opus-run | The validator finds 0 violations in 46 scenarios, a synthetic bundle reply collects into its subfolder, and the operator approved the scenario plan | Validator output, the approval recorded in phase 003's continuity block |
| 004-opus-run | 005-grading-and-report | Every turn completed, the isolation proofs and `check_run.py` clean, and the collection into `export/benchmark/` done | `run-status.json`, `check_run.py` output, the collection listing |
| 005-grading-and-report | 006-concise-writing | Every scenario graded, the report written and the three rounds committed and pushed | `results.csv` in the run and both rounds, the pushed commits |
| 006-concise-writing | 007-drop-clarification-exports | The caps in the rules, the exports edited and both repos pushed | Product Owner `fdc8a28`, Barter `48ca7a3f` |
| 007-drop-clarification-exports | 008-cut-exports-and-word-budget | No clarification published or kept locally | Product Owner `e042272`, Barter `c6493c1b` |
| 008-cut-exports-and-word-budget | 009-template-forms-and-checklists | 008 committed and pushed | Product Owner bb9210f, Barter 0b08add1 on origin |
<!-- /ANCHOR:phase-map -->

---

<!-- ANCHOR:questions -->
## 4. OPEN QUESTIONS

- The Story and Epic H1 rule bans `BO`, `BE` and `FE` codes, while the realism rubric planned for phase 003 expects titles to carry a discipline code as real ones do. Phase 003 settles how Story and Epic titles are graded, or the operator changes the rule
- A Story request that says "create a task for each platform" routes to Task Mode today. Phase 001 leaves the router unchanged, so phase 003 keeps the bundle scenario on `$story`
<!-- /ANCHOR:questions -->

---

## RELATED DOCUMENTS

- **Phase children**: `001-story-prefix-and-bundle/`, `002-company-context-fixtures/`, `003-playbook-rewrite/`, `004-opus-run/`, `005-grading-and-report/`
- **Goal**: `goal.md`, holding decisions D1 to D7 and the completion criteria
- **Graph Metadata**: See `graph-metadata.json` for `derived.last_active_child_id` pointer
