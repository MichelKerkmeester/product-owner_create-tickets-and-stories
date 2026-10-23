# Iteration 14: Scoring the sync options against proven mechanics

## Focus

Evaluate the candidate low-friction sync paths for an embedded copy using only mechanisms already observed in this repository. This deepens the three-hop chain into an option comparison, so the recommended path is an evidence-backed choice rather than a preference.

## Findings

1. Build-output duplication with a source-difference refusal is the only drift-proof pattern demonstrated locally: the Media Editor plugin copies the skill on every build, replaces the whole folder, and fails when any copied file differs from its source. [SOURCE: AI Systems/Media Editor/runtime/claude-plugin/README.md:83] [SOURCE: AI Systems/Media Editor/specs/003-media-editor-extension/008-claude-code-plugin/implementation-summary.md:55]
2. Vendored copies with an explicit declaration are the fallback when generation is impossible, and Product Owner already runs that pattern for four shared rule cards, accepting that a card change turns the system red until the copy is refreshed. [SOURCE: AI Systems/Product Owner/SYNC.md:44]
3. Symlinks are disproven in this workspace: a link that climbs out of the repository resolves to nothing once cloned, and the plugin build refuses any link in an unpacked payload. [SOURCE: AI Systems/Product Owner/SYNC.md:44] [SOURCE: AI Systems/Media Editor/specs/003-media-editor-extension/008-claude-code-plugin/implementation-summary.md:55]
4. No local precedent exists for sharing a skill through a git submodule, a subtree merge, or a published package; adopting one would be an unproven step in a phase whose scope is research, and none of the two precedents uses either. [INFERENCE: based on the two precedent records and the absence of submodule or package-publishing mechanics in both skill packages]
5. The first hop, shared skill to Product Owner copy, is generatable because both ends are git-tracked files with a stable path; the second hop, copy to Claude Project mirror, is not, because the contract requires a per-paragraph human decision and a named reviewer's dated record. [SOURCE: AI Systems/Product Owner/SYNC.md:9] [SOURCE: AI Systems/Media Editor/runtime/claude-plugin/README.md:83]
6. The best available path is therefore one generated hop with a refusal plus one manual hop with a dated record; claiming a fully automated sync would require abandoning the manual parity contract that the root rules require. [SOURCE: AGENTS.md:127] [SOURCE: AI Systems/Product Owner/SYNC.md:17]

## Ruled Out

- Symlinks or submodules for the embedded skill. Both fail the clone requirement, and the plugin build rejects links outright.
- A fully generated Project mirror. It would contradict the hand-parity contract and the review-recording rule.

## Dead Ends

- A published-package route for a skill-only artifact. Neither precedent publishes a skill; the plugin publishes a compiled server, which is a different problem.

## Edge Cases

- Ambiguous input: "low-friction" could mean zero-touch or few steps. Selected few steps with mechanical drift detection, since zero-touch conflicts with the review gate.
- Contradictory evidence: none.
- Missing dependencies: the PO repo's own build tooling was not inspected, so whether a generator can run there is unverified.
- Partial success: none.

## Sources Consulted

- `AI Systems/Media Editor/runtime/claude-plugin/README.md:83`
- `AI Systems/Media Editor/specs/003-media-editor-extension/008-claude-code-plugin/implementation-summary.md:55`
- `AI Systems/Product Owner/SYNC.md:9,17,44`
- `AGENTS.md:127,138`

## Assessment

- New information ratio: 0.8
- Questions addressed: which sync path is low-friction and defensible.
- Questions answered: the sync question is answered at option level, with one unverified dependency.

## Reflection

- What worked and why: scoring each option against the clone requirement eliminated two options without debate, because that constraint is absolute in this workspace.
- What did not work and why: trying to find a submodule precedent used two searches for a mechanism that does not exist here.
- What I would do differently: state the two-hop split before evaluating options, since the hops have different solvability.

## Recommended Next Focus

Iteration 15: turn the hub anatomy and the hub-conversion cost into a concrete Product Owner change list: which files gain what, in which order, and which existing checkers must learn the new structure.
