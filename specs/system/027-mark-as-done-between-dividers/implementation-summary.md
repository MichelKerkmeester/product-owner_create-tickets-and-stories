---
title: "Implementation Summary"
description: "Each Story and Epic Mark-as-done line now sits between two dividers in every template, example, mirror and the format gate."
trigger_phrases:
  - "mark-as-done line between two dividers implementation summary"
importance_tier: "normal"
contextType: "general"
_memory:
  continuity:
    packet_pointer: "system/027-mark-as-done-between-dividers"
    last_updated_at: "2026-11-10T19:30:00Z"
    last_updated_by: "claude-opus-5-5"
    recent_action: "Moved the Mark-as-done rule to two dividers across sources, mirrors and the gate"
    next_safe_action: "Bump versions, commit and run the residency and parity checks"
    blockers: []
    key_files:
      - "sk-product-owner/references/story-mode.md"
      - "claude project/Custom Instructions.md"
      - "benchmark/format/validate-output-format.cjs"
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "77e809ab-7e4a-4669-a9c5-ee0fa5f7617b"
      parent_session_id: null
    completion_pct: 100
    open_questions:
      - "Should the gate enforce only the lower divider? Both are enforced for now"
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
| **Spec Folder** | 027-mark-as-done-between-dividers |
| **Completed** | 2026-11-10 |
| **Level** | 1 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

The Mark-as-done line now sits between two dividers in every Story and Epic shape.

### Mark-as-done line between two dividers

Templates, examples, playbooks, the kernel, the knowledge files and the format gate all carry the new rule, and the gate now reports a missing divider above or below the line.

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| `AGENTS.md`, `sk-product-owner/` rule, template, example and playbook files | Modify | New divider rule |
| `claude project/Custom Instructions.md` and knowledge mirrors | Modify | Same rule in the Project |
| `benchmark/format/`, `../z — Claude Project Sync Loop/` validator, fixtures, statements | Modify and Create | Gate requires both dividers |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

A Sonnet agent changed every surface while the page writer was built. It also added a gate error for a doubled divider and made `--write` insert the missing dividers.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| Enforce both dividers | The band only reads as a band with a rule on each side |
| Leave old exports alone | They are delivered work, refined only on request |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| `run_fixtures.sh` (Product Owner) | 62 PASS |
| Sync Loop fixtures | 157 PASS |
| `validate-output-format.cjs --system product-owner` | exit 0, 73 files |
| `run_gates.sh` | 1 of 15 fails, vendor sync on `mcp-code-mode` |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **Old exports fail the lint.** The Media, Reel Player Story reports 15 missing dividers until it is refined.
<!-- /ANCHOR:limitations -->

---
