---
title: "Goal: Phase 12: Vendored ClickUp packet"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "vendored clickup goal"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "product-owner/017-figjam-flow-generation/012-vendored-clickup"
    last_updated_at: "2026-10-20T14:30:00Z"
    last_updated_by: "scaffold"
    recent_action: "Authored the durable directive"
    next_safe_action: "Execute against the completion criteria"
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
# Goal: Phase 12: Vendored ClickUp packet

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Vendor the mcp-click-up skill into the Product Owner hub as a byte copy that vendor-sync.py keeps in step with .skilled, registered as a tool packet the hub routes to.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | The copy is real files, not a symlink, under the upstream folder name mcp-click-up, on the operator's choice of 2026-10-20 |
| D2 | Bare clickup is no stage one signal, because Product Owner writes ClickUp-native artifacts |
| D3 | Nothing inside mcp-click-up/ is edited here. A change goes upstream through push |

<!-- /ANCHOR:directive -->

---


<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [x] vendor-sync.py status reports mcp-click-up in step with 0 files differing
- [x] check_hub.py replays the ClickUp gold rows and passes
- [x] run_gates.sh prints all 10 gates pass
- [x] validate.sh --strict on 012-vendored-clickup prints RESULT: PASSED
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
| Vendored | Done | 178 files at 325ebb22, diff -rq clean, 0 symlinks, status in step |
| Hub | Done | Registry row, signals mcp-click-up, cupt and clickup mcp, five gold rows pass |
| Plugin | Done | Shipped among 292 files, claude plugin validate passed |

### Deviations and findings

| Item | Note |
|------|------|
| Product Owner's ClickUp table disagrees with the vendored contract | Product Owner names `markdown_content` for a task update. The vendored skill says the ClickUp MCP takes `markdown_description` for create and update. The operator ruled the vendored skill the truth, so `SKILL.md`, `AGENTS.md`, both READMEs, the Project README and the kernel read-back line now follow it, with the kernel statement resynced. Scratch clone parity 39/39, residency and the residency report pass |
<!-- /ANCHOR:log -->
