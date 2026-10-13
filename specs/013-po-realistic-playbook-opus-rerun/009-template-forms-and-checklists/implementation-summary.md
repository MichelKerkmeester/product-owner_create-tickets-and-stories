---
title: "Implementation Summary: Phase 9, template forms and checklists"
description: "Every Product Owner template, rule, mirror, example and export now uses the operator's ClickUp forms: H4 openings, a bold Expected outcomes label, About at H2, Story requirements as checklist items and every checkbox written `[]`."
trigger_phrases:
  - "implementation summary"
  - "template forms"
  - "checklist bracket form"
importance_tier: "normal"
contextType: "general"
_memory:
  continuity:
    packet_pointer: "013-po-realistic-playbook-opus-rerun/009-template-forms-and-checklists"
    last_updated_at: "2026-09-26T14:30:00Z"
    last_updated_by: "claude-code"
    recent_action: "Committed and pushed Product Owner 0d085cb and Barter b6ac9d86"
    next_safe_action: "None for this phase"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "scaffold-009-template-forms-and-checklists"
      parent_session_id: null
    completion_pct: 100
    open_questions: []
    answered_questions: []
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
| **Spec Folder** | 009-template-forms-and-checklists |
| **Completed** | 2026-09-26 |
| **Level** | 2 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

A Story written the operator's way now passes the gate. The templates, rules and kernel teach the forms the operator already uses in ClickUp, and all 78 benchmark exports carry them.

### Phase 9: template forms and checklists

A Story opens with `## About`, then `#### Problem` and `#### Solution`, and Solution closes on a bold `**Expected outcomes**` label over a divider. An Epic's Problem, Goal and Solution sit at H4 too. Task and Bug open with `## About` and keep their other sections at H3. Story requirements are `- []` items under bold group names, still hard constraints and never build steps. Every checkbox a deliverable carries is written `[]`, and the gate blocks the spaced `[ ]` in a Product Owner deliverable.

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| `sk-product-owner/assets/*.md`, `references/*.md`, `SKILL.md`, `AGENTS.md` | Modify | The five forms in every template and rule |
| `claude project/Custom Instructions.md`, `claude project/knowledge/*` | Modify, Rename | Kernel v0.20.0 and 11 renamed mirrors |
| `sk-product-owner/assets/examples/**`, `export/benchmark/**` | Modify | 17 examples and 75 exports converted, all 78 checked |
| `validate-output-format.cjs` (both copies), `systems.cjs`, `run_fixtures.sh` (both), `fixtures/` (both) | Modify, Create | The gate reads `[]` and blocks the retired forms |
| `systems.py`, `carrier_query_evidence.py`, `residency/backlog.md` | Modify | Declared statements resynced, mirror names repointed |
| `sk-product-owner/manual-testing-playbook/**` | Modify | 42 scenarios and root 2.5.0.0, 38 with the new forms |
| `changelog/v0.17.0.0.md`, `SYNC.md`, READMEs, `description.json`, run README | Create, Modify | Versions, the pending review and the ClickUp risk |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

The rules changed first, each edit on its own line so no playbook citation moved. The gate then learned `[]` in every checkbox pattern, which had missed that form before. A scratch transform converted the exports and examples against a snapshot, and its check proved each changed line was an allowed transform. The run found the retired forms on the old snapshot and none on the converted files.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| Only About moves to H2 in Task and Bug | The operator's own DS parent export keeps Requirements and Bug at H3 |
| `#### **User Story**` becomes a bold label | Inside an H4 Solution, an H4 block would read as its sibling, the same problem the Expected outcomes change fixes |
| The `[ ]` rule keyed to Product Owner artifacts | The sources name the retired form when they ban it and keep it in the model's own checklists, and other systems state no checkbox form |
| "Build checklist" reworded to "build steps" | With checklist items now the marker, the old phrase would read as banning the new form |
| The model's quality checklists keep `- [ ]` | They are never output, and the operator scoped `[]` to artifact checklists |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| `transform.py --check` on exports and examples | 78 of 78 and 21 of 21 pass; two planted faults caught |
| Gate on the old snapshot | 815 `[ ]` lines and 290 plain Requirements bullets found, 75 files fail |
| Gate on sources and exports | 40 sources and 78 exports exit 0 |
| Fixture suites and reference parity | Copywriter, Deal, Sales 131 each; Product Owner 129 and PASSED; parity identical |
| Residency precheck, `rule_parity.py` | PASSED for 7 systems; PASSED, 6 rules |
| Playbook validator, selftest | PASS, 46 scenarios, 0 violations; 7 of 7 |
| Commits and pushes | Product Owner `bb9210f..0d085cb` (195 files); Barter `0b08add1..b6ac9d86` (210 files), every hook passing with no bypass, both pushed on the operator's go-ahead |
| Parity and residency on the commit | `validate_parity.py product-owner` PASSED 38/38; `run_residency.sh product-owner` PASSED |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **ClickUp rendering of `- []` is unverified.** Standard markdown renders only `- [ ]` as a checkbox. The operator chose `[]` knowing this, and a paste into ClickUp would confirm it.
2. **The kernel review is stale.** The operator reviewed v0.18.0, and v0.19.0 and v0.20.0 wait on that review.
3. **No scenario reran.** Nothing shows the runtimes write the new forms yet.
<!-- /ANCHOR:limitations -->

---
