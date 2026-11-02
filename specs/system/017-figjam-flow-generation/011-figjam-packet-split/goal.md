---
title: "Goal: Phase 11: FigJam packet split"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "figjam packet split goal"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "product-owner/017-figjam-flow-generation/011-figjam-packet-split"
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
# Goal: Phase 11: FigJam packet split

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Move Flow Mode out of sk-product-owner into its own hub packet, sk-create-figjam, which the hub picks at stage one, with no change to Flow behavior or the Claude Project kernel.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | The packet is named sk-create-figjam, on the operator's choice of 2026-10-20 |
| D2 | The hub routes $flow, $figjam and FigJam requests to the packet at stage one, and a Flow route reaching the Product Owner router hands off to it |
| D3 | The packet reads the Human Voice cards from sk-product-owner/references/ and copies none |
| D4 | The kernel router code is unchanged, so its FLOW lane strings stay and only comments explain where the files live |

<!-- /ANCHOR:directive -->

---


<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [x] No Flow file remains under sk-product-owner/, and a search of the repository outside specs/ finds no old Flow path
- [x] check_hub.py passes with the sk-create-figjam row and its gold rows, and its self-test fails on every planted defect
- [x] run_gates.sh prints all 10 gates pass and differential.py passes every input
- [x] run_parity.sh and run_residency.sh exit 0 in a scratch clone with the work committed
- [x] validate.sh --strict on 011-figjam-packet-split prints RESULT: PASSED
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
| Move and packet files | Done | Four files moved, SKILL.md, ROUTER.md, README.md and changelog written, flow_check.py self-test 35 of 35 from the new path |
| Hub routing | Done | check_hub.py 4 packets and 24 gold rows, self-test 11 of 11 |
| Readers | Done | Fixtures 123 of 123, differential 201 of 201, format gate 47 files, reference parity byte-identical, playbook 48 scenarios and 0 violations with 29 citations remapped |
| Sync Loop | Done | Scratch clone: run_parity.sh 39/39 with 40 sources, run_residency.sh pass, five proof scripts exit 0, receipts fails only on the missing upload receipt |
| DeepSeek review | Done | Three read-only batches on DeepSeek V4.1 Flash max, 23 findings, 17 confirmed and fixed, 6 rejected after a check |

### Deviations and findings

| Item | Note |
|------|------|
| The Doc Mode ClickUp line stayed on `mcp-tooling` | Any edit there is a Project-visible change that parity holds for a human review, and the name is still accurate |
| A seventh hub rule, the opening signal | ClickUp operations name tasks and docs, so the artifact-word rule alone kept `cupt list my open tasks` in Product Owner |
| The shared Sync Loop gained `extra_skill_dirs` | Without it the inventory stopped at the skill folder and a new packet file would never be flagged as unmirrored |
| Two rejected review findings | The vendor gate was not skipped, its run printed ok. The opening-signal rule steals no bug report the signal rule did not already send to the tool packet |
<!-- /ANCHOR:log -->
