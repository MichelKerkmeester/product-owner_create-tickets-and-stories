# Iteration 3: What the corpus already answers, and what the wider web adds

## Focus

Q3, building on iteration 2 findings 6, 8 and 9. Two jobs: read the pinned corpus files that the earlier synthesis never opened for these questions (the `generate-project-plan` diagram block and the server guide README), then widen with public material published outside the 22 repos. The iteration keeps the same discipline as iteration 2: a claim is only new when no local file holds it.

## Actions Taken

1. Read the `generate-project-plan` diagram block's call sequence, including its node-shape claim and its return-value fallback.
2. Read the corpus server guide's rate-limit note.
3. Re-read the pinned `figma-generate-diagram` Step 6 parameter list beside the workflow block's call shape.
4. Searched for post-pin Figma MCP skills, the architecture layout code, and the connector cap vocabulary; read Figma's `ConnectorStrokeCap` type page.
5. Confirmed which public skills the corpus does not carry.

## Findings

1. **The corpus states how a caller finds what a diagram write created, and the packet states nothing.** Figma's own block says to "Capture whatever the tool returns — diagram node ID, or nothing (then fall back to scanning page children)" [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/references/blocks/diagram-section.md:63]. That is the discovery rule iteration 1 finding 5 said the tag step lacks: the id from the tool call, or a page-children scan when the call returns nothing.

2. **An architecture diagram is not one node, so the packet's one-write-one-diagram assumption does not hold for it.** The block says a `FIGMA_DIAGRAM_2026` write produces "1–2 subgraph `SECTION` nodes … Multiple `SHAPE_WITH_TEXT` nodes at the page level … Multiple `CONNECTOR` nodes at the page level" [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/references/blocks/diagram-section.md:67], [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/references/blocks/diagram-section.md:69]. The packet's tag step says "tag every node the write created" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:188] and its rollback stops on any node it did not create [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:190], but neither text says an architecture is a page-level set that may include sections.

