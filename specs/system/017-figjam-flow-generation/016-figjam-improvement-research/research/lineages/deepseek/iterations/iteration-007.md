# Iteration 7: Two-stage routing, the one-way Flow handoff, and where a board can legitimately land in an artifact

## Focus

Read the integration surfaces — the hub `SKILL.md`, `ROUTER.md`, `hub-router.json`, `mode-registry.json`, the Product Owner `AGENTS.md`, and `sk-product-owner/SKILL.md` with `references/routing.md`, `references/router-contract.md`, `references/doc-mode.md`, `references/story-mode.md` and `assets/story-template.md` — to trace how a request reaches the FigJam packet and what happens to the board afterwards. Addresses Q4 and extends iteration 6 finding 10 (the doc-first link-back pattern).

## Actions Taken

1. Read `AI Systems/Product Owner/SKILL.md` and `ROUTER.md` for the two-stage contract, stage-one order and the leaf map.
2. Read the FLOW entries in `mode-registry.json` and the `orderedBundle` outcome in `hub-router.json`.
3. Read `sk-product-owner/SKILL.md` Section 2 and the Flow lines in `AGENTS.md`.
4. Read `references/routing.md` (framing rules), `references/router-contract.md` (the RESOURCE_MAP guard and Flow regexes), `references/doc-mode.md` (diagram preservation) and `references/story-mode.md` plus `assets/story-template.md` (reference and image rules).

## Findings

1. Routing is genuinely two-stage: the hub picks one of four modes from the registry and policy, then `ROUTER.md` maps intent to packet-qualified leaves, and the packet's own Section 2 routes inside the packet [SOURCE: AI Systems/Product Owner/SKILL.md:38], [SOURCE: AI Systems/Product Owner/ROUTER.md:21]. The separation is sound and the FigJam packet is a peer mode, not a sub-route of Doc or Task.
2. Flow is an explicit sibling route with its own leaf set: `$flow`, `$figjam` and FigJam output wording load `flow-mode.md` plus `flow-templates.md`, and the packet then adds the chosen type's reference and template [SOURCE: AI Systems/Product Owner/ROUTER.md:33], [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:57].
3. The handoff is prose, not a resolvable resource: the Product Owner resource map still lists a FLOW lane, but a guard drops it because the pair lives in the other packet, and Section 2 hands the route over instead [SOURCE: AI Systems/Product Owner/sk-product-owner/references/router-contract.md:146], [SOURCE: AI Systems/Product Owner/sk-product-owner/references/router-contract.md:149], [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:72]. Nothing in the router can load the FigJam packet's leaves itself.
4. The two halves have incompatible completion protocols: every artifact must be saved to `export/` before the reply, while Flow Mode is the single exemption and saves nothing, answering with the board URL, read-back, `Left out:` line and self-scan [SOURCE: AI Systems/Product Owner/AGENTS.md:37], [SOURCE: AI Systems/Product Owner/AGENTS.md:39], [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:170]. There is no shared artifact between the halves.
5. The Flow reply is terminal and self-contained: "the reply carries the board, its proof and the self-scan, and nothing else" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:221]. Since no Story, Doc or Task is written afterwards, the produced board URL has no route back into the request that motivated it.
6. An artifact word beats FigJam framing: FigJam wording beside another artifact's framing is that artifact's subject, so it never makes a conflict, and the artifact's leaf set loads alone [SOURCE: AI Systems/Product Owner/sk-product-owner/references/routing.md:26], [SOURCE: AI Systems/Product Owner/ROUTER.md:37]. A request such as "write a runbook with a FigJam process diagram" therefore never loads Flow Mode, so the diagram cannot be produced by the skill that was asked.
7. Doc Mode preserves only diagrams already supplied as text and has no instruction to commission a board or insert a board link [SOURCE: AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:275]. The corpus's doc-first pattern — doc authoritative, diagram optional, labels matching the doc, board link written back under a heading — is exactly the missing half [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/hferello__ai/arch-flow/SKILL.md:170].
8. Story Mode forbids the very value a board should supply: it never invents a Figma destination or a ClickUp link, and a Story or Epic never carries an image, a screenshot reference or a file path to one, because images are embedded in ClickUp after export [SOURCE: AI Systems/Product Owner/sk-product-owner/references/story-mode.md:163], [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/story-template.md:103]. A board URL returned later in the same session is not "supplied" under this wording, so a Story that asks for a flow cannot legally carry the result.
9. The registry records no handoff shape: the FigJam mode declares its `workflowMode`, `packetKind`, `backendKind` as a checked-model board, its tool surface, packet name and aliases, and nothing about inputs, an artifact it serves or a write-back [SOURCE: AI Systems/Product Owner/mode-registry.json:87], [SOURCE: AI Systems/Product Owner/mode-registry.json:102]. Any integration must be invented in prose unless the registry gains a field, even though the registry is already the authority for mode selection.
10. Stage one refuses ordered bundles by design: `orderedBundle` is never formed at stage one and two packets' signals start in the default mode, which asks which comes first [SOURCE: AI Systems/Product Owner/hub-router.json:15], [SOURCE: AI Systems/Product Owner/SKILL.md:79]. A Story plus its flow therefore costs a question even when the order is obvious: the artifact first, the diagram from it.
11. A Flow request that names an artifact crosses three routing surfaces before any Flow guidance loads: the hub keeps it in the Product Owner packet, that packet's router hands it on, and only then does the FigJam packet's Section 2 pick a type [SOURCE: AI Systems/Product Owner/SKILL.md:60], [SOURCE: AI Systems/Product Owner/AGENTS.md:166]. The hub's own note that this request "is still read as Flow there" shows the seam is known, but no artifact context is carried across it.
12. ClickUp is a separate vendored transport, and the templates defer images to ClickUp embedding after export, so the only legal cross-system path for a generated board is a link in the artifact's `References` sub-groups, never an attachment [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/story-template.md:103], [SOURCE: AI Systems/Product Owner/ROUTER.md:95]. This bounds any ClickUp integration to a URL written into an artifact, not a file upload.

