---
title: "Implementation Summary: Phase 3, the playbook rewrite and the approval gate"
description: "The Product Owner playbook now holds 46 realistic scenarios at Roamstay, Loomlist and Fernhouse, with a Ticket realism rubric and an attachment-aware run folder. Committed as Product Owner 3023c5e and Barter c15c05e9 and approved by the operator on 2026-09-25."
trigger_phrases:
  - "implementation summary"
  - "playbook rewrite status"
  - "phase 3 complete"
  - "scenario plan approved"
importance_tier: "normal"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "013-po-realistic-playbook-opus-rerun/003-playbook-rewrite"
    last_updated_at: "2026-09-25T19:32:00Z"
    last_updated_by: "claude-opus-5-5"
    recent_action: "Recorded the operator's approval of the scenario plan and closed the phase"
    next_safe_action: "Start phase 004 with the SID-001 and PID-001 smoke run"
    blockers: []
    key_files:
      - "AI Systems/Product Owner/sk-product-owner/manual-testing-playbook/manual-testing-playbook.md"
      - "AI Systems/Product Owner/benchmark/reports/2026-09-25--manual-testing-playbook--claude-opus-5-5-medium/run/playbook_runner.py"
      - "AI Systems/Product Owner/benchmark/reports/2026-09-25--manual-testing-playbook--claude-opus-5-5-medium/run/selftest.py"
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "12f293fe-5421-46a0-b1ea-9fdc15ce0f8e"
      parent_session_id: null
    completion_pct: 100
    open_questions: []
    answered_questions:
      - "Every scenario attaches its company's context file: confirmed"
      - "The two new advisory items stay advisory, the discipline code item for Task and Bug titles only"
      - "SST-004 follows the phase 001 bundle design and keeps the $story break-it-into-tasks phrasing"
      - "The report folder stays dated 2026-09-25, renamed by phase 004 if the run starts later"
      - "The operator approved the scenario plan on 2026-09-25 against Product Owner 3023c5e and Barter c15c05e9"
---
<!-- SPECKIT_TEMPLATE_SOURCE: impl-summary-core | v2.2 -->
# Implementation Summary

<!-- SPECKIT_LEVEL: 2 -->
<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

---

<!-- ANCHOR:metadata -->
## Metadata

| Field | Value |
|-------|-------|
| **Spec Folder** | 003-playbook-rewrite |
| **Status** | Complete |
| **Completed** | 2026-09-25 |
| **Level** | 2 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

The Product Owner playbook no longer asks for toy tickets about a payout pause. Its 46 scenarios, 23 skill scenarios and their Project twins, each ask for real engineering work at one of three fictional companies, with that company's context file and sources attached. A new report folder can stage those attachments, keep a Story bundle whole and refuse a run at the wrong model or effort.

### Phase 3: playbook-rewrite

| Change | Where |
|--------|-------|
| 46 scenarios in six waves: 7 tasks, 3 bugs, 5 Stories including the Story with 4 tasks, 4 Epics and 4 docs per side, plus the handover, a vague intake and a command conflict | Ten `skill-*` and `project-*` folders |
| A `### Ticket realism` subsection with 5 Blocking and 4 Advisory items, the existing readings untouched | Root section 5 |
| A "Company context and attachments" section, `Story-` and the bundle path in Export names, waves 1 to 6, 46 summaries and the section 18 index | Root `manual-testing-playbook.md` v2.0.0.0 |
| Attachment staging into `context/` with sha256, a byte-exact isolation proof, a bundle-keeping collector, an engine, model and effort check, and a selftest planting a fault for each | New report folder `run/` |

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| `AI Systems/Product Owner/sk-product-owner/manual-testing-playbook/manual-testing-playbook.md` | Modified | Root v2.0.0.0, rubric, companies section, waves, index |
| `AI Systems/Product Owner/sk-product-owner/manual-testing-playbook/{skill,project}-*/` (12 files) | Deleted | The retired payout pause and retry scenarios |
| `AI Systems/Product Owner/sk-product-owner/manual-testing-playbook/{skill,project}-*/` (46 files) | Created or rewritten | The new scenarios, both identity handovers kept in place |
| `AI Systems/Product Owner/benchmark/reports/2026-09-25--manual-testing-playbook--claude-opus-5-5-medium/` | Created | `.gitignore` and `run/playbook_runner.py`, `collect_exports.py`, `check_run.py`, `selftest.py` |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

