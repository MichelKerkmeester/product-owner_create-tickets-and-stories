---
title: "Goal: Phase 18: Artifact plus board pair"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "artifact plus board pair goal"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "product-owner/017-figjam-flow-generation/018-artifact-plus-board-pair"
    last_updated_at: "2026-10-20T23:30:00Z"
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
# Goal: Phase 18: Artifact plus board pair

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** A request for an artifact and a FigJam diagram together routes to the artifact with then FLOW, and the diagram follows from it.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | The change is the one phase 016 ranked, adopted by the operator on 2026-10-20 with all twelve |
| D2 | A read-only DeepSeek V4.1 Flash worker at max through cli-pi on llmgateway proposes the edits, and the orchestrator applies and checks them |
| D3 | Every changed source with a Project mirror is mirrored by the SYNC.md parity method, and the kernel stays at the unreleased v1.2.2 |

<!-- /ANCHOR:directive -->

---

<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [x] The router oracle returns STORY with then FLOW for a story plus FigJam flow request, the subject cases stay without then, and the three router copies agree
- [x] run_gates.sh prints all gates pass on the final tree
- [x] The format gates and the playbook validators pass on the final tree
- [x] validate.sh --strict on 018-artifact-plus-board-pair prints RESULT: PASSED
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
| Phase opened | Done | 2026-10-20, a child of 017 |
| Change applied | Done | route_contract.py returns STORY with then FLOW for the story plus FigJam flow request, TASK with no then for a task to make the figjam labels readable and DOC with then FLOW for a runbook with a FigJam process. The router fixtures pass 129 of 129 and the differential 208 of 208, so the three router copies agree. check_hub.py passes 35 gold rows including two new pair rows, and playbook scenario FJ-037 covers it |
| Gates | Done | run_gates.sh all 12 gates pass. Both format gates pass on 70 source files with 38 advisory warnings, the baseline count. reference-parity.cjs byte-identical. The playbook validator passes 47 scenarios with 0 violations and topology 9 of 9. validate_skill_package.py --strict passes on the hub and both packets, leaf-manifest.json is fresh, the plugin rebuilds to 370 skill files and validates. In the scratch clone run_parity passes 62 of 62 pairs and run_residency passes for Product Owner |
| Strict validation | Done | validate.sh --strict on this folder printed RESULT: PASSED |
<!-- /ANCHOR:log -->
