# Iteration 3: Flowchart rules for FigJam

## Focus
Separate portable flow semantics and connector legibility from the diagram skill's SVG- and HTML-specific mechanics.

## Actions Taken
- Read the flowchart type reference, diagram-wide connector and density rules, output contract, and the local FigJam CLI taxonomy.
- Checked which FigJam commands are documented at the category level and whether their available shape and connector parameters are specified.

## Findings
1. The flowchart grammar transfers: start/end, action, decision, and merge each retain distinct shape roles; the flow stays top-to-bottom; every decision exit is labeled; and a diamond has at most three exits. Color remains an accent rather than a type code. Map these semantics to FigJam-native shapes after confirming the available shape variants. [SOURCE: .skilled/skills/sk-design/sk-design-diagram/references/types/type-flowchart.md:20] [SOURCE: .skilled/skills/sk-design/sk-design-diagram/references/types/type-flowchart.md:25] [SOURCE: .skilled/skills/sk-design/sk-design-diagram/references/types/type-flowchart.md:30]
2. Keep connector legibility rules: favor orthogonal paths, keep each branch label clear of its connector, prevent overlaps and hidden routes, fan connectors apart at shared node edges, and route around unrelated nodes. These are semantic readability constraints; the SVG-specific bend radii, pixel gaps, mask rectangles, and bridge-path recipe need FigJam-native equivalents and should not be copied literally. [SOURCE: .skilled/skills/sk-design/sk-design-diagram/SKILL.md:291] [SOURCE: .skilled/skills/sk-design/sk-design-diagram/SKILL.md:295] [INFERENCE: based on the SVG geometry in those rules and .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:150]
3. Carry over restraint and readable density, but convert the existing 9-node split heuristic and 4px grid into FigJam layout guidance instead of treating them as proven FigJam limits. The diagram skill defines one idea per node, removable redundant links, a target density of 4/10, and a 4px grid in its own coordinate system. [SOURCE: .skilled/skills/sk-design/sk-design-diagram/SKILL.md:260] [SOURCE: .skilled/skills/sk-design/sk-design-diagram/SKILL.md:266] [INFERENCE: FigJam has a different canvas and command model, documented at .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:149]
4. Do not carry over the existing delivery mechanics: format presets and SVG viewBoxes, HTML wrappers, SVG role/aria/title/desc markup, mandatory inline masks, HTML/SVG validators, and corpus checks are tied to the current HTML/SVG or ASCII formats. A FigJam-only mode needs a board-native quality gate and FigJam read-back, not an HTML/SVG export sidecar. [SOURCE: .skilled/skills/sk-design/sk-design-diagram/SKILL.md:235] [SOURCE: .skilled/skills/sk-design/sk-design-diagram/SKILL.md:241] [SOURCE: .skilled/skills/sk-design/sk-design-diagram/SKILL.md:270] [SOURCE: .skilled/skills/sk-design/sk-design-diagram/references/foundations/output-spec.md:23]
5. The documented FigJam surface exposes read verbs (list, info, nodes), write verbs (sticky, shape, text, connect, move, update), destructive delete, and arbitrary eval, but the summary does not pin shape types or connector-routing parameters. Verify those details with the live CLI help before designing the adapter; route ordinary generation through named shape/text/connect commands and keep delete/eval out of the default path. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:149] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:152] [SOURCE: .skilled/skills/sk-design/sk-design-diagram/SKILL.md:265]

## Questions Answered
- Which sk-design-diagram flowchart rules transfer to FigJam, and what must be adapted?

## Questions Remaining
- How should Product Owner embed mcp-figma and sync improvements to .skilled across the two git repositories?
- What should Product Owner copy or avoid from Media Editor’s Claude Code plugin and Moneybird Accountant’s parent hub?

## Next Focus
Compare the shared mcp-figma source with Product Owner packaging and work out an embedded-copy update path across separate repositories.

## Sources Consulted
- .skilled/skills/sk-design/sk-design-diagram/references/types/type-flowchart.md:17-37
- .skilled/skills/sk-design/sk-design-diagram/SKILL.md:228-250, 260-272, 289-305
- .skilled/skills/sk-design/sk-design-diagram/references/foundations/output-spec.md:23-49
- .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:149-152
- .skilled/skills/mcp-tooling/mcp-figma/references/figma-cli-reference.md:348
