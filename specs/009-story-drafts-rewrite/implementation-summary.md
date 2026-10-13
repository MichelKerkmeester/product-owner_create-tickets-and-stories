---
title: "Implementation Summary: Story Drafts two-pass rewrite"
description: "The sixteen Product Owner Story Drafts were rewritten in place as full Stories and the second pass took the format gate 16 of 16 with no hand fixes, with per-screen Requirements groups carrying every hard value from the five context files. The one open item is the per-surface acceptance-criteria ceiling behind Content Gallery - Highlights - Edit Reel UX, and the benchmark left one invalid GLM row and one discarded attempt on the record."
trigger_phrases:
  - "story drafts two-pass rewrite"
  - "lane timings results tsv"
  - "criteria cleanup rerun three stories"
  - "glm flash benchmark invalid run"
  - "per-surface criteria ceiling open"
importance_tier: "normal"
contextType: "general"
_memory:
  continuity:
    packet_pointer: "009-story-drafts-rewrite"
    last_updated_at: "2026-10-13T11:38:50Z"
    last_updated_by: "pi"
    recent_action: "Recorded the sixteen-draft rewrite and the two-pass gate result"
    next_safe_action: "Read README.md for the tsv column meanings and the open criteria ceiling"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "scaffold-009-story-drafts-rewrite"
      parent_session_id: null
    completion_pct: 100
    open_questions:
      - "Per-surface acceptance-criteria ceiling for Content Gallery - Highlights - Edit Reel UX"
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: impl-summary-core | v2.2 -->
# Implementation Summary: Story Drafts two-pass rewrite

<!-- SPECKIT_LEVEL: 1 -->
<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

---

<!-- ANCHOR:metadata -->
## Metadata

| Field | Value |
|-------|-------|
| **Spec Folder** | 009-story-drafts-rewrite |
| **Completed** | 2026-09-08 |
| **Level** | 1 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

All sixteen Story Drafts under `AI Systems/Product Owner/export/Story Drafts/` were rewritten in place as full Stories, twice. The first pass ran with DeepSeek V4 Flash at max thinking on the llmgateway provider, routed through `/agent-router product owner $story`, three lanes at once because each rewrite takes several minutes and the folders are independent. Each rewrite read one draft and the `context.md` beside it as the only source, overwrote that exact file path, wrote no numbered export, and stayed away from the screenshots in that folder, which get embedded in ClickUp later.

### Story Drafts two-pass rewrite

The first pass finished with 16 of 16 drafts exported in place and 15 of 16 gate-clean. Three stories were written before the Delivery-opt-in and hard-value rules landed and had UI mechanics written as acceptance criteria: Content Gallery - Highlights - Edit Reel UX at 13 criteria, Creator - Media Editor at 9 and Onboarding - Birthday at 9. `rerun3.sh` ran those three again from the same source with one extra sentence of steer, asking each rewrite to keep criteria to the few outcomes a user relies on per surface and to move any fixed mechanic such as gesture, angle, ratio or column behaviour into Requirements as a hard constraint.

The second pass ran again from the original drafts and context files only, after the full Story-shape rewrite had landed. 16 of 16 passed the gate with no hand fixes: no Delivery sections written unasked, no image or screenshot references, no design values (pixel sizes, heading levels, button order) in acceptance criteria, no source hedges copied verbatim into Story prose, and all five context files' hard values carried into per-screen Requirements groups. `README.md` points at `Specs/030-system-hardening/product-owner.md` for the full narrative, naming the Social Relink case that drove the hard-value rule; that file carries the sixteen-draft rewrite in its section 9 and the Social Relink case in its section 8.

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| `AI Systems/Product Owner/export/Story Drafts/*/*.md` | Modified | All sixteen drafts overwritten in place as full Stories |
| `run.sh`, `results.tsv` | Created | First-pass script and its sixteen lane, seconds, exit, path rows |
| `rerun3.sh`, `rerun3.tsv` | Created | Second-pass script for the three flagged stories and its three rows |
| `story-benchmark-results.tsv` | Created | Separate one-request benchmark, one row per model |
| `README.md` | Created | Reading guide for the tsv files and the two-pass result |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

