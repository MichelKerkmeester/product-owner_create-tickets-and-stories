# Iteration 1: Figma MCP and FigJam capability boundary

## Focus
Determine which documented parts of the local mcp-figma package can read Figma input and which can write a FigJam-only output.

## Actions Taken
- Read the mcp-figma skill, FigJam command taxonomy, optional MCP wiring, and FigJam MCP adapter README. No live Figma tool discovery or board mutation was performed.
- Followed the dispatch instruction to run initialization and the main loop inline. The YAML's default fan-out branch says to skip those phases and proceed to synthesis; that branch conflicts with this bound run request, so this run follows the explicit per-lineage override. [SOURCE: .skilled/commands/deep/assets/deep-research-auto.yaml:217]

## Findings
1. The local mcp-figma contract makes Framelink MCP an optional read-context path into the agent and keeps Figma Desktop CLI as the primary author, modify, and export surface. The documented MCP route therefore cannot create FigJam by itself; a FigJam-only workflow needs the CLI FigJam surface as its board-writing step. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/mcp-wiring.md:32] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:42]
2. The local wiring notes identify two live-confirmed Framelink tools: figma_get_figma_data and figma_download_figma_images. The tool names and schemas are not pinned; the manual warns to discover the registered tool list and call schema before use because the package is @latest. The cited live discovery is dated 2026-06-14, so this run does not treat it as current runtime verification. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/mcp-wiring.md:95] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/mcp-wiring.md:112]
3. The FigJam CLI namespace separates read operations (fj list, info, nodes) from write operations (sticky, shape, text, connect, move, update); fj delete is destructive and fj eval is arbitrary execution. This gives a documented FigJam-native output surface while keeping the risk class visible per operation. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:149]
4. The FigJam-writing route inherits Desktop and version dependencies: the skill says the CLI needs Figma Desktop installed and open, and its complete command surface requires figma-ds-cli 1.2.0 from the silships repository because npm only publishes a minimal 1.0.0 build. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:18] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:54]
5. The local Figma skill requires confirmation, an explicit target, and a rollback note before FigJam write verbs; destructive actions and arbitrary evaluation have stricter explicit-request rules. Product Owner should therefore separate source interpretation from board mutation and define how a user authorizes the target board before any generated output is written. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:181] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:190]

## Questions Answered
- What FigJam creation and editing capabilities and limits does the local Figma MCP expose?

## Questions Remaining
- How should Product Owner ingest screenshots, Figma flows, and product documentation into a FigJam-only output?
- Which sk-design-diagram flowchart rules transfer to FigJam, and what must be adapted?
- How should Product Owner embed mcp-figma and sync improvements to .skilled across the two git repositories?
- What should Product Owner copy or avoid from Media Editor’s Claude Code plugin and Moneybird Accountant’s parent hub?

## Next Focus
Trace a safe input-to-board path for screenshots, Figma file/node links, and product documents, preserving provenance and source ambiguity while keeping the output in FigJam.

## Sources Consulted
- .skilled/skills/mcp-tooling/mcp-figma/SKILL.md:18, 32, 42, 46, 54, 62
- .skilled/skills/mcp-tooling/mcp-figma/references/mcp-wiring.md:17, 32-35, 95-114, 146-148
- .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:149-152, 181-191
- .skilled/skills/mcp-tooling/mcp-figma/feature-catalog/render-and-create/render-and-create.md:18-36

## SCOPE VIOLATIONS
- scope_violation: The workflow pre-init branch can create or edit {spec_folder}/spec.md, which is outside this run's lineage write boundary; that branch and its strict spec validator were skipped. [SOURCE: .skilled/commands/deep/assets/deep-research-auto.yaml:477] [SOURCE: .skilled/commands/deep/assets/deep-research-auto.yaml:520]
- scope_violation: The workflow convergence command persists a graph snapshot under {spec_folder}, and the synthesis writeback edits {spec_folder}/spec.md; both are excluded because they leave the bound lineage. Convergence is configured off and max-iterations is the stop policy. [SOURCE: .skilled/commands/deep/assets/deep-research-auto.yaml:741] [SOURCE: .skilled/commands/deep/assets/deep-research-auto.yaml:2210]
