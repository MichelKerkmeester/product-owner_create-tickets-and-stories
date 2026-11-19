# Iteration 4: Board read-back, snapshot diff and revision history across five public projects

## Focus

Read the board-as-context and read-back projects — `ecestnrkl__figjam-mcp`, `ulasbilgen__mcp-skills-plugins` (`get_figjam`), `rrichardsonv__parse-figjam`, `southleft__figma-console-mcp-skills` (version history and blame) and `atezer__FMCP` — and compare their read-back, diff and revision models with the packet's `get_figjam` / `fj nodes -l` read-back and its fileKey reuse rule. Builds on iteration 1 finding 8 (read-back honesty) and iteration 2 finding 6 (reparenting changes what a read-back sees).

## Actions Taken

1. Listed the five repos and selected the read-back, diff and revision surfaces.
2. Read `rrichardsonv__parse-figjam/SKILL.md` (connector semantics, colour/legend handling, edge cases).
3. Read `ulasbilgen__mcp-skills-plugins/.../mcp-figma-desktop/SKILL.md` (get_figjam wrapper, board URL and node-id format).
4. Read `ecestnrkl__figjam-mcp/README.md`, `src/lib/boardDiff.ts`, `src/tools/diffBoard.ts`, `src/lib/evidence.ts` and the direction logic in `src/lib/connectorGraph.ts`.
5. Read `southleft__figma-console-mcp-skills/skills/figma-version-history/SKILL.md` and `skills/figma-blame-node/SKILL.md`.

## Findings

1. `parse-figjam` derives connector semantics from the board itself rather than from a label: it reads `connectorStart.endpointNodeId` and `connectorEnd.endpointNodeId`, then checks both stroke caps for direction and `strokeDashes` for relationship type [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/rrichardsonv__parse-figjam/SKILL.md:44], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/rrichardsonv__parse-figjam/SKILL.md:50], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/rrichardsonv__parse-figjam/SKILL.md:80]. The packet's read-back requires every board connector to join the same two ends in the same direction with the same label but never says how direction is derived from the board [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:212].
2. `parse-figjam` refuses to assume colour meanings: it groups nodes by fill, uses a SECTION named `legend` to map colours to meanings when one exists, and asks the user when colour variation is significant without a legend [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/rrichardsonv__parse-figjam/SKILL.md:54], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/rrichardsonv__parse-figjam/SKILL.md:57], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/rrichardsonv__parse-figjam/SKILL.md:58]. The packet's palette assigns fixed meanings and its read-back never reverse-maps a board's colours [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:77].
3. `figjam-context-mcp` skips the download when Figma reports the same file version as the last ingest and stores one snapshot per distinct board state [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ecestnrkl__figjam-mcp/README.md:78], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ecestnrkl__figjam-mcp/README.md:89]. The packet has no version check and no snapshot, so a repeated read-back re-reads the board with no baseline to compare against.
4. `diff_board` compares two snapshots for added, removed and modified clusters, nodes, table cells, connections and arrows [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ecestnrkl__figjam-mcp/README.md:23], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ecestnrkl__figjam-mcp/src/lib/boardDiff.ts:7], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ecestnrkl__figjam-mcp/src/lib/boardDiff.ts:75]. The packet's revision check is a read-back count against the model; there is no pre/post diff, so a second write beside the first is caught only by the count mismatch the packet warns about [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:246].
5. `answer_from_board` returns node-level citations or an explicit insufficient-evidence result, and every evidence row carries `modelDerived` so board text and model interpretation stay distinguishable [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ecestnrkl__figjam-mcp/README.md:22], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ecestnrkl__figjam-mcp/src/lib/evidence.ts:23], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ecestnrkl__figjam-mcp/src/lib/evidence.ts:383]. The packet's `Read-back:` line is a count with no per-item evidence pointer and no insufficient-evidence outcome; its only honest failure mode is "not possible, the connector has no read tool" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:224].
6. Connector direction is computed from the two caps and resolves to forward, reverse, bidirectional or undirected [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ecestnrkl__figjam-mcp/src/lib/connectorGraph.ts:40], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ecestnrkl__figjam-mcp/src/lib/connectorGraph.ts:48]. This is the concrete algorithm the packet's read-back needs but does not name; the packet's user-flow type allows only forward arrows, so its check would pass a reversed arrow it failed to notice in the model [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md:59].
7. Version history is a REST-only capability: `southleft` states it is not reachable through the Plugin API, `use_figma` or the native Figma MCP, snapshots at a version are immutable, and a page-structure diff costs two calls while a component diff costs two per node [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/southleft__figma-console-mcp-skills/skills/figma-blame-node/SKILL.md:3], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/southleft__figma-console-mcp-skills/skills/figma-version-history/SKILL.md:9], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/southleft__figma-console-mcp-skills/skills/figma-version-history/SKILL.md:65]. The packet's rollback is Undo, a version restore, or deleting only self-created nodes, and it never records which version the write produced [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:187], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:199].
8. `figma-blame-node` binary-searches immutable versions to find which version introduced a node or property, because existence is monotonic and around eight probes cover roughly 200 versions [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/southleft__figma-console-mcp-skills/skills/figma-blame-node/SKILL.md:15], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/southleft__figma-console-mcp-skills/skills/figma-blame-node/SKILL.md:20]. This is the audit trail a Product Owner would want after a board changes between reviews; the packet has no equivalent.
9. The same sources draw the claude.ai boundary explicitly: REST-plus-shell skills do not run in plain Claude Desktop or claude.ai chat, and Figma connector OAuth does not authorize REST calls, so a personal access token is required [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/southleft__figma-console-mcp-skills/skills/figma-version-history/SKILL.md:17]. That is direct evidence that the claude.ai kernel cannot use REST-based read-back or version history, and must either use connector tools or say the read is unavailable [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:224].
10. The packet's read-back is stronger in one decisive respect: it compares the board with an expected model and refuses to call a board done on a mismatch [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:228]. The corpus tools report what exists or what changed; none has an expected model to compare against, so they can describe a wrong board accurately but cannot declare it wrong.
11. `get_figjam` returns the full node tree as XML with page, section, sticky and connector IDs, and the corpus uses that tree to anchor extensions [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills-figquery/figma-use-figjam/SKILL.md:17]. The packet's rule to read node by node and never whole-board [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:68] saves tokens on a large board but costs the section and sticky IDs an extension needs on the packet's own small diagram.
12. `mcp-figma-desktop` confirms the FigJam tool boundary the packet relies on — `get_figjam` for `/board/` URLs, not `get_design_context` — and adds an image option the packet's read-back does not mention [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ulasbilgen__mcp-skills-plugins/figma-desktop-plugin/skills/mcp-figma-desktop/SKILL.md:59], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ulasbilgen__mcp-skills-plugins/figma-desktop-plugin/skills/mcp-figma-desktop/SKILL.md:67], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ulasbilgen__mcp-skills-plugins/figma-desktop-plugin/skills/mcp-figma-desktop/SKILL.md:305]. Images on a board are counted by no packet read-back rule.

