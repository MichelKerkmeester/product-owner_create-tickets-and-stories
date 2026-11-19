# Iteration 18: What "FigJam is the only output" actually constrains

## Focus

Resolve the delivery paradox the earlier iterations exposed: the topic says FigJam is the only output, while Product Owner's protocol blocks delivery until a markdown file is saved and read back. This deepens the export-contract finding into a definition, and it checks what the packet itself demands of the synthesis.

## Findings

1. The phase directive is stricter than the topic: it produces findings only, and no file outside the research folder may change, so during research not even a FigJam board is touched. [SOURCE: specs/z-staging-po-017-research/goal.md:48]
2. For the eventual feature, "FigJam is the only output" excludes every artifact the diagram skill currently ships: HTML/SVG documents, ASCII markdown flowcharts, PNG/SVG exports and redrawn draw.io or Mermaid sources, so the board itself must carry all the information. [SOURCE: .skilled/skills/sk-design/sk-design-diagram/SKILL.md:42]
3. Product Owner's protocol blocks delivery until a markdown artifact is saved and read back from its exact path, so a board-only delivery requires a redefinition of the receipt rather than a silently dropped step. [SOURCE: AI Systems/Product Owner/AGENTS.md:37] [SOURCE: AI Systems/Product Owner/AGENTS.md:46]
4. The only board read-back available is the read side of the FigJam group, `fj list|info|nodes`, which can prove that pages and nodes exist but not that labels and edges are correct, so a correctness proof needs the intermediate model in text form as well. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:149]
5. The packet's completion criteria put two obligations on the synthesis: every claim must be tagged confirmed or inferred, and there must be a copy-and-avoid section for each of the two precedents. [SOURCE: specs/z-staging-po-017-research/goal.md:61] [SOURCE: specs/z-staging-po-017-research/goal.md:62]
6. The coherent reading is: one delivered artifact, the FigJam board, plus a non-deliverable verification receipt that records the node read-back and the model that produced it; without that distinction the topic and the protocol contradict each other. [INFERENCE: based on the board read-back at tool-surface.md:149 and the delivery gate at AGENTS.md:37-46]

## Ruled Out

- Treating the markdown receipt as a second output. It is verification evidence, not a deliverable, and calling it an output would contradict the topic.
- Exports as a fallback. A PNG or SVG export is exactly what "only output" excludes.

## Dead Ends

- Looking for a FigJam export verb that could serve as read-back proof. The FigJam group has no export verb.

## Edge Cases

- Ambiguous input: "only output" could forbid all files or only forbid alternative diagram formats. Selected the second reading and stated the receipt carve-out explicitly, because the first reading would make the feature undeliverable under the protocol.
- Contradictory evidence: the topic and the export protocol do conflict; recorded rather than smoothed.
- Missing dependencies: the eventual board's exact node read-back format is undocumented, so correctness verification remains partial.
- Partial success: none.

## Sources Consulted

- `specs/z-staging-po-017-research/goal.md:48,61,62`
- `AI Systems/Product Owner/AGENTS.md:37,46`
- `.skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:149`
- `.skilled/skills/sk-design/sk-design-diagram/SKILL.md:42`

## Assessment

- New information ratio: 0.85
- Questions addressed: what the FigJam-only constraint forbids and how delivery can be proven.
- Questions answered: the output-constraint question.

## Reflection

- What worked and why: holding the topic and the protocol side by side produced the receipt distinction, which neither document states alone.
- What did not work and why: the packet's plan and tasks are still template scaffolds, so they could not supply acceptance detail; the goal had to carry it.
- What I would do differently: check the plan and tasks for real content before citing them, since this packet ships them unfilled.

## Recommended Next Focus

Iteration 19: handle the Project side of the embedded skill. Work through what a claude.ai Project can and cannot do with a FigJam capability, given that a Project has no filesystem and no CLI, and what that means for the parity mirror.
