---
title: "Receipt: Story Template House-Format Implementation"
description: "Owner overrode the audit's conservative verdict and aligned the Story Mode template to the real house format. Records what shipped in Product Owner Skill v1.5.0 and the sync outcome."
contextType: "reference"
---

# Receipt: Story Template House-Format Implementation

## Decision

The audit in `spec.md` recommended refining the stories and leaving the guidelines mostly unchanged. The owner overrode that: align the template to the real house format, keep the heavier machinery as optional, and add a maximal reference example. This receipt records what shipped.

Owner choices, captured in session:

- Rewrite depth: house shape becomes the default; the per-requirement Connextra value line, Rule block, Which-means-that, and Definition of Ready/Done gates become optional enrichments.
- Add one large example populated with every section and every optional element.
- Run the full change protocol (version bumps, mirror recopy, checksums, changelog, kernel review).

## What shipped (Product Owner Skill v1.5.0)

Source edits under `AI_Systems/Barter/Product Owner/sk-product-owner/`:

- `assets/story-templates.md` v0.102 to v0.200. One house shape (blockquote preamble, `### About`, `### Requirements` with prose lead plus `**Checklist**`, numbered `1\.` Given/When/Then acceptance criteria each closed with `- [ ] Mark as done`), sized by tier. Section 4 is the optional-enrichment catalog. Section 1 documents the `Story - {Platform/Area} - {Feature} - {Name}` H1 with an open BO/BE/FE code set.
- `references/story-mode.md` v0.103 to v0.200. Tiers restated as size only. Acceptance criteria are numbered, not `**Scenario:**` blocks, which retired the create-time scenario-count export gate and resolved its collision with refinement preservation (the audit's E1). A research/spike routing note added (the audit's E3).
- `assets/examples/story/story-example-simple.md`, `-medium.md`, `-complex.md` each v0.100 to v0.200, reshaped and sized to show the enrichment range.
- `assets/examples/story/story-example-complete.md` v0.100, new. The maximal reference: every section and every optional enrichment in one story.
- `SKILL.md` v1.4.0 to v1.5.0. Four surgical carve-outs so the router grammar contract recognizes the Story house format (`- [ ]` checklists, H3 anchors, numbered acceptance criteria, blockquote preamble) distinct from Doc.
- `changelog/v1.5.0.0.md` added.

Kernel and package edits:

- `claude project/Custom Instructions.md` v1.3.0 to v1.4.0: tier guard counts acceptance criteria not scenarios, a new-Story grammar rule, Story routing row names the house format.
- `claude-project.sync.json`: version pins, six mirror renames, the Complete Reference mirror added, `expectedKnowledgeCount` 30 to 31, six superseded names retired.
- `claude project/README.md`: source-to-mirror map, aligned-Skill version, and counts.

## Sync outcome

- `sync --write`: applied 10 changes, regenerated mirrors, the SYNC.md inventory region and the README checksum region.
- Deleted the 6 superseded knowledge mirrors (the compiler never auto-deletes undeclared files).
- `review-kernel`: recorded for the contract-input change.
- `check --system product-owner --run-validators`: **clean**. 31 mirrors, byte parity, checksums, inventory, kernel review all pass.

## Examples: kept fictional

The examples were briefly rebased onto the real Barter stories, then reverted at the owner's call ("too literally Barter"): the light anonymization read as the real tickets with renamed nouns. The final state keeps all 18 examples on generic fictional products, in the new house shape.

- Story examples: Simple = Fieldstack inline project rename; Medium = Lumen profile identity updates (Documentation link plus one Rule block); Complex = Northbeam activity digest pipeline (shared-mechanism section, `← PRIO`, per-requirement value lines, Definition of Done); Complete = Beacon broadcast scheduling and targeting (the maximal reference, every section and enrichment populated).
- Task, bug and doc examples: git-restored to their original fictional versions (Ledgerly, Vantage, Meridian, Prism and the rest), unchanged in shape.
- The v1.5.0 house-format template, story-mode logic, SKILL carve-outs and kernel are unaffected; only example content moved. `sync --write` re-rendered the example mirrors; `check --run-validators` clean.

## Longer Doc example added

Owner asked for a longer document example, modeled on the real Feed how-it-works doc's shape but on a non-feed subject. Added `doc-example-how-it-works.md` (246 lines, prose-first): a system-scale Behavior Reference for a fictional subscription billing lifecycle ("Vantage"), demonstrating the shape off the feed domain with a descriptive paragraph leading every section and each rule, and the When/Then blocks and tables kept as precise support (states, renewal and proration, dunning retries with a grace window, cancellation and pause, a combinations-and-precedence table, worked examples, one unresolved edge). Kept fictional; zero feed or Barter references.

- Registered as the nineteenth example mirror in `claude-project.sync.json`; `expectedKnowledgeCount` 31 to 32; README counts updated.
- `doc-templates.md` section 5 now points at both the short state-machine behavior reference and this longer system-scale one.
- `sync --write` rendered the new mirror; `check --run-validators` clean at 32 mirrors. No contract-input change, so no kernel re-review.

## Not done here

The live claude.ai Project upload is a separate manual step (the compiler validates the local package; it does not upload). The five source stories in the Barter documentation tree were not refined in this pass; those Track A actions in `tasks.md` still stand.
