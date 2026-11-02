---
title: "Acceptance Criteria: Rename leftover PRD terminology to Story and Epic across the Product Owner skill, Claude Project, router benchmark and Sync Loop declaration"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record, or superseded by one."
trigger_phrases:
  - "rename prd terminology to story and epic acceptance criteria"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "015-rename-prd-terminology-to-story-and-epic"
    last_updated_at: "2026-10-17T13:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Closed the packet: drift check follows renames, every gate at baseline"
    next_safe_action: "Commit both repos when the operator asks"
    blockers: []
    key_files:
      - "sk-product-owner/references/story-mode.md"
      - "claude project/Custom Instructions.md"
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "c1f3f990-9ebe-4506-bb46-44c5323d4af7"
      parent_session_id: null
    completion_pct: 100
    open_questions: []
    answered_questions:
      - "Scope: label, prose, file names and router key"
      - "Rename drift: rename-aware gate"
---
<!-- SPECKIT_TEMPLATE_SOURCE: acceptance-criteria | v2.2 -->
# Acceptance Criteria: Rename leftover PRD terminology to Story and Epic across the Product Owner skill, Claude Project, router benchmark and Sync Loop declaration

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** 015-rename-prd-terminology-to-story-and-epic
**Level:** 2
**Status:** Complete
**Date:** 2026-10-17
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:criteria -->
## 2. CRITERIA

One row per criterion. `AC-ID` is stable once written: supersede a criterion, never renumber it.

| AC-ID | REQ | Given / When / Then | Verification | Status | Waiver |
|-------|-----|---------------------|--------------|--------|--------|
| AC-001 | REQ-001 | Given the Story Mode template and examples on both packagings, When a Story uses the per-requirement value line, Then it opens `**Story:**` | T004; grep for `**PRD:**` outside specs and changelogs returns nothing | Met | - |
| AC-002 | REQ-002 | Given the router fixtures and differential corpus, When the router gate runs, Then every input keeps its intent | T010; "PASSED 117/117 fixtures", "PASSED 189/189 differential inputs" | Met | - |
| AC-003 | REQ-003 | Given both packagings, When the artifact is named, Then it is Story or Epic and each skill line has its mirror | T007; phrase pairs hit source and mirror counts together, residual grep holds only aliases, input wording, the `PRD -` ban and history | Met | - |
| AC-004 | REQ-004 | Given the examples and router topic, When a live file references them, Then it uses `story-example-` and `story` | T005, T006; no live `prd-example` reference, leaf metadata check "passed=1 failed=0" | Met | - |
| AC-005 | REQ-005 | Given a scratch clone with the change committed, When residency and parity run, Then findings equal the HEAD baseline | T012, T013; residency 5 = baseline 5, parity "PASSED 37/37" = baseline, all seven systems equal to baseline | Met | - |

### Status values

| Value | Meaning |
|-------|---------|
| `Met` | Verified. The Verification cell names evidence that was actually observed. |
| `Unmet` | Not yet satisfied. Blocks closure. |
| `Waived` | Deliberately not pursued. Requires an ADR in the Waiver cell. |
| `Superseded` | Replaced by a different criterion or decision. Requires an ADR in the Waiver cell. |

### Waiver cell

Write `-` when the row is `Met` or `Unmet`. Write `ADR-NNN` when the row is
`Waived` or `Superseded`, naming a decision record that exists in
`decision-record.md`. A waiver naming an ADR that is not there fails validation:
the point of a waiver is that someone recorded the reasoning, so an unbacked
waiver is treated as an unmet criterion rather than as a pass.
<!-- /ANCHOR:criteria -->

---

<!-- ANCHOR:closure -->
## 3. CLOSURE STATEMENT

**Closeable:** Yes

All five criteria are met. AC-005 needed a rename-aware drift check, proved by `prove_rename_drift.py`. Aliases, PRD input wording, the `PRD -` ban and history were left out on purpose.
<!-- /ANCHOR:closure -->
