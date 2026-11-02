# Iteration 2: Screenshots as a pre-structured flow model

## Focus

Open the input-type question with screenshots: what evidence exists in the repo today for turning a screenshot flow into nodes and edges, and whether Product Owner already has any surface that consumes images. This deepens iteration 1's transport finding by asking what the transport must be fed.

## Findings

1. The screenshot corpus is already a flow model on disk: `Product Context/a — Screenshots/<product>/<area>/Flows/<flow>/Flow/<platform>/` holds ordered step captures, while a sibling `Components/<platform>/` holds reusable states and variants. The Change Location flow ships 7 step images across Desktop and Mobile plus 6 component images. [SOURCE: Product Context/a — Screenshots/Barter Managed/Dashboard/Flows/Change Location/Flow/Desktop/Dashboard - Click_ Location Selector.png] [SOURCE: Product Context/a — Screenshots/Barter Managed/Dashboard/Flows/Change Location/Components/Desktop/Dropdown.png]
2. Screenshot filenames encode the trigger and the post-state in prose ("Dashboard - Click_ Location Selector", "Dashboard - Location Change - Success", "Sheet - Menu - Locations - Click_ Location"), so a flow folder yields node labels and transition intents without reading pixels first. [SOURCE: Product Context/a — Screenshots/Barter Managed/Dashboard/Flows/Change Location/Flow/Mobile/Sheet - Menu - Locations - Click_ Location.png]
3. Scale is a selection problem, not a processing problem: the corpus holds 341 PNGs, so a Product Owner procedure must take one flow folder (7 steps in Change Location) rather than ingest the whole library. [SOURCE: Product Context/a — Screenshots/Barter Managed/Dashboard/Flows/Change Location/Flow]
4. The only local pixel reader available to a text-only model is `sk-vision`, which exposes 13 `sk_vision_*` tools for OCR, scene inspection, detection, pointing and pixel analysis with no API key and no cloud upload; its default posture is opt-in and idle, and a fresh clone needs a one-time Bun build before the tools work. [SOURCE: .skilled/sk-vision/SKILL.md:11] [SOURCE: .skilled/sk-vision/SKILL.md:38]
5. Product Owner today has no Figma, screenshot or diagram routing at all: its bootstrap names exactly one skill, `sk-product-owner`, and lists backlog and doc artifacts as its outputs, with no image or diagram input in the boundary list. [SOURCE: AI Systems/Product Owner/AGENTS.md:7] [SOURCE: AI Systems/Product Owner/AGENTS.md:10]
6. Inference from 1-5: screenshot input needs a new handler that (a) selects one `Flow/<platform>` folder, (b) runs OCR and detection only on labels, states and target elements, and (c) emits nodes from filenames plus grounded OCR evidence, because no existing Product Owner surface consumes images. [INFERENCE: based on the AGENTS.md boundary list, the sk-vision tool inventory, and the screenshot folder layout]

## Ruled Out

- Reading every screenshot in the corpus. 341 images with a per-flow structure means the folder, not the library, is the unit of work.
- Treating filenames as sufficient. Filenames give the step label and intent but not the on-screen control a step clicks, so OCR or detection is still needed for a grounded node.

## Dead Ends

- Looking for a Product Owner documentation file that already describes the screenshot library. No PO doc in the skill or bootstrap mentions screenshots, so there is no existing contract to extend.

## Edge Cases

- Ambiguous input: "screenshots" could mean a full library or one flow. Selected the narrowest useful unit (one flow folder) and deferred corpus-wide handling.
- Contradictory evidence: none.
- Missing dependencies: `sk-vision`'s runtime is not built in this clone, so its exact output shape is documented rather than observed. Fallback: cited the skill's tool inventory.
- Partial success: none.

## Sources Consulted

- `Product Context/a — Screenshots/Barter Managed/Dashboard/Flows/Change Location/` (Flow and Components subtrees, both platforms)
- `.skilled/sk-vision/SKILL.md:11,33-45`
- `AI Systems/Product Owner/AGENTS.md:7,10`

## Assessment

- New information ratio: 1.0
- Questions addressed: screenshot input handling; Product Owner current scope.
- Questions answered: none fully; the screenshot half of the input question is answered, the Figma-flow and product-doc halves remain.

## Reflection

- What worked and why: reading the folder tree before the vision skill showed that the repo already solved step ordering through naming, which changes what the vision step is for.
- What did not work and why: searching for a documenting markdown file wasted a step; the folder naming itself is the evidence.
- What I would do differently: quantify the flow folder (7 images) at the same time as the corpus count, to state the selection rule precisely.

## Recommended Next Focus

Iteration 3: Figma frame flows as input. Establish what a Figma design file exposes to the CLI (frames, node ids, platform variants, naming) and whether anything in the repo documents a bridge from a design file into a FigJam board, since iteration 1 showed the `fj` verbs target FigJam pages rather than design documents.
