# Iteration 2: What the public tool documentation settles

## Focus

Q2, building on iteration 1 findings 5, 6, 7 and 9 and on `research.md` Section 7. The earlier synthesis left four tool questions open: the hosted server's tool list, `whoami`, the fields `get_figjam` returns, and whether `use_figma` allows plugin data. This iteration answers them from Figma's published tool reference and from the corpus copies of the `figma-use` skill, then re-reads the packet text that depends on each answer. A secondary check widens the `get_figjam` question into the connector-direction rule phase 028 added.

## Actions Taken

1. Searched the corpus for `setPluginData`, `getPluginData`, `setSharedPluginData` and read every hit.
2. Read the corpus copies of `figma-use` Critical Rules and `figma-use-figjam`, plus `figma-spec`'s `whoami` warning.
3. Fetched Figma's published MCP tool reference and read its read-tool and write-tool tables, the `whoami` and `create_new_file` entries, the `get_figjam` entry and the `generate_diagram` supported-type list.
4. Read the corpus connector parser that maps arrowhead caps to direction.
5. Verified by search of the packet that it never mentions `get_screenshot`, `get_metadata` or `create_new_file`.

## Findings

1. **Figma documents `setPluginData` as unsupported inside `use_figma`, and names `setSharedPluginData` as the supported call.** The corpus copy states "`getPluginData()` / `setPluginData()` are **not supported** in `use_figma` — do not use them. Use `getSharedPluginData()` / `setSharedPluginData()` instead (these ARE supported)" [SOURCE: research/corpus/lightspeedwp__.github/plugins/figma/figma-use/SKILL.md:28]. A second corpus copy repeats it in a gotchas entry [SOURCE: research/corpus/lightspeedwp__.github/plugins/figma/figma-use/references/gotchas.md:280], and its API index marks the mixin the same way [SOURCE: research/corpus/lightspeedwp__.github/plugins/figma/figma-use/references/plugin-api-standalone.index.md:232]. The packet's "may refuse" hedge [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:188] is therefore a documented prohibition read as a risk.

2. **The shared-plugin-data namespace needs no manifest entry, so a fixed namespace works in any client.** Figma's own API page states the namespace is passed at the call site, needs at least three alphanumeric characters, and does not have to be declared in the manifest; data written that way is readable by other plugins [SOURCE: https://developers.figma.com/docs/plugins/api/properties/nodes-setsharedplugindata/]. That answers iteration 1 finding 6: the namespace can be stable, the diagram name is the key, and the run id belongs in the value.

3. **`whoami` returns identity, plans and seats, and `create_new_file` already asks which team when there are several.** Figma lists `whoami` as "Gets your identity, plans, and seats", marks it remote-only [SOURCE: https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/], and its `create_new_file` entry says the agent asks which team or organization to use when the account holds more than one plan [SOURCE: https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/]. The packet's phase 025 wording matches the "several plans become one question" behaviour but never names the field it must copy.

4. **The plan field has a name and a format the packet never states.** Figma's plugin and shader tools take a `planKey` "in the format `(team|organization)::<numeric-id>`, copied from `whoami`" [SOURCE: https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/]. The packet says only "where the server reports a plan field, pass the plan the gate named" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:183].

5. **`whoami` cannot tell which plan owns the file, so the plan gate is not a `whoami` call.** Figma's spec skill says a caller "MUST always call `whoami`" first, and then warns that "`whoami` does not identify which plan owns a file. If the plan is unclear, you MUST ask the user; never infer it from the file key or another plan's access" [SOURCE: research/corpus/figma__mcp-server-guide/skills/figma-spec/SKILL.md:9]. Phase 025 added `whoami` to resolve the plan before the gate [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:183], which a model can read as "whoami answered the plan question". It answers the account's plans, not the file's.

6. **`get_figjam` returns an XML outline plus screenshots of the nodes, so the critic pass has a screenshot source it never names.** The tool page describes `get_figjam` as returning "an XML outline of FigJam diagrams, similar to `get_metadata`, plus screenshots of the nodes" [SOURCE: https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/], and the corpus skill says the XML carries "IDs of pages, sections, stickies, connectors, and other nodes" [SOURCE: research/corpus/figma__mcp-server-guide/skills/figma-use-figjam/SKILL.md:17]. The board section requires "one screenshot of the diagram" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:78] without saying where it comes from, and `get_screenshot` fails on an empty node id [SOURCE: research/corpus/figma__mcp-server-guide/skills/figma-use-figjam/SKILL.md:21].

7. **The "hosted route" is specifically the remote server, and three of its tools do not exist on the desktop server.** Figma marks `generate_diagram`, `use_figma`, `create_new_file` and `whoami` remote-only [SOURCE: https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/], while `get_figjam` and `get_screenshot` are not marked. The packet presents the hosted route as one thing with `fj` as its fallback [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:66], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:178], so a reader on the desktop server is left to discover that the primary write tool is absent.

