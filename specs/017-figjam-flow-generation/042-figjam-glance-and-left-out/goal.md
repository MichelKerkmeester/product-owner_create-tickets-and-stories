---
title: "Goal: Phase 42: FigJam glance plans and Left out"
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
    packet_pointer: "017-figjam-flow-generation/042-figjam-glance-and-left-out"
    last_updated_at: "2026-10-27T08:10:00Z"
    last_updated_by: "claude-code"
    recent_action: "Authored the durable directive"
    next_safe_action: "Execute against the completion criteria"
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
# Goal: Phase 42: FigJam glance plans and Left out

<!-- SPECKIT_TEMPLATE_SOURCE: goal | v2.2 -->
<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Fix the gaps the v1.0.7.0 Claude Sonnet 5.5 high rerun still shows as `sk-create-figjam` v1.0.8.0 with its Claude Project mirror, so glance plans match the drawn board and every omission is named, and prove it by rerunning the 14 failures.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | With no state named, a state board plans its first state first, and the composite reads as part of the frame like the title block. The composer stays unchanged |
| D2 | FJ-045's signals change to a light green goal that is not pink and a first glance on the accented node. The rubric's accent candidates stay |
| D3 | A `Left out:` line appears in the reply and the gate whenever the board does not hold something named: a cut, a split or a later board |
| D4 | FJ-017 passes or fails on its own signals with no scorecard |
| D5 | Exact sentence swaps are scripted and byte-checked, DeepSeek V4.1 Flash max on cli-pi through llmgateway makes the code changes one per brief, a fresh Opus reviewer verifies the whole diff and GPT 6 Luna max fast on cli-codex is the only fallback |
| D6 | Every skill change reaches its Claude Project file in the same commit |
| D7 | Each rerun board scenario writes into a fresh draft file in the Barter team plan with its starting section count recorded. No board URL, file key, plan name or email reaches a committed file |

<!-- /ANCHOR:directive -->

---

<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [ ] `compose_board.py --self-test`, `--design-check`, `flow_check.py --self-test`, `pytest scripts/tests`, `run_gates.sh` (all 15 gates) and the output format gate each exit 0 on the committed tree
- [ ] `validate_parity.py product-owner` and `residency_check.py --all` each print PASSED after the last commit, and the Flow Board Composer Knowledge code block equals `compose_board.py --template`
- [ ] Each finding and critic gap of the v1.0.7.0 rerun is fixed in its named file and its Project counterpart, or recorded in the implementation summary with the reason it needed no change
- [ ] `sk-create-figjam` and the hub read 1.0.8.0 with a changelog and the kernel reads v1.2.10
- [ ] Each of the 14 failures has one graded line in `grades/sonnet-high-042.jsonl`, every board it writes has a full-size render in `renders/` and the run README names every remaining failure with its cause
- [ ] `validate.sh --strict` on this phase prints RESULT: PASSED, and both repositories are pushed with `git status --short` empty in Product Owner
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

### Deviations and findings

| Item | Note |
|------|------|
| None yet | - |
<!-- /ANCHOR:log -->
