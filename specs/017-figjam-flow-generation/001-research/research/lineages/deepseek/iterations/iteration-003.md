# Iteration 3: Figma frame flows as input, and the missing bridge into FigJam

## Focus

Test the second input type: what a Figma design file exposes to the CLI, and whether anything documented can carry a design frame into a FigJam board. This opens a new question because iteration 1 established FigJam writes as a distinct verb group, and iteration 2 established that screenshots are transcribed rather than transported.

## Findings

1. Design-file reading is a separate verb family from FigJam writing: `files` lists open design files, `node tree` and `node bindings` show hierarchy and bindings, `get`/`inspect` read node properties and specs, and `export screenshot|node|css|tailwind` writes files. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:108] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:112] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:153]
2. The FigJam write surface contains exactly six mutating verbs, `fj sticky|shape|text|connect|move|update`, and no image, frame, section, table, code-block or file-embed verb. A Figma frame therefore cannot be placed into a FigJam board through the documented surface; only its content can be retyped as FigJam nodes. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:150] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/figma-cli-reference.md:348]
3. No cross-file operation is documented anywhere in the skill: the `fj` verbs act on FigJam pages and nodes, the design verbs act on the open design file, and neither the tool surface nor the CLI reference names a "copy design frames into a FigJam board" path. [INFERENCE: based on the verb inventory at tool-surface.md:108-153 and the FigJam group at 149-152, plus the absence of any bridge row]
4. A frame flow is still enumerable with grounded evidence: `node tree` yields the frame hierarchy and names, `inspect` yields per-node specs, and `export screenshot` yields pixels that `sk-vision` can read, so a flow can be reconstructed node by node without guessing. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:112] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:137]
5. Large design files fragment on read: `extract` writes `DESIGN.md` and auto-splits into a `DESIGN-structure/` directory above roughly 50k tokens, so intake must pin one frame subtree instead of extracting a whole file. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:203]
6. Every claim in 1-5 is documentation-grade rather than live-verified in this environment, because the CLI was not installed or executed here; the skill itself records the docs-versus-source drift as a confirmed gap and demands `<bin> <command> --help` before reliance. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/figma-cli-reference.md:372] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:248]

## Ruled Out

- Transporting design frames into FigJam as embedded objects. There is no documented verb for it, and inventing one from the Figma Plugin API would mean `fj eval`, which the skill classes as arbitrary mutation.
- Extracting whole files. The auto-split behavior makes a whole-file read a directory-producing operation, not a bounded input.

## Dead Ends

- Searching the skill for an official Figma Dev Mode MCP bridge into FigJam. Iteration 1 already placed it out of scope; this iteration confirms nothing else bridges design files to FigJam boards.

## Edge Cases

- Ambiguous input: "Figma flows" could mean a Figma prototype with connectors or a set of frames. Selected frames plus node tree, because the CLI exposes frames and nodes, not prototype interactions.
- Contradictory evidence: none. The two references agree on the six `fj` write verbs.
- Missing dependencies: no live CLI, so frame export flags are unverified. Fallback: documentation citations plus the skill's own verification rule.
- Partial success: four findings are documentation-backed, one is an inference from absence, and one is a caveat.

## Sources Consulted

- `.skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:108,112,137,149-152,153,203,248`
- `.skilled/skills/mcp-tooling/mcp-figma/references/figma-cli-reference.md:348,372`

## Assessment

- New information ratio: 0.92
- Questions addressed: Figma frame flow input; FigJam transport limits.
- Questions answered: none fully; the Figma half of the input question is answered, the product-doc half remains.

## Reflection

- What worked and why: comparing two verb families side by side exposed the absence of a bridge faster than searching for one, because an absence is only meaningful against a complete inventory.
- What did not work and why: the first pass assumed FigJam could hold an image; the six-verb list disproved it.
- What I would do differently: capture the six-verb list verbatim from the start, since it is the single constraint the whole FigJam-only design must respect.

## Recommended Next Focus

Iteration 4: product docs as input. Read Product Owner's own artifact formats and the `sk-product-owner` skill to establish what a doc contributes to a flow (steps, actors, states, conditional branches) and what it cannot supply, so the three input types can be compared on one axis in a later iteration.
