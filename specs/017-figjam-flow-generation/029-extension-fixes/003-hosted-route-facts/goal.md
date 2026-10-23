---
title: "Goal: Phase 3: Hosted route facts"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "hosted route facts goal"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "product-owner/017-figjam-flow-generation/029-extension-fixes/003-hosted-route-facts"
    last_updated_at: "2026-10-21T09:30:00Z"
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
# Goal: Phase 3: Hosted route facts

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** The packet gives the true reason the hosted call skips Code Mode and says a desktop-only session has no generate_diagram.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | The change is the phase 016 Section 9 finding, adopted by the operator on 2026-10-21 with all thirteen |
| D2 | A read-only DeepSeek V4.1 Flash worker at max through cli-pi on llmgateway proposes the edits, and the orchestrator applies and checks them |
| D3 | Every changed source with a Project mirror is mirrored by the SYNC.md parity method, and the kernel stays at the unreleased v1.2.2 |

<!-- /ANCHOR:directive -->

---

<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [x] flow-mode.md Section 6 states that Code Mode holds no manual for Figma's hosted server and that the desktop server lacks the write tool
- [x] run_gates.sh prints all gates pass on the final tree
- [x] The format gates and the playbook validators pass on the final tree
- [x] validate.sh --strict on 003-hosted-route-facts prints RESULT: PASSED
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
| Phase opened | Done | 2026-10-21, a child of 029-extension-fixes |
| Change applied | Done | flow-mode.md Section 6 says Code Mode holds no manual for Figma's hosted server here and its figma manual runs Framelink's figma-developer-mcp, that admission of a Code Mode client is unverified, that a desktop-only session has no generate_diagram and falls to the fj route or No route, and that the frontmatter waits for a live session to name the native tool prefix |
| Gates | Done | run_gates.sh all 12 gates pass. The format gate passes on 70 source files with 38 advisory warnings, the baseline count, and reference-parity.cjs is byte-identical. Router fixtures pass 141 of 141, the differential 219 of 219 and check_hub.py 37 gold rows, and the flow_check self-test passes 149 of 149. The playbook validator passes sk-create-figjam with 47 scenarios and 0 violations, and sk-product-owner with 48 scenarios and the baseline 37 warnings. validate_skill_package.py --strict passes on the hub and both packets, and the plugin rebuilds to 370 files and validates. In the scratch clone run_parity passes 62 of 62 pairs and run_residency passes for Product Owner |
| Strict validation | Done | validate.sh --strict on this folder printed RESULT: PASSED |
<!-- /ANCHOR:log -->
