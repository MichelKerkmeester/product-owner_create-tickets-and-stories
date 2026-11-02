# Iteration 20: Closing the loop, separating what is known from what must be run

## Focus

Consolidate the nineteen prior iterations, list what remains unverified, and separate findings later phases can act on from those only a live Figma run can settle. This is the final research iteration before synthesis, so it also records what the synthesis itself must supply.

## Findings

1. Nineteen iterations are recorded and three of the five key questions are answered at decision level: the input-to-model question (iteration 5), the rule-transfer question (iteration 7) and the sync-path question (iteration 14); the capability question is answered only up to the documented surface, because the CLI was never executed here. [SOURCE: specs/z-staging-po-017-research/research/lineages/deepseek/deep-research-strategy.md:34]
2. The unverified set is now explicit: no live `figma-ds-cli` install, so every verb flag is documentation-grade; the unpublished 1.2.0 availability, `fj connect` label support, `fj shape` kinds, the node-id return contract, `fj info` output shape and any rate limit all need a live run. [SOURCE: .skilled/skills/mcp-tooling/mcp-figma/references/figma-cli-reference.md:367]
3. Nine findings are actionable without a live run: pin 1.2.0 from the repo, design to the six-verb ceiling, treat Desktop and the daemon as prerequisites, split the Project mirror into applicable and runtime-only rules, declare the new pair in the shared `systems.py`, generate the duplicate with a source-difference refusal, follow the per-packet hub order, separate the board from its verification receipt, and treat public exposure as structural. [SOURCE: specs/z-staging-po-017-research/research/lineages/deepseek/iterations/iteration-007.md:1] [SOURCE: specs/z-staging-po-017-research/research/lineages/deepseek/iterations/iteration-016.md:1]
4. The two precedents converge on three corrections each: from Media Editor, duplicate as an untracked build output, refuse links, and replace the whole copied folder every build; from Moneybird, one router per packet rather than one shared file, per-file contract checks, and hub-level gold rows for stage one. [SOURCE: AI Systems/Media Editor/runtime/claude-plugin/README.md:83] [SOURCE: AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/017-parent-hub-and-router/implementation-summary.md:74]
5. The synthesis must supply the later-phase plan itself, because this packet's `plan.md` and `tasks.md` are still unfilled template scaffolds and only `goal.md` carries real acceptance criteria. [SOURCE: specs/z-staging-po-017-research/plan.md:10] [SOURCE: specs/z-staging-po-017-research/tasks.md:34]
6. The research format has a working precedent in this workspace: the Moneybird routing research lineage produced a fourteen-section `research.md` with a convergence appendix, so the synthesis can follow a house shape rather than invent one. [SOURCE: AI Systems/Moneybird Accountant/specs/011-skill-routing-research/003-research-expansion/research/lineages/deepseek-4/research.md:1]

## Ruled Out

- Raising the confidence of any verb-level claim without a live run. The documentation gap is measured, not closable by more reading.
- Treating the sibling Luna lineage as a source. It runs the same topic independently and is not evidence for this lineage's claims.

## Dead Ends

- Searching for a local record of `fj` output formats. None exists, and the skill's own uncertainty list stands.

## Edge Cases

- Ambiguous input: "close the loop" could mean stop research or prepare synthesis. Selected prepare synthesis, because the stop policy is a forced twenty iterations.
- Contradictory evidence: none; the uncertainty list is consistent with the confirmed version gap.
- Missing dependencies: a live Figma session, which this environment does not provide.
- Partial success: the iteration records consolidation rather than new external evidence; status is `insight` for that reason.

## Sources Consulted

- `specs/z-staging-po-017-research/research/lineages/deepseek/deep-research-strategy.md:34`
- `specs/z-staging-po-017-research/research/lineages/deepseek/iterations/iteration-007.md`
- `specs/z-staging-po-017-research/research/lineages/deepseek/iterations/iteration-016.md`
- `.skilled/skills/mcp-tooling/mcp-figma/references/figma-cli-reference.md:367`
- `AI Systems/Media Editor/runtime/claude-plugin/README.md:83`
- `AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/017-parent-hub-and-router/implementation-summary.md:74`
- `specs/z-staging-po-017-research/plan.md:10` and `tasks.md:34`
- `AI Systems/Moneybird Accountant/specs/011-skill-routing-research/003-research-expansion/research/lineages/deepseek-4/research.md:1`

## Assessment

- New information ratio: 0.45
- Questions addressed: consolidation, remaining uncertainty, synthesis obligations.
- Questions answered: none new; the consolidation makes the existing answers usable.

## Reflection

- What worked and why: separating actionable from live-run findings produced a handoff list the synthesis can copy, which is the most useful output of a forced-depth run.
- What did not work and why: no new external evidence was available without a Figma session, so the ratio is low by construction.
- What I would do differently: keep a running unverified list from iteration 1, so the final iteration reconciles rather than reconstructs.

## Recommended Next Focus

Synthesis: write `research.md` in this lineage with the executive summary, method, sources, the five tracks, the two precedent copy-and-avoid sections, the eliminated alternatives, the divergence map, the ranked later-phase plan, open questions, the verification plan and the convergence report, then hand the terminal synthesis record to the gateway with stopReason maxIterationsReached.
