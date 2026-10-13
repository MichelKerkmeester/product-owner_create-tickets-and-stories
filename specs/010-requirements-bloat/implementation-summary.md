---
title: "Implementation Summary: Requirements bloat in Story Mode"
description: "The review names why narrative UI description passes into Requirements, measures it at 28 of 221 bullets, gives a build-can-fail test, sixteen proposed edits and a narration check measured at zero false positives."
trigger_phrases:
  - "requirements bloat review"
  - "story requirements description rate"
  - "build can fail requirements test"
  - "narration check zero false positives"
importance_tier: "normal"
contextType: "general"
_memory:
  continuity:
    packet_pointer: "010-requirements-bloat"
    last_updated_at: "2026-10-13T13:02:45Z"
    last_updated_by: "claude-code"
    recent_action: "Wrote findings.md with the rule conflict, the corpus counts and the proposed edits"
    next_safe_action: "Apply the proposed edits and resync the three Claude Project knowledge files"
    blockers: []
    key_files:
      - "findings.md"
      - "brief.md"
      - "run.log"
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "scaffold-010-requirements-bloat"
      parent_session_id: null
    completion_pct: 100
    open_questions:
      - "Whether a second edit to SKILL.md and Custom Instructions.md is authorized so their gate rosters match the new rule"
    answered_questions:
      - "The carry-through rule wins because it names a defect while the hard-constraint rule excludes only a Checklist and a user outcome"
      - "Bloat tracks the absence of stated values in the source, 10.4% where a folder ships screenshots only against 1.4% for the context.md folders excluding ReAuth"
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
| **Spec Folder** | 010-requirements-bloat |
| **Completed** | Not recorded in this folder. |
| **Level** | 1 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

The review answers why narrative UI description passes into Requirements and what to do about it. Four of the five bullets under `Initial Instagram Sheet` in `Highlights - Onboarding - Instagram ReAuth.md` report what the screenshot says, shows or contains rather than stating a constraint, and the two rules that govern the section point in opposite directions.

### Requirements bloat in Story Mode

Requirements is supposed to hold hard constraints only. The carry-through rule at `story-mode.md:79` orders every source line into the draft and names an omitted line a defect. The hard-constraint rule at `story-mode.md:116` excludes exactly two shapes, a `**Checklist**` and a user outcome, and narrative UI description is neither. Bloat tracks the absence of stated values in the source, at 10.4% description where a folder ships screenshots only against 1.4% for the `context.md` folders excluding ReAuth. The proposed repair is a test a model applies without judgement. A Requirements bullet must be a sentence a build can fail, so a bullet reporting what a screen says, shows or contains, naming no value, limit, condition, effect or named flow a build could get wrong, is description and is struck rather than reworded.

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| `findings.md` | Created | The one deliverable, 593 lines holding the seven answers |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

One dispatched review. `run.sh` runs `claude -p --model claude-opus-5 --effort xhigh` on `brief.md` and writes `run.log`, which closes with `exit=0 seconds=868`. The run read only, ran the format gate and the fixtures, and wrote `findings.md`. `run.log` records that nothing outside the folder changed, that no sync compiler ran and that nothing was committed.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| Propose edits rather than apply them | The brief demanded a review and forbade edits outside the folder |
| Do not propose a broad description heuristic | Two candidates measured 0.15 and 0.38 precision on the corpus, and `run_fixtures.sh` states that a gate which misfires gets switched off |
| Name the narration check a copy-paraphrase check | Recall against the full description class is 0.16, so calling it a description check would mislead |
| Drop screen description entirely | The References design link already carries it, and a prose copy goes stale when the design moves |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| Format gate and fixtures at baseline | PASS, recorded in `run.log` |
| Narration check on the 221-bullet corpus | 3 true positives, 0 false positives, precision 1.00 |
| Narration check on the worked examples, exported PRDs and knowledge mirrors | 0 findings across 93 bullets |
| Fixture pair | Violation fixture produces exactly two findings, exempt fixture produces none |
| Files outside this folder | None changed, no sync compiler, nothing committed (`run.log`) |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **Proposals only.** No skill or Claude Project file changed, so the bloat reproduces until a follow-up pass applies the sixteen edits.
2. **No general check.** The wider description class is not mechanically separable, so Requirements still needs a reader.
3. **Gate roster gap.** `SKILL.md:388` and `Custom Instructions.md:214` stay narrower than the proposed rule until a second edit to each file is authorized.
4. **Mirrors not resynced.** The three derived Claude Project knowledge files carry edits A to C, D to M and P and stay stale until the follow-up resync.
<!-- /ANCHOR:limitations -->

---
