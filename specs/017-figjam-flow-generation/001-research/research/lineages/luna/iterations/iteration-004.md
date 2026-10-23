# Iteration 4: Embedding mcp-figma and syncing across repositories

## Focus
Determine what an embedded copy needs to function inside Product Owner, and define a safe low-friction path for improvements to travel back to the shared skill.

## Actions Taken
- Read Product Owner’s router, manifest configuration, parity note, and FigJam parent specification.
- Compared Product Owner’s declared tools with mcp-figma’s runtime requirements and resource-loading model.
- Checked both Git roots read-only and searched Product Owner’s skill tree for an existing Figma or FigJam package.

## Findings
1. Product Owner routes one primary intent to one resource lane and discovers routable material from references and assets; its manifest declares references, assets, and the manual-testing playbook as its leaf roots, so embedding mcp-figma requires an explicit FigJam route and resource inventory rather than an unreferenced folder copy. [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:44] [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:103] [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:109] [SOURCE: AI Systems/Product Owner/sk-product-owner/leaf-manifest.config.json:4] [SOURCE: AI Systems/Product Owner/sk-product-owner/leaf-manifest.config.json:11]
2. Copying mcp-figma’s instructions does not provide its tools: Product Owner currently declares Read, Write, Edit, Glob, Grep, WebFetch, and WebSearch, while mcp-figma declares Bash and Code Mode MCP; its documented CLI path also depends on an open Figma Desktop file, Node.js 18 or newer, and the full CLI version. Make the plugin/runtime expose and verify those dependencies before the FigJam route claims generation capability. [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:4] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:4] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:5] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:18] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:54] [INFERENCE: copied skill instructions do not themselves add missing runtime tools]
3. The upstream skill covers broad Figma authoring, modification, export, and optional context retrieval, while the Product Owner specification requires FigJam as the only output; retain a verbatim vendored upstream subtree and put the output restriction in a narrow Product Owner FigJam route/adapter that exposes only named FigJam commands by default. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:14] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:89] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:149] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:152] [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:77] [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:82] [INFERENCE: a thin route keeps product-specific limits from forking upstream Figma behavior]
4. Product Owner’s SYNC.md governs manual parity from its skill sources to the Claude Project kernel and knowledge files; it says the compiler is retired and keeps no manifest, lock, or checksum ledger, so this procedure does not solve the separate cross-repository vendoring problem. Document vendor sync independently from Claude Project review. [SOURCE: AI Systems/Product Owner/SYNC.md:8] [SOURCE: AI Systems/Product Owner/SYNC.md:10] [SOURCE: AI Systems/Product Owner/SYNC.md:15]
5. The FigJam specification names the shared .skilled copy as the current source and asks for changes to flow back from Product Owner; read-only Git-root discovery confirms these are separate repositories, so a low-friction sync helper should take explicit source and destination roots, offer a drift check and patch export, refuse ambiguous/diverged files, and update the vendored copy only after the shared-source change is reviewed and accepted. [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:64] [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:67] [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:83] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:2] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:6] [INFERENCE: read-only git rev-parse showed different repository roots; a reviewed patch followed by re-vendoring preserves the shared source as authority]

## Questions Answered
- How should Product Owner embed mcp-figma and sync improvements to .skilled across the two git repositories?

## Questions Remaining
- What should Product Owner copy or avoid from Media Editor’s Claude Code plugin and Moneybird Accountant’s parent hub?
- Which concrete risks should gate the build phases?

## Next Focus
Inspect Media Editor’s Claude Code plugin and Moneybird Accountant’s router and registry to separate reusable packaging patterns from system-specific behavior.

## Sources Consulted
- AI Systems/Product Owner/sk-product-owner/SKILL.md:1-5, 42-111, 330-344
- AI Systems/Product Owner/sk-product-owner/leaf-manifest.config.json:1-11
- AI Systems/Product Owner/SYNC.md:6-18
- AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:60-84
- .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:1-18, 89-111
- .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:149-152
