---
title: "Phase Specification: Uniform reference preambles and the restored quality rubric"
description: "Give every non-symlink reference the same seven-key preamble carrying routing and connection information, and restore the six-dimension scoring rubric the DEPTH retirement dropped, extended to the current artifact set and the two always-loaded layers"
importance_tier: "high"
contextType: "specification"
_memory:
  continuity:
    packet_pointer: "008-router-and-skill-slimming/005-preamble-and-quality-scoring"
    last_updated_at: "2026-09-03T00:00:00Z"
    last_updated_by: "claude"
    recent_action: "Preambles standardised on seven keys and the rubric restored across SKILL.md Section 6 and a new ON_DEMAND reference"
    next_safe_action: "Obtain the named human's decision for review-kernel, since both contract inputs already sit ahead of the recorded kernel review"
    blockers:
      - "KERNEL_REVIEW_REQUIRED: contract inputs changed since the recorded review, and review-kernel is out of scope for this phase"
    completion_pct: 100
---
# Phase Specification: Uniform reference preambles and the restored quality rubric

<!-- SPECKIT_LEVEL: 2 -->

---

## 1. METADATA

| Field | Value |
| --- | --- |
| Phase | 005-preamble-and-quality-scoring |
| Parent | 008-router-and-skill-slimming |
| Requirement | Follow-on to R3 |
| Status | Implemented |

---

## 2. SCOPE

Two changes, both landing on the skill's instruction surface.

**Uniform preambles.** The preamble block varied across references: four keys on the mode files, three on `conciseness.md` and `router-contract.md` on the reasoning that a file producing no artifact should omit `Output Path`. Every non-symlink reference now carries the same seven keys. `Output Path` states the absence plainly where there is no artifact, so a reader never has to decide whether a missing key is an omission or a design choice. Three connection keys were added after the original four so a model learns where a file sits in the system from its own header.

**Restored quality rubric.** Retiring DEPTH deleted the six-dimension scoring rubric along with the framework, leaving six blocking floors in `SKILL.md` with nothing defining what any dimension measured. The identity paragraph still asserted six-dimension quality gates, so the skill claimed a system it no longer described.

Out of scope: `human-voice-rules.md` and `hvr-core.md`, which are relative symlinks into the fleet-shared `z — Knowledge/` and are read by nine systems. This system's preamble convention is not theirs to inherit.

---

## 3. THE PREAMBLE KEY SET

Seven keys, uniform across all seven non-symlink references.

| Key | Authority it is derived from | Why it earns its place |
| --- | --- | --- |
| Loading Condition | SKILL.md Resource Loading Levels | Tells a reader whether the file is in context by default or was fetched |
| Purpose | The file itself | What the file is for |
| Scope | The file itself | What is inside, so a reader knows whether to keep reading |
| Output Path | SKILL.md Artifact And Export | Where the artifact lands, or a plain statement that the file writes none |
| Loads With | SKILL.md Resource Loading Levels | Names the other rules simultaneously in play, which a reader of one file cannot otherwise know |
| Routed By | SKILL.md Primary Detection Signal and Semantic Topics | Makes a mis-route visible from inside the file that was loaded |
| Hands Off To | The mode files' own escalation rules | Names the exit edge and its condition, so control flow is readable one file at a time |

`Depends On` was considered and rejected. Its value would have been identical on five of the seven files, naming SKILL.md Section 2 plus the two always-loaded layers, and a key that says the same thing everywhere carries no per-file information. Where it would genuinely have differed it was an authority statement that `Purpose` and `Scope` already carry.

Every key is derivable from a single named authority, which is what makes the block maintainable rather than a second place for facts to rot.

### Asset templates

The seven asset templates keep their existing opening and take no preamble. Each already opens `## 1. OVERVIEW` with `### Purpose` and `### Usage`, and every `Usage` line names the mode that loads the asset and what to do with it. An asset also has no independent loading condition, since the router never selects one on its own: it arrives as the paired half of a routed mode reference, and the Story lane's three scaffolds are selected by a resolved shape rather than by a command. A preamble would restate the pairing four lines above where it already lives and add a second copy of one fact.

---

## 4. RUBRIC PLACEMENT

Split, with the applicable minimum inline and the depth one hop away.

`SKILL.md` Section 6 carries a six-row table: dimension, floor, what it measures, and the test that separates a floor-clearing score from the near miss one band below. The floors are checked on every delivery, so a delivery has to be able to score without fetching anything. A rubric that is only reachable ON_DEMAND would leave the floors undefined in practice, which is the defect being repaired.

`references/quality-scoring.md` carries the depth: the three bands, the per-shape reading, the relationship to the two always-loaded layers, and the revision ladder with a return target per dimension. Putting that in SKILL.md would have spent most of the remaining headroom under 600 lines on material consulted at one point in the flow. The system already splits this way for the router, prose in SKILL.md and the exact algorithm in an ON_DEMAND reference, so following the existing pattern beats inventing a second one.

### Extended beyond the original rubric

- Per-shape reading across the current artifact set. The old rubric predates Story Mode's three shapes and would score an Epic down for absent requirements and fail every correct Story Draft against Story completeness
- The two always-loaded layers. The Human Voice card's blockers are binary and never trade against a dimension score. The conciseness layer's cuts are edits and never scored penalties
- Over-compression as a Clarity failure. Relevance read alone rewards cutting without limit, so Clarity is named as the counterweight, and the reconstruction test is borrowed rather than restated so the two cannot disagree
- Refinement scoring. A refinement is scored on the requested change plus preserved fidelity, never on gaps the source already carried
- Accuracy fed by the Doc source-authority gate. A claim whose subject no supplied source covers is an Accuracy failure rather than a Completeness gap
- Scores stay out of the artifact. The old rubric mandated Quality Score headers inside deliverables, which the current delivery contract bans outright

---

## 5. VERIFICATION

Inherited from the parent, all run and green: router fixtures and the differential harness, the format validator and its fixtures, the held-out probe, the 91 artifacts under `export/z — Test Exports*/`, and SKILL.md under 600 lines. Sync compiler run with the knowledge count moving from 36 to 37 for the one new reference.

One gate is deliberately not cleared. `check --run-validators` reports `KERNEL_REVIEW_REQUIRED`, because both contract inputs were already ahead of the recorded kernel review before this phase began and `SKILL.md` changed again here. Clearing it needs the named human's decision and reason, which no agent can supply.
