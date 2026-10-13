---
title: "Acceptance Criteria: Phase 9, template forms and checklists"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record, or superseded by one."
trigger_phrases:
  - "acceptance criteria"
  - "closure gate"
  - "ac traceability"
  - "waiver adr"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "013-po-realistic-playbook-opus-rerun/009-template-forms-and-checklists"
    last_updated_at: "2026-09-26T14:30:00Z"
    last_updated_by: "claude-code"
    recent_action: "Met every criterion, AC-007 on the commit"
    next_safe_action: "None for this phase"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "[SESSION-ID]"
      parent_session_id: null
    completion_pct: 100
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: acceptance-criteria | v2.2 -->
# Acceptance Criteria: Phase 9, template forms and checklists

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** 013-po-realistic-playbook-opus-rerun/009-template-forms-and-checklists
**Level:** 2
**Status:** Complete
**Date:** 2026-09-26
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:criteria -->
## 2. CRITERIA

One row per criterion. `AC-ID` is stable once written: supersede a criterion, never renumber it.

| AC-ID | REQ | Given / When / Then | Verification | Status | Waiver |
|-------|-----|---------------------|--------------|--------|--------|
| AC-001 | REQ-001 | Given the five templates, When each is read, Then Story and Epic open at H4, Expected outcomes is a bold label inside Solution, About is H2, and every checkbox is `[]` | Story Template v0.101, Epic v0.102, Task v0.103, Bug v0.102, Doc v0.109; the old forms appear only where a rule names them as retired or in the model's own quality checklists | Met | - |
| AC-002 | REQ-002 | Given the snapshots, When `transform.py --check` runs on the exports and examples, Then every changed line is an allowed transform and no file fails | `scratch/verify-exports.txt`: checked 78, fails 0; `scratch/verify-examples.txt`: checked 21, fails 0; a planted `###` heading and an added word were caught | Met | - |
| AC-003 | REQ-003 | Given the old snapshot, When the updated gate runs, Then it blocks each retired form, and on the converted files it exits 0 | 815 `[ ]` lines and 290 plain Requirements bullets found, 75 snapshot files fail; 40 sources and 78 exports exit 0 | Met | - |
| AC-004 | REQ-003 | Given both validators, When every fixture suite and `reference-parity.cjs` run, Then each passes and the two copies agree | Copywriter, Deal and Sales 131 pass each; Product Owner 129 via the shared runner and PASSED on its own; reference parity identical; fixture folders `cmp` identical | Met | - |
| AC-005 | REQ-004 | Given the kernel, mirrors, declaration and playbook, When residency, rule parity and the playbook validator run, Then each passes | Residency precheck PASSED for 7 systems; `rule_parity.py` PASSED, 6 rules; playbook PASS, 46 scenarios, 0 violations; selftest 7 of 7 | Met | - |
| AC-006 | REQ-005 | Given the version surfaces, When they are read, Then skill 0.17.0, kernel v0.20.0 and root 2.5.0.0 agree everywhere, and `SYNC.md` marks the v0.20.0 review pending | SKILL.md, sk-product-owner/README.md, description.json 0.17.0.0, both READMEs, SYNC.md line 18 and the new note, changelog v0.17.0.0 | Met | - |
| AC-007 | REQ-004 | Given the commit, When parity, residency and `validate.sh --recursive` run, Then each passes | Product Owner `0d085cb`, Barter `b6ac9d86`: `validate_parity.py product-owner` PASSED 38/38, `run_residency.sh product-owner` PASSED, `validate.sh --recursive --strict` RESULT: PASSED | Met | - |

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

The transform check and the gate's catch on the old snapshot carried the packet: every changed line is an allowed transform, and every retired form is found. How ClickUp renders `- []` is outside every criterion, since the operator accepted that risk.
<!-- /ANCHOR:closure -->
