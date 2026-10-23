---
title: "Implementation Summary"
description: "Ten DeepSeek iterations on 22 public FigJam repos and the Product Owner integration ended in 12 ranked changes, 5 of them on how sk-create-figjam and sk-product-owner hand work to each other."
trigger_phrases:
  - "figjam improvement research implementation summary"
importance_tier: "normal"
contextType: "general"
_memory:
  continuity:
    packet_pointer: "017-figjam-flow-generation/016-figjam-improvement-research"
    last_updated_at: "2026-10-20T21:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Wrote and verified the synthesis"
    next_safe_action: "The operator chooses which ranked changes to apply"
    blockers: []
    key_files:
      - "research/research.md"
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "1004bf13-7863-4447-a63e-6ad2f5fcfd86"
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
| **Spec Folder** | 016-figjam-improvement-research |
| **Completed** | 2026-10-20 |
| **Level** | 2 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

You now have 12 ranked changes for sk-create-figjam and its integration, each traced to a source line and to the Product Owner line it would change. Three lead: write a verified board URL back into the artifact's `Flows` group, stop the router dropping a FigJam diagram asked for beside an artifact, and name how the hosted Figma route is reached.

### The run

One DeepSeek V4.1 Flash lineage ran 10 iterations at max reasoning through cli-pi and llmgateway, on 15 newly pinned repos and seven from phase 009. A fresh Opus 5.5 high agent opened every cited line it used, ran the check self-test, the router oracle and a GitHub compare of the two Figma pins, and wrote `research/research.md`. It corrected or dropped 18 iteration claims, most of them claimed absences the packet already covers.

### The extension

On 2026-10-21 a second DeepSeek V4.1 Flash max lineage ran 5 more iterations against the packet as phases 017 to 028 left it. A Luna lineage started first and was stopped in its first iteration when the operator switched to DeepSeek. A fresh Opus 5.5 high agent wrote `research/research.md` Section 9. It finds 8 of the 12 implemented ranks wanting, holds ranks 4, 7, 10 and 11, ranks five more changes as 13 to 17 and corrects or drops 20 iteration claims. The lead finding is that a Doc or Bug asked for beside a FigJam board still routes to FLOW alone, and seven pair phrasings still drop the board.

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| research/ | Created | The lineage, the merged registry, the git-ignored corpus and the synthesis |
| scratch/ | Created | The topic, the fan-out matrix, the pins and the runner output |
| spec.md, plan.md, tasks.md, acceptance-criteria.md, goal.md | Created | The phase docs |
| ../spec.md, ../goal.md | Modified | The phase map, handoff and binding rows |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

The run was staged at `specs/z-staging-po-016-research` in the outer repository, as 009 was, because the runner refuses symlinked spec paths and running inside Product Owner loads its persona. `fanout-run.cjs` ran the lineage with the stop policy at max-iterations and convergence off, and `fanout-merge.cjs` merged 119 key findings. The research folder was copied here, staging paths in the markdown were repointed and the staging folder was deleted.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| One DeepSeek lineage | Parent D4 names DeepSeek first and the operator asked for it |
| The 009 corpus copied beside the new repos | The integration and the upstream diff need the earlier sources in view |
| Figma's guide re-pinned at 056adaf7 | The upstream question needs the current commit, and the compare shows one commit between the pins |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| State log | 10 iteration records, stopReason maxIterationsReached, fanout exit 0 |
| Citations per iteration | 20 to 47 SOURCE tags each, none below 1 |
| Synthesis citations | Every SOURCE tag in research.md resolves to an existing file |
| Orchestrator spot-checks | The router returns STORY with no question for a story plus FigJam request, `mcp-wiring.md` calls the hosted server not a supported path, the four artifact templates carry a `Flows` group, the kernel ClickUp offer reads "Outside Flow Mode", and the GitHub compare shows one commit adding `mcp.json` and `plugin.json` |
| Scope | No Product Owner source file changed, and the outer repository's `specs/` is clean after the staging folder was deleted |
| Extension run | 5 iteration records, stopReason maxIterationsReached, fanout exit 0, 12 to 28 SOURCE tags per iteration, 43 merged key findings |
| Extension spot-checks | The router sends "write a doc about onboarding and draw it on a figjam board" and "write a bug about it and add a figjam diagram" to FLOW with no then, "…, then make a FigJam flow" and "plus a figjam diagram" to STORY with no then, and a model with four connectors labelled then passes flow_check.py with exit 0 |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **Thirteen claims stay unverified.** research.md Section 7 lists them, among them which tools the claude.ai Figma connector exposes and whether `use_figma` can tag generated nodes.
2. **Eight corpus repos were never cited.** research.md names them.
3. **The CLI lineage records carry no route-proof fields.** 009's DeepSeek lineage has the same shape, so this comes from how CLI lineages run.
<!-- /ANCHOR:limitations -->