3. **Figma's connector cap type is wider than the corpus parser's list, and includes ERD caps that the parser would read as no arrow.** The documented `ConnectorStrokeCap` union is `NONE`, `ARROW_EQUILATERAL`, `ARROW_LINES`, `TRIANGLE_FILLED`, `DIAMOND_FILLED`, `CIRCLE_FILLED` and five `ERD_*` values [SOURCE: https://developers.figma.com/docs/plugins/api/ConnectorStrokeCap/]. The corpus parser counts only an `ARROW_` prefix, `TRIANGLE_FILLED` or `LINE_ARROW` [SOURCE: research/corpus/ecestnrkl__figjam-mcp/src/lib/connectorGraph.ts:45], and `LINE_ARROW` is not in the documented union at all. So an ERD read would classify a crows-foot connector as undirected.

4. **The packet's read-back chain spends a rationed resource the gate never mentions.** Figma limits read tools by plan: a Starter plan or a View or Collab seat is "limited to up to 6 tool calls per month", while tools that write are exempt [SOURCE: research/corpus/figma__mcp-server-guide/README.md:8], [SOURCE: research/corpus/figma__mcp-server-guide/README.md:6]. The packet requires a read-back, a screenshot and a tag call after the write [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:188], and its gate states the plan and the rollback but not the call allowance.

5. **Figma's own current documentation still gives two call shapes, which confirms the earlier synthesis's open claim rather than settling it.** The diagram skill requires `name` and `mermaidSyntax` and makes `fileKey` optional [SOURCE: research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:85], while the workflow block calls the same tool with `mermaid` and `editorType: "figjam"` [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/references/blocks/diagram-section.md:57], [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/references/blocks/diagram-section.md:59]. A model that reads only one of the two will "correct" a call that works.

6. **A regenerating caller is explicitly told that every write without a `fileKey` makes a new draft file.** The skill says "Every call to `generate_diagram` without a `fileKey` creates a new FigJam file in the user's drafts. Regenerating 4 times = 4 draft files to clean up" [SOURCE: research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:102]. The packet carries the `fileKey` rule [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:185] but not the draft-file consequence, which is the cost a user actually sees.

7. **The wider web adds no new diagram discipline, only distribution.** Post-pin public material is Figma's MCP skill family in a second client distribution (`figma-use-slides` for Slides, the community skills page) and a Figma blog post announcing the architecture layout and FigJam skills [SOURCE: https://github.com/figma/mcp-server-guide/blob/main/skills/figma-use-slides/SKILL.md], [SOURCE: https://www.figma.com/community/skills], [SOURCE: https://www.figma.com/blog/figjam-your-coding-agents-whiteboard/]. None of it contradicts the packet's protected behaviours, and none of it adds a check the packet lacks.

8. **The architecture layout code is documented as a parameter value, not a type name.** Figma's architecture reference says the layout is "controlled by the `useArchitectureLayoutCode` parameter on `generate_diagram`" and the workflow block passes the literal `FIGMA_DIAGRAM_2026` [SOURCE: https://github.com/figma/mcp-server-guide/blob/main/skills/figma-generate-diagram/references/architecture.md], [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/references/blocks/diagram-section.md:58]. The packet already passes that exact value for architecture only, so this is a confirmation rather than a gap.

## Ruled Out

- Adopting `figma-use-slides` as a corpus source. It governs Slides writes and says nothing about FigJam boards.
- Treating the community skills page as evidence of a capability. It lists distributions, not behaviours [SOURCE: https://www.figma.com/community/skills].
- Concluding the call shape is settled by the newer file. Both shapes are in the same pinned tree, so recency does not decide it.

## Dead Ends

- Fetching an independent third-party FigJam skill (a public `figjam-diagram-generator` skill). The blob URL returned 404, so nothing could be read and nothing is claimed from it.
- Searching for a published `get_figjam` XML sample. Still none, so attribute names stay unproven.

## Edge Cases

- Ambiguous input: "published after the pins" can mean after the corpus commit or after phase 016. Both readings were searched; the material found predates both, so it is reported as distribution rather than novelty.
- Contradictory evidence: the two call shapes are incompatible and both are Figma's. Recorded as unresolved; the packet's run-time confirmation rule is the only safe position.
- Missing dependencies: no live server, so the return-value behaviour is quoted from Figma's prose rather than observed.
- Partial success: the corpus-widening half of this iteration produced one useful local find (findings 1, 2) and no new external discipline (finding 7).

## Sources Consulted

- `research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/references/blocks/diagram-section.md`
- `research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md`
- `research/corpus/figma__mcp-server-guide/README.md`
- `research/corpus/ecestnrkl__figjam-mcp/src/lib/connectorGraph.ts`
- `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md`
- `https://developers.figma.com/docs/plugins/api/ConnectorStrokeCap/`
- `https://github.com/figma/mcp-server-guide/blob/main/skills/figma-generate-diagram/references/architecture.md`
- `https://www.figma.com/blog/figjam-your-coding-agents-whiteboard/`

## Assessment

- New information ratio: 0.75
- Questions addressed: Q3
- Questions answered: Q3

## Reflection

- What worked and why: reading the workflow block after the skill's Step 6 exposed the return-value fallback and the multi-node architecture claim, which no iteration had read because the earlier synthesis had dismissed that folder as "already upstream". The folder was already present, but its content answered a question the run had left open.
- What did not work and why: web search added distribution pages and no new discipline, because Figma publishes the same skills it ships into the corpus. The search was still worth one call for the `ConnectorStrokeCap` enum, which is the only place the ERD caps appear.
- What I would do differently: search Figma's plugin API type pages earlier, since they name the exact values while the skills only describe behaviour.

## SCOPE VIOLATIONS

None. Every write stayed inside `research/lineages/deepseek-extension/`.

## Recommended Next Focus

Q4. The integration gaps that remain: the router pair's framing dependency from iteration 1, the claude.ai Project's Flow path, ClickUp handoff of a board URL, and the playbook scenarios that assert behaviour the packet now contradicts.