The orchestrator wrote the rubric into the root first. Opus 5.5 group writers then built the scenario files in parallel from one brief, and the run scripts were extended from byte-identical copies of the Sonnet ones. The orchestrator copied every summary Prompt into the root by script, applied six writer amendments, and committed Product Owner 3023c5e and Barter c15c05e9 with no attribution line.

The gate then ran on those commits. The orchestrator printed the scenario table, published a private plan page at https://claude.ai/artifact/YE9rqVDigYxfRXTs8u3NR8 and asked through AskUserQuestion.

### Operator approval

| Field | Value |
|-------|-------|
| Date | 2026-09-25, 19:31 UTC |
| Answer | "Approve and run" |
| Approved state | Product Owner 3023c5e, Barter c15c05e9 |
| Report folder at approval | `.gitignore` and the four `run/` scripts only, no `manifest.json`, `run-status.json` or `run-log.jsonl` |
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| The gate requires `warnings=0` as well as `violations=0` | The validator reports a prompt out of sync only as a `PROMPT_UNSYNCED` warning |
| A selftest compares twins | The validator checks prompt sync inside one file and never across the skill and Project twin |
| Attachments are written as links | The validator's link check then proves every fixture exists, and the runner reads the same links |
| Every scenario attaches its company's context file | The rubric's context items need context to grade against |
| The size band sits in its own bullet, outside Pass/fail | The root fails any turn that misses a Pass clause, so a band inside one would turn advisory into blocking |
| A discipline code is advisory, and for Task and Bug titles only | No routed template asks for one, and the skill's H1 rule bans the short codes in Story and Epic titles |
| A placeholder quoted from a source and a labelled unverified hypothesis are exempt | Both are faithful to the input, so failing them would punish accuracy |
| `check_run.py` also reads the engine and the effort | The Sonnet version checked only the model, so a run at the wrong effort would pass |
| The commit comes before the gate | The operator approves a named SHA rather than a working tree |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

Rerun on 2026-09-25 against the committed state, just before the approval was recorded. Acceptance: 18 of 18 criteria met, see `acceptance-criteria.md`. Checklist: 12 of 12 P0 and 8 of 8 P1 items checked with evidence in `tasks.md`.

| Check | Result |
|-------|--------|
| `validate-playbook-package.cjs` | `PASS ... scenarios=46 categories=10 operator=46 routing_gold_excluded=0 violations=0 warnings=0`, `exit=0` |
| `run/selftest.py` | 7 of 7 tests passed, parse-real 463 checks, every planted fault caught |
| Runner `--dry-run` | 46 rows, 86 turns, all 46 with attachments, 23 per side, waves 2, 12, 6, 8, 14 and 4 |
| `PRD-`, em dash and `/Users/` searches | Nothing printed |
| Sonnet report folder | `git diff --stat` empty in both repositories |
| Turn inputs | 0 of 86 hold a backtick, pipe, ISO date or line break |
| Size band bullets | 46, none inside a Pass clause |
| Operator approval | Given, see How It Was Delivered |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **Context items need a reader.** The rubric's context and placeholder items are graded by reading the attachments in phase 005. No script checks them.
2. **Not pushed.** Both commits wait for the operator's go-ahead.
3. **No phase changelog.** The nested changelog tool resolves its project root to the linked Public repo and refuses packets here, as it did for 075.
4. **Goal log kept late.** The phase goal log was not written row by row while the writers ran, so the rubric-before-writers order is evidenced by `tasks.md` T003 and the parent log instead.
<!-- /ANCHOR:limitations -->

---