8. **Figma's documented `generate_diagram` type list does not name a user flow or a process.** The page lists "Flowcharts, Gantt charts, state diagrams, sequence diagrams, architecture diagrams, and entity relationship diagrams (ERDs)" [SOURCE: https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/]. The packet says the hosted route "draws every type in Section 3" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:178], and Section 3 includes user flow and process. Two of the seven types rest on an inference the packet never states.

9. **The corpus already contains the connector-direction vocabulary the packet's read-back describes in prose.** The parser reads `connectorStartId` and `connectorEndId` and both arrowheads, treats `ARROW_*`, `TRIANGLE_FILLED` and `LINE_ARROW` as an arrow, and derives forward, reverse, bidirectional or undirected from the two caps [SOURCE: research/corpus/ecestnrkl__figjam-mcp/src/lib/connectorGraph.ts:45], [SOURCE: research/corpus/ecestnrkl__figjam-mcp/src/lib/connectorGraph.ts:48]. Phase 028's read-back says the same thing without a single field or cap name [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:218].

10. **The same parser skips a connector whose endpoints are missing, which the packet's read-back has no rule for.** It drops connectors "dangling in empty space (missing either endpoint) … without both endpoints there is no relation to express" [SOURCE: research/corpus/ecestnrkl__figjam-mcp/src/lib/connectorGraph.ts:13]. The packet counts every connector and compares endpoints [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:215], so a dangling connector on the board reads as a mismatch with no rule for what to do.

## Ruled Out

- Treating the root `mcp.json` 18-title list as the live tool list. The published page lists a different and larger set, including tools the packet never names, so the packet's "confirm at run time" rule remains right [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:182].
- Concluding `get_metadata` is a usable FigJam read. Figma restricts it to Figma Design, and the corpus says it fails on FigJam [SOURCE: research/corpus/figma__mcp-server-guide/skills/figma-use-figjam/SKILL.md:20]. The packet never mentions it, so there is nothing to fix.
- Reading `generate_image` as a route for the refused image stand-in. Figma's page confirms `use_figma` cannot add new images at all, which strengthens the packet's no-stand-in rule rather than reopening it [SOURCE: https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/].

## Dead Ends

- Searching the corpus for a `get_figjam` response sample. None exists, so the exact XML attribute names for connector caps stay unproven; only the semantic set is settled.
- Looking for a documented `planKey` field on `generate_diagram`. The tool page does not list one, so the packet's "where the server reports a plan field" conditional is the correct shape.

## Edge Cases

- Ambiguous input: "the fields `get_figjam` returns" can mean the XML attribute names or the node classes. The documented answer names the classes (pages, sections, stickies, connectors) and states the format is XML plus screenshots, so only that level is claimed.
- Contradictory evidence: the pinned corpus copy of `figma-use` carries a different Critical Rule 3a than the copy that names the plugin-data prohibition. Both are recorded; the prohibition is corroborated by two further files in the same corpus and by Figma's API page for the supported call.
- Missing dependencies: no live session, so nothing here proves a specific client exposes a given tool.
- Partial success: four of the five open Section 7 claims are settled; the `generate_diagram` call shape (`mermaidSyntax` alone or `mermaid` with `editorType`) is not.
- Citation correction: two line numbers recorded in iteration 1 were off by two on the rubric's board checklist, and one Adobe critic line was off by one. They are corrected in that narrative. The delta rows for iteration 1 keep the numbers as first written and are not rewritten; the synthesis uses the corrected lines.

## Sources Consulted

- `research/corpus/lightspeedwp__.github/plugins/figma/figma-use/SKILL.md`, `references/gotchas.md`, `references/plugin-api-standalone.index.md`
- `research/corpus/figma__mcp-server-guide/skills/figma-use-figjam/SKILL.md`, `skills/figma-spec/SKILL.md`
- `research/corpus/ecestnrkl__figjam-mcp/src/lib/connectorGraph.ts`
- `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md`, `references/quality-rubric.md`
- `https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/`
- `https://developers.figma.com/docs/plugins/api/properties/nodes-setsharedplugindata/`

## Assessment

- New information ratio: 0.88
- Questions addressed: Q2, Q5 in part
- Questions answered: Q2

## Reflection

- What worked and why: searching the corpus for the exact API name before the web turned the plugin-data question from open into settled, because the corpus already carried Figma's own prohibition in a redistributed copy. Fetching the tool page then fixed the vocabulary (`planKey` format, remote-only markers) that no local file states.
- What did not work and why: the pinned `figma-use` copy's Rule 3a is a different rule, so a reader who trusts the pin alone would not find the prohibition; the answer lives in a copy the earlier synthesis had already discounted as a duplicate. That is a reminder that a "redistributed copy" can carry the newer rule.
- What I would do differently: diff the corpus copies of `figma-use` against each other before declaring them duplicates, since a differing copy is exactly where a changed rule hides.

## SCOPE VIOLATIONS

None. Every write stayed inside `research/lineages/deepseek-extension/`.

## Recommended Next Focus

Q3. Widen the corpus with material published after the pins: FigJam skills, MCP servers and plugins, and Figma documentation pages that postdate the corpus commits, to see whether anything here is already solved elsewhere and whether the packet's seven-type mapping has a published counterpart.
