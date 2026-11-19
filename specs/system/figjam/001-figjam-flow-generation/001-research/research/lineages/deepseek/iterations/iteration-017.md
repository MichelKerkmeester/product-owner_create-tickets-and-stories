# Iteration 17: The risk register, ranked by what research can reduce

## Focus

Assess the risks the topic names, using the version, licence, authentication and runtime evidence gathered so far, and rank each by whether a later phase can reduce it or only name it. This opens the risk question with a severity basis rather than a list.

## Findings

1. The FigJam surface exists only in the unpublished 1.2.0 build from the silships repository: npm publishes only `figma-ds-cli@1.0.0`, and its `--help` lists no `daemon`, no `extract`, no safe `connect` and no `fj` at all, so a user following a normal install gets none of the FigJam verbs. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/figma-cli-reference.md:54] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/figma-cli-reference.md:57]
2. Product Owner ships as a public MIT repository from a GitHub origin, so an embedded skill copy, its examples and any board links become public content, and the vendored source's MIT terms travel with it. [SOURCE: AI Systems/Product Owner/LICENSE:1] [SOURCE: AI Systems/Product Owner/.git]
3. Authentication differs by transport: the CLI needs no API key at all, while the optional MCP path needs a Figma personal access token in `.env` under the prefixed name `figma_FIGMA_API_KEY`; the daemon token at `~/.figma-ds-cli/.daemon-token` is a second credential that must never appear in output. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/mcp-wiring.md:80] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/figma-cli-reference.md:123]
4. Rate limits are unpinned: the skill documents none, and the MCP path wraps the Figma REST API whose quotas are external to this repository, so a batch flow-generation run has no documented ceiling to plan against. [INFERENCE: based on the absence of any rate-limit statement in the tool surface, CLI reference and MCP wiring documents]
5. Two verbs can damage a real board: `fj delete` is destructive and `fj eval` is arbitrary execution; a pipeline that needs a missing capability (images, tables) would be tempted to reach for `fj eval`, which is exactly the arbitrary path the skill's policy keeps out of the default flow. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:151] [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:190]
6. The runtime is local and fragile: the daemon is idle-timed and not reboot-persistent, macOS is the supported baseline, and yolo connect patches `app.asar` and breaks on Figma updates, so unattended or scheduled board generation is unsupported. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/README.md:109]
7. The risk that research can reduce is the version gap, because pinning the 1.2.0 repo build and verifying `fj --help` turns an assumption into a known surface; the risks research cannot reduce are public exposure, external quotas and operator-dependent local runtime. [INFERENCE: derived from findings 1-6]

## Ruled Out

- Planning against npm `latest`. It has no FigJam verbs, so a plan built on it would fail at the first write.
- Using `fj eval` to fill a capability gap. It converts a bounded pipeline into arbitrary execution against a live board.

## Dead Ends

- Searching for a documented rate limit. None exists in the skill; only the external API owner could supply it.

## Edge Cases

- Ambiguous input: "risks" could mean security risks or delivery risks. Selected delivery and security together and ranked by reducibility.
- Contradictory evidence: the skill's README says the skill works with the CLI alone, while the published CLI cannot run FigJam; both are true for different versions.
- Missing dependencies: no live install was performed here, so the version gap rests on the skill's own confirmed measurement.
- Partial success: none.

## Sources Consulted

- `.skilled/skills/mcp-tooling/mcp-figma/references/figma-cli-reference.md:54,57,123`
- `.skilled/skills/mcp-tooling/mcp-figma/references/mcp-wiring.md:80`
- `.skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:151,190`
- `.skilled/skills/mcp-tooling/mcp-figma/README.md:109`
- `AI Systems/Product Owner/LICENSE:1` and repository origin

## Assessment

- New information ratio: 0.9
- Questions addressed: which risks exist and which are reducible.
- Questions answered: the risk question at register level.

## Reflection

- What worked and why: ranking by reducibility produced a different ordering than severity alone, because the version gap is both severe and fixable while the public-exposure risk is structural.
- What did not work and why: the rate-limit search produced an absence rather than a number, which is still a finding but not a budget.
- What I would do differently: check the published-versus-repo version split in iteration 1, since it changes what "capability" means for every later claim.

## Recommended Next Focus

Iteration 18: pin down what "FigJam is the only output" forbids and permits. Read the goal, spec and plan acceptance criteria, then decide what proof of delivery exists when the artifact is a board and not a file.
