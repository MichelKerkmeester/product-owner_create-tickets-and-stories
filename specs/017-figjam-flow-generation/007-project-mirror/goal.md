---
title: "Goal: Phase 7: Claude Project mirror"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "project mirror goal"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "product-owner/017-figjam-flow-generation/007-project-mirror"
    last_updated_at: "2026-10-20T00:00:00Z"
    last_updated_by: "scaffold"
    recent_action: "Authored the durable directive"
    next_safe_action: "Execute against the completion criteria"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "unset"
      parent_session_id: null
    completion_pct: 0
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: goal | v2.2 -->
# Goal: Phase 7: Claude Project mirror

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Bring Flow Mode's Project-applicable rules into the Product Owner Claude Project kernel and knowledge files, with connector-conditional board writing, while every Sync Loop gate stays green.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | Project files are hand-written from the skill sources per SYNC.md. No generated mirror. |
| D2 | mcp-figma is not mirrored into the Project. |

<!-- /ANCHOR:directive -->

---


<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [ ] run_parity.sh, run_receipts.sh, run_residency.sh and run_gates.sh each exit 0
- [x] validate-output-format.cjs --system product-owner passes
- [x] A deliberate rule-span drift makes the parity gate fail
- [x] The kernel names the Flow command and states the connector-conditional write or refusal
- [x] No review sentence is added to SYNC.md until the named human confirms the review
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
| Two Flow Knowledge mirrors and kernel v1.2.2 | Done | claude project/knowledge/, Custom Instructions.md |
| Pairs declared and 8 residency rows resynced | Done | systems.py; other systems' rows unchanged against a backup |
| Parity, residency and the residency report | Done | Scratch clone 2026-10-20, each exit 0, 39/39 pairs |
| run_gates.sh and the format gate | Done | 10 of 10 gates; 44 files |
| Planted rule-span drift | Done | rule_parity.py exit 1 on "at most 4 exits" |
| run_receipts.sh | Blocked | Needs the operator's upload and a dated receipt in SYNC.md |

### Deviations and findings

| Item | Note |
|------|------|
| Kernel bump is a patch step | v1.2.1 to v1.2.2 per the operator's standing rule, against the minor bump SYNC.md and this spec name for a rule change |
| validate_parity.py misses rule text | A planted "4 exits" passed it, so the Flow limits joined rule_parity.py as its seventh rule |
| validate_parity.py skipped unknown count words | It now reads "thirty-nine" and reports an unreadable count word as a finding |
<!-- /ANCHOR:log -->
