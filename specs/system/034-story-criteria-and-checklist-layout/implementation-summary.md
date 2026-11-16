---
title: "Implementation Summary"
description: "New Stories and Epics now use the new house layout: no divider under a Mark-as-done line, a Checklist label over each requirement section's checks, split user flows and screenshots in columns on a push."
trigger_phrases:
  - "story criteria and checklist layout implementation summary"
importance_tier: "normal"
contextType: "general"
_memory:
  continuity:
    packet_pointer: "system/034-story-criteria-and-checklist-layout"
    last_updated_at: "2026-11-16T18:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Moved the Story layout rules, both gates and the Project mirrors to the new house layout"
    next_safe_action: "Upload the kernel and ten knowledge files to the Claude Project"
    blockers: []
    key_files:
      - "sk-product-owner/references/story-mode.md"
      - "benchmark/format/validate-output-format.cjs"
      - "claude project/Custom Instructions.md"
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "bfbc28c2-4dbf-4675-bf2b-991dec9b2603"
      parent_session_id: null
    completion_pct: 100
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: impl-summary-core | v2.4 -->
# Implementation Summary

<!-- SPECKIT_LEVEL: 1 -->
<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

---

<!-- ANCHOR:metadata -->
## Metadata

| Field | Value |
|-------|-------|
| **Spec Folder** | 034-story-criteria-and-checklist-layout |
| **Completed** | 2026-11-16 |
| **Level** | 1 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

New Stories and Epics default to the new house layout, and the format gate checks it.

### Acceptance criteria spacing

A Mark-as-done line sits under the divider that closes its Given/When/Then bullets, with no divider under it and one empty line before the next criterion. The last criterion ends the artifact. When a Delivery section follows, a spacer with no divider above it leads into it.

### Requirement sections

A numbered section opens on a `**User flow:**` label with one bullet per step. Its direct checks follow a `**Checklist**` label with a divider under it. The gate now reads past a bold Part heading, which before ended its Requirements scan, so the old checks never reached a Story split into parts.

### Screenshot columns

A drafted Story still carries no image. On a push, a section's screenshots sit side by side in ClickUp columns, and a task holding columns is never rewritten through `markdown_description`.

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| `AGENTS.md`, `sk-product-owner/SKILL.md`, `references/story-mode.md`, `references/doc-mode.md` | Modify | The four layout rules |
| Both templates, six Story examples, two playbook scenarios | Modify | Shown and graded in the new layout |
| `benchmark/format/` validator, runner, fixtures, README and `benchmark/gates/` parity span | Modify and Create | Gate enforces the layout |
| `../z — Claude Project Sync Loop/` validator, runner, fixtures, `systems.py`, `systems.cjs` | Modify and Create | Shared gate and declaration, in the parent repository |
| `claude project/` kernel, ten knowledge files and README, `SYNC.md` | Modify | Hand-written mirrors and the parity note |
| Version files and two changelogs | Modify and Create | Hub v1.0.36.0, skill v1.2.20.0, kernel v1.2.22 |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

A Story in the new layout was run through the old gate as the red case. Both validators changed through one script so their output stays identical. The formatter's `--write` removed the 31 lower dividers in the sources, and the rest was edited by hand.
An independent review then found four gate edge cases and one gap in Story Mode. The gate cases are fixed in both validators, and each new behaviour has a fixture. An empty line under a `**User flow:**` label no longer ends the run, a `**Checklist**` label outside a numbered section fires, the Requirements scan reads past a `##   ` spacer, and `--write` removes a spacer left after the last Mark-as-done line. Story Mode now states the empty line before a Delivery spacer, which the template already required.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| A Checklist label only over a numbered section's direct checks | A compact group's bold name already labels its checks |
| Delivery after Acceptance criteria keeps its spacer, with no divider above it | The new layout shows no Delivery case, so this follows the no-divider rule, with an empty line before the spacer as the Story template states |
| A closing code fence may sit directly under a Mark-as-done line | A fence ends a shown sample in a README or template |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| `run_gates.sh` | 18 of 19, vendor sync failing with output identical to the baseline |
| `benchmark/format/run_fixtures.sh` | 82 PASS, from 73 |
| Sync Loop `run_fixtures.sh` | 176 PASS, from 167 |
| `reference-parity.cjs` | byte-identical |
| `run_residency.sh` in a scratch clone | PASSED 1 system |
| A Story in the new layout through the gate | passed |
| `check_criteria.sh` in a scratch clone | the same three rows fail as at HEAD, none added |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **Task columns need the browser.** The vendored page writer pastes over a doc page, and the task-editor write for task columns is not in `mcp-click-up` yet. It belongs upstream through `scripts/vendor-sync.py push`.
2. **Old exports fail the lint.** A Story exported before this change reports a divider under each Mark-as-done line until it is refined.
<!-- /ANCHOR:limitations -->

---
