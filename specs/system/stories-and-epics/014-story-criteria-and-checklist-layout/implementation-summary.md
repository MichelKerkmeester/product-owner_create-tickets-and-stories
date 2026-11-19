---
title: "Implementation Summary"
description: "New Stories and Epics now use the new house layout: no divider under a Mark-as-done line, a Checklist label over each requirement section's checks, split user flows and screenshots in columns on a push. Copy read off a screenshot or design stays in the design, and the gate advises when a Story quotes many UI strings."
trigger_phrases:
  - "story criteria and checklist layout implementation summary"
importance_tier: "normal"
contextType: "general"
_memory:
  continuity:
    packet_pointer: "system/stories-and-epics/014-story-criteria-and-checklist-layout"
    last_updated_at: "2026-11-16T18:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Added the design-copy rule and gate advisory"
    next_safe_action: "Upload kernel v1.2.23 and the changed knowledge files to the Claude Project"
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
| **Spec Folder** | 014-story-criteria-and-checklist-layout |
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

### Design copy

Copy the requester types travels verbatim. Copy read off a screenshot or design stays in the design, apart from the one string the requester says is the change, which is quoted once. A rule and a Given, When or Then line name an element by its role, such as the primary action or the confirmation toast. Both gates now advise when a Story or Epic quotes twelve or more distinct copy-like strings in Requirements and Acceptance criteria, and the narration check's repair strikes the item instead of quoting the copy into it.

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| `AGENTS.md`, `sk-product-owner/SKILL.md`, `references/story-mode.md`, `references/doc-mode.md` | Modify | The four layout rules |
| Both templates, six Story examples, two playbook scenarios | Modify | Shown and graded in the new layout |
| `benchmark/format/` validator, runner, fixtures, README and `benchmark/gates/` parity span | Modify and Create | Gate enforces the layout |
| `../z — Claude Project Sync Loop/` validator, runner, fixtures, `systems.py`, `systems.cjs` | Modify and Create | Shared gate and declaration, in the parent repository |
| `claude project/` kernel, ten knowledge files and README, `SYNC.md` | Modify | Hand-written mirrors and the parity note |
| Version files and two changelogs | Modify and Create | Hub v1.0.36.0, skill v1.2.20.0, kernel v1.2.22 |
| `story-mode.md`, `story-template.md`, the sectioned example, their three mirrors and the kernel Story paragraph | Modify | The copy split and naming by role |
| Both validators, `systems.cjs`, `systems.py`, two fixtures per folder, both runners and the format README | Modify and Create | The design-copy advisory, the narration repair and the declaration |
| Version files, two changelogs and `SYNC.md` | Modify and Create | Hub v1.0.37.0, skill v1.2.21.0, kernel v1.2.23 |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

A Story in the new layout was run through the old gate as the red case. Both validators changed through one script so their output stays identical. The formatter's `--write` removed the 31 lower dividers in the sources, and the rest was edited by hand.
An independent review then found four gate edge cases and one gap in Story Mode. The gate cases are fixed in both validators, and each new behaviour has a fixture. An empty line under a `**User flow:**` label no longer ends the run, a `**Checklist**` label outside a numbered section fires, the Requirements scan reads past a `##   ` spacer, and `--write` removes a spacer left after the last Mark-as-done line. Story Mode now states the empty line before a Delivery spacer, which the template already required.
The design-copy rule started from a measurement. One Story built from screenshots quoted 17 distinct UI strings, while 262 graded benchmark Stories built from typed notes quoted at most 8, so the advisory fires at 12. The JavaScript check was run over the same files and matched the first count exactly. The old validator printed no advisory on the new violation fixture, which is the red case.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| A Checklist label only over a numbered section's direct checks | A compact group's bold name already labels its checks |
| Delivery after Acceptance criteria keeps its spacer, with no divider above it | The new layout shows no Delivery case, so this follows the no-divider rule, with an empty line before the spacer as the Story template states |
| A closing code fence may sit directly under a Mark-as-done line | A fence ends a shown sample in a README or template |
| The design-copy check advises and never blocks | Michel chose advisory, because the gate cannot tell copy the requester typed from copy read off a design |
| Count distinct strings, not every span | Typed briefs repeat a few status names many times, which a raw count mistook for transcription |
| The sectioned example names its empty states by role | It quoted two empty-state strings from its design, which the new rule forbids |
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
| Design copy: `benchmark/format/run_fixtures.sh` | 84 PASS, from 82 at HEAD |
| Design copy: shared `run_fixtures.sh` through each system's entry | 181 PASS, from 178 at HEAD, 0 FAIL in all three |
| Design copy: `reference-parity.cjs` | byte-identical |
| Design copy: `run_gates.sh` | 18 of 19, vendor sync failing as before |
| Design copy: residency, `validate_parity.py product-owner` and `pair_divergence.py --all` in a scratch clone | PASSED 1 system, PASSED 68/68 pairs, PASSED 7 systems |
| Design copy: the old validator on `design-copy-violation.md` | no advisory, the red case |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **Task columns need the browser.** The vendored page writer pastes over a doc page, and the task-editor write for task columns is not in `mcp-click-up` yet. It belongs upstream through `scripts/vendor-sync.py push`.
2. **Old exports fail the lint.** A Story exported before this change reports a divider under each Mark-as-done line until it is refined.
<!-- /ANCHOR:limitations -->

---
