# Iteration 5: One intermediate flow model for three input types

## Focus

Compare the three input types on a single axis and derive the intermediate representation that every FigJam write must pass through. This opens a new question rather than repeating intake: what does the flow model have to contain so that six FigJam verbs can render it without a second output artifact?

## Findings

1. No input type supplies a complete edge. Screenshots supply step order plus a trigger phrase in the filename, Figma frames supply hierarchy and names but not transitions, and product docs supply conditions and outcomes but not visual states; an edge of the form source, target and condition label must always be synthesized by the agent. [SOURCE: Product Context/a — Screenshots/Barter Managed/Dashboard/Flows/Change Location/Flow/Mobile/Sheet - Menu - Locations - Click_ Location.png] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:112]
2. The six write verbs set the ceiling on what the model may contain: sticky, shape and text create nodes, connect creates an edge between nodes, and move and update position or relabel them. Images, tables, code blocks, sections and embedded files are outside the documented FigJam surface, so the model may not require them. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:150]
3. Connector creation needs node identifiers as inputs, yet the skill documents no return contract for the creation verbs; the only documented way to resolve ids after a write is reading them back through `fj nodes` or `fj info`. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:149] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/figma-cli-reference.md:348]
4. The minimum representation therefore is: nodes carrying an id, a kind from a small vocabulary (start, end, step, decision, state, note), a label and a platform/source pointer; edges carrying a source, a target and an optional condition label; plus layout order and grouping hints, because move and update exist but no automatic layout verb does. [INFERENCE: derived from the verb inventory at tool-surface.md:150 and the input evidence in iteration 2-4]
5. Evidence-bearing nodes are feasible and cheap: Product Owner already proves read-back discipline as its completion gate, so each node can carry its source path while the board itself stays the only delivered artifact. [SOURCE: AI Systems/Product Owner/AGENTS.md:46]
6. Because FigJam is the only output named by the topic, the intermediate model must stay transient: it can live as a fenced block inside the markdown receipt, but it must not become a second deliverable that competes with the board. [SOURCE: specs/z-staging-po-017-research/research/lineages/deepseek/deep-research-strategy.md:27]

## Ruled Out

- A model that needs tables or embedded images. The six-verb surface cannot render either, so any such requirement would force `fj eval` and its arbitrary-mutation gate.
- Trusting creation output to return ids. That contract is undocumented; a read-back step is the only grounded option.

## Dead Ends

- Looking for a layout verb in the FigJam group. There is none; positioning is manual through move or update.

## Edge Cases

- Ambiguous input: "flow model" could mean a graph or a linear checklist. Selected a graph with optional design grouping, because connect implies edges.
- Contradictory evidence: none.
- Missing dependencies: `fj` output shapes are unverified, so the id-read-back step is a requirement, not an implementation detail.
- Partial success: this is an analytical iteration; no new external source was read beyond the citations already held.

## Sources Consulted

- `.skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:112,149,150`
- `.skilled/skills/mcp-tooling/mcp-figma/references/figma-cli-reference.md:348`
- `AI Systems/Product Owner/AGENTS.md:46`
- `specs/z-staging-po-017-research/research/lineages/deepseek/deep-research-strategy.md:27`
- Screenshot flow folders from iteration 2

## Assessment

- New information ratio: 0.6
- Questions addressed: how each input type becomes a flow model.
- Questions answered: the second key question is now answered at model level.

## Reflection

- What worked and why: deriving the model from the verb ceiling instead of from diagram theory kept it renderable, because the transport is the binding constraint.
- What did not work and why: an early draft assumed tables for swimlanes; the six-verb list removed that option.
- What I would do differently: state the id-read-back requirement as a risk item immediately, since it affects every write sequence.

## Recommended Next Focus

Iteration 6: open the rule-transfer question at the source. Read `sk-design-diagram`'s flowchart type reference and its validation rules to enumerate the rules a flow chart currently obeys, so iteration 7 can classify each rule as portable to FigJam or needing replacement.
