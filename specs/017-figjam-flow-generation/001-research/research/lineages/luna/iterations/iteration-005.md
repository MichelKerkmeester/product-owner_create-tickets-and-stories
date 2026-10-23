# Iteration 5: Media Editor’s Claude Code plugin as a packaging precedent

## Focus
Extract the plugin structure, build boundaries, and verification lessons that fit Product Owner’s FigJam-only route.

## Actions Taken
- Read the plugin README and manifests, build script, packaging tests, and the dated implementation summary.
- Compared the plugin’s bundled CLI architecture with mcp-figma’s external Figma Desktop CLI dependency.
- Checked the plugin support boundary and current-versus-dated tool-count evidence.

## Findings
1. The reusable plugin shell is a Claude Code plugin manifest and README plus a skills folder and optional bin shim; Claude Code adds the plugin bin folder to Bash PATH, and the Media Editor plugin is explicitly Claude Code-only because its bin-based command is not installed by claude.ai or Cowork. [SOURCE: AI Systems/Media Editor/runtime/claude-plugin/README.md:9] [SOURCE: AI Systems/Media Editor/runtime/claude-plugin/README.md:15] [SOURCE: AI Systems/Media Editor/runtime/claude-plugin/README.md:70]
2. Reuse the source-to-plugin copy check, but keep it as a separate step from the cross-repository vendor sync: Media Editor replaces the generated skills folder, copies its tracked skill, compares shipped-file hashes, rejects a mismatching copy, and verifies package/plugin/server versions before writing the output. [SOURCE: AI Systems/Media Editor/runtime/claude-plugin/README.md:83] [SOURCE: AI Systems/Media Editor/runtime/scripts/build-plugin.ts:337] [SOURCE: AI Systems/Media Editor/runtime/scripts/build-plugin.ts:363] [SOURCE: AI Systems/Media Editor/runtime/scripts/build-plugin.ts:402] [SOURCE: AI Systems/Media Editor/runtime/scripts/build-plugin.ts:408] [SOURCE: AI Systems/Media Editor/runtime/scripts/build-plugin.ts:411]
3. Do not reproduce Media Editor’s platform bundle unless Product Owner needs a custom FigJam server: Media Editor builds a platform-specific server bundle and plugin shim around its own runtime, while mcp-figma documents an already-installed figma-ds-cli that requires Figma Desktop, Node.js, and version 1.2.0 or newer; for this workflow, a thin plugin should preflight that existing CLI and expose the FigJam route. [SOURCE: AI Systems/Media Editor/runtime/claude-plugin/README.md:31] [SOURCE: AI Systems/Media Editor/runtime/claude-plugin/README.md:38] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:4] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:18] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:54] [INFERENCE: the current FigJam command surface is external, so bundling Media Editor’s separate server would add an unnecessary runtime]
4. Keep the Claude Code plugin and Product Owner’s Claude Project packaging as separate targets: Media Editor documents that the bin plugin does not install in claude.ai or Cowork and uses its Desktop extension there, while Product Owner’s SYNC.md separately governs manually authored Project mirrors. [SOURCE: AI Systems/Media Editor/runtime/claude-plugin/README.md:15] [SOURCE: AI Systems/Product Owner/SYNC.md:8] [SOURCE: AI Systems/Product Owner/SYNC.md:10]
5. Media Editor’s shipped-binary review found an ffmpeg 9 output-format change that made ten filter-gated tools appear unavailable, and its dated summary records 39 tools while the current packaging test expects 40; Product Owner should smoke-test the actual installed figma-ds-cli version and FigJam read/write calls, and keep dated evidence distinct from current source assertions. [SOURCE: AI Systems/Media Editor/specs/003-media-editor-extension/008-claude-code-plugin/implementation-summary.md:59] [SOURCE: AI Systems/Media Editor/specs/003-media-editor-extension/008-claude-code-plugin/implementation-summary.md:150] [SOURCE: AI Systems/Media Editor/specs/003-media-editor-extension/008-claude-code-plugin/implementation-summary.md:153] [SOURCE: AI Systems/Media Editor/runtime/tests/packaging/build-plugin.vitest.ts:423] [SOURCE: AI Systems/Media Editor/runtime/tests/packaging/build-plugin.vitest.ts:432] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:18] [INFERENCE: current runtime behavior must be checked independently of a dated report or static assertion]

## Questions Answered
- What plugin packaging boundary and verification lessons from Media Editor fit Product Owner’s FigJam-only workflow?

## Questions Remaining
- What should Product Owner copy or avoid from Moneybird Accountant’s parent hub?
- Which build risks should block or sequence the proposed phases?

## Next Focus
Inspect Moneybird Accountant’s hub-router.json and mode-registry.json, then compare their routing boundaries with Product Owner’s current single-mode skill.

## Sources Consulted
- AI Systems/Media Editor/runtime/claude-plugin/README.md:7-25, 29-52, 70-95
- AI Systems/Media Editor/runtime/claude-plugin/.claude-plugin/plugin.json:1-9
- AI Systems/Media Editor/runtime/scripts/build-plugin.ts:337-433
- AI Systems/Media Editor/runtime/tests/packaging/build-plugin.vitest.ts:418-440
- AI Systems/Media Editor/specs/003-media-editor-extension/008-claude-code-plugin/implementation-summary.md:48-59, 143-155, 194-203
- AI Systems/Product Owner/SYNC.md:8-15
- .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:4-18, 54
