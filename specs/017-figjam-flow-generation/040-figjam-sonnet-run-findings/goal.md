---
title: "Goal: Phase 40: FigJam Sonnet run findings"
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
    packet_pointer: "017-figjam-flow-generation/040-figjam-sonnet-run-findings"
    last_updated_at: "2026-10-26T18:55:00Z"
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
# Goal: Phase 40: FigJam Sonnet run findings

<!-- SPECKIT_TEMPLATE_SOURCE: goal | v2.2 -->
<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Ship the fixes the 54-scenario Claude Sonnet 5.5 high run found as `sk-create-figjam` v1.0.6.0 with its Claude Project mirror, refresh the skill's screenshots and docs from boards the new composer draws and prove the fixes by rerunning the 29 failed and 2 skipped scenarios.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | No rerun starts before 23:00 Amsterdam time (22:00 UTC) on 2026-10-26 |
| D2 | DeepSeek V4.1 Flash max on cli-pi through llmgateway makes the edits, Opus agents plan and verify them and GPT 6 Luna max fast on cli-codex is the only fallback |
| D3 | One Opus grader scores every rerun board on one scale, then skeptics and adjudicators check each verdict, as `grades/grader-brief-039.md` sets out |
| D4 | Every skill change reaches its Claude Project file in the same commit. The shared Human Voice card in `z — Knowledge` changes only on the operator's yes |
| D5 | Reruns run in parallel lanes, each writing into its own FigJam file in drafts of the Barter team plan. No board URL, file key, plan name or email reaches a committed file |

<!-- /ANCHOR:directive -->

---

<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [ ] `compose_board.py --self-test`, `flow_check.py --self-test`, `pytest scripts/tests`, `run_gates.sh` (all 15 gates) and the output format gate each exit 0 on the committed tree
- [ ] `validate_parity.py product-owner` and `residency_check.py product-owner` each print PASSED after the last commit
- [ ] `sk-create-figjam` and the hub read version 1.0.6.0 with v1.0.6.0 changelogs, and the Flow Board Composer Knowledge code block equals `compose_board.py --template` byte for byte
- [ ] Every board the rerun writes has a 100% render in the run's `renders/` folder, and `sk-create-figjam/assets/screenshots/` holds the best v1.0.6.0 board of each of the seven diagram types with a caption naming its scenario, model and score
- [ ] Every `sk-create-figjam` README, reference, template and example that states a rule, count, size or image the fixes changed says what v1.0.6.0 does, and the implementation summary lists each file checked
- [ ] `grades/sonnet-high-rerun.jsonl` holds one graded line for each of the 31 rerun scenarios, and the earliest rerun turn in `run-log.jsonl` is at or after 22:00 UTC on 2026-10-26
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
| 54-scenario run graded and adjudicated | Done | 23 PASS, 29 FAIL, 2 SKIP after skeptics and adjudicators |
| Fix lanes for skill, playbook, driver and records | Done | Four lanes report all 15 gates passing |
| Design and composer lane, Project mirror and review | In Progress | Implementation workflow running |
| Rerun of the 31 failed and skipped scenarios | Pending | Held until 22:00 UTC by D1 |
| Fixes, mirror, review repairs and leftover handoffs | Done | 1,240 and 163 self-test checks, all 15 gates and the format gate exit 0, 040 validates PASSED |
| Shared Human Voice card and FJ-027 rescore | Done | operator yes, 12 copies one md5, kernel v1.2.8, 7 systems parity PASSED, record 24 PASS 28 FAIL 2 SKIP |

### Deviations and findings

| Item | Note |
|------|------|
| Shared Human Voice card | `hvr-core.md` is a byte copy of a `z — Knowledge` file five systems share, so its wording fix waits for the operator's yes under D4 |
<!-- /ANCHOR:log -->
