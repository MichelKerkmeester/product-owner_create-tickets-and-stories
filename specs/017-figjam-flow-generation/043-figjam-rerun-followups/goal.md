---
title: "Goal: Phase 43: FigJam rerun follow-ups"
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
    packet_pointer: "017-figjam-flow-generation/043-figjam-rerun-followups"
    last_updated_at: "2026-10-27T12:40:00Z"
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
# Goal: Phase 43: FigJam rerun follow-ups

<!-- SPECKIT_TEMPLATE_SOURCE: goal | v2.2 -->
<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Fix the gaps the v1.0.8.0 Claude Sonnet 5.5 high rerun still shows as `sk-create-figjam` v1.0.9.0 with its Claude Project mirror, so a composite's inner states, a split, a revision, the reply's first line, adjacent stickies and a missing route each follow one rule, and prove it by rerunning the 7 failures with two readers per board.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | With no state named, a state board plans its first state first, the states inside a composite second with their section and the end states last. With a state named, the focus line marks it first |
| D2 | The 56 pixel rule holds on the composer's path estimate, FigJam may draw an elbow closer and graders do not count it. The composer is not changed |
| D3 | Two fresh readers per scored board, and a Composition point is lost only when both read an unplanned part early |
| D4 | The rerun covers FJ-009, FJ-017, FJ-026, FJ-029, FJ-031, FJ-032 and FJ-036 |
| D5 | Lanes and zones read as frame on every type, like the title block |
| D6 | Exact sentence swaps are scripted and byte-checked, DeepSeek V4.1 Flash max on cli-pi through llmgateway makes the code change, a fresh Opus reviewer verifies the whole diff and GPT 6 Luna max fast on cli-codex is the only fallback |
| D7 | Every skill change reaches its Claude Project file in the same commit |
| D8 | Each rerun board scenario writes into a fresh draft file in the Barter team plan, each run has its own temp folder and no board URL, file key, plan name or email reaches a committed file |

<!-- /ANCHOR:directive -->

---

<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [ ] `compose_board.py --self-test`, `--design-check`, `flow_check.py --self-test`, `pytest scripts/tests`, `run_gates.sh` (all 15 gates) and the output format gate each exit 0 on the committed tree
- [ ] `validate_parity.py product-owner` and `residency_check.py --all` each print PASSED after the last commit, and the Flow Board Composer Knowledge code block equals `compose_board.py --template`
- [ ] Each finding and critic gap of the v1.0.8.0 rerun is fixed in its named file and its Project counterpart, or recorded in the implementation summary with the reason it needed no change
- [ ] `sk-create-figjam` and the hub read 1.0.9.0 with a changelog, and the kernel H1 matches its rules
- [ ] Each of the 7 failures has one graded line in `grades/sonnet-high-043.jsonl`, every board it writes has a full-size render in `renders/` and two reader notes, and the run README names every remaining failure with its cause
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
| Phase 043 closed | done | v1.0.9.0 shipped, rerun 1 of 7 PASS, SC-001 unmet and carried to 044, validate PASSED |

### Deviations and findings

| Item | Note |
|------|------|
| None yet | - |
<!-- /ANCHOR:log -->
