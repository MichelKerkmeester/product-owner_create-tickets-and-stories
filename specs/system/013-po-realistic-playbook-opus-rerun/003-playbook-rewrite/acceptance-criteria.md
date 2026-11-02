---
title: "Acceptance Criteria: Phase 3, the playbook rewrite and the approval gate"
description: "The criteria this phase must satisfy before it may close, each one met, waived by a decision record, or superseded by one."
trigger_phrases:
  - "playbook rewrite acceptance"
  - "phase 3 closure"
  - "ticket realism rubric criteria"
  - "scenario plan approval criterion"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "013-po-realistic-playbook-opus-rerun/003-playbook-rewrite"
    last_updated_at: "2026-09-25T18:45:00Z"
    last_updated_by: "claude-opus-5-5"
    recent_action: "Wrote one criterion per requirement, all unmet"
    next_safe_action: "Start T001 once phases 001 and 002 are committed"
    blockers:
      - "Phases 001 and 002 are not committed yet"
    key_files:
      - "AI Systems/Product Owner/sk-product-owner/manual-testing-playbook/manual-testing-playbook.md"
      - "AI Systems/Product Owner/benchmark/reports/2026-09-25--manual-testing-playbook--claude-opus-5-5-medium/run/selftest.py"
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "12f293fe-5421-46a0-b1ea-9fdc15ce0f8e"
      parent_session_id: null
    completion_pct: 0
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: acceptance-criteria | v2.2 -->
# Acceptance Criteria: Phase 3, the playbook rewrite and the approval gate

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** 013-po-realistic-playbook-opus-rerun/003-playbook-rewrite
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
| AC-001 | REQ-001 | Given root section 5, When it is read after the rubric lands, Then a `### Ticket realism` subsection holds the five Blocking and four Advisory items `spec.md` settles, and the Defect severity lists and six existing advisory readings keep their wording, re-anchored line numbers apart | `git diff` of section 5 shows the subsection added and the Defect severity lines unchanged apart from line numbers, and the `goal.md` log records the rubric row before the writer dispatch row | Met | - |
| AC-002 | REQ-002 | Given each `file:line` citation in the root and the scenarios, When the cited line is printed on the post-001 commit, Then it holds the cited rule | `scratch/root-citations.md` with a `sed -n` read-back per citation | Met | - |
| AC-003 | REQ-003 | Given the package, When it is searched, Then no `PRD-` export word remains, Export names grades `task`, `bug`, `doc`, `Story`, `Epic` and `intake` and the bundle path reads `export/[###] - Story-[description]/` | `grep -rn "PRD-"` over the package prints nothing, root Export names read | Met | - |
| AC-004 | REQ-004 | Given the root, When "Company context and attachments" is read, Then it names Roamstay, Loomlist and Fernhouse, links their folders and states the staging rule | Section read, every link resolved by `run/selftest.py` | Met | - |
| AC-005 | REQ-005 | Given the root, When the runner's `load_waves` reads it, Then every ID gets its manifest wave, and the coverage map, natural Turn 1 list and section 18 index name the 46 files | `run/selftest.py` wave assertions, validator `INDEX_ORPHAN_FILE` absent | Met | - |
| AC-006 | REQ-006 | Given the playbook folders, When they are listed, Then the 12 retired files are gone, the 46 manifest files exist with twins and each file names its manifest export word | File count 46, `run/selftest.py` parse and export-word assertions | Met | - |
| AC-007 | REQ-007 | Given each twin pair, When `load_playbook` parses both, Then their turn lists and attachment lists are identical and the turn counts match the manifest, 86 turns in all | `run/selftest.py` twin assertions | Met | - |
| AC-008 | REQ-008 | Given each scenario, When its `- Attachments:` links are resolved, Then each file exists, the list matches the phase 002 manifest row with the context file first and Turn 1 names each as `context/<basename>` | `run/selftest.py` attachment assertions, validator `PATH_MISSING` absent | Met | - |
| AC-009 | REQ-009 | Given the finished package, When the playbook validator runs, Then it prints `scenarios=46 categories=10 operator=46` with `violations=0 warnings=0` and exits 0 | The validator command in `plan.md` section 4, its output line quoted | Met | - |
| AC-010 | REQ-010 | Given the new report folder, When it is listed and the Sonnet folder is diffed, Then it holds `.gitignore` and the four `run/` scripts and the Sonnet folder shows no change | `ls -la` of the folder, `git diff --stat` on the Sonnet folder prints nothing | Met | - |
| AC-011 | REQ-011 | Given a scenario with attachments, When the runner builds its sandbox, Then each file sits in `context/` before the baseline on both sides, and a missing link or a basename collision exits 2 before any scenario | `run/selftest.py` staging tests with both planted faults, dry-run manifest showing each basename and sha256 | Met | - |
| AC-012 | REQ-012 | Given a staged sandbox, When `context/` gains an extra file, loses one or has one byte changed, Then `prove_isolation` reports a problem in each case, and the clean sandbox reports none | `run/selftest.py` isolation tests, three faults caught | Met | - |
| AC-013 | REQ-013 | Given a synthetic run holding a bundle on both sides, When the new collector runs, Then each bundle lands in `<side>/<id> - <folder>/`, a single file stays flat, `context/` is skipped and the Sonnet collector on the same input flattens | `run/selftest.py` collector test and its negative control | Met | - |
| AC-014 | REQ-014 | Given green checks on a committed state, When the orchestrator presents the terminal table and the private artifact page, Then the operator's explicit approval is recorded with date and both SHAs, and the new report folder holds no run output at that moment | `goal.md` log row, `implementation-summary.md`, `ls` of the report folder at approval | Met | - |
| AC-015 | REQ-015 | Given the post-001 tree, When the four identity greps run, Then their counts match what `SID-001` and `PID-001` state, and both files keep their `- Playbook ID:` line | The four greps' output, `grep -rhE "^- Playbook ID: (SID\|PID)-001"` counts 2 | Met | - |
| AC-016 | REQ-016 | Given the 46 files, When their contracts and tables are read, Then each has one `- Size band (advisory):` bullet and no Pass clause or Pass/fail cell names the size band or commentary or expects a code in a Story or Epic H1 | `grep -c` for the bullet gives 46, a search of the Pass lines gives 0 | Met | - |
| AC-017 | REQ-017 | Given the new `check_run.py`, When it reads a synthetic manifest at effort `high`, Then it reports a finding, and with no `--model` it expects `claude-opus-5-5` | `run/selftest.py` check_run test | Met | - |
| AC-018 | REQ-018 | Given the phase commits, When both repos' logs are read, Then each carries the change, the public one with no attribution line, nothing is pushed without the go-ahead and no changed file holds an em dash | `git log -1` in both repos, `git status` against the remote, the em dash search in `plan.md` section 4 | Met | - |

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

All 18 criteria are met. The gates were rerun on 2026-09-25 against Product Owner 3023c5e and Barter c15c05e9, and the operator approved the scenario plan through AskUserQuestion the same day, while the report folder held no run output. AC-001's goal log ordering is read from `tasks.md` instead, because the phase goal log was not kept row by row while the writers ran.
<!-- /ANCHOR:closure -->
