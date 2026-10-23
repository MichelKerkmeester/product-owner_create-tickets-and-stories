# Iteration 003 — The action between two screens, and prose that already holds the answer

## Focus

Iteration 3 answers the two questions iteration 2 left: how the action that moves between two screens is found when it is only implied, and how prose rules and acceptance criteria become decisions and branches. It builds on iteration 2 findings 6 (an edge has an actor) and 7 (explicit evidence outranks inference), and it widens the source set from the FigJam packet to the Product Owner packet's own Story and Doc rules, which the Flow intake already cites by name but never reads in detail.

## Actions Taken

- Read `AI Systems/Product Owner/sk-product-owner/references/story-mode.md` around the acceptance-criteria, Requirements and Delivery rules.
- Read `AI Systems/Product Owner/sk-product-owner/references/doc-mode.md` Sections 3 and 4: the five source classes, their classification rules, the authority order and the conflict gate.
- Re-read `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md` Section 4 against those two files, to test the intake's own claim that it applies Doc Mode's classes and gate.
- Re-read `AI Systems/Product Owner/sk-create-figjam/assets/flow-templates.md` Section 3 for the provenance table's granularity.
- Searched all 22 corpus repos for support-ticket or bug-report intake guidance. Two unrelated hits, no modelling guidance; recorded as a gap in the public sources rather than filled by invention.

## Findings

1. **An acceptance criterion is already a labelled edge, and the packet reads it as prose.** Each criterion "holds `*   **Given/When/Then/And**` ClickUp bullets", and "One outcome per Then or And line" [SOURCE: AI Systems/Product Owner/sk-product-owner/references/story-mode.md:151]. Given names the starting condition, When names the action, Then names the outcome; that is a state, an edge and a state, in the order a user flow needs. The Flow intake files a Story under "Product docs" and asks only that every claim be classified and that each causal edge be "asserted from both ends" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:119], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:120], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:123]. So the one input type that arrives pre-structured is flattened into prose before it is modelled. Reading the triples directly is the cheapest extraction gain found in this lineage so far.

2. **A criterion carries an outcome and deliberately leaves out the mechanism, so a Then without a When is a named gap and never a pair to bridge.** "A criterion states what the user can rely on once the work ships and the quality it has to have ... and leaves the mechanism to the developer" [SOURCE: AI Systems/Product Owner/sk-product-owner/references/story-mode.md:151]. That is right for a Story and wrong for a flow: a Then is a node, and with no When there is no edge into it. Story criteria also "verify screen-level behavior" while Epic criteria "stay release-level" [SOURCE: AI Systems/Product Owner/sk-product-owner/references/story-mode.md:151], so an Epic's release-level criterion names no screen at all and cannot be a node. The intake therefore needs the rule: a criterion contributes an edge only when its When names an action, and a release-level criterion contributes none.

3. **The house already has a legal place for an unknown value, and Flow Mode refuses it.** A Story keeps an undecided part visible with an "`**Open:**` line under its name" [SOURCE: AI Systems/Product Owner/sk-product-owner/references/story-mode.md:74], and a Delivery section leaves "unknown values ... as `TBD...` rather than an inferred estimate, risk or exclusion" [SOURCE: AI Systems/Product Owner/sk-product-owner/references/story-mode.md:155]. Flow Mode instead requires every label to use "the product's or the source's own terms" and sends anything missing to `Left out:` [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:169], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:240]. Neither rule is wrong, but they meet at a board drawn from a Story: a `TBD` value is the source's own word, so it is legal on a label, and dropping it instead would hide a decision the Story deliberately left open. This is a recorded source conflict, resolved below.

4. **The provenance table classifies a node and not an edge, which is coarser than the rule it claims to apply.** "One row per drawn item ... a node, a state, a participant, an entity or a task, and a sequence, a state diagram or an ER diagram adds one row per message, transition or relationship whose source differs from its ends" [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/flow-templates.md:110]. A plain user-flow connector has no row at all, so it has no class, even though it is the one item most likely to be inferred rather than read. Doc Mode classifies "at section, field, table row, or individual claim level" [SOURCE: AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:140], and its five classes include "Unknown: Authority or lifecycle status cannot be established safely" [SOURCE: AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:149]. The intake claims to apply that rule [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:120], so the table's missing edge row is a gap between the rule and the artifact that carries it.

5. **The conflict gate ends at a question, while Flow Mode's rule ends at a vanished edge, and the finding has no surface.** Doc Mode's gate compares claims, looks for a winner, and "If no source clearly wins, stop composition" and "Ask one consolidated question ... Do not choose a winner" [SOURCE: AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:184], [SOURCE: AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:186]. Flow Mode's version is "An edge one source states and the other contradicts is a finding, not a connector" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:61]. Followed literally, that rule removes the connector and reports nothing the user can see: no node, no row, no `Left out:` line. A contradicted edge is the most important thing a reader of the board needs to know, and today it is the one thing with no surface. The fix is to give the finding a home the reply already has, not to add a line to the reply.

6. **A support ticket can prove that an error path exists and cannot prove the trigger that reaches it.** No public source in the 22-repo corpus gives ticket-to-diagram guidance; a search for support-ticket and bug-report wording returned two unrelated hits. The nearest authority is Doc Mode's scope limit: "Each authority signal is limited to the scope it actually covers" [SOURCE: AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:175], and a present-tense report of one user's path is a claim about that path only. This is an inference from that rule, not a quoted one: a ticket is evidence of an exit or error state, and the action that produces it must come from a screen, a criterion or a question. Stating it prevents the commonest invention in this mode, which is inventing a trigger to make a reported error reachable.

## Questions Answered

- How should the action that moves between two screens be found, and what happens when it is only implied?
- How should prose rules and acceptance criteria become decisions and branches without inventing either?

## Questions Remaining

- What Flow Mode should read from a Figma prototype link, frame name or prototype connection, and which read tool returns it.
- Merging sources, resolving conflicts, provenance per node and marking gaps in one stated procedure.
- Type choice from what the input holds, and chunking a large input.
- The pre-gate check of a model against its sources.

## Next Focus

Iteration 4: the Figma side of the intake — prototype links, frame names and the read tools — then the merge and provenance procedure that findings 4 and 5 of this iteration sketch. Build on iteration 3 findings 4 and 5.
