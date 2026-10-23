# Iteration 7: Which flowchart rules survive FigJam, and what replaces the rest

## Focus

Classify every rule inventoried in iteration 6 against the six-verb FigJam surface. This deepens the earlier finding rather than opening a new topic: the question is now whether the diagram system's grammar can be enforced somewhere other than its renderer.

## Findings

1. Shape-carries-type survives as intent but not as a verified contract: `fj shape` exists, yet neither the tool surface nor the CLI reference enumerates which shape kinds or flags it accepts, so a FigJam vocabulary of rectangle, diamond and rounded shape must be confirmed with `--help` before it is written into the skill. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:150] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/figma-cli-reference.md:348]
2. Four rules are portable unchanged because they are model-level, not renderer-level: a labelled exit on every edge, at most three exits per decision, no colour-encoded node types, and one emphasis colour used only for the happy path or a single consequential decision. [SOURCE: .skilled/skills/sk-design/sk-design-diagram/references/types/type-flowchart.md:25] [SOURCE: .skilled/skills/sk-design/sk-design-diagram/references/types/type-flowchart.md:29]
3. Three rules are unenforceable in FigJam and need a substitute: the merge dot has no verb, so branches rejoin by connecting several edges to one target node; the arc jump for crossings has no equivalent, so crossings are avoided by column placement; and the HTML/SVG shape rendering has no import path, so shapes are created one node at a time. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:150]
4. Top-to-bottom layout remains a rule but becomes expensive: there is no automatic layout verb in the FigJam group, only `move` and `update`, so the pipeline must compute positions for every node and edge instead of relying on a renderer. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:150]
5. Edge labelling is the highest-risk rule: if `fj connect` cannot carry a label, every condition becomes either a text node beside the connector or a suffix inside the target node's label, and the second option is the only one that cannot drift out of alignment. [INFERENCE: based on the six-verb surface at tool-surface.md:150 and the labelling rule at type-flowchart.md:25]
6. The enforcement layer must move with the rules: the ASCII validator cannot run against a FigJam board, and no FigJam validator exists, so the pipeline needs its own model check (three-exit ceiling, labelled branches, node-kind vocabulary) that runs before any write. [SOURCE: .skilled/skills/sk-design/sk-design-diagram/scripts/validate-flowchart.sh:82] [SOURCE: .skilled/skills/sk-design/sk-design-diagram/SKILL.md:42]

## Ruled Out

- Porting the HTML/SVG taste gate wholesale. Its palette, typography and spacing rules describe a rendered page, not a board whose colours and shapes are FigJam primitives.
- Deferring layout to FigJam. No automatic layout verb exists, so a deferral would produce overlapping nodes.

## Dead Ends

- Looking for a FigJam-native validator in either skill package. Neither the mcp-figma skill nor the diagram skill ships one.

## Edge Cases

- Ambiguous input: "carry over" could mean reuse the rules or reuse the files. Selected reuse the rules, since the files are renderer-specific.
- Contradictory evidence: none.
- Missing dependencies: `fj shape` and `fj connect` flag detail is unverified, so three classifications are provisional pending `--help`.
- Partial success: two classifications are firm (model-level rules and unenforceable renderer rules), three are provisional.

## Sources Consulted

- `.skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:150`
- `.skilled/skills/mcp-tooling/mcp-figma/references/figma-cli-reference.md:348`
- `.skilled/skills/sk-design/sk-design-diagram/references/types/type-flowchart.md:20-32`
- `.skilled/skills/sk-design/sk-design-diagram/scripts/validate-flowchart.sh:82`
- `.skilled/skills/sk-design/sk-design-diagram/SKILL.md:42`

## Assessment

- New information ratio: 0.7
- Questions addressed: which rules carry over to FigJam and which need replacement.
- Questions answered: the third key question is answered at classification level, with three provisional rows.

## Reflection

- What worked and why: splitting the rule set by layer (model versus renderer) produced a decision for every rule without needing new sources.
- What did not work and why: an early attempt to keep the merge dot as a "small sticky" broke the grammar, because a sticky is a node, not a junction.
- What I would do differently: name the `--help` verification list as a first-class artifact here, because three of the six findings depend on it.

## Recommended Next Focus

Iteration 8: open the embedding question. Read how Product Owner's own skill package is structured as a leaf (manifest files, graph metadata, routing table, changelog) so a second skill can be added without breaking the existing router or parity files.
