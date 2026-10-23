# Iteration 9: The claude.ai Project without a Figma connector, and the ClickUp carrier for a board URL

## Focus

Read the Project packaging and the ClickUp transport for Q5: `claude project/Custom Instructions.md` (advisory-only kernel, Flow Mode Delivery, ClickUp Connector Delivery), the Flow Knowledge mirror `Product Owner - Templates - Flow Mode.md`, the `SYNC.md` parity method and records, and `mcp-click-up`'s tool guide for comments and attachments. Builds on iteration 7 finding 12 (link, not attachment) and iteration 8 finding 12 (no stand-in file).

## Actions Taken

1. Read the kernel's identity rule, Strict Sequence, ClickUp Connector Delivery and Flow Mode Delivery sections.
2. Read the Flow Knowledge mirror's workflow, write routes, no-connector section, read-back and delivery sections.
3. Read the `mcp-click-up` markdown contract and its comment, attachment and task tool entries.
4. Read `SYNC.md`'s parity method and its dated maintenance records, including the pending kernel review.

## Findings

1. The Project kernel is advisory by construction: it cannot write or read local files, run the CLI runtime or call ClickUp except through the claude.ai connector, renders every deliverable as a Deliverable Block, and never claims a save, verification or push it did not perform [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:2]. This is the correct shape for Q5: the question is not whether a Project can match the CLI, but what it can honestly deliver.
2. Flow is the one exception to the Deliverable Block, because its deliverable is a board, and the kernel's Flow Mode Delivery reproduces the CLI's reply contract: board URL, `Read-back:`, `Extensions:` when extended, `Left out:` when cut, and the `HVR self-scan:` line, with `Read-back: not possible, the connector has no read tool` when no read tool exists [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:250], [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:254].
3. With no Figma connector the kernel says so, never claims a board exists, and offers the checked model as a fenced Mermaid block labelled as the model [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:255]. A Project therefore already runs Flow as far as a verified model and returns something the user can keep, which answers the first half of Q5 without new machinery.
4. The Flow Knowledge mirror states the same fallback more tightly: the block is labelled as the model and never as the board, no image or HTML page is a stand-in, and the Desktop `figma-ds-cli` route is unavailable in a Project [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:168]. This is the best-worded no-connector rule in the whole system.
5. There is a parity gap inside the package: the kernel's sentence omits the mirror's "never as the board" qualifier and its image and HTML ban, so a reader who loads only the kernel gets a weaker rule than one who also retrieves the Knowledge file [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:255], [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:168]. The fix is one sentence, not a redesign.
6. The Project cannot run `flow_check.py`, so the mirror converts the script into a rule-by-rule check of the model before anything is written [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:40]. The substitution is sound, but it makes the Project's check quality depend entirely on mirror fidelity, which is why the parity gate matters more here than in the CLI.
7. ClickUp delivery through the connector is body-only and markdown-aware: create or update a task with `markdown_description`, turn the artifact's H1 into the task name, never use the plain `description` field, and read back with `include: ["description"]` before reporting delivery [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:242], [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:246]. A board URL is not an artifact body, so this contract gives it no slot of its own.
8. The transport does support comment threads and attachments: `clickup_create_comment` and the threaded comment tools exist, and `clickup_attach_task_file` plus `clickup_request_attachment_upload` handle files [SOURCE: AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:102], [SOURCE: AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:150]. An attachment is a file upload, not a URL, so the attachment tools are the wrong carrier for a FigJam board; a comment or a body link is the right one.
9. The canonical slot already exists in the artifact templates: the Story and Epic References block has a `Flows` sub-label, and the artifact may carry supplied links but never an image, a screenshot reference or a file path [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/story-template.md:103]. A board URL written under `Flows` is therefore the one legal backlog carrier, and it survives the ClickUp push because the body travels verbatim after the H1 and internal comments are stripped [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:248].
10. The ClickUp offer never fires for a board: the kernel offers ClickUp publishing after every Deliverable Block when the connector is present, and Flow Mode renders no block at all, so a generated board can never trigger the offer in a Project [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:236], [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:295]. This is the concrete integration break on Q5's ClickUp half, and it is a one-line addition to Flow Mode Delivery rather than a routing change.
11. The Project has no hub, which is why the kernel carries the FLOW regexes directly instead of deferring to `ROUTER.md` [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:570]. The stage-two handoff defect from iteration 7 therefore does not reproduce in a Project; the equivalent defect there is the missing ClickUp offer, not a missing route.
12. The parity method is manual and documented: after a skill change, list each skill file against its Project counterpart by name, decide what applies inside a Project, and update the kernel or knowledge file by hand or record why no Project-facing change is needed [SOURCE: AI Systems/Product Owner/SYNC.md:10]. The records also state that the kernel's v1.2.2 review is pending, which is the correct status to carry into the synthesis rather than claiming a reviewed package [SOURCE: AI Systems/Product Owner/SYNC.md:78].
13. The `mcp-click-up` packet is deliberately not mirrored into the Project, because a Project reaches ClickUp through its own connector [SOURCE: AI Systems/Product Owner/SYNC.md:75]. That decision keeps the package small and makes the kernel's ClickUp contract the only Project-side authority, which is why finding 10 must be fixed in the kernel rather than in a mirrored transport file.

