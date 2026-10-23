# Iteration 12: stress-testing the accent and subgraph rows, and fitting new rules into the checker's self-test

## Focus

Two of iteration 11's rows are weaker than the rest. This iteration tests whether "accent family" is implementable at all, decides the subgraph policy on evidence rather than on the corpus's disagreement, and maps the four mechanical checks onto `flow_check.py`'s existing structure. Deepens iterations 10 and 11 and the corpus conflict recorded in iteration 8.

## Actions Taken

1. Read `flow_check.py` in full: constants, `diagram_problems`, `GOOD`, `PLANTED`, `self_test`.
2. Read the official subgraph guidance and rocket-path's and Mermaid Jam's positions side by side.
3. Tested whether "accent family" can be defined without a palette.
4. Drafted the planted models each new rule needs.

## Findings

1. **"Accent family" is not implementable as written.** A family needs a membership rule — hue distance, a named palette, or a role map — and Flow Mode has none of the three. Any threshold would be arbitrary and untestable, so iteration 10's recommendation is withdrawn: the check stays at one hex until a palette exists [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:45] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/IamTheLime__dotfiles/agents/skills/figjam-diagrams/references/themes.md:26]. This is the iteration's main correction.

2. **One hex remains the right unit for a nine-node flow.** Colour in Flow Mode marks the happy path or one decision, and the model carries no role vocabulary for note or warning. Counting hexes is exact, self-testable and matches the product rule; counting families would be a new spec with a new failure mode [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:88]. If a palette is ever added, it belongs in `flow-templates.md` and the check should count roles, not hexes.

3. **Subgraph verdict: reject explicitly.** Three independent reasons converge. At nine nodes a subgraph grouping is rarely worth its visual weight, the official guidance itself says not to subgraph a pair and to reserve subgraphs for 3+ related nodes; the official subgraph recipe requires per-subgraph tint fills, which collide with the one-accent rule; and it advertises per-subgraph direction overrides, which collide with the TD-only rule [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:146] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:169]. Mermaid Jam's rejection supplies the precedent [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/src/parser/mermaidJam.ts:23].

4. **Supporting subgraphs would cascade into three rule changes, not one.** The official guidance couples subgraphs to tinted fills, per-subgraph direction and node-to-node edges rather than subgraph-to-subgraph edges [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:153] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:157]. Adopting it would mean relaxing the accent rule, the direction rule and the connector rule at once — a product redesign, not a fix. Rejection is the smaller, more coherent choice.

5. **The four mechanical checks fit the checker's existing shape.** Each is a constant plus a condition inside `diagram_problems`, exactly like `MARKUP_MARKS` and `MAX_NODES` [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:40] [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:57]. No new dependency is needed: node IDs and labels are already on `diagram.nodes`, and `block_text` is already passed for the accent check.

6. **The subgraph check must read `block_text`, like the accent check.** The extractor drops styling lines, so the raw block is the only reliable place to spot a `subgraph` keyword and its closing `end` [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:46]. A regex anchored at line start is enough; it does not need to parse nesting.

7. **The reserved-ID check needs whole-word, case-insensitive matching.** `end` must trip `end`, `endNode` and `END`, but not `ending` or `weekend`. Mermaid keywords are lowercase and reserved in node position, so the match should be on the node ID token, not a substring [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/lint.py:37].

8. **The emoji check should scan labels and edge labels together.** `MARKUP_MARKS` is applied to both today, and an emoji in a decision exit label breaks the same way as one in a node [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:66] [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:78]. A single emoji range test in one helper keeps the two paths consistent.

9. **Label length should be a hard error at 80 characters.** ompug truncates at 80 and Mermaid Jam simplifies at 120; for nine-node diagrams read on a board, 80 is the readable bound, and a hard error is testable where a warning is not [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/build.py:25] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/src/shared/reviser.ts:138]. The rule should count characters after trimming, not bytes.

10. **Every new rule needs its own planted model.** `self_test` proves each rule fails on a planted case and the good model passes; adding a check without a `PLANTED` entry silently weakens the suite [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:119] [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:160]. The four needed models are an emoji label, a reserved-ID node, an underscore ID and an 81-character label; the subgraph rejection needs a fifth with `subgraph`/`end`.

11. **The existing `GOOD` model survives all five additions.** It uses four nodes, short labels, no emoji, camelCase IDs and one accent, so the new checks do not require rewriting the passing fixture [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:109]. That keeps the change additive.

12. **The underscore rule must not fire on edge labels.** Flow Mode edges are unlabelled by ID; only node IDs are identifiers. Applying the rule to the edge's label text would reject ordinary prose with underscores, so the check belongs in the node loop only [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:63].

## Ruled Out

- **Accent family** as a change: withdrawn for lack of a palette; replaced by a documentation line explaining why one hex is deliberate.
- **Subgraph support**: rejected explicitly, with the three-reason rationale above.
- **A 120-character cap**: too loose for a board at this size; 80 chosen.
- **Parsing subgraph nesting**: unnecessary once subgraphs are rejected.

## Dead Ends

- Trying to derive colour families from hue distance: every threshold was arbitrary, and the self-test could not distinguish a disciplined palette from a sloppy one. Recorded so a later iteration does not retry it.

## Edge Cases

- Ambiguous input: the corpus conflict on subgraphs; resolved by product coherence, not majority vote.
- Contradictory evidence: official support versus Mermaid Jam rejection; both recorded, with the rejection justified by Flow Mode's own rules.
- Missing dependencies: none.
- Partial success: none.

## Questions Answered

- Follow-on: is "accent family" implementable? No, withdrawn.
- Follow-on: should Flow Mode support subgraphs? No, rejected with reasons.

## Questions Remaining

- None. Remaining iterations deepen the mechanical rows and prepare the synthesis ranking.

## Sources Consulted

- `AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py`
- `AI Systems/Product Owner/sk-product-owner/references/flow-mode.md`
- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md`
- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/lint.py`
- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/build.py`
- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/src/parser/mermaidJam.ts`
- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/src/shared/reviser.ts`

## Assessment

- New information ratio: 0.52 (all synthesis and implementation analysis, two verdicts reversed or narrowed)
- Questions addressed: the two weakest candidate rows
- Questions answered: accent family (withdrawn), subgraph policy (reject)

## Reflection

- What worked and why: reading the checker before recommending checker changes exposed that one recommendation was unimplementable; evidence from the target file beats evidence from the corpus.
- What did not work and why: iteration 10's accent verdict was too quick — it treated a corpus pattern as a rule without asking what the check would compare.
- What I would do differently: stress-test every recommendation against the target file before it enters the table.

## Recommended Next Focus

Iteration 13: verify the remaining mechanical rows against `mermaid_extract`'s actual node fields — what it exposes for IDs, labels and shapes — so the reserved-ID, underscore, emoji and length checks are written against real data rather than assumed fields.
