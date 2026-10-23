---
title: "Goal: Product Owner deep review"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "product owner deep review goal"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "product-owner/018-product-owner-deep-review"
    last_updated_at: "2026-10-21T12:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Closed all five review phases"
    next_safe_action: "The operator chooses which findings to fix"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "1004bf13-7863-4447-a63e-6ad2f5fcfd86"
      parent_session_id: null
    completion_pct: 70
    open_questions: []
    answered_questions: []
---
# Goal: Product Owner deep review

<!-- SPECKIT_TEMPLATE_SOURCE: goal | v2.2 -->
<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Deep-review each of Product Owner's four modes and the whole repository, five DeepSeek iterations each, then fix the findings the operator chooses.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | DeepSeek V4.1 Flash at max through cli-pi on llmgateway runs every iteration, with convergence stopping off, as the operator asked on 2026-10-21 |
| D2 | The five runs are independent and run in parallel, each staged outside Product Owner and copied in |
| D3 | Fixes follow the operator's choice, and fixes to a vendored packet go to its upstream skill |

<!-- /ANCHOR:directive -->

---

<!-- ANCHOR:binding -->
## 2. BINDING

**Read the child goal before working a phase.** Each is authoritative for its
phase and binds as if written here.

| Phase | Goal document |
|-------|---------------|
| 001 | `001-sk-product-owner/goal.md` |
| 002 | `002-sk-create-figjam/goal.md` |
| 003 | `003-mcp-click-up/goal.md` |
| 004 | `004-mcp-figma/goal.md` |
| 005 | `005-whole-repo/goal.md` |
| 006 | `006-own-fixes/goal.md` |
| 007 | `007-vendor-sync/goal.md` |

**Precedence.** Decisions above outrank child detail. Child detail outranks any
summary of it. Name a conflict rather than resolving it silently.

**Stop.** Only the criteria below decide done. An evaluator sees the objective
string, not these files.
<!-- /ANCHOR:binding -->

---

<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [x] Every child phase folder has a Phase Documentation Map row and a binding row above
- [x] Each review child's review/ holds five iteration records and a review report
- [x] Every finding the operator chose to fix is fixed or recorded with its reason
- [x] validate.sh --recursive --strict on this folder prints RESULT: PASSED
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
| Packet opened | Done | 2026-10-21 |
| Five lineages | Done | Run in parallel 13:00 to 13:21, 5 iteration records each, fanout exit 0 each |
| Findings | Done | 0 P0, 14 P1, 54 P2. 13 of 14 P1 hold on the cited line |

### Deviations and findings

| Item | Note |
|------|------|
| D3 amendment | On 2026-10-21 the operator chose to fix every finding, upstream included, so D3 moved from review only to fixes following that choice, and phases 006 and 007 were added |
<!-- /ANCHOR:log -->
