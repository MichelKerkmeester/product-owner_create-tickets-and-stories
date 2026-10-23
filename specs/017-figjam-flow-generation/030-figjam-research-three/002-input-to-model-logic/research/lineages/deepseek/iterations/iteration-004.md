# Iteration 004 — What a Figma file already knows, and which read reaches it

## Focus

Iteration 4 answers the Figma half of the intake: what Flow Mode should read from a frame, a frame name and a prototype connection, and which read tool returns each. It builds on iteration 2 finding 4 (a state is a screen until a different action reaches it) and iteration 3 finding 5 (a conflict needs a surface), and it widens the source set with the vendored `mcp-figma` tool surface, Figma's own plugin API index and two corpus repos this lineage has not yet used for the intake side: `southleft`'s skills index and `arinspunk__claude-talk-to-figma-mcp`.

## Actions Taken

- Read `AI Systems/Product Owner/mcp-figma/references/tool-surface.md` for the read verbs and what each returns.
- Read `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md` Section 4 "Figma flows" and Section 6's read rules as the baseline.
- Read `research/corpus/figma__mcp-server-guide/skills/figma-use/references/plugin-api-standalone.index.md` around the mixin table.
- Read `research/corpus/figma__community-resources/agent_skills/README.md` for the tool combinations published skills use.
- Read `research/corpus/arinspunk__claude-talk-to-figma-mcp/CHANGELOG.md` for its prototype-interaction tools.
- Read `research/corpus/lightspeedwp__.github/plugins/figma/figma-generate-design/SKILL.md` for URL parsing.

## Findings

1. **A Figma file already states its own navigation graph, and the intake never reads it.** The plugin API exposes a `ReactionMixin` whose property is "`reactions` (prototyping)", beside a `FramePrototypingMixin` carrying `overflowDirection` and `numberOfFixedChildren` [SOURCE: research/corpus/figma__mcp-server-guide/skills/figma-use/references/plugin-api-standalone.index.md:194], [SOURCE: research/corpus/figma__mcp-server-guide/skills/figma-use/references/plugin-api-standalone.index.md:198]. A reaction is the designer's own answer to "what moves from this frame", stored on the node. Flow Mode's Figma intake reads "node by node" for content and then infers every move, and its only structural rule is that "No verb copies a design frame onto a board, so frame content is retyped into the model" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:116], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:117]. So the strongest evidence for the edges — the only evidence in the whole intake that is stated rather than inferred — is skipped by a rule about content copying.

2. **The read that reaches reactions is `use_figma`, which the packet uses only as a write tool.** A published skill walks a component and returns "its full node tree with resolved token bindings, main-component references, and prototype reactions", and it does so with `use_figma`, `get_design_context` and `get_metadata` [SOURCE: research/corpus/figma__community-resources/agent_skills/README.md:105], [SOURCE: research/corpus/figma__community-resources/agent_skills/README.md:106]. `use_figma` runs plugin JavaScript in the file, which is why it can read a plugin-API property at all. In Flow Mode, `use_figma` appears only in Section 6: the tag call, the rollback and the delete-after-yes [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:190], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:195]. A read-only `use_figma` call is not a write route, and the packet has no slot for it, so the intake is limited to the hosted read tools by accident rather than by decision.

3. **A reaction's trigger and action classify the move, which is the screen-versus-state test the packet lacks.** One corpus implementation lists triggers "CLICK, HOVER, etc." and actions "NAVIGATE, OVERLAY, BACK" [SOURCE: research/corpus/arinspunk__claude-talk-to-figma-mcp/CHANGELOG.md:29]. Read against iteration 2 finding 4: `NAVIGATE` to another frame is a different screen and earns a node; `OVERLAY` is a layer appearing over the same screen, which is a state unless its own trigger traps the reader; `BACK` is a return edge to a node already drawn, not a new node. That is a three-way classification computed from the file, with no vision read and no guess.

4. **The node id in a Figma URL is not the node id the API takes, and the packet's instruction is literally wrong for a hyphenated URL.** A design URL carries `node-id=609-35535`, and the documented parsing rule is "Parse `fileKey` = `ABC123`, `nodeId` = `609:35535`" [SOURCE: research/corpus/lightspeedwp__.github/plugins/figma/figma-generate-design/SKILL.md:80]. Flow Mode says only "Take the `fileKey` and `nodeId` from the URL and read node by node" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:116]. A reader who copies `609-35535` gets a lookup that fails or, worse, a different node. It is one clause and it is the first step of the whole Figma intake.

5. **A frame name and the screen's visible heading can disagree, and no rule says which wins.** The packet's label rule is the strongest in the packet: "Labels use the product's or the source's own terms" and proper nouns are never renamed [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:169]. But the Figma route gives two candidate words for one node — the layer name the designer typed, and the heading the screen shows — and frame names are commonly shorthand, a ticket key or a duplicate marker. Nothing in Section 4 or the provenance table decides. This is iteration 3 finding 5's conflict class arriving at the Figma route specifically: the two candidates are both "the source's words", so neither the never-invent rule nor the remove test can settle it.

6. **Reading the graph first is cheap; the packet's cost rule is about content and reads as if it were about the file.** "A whole-file read is token-heavy and is never the first read" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:116] is correct for frame content and misleading for the reaction graph: one script that returns `id`, `name` and `reactions` for each top-level frame is a single call and yields every node and edge candidate at once. The packet's rule then pushes the intake toward exactly the pattern that costs most — one content read per frame — before any edge is known. Narrowing the rule to content, and adding a graph read as the first Figma step, changes the cost profile without touching the write path.

## Questions Answered

- What should Flow Mode read from a Figma prototype link, frame name or prototype connection, and which Figma read tool returns it?

## Questions Remaining

- Merging sources, resolving conflicts, provenance per node and marking gaps in one stated procedure.
- Type choice from what the input holds, and chunking a large input.
- The pre-gate check of a model against its sources.
- Whether a `figma.com/proto` URL carries navigation metadata the design URL does not. No corpus source describes its parameters, so this stays unverified and is not claimed.

## Next Focus

Iteration 5: merge, provenance, gaps, type choice, chunking and the pre-gate check, assembled as one ordered intake procedure. Build on iteration 3 findings 4 and 5 and iteration 4 findings 1 and 3.
