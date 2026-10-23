---
title: "Goal: Phase 29: Extension fixes"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "extension fixes goal"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "product-owner/017-figjam-flow-generation/029-extension-fixes"
    last_updated_at: "2026-10-21T08:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Closed all twelve child phases"
    next_safe_action: "The operator gives the commit go-ahead"
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
# Goal: Phase 29: Extension fixes

<!-- SPECKIT_TEMPLATE_SOURCE: goal | v2.2 -->
<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Apply the thirteen findings of phase 016 Section 9 to Product Owner, one child phase per finding, so the shipped FigJam changes hold and the five new ones land.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | The operator adopted all thirteen findings on 2026-10-21, and the two router findings share one child |
| D2 | Read-only DeepSeek V4.1 Flash workers at max through cli-pi on llmgateway propose the edits in parallel, and the orchestrator applies and checks them |
| D3 | Changed sources are mirrored by the SYNC.md parity method, and the kernel stays at the unreleased v1.2.2 |
| D4 | The Flow reply keeps the lines parent D6 lists. A re-save is reported inside the read-back line |

<!-- /ANCHOR:directive -->

---

<!-- ANCHOR:binding -->
## 2. BINDING

**Read the child goal before working a phase.** Each is authoritative for its
phase and binds as if written here.

| Phase | Goal document |
|-------|---------------|
| 001 | `001-board-link-resave/goal.md` |
| 002 | `002-pair-phrasing-and-framing/goal.md` |
| 003 | `003-hosted-route-facts/goal.md` |
| 004 | `004-critic-pass-source/goal.md` |
| 005 | `005-tag-key-and-set/goal.md` |
| 006 | `006-delivery-pointer-lines/goal.md` |
| 007 | `007-revision-plan/goal.md` |
| 008 | `008-dangling-connectors/goal.md` |
| 009 | `009-pair-reply-ending/goal.md` |
| 010 | `010-repeated-label-check/goal.md` |
| 011 | `011-read-call-allowance/goal.md` |
| 012 | `012-er-cardinality-caps/goal.md` |

**Precedence.** Decisions above outrank child detail. Child detail outranks any
summary of it. Name a conflict rather than resolving it silently.

**Stop.** Only the criteria below decide done. An evaluator sees the objective
string, not these files.
<!-- /ANCHOR:binding -->

---

<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [x] Every child phase folder has a Phase Documentation Map row and a binding row above
- [x] The router oracle forms the pair for each phrasing in 016 Section 9 rank 2 and frames write a doc and write a bug
- [x] run_gates.sh, the format gates, the playbook validators and the Sync Loop gates pass on the final tree
- [x] validate.sh --recursive --strict on the top parent prints RESULT: PASSED
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
| Phase parent opened | Done | 2026-10-21, a child of 017, split out because the top parent goal sat at 3,998 of 4,000 characters |
| Workers | Done | 12 DeepSeek V4.1 Flash max workers through cli-pi on llmgateway, run in parallel. 10 returned edits on the first attempt and 2 on the second |
| Review and apply | Done | 3 worker edits skipped as unclear, overclaimed or colliding, and the colliding kernel sentence merged by hand |
| Router | Done | The oracle forms the pair for all six Section 9 rank 2 phrasings and frames write a doc and write a bug. Fixtures 141 of 141, differential 219 of 219, check_hub.py 37 gold rows |
| Gates | Done | run_gates.sh 12 of 12, format gate 38 advisories as at baseline, both playbook validators pass, plugin rebuilds and validates, run_parity 62 of 62 and run_residency pass in the scratch clone |
| Child phases | Done | All twelve closed with every acceptance row Met |
<!-- /ANCHOR:log -->