Bash only. `run.sh` read `files.txt`, split the draft paths round-robin across lanes 1, 2 and 3, and fired one `pi -p --provider llmgateway --model deepseek-v4-flash:max` call per draft through the router, timing each call and appending a TSV row while that run's stdout went to its own log beside the script. `rerun3.sh` did the same for the three flagged stories, with the extra sentence of steer and its own TSV. The benchmark was a separate single request, run against the same prompt on three models and recorded row by row. The folder's own artifacts are dated 2026-09-08 and `README.md` was last updated 2026-10-13; this record was written afterwards, from those files.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| Rewrite in place instead of writing a numbered export | The prompt asks for it, and the screenshots in each draft folder get embedded in ClickUp later |
| Three lanes at once | Each rewrite takes several minutes and the folders are independent |
| One extra sentence of steer for the second pass, not a new pipeline | Same model and router, and only the criteria had to change |
| Move fixed mechanics (gesture, angle, ratio, column behaviour) into Requirements as a hard constraint | That is what the second-pass prompt asks for, and the prose carries the reasoning |
| Keep the discarded GLM attempt in the benchmark file | It is a record of a run that found and verified a previous export instead of writing one |
| Mark the GLM rerun invalid rather than compare it | It ran during skill edits, shared the gateway with other runs, and searched outside the repository for the screenshots |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| `results.tsv`, first pass | 16 rows, one per draft, exit 0 on every row, 187.7s to 648.7s across three lanes |
| Format gate, first pass | 15 of 16 gate-clean; three stories flagged for criteria that described UI mechanics |
| `rerun3.tsv`, second pass | 3 rows, exit 0: Creator - Media Editor 201.3s, Edit Reel UX 310.9s, Onboarding - Birthday 334.3s |
| Criteria counts, second pass | Dropped to 8, 5 and 6 on the three stories |
| Format gate, second pass | 16 of 16 passed with no hand fixes |
| Content read, second pass | No Delivery sections written unasked, no image or screenshot references, no design values in criteria, no copied hedges, all five context files' hard values carried into per-screen Requirements groups |
| `story-benchmark-results.tsv` | Sonnet 5 high native 115.6s valid, DeepSeek V4 Flash max 424.6s valid, GLM 5.3 Flash max 5,762.2s invalid |
| Pre-rewrite backup | `README.md` names `~/story-drafts-backup-20260908/story-drafts-pre-rewrite.tgz` for all sixteen drafts |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **The work products are outside this folder.** `AI Systems/Product Owner/export/Story Drafts/` holds no such directory in this working tree now, and the backup archive the README names is not on this machine, so the sixteen finished Stories cannot be read back from this record.
2. **The benchmark's GLM 5.3 Flash max rerun is invalid.** It ran during skill edits, shared the gateway with other runs, and searched outside the repository for the screenshots.
3. **The GLM row at 1,458.3s is an earlier, discarded attempt**, kept in the file for the record. That run found and verified a previous export instead of writing one, so it is not counted as a valid comparison point anywhere this data is cited.
4. **The per-surface acceptance-criteria ceiling stays open.** Content Gallery - Highlights - Edit Reel UX still returns a high criteria count, at 13 criteria on a four-surface draft.
5. **The folder does not reconcile that count** with the second-pass counts of 8, 5 and 6 in `rerun3.tsv`'s row set. `Specs/030-system-hardening/spec.md` section 6 carries the 13-criteria reading.
6. **The cited commits do not resolve here.** `README.md` cites commits `84bba2e` through `1d70181` for the Story-shape rewrite, and neither is in the current `main` history of this working tree.
7. **Inputs and logs are missing.** `files.txt`, which `run.sh` reads and the README states is not committed, and the per-run logs `run.sh` writes as `lane$N-$n.txt` are not in this folder.
<!-- /ANCHOR:limitations -->

---
