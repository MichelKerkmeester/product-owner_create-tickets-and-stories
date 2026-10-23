# Iteration 9: The Media Editor plugin as a packaging precedent

## Focus

Read the Media Editor Claude Code plugin as the packaging precedent the topic names: what a plugin actually is, how the skill duplicate gets there, and which build-time refusals already protect it. This deepens the embedding mechanics with a working example rather than a design.

## Findings

1. Plugin identity is minimal: `.claude-plugin/plugin.json` carries five fields (name, version, description, author, license) plus keywords, and `.claude-plugin/marketplace.json` declares a one-plugin local marketplace whose source is `./`. [SOURCE: AI Systems/Media Editor/runtime/claude-plugin/.claude-plugin/plugin.json:2] [SOURCE: AI Systems/Media Editor/runtime/claude-plugin/.claude-plugin/marketplace.json:9]
2. The plugin is a build output, not a hand-authored tree: `npm run bundle` builds a platform bundle, `npm run plugin` unpacks `server/`, copies the skill into `skills/sk-media-editor/` and writes the `bin/` shims, and all three of those directories are explicitly not tracked. [SOURCE: AI Systems/Media Editor/runtime/claude-plugin/README.md:31] [SOURCE: AI Systems/Media Editor/runtime/claude-plugin/README.md:78]
3. The copied skill is a wholesale copy of `../../sk-media-editor/`, the build replaces the whole `skills/` folder each time, and the documented workflow is "edit the skill there and rebuild", with the copy never treated as a source. [SOURCE: AI Systems/Media Editor/runtime/claude-plugin/README.md:83]
4. The build already enforces three refusals that solve the duplicate-drift problem: it fails if any copied file differs from its source, refuses a server that unpacks with any link, and refuses a `plugin.json` that registers an MCP server. [SOURCE: AI Systems/Media Editor/runtime/claude-plugin/README.md:83]
5. The plugin registers no MCP server, which the README names as an accepted cost: claude.ai and Cowork do not install a plugin carrying a `bin/` folder, so this plugin reaches Claude Code only and a claude.ai Project needs a separate Desktop extension that is an MCP server. [SOURCE: AI Systems/Media Editor/runtime/claude-plugin/README.md:15]
6. Runtime cost sits outside the plugin: Node 20.9.0 must already be on the PATH the session sees, and one pinned ffmpeg build exists per platform. [SOURCE: AI Systems/Media Editor/runtime/claude-plugin/README.md:24]

## Ruled Out

- Hand-maintaining the copy in the plugin directory. The build replaces it and fails on any divergence, so hand edits are rejected by design.
- Copying the "no MCP server" choice for a FigJam plugin. Product Owner's writer is an external CLI binary rather than a bundled server, so the two cases do not share a transport.

## Dead Ends

- Looking for a tracked plugin payload in git. The three payload directories are untracked by design, which is why this precedent answers the drift question so cleanly.

## Edge Cases

- Ambiguous input: "Claude Code plugin" could mean the packaging or the product. Selected the packaging and its build contract, because that is what the Product Owner copy must imitate.
- Contradictory evidence: none. The README's structure block and the sync paragraph agree.
- Missing dependencies: the build scripts themselves were not read, so the exact parity check is documented rather than inspected.
- Partial success: none.

## Sources Consulted

- `AI Systems/Media Editor/runtime/claude-plugin/.claude-plugin/plugin.json:2-11`
- `AI Systems/Media Editor/runtime/claude-plugin/.claude-plugin/marketplace.json:9-14`
- `AI Systems/Media Editor/runtime/claude-plugin/README.md:15,24,31,76-83`

## Assessment

- New information ratio: 1.0
- Questions addressed: what the plugin precedent is and how it duplicates a skill.
- Questions answered: none fully; the packaging half is answered, the lessons-and-mistakes half needs the changelog record.

## Reflection

- What worked and why: reading the structure block after the quick start exposed the untracked-payload decision, which is the single most reusable idea in this precedent.
- What did not work and why: an early expectation of a rich plugin schema was wrong; the manifest is five fields.
- What I would do differently: read the structure section first in packaging precedents, since it encodes the ownership decisions that prose repeats.

## Recommended Next Focus

Iteration 10: find the mistakes in the Media Editor plugin record. Read its changelog and the plugin-related spec notes for what broke, what was refused, and what was rebuilt, so the Product Owner plugin form inherits the correction rather than the first design.
