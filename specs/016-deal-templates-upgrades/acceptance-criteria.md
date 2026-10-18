---
title: "Acceptance Criteria: Deal Templates upgrades for Product Owner"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record, or superseded by one."
trigger_phrases:
  - "deal templates upgrades acceptance criteria"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "016-deal-templates-upgrades"
    last_updated_at: "2026-10-18T18:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Closed the packet: every gate passes"
    next_safe_action: "Resync the handed-over systems.py pairs, then commit when the operator asks"
    blockers: []
    key_files:
      - "sk-product-owner/assets/interactive-response-templates.md"
      - "claude project/Custom Instructions.md"
      - "benchmark/gates/example_lint.py"
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "61ef885c-592f-4cc5-8163-827a30b0a258"
      parent_session_id: null
    completion_pct: 100
    open_questions: []
    answered_questions:
      - "Catalog em dash: widen the exception"
      - "Explicit commands: keep asking first"
---
<!-- SPECKIT_TEMPLATE_SOURCE: acceptance-criteria | v2.2 -->
# Acceptance Criteria: Deal Templates upgrades for Product Owner

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** 016-deal-templates-upgrades
**Level:** 2
**Status:** Complete
**Date:** 2026-10-18
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:criteria -->
## 2. CRITERIA

One row per criterion. `AC-ID` is stable once written: supersede a criterion, never renumber it.

| AC-ID | REQ | Given / When / Then | Verification | Status | Waiver |
|-------|-----|---------------------|--------------|--------|--------|
| AC-001 | REQ-001 | Given every worked example and Project mirror, When the validator runs in artifact mode, Then none fails | T004, T009; example lint "PASSED 42 files" | Met | - |
| AC-002 | REQ-002 | Given a Catalog with an Index heading, When an entry heading or its link carries one em dash after a stable ID, Then it passes, and any other em dash fails | T007; format fixtures pass 59 cases, reference parity identical, Deal Templates, Copywriter and Sales Direct fixtures pass | Met | - |
| AC-003 | REQ-003 | Given the four reply surfaces and the kernel, When a reply is described, Then it points at Section 3, which holds a wrong and a right first line and three worked replies | T005, T006; example lint reads the worked replies on both packagings | Met | - |
| AC-004 | REQ-004 | Given one answered question round, When the next reply comes, Then it drafts and lists each addition under Open items | T006; Core Rule 1, `SKILL.md` Clarification Protocol, kernel line 9 and rule 6 | Met | - |
| AC-005 | REQ-005 | Given the gate runner, When it runs, Then every gate reports and a broken example or reply fails the lint | T009, T012; "all 5 gates pass", self-test passes 3 cases | Met | - |
| AC-006 | REQ-006 | Given the playbook, When its validator runs, Then no scenario fails and changed expectations read the new wording | T010, T013; playbook validator PASS, 46 scenarios, 0 violations | Met | - |

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

All six criteria are met. Residency stays red until the handed-over `systems.py` pairs land, and the shared Human Voice card still needs the Catalog grant line. Both sit outside this packet's write scope.
<!-- /ANCHOR:closure -->
