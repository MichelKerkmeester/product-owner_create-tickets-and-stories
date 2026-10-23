# Iteration 10: Synthesis — twelve ranked improvements, five of them integration changes

## Focus

Close the loop. Rank the improvements the nine prior iterations established, separate the packet-local changes from the integration changes, name the exact Product Owner file each change touches and the corpus or packet evidence it comes from, and state what the evidence does not support. Answers no new key question; it compiles Q1 to Q5.

## Actions Taken

1. Re-read the findings of iterations 1 to 9 from the lineage registry and the iteration files, and grouped them by the surface they change.
2. Ranked each candidate by durability (does it survive a model or tool change), blast radius (how many diagrams or requests it touches) and evidence strength (how many independent sources agree).
3. Rejected candidates the evidence does not support and recorded them below.
4. Wrote the ranked list as the twelfth finding set and mirrored it into `research/research.md`.

## Findings

1. **Rank 1 — replace the accent menu with an accent test and a one-message caption.** The packet lists four candidates for its single accent and never says how to choose [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:47]; Adobe states the test as "the one node the diagram exists to explain", forbids choosing by position, and requires a one-sentence caption that cuts everything not serving it [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md:22], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md:69]. Change `references/style-guide.md` Signal and `references/quality-rubric.md` Section 3, and add the caption to the model and the reply. Evidence: two independent rules, one packet gap, every diagram affected.
2. **Rank 2 — add a redundant-label rule and a neutral ordering ramp.** Adobe drops four or more identical edge labels to zero or one and shows precedence as a light-to-dark neutral step rather than one hue per stage [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md:36], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md:50]. The packet's style guide only says most diagrams need no colour [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:31], and its process and gantt types have no ordering rule. Change `references/style-guide.md` and the type references' judged-by-hand lists.
3. **Rank 3 — add a bounded post-write critic pass.** The packet checks the board for structural counts and for visual defects [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:76], but it never re-reads the rendered board against the diagram's one message; Adobe runs a bounded critic on the Mermaid plus a screenshot, applies findings in one batch and stops [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md:82]. The packet's two-attempt stop already bounds the loop [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:245], so the critic costs one pass. Change `references/quality-rubric.md` Section 6 and `references/flow-mode.md` Section 7.
4. **Rank 4 — emit a run manifest with the model's audit trail.** The reply counts nodes and connectors but leaves no durable record of the fileKey, the node ids written, the pending action or which model items were skipped [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:224]. `diagram-codebase` keeps exactly that as a manifest and a publish review, plus a per-diagram content hash [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ompug__diagram-codebase/docs/DESIGN.md:59], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ompug__diagram-codebase/docs/DESIGN.md:60], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ompug__diagram-codebase/docs/DESIGN.md:175]. Change `references/flow-mode.md` Section 8, `assets/flow-templates.md` and the check script's output; the manifest is the prerequisite for any later revision mode.
5. **Rank 5 — add a coverage and skipped report beside `Left out:`.** `diagram-codebase` records skipped diagram types with reasons and a coverage object of model nodes drawn in which diagram [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ompug__diagram-codebase/docs/DESIGN.md:148]. The packet's only omission record is the `Left out:` line, which reports cuts but not coverage [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:226]. Change the provenance table and the reply contract so every source item is accounted for as drawn, split or skipped with a reason.
6. **Rank 6 — make the budget type-specific instead of one global nine.** The packet applies 9 nodes and 12 connectors to every type [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:162], while the corpus allows 25 nodes and 30 edges, 12–20 for a master, and splits oversized diagrams with every omission in notes [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ompug__diagram-codebase/docs/DESIGN.md:192], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ompug__diagram-codebase/docs/DESIGN.md:193]. The evidence supports per-type caps, not a blanket raise: a gantt with dated milestones and an ER with key fields carry more legitimate nodes than a user flow. Change each `references/types/*.md` budget and the check's per-type limits.
7. **Rank 7 — integration: write the board URL back into the artifact that asked for it.** The Flow reply is terminal and carries the board, its proof and the self-scan and nothing else [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:221], and no surface writes the URL into a Story, Epic, Doc or Task. The Story template already has the exact slot — a `Flows` sub-label under References that may carry supplied links and never an image or path [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/story-template.md:103] — and `hferello` shows the doc-first pattern of finishing the doc, then adding a `## Visual diagram` section with the board link [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/hferello__ai/arch-flow/SKILL.md:170], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/hferello__ai/arch-flow/SKILL.md:173]. Change `sk-product-owner/references/story-mode.md`, `assets/story-template.md` Notes, `references/doc-mode.md` and `references/task-mode.md` so a board produced in the same session counts as a supplied link.
8. **Rank 8 — integration: carry the artifact into Flow Mode as its source.** A Flow request that names an artifact is kept in the Product Owner packet and handed on with no artifact context [SOURCE: AI Systems/Product Owner/SKILL.md:60], so the diagram cannot quote the Story's or Doc's own words. `hferello` makes the markdown doc the source of truth and requires node labels to match it [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/hferello__ai/arch-flow/SKILL.md:166], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/hferello__ai/arch-flow/SKILL.md:168]. Change `sk-create-figjam/references/flow-mode.md` Section 4 to accept an artifact path or body as a source class, and `sk-product-owner/references/router-contract.md` to pass the artifact reference across the handoff.
9. **Rank 9 — integration: define the artifact-then-diagram order at stage one.** Stage one never forms an ordered bundle, so two packets' signals start in the default mode and cost a question [SOURCE: AI Systems/Product Owner/hub-router.json:15], [SOURCE: AI Systems/Product Owner/SKILL.md:79]. When the request names an artifact and a FigJam output, the order is determined: artifact first, diagram from it. Change the hub stage-one rules and `routerPolicy.outcomes`, plus the `ROUTER.md` tie rule that currently loads the artifact set alone [SOURCE: AI Systems/Product Owner/ROUTER.md:37].
10. **Rank 10 — integration: offer ClickUp after a Flow reply, as a link and never an attachment.** The ClickUp offer follows a Deliverable Block, and Flow renders none, so a board can never trigger it in a Project [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:295], [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:250]. The transport supports comments and file attachments, but an attachment is a file upload [SOURCE: AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:102], [SOURCE: AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:150], so the board URL belongs in a task body's `Flows` group or a comment. Change the kernel's Flow Mode Delivery and `sk-product-owner/references/task-mode.md`.
11. **Rank 11 — integration: close the no-connector parity gap and name the model-not-board rule once.** The Flow Knowledge mirror states the rule correctly — offer the checked model, labelled as the model and never as the board, with no image or HTML stand-in [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:168] — while the kernel's sentence offers the block without that qualifier [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:255]. Change the kernel sentence only; the knowledge file already carries the stronger rule.
12. **Rank 12 — define a revision as a scoped rewrite under the same fileKey, and name what cannot be revised.** The packet reuses `fileKey` and deletes only what the write created [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:182], but it has no revision mode: a bad layout is fixed only by splitting or reshaping, never by moving nodes [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:164], while `diagram-codebase` regenerates only affected diagrams [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ompug__diagram-codebase/README.md:192] and `mermaid-jam` preserves moved positions [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/memi-design__mermaid-jam/README.md:27]. Change `references/flow-mode.md` Section 9 to state a revision contract: same fileKey, delete the diagram's own nodes, re-check, re-read, and report what changed.

