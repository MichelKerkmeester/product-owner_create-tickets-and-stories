---
title: "Implementation Summary: Held-out review of Creator - Deals - Saved Deals Shelf"
description: "The held-out artifact is the only one of seventeen stories that fails the format gate, and the Requirements rule failed on the one paraphrase it was rewritten to catch. The report ranks the repairs, names the phrase list that catches the bullet, and recommends moving the source into a tracked holdout folder."
trigger_phrases:
  - "saved deals shelf artifact fails format gate"
  - "requirements bullet paraphrase survived"
  - "holdout fixture location"
  - "story mode requirement changes"
  - "held-out review findings"
importance_tier: "normal"
contextType: "general"
_memory:
  continuity:
    packet_pointer: "011-holdout-review"
    last_updated_at: "2026-10-13T13:09:36Z"
    last_updated_by: "pi-worker"
    recent_action: "Wrote the Level 1 retrospective docs from the folder's brief, findings and run log"
    next_safe_action: "Apply the ranked repairs and move the held-out source into benchmark/holdout/"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "scaffold-011-holdout-review"
      parent_session_id: null
    completion_pct: 100
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: impl-summary-core | v2.2 -->
# Implementation Summary

<!-- SPECKIT_LEVEL: 1 -->
<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

---

<!-- ANCHOR:metadata -->
## Metadata

| Field | Value |
|-------|-------|
| **Spec Folder** | 011-holdout-review |
| **Completed** | 2026-09-09 |
| **Level** | 1 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

A read-only review of the held-out artifact `Creator - Deals - Saved Deals Shelf` and of the rules that produced it. The report lives in `findings.md`, and `run.log` carries the printed copy and the closing `exit=0 seconds=842` line.

### Held-out review of Creator - Deals - Saved Deals Shelf

The artifact is the only one of seventeen stories under `export/Story Drafts/` that fails the format gate, on a prose semicolon at `:44`. Seven of the eight trap families held. The Requirements rule failed on the one paraphrase it was rewritten to catch, because the source sentence survived into the artifact with its verb intact. The smallest repair that catches it is a named phrase list rather than a further principle, and the list was already written and measured in `AI Systems/Product Owner/specs/010-requirements-bloat/findings.md` section 6.2. The review also found the ReAuth story does not prove the rule generalises, since its Requirements group is byte-identical to the four-line worked example the rules print.

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| `brief.md` | Created | The review brief, with the reading list, the trap families and the six advisory questions |
| `run.sh` | Created | The runner that dispatched the reviewer and captured `run.log` |
| `run.log` | Created | The printed report and the closing `exit=0 seconds=842` line |
| `findings.md` | Created | The report, with the trap verdicts, the measurements and the ranked changes |
| `export/Story Drafts/Creator - Deals - Saved Deals Shelf/Creator - Deals - Saved Deals Shelf.md` | Reviewed, not changed | The held-out artifact, judged section by section |
| `sk-product-owner/references/story-mode.md`, `sk-product-owner/assets/story-template.md`, `benchmark/format/validate-output-format.cjs` | Reviewed, not changed | The rules and the gate, which carry the P0 to P3 proposals |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

One reviewer run from `run.sh`, with `brief.md` as the prompt. The format gate and its fixture suite were baselined first, then the gate ran over the artifact and all seventeen stories, and a Python pass measured the proposed phrase list over 261 bullets in those stories and 67 in the worked examples, the knowledge mirrors and the numbered exports.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| Judge the rules as well as the artifact | The brief asked for both, and the ReAuth story showed the rule had only been proved against the exemplar the rules print |
| Recommend a phrase list over a further prose principle | Two commits had already stated and illustrated the principle and the holdout reproduced the failure, so the repair has to be mechanical |
| Keep the list at four verbs | Widening it took the corpus from 1 hit to 17, and 16 of the 17 are legitimate constraints |
| Recommend moving the source into `benchmark/holdout/` | The source and the artifact are one file under a masked export tree, so a rerun would see the answer and the fixture can be lost |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| `node benchmark/format/validate-output-format.cjs` on the artifact | FAIL, exit 1 at `:44`, a prose semicolon in a Requirements bullet |
| The same gate on the other sixteen stories | PASS, exit 0 |
| `bash benchmark/format/run_fixtures.sh` at baseline | PASS, fixtures 18/18 |
| Python pass over 328 Requirements bullets for the proposed phrase list | 1 hit, the bullet under review, precision 1.00 |
| Widened verb list over the same corpus | 17 hits, 16 of them legitimate constraints, so the list stays at four verbs |
| Reviewer run | `exit=0 seconds=842` |
| Scope check via `git status` against `AI Systems/Product Owner/` | Nothing outside this folder modified, nothing committed |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **Low recall.** The phrase list is a copy-paraphrase check, not a description check. It catches a bullet that reports a screen says something without saying what. It does not catch a layout inventory.
2. **The repairs are proposals.** Nothing outside this folder was edited, so the format-gate failure, the surviving paraphrase and the dropped bookmark-icon change are still in the corpus.
3. **The held-out source is untracked.** `.gitignore:68` masks `**/export/*`, and the source sits in the same tree as the artifact, so the only source the skill has never seen can be lost and a rerun can read its own answer.
<!-- /ANCHOR:limitations -->

---
