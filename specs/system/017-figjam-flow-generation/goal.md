---
title: "Goal: Product Owner FigJam flow generation upgrade"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "packet goal"
  - "durable directive"
  - "completion criteria"
  - "goal binding"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "product-owner/017-figjam-flow-generation"
    last_updated_at: "2026-10-19T21:00:00Z"
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
# Goal: Product Owner FigJam flow generation upgrade

<!-- SPECKIT_TEMPLATE_SOURCE: goal | v2.2 -->
<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Make Product Owner turn screenshots, Figma flows and product docs into FigJam flows, as a parent hub with an embedded figma skill and a Claude Code plugin that syncs back to .skilled.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | FigJam is the only output and flows follow sk-design-diagram. |
| D2 | The plugin follows the sk-create-skill parent-hub contract. |
| D3 | Research comes first and names the later phases. |
| D4 | Research runs on DeepSeek V4.1 Flash max via cli-pi. |
| D5 | Flow Mode composes each board with use_figma from a checked model. |
| D6 | Flow Mode replies with the board URL, its read-back lines and the HVR self-scan, and saves no export. |
| D7 | The plugin ships skills only, no bin folder or MCP server. |

<!-- /ANCHOR:directive -->

---

<!-- ANCHOR:binding -->
## 2. BINDING

**Read the child goal before working a phase.** Each is authoritative for its
phase and binds as if written here.

| Phase | Goal document |
|-------|---------------|
| 001 | `001-research/goal.md` |
| 002 | `002-write-route-spike/goal.md` |
| 003 | `003-vendored-figma-and-sync/goal.md` |
| 004 | `004-parent-hub-conversion/goal.md` |
| 005 | `005-flow-mode/goal.md` |
| 006 | `006-claude-code-plugin/goal.md` |
| 007 | `007-project-mirror/goal.md` |
| 008 | `008-upstream-roundtrip-and-release/goal.md` |
| 009 | `009-figjam-skill-research/goal.md` |
| 010 | `010-flow-mode-hardening/goal.md` |
| 011 | `011-figjam-packet-split/goal.md` |
| 012 | `012-vendored-clickup/goal.md` |
| 013 | `013-skilled-hub-alignment/goal.md` |
| 014 | `014-hub-to-root/goal.md` |
| 015 | `015-figjam-rebuild/goal.md` |
| 016 | `016-figjam-improvement-research/goal.md` |
| 017 | `017-board-link-in-artifact/goal.md` |
| 018 | `018-artifact-plus-board-pair/goal.md` |
| 019 | `019-hosted-route-connection/goal.md` |
| 020 | `020-accent-and-cut-test/goal.md` |
| 021 | `021-board-critic-pass/goal.md` |
| 022 | `022-created-node-tags/goal.md` |
| 023 | `023-kernel-no-connector-sentence/goal.md` |
| 024 | `024-flow-delivery-pointers/goal.md` |
| 025 | `025-plan-whoami/goal.md` |
| 026 | `026-self-edit-guidance/goal.md` |
| 027 | `027-repeated-edge-labels/goal.md` |
| 028 | `028-readback-direction/goal.md` |
| 029 | `029-extension-fixes/goal.md` |
| 030 | `030-figjam-research-three/goal.md` |
| 031 | `031-round-three-apply/goal.md` |
| 032 | `032-clickup-push-targets/goal.md` |
| 033 | `033-composed-boards/goal.md` |
| 034 | `034-stop-and-label-fixes/goal.md` |
| 035 | `035-first-glance-and-routing/goal.md` |
| 036 | `036-figjam-design-system/goal.md` |
| 037 | `037-figjam-design-spec/goal.md` |
| 038 | `038-figjam-model-comparison/goal.md` |
| 039 | `039-figjam-run-findings/goal.md` |
| 040 | `040-figjam-sonnet-run-findings/goal.md` |

**Precedence.** Decisions above outrank child detail. Child detail outranks any
summary of it. Name a conflict rather than resolving it silently.

**Stop.** Only the criteria below decide done. An evaluator sees the objective
string, not these files.
<!-- /ANCHOR:binding -->

---

<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [ ] 001-research/research/research.md holds the approved 20-iteration synthesis
- [ ] Every phase folder has a Phase Documentation Map row and a binding row above
- [ ] A FigJam flow exists at a recorded URL for a screenshot, a Figma flow and a product doc
- [ ] Product Owner holds mcp-figma and a plugin that loads with claude --plugin-dir
- [ ] The sync command reports 0 files differing from .skilled
- [ ] validate.sh --recursive --strict on the parent prints RESULT: PASSED
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
| 003-vendored-figma-and-sync | Done | 58 files vendored, 7 of 7 tests, run_gates.sh 7 of 7, validate PASSED |
| 002-write-route-spike | Blocked | No Figma MCP connected in the session |
| 001-research | Done. Operator approved the later-phase list and decisions Q1, Q3 and Q8 on 2026-10-20 | 001-research/research/research.md section 15 |

### Deviations and findings

| Item | Note |
|------|------|
| D6 amendment | The operator amended D6 on 2026-10-20 to match the reply the packet ships, so the decision lists the `Extensions:` line |
| Budget cut | Phases 017 to 028 took the durable slice to 4,826 characters, so on 2026-10-20 the binding labels became phase numbers and D2, D3, D4, D5, D6 and four criteria were reworded to 3,998, with no row or criterion removed. D2 was amended twice on 2026-10-20 |
| Budget split | On 2026-10-21 phase 029 became a nested phase parent with its own goal for the thirteen Section 9 findings, so the binding gained one row, D2 dropped its extension name and D5 two words to fit |
| D4 amendment | On 2026-10-21 the operator asked for DeepSeek for all research, so D4 moved the synthesis from a fresh Opus 5.5 high agent to DeepSeek and was shortened to fit phase 030's binding row |
| Budget cut 2 | On 2026-10-21 phase 031's binding row needed room, so the first criterion and D7 were reworded with no criterion removed |
| Budget cut 3 | On 2026-10-21 the operator placed the ClickUp push targets under this packet as phase 032, so D1, D4, D6 and D7 were reworded to fit its binding row, each keeping its meaning |
| Budget cut | On 2026-10-25 D5 was amended to the composed route phase 033 built, which replaced hosted generate_diagram, and D1, D3, D4 and D6 were shortened to fit rows 033 and 034, with no criterion removed. D4's fallbacks are GLM 5.3 Flash max, Luna max fast and SWE 2 max. D1, D2 and D7 lost a few words for row 035. The slice now sits just under 4,000, so a phase 036 means splitting 033 onward into a nested parent as 029 was |
<!-- /ANCHOR:log -->
