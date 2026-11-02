---
title: "Goal: Phase 32: Local ClickUp push targets with a private doc option"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "clickup push targets goal"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "product-owner/017-figjam-flow-generation/032-clickup-push-targets"
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
# Goal: Phase 32: Local ClickUp push targets with a private doc option

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** A ClickUp push goes to the link the operator set locally for that artifact kind, or asks where when none is set, and always offers a private doc.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | Links stay local: a gitignored `.env` or the shell, one link per artifact kind, with a tracked `.env.example` holding empty keys |
| D2 | With a link set the offer names it and adds a private doc. With none it asks where, recommending a private doc. The kernel always asks |
| D3 | Every changed source with a Project mirror is mirrored by the SYNC.md parity method, and the kernel stays at the unreleased v1.2.2 |

<!-- /ANCHOR:directive -->

---

<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [x] The push targets live in a gitignored `.env` or the shell, with a tracked `.env.example`, one link per artifact kind. With a link set the offer names it and adds a private doc option, and with none set it asks where and recommends a private doc. The claude.ai kernel always asks
- [x] run_gates.sh prints all gates pass on the final tree
- [x] The format gates and the playbook validators pass on the final tree
- [x] validate.sh --strict on 032-clickup-push-targets prints RESULT: PASSED
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
| Phase opened | Done | 2026-10-21, a child of 017 on the operator's choice |
| Change applied | Done | AGENTS.md ClickUp Handoff, sk-product-owner/SKILL.md Section 7 Push Targets and interactive-response-templates.md Section 3 read one link per artifact kind from the shell and then the gitignored .env, offer that link with a private ClickUp doc when it is set, and ask where with a private doc recommended when it is not. The Knowledge mirror and the kernel always ask, because a Project cannot read a local file. example_lint.py accepts the two new closing lines, README.md documents the setup, and the playbook gained STK-007 and PTK-007 |
| Gates | Done | On the final tree run_gates.sh printed all 12 gates pass, the format gate passed across 70 source files at the 38 baseline advisories, reference parity was byte-identical, the sk-product-owner playbook passed at 50 scenarios with 39 warnings, the two new ones the same sandbox context path as the 37 before, the two skill packages validated, the plugin rebuilt to 375 files and validates, and in the scratch clone the Sync Loop parity passed 62 of 62 and Product Owner residency passed |
| Strict validation | Done | validate.sh --strict on this folder printed RESULT: PASSED |
<!-- /ANCHOR:log -->
