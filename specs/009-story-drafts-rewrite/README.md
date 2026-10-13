# 054 - Story Drafts rewrite

Sixteen Story Drafts under `AI Systems/Product Owner/export/Story Drafts/` were
rewritten twice with DeepSeek V4 Flash at max thinking via llmgateway, routed
through `/agent-router product owner $story`, three lanes running in parallel
because each rewrite takes several minutes and the folders are independent.

Full narrative, including the Social Relink case that drove the hard-value
rule, is in `Specs/030-system-hardening/product-owner.md` section 9. This file
covers only what the tsv files record and how to read them.

## Files

- `run.sh` - the first-pass script. Reads `files.txt` (not committed, one
  draft path per line), splits it three ways round-robin across lanes 1, 2
  and 3, and rewrites each draft in place as a full Story from that draft and
  its sibling `context.md`, with no numbered export and no reference to the
  folder's screenshots.
- `results.tsv` - the first-pass timings. Columns: `lane`, `seconds`, `exit`,
  `file`. Sixteen rows, one per draft, ranging from 187.7s to 648.7s. This
  pass ran before the Delivery-opt-in and hard-value rules landed
  (`Specs/030-system-hardening/product-owner.md` sections 5 and 6). 16 of 16
  exported in place, 15 of 16 passed the format gate. Three needed a second
  pass because UI mechanics had been written as acceptance criteria: Content
  Gallery - Highlights - Edit Reel UX (13 criteria), Creator - Media Editor (9)
  and Onboarding - Birthday (9).
- `rerun3.sh` - the second-pass script for exactly those three stories. Same
  model and router, one extra sentence of steer asking each rewrite to keep
  criteria to the few outcomes a user relies on per surface and move any fixed
  mechanic (gesture, angle, ratio, column behaviour) into Requirements as a
  hard constraint.
- `rerun3.tsv` - the second-pass timings for those three stories. Columns:
  `seconds`, `exit`, `file`. Criteria counts dropped to 8, 5 and 6
  respectively.
- `story-benchmark-results.tsv` - a separate, one-request benchmark, not part
  of the sixteen-draft rewrite. Columns: `model`, `seconds`, `exit`, `bytes`.
  Three models run against the same request on the hardened Story shape:
  "creators upload a proof video to a deal, 1GB, HLS, instant adaptive
  playback, two screenshots named". Sonnet 5 high native finished in 115.6s
  valid, DeepSeek V4 Flash max in 424.6s valid, GLM 5.3 Flash max in 5,762.2s
  invalid (it ran during skill edits, shared the gateway with other runs, and
  searched outside the repository for the screenshots). The `glm-5.3-flash-max`
  row at 1,458.3s is an earlier, discarded attempt kept in the file for the
  record: that run found and verified a previous export instead of writing
  one, so it is not counted as a valid comparison point anywhere this data is
  cited.

## The two-pass result

First pass, before the Delivery and hard-value rules: 16 of 16 exported, 15 of
16 gate-clean, three needed acceptance-criteria cleanup.

Second pass, run again from the original drafts and context files only, after
the full Story-shape rewrite (`Specs/030-system-hardening/product-owner.md`,
commits `84bba2e` through `1d70181`) had landed: 16 of 16 passed the gate with
no hand fixes. No Delivery sections were written unasked, no image or
screenshot references appeared, no design values (pixel sizes, heading levels,
button order) leaked into acceptance criteria, no source hedges were copied
verbatim into Story prose, and all five context files' hard values carried
into per-screen Requirements groups.

The one story that still returns a high criteria count after the second pass,
Content Gallery - Highlights - Edit Reel UX at 13 criteria on a four-surface
draft, is the case behind the open per-surface criteria ceiling recorded in
`Specs/030-system-hardening/spec.md` section 6.

The pre-rewrite backup of all sixteen drafts is
`~/story-drafts-backup-20260908/story-drafts-pre-rewrite.tgz`.
