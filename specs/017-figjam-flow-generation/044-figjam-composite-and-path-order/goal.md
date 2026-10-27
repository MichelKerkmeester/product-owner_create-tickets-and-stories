---
title: "Goal: Phase 44: FigJam composite placement and path order"
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
    packet_pointer: "017-figjam-flow-generation/044-figjam-composite-and-path-order"
    last_updated_at: "2026-10-27T14:20:00Z"
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
# Goal: Phase 44: FigJam composite placement and path order

<!-- SPECKIT_TEMPLATE_SOURCE: goal | v2.2 -->
<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Fix the causes the v1.0.9.0 Claude Sonnet 5.5 high rerun found as `sk-create-figjam` v1.0.10.0 with its Claude Project mirror, so a state board draws its first state where the plan reads it first and a flow's plan follows the order readers take, and prove it by rerunning the 6 failures with a working node and two readers per board.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | The composer lays an edge to or from a composite against the zone's inner start, so the first state keeps the top-left place whatever order the model declares its states in. Every existing model keeps its geometry and the Project keeps its room |
| D2 | After the accent and the entry, readers follow a flow's main row in path order. A plan names every node it draws, the main row in path order after the outlined kinds and the entry, and two decisions share a line |
| D3 | On a revision whose changed end holds the planned second glance, every main-row node planned last costs no point when it reads before the changed end |
| D4 | The launcher puts the working nvm node first on PATH, proven by a fixture that prints a `Label:` line |
| D5 | The rerun covers FJ-017, FJ-026, FJ-029, FJ-031, FJ-032 and FJ-036, with FJ-017 graded on the 042 reading of beside |
| D6 | Exact sentence swaps are scripted and byte-checked, DeepSeek V4.1 Flash max on cli-pi through llmgateway makes the code changes, a fresh Opus reviewer verifies the whole diff and GPT 6 Luna max fast on cli-codex is the only fallback |
| D7 | Every skill change reaches its Claude Project file in the same commit, the composer code block included |
| D8 | Each rerun board scenario writes into a fresh draft file in the Barter team plan, each run has its own temp folder and no board URL, file key, plan name or email reaches a committed file |

<!-- /ANCHOR:directive -->

---

<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [x] `compose_board.py --self-test`, `--design-check`, `flow_check.py --self-test`, `pytest scripts/tests`, `run_gates.sh` (all 15 gates) and the output format gate each exit 0 on the committed tree
- [x] `validate_parity.py product-owner` and `residency_check.py --all` each print PASSED after the last commit, and the Flow Board Composer Knowledge code block equals `compose_board.py --template`
- [x] A state model that declares a label line first composes with the first state left of its composite, and every shipped example and board fixture traces to the same geometry
- [x] The path-order glance rule and the wider revision exemption read in the rubric, the playbook and the Project
- [x] `sk-create-figjam` and the hub read 1.0.10.0 with a changelog
- [x] Each of the 6 failures has one graded line in `grades/sonnet-high-044.jsonl`, every board it writes has a render and two reader notes, and the run README names every remaining failure with its cause
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
| Phase 044 closed | Done | rerun 2 of 6 with FJ-032 by operator ruling, README 8.10, ACs Met with AC-006 superseded by ADR-001, validate RESULT: PASSED |

### Deviations and findings

| Item | Note |
|------|------|
| D4 superseded | The launcher's node pin did not reach the model's Bash tool, which rebuilds PATH from the shell profile. ADR-001 replaces it with a Homebrew node reinstall |
| Result | 2 of 6 pass, FJ-032 by the operator's ruling. SC-001 and SC-002 are unmet, and the operator closed testing and sent the findings to the skills |
| None yet | - |
<!-- /ANCHOR:log -->