## What the evidence does not support

- A blanket budget raise from 9 to 25 nodes. The corpus figures come from tools that own layout differently, and the packet cannot move a generated node, so a flat raise would trade legibility for coverage. Only per-type caps are supported.
- An export-and-embed delivery path inside Flow Mode. Adobe's screenshot-and-crop pipeline needs a site build and conflicts with the packet's no-file rule [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:203]; it belongs to a Doc or publication route, not to the board reply.
- Preserving manually moved positions during a revision. That requires the generator to accept external geometry, which the packet's no-move rule and the `generate_diagram` contract both deny.
- Mirroring `mcp-click-up` into the Project. The Project uses its own connector and the CLI verbs do not exist there [SOURCE: AI Systems/Product Owner/SYNC.md:75].
- A screenshot as proof of structure. The packet already states a picture cannot prove which nodes a connector joins [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:215]; Adobe's critic uses screenshots for visual judgment, not for join proof.

## Questions Answered

- None newly. Q1 to Q5 were answered in iterations 5 to 9; this iteration compiles them.

## Questions Remaining

- None. The ranking is the deliverable.

## Ruled Out

- Ranking the source-coverage gaps above the delivery gaps. Coverage reporting is valuable, but the manifest (Rank 4) is what makes coverage trustworthy.
- Proposing a new packet for diagrams. The hub already routes Flow to a sibling packet, and the integration findings are fixes inside existing files.

## Dead Ends

- No dead end. The ranking was constrained by evidence strength, not by missing material.

## Edge Cases

- Contradictory evidence: the corpus's higher budgets versus the packet's nine-node rule. Resolved by per-type caps, not by a flat raise.
- Ambiguous input: none.
- Missing dependencies: kernel v1.2.2 review is pending and is reported as pending, not as reviewed.
- Partial success: the synthesis is complete for the evidence gathered; two corpus areas (the `figma-power` folder and the OpenAI plugins packaging) were sampled rather than read in full and are not cited as evidence here.

## Sources Consulted

- specs/017-figjam-flow-generation/016-figjam-improvement-research/research/lineages/deepseek/iterations/iteration-001.md through iteration-009.md
- specs/017-figjam-flow-generation/016-figjam-improvement-research/research/lineages/deepseek/findings-registry.json
- AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md
- AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md
- AI Systems/Product Owner/sk-product-owner/assets/story-template.md
- AI Systems/Product Owner/claude project/Custom Instructions.md
- specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md
- specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ompug__diagram-codebase/docs/DESIGN.md
- specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/hferello__ai/arch-flow/SKILL.md

## Assessment

- New information ratio: 0.42
- Questions addressed: Q1 to Q5
- Questions answered: none newly

## Reflection

- What worked and why: ranking by durability and blast radius rather than by novelty surfaced the accent test and the artifact link-back as the two changes with the widest effect for the smallest edit. The integration items clustered naturally once each was tied to a file that already has a slot for it.
- What did not work and why: the corpus repeatedly suggested a higher budget, but the packet's no-move rule makes those numbers non-transferable; the ranking had to resist the loudest evidence.
- What I would do differently: write the "what the evidence does not support" section before ranking, because it removed three candidates early and kept the list honest.

## Recommended Next Focus

None. The lineage reaches `config.maxIterations` with all five key questions answered and the ranking delivered in `research/research.md`.