## Questions Answered

- Q5: What must the claude.ai kernel and knowledge files change so a Claude Project without a Figma connector can still run Flow, and should a board URL reach ClickUp through the vendored mcp-click-up?

  Answer: almost nothing is missing for the no-connector case — both the kernel and the Flow Knowledge mirror already stop at a checked model, refuse to claim a board, and hand back a labelled Mermaid block. The changes are one parity sentence (carry the mirror's "never as the board" and image/HTML ban into the kernel) and one delivery line (offer ClickUp after a Flow reply when the connector is present). The board URL should travel to ClickUp as a link in the artifact's `Flows` reference group, or as a task comment when there is no artifact, and never as an attachment, because an attachment is a file upload and the vendored transport is not mirrored into a Project.

## Questions Remaining

- None open. Q1 to Q5 are answered; iteration 10 turns the findings into ranked recommendations.

## Ruled Out

- Mirroring `mcp-click-up` into the Project: a Project uses its own connector and the packet's CLI verbs do not exist there.
- Attaching a screenshot of the board to a ClickUp task as the carrier: the artifact rules forbid images and image paths, and a picture cannot prove joins.
- Building a Project-side check script substitute beyond the rule-by-rule mirror: the mirror already converts the script's checks and a Project cannot execute one.

## Dead Ends

- No dead end. The kernel and mirror were both explicit, and the only gap was a sentence.

## Edge Cases

- Contradictory evidence: the CLI forbids rendering the diagram as a Mermaid file as a stand-in for the board, while the Project offers a Mermaid block when no connector exists. The conflict is terminological, not substantive: the Project labels the block as the model, never as the board, and the CLI already offers the checked model in its no-route reply. Both are recorded here rather than merged.
- Ambiguous input: none.
- Missing dependencies: the kernel review is pending, recorded rather than assumed.
- Partial success: the kernel's review status is itself partial and is reported as such.

## Sources Consulted

- AI Systems/Product Owner/claude project/Custom Instructions.md
- AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md
- AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md
- AI Systems/Product Owner/sk-product-owner/assets/story-template.md
- AI Systems/Product Owner/SYNC.md

## Assessment

- New information ratio: 0.87
- Questions addressed: Q5
- Questions answered: Q5

## Reflection

- What worked and why: reading the kernel's Flow Mode Delivery beside the Flow Knowledge mirror exposed a real one-sentence parity gap that neither file shows alone. The ClickUp section then made the missing offer obvious, because the offer is attached to a Deliverable Block that Flow never renders.
- What did not work and why: grepping for "figjam" in the kernel returned mostly router regexes; the delivery sections were the only substantive content, and they sit far apart in the file.
- What I would do differently: read the kernel's Section 9 first, since it holds both delivery contracts and the ClickUp offer rule in one place.

## Recommended Next Focus

Iteration 10: synthesize. Rank the improvements across iterations 1 to 9 by durability and blast radius, separate the packet-local changes from the three integration changes, name the exact files and sections each change touches, and state what the evidence does not support. Then write the terminal synthesis record through the gateway.
