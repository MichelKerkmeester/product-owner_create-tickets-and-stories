---
title: "Goal: Phase 45: FigJam findings fixes"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "packet goal"
  - "durable directive"
  - "completion criteria"
  - "goal binding"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "017-figjam-flow-generation/045-figjam-findings-fixes"
    last_updated_at: "2026-10-27T17:30:00Z"
    last_updated_by: "claude-code"
    recent_action: "Scaffolded the phase"
    next_safe_action: "Write the composer brief and the sentence swaps"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "348b59cb-58a2-4b49-8147-c40143312bc1"
      parent_session_id: null
    completion_pct: 0
    open_questions: []
    answered_questions: []
---
# Goal: Phase 45: FigJam findings fixes

<!-- SPECKIT_TEMPLATE_SOURCE: goal | v2.2 -->
<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Fix the causes the v1.0.10.0 Claude Sonnet 5.5 high rerun found as `sk-create-figjam` v1.0.11.0 with its Claude Project mirror in the same commits, so every plan follows the board the composer draws and the intake, sticky, revision, read-back and grading rules each say one thing, with no rerun.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | The plan follows a state board as drawn: the first state, the states inside a composite, then the end states, with the state a `%% focus:` line marks leading its line |
| D2 | On a user flow or a process the second glance is the main row as drawn, entry to goal in path order, and every node off it goes last. Two decisions no longer share a line |
| D3 | When every side of a noted node is taken, the gate offers pins and a legend or a recompose, a single sticky never sits more than one sticky width from its node and a sticky is a fixed 240 pixel square |
| D4 | After accepted answers the next reply is the playback, or one round about a row the last round left open or a gap the answers opened, and board scenarios allow the rounds a run opens |
| D5 | A revision playback reads the board first and the revision read-back names the changed end |
| D6 | Connector labels are matched from the write's return and the screenshot, and the read-back line says so |
| D7 | The playbook writes down the grading conventions: no order between the entry and the goal in one line, earlier file content outside the glance order and FigJam's close elbows not a trunk |
| D8 | Sentence swaps are scripted and byte-checked, every skill change reaches its Project file in the same commit and a fresh Opus reviewer reads the whole diff |

<!-- /ANCHOR:directive -->

---

<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [x] `compose_board.py --self-test`, `--design-check`, `flow_check.py --self-test`, `pytest scripts/tests`, `run_gates.sh` (all 15 gates) and the output format gate each exit 0 on the committed tree
- [x] `validate_parity.py product-owner` and `residency_check.py --all` each print PASSED after the last commit
- [x] The state, flow glance, boxed-in sticky, intake, revision and read-back rules read the same in the skill and the Project
- [x] No source keeps "two decisions share a line" or the single-round intake wording
- [x] The playbook carries the grading conventions and FJ-031's write-time signal
- [x] `sk-create-figjam` and the hub read 1.0.11.0 with a changelog
- [x] `validate.sh --strict` on this phase prints RESULT: PASSED, and both repositories are pushed
<!-- /ANCHOR:completion -->

---

<!-- ANCHOR:log -->
## 4. LOG

Everything below is VOLATILE. It is not part of the directive, it is not copied
into the objective, and it is expected to grow. Progress, evidence, deviations
and findings belong here.

### Progress

| Item | State | Evidence |
|------|-------|----------|
| Phase scaffolded | Done | spec, plan, tasks, acceptance criteria and this goal |
| Phase 045 closed | Done | v1.0.11.0 skill and Project fixes, review repaired, parity PASSED 65/65, residency PASSED 7, validate RESULT: PASSED |
| Homebrew node reinstalled | Done | v26.12.1 loads and flow_check prints the Label line on it and from a login shell |

### Deviations and findings

| Item | Note |
|------|------|
<!-- /ANCHOR:log -->