## Questions Answered

None fully. Q3 now has read-back, diff and revision evidence from four independent projects and still needs the conversion tools (Mermaid to FigJam and back) before the delivery half of the question is complete.

## Questions Remaining

- Q1: type/kind and model-rule coverage.
- Q2: layout, colour, density and board-quality measurement.
- Q3: read-back, revision, fileKey reuse, failure/retry, delivery.
- Q4: request routing and artifact handoff.
- Q5: claude.ai kernel without a Figma connector, and ClickUp.

## Ruled Out

- Treating `get_board_context`'s BM25 retrieval and vision clustering as a read-back model for the packet: those tools interpret a board the packet did not draw, while the packet's read-back has an expected model and exact counts. Their diff and evidence ideas transfer; the retrieval pipeline does not.
- Building version history into the packet: it is REST-only, requires a personal access token, and therefore cannot be a claude.ai Project capability.

## Dead Ends

- Nothing read this iteration was unusable. `atezer__FMCP` was listed but its skills are design-system and token workflows with no FigJam diagram or read-back surface worth citing here.

## Edge Cases

- Contradictory evidence: none. The packet's read-back and the corpus readers answer different questions (is the board correct versus what does the board say), and that distinction is recorded rather than collapsed.
- Ambiguous input: none.
- Missing dependencies: none.
- Partial success: `atezer__FMCP` yielded no relevant surface; recorded as a dead end rather than a finding.

## Sources Consulted

- specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/rrichardsonv__parse-figjam/SKILL.md
- specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ulasbilgen__mcp-skills-plugins/figma-desktop-plugin/skills/mcp-figma-desktop/SKILL.md
- specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ecestnrkl__figjam-mcp/README.md
- specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ecestnrkl__figjam-mcp/src/lib/boardDiff.ts
- specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ecestnrkl__figjam-mcp/src/tools/diffBoard.ts
- specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ecestnrkl__figjam-mcp/src/lib/evidence.ts
- specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ecestnrkl__figjam-mcp/src/lib/connectorGraph.ts
- specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/southleft__figma-console-mcp-skills/skills/figma-version-history/SKILL.md
- specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/southleft__figma-console-mcp-skills/skills/figma-blame-node/SKILL.md

## Assessment

- New information ratio: 0.9
- Questions addressed: Q3, Q5 (partial)
- Questions answered: none

## Reflection

- What worked and why: reading the source rather than the README for `figjam-context-mcp` produced the two transferable mechanisms — a content-hash snapshot diff and a `modelDerived` provenance flag — that the README only advertises. Reading `parse-figjam` and `connectorGraph.ts` together produced the concrete direction algorithm the packet's read-back assumes but never states.
- What did not work and why: `atezer__FMCP` looked promising by name but its skills are design-system and token workflows; a directory listing before reading prevented a wasted pass.
- What I would do differently: check each repo's actual skill inventory before committing to five reads, since two of the five were thin on the topic.

## Recommended Next Focus

Iteration 5: read the FigJam builders and converters — `prasantloki__figjam-builder`, `tmcw__figjam-mermaid`, `memi-design__mermaid-jam`, `lauragalera__figjam-erd-plugin` and `bluescaban__blueprints` — and compare their build, parse and round-trip models with the packet's model-first, write-once flow. Builds on iteration 4's read-back and diff findings and on iteration 3's type coverage.
