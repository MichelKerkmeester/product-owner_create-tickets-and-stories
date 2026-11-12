---
title: "Implementation Summary"
description: "A Story now points at the design for a designed screen's copy instead of writing one requirement per visible string, in the skill and in two Claude Project knowledge files."
trigger_phrases:
  - "design copy pointer requirements implementation summary"
importance_tier: "normal"
contextType: "general"
_memory:
  continuity:
    packet_pointer: "system/033-design-copy-pointer-requirements"
    last_updated_at: "2026-11-12T15:10:00Z"
    last_updated_by: "claude-code"
    recent_action: "Changed the Story design copy rule in the skill and the Project mirrors"
    next_safe_action: "Upload the two changed knowledge files to the Claude Project"
    blockers: []
    key_files:
      - "sk-product-owner/references/story-mode.md"
      - "sk-product-owner/assets/story-template.md"
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "ea1d6c8f-a3bd-4c7e-aa69-94dcca4ee626"
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
| **Spec Folder** | 033-design-copy-pointer-requirements |
| **Completed** | 2026-11-12 |
| **Level** | 1 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

A Story for a new screen no longer lists every badge, heading and button label as its own requirement. The screen gets one item saying its copy and layout follow the design, and the other items hold only what a design cannot show.

### Design copy pointer requirements

Story Mode used to say the verbatim rule binds copy the source shows as much as copy it types. That made every string in a Figma frame or a screenshot a supplied value, and the per-screen count rule then asked for one item each. The rule now binds a string the source types and a shown string that is itself the change, such as replaced copy.

A new screen or component supplied as a design keeps its copy in the design. Its group holds the pointer item and then an order, a condition, a navigation target, a state, a platform or a reuse entry. A string is quoted only where it names the element a rule is about.

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| `sk-product-owner/references/story-mode.md` | Modified | Narrowed verbatim rule, new design pointer rule, item count |
| `sk-product-owner/assets/story-template.md` | Modified | Strike rule for quoted design strings, design pointer note |
| `claude project/knowledge/Product Owner - Templates - Story Mode.md` | Modified | Same sentences as the Story Mode source |
| `claude project/knowledge/Product Owner - Assets - Story Template.md` | Modified | Same sentences as the template source |
| `SKILL.md`, `hub-router.json`, `mode-registry.json`, `description.json` | Modified | Hub 1.0.34.0 |
| `sk-product-owner/SKILL.md`, `sk-product-owner/README.md` | Modified | Skill 1.2.19.0 |
| `README.md`, `claude project/README.md` | Modified | Version lines and release links |
| `changelog/v1.0.34.0.md`, `sk-product-owner/changelog/v1.2.19.0.md` | Created | Release notes |
| `SYNC.md` | Modified | Dated parity note |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

The gate runner ran first and printed `all 19 gates pass`. One script applied each replacement to a source and its mirror and stopped unless the old text matched exactly once. The gate runner ran again and printed the same line. The residency check then failed with 3 findings on a kernel clause and a quality-scoring edit, both were backed out, and the rerun printed `PASSED 1 system(s)`.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| Point at the design instead of quoting it | A list of the design's strings is a second copy of the design, and it goes stale the day the design changes |
| Keep typed values and changed strings verbatim | A value in a build or a translation file with no design behind it still has to arrive exact |
| Leave the kernel at v1.2.21 | It says an item carries its supplied value verbatim and leaves what counts as supplied to Story Mode |
| Leave two pinned statements as written | A rewrite needs a resync of the shared declaration in the parent repository, which is outside this system |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| `bash benchmark/gates/run_gates.sh` before the edits | `all 19 gates pass` |
| `bash benchmark/gates/run_gates.sh` after the edits | `all 19 gates pass` |
| `bash benchmark/parity/run_residency.sh` | `PASSED 1 system(s), every declared statement owned and placed` |
| Old sentences in the two sources | 1 each at `HEAD`, 0 each now |
| `Never write one item per visible string` | 1 in each source and each mirror |
| Changed lines, source against mirror | `diff` prints nothing for both pairs |
| `bash benchmark/parity/run_parity.sh` before the commit | Reported only the four edited rule files as differing from `HEAD` |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **No model run proves the behavior.** The gates check wording and parity. Write one Story from a design to confirm the list is gone.
2. **Two pinned statements still speak of quoting.** The quality-scoring line asks for every supplied hard value verbatim, and the moved statement in `task-mode.md` says screenshot copy is quoted verbatim or dropped. Neither contradicts the new rule, but rewording them needs a resync of the shared declaration.
3. **No playbook scenario covers a designed screen.** The fixtures hold text only, so a scenario needs an image fixture first.
<!-- /ANCHOR:limitations -->

---
