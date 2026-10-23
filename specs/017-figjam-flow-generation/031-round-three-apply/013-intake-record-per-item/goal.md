---
title: "Goal: Phase 13: Keep one intake record per item, with a class and a confidence"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "intake record per item goal"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "product-owner/017-figjam-flow-generation/031-round-three-apply/013-intake-record-per-item"
    last_updated_at: "2026-10-21T10:30:00Z"
    last_updated_by: "claude-code"
    recent_action: "Applied the change and closed the phase"
    next_safe_action: "None, the phase is closed"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "1004bf13-7863-4447-a63e-6ad2f5fcfd86"
      parent_session_id: null
    completion_pct: 100
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: goal | v2.2 -->
# Goal: Phase 13: Keep one intake record per item, with a class and a confidence

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Keep one intake record per item, with a class and a confidence.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | The change is input to model logic rank 2 from phase 030, adopted by the operator on 2026-10-21 with all 32 |
| D2 | A read-only DeepSeek V4.1 Flash worker at max through cli-pi on llmgateway proposes the edits, and the orchestrator applies and checks them |
| D3 | Every changed source with a Project mirror is mirrored by the SYNC.md parity method, and the kernel stays at the unreleased v1.2.2 |

<!-- /ANCHOR:directive -->

---

<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [x] The change from the input to model logic rank 2 synthesis is in place: the intake produces one row per item before any Mermaid, carrying kind, source, class, confidence and the rung that produced it. The table gains a confidence column and an edge row whenever the edge was inferred. A frame name and the visible heading both land in the row, the heading labels the node and a disagreement is recorded rather than resolved
- [x] run_gates.sh prints all gates pass on the final tree
- [x] The format gates and the playbook validators pass on the final tree
- [x] validate.sh --strict on 013-intake-record-per-item prints RESULT: PASSED
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
| Phase opened | Done | 2026-10-21, a child of 031-round-three-apply |
| Change applied | Done | Applied to sk-create-figjam/references/flow-mode.md, sk-create-figjam/assets/flow-templates.md: the intake produces one row per item before any Mermaid, carrying kind, source, class, confidence and the rung that produced it. The table gains a confidence column and an edge row whenever the edge was inferred. A frame name and the visible heading both land in the row, the heading labels the node and a disagreement is recorded rather than resolved |
| Gates | Done | On the final tree run_gates.sh printed all 12 gates pass, the format gate passed across 70 source files at the 38 baseline advisories, reference parity was byte-identical, the playbooks passed at 51 scenarios with 0 warnings and 48 scenarios at the 37 baseline warnings, the topology check passed, the three skill packages validated, the plugin rebuilt to 375 files and validates, the flow_check self-test passed 154 of 154, the router passed 141 of 141 fixtures and 219 of 219 differential inputs, check_hub passed 37 gold rows, and in the scratch clone the Sync Loop parity passed 62 of 62 and Product Owner residency passed |
| Strict validation | Done | validate.sh --strict on this folder printed RESULT: PASSED |
<!-- /ANCHOR:log -->
