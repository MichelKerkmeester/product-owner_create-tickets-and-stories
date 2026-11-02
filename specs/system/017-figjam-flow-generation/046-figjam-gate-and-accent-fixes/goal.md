---
title: "Goal: Phase 46: FigJam gate and accent fixes"
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
    packet_pointer: "017-figjam-flow-generation/046-figjam-gate-and-accent-fixes"
    last_updated_at: "2026-10-27T22:30:00Z"
    last_updated_by: "claude-code"
    recent_action: "Scaffolded the phase"
    next_safe_action: "Review the diff and commit"
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
# Goal: Phase 46: FigJam gate and accent fixes

<!-- SPECKIT_TEMPLATE_SOURCE: goal | v2.2 -->
<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Fix the causes the v1.0.11.0 Claude Sonnet 5.5 high rerun found as `sk-create-figjam` v1.0.12.0 with its Claude Project mirror in the same commits, so the gate sees where each note lands, the goal never takes the accent, every stop ends on its question and the gate shows its sketch and critique, then rerun FJ-017, FJ-036, FJ-022 and FJ-023 and refresh the gallery.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | A `%% notes:` line moves the key down, `flow_check.py --notes` prints each noted node's side and the gate names it or offers pins or a model change |
| D2 | The goal never takes the accent. A `%% goal:` line names it, and the accent goes to a decision, a failure end or the step in focus |
| D3 | All nine shipped flows that accented their goal are re-accented, with their mirrors and the extension and revision rules |
| D4 | An intake round, the playback and the gate end on their question with no self-scan line |
| D5 | A group the request names as one, such as the end states, reads as a set whose member order is not scored |
| D6 | The gate always shows the sketch with the check result and answers four named critique questions unless the user settled them |
| D7 | The label trace reads at the normal and the narrow measure |
| D8 | Sentence swaps are scripted and byte-checked, every skill change reaches its Project file in the same commit and a fresh Opus reviewer reads the whole diff |

<!-- /ANCHOR:directive -->

---

<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [ ] `compose_board.py --self-test`, `--design-check`, `flow_check.py --self-test`, `pytest scripts/tests`, `run_gates.sh` (all 15 gates) and the output format gate each exit 0 on the committed tree
- [ ] `validate_parity.py product-owner`, `residency_check.py --all` and `pair_divergence.py product-owner` each print PASSED after the last commit
- [ ] The notes, goal, stop, gate and end-state rules read the same in the skill and the Project
- [ ] No source lets the goal take the accent, and every shipped flow model names its goal
- [ ] `sk-create-figjam` and the hub read 1.0.12.0 with a changelog
- [ ] FJ-017, FJ-036, FJ-022 and FJ-023 are rerun and graded on v1.0.12.0, recorded as README section 8.12, with the gallery refreshed
- [ ] `validate.sh --strict` on this phase prints RESULT: PASSED, and both repositories are pushed
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
| Release v1.0.12.0 committed and pushed | Done | PO 7ed6e7d5 and 7d10f39e, outer 2169cd312 and f5d8f2360, parity PASSED 65 of 65 |
| Rerun on v1.0.12.0 graded | Done | 0 of 4 pass, run README section 8.12, causes go to phase 047 |

### Deviations and findings

| Item | Note |
|------|------|
<!-- /ANCHOR:log -->
