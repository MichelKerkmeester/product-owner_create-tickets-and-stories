# Iteration 4: Product docs as input, and the output contract they collide with

## Focus

Test the third input type by reading Product Owner's own artifact lanes and export contract: what a product doc contributes to a flow model, and whether a FigJam deliverable fits the existing output contract at all. This opens a new question because the first two input types were external artifacts, while docs are Product Owner's native material.

## Findings

1. Product Owner's only existing Figma touchpoint is textual: its activation triggers include "Figma feedback or product notes turned into task-ready outcomes", so Figma enters the system as narrative to be rewritten, never as a visual artifact to be produced. [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:26]
2. The skill has five artifact lanes, task, bug, doc, story and epic, all producing ClickUp-ready markdown; none of them produces a diagram, canvas or FigJam artifact. [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:34]
3. The doc lane explicitly covers behavior references, runbooks, architecture documents and technical proposals, which is exactly the prose that carries ordered steps, actors and conditions a flow model needs. [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:29]
4. Routing is command-exact with confidence thresholds, so a FigJam flow request has to become a new intent and command; it cannot ride an existing lane without contradicting the router contract. [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:58] [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:62]
5. The export protocol is a blocking requirement to save every artifact as markdown under `export/` and verify it by read-back, so a FigJam-only deliverable has no compliant home unless the contract gains a named exception or a markdown receipt that points at the board. [SOURCE: AI Systems/Product Owner/AGENTS.md:37] [SOURCE: AI Systems/Product Owner/AGENTS.md:44] [SOURCE: AI Systems/Product Owner/AGENTS.md:46]
6. Inference: product docs supply variables, steps, conditions and expected outcomes, but not states, visual hierarchy, platform split or coordinates, so a doc-sourced flow needs the most model-side invention of the three input types. [INFERENCE: based on the doc lane's artifact list at SKILL.md:29 and the export-first contract at AGENTS.md:37-46]

## Ruled Out

- Reusing the doc lane to emit a FigJam board. The lane's contract is markdown plus read-back, and a canvas has no read-back equivalent.
- Treating the existing "Figma feedback" trigger as diagram input. It consumes prose about Figma, not a Figma file.

## Dead Ends

- Looking for an existing diagram or canvas artifact type in the Product Owner skill. None exists in the lane list or in the export path pattern.

## Edge Cases

- Ambiguous input: "product docs" could mean PO-authored docs or the `Product Context/` corpus. Selected both as prose sources and noted that PO-authored docs are the nearer lane.
- Contradictory evidence: the export protocol says "ALL artifacts" while a FigJam board is not a file; recorded the conflict rather than resolving it by assumption.
- Missing dependencies: none.
- Partial success: none.

## Sources Consulted

- `AI Systems/Product Owner/sk-product-owner/SKILL.md:26,29,34,58,62`
- `AI Systems/Product Owner/AGENTS.md:37,44,46`

## Assessment

- New information ratio: 0.85
- Questions addressed: product doc input; output contract fit.
- Questions answered: none fully; the input-type question now has all three halves, so a comparison iteration is possible.

## Reflection

- What worked and why: reading the trigger list and the export protocol together exposed the contract collision, which a single-lane read would have missed.
- What did not work and why: expecting a diagram lane in the skill wasted a search; the lane list is complete and short.
- What I would do differently: state the export-contract conflict as its own key question earlier, because it constrains the entire design more than any input type does.

## Recommended Next Focus

Iteration 5: compare the three input types on one axis. Build the handoff model, which fields each input type supplies natively, which must be supplied by the agent, and what a common intermediate representation must therefore contain before any FigJam write.
