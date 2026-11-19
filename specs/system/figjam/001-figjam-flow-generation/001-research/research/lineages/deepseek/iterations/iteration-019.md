# Iteration 19: What the claude.ai Project can do with a FigJam capability

## Focus

Work the Project side of the embedded skill: given that a Project is advisory-only and has no filesystem or CLI, decide what a FigJam capability can even mean there and how the parity mirror must split. This opens the mirror question that iteration 16's pair declarations depend on.

## Findings

1. The Project kernel is advisory-only by declaration: a claude.ai Project cannot read or write local files, cannot run the CLI runtime, and can reach ClickUp only through the connector when it is present. [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:2]
2. The Project has no file system at all: the deliverable is the rendered Canvas Artifact, the path-like names are labels rather than writes, and this protocol explicitly overrides any mirrored filesystem save-and-read-back instruction. [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:265] [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:279]
3. A Project therefore cannot perform a FigJam write: there is no CLI, no Figma Desktop and no daemon in that runtime, so the only possible Project role is to prepare and validate the flow model as a Deliverable Block and hand execution to the CLI runtime. [INFERENCE: based on findings 1-2 and the transport requirements in iteration 1]
4. Connector-mediated capability is the only exception pattern the kernel already supports, and it is conditional and approval-gated; the repository's Framelink MCP is a Code Mode stdio server with an API key, not a claude.ai connector. [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:229] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/mcp-wiring.md:17]
5. The parity mirror must therefore split two ways: rules a Project can apply, such as model building, the three-exit ceiling, labelled branches and refusal wording, and rules only the CLI runtime can execute, such as the write verbs, read-back and positioning, which need a runtime-only marker instead of a mirror. [SOURCE: AI Systems/Product Owner/SYNC.md:9]
6. A refusal path is mandatory and consistent with the kernel: a Project asked for a FigJam board must say it cannot write, render the model, and name the command the CLI would run, never claim a write it did not perform. [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:2]

## Ruled Out

- Mirroring the FigJam write procedure into Project knowledge. It would instruct a runtime that cannot execute it, which the hand-parity method explicitly excludes.
- Assuming a Figma connector exists for claude.ai. Nothing in the repository registers one, and the existing Figma MCP is not a connector.

## Dead Ends

- Looking for a Project-side export path for a board. There is none; the Project cannot reach Figma at all.

## Edge Cases

- Ambiguous input: "Project side" could mean the kernel only or the whole knowledge package. Selected both, because the split rule applies to each mirrored file.
- Contradictory evidence: none; the kernel states the constraint twice.
- Missing dependencies: claude.ai's connector catalogue is external and unverified here, so a future Figma connector cannot be ruled out forever, only today.
- Partial success: none.

## Sources Consulted

- `AI Systems/Product Owner/claude project/Custom Instructions.md:2,229,265,279`
- `.skilled/skills/mcp-tooling/mcp-figma/references/mcp-wiring.md:17`
- `AI Systems/Product Owner/SYNC.md:9`

## Assessment

- New information ratio: 0.9
- Questions addressed: what a Project can do with the capability and how the mirror splits.
- Questions answered: the Project half of the packaging question.

## Reflection

- What worked and why: reading the kernel's own constraint lines first turned the mirror question into a split, which is a cheap rule the next phase can apply per file.
- What did not work and why: an early attempt to design a Project-side write path contradicted line 2 and was discarded immediately.
- What I would do differently: read the kernel before the skill on any Project-facing question, since it declares the runtime's limits.

## Recommended Next Focus

Iteration 20: close the loop. Re-read all nineteen iteration records and the strategy, list what remains unverified, and separate the findings that later phases can act on from the ones that only a live Figma run could settle.
