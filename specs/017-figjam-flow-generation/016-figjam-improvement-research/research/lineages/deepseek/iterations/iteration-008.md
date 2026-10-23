# Iteration 8: Read-back, revision, fileKey reuse, retry and rollback, read directly

## Focus

Read the packet's own revision and failure surfaces in full — `references/flow-mode.md` Sections 5 to 9, `references/quality-rubric.md` and the write routes — and compare them with the corpus's update behavior: `memi-design__mermaid-jam` (preserved positions on update), `ompug__diagram-codebase` (`--resume`, `--update`, one file per run) and `adobe__spectrum-design-data` (bounded regeneration). Addresses Q3 and extends iteration 5 finding 8, iteration 6 finding 11 and iteration 7 finding 5.

## Actions Taken

1. Read `sk-create-figjam/references/flow-mode.md` lines 138 to 254: never invent, the two dials, the shared rules, the hosted and `fj` write routes, read-back, delivery and error recovery.
2. Read `sk-create-figjam/references/quality-rubric.md` in full: type fit, remove test, signal, provenance, check and gate, board, reply.
3. Compared with `memi-design__mermaid-jam` README lines 27 and 83, `ompug__diagram-codebase` README lines 58, 191, 192 and 232, and `adobe__spectrum-design-data` SKILL.md line 161.

## Findings

1. Revision continuity is keyed to the file, not the session: the first call carries no `fileKey` and creates a file, and every later diagram of the same work and every revision passes that file's `fileKey` so the work stays on one board [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:182]. The corpus matches the principle, with `diagram-codebase` reusing one FigJam file for `--resume` and `--update` [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ompug__diagram-codebase/README.md:232].
2. The retry rule is the strongest in the corpus because it refuses to assume failure means nothing landed: a failed or timed-out call is not proof, the target file is read before a retry, the retry happens only when the diagram is absent, and a failed first call has no `fileKey`, so the user is asked to look for a new draft before any retry [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:183]. `figjam-builder` only halves batch size on timeout [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/prasantloki__figjam-builder/SKILL.md:412].
3. Rollback is scoped to what this write created: a new file is its own rollback, an existing board deletes only the nodes and connectors the write created, through `use_figma` and only after the user agrees, and the run stops if a node to delete was not created by this write [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:186]. No corpus source defines a scoped rollback; `diagram-codebase` instead tracks a manifest with Figma ids and a pending action [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ompug__diagram-codebase/docs/DESIGN.md:60].
4. Mismatch repair is ordered and bounded: report the measured counts, delete the created nodes, regenerate with the same `fileKey` only after the user agrees, because a second write beside the first duplicates the diagram, and after two attempts at the same diagram stop and ask what is wrong [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:245].
5. Adobe independently caps regeneration at two attempts on the same complaint and then asks what is specifically wrong or suggests editing in FigJam [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/SKILL.md:161]. Two unrelated skills converging on a two-attempt stop is the strongest evidence in the run that the packet's bound is right, and that unbounded update loops are the failure mode to avoid.
6. Read-back is a model-to-board comparison by count, label, endpoints, direction and the type's own extras, never a memory comparison [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:211], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:212]. The packet then separates a visual read: when only a screenshot could be read, the line says so, because a picture cannot prove which nodes a connector joins [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:215].
7. The rubric's board check is deliberately narrow and visual: one screenshot must show no stretched shape, no cut label and no overlap with existing board content, and nothing may have been moved, resized or restyled after generation [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:76], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:78]. Together with finding 6 this gives two checks on one artifact, structural and visual, a division Adobe collapses into a single critic pass.
8. The plan is fixed before the write for a stated disclosure reason: a board in the wrong plan is visible to that plan's members as soon as it lands [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:253]. No corpus source has a confidentiality gate; `diagram-codebase`'s nearest equivalent is a review file listing what will leave the machine.
9. Extension failure is explicit partial success: the diagram stands and the reply reports what landed and what did not [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:249]. This is the formal version of the link-first rule iteration 4 found in the corpus's board-content planning.
10. Revision is all-or-nothing at diagram granularity: the packet forbids moving a generated node and fixes a bad layout only by splitting or reshaping the model [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:164]. `mermaid-jam` instead preserves manually moved positions on update when ids match and can reset to a deterministic layout [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/memi-design__mermaid-jam/README.md:27], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/memi-design__mermaid-jam/README.md:83], and `diagram-codebase` regenerates only the diagrams affected by changed files [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ompug__diagram-codebase/README.md:192].
11. The `fj` fallback changes read-back semantics: every edge label is its own `fj text` node, which the read-back counts as a label and never as a node [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:196]. The same model therefore produces different counts on the two routes, and the packet says so; the corpus's local plugins hide the distinction.
12. With no route at all the packet refuses a stand-in: it names what is missing, offers the checked model for the user to keep, and never renders the diagram as an image, an HTML page or a Mermaid file [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:203]. Every corpus alternative that hits a wall produces a file instead — Adobe embeds a PNG, `mermaid-jam` writes a board, `figjam-mermaid` emits Mermaid text.
13. The 9-node and 12-connector budget, with split-not-shrink and ordered cuts, is the strictest density rule in the corpus, and the no-move rule is why: a generator that owns layout cannot be rescued by dragging, so the budget protects legibility before the write [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:162], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:170]. The rubric adds a compression step before any split: two nodes that always travel together are one node [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:39].

