---
title: "Goal: Phase 31: Round three apply"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "round three apply goal"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "product-owner/017-figjam-flow-generation/031-round-three-apply"
    last_updated_at: "2026-10-21T10:30:00Z"
    last_updated_by: "claude-code"
    recent_action: "Applied all 32 changes and closed every child"
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
# Goal: Phase 31: Round three apply

<!-- SPECKIT_TEMPLATE_SOURCE: goal | v2.2 -->
<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Apply the 32 ranked changes of phase 030 to Product Owner, one child phase per change, so both packets run an interactive intake, read inputs into a model by a stated method and compose better FigJam boards.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | The operator adopted all 32 on 2026-10-21. Waves run intake, then input logic, then design output |
| D2 | DeepSeek V4.1 Flash max workers through cli-pi on llmgateway propose the edits in parallel within a wave, and the orchestrator applies and checks them |
| D3 | Changed sources are mirrored by the SYNC.md parity method, and the kernel stays at the unreleased v1.2.2 |
| D4 | Every question either packet asks states the AI's reading of the input and its recommended answer. An unanswered question is never a dead end: the AI proceeds on its recommendation, marks it assumed and names it in the playback before the gate. This outranks the research's rule that reader and question are never assumed |

<!-- /ANCHOR:directive -->

---

<!-- ANCHOR:binding -->
## 2. BINDING

**Read the child goal before working a phase.** Each is authoritative for its
phase and binds as if written here.

| Phase | Goal document |
|-------|---------------|
| 001 | `001-intake-brief/goal.md` |
| 002 | `002-draw-ready-stop-rule/goal.md` |
| 003 | `003-question-bank/goal.md` |
| 004 | `004-sparring-outline-pass/goal.md` |
| 005 | `005-playback-and-gate-line/goal.md` |
| 006 | `006-challenge-ladder/goal.md` |
| 007 | `007-po-lane-board-block/goal.md` |
| 008 | `008-quick-and-just-do-it/goal.md` |
| 009 | `009-kernel-carries-loop/goal.md` |
| 010 | `010-intake-in-always-and-router/goal.md` |
| 011 | `011-intake-test-contract/goal.md` |
| 012 | `012-reaction-graph-first/goal.md` |
| 013 | `013-intake-record-per-item/goal.md` |
| 014 | `014-verify-image-labels/goal.md` |
| 015 | `015-inference-ladder/goal.md` |
| 016 | `016-screen-or-state/goal.md` |
| 017 | `017-criterion-as-triple/goal.md` |
| 018 | `018-edge-actor/goal.md` |
| 019 | `019-source-evidence-limits/goal.md` |
| 020 | `020-type-against-needs-row/goal.md` |
| 021 | `021-contradicted-item-surface/goal.md` |
| 022 | `022-chunk-allocation/goal.md` |
| 023 | `023-pre-gate-reread/goal.md` |
| 024 | `024-first-glance/goal.md` |
| 025 | `025-visible-titles/goal.md` |
| 026 | `026-spacing-scale/goal.md` |
| 027 | `027-multi-diagram-board/goal.md` |
| 028 | `028-better-mermaid-lane-order/goal.md` |
| 029 | `029-legend-as-key/goal.md` |
| 030 | `030-reading-distance-dial/goal.md` |
| 031 | `031-pre-write-layout-check/goal.md` |
| 032 | `032-composition-scorecard/goal.md` |

**Precedence.** Decisions above outrank child detail. Child detail outranks any
summary of it. Name a conflict rather than resolving it silently.

**Stop.** Only the criteria below decide done. An evaluator sees the objective
string, not these files.
<!-- /ANCHOR:binding -->

---

<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [x] Every child phase folder has a Phase Documentation Map row and a binding row above
- [x] flow-mode.md and interactive-mode.md carry a question rule that states the AI's reading and recommendation and never stops on an unanswered question
- [x] run_gates.sh, the format gates, the playbook validators and the Sync Loop gates pass on the final tree
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
| Phase parent opened | Done | 2026-10-21, a child of 017. D4 records the operator's two rules sent during setup: always give a reading and a recommendation, and never stop on an unanswered question |
| Three waves applied | Done | 2026-10-21, 32 DeepSeek V4.1 Flash max workers on cli-pi, every edit set reviewed against D4 and applied, with colliding and refused edits merged by hand |
| Gates | Done | run_gates.sh 12 of 12, format gate at 38 baseline advisories, playbooks 51 and 48 scenarios, plugin 375 files, self-test 154 of 154, router 141 of 141, differential 219 of 219, Sync Loop parity 62 of 62 and Product Owner residency in the scratch clone |

### Deviations and findings

| Item | Note |
|------|------|
| Type order | Rank 6 of the intake synthesis put the type before the Brief and ranks 9 and 10 put the Brief before the type. The Brief's first round, the reader, the question and the outcome, now runs before the type and the later rounds ask what that type needs, in flow-mode.md, SKILL.md and the kernel alike |
| No new reply line | Rank 4 of the design synthesis added a Start here line. Parent D6 freezes the reply lines, so the zone to open first and the first glance are clauses of the read-back line |
| D4 gaps fixed in review | Workers 006, 017, 019 and 021 wrote questions with no reading or recommendation or an Unknown trigger with no recommended trigger, and each was fixed before it was applied |
| Kernel version | SYNC.md would bump the kernel to v1.3.0 for a moved rule. Releases move by patch steps only, so the kernel stays at the unreleased v1.2.2 |
| Style guide loading | Phase 026 put the spacing bands in style-guide.md, which the packet loaded only for a colour, so a plain request never loaded the bands the rubric checks. The packet SKILL.md and the kernel's Knowledge table now load it with the rubric before every gate |
<!-- /ANCHOR:log -->
