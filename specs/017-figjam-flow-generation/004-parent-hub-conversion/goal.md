---
title: "Goal: Phase 4: Parent hub conversion"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "parent hub conversion goal"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "product-owner/017-figjam-flow-generation/004-parent-hub-conversion"
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
# Goal: Phase 4: Parent hub conversion

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Convert Product Owner into a parent hub on the Moneybird Accountant pattern, with sk-product-owner as the default packet and the vendored mcp-figma as its only tool packet, without changing how existing requests route.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | sk-product-owner stays the default packet. The vendored mcp-figma is the hub's only tool packet. |
| D2 | The conversion is built in a scratch clone and applied as one patch. |
| D3 | ROUTER.md and the hub SKILL.md join the format gate's lint list in both the shared Sync Loop validator and Product Owner's twin, as identical edits (operator, 2026-10-20). |
| D4 | The token allowance is the hub SKILL.md plus the hub shape's measured fixed cost of 286 o200k tokens: the ROUTER.md head, the SKILL.md pointer and the AGENTS.md read order that the parent goal's Moneybird shape (D2) requires (operator amendment, 2026-10-20). |

<!-- /ANCHOR:directive -->

---


<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [x] Router and format fixtures pass with the same counts as the baseline captured before the change
- [x] The hub check passes, and fails on each of three planted defects: an unregistered packet folder, a wrong default and a missing router pointer
- [x] Gold rows pass for a bare request, the existing figma Task fixture, a figma-ds-cli-only request and a negated Figma mention
- [x] The default Task request's token count, measured with one tokenizer before and after, rises by no more than the hub SKILL.md plus 286 tokens of hub overhead (D4)
- [x] A fresh reviewer has read the diff and its findings are recorded in this phase's log
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
| Phase opened | Done | |
| Baseline and convert.py proven on scratch | Done | scratch/base-*.txt, 125 citations remapped, 0 bad |
| Hub check, validators, patch applied live | Done | implementation-summary.md:97-105, all gates at baseline |

### Deviations and findings

| Item | Note |
|------|------|
| Token criterion | Overhead 432 trimmed to 286, then amended by the operator as D4 |
| Review, P1 | Stage one sent `$d figma-ds-cli ...`, "document how figma-ds-cli ..." and PRD requests to mcp-figma. Fixed: any `$` command or a wider artifact word list keeps Product Owner, with gold rows |
| Review, P1 | Stale routing mentions in SKILL.md, router-contract.md, READMEs and 7 playbook rows. Fixed. interactive-mode.md kept on purpose, a pair source whose pointer still forwards |
| Review, P1 | AGENTS.md read order was not conditional on the packet. Fixed, and workflow step 2 updated |
| Review, P2 | Clause-scoped negation and curly apostrophes, vendored exemption limited to non-default tool packets with two more self-test defects, gate counts 9, hub allowed-tools, leaf-manifest note, Sync Loop docs, SYNC.md record. Fixed |
| Review, P2 deferred | Router contract ALWAYS list is a kernel copy, so 007. Versions and changelog, so 008 |
| run_receipts.sh | Exits 1 before and after this phase: SYNC.md has no upload receipt. Operator step, tracked for 007 |
<!-- /ANCHOR:log -->