## Questions Answered

- Q3: How do public projects handle board read-back, revision, fileKey reuse, failure and retry, and delivery, and what does the packet handle differently?

  Answer: the corpus converges with the packet on fileKey continuity and one board per work, and diverges on revision mechanics. Public tools update in place, preserve manual positions and regenerate only affected diagrams; the packet deletes and regenerates a whole diagram, forbids moving generated nodes, and has no partial-update path. On failure the packet is ahead of every corpus source: it reads before retrying, treats a timeout as unknown rather than failed, asks the user to find a first-call draft, and bounds repair at two attempts. Delivery is ahead on honesty (a screenshot read is labelled as visual and cannot prove joins) and behind on reach (no artifact, no image, no file), since the only output is the board URL and read-back.

## Questions Remaining

- Q5: the claude.ai kernel without a Figma connector, and whether a board URL should reach ClickUp through the vendored transport.

## Ruled Out

- Adopting a preserve-positions update model inside Flow Mode: the packet's generator owns layout, so preserved positions cannot be reconciled with its no-move rule without a hand-built route it does not have.
- Replacing the model-to-board read-back with a screenshot-only check: the packet's own rule states a picture cannot prove which nodes a connector joins.

## Dead Ends

- No dead end. The packet's Sections 5 to 9 answered the question directly and the corpus supplied only two genuine divergences.

## Edge Cases

- Contradictory evidence: the packet trusts a screenshot for visual defects but refuses it as proof of joins, while Adobe's critic uses a screenshot as its primary evidence. The two are compatible once the claim under test is separated, and the packet's distinction is the more precise one; the conflict is recorded rather than merged.
- Ambiguous input: none.
- Missing dependencies: none.
- Partial success: extension failure is the packet's own partial-success path and is handled.

## Sources Consulted

- AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md
- AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md
- specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/memi-design__mermaid-jam/README.md
- specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ompug__diagram-codebase/README.md
- specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/SKILL.md
- specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/prasantloki__figjam-builder/SKILL.md

## Assessment

- New information ratio: 0.85
- Questions addressed: Q3
- Questions answered: Q3

## Reflection

- What worked and why: reading the packet's own error-recovery section against the corpus's update sections produced two real divergences (all-or-nothing revision, no partial update) and one convergence worth keeping (the two-attempt stop). The packet is stronger than expected on failure honesty.
- What did not work and why: the rubric's board section is short and mostly repeats the read-back rule; the unique content was one line about overlaps, which needed the write routes to interpret.
- What I would do differently: read the error-recovery section before the write routes, because the recovery rules name the rollback and retry behaviors that make the routes' constraints legible.

## Recommended Next Focus

Iteration 9: read the claude.ai packaging — `AI Systems/Product Owner/claude project/Custom Instructions.md`, the Flow knowledge files, `SYNC.md`'s manual parity method and `mcp-click-up`'s SKILL and tool guide — for Q5: what a Project without a Figma connector can still do, and whether a board URL belongs in a ClickUp task or comment. Builds on iteration 7 finding 12 (link, not attachment) and iteration 8 finding 12 (no stand-in file).
