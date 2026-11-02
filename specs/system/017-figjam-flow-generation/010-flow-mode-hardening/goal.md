---
title: "Goal: Phase 10: Flow Mode hardening"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "flow mode hardening goal"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "product-owner/017-figjam-flow-generation/010-flow-mode-hardening"
    last_updated_at: "2026-10-20T09:38:56Z"
    last_updated_by: "scaffold"
    recent_action: "Authored the durable directive"
    next_safe_action: "Execute against the completion criteria"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "1004bf13-7863-4447-a63e-6ad2f5fcfd86"
      parent_session_id: null
    completion_pct: 0
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: goal | v2.2 -->
# Goal: Phase 10: Flow Mode hardening

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Apply the 15 changes the phase 9 research ranked, so Flow Mode writes to a FigJam file instead of a page, refuses models the board generator rejects, and proves which nodes each connector joins.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | All 15 ranked changes apply, on the operator's choice of 2026-10-20 |
| D2 | A flow runs top to bottom by default or left to right, one direction per flow, on the operator's choice of 2026-10-20, with the reason for the default written down |
| D3 | The kernel stays at the unreleased v1.2.2, because unshipped work folds into the pending version |
| D4 | The label cap is 40 characters, above the longest label in the shipped patterns and the Change Location model |
| D5 | A fill and its paired darker stroke are one accent, and rule_parity.py holds the new model rules on both sides |

<!-- /ANCHOR:directive -->

---


<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [x] flow_check.py --self-test passes 35 of 35, each planted model failing with its own message
- [x] flow_check.py passes flow-templates.md and the Change Location model
- [x] A search of flow-mode.md, both Flow Knowledge files and the kernel finds no write that targets or clears a page
- [x] run_gates.sh prints all 10 gates pass, and rule_parity.py holds 8 rules
- [x] run_parity.sh and run_residency.sh exit 0 in a scratch clone with the work committed
- [x] validate.sh --strict on 010-flow-mode-hardening prints RESULT: PASSED
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
| Phase opened | Done | 2026-10-20 |
| Check script | Done | 8 new conditions, 9 planted models, self-test 17 of 17 |
| Skill, templates, mirror and kernel | Done | Page target replaced, rule list and recovery updated |
| Shipped models | Done | flow-templates.md 6 diagrams and the Change Location model pass |
| run_gates.sh and format gate | Done | 10 of 10 gates, 44 files |
| Second pass | Done | Left to right, one direction per flow, paired-stroke accent, rule_parity.py rule 8 with a planted drift that failed it. Self-test 20 of 20 |
| Sync Loop | Done | Two statements resynced, scratch clone: parity 39/39, residency pass, residency report pass, receipts fails only on the missing upload receipt |
| Third pass, 21 review findings | Done | Self-test 35 of 35 with messages asserted and both template files checked, three statements resynced, playbook pair SFL-001 and PFL-001, gates 10 of 10, scratch clone parity 39/39 and residency pass |
| Playbook citations | Done | 553 line citations checked against the cited text. 46 kernel citations remapped after the Flow lines shifted the kernel, plus Task Mode 133 and 111, the Mobile Crash example 68 and the clarification rule's Flow exception. Validator 48 scenarios, 0 violations |

### Deviations and findings

| Item | Note |
|------|------|
| The fj rollback dropped its page duplicate | The research left it unverified, but duplicating a page creates one, which a FigJam file cannot hold. Kept would contradict the new gate |
| The completion criterion moved from 20 of 20 to 35 of 35 | The fresh review added planted models, so the count rose. Every row still has to pass |
| The markup check stopped scanning cleaned labels for angle brackets | The extractor strips tags before the check sees a label, so those marks could never fire. The raw block is scanned instead |
<!-- /ANCHOR:log -->
