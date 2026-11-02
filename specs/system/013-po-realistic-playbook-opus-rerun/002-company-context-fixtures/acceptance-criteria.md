---
title: "Acceptance Criteria: Phase 2, company context fixtures"
description: "The criteria this phase must satisfy before it may close, each one met, waived by a decision record, or superseded by one."
trigger_phrases:
  - "company fixtures acceptance"
  - "phase 2 closure"
  - "fixture manifest criteria"
  - "fixture checks evidence"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "013-po-realistic-playbook-opus-rerun/002-company-context-fixtures"
    last_updated_at: "2026-09-25T18:45:00Z"
    last_updated_by: "claude-opus-5-5"
    recent_action: "Wrote one criterion per requirement, all Unmet"
    next_safe_action: "Write the values check and the three writer briefs"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "12f293fe-5421-46a0-b1ea-9fdc15ce0f8e"
      parent_session_id: null
    completion_pct: 0
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: acceptance-criteria | v2.2 -->
# Acceptance Criteria: Phase 2, company context fixtures

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** 013-po-realistic-playbook-opus-rerun/002-company-context-fixtures
**Level:** 2
**Status:** Draft
**Date:** 2026-09-25
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:criteria -->
## 2. CRITERIA

One row per criterion. `AC-ID` is stable once written: supersede a criterion, never renumber it. Check numbers refer to the commands in `plan.md` section 5.

| AC-ID | REQ | Given / When / Then | Verification | Status | Waiver |
|-------|-----|---------------------|--------------|--------|--------|
| AC-001 | REQ-001 | Given the fixtures folder, When its files are counted and matched to the manifest, Then exactly the 25 named files exist, each in its company folder, and nothing else | Check 1 prints 25, and check 2 (`scratch/check_manifest_values.py`) exits 0 Observed: 25 files, check 2 exit 0 with 512 values and 0 misses, planted miss exit 1 | Met | - |
| AC-002 | REQ-002 | Given the three context documents, When their lines and H2 headings are counted, Then each is 150 to 250 lines with the eleven named sections in order | Checks 5 and 6 (`wc -l`, `grep -cE` prints 11 per file), plus a read of the heading order Observed: 165, 191 and 185 lines, 11 sections each in the required order | Met | - |
| AC-003 | REQ-003 | Given the manifest table, When the values check runs, Then every backticked value is found verbatim in its file | Check 2 exits 0 and reports each file's value count Observed: Roamstay 159, Loomlist 203 and Fernhouse 150 values, 0 misses | Met | - |
| AC-004 | REQ-004 | Given the 25 fixtures, When they are grepped for U+2014, Then nothing prints | Check 3, `grep -rn $'\xe2\x80\x94'` on the folder Observed: 0 lines, and 0 semicolons | Met | - |
| AC-005 | REQ-005 | Given the 25 fixtures, When `lint_replies.py --brief` runs on each file, Then every line reads `clean` and the run exits 0 | Check 4 Observed: 25 files read `clean` | Met | - |
| AC-006 | REQ-006 | Given the two given inputs, When they are read and grepped, Then the parent task has the house parent-task shape with four backticked subtask titles, the draft opens with `# PRD - ` and carries a `**Checklist**` list, and no other file carries a template marker | Check 10 lists at most `loomlist-recurring-todos-parent-task.md` and `fernhouse-save-card-draft.md`, check 2 covers both rows, and the orchestrator's read confirms the shapes Observed: check 10 lists only the save-card draft, both given inputs pass check 2, and the read confirms the parent-task and rough-draft shapes | Met | - |
| AC-007 | REQ-007 | Given the digest pair, When each is grepped for the other's send time and for authority words, Then `07:00` is absent from the spec, `08:00` is absent from the inventory, and no authority word appears | Check 11, plus a read confirming every other entry agrees Observed: 0, 0 and no authority word, and every other entry agrees on read | Met | - |
| AC-008 | REQ-008 | Given the 25 fixtures, When they are grepped for links, brands and test vocabulary and read for people, Then nothing prints and no real person appears | Check 9 prints nothing, and the orchestrator's read in T008 is recorded in the implementation summary Observed: no URL, listed brand or test word, and the read found no real person | Met | - |
| AC-009 | REQ-009 | Given the 25 file names, When they are matched against the naming pattern and the reserved words, Then every name starts with its slug, is lowercase kebab-case `.md`, and holds no reserved word | Check 8 prints nothing Observed: both finds print nothing | Met | - |
| AC-010 | REQ-010 | Given the shared-values table, When the values check runs and each pair of files is read, Then each shared value matches and no file states a second value for the same fact | Check 2 exits 0, and the read is recorded in the implementation summary Observed: check 2 exit 0, and the read confirmed the status traps and sums, for example the ticket's `€387.00` plus `€18.00` equals `€405.00` | Met | - |
| AC-011 | REQ-011 | Given the 22 attachments, When their lines are counted and their first 5 lines read, Then each is 20 to 150 lines and names its source, its author by first name and role, and a 2026 date no later than `2026-09-25` | Checks 7 and 12, plus the read for author and date range Observed: no attachment outside 20 to 150 lines, every attachment dated in its first 5 lines | Met | - |
| AC-012 | REQ-012 | Given the committed fixtures, When both repos' logs are read, Then each holds the fixture commit, the public one has no attribution line, and nothing was pushed before the operator's go-ahead | `git log -1` in the Barter repo and in `AI Systems/Product Owner`, and the go-ahead recorded in the goal log before any push Observed: Product Owner ff5c80f and Barter 37591a16, no attribution line, nothing pushed pending the operator's go-ahead | Met | - |

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

Every criterion is met with observed evidence on Product Owner ff5c80f and Barter 37591a16. The push waits for the operator's go-ahead.
<!-- /ANCHOR:closure -->
