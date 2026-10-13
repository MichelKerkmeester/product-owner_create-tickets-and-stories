---
title: "Acceptance Criteria: Phase 5, grade the Opus run and write the report"
description: "The criteria phase 5 must satisfy before it may close, each one met, waived by a decision record, or superseded by one."
trigger_phrases:
  - "grading acceptance"
  - "phase 5 closure"
  - "results csv 46 rows"
  - "every export reviewed"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "013-po-realistic-playbook-opus-rerun/005-grading-and-report"
    last_updated_at: "2026-09-26T05:10:00Z"
    last_updated_by: "claude-opus-5-5"
    recent_action: "Met all 13 criteria with observed evidence"
    next_safe_action: "None, the phase is closed"
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
# Acceptance Criteria: Phase 5, grade the Opus run and write the report

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** 013-po-realistic-playbook-opus-rerun/005-grading-and-report
**Level:** 2
**Status:** Complete
**Date:** 2026-09-25
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:criteria -->
## 2. CRITERIA

One row per criterion. `AC-ID` is stable once written: supersede a criterion, never renumber it.

| AC-ID | REQ | Given / When / Then | Verification | Status | Waiver |
|-------|-----|---------------------|--------------|--------|--------|
| AC-001 | REQ-001 | Given the run's 46 scenarios, When each is graded, Then it has exactly one verdict from all its turns citing its evidence, and a missed Pass clause on any turn makes it FAIL | `results.csv` holds the playbook's 46 IDs, one row each, and each note names the reply line, stream or export that decides it; every early-draft FAIL cites its Turn 1 Pass clause | Met | - |
| AC-002 | REQ-002 | Given the rule sources, When a grader reads them, Then it reads them with `git show` at the commits phase 004 recorded | `grading-notes.md` opens on Product Owner `3023c5e`, and `scratch/root-at-run.md` and `scratch/sources-at-run.txt` came from `git show` at it; the rounds cite `39bcd29` and `b591571` the same way | Met | - |
| AC-003 | REQ-003 | Given `results.csv`, When it is read, Then its header is `id,runtime,model,result,turns_run,turns_declared,after_failed_gate,facts_intact,note` and it has 46 rows, one per scenario ID | The step 6 one-liner prints 46 rows, the header `id,runtime,model,result,turns_run,turns_declared,after_failed_gate,facts_intact,note` and the one model `claude-opus-5-5-medium` | Met | - |
| AC-004 | REQ-004 | Given each total in the README and `results.md`, When it is recomputed from `results.csv` with the command the report names, Then it matches | The README count command reran and printed skill 12 and 11, Project 8 and 15, `facts_intact` yes 38 of 46, `after_failed_gate` yes 22 and 4 of 23 twins differing, each equal to README and `results.md` | Met | - |
| AC-005 | REQ-005 | Given the five batch drafts, When they come back, Then the orchestrator reviews every verdict before writing and reads every FAIL and every disagreement a second time | `grading-notes.md` section 1 lists each ruling and the rows it changed, and every FAIL was read a second time; the rounds' review sections record the `PDK-003` regrade | Met | - |
| AC-006 | REQ-006 | Given `<run folder>`, When `check_report.sh` runs, Then both checks execute, `hvr-lint.csv` is written and every finding appears in `grading-notes.md` | `check_report.sh` exit 2 with both checks run and neither unable to run; `hvr-lint.csv` written; its lint and twin findings in `grading-notes.md` section 2 | Met | - |
| AC-007 | REQ-007 | Given every file in `export/benchmark/`, When the realism review runs, Then each has an entry for artifact kind and template shape, verbatim fixture facts and size against its advisory band | 200 files in `export/benchmark/`, each with a realism entry: 98 in the main notes, 59, 20 and 23 in the three rounds' notes. On 2026-09-26 the operator removed the 102 round files, which stay at Product Owner `3fdce37`, so the folder now holds the main run's 98 | Met | - |
| AC-008 | REQ-008 | Given the findings, When they go to the operator, Then they go through the ask tool and no repair lands without a recorded decision | Sixteen decisions in `implementation-summary.md`, each through the ask tool; the repair commits `39bcd29`, `b591571` and `b50f0a0` each post-date their decisions | Met | - |
| AC-009 | REQ-009 | Given the finished packet, When it closes, Then `validate.sh --recursive` reports 0 errors, every phase's `acceptance-criteria.md` reads `Closeable: Yes` and each parent goal criterion is checked with fresh output | `validate.sh --recursive --strict` on the packet: Errors 0 in every folder; the `grep -L` for `Closeable: Yes` over the five phases prints nothing; parent log rows record each criterion checked on 2026-09-26 | Met | - |
| AC-010 | REQ-010 | Given the 23 twin pairs, When their verdicts are compared, Then each has an agreement entry and each disagreement carries one cause confirmed in both sides' rule files | `results.md` has 23 twin rows matching `results.csv` and the `twin_divergence` output; the four disagreements each carry one cause checked in both packagings (`grading-notes.md` section 3) | Met | - |
| AC-011 | REQ-011 | Given a failed handover, When the README is written, Then the failure opens the README before any other result and names the runtime whose other verdicts it puts in question | README section 1 opens on the failed Project handover `PID-001` and names the Project runtime; 22 Project rows carry `after_failed_gate` yes | Met | - |
| AC-012 | REQ-012 | Given a repair the operator decides, When it is carried out, Then it has its own tasks in `tasks.md` and its scenarios rerun into a graded `remeasure-<slug>/run-<n>/` round | Tasks T024 to T041; rounds `remeasure-operator-repairs/run-1` (26 rows), `remeasure-file-forecast/run-1` (8 rows) and `remeasure-supplied-values/run-1` (12 rows), each graded | Met | - |
| AC-013 | REQ-013 | Given the report, When it is committed, Then Barter and the Product Owner public repo carry it, the public commit has no attribution line, the push waits for the operator's go-ahead and no `SYNC.md` marks a kernel review done without the operator's confirmation | Product Owner `01200fa`, `b50f0a0` and `3fdce37`, Barter `3b55bfbe`, `7396d79e` and `d214c160`, no attribution line in any; pushed on the operator's go-ahead of 2026-09-26 (`a02f3b2..3fdce37`, `0545f2a4..d214c160`); `SYNC.md` still says the kernel review is pending, as the operator confirmed | Met | - |

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

Every criterion is `Met` with observed evidence. The report is committed and pushed in both repos, and the kernel review stays pending on the operator's word.
<!-- /ANCHOR:closure -->
