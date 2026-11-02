---
title: "Acceptance Criteria: Phase 9: figjam-skill-research"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record, or superseded by one."
trigger_phrases:
  - "figjam skill research acceptance criteria"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "product-owner/017-figjam-flow-generation/009-figjam-skill-research"
    last_updated_at: "2026-10-20T07:37:46Z"
    last_updated_by: "scaffold"
    recent_action: "Authored the acceptance criteria for this packet"
    next_safe_action: "Meet, waive or supersede the open criteria"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "1004bf13-7863-4447-a63e-6ad2f5fcfd86"
      parent_session_id: null
    completion_pct: 0
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: acceptance-criteria | v2.2 -->
# Acceptance Criteria: Phase 9: FigJam skill research

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** product-owner/017-figjam-flow-generation/009-figjam-skill-research
**Level:** 2
**Status:** In Progress
**Date:** 2026-10-20
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:criteria -->
## 2. CRITERIA

One row per criterion. `AC-ID` is stable once written: supersede a criterion, never renumber it.

| AC-ID | REQ | Given / When / Then | Verification | Status | Waiver |
|-------|-----|---------------------|--------------|--------|--------|
| AC-001 | REQ-001 | Given the DeepSeek lineage, When the 20 iterations finish, Then the state log holds 20 iteration records and the run stopped on maxIterationsReached | research/lineages/deepseek/deep-research-state.jsonl: 20 iteration records, synthesis_complete with stopReason maxIterationsReached, read 2026-10-20 | Met | - |
| AC-002 | REQ-002 | Given the run ended, When the iterations are read, Then iteration-001.md to iteration-020.md exist and each cites at least one corpus file | `ls research/lineages/deepseek/iterations` lists 20 files, and a per-file count of SOURCE tags found none below 1 | Met | - |
| AC-003 | REQ-003 | Given the iterations, When a fresh Opus 5.5 high agent synthesizes, Then research/research.md lists every claim it dropped or corrected | research/research.md sections 5 and 6, and three corrections rechecked by the orchestrator with flow_check.py and the cited lines | Met | - |
| AC-004 | REQ-004 | Given the synthesis, When it is read alone, Then it ranks at least 10 changes with their Flow Mode file and corpus file, and gives a verdict on the four known gaps | research/research.md section 4 holds 15 ranked changes, section 2 adopts all four gaps | Met | - |
| AC-005 | REQ-005 | Given a long run, When agents are working, Then a one-line status is posted about every 3 minutes | Status lines in the session from 09:40 to 10:20 | Met | - |

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

**Closeable:** No

Every criterion is met. The phase stays open until the operator chooses which ranked changes to apply.
<!-- /ANCHOR:closure -->
