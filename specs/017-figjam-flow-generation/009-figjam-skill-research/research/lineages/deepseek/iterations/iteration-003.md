# Iteration 3: `southleft__figma-console-mcp-skills` — granular console route and read-back queries

## Focus

The third distinct write route: element-by-element board authoring through the Figma Console MCP `use_figma` snippets. Compare its pre-flight guard, atomicity, connector wiring and two read-back queries against iteration 1 (hosted route) and iteration 2 (plugin route).

## Actions Taken

1. Read `southleft__figma-console-mcp-skills/skills/figjam-create-content/SKILL.md` (42 lines).
2. Read `references/figjam-snippets.md` (237 lines), focusing on connector creation, auto-arrange, board read and connection-graph read.
3. Compared the route, guard, retry semantics and read-back with Flow Mode's hosted and `fj` routes.

## Findings

1. This skill positions itself as the granular alternative to the native one-shot `generate_diagram`, for "specific colors, positions, magnets, or to extend an existing board" [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/southleft__figma-console-mcp-skills/skills/figjam-create-content/SKILL.md:10]. Flow Mode has the same two-level split, but its granular level is `figma-ds-cli fj` rather than a console/Plugin API bridge [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:121]. The split is confirmed as a general pattern, not a Flow Mode quirk.

2. Every operation starts with a file-kind guard: `return { editorType: figma.editorType };` must be `'figjam'`, because "every op throws outside FigJam" [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/southleft__figma-console-mcp-skills/skills/figjam-create-content/SKILL.md:24] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/southleft__figma-console-mcp-skills/skills/figjam-create-content/references/figjam-snippets.md:5]. Flow Mode's `fj` route checks the daemon and version but not the file kind before the first write [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:121]. Adopt the guard.

3. The retry model is atomic: "atomic errors (a failed script applies nothing — read the error, fix, retry)" [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/southleft__figma-console-mcp-skills/skills/figjam-create-content/SKILL.md:18]. Flow Mode's recovery is page-oriented — re-run the write into a cleared page only after the user agrees, because a second write duplicates the board [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:159]. Atomicity is a stronger guarantee than rollback-by-clear, and it removes the need to renegotiate with the user after a failed call.

4. Connectors require real node IDs, so the workflow is create nodes first, capture their returned IDs, then create connectors referencing those IDs with start/end plus magnets [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/southleft__figma-console-mcp-skills/skills/figjam-create-content/SKILL.md:28]. Flow Mode arrives at the same requirement from the other direction: read node ids back with `fj nodes -l` between steps when a create verb prints none [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:125]. Two independent sources make this a durable rule.

5. Read-back has two specialized queries, not one: "read board contents" returns a bounded node list (`MAX_NODES = 500`) with id, type, name, geometry, text, shapeType and per-type extras; "read the connection graph" returns every connector with `connectorStart`/`connectorEnd`, label, plus connected-node count [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/southleft__figma-console-mcp-skills/skills/figjam-create-content/references/figjam-snippets.md:196] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/southleft__figma-console-mcp-skills/skills/figjam-create-content/references/figjam-snippets.md:219]. Flow Mode's read-back compares node count, connector count and labels but has no query recipe and no edge endpoint check [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:65].

6. The connection-graph read supplies exactly the evidence Flow Mode's read-back lacks: for each connector, which node is on each end and what the label says, so a connector attached to the wrong pair is detectable, not merely countable [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/southleft__figma-console-mcp-skills/skills/figjam-create-content/references/figjam-snippets.md:221]. Counting connectors cannot distinguish a correct wiring from a permuted one.

7. The board read is deliberately bounded and type-filtered rather than a whole-page dump: it breaks at `MAX_NODES`, walks `figma.currentPage.children`, and records only FigJam types [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/southleft__figma-console-mcp-skills/skills/figjam-create-content/references/figjam-snippets.md:197] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/southleft__figma-console-mcp-skills/skills/figjam-create-content/references/figjam-snippets.md:200]. This corroborates iteration 2 finding 10's warning that a whole-page read can overflow, and gives a concrete shape for the bounded read.

8. Auto-arrange is a post-creation positioning helper: grid, horizontal or vertical layout with a configurable gap, computed from current node geometry [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/southleft__figma-console-mcp-skills/skills/figjam-create-content/references/figjam-snippets.md:170] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/southleft__figma-console-mcp-skills/skills/figjam-create-content/references/figjam-snippets.md:180]. Flow Mode's `fj` route computes every position by hand "because `fj` has no layout verb" [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:123]; an arrange pass would replace a large amount of that arithmetic, at the cost of a second write pass.

9. Fonts must be loaded before any text write, with an Inter fallback when the node's default font is unavailable [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/southleft__figma-console-mcp-skills/skills/figjam-create-content/SKILL.md:31] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/southleft__figma-console-mcp-skills/skills/figjam-create-content/SKILL.md:32]. Flow Mode's `fj` route has no font rule, and no fallback if a font fails to load [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:124].

10. The route is Desktop-only because the Plugin API is unavailable in the browser [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/southleft__figma-console-mcp-skills/skills/figjam-create-content/SKILL.md:40]. This matches Flow Mode's statement that `figma-ds-cli` writes into the FigJam file open in Figma Desktop [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:121], and reinforces that the hosted route is the only Desktop-free option.

## Ruled Out

- Adopting the console bridge as a third Flow Mode route: it requires the same Desktop Plugin API as `fj` but adds a second tool surface, so it is redundant for Flow Mode's constraints.
- Treating the snippet file's broader shape list (`ROUNDED_RECTANGLE`, triangles, parallelograms) as a rule: it is an API capability list with no check attached.

## Dead Ends

- Searching this repo for a Mermaid parser or pre-write validator: none exists; the skill validates by running the operation and reading back.

## Edge Cases

- Ambiguous input: none.
- Contradictory evidence: none; the atomicity claim and Flow Mode's clear-page rollback are different remedies for the same failure class.
- Missing dependencies: none.
- Partial success: none.

## Questions Answered

- None in full. Q2 now has three of the corpus's routes recorded (hosted, plugin, console); three repos remain.

## Questions Remaining

- Q1, Q2, Q4, Q5 remain open.

## Sources Consulted

- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/southleft__figma-console-mcp-skills/skills/figjam-create-content/SKILL.md`
- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/southleft__figma-console-mcp-skills/skills/figjam-create-content/references/figjam-snippets.md`
- `AI Systems/Product Owner/sk-product-owner/references/flow-mode.md`

## Assessment

- New information ratio: 0.89 (8 new, 2 partial — connector-ID and Desktop requirements corroborate earlier findings)
- Questions addressed: Q2 (three routes recorded), Q1 (read-back rather than pre-write check)
- Questions answered: none

## Reflection

- What worked and why: reading the snippet bodies rather than the prose produced the useful material — the two read queries and the atomicity note are not visible in the 42-line SKILL.
- What did not work and why: none failed; the skill has no model-level rules, so it cannot advance Q1.
- What I would do differently: for thin skills, read the references first and the SKILL second.

## Recommended Next Focus

Iteration 4: `mkaralevich__pi-figma-labor/skills/figjam-create/SKILL.md` — the fourth route (CLI-driven creation) and the first chance to check whether any community skill parses Mermaid before writing.
