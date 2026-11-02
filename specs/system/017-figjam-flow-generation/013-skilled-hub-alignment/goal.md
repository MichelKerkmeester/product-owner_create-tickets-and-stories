---
title: "Goal: Phase 13: Skilled hub alignment"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "skilled hub alignment goal"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "product-owner/017-figjam-flow-generation/013-skilled-hub-alignment"
    last_updated_at: "2026-10-20T18:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Met every completion criterion"
    next_safe_action: "Commit both repositories on the operator's go-ahead"
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
# Goal: Phase 13: Skilled hub alignment

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Rebuild the Product Owner hub on the skilled parent-hub contract in a product-owner/ folder, so the skilled checker and validator pass it with no exemption and it routes the way every skilled hub routes.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | The hub lives in product-owner/ at the repository root, on the operator's choice of 2026-10-20. Repository files stay at the root |
| D2 | Stage two lives in the hub root ROUTER.md, and each workflow packet routes inside its own SKILL.md Section 2, as skilled packets do |
| D3 | The Product Owner stage one rules stay, declared as a routing policy beside the canonical hub-router schema |
| D4 | Nothing inside mcp-figma/ or mcp-click-up/ is edited, and the kernel router code stays equal to router-contract.md |

<!-- /ANCHOR:directive -->

---


<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [x] parent-skill-check.cjs on product-owner/ prints 0 failures
- [x] validate_skill_package.py --strict passes on product-owner/, sk-product-owner and sk-create-figjam
- [x] run_gates.sh prints all gates pass and the hub check replays every gold row
- [x] The plugin build, the playbook validator and the Sync Loop parity and residency gates pass
- [x] validate.sh --strict on 013-skilled-hub-alignment prints RESULT: PASSED
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
| Phase opened | Done | 2026-10-20, baseline parent-skill-check 39 failures, packet validator FAIL on both workflow packets |
| Hub moved and checked | Done | 2026-10-20, parent-skill-check 0 failures and 0 warnings, validate_skill_package --strict PASS on the hub and four packets |
| Gates | Done | run_gates.sh all 12 pass, playbook 48 scenarios 0 violations, plugin validates, scratch clone run_parity.sh 39 of 39 and run_residency.sh pass |
<!-- /ANCHOR:log -->
