---
title: "Goal: Phase 41: FigJam rerun findings"
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
    packet_pointer: "017-figjam-flow-generation/041-figjam-rerun-findings"
    last_updated_at: "2026-10-26T23:45:00Z"
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
# Goal: Phase 41: FigJam rerun findings

<!-- SPECKIT_TEMPLATE_SOURCE: goal | v2.2 -->
<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Fix the 35 findings of the v1.0.6.0 Claude Sonnet 5.5 high rerun as `sk-create-figjam` v1.0.7.0 with its Claude Project mirror, correct the 040 run records and prove the fixes by rerunning every scenario that did not pass.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | A user asked for one board only when the request says one board, a single board or one diagram. A destination such as on a new board is not that request |
| D2 | DeepSeek V4.1 Flash max on cli-pi through llmgateway makes the edits, Opus agents plan and verify them and GPT 6 Luna max fast on cli-codex is the only fallback |
| D3 | One Opus grader scores every rerun board on one scale, then skeptics and adjudicators check each verdict |
| D4 | Every skill change reaches its Claude Project file in the same commit |
| D5 | Each rerun board scenario writes into a fresh draft file in the Barter team plan with its starting section count recorded. No board URL, file key, plan name or email reaches a committed file |
| D6 | The greyscale outline weights stay, and the glance order they cost is fixed in the planning rules |

<!-- /ANCHOR:directive -->

---

<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [ ] `compose_board.py --self-test`, `--design-check`, `flow_check.py --self-test`, `pytest scripts/tests`, `run_gates.sh` (all 15 gates) and the output format gate each exit 0 on the committed tree
- [ ] `validate_parity.py product-owner` and `residency_check.py --all` each print PASSED after the last commit, and the Flow Board Composer Knowledge code block equals `compose_board.py --template`
- [ ] Each of the 35 findings is fixed in its named file and its Project counterpart, or recorded in the implementation summary with the reason it needed no change
- [ ] `sk-create-figjam` and the hub read 1.0.7.0 and `sk-product-owner` 1.2.4.0, each with a changelog
- [ ] Every scenario that did not pass on the v1.0.6.0 rerun has one graded line in `grades/sonnet-high-041.jsonl`, every board it writes has a full-size render in `renders/` and the run README names every remaining failure with its cause
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