## Questions Answered

- Q4: How should request routing and artifact handoff work in the integration?

  Answer: routing is correctly registry-driven in two stages with FigJam as a peer mode, but the handoff is a one-way prose instruction: the Product Owner resource map drops the Flow leaves, the Flow reply is terminal, and artifact modes treat FigJam as a subject without carrying context in or writing a board URL out. A working integration needs three additions — the artifact's context carried into Flow Mode as its source, a same-session board URL accepted as a supplied link in the artifact's `Flows` reference group, and an explicit artifact-then-diagram order so the pair does not cost a disambiguation question.

## Questions Remaining

- Q3: read-back, revision, fileKey reuse, failure and retry (partly covered; the revision and retry surfaces still need a direct read).
- Q5: the claude.ai kernel without a Figma connector, and ClickUp.

## Ruled Out

- Treating the Flow lane in `router-contract.md` as loadable: the guard drops it by design and the lane exists only for Project knowledge naming.
- Proposing a file attachment pipeline into ClickUp: the templates forbid images and image paths in artifacts, so a link is the only legal carrier.

## Dead Ends

- No dead end. The routing files were long but each answered a specific question.

## Edge Cases

- Contradictory evidence: the hub note says a Flow request naming a product doc is "still read as Flow" and handed on, while the stage-two rule says FigJam beside another artifact's framing is that artifact's subject and the artifact's set loads alone. Both are true at different layers, which is precisely the seam this iteration records; the practical effect is that the diagram is either produced by Flow with no artifact context or never produced at all.
- Ambiguous input: none.
- Missing dependencies: none.
- Partial success: none.

## Sources Consulted

- AI Systems/Product Owner/SKILL.md
- AI Systems/Product Owner/ROUTER.md
- AI Systems/Product Owner/hub-router.json
- AI Systems/Product Owner/mode-registry.json
- AI Systems/Product Owner/AGENTS.md
- AI Systems/Product Owner/sk-product-owner/SKILL.md
- AI Systems/Product Owner/sk-product-owner/references/routing.md
- AI Systems/Product Owner/sk-product-owner/references/router-contract.md
- AI Systems/Product Owner/sk-product-owner/references/doc-mode.md
- AI Systems/Product Owner/sk-product-owner/references/story-mode.md
- AI Systems/Product Owner/sk-product-owner/assets/story-template.md

## Assessment

- New information ratio: 0.9
- Questions addressed: Q4, Q5
- Questions answered: Q4

## Reflection

- What worked and why: reading the hub, the stage-two map, the packet router and the artifact templates in that order made the seam visible. Each file is internally consistent; the gap appears only when the Flow exemption, the Story image ban and the dropped Flow lane are read together.
- What did not work and why: searching the packet for "figjam" produced forty hits that were mostly routing keywords; the decisive lines were the template Notes For Use and the router contract comment, neither of which mentions FigJam in its heading.
- What I would do differently: start from the artifact templates' reference rules rather than the router, because the templates state what the artifact may legally carry, and that constraint decides the integration shape.

## Recommended Next Focus

Iteration 8: read the revision, retry and fileKey surfaces directly — `sk-create-figjam/references/flow-mode.md` Sections 6 to 9, `references/quality-rubric.md`, `references/hybrid-workflow.md` and the type references' revision rules — and compare them with `rrichardsonv__parse-figjam`, `memi-design__mermaid-jam` and `ompug__diagram-codebase`'s resume and update behavior. Builds on iteration 6 finding 11 (manifest and resume) and iteration 5 finding 8 (preserved manual positions).
