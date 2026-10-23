# Iteration 13: The sync reality that already exists between the two repositories

## Focus

Establish how Product Owner keeps its three surfaces in step today: the shared rule cards, its own skill package, and the Claude Project mirror. This opens the sync question from current mechanics, so any proposed low-friction path is measured against a baseline rather than a blank page.

## Findings

1. Product Owner's Project package is hand-written under a four-step manual parity method: list each skill file against its Project counterpart, decide which paragraphs apply inside a Project, check the read-only drift list, and record each review as a dated sentence. [SOURCE: AI Systems/Product Owner/SYNC.md:9]
2. No manifest, lock file or checksum ledger is kept; the retired compiler's `claude-project.sync.json` and generated regions were archived, and parity is now a reviewer obligation rather than a generated artifact. [SOURCE: AI Systems/Product Owner/SYNC.md:17]
3. The workspace contract agrees and adds the missing piece: a hand-written mirror proves neither human review nor live deployment, review is recorded only after the named human confirms it, and deployment is claimed only with a current receipt and passing smoke evidence. [SOURCE: AGENTS.md:138]
4. Shared rule cards live in `AI Systems/z — Knowledge/`, and Product Owner vendors four of them as regular-file copies because a symlink that climbs out of the repository resolves to nothing once the public repo is cloned; the parity declaration names them `vendored_shared_copies` so a card change turns the system red until the card is copied over its copy. [SOURCE: AI Systems/Product Owner/SYNC.md:44]
5. Kernel review is a human gate with a dated artifact: `claude project/kernel-review.json` records reviewer, decision, `kernelSha256`, kernel version and aligned skill version, and says plainly that nothing reads the file because parity is checked by the parity benchmark plus hand reading. [SOURCE: AI Systems/Product Owner/claude project/kernel-review.json:1]
6. The result is a three-hop manual chain: shared card, then vendored skill copy, then Project mirror, with drift detected only by comparing commit timestamps between a skill file and its counterpart. [INFERENCE: based on the manual parity steps at SYNC.md:9-15 and the vendoring rule at SYNC.md:44]

## Ruled Out

- Assuming an automated mirror still exists. The compiler is retired and the generated regions are archived.
- Treating the git submodule or symlink as a clean sharing mechanism. The vendoring decision exists precisely because links fail in a standalone clone.

## Dead Ends

- Looking for a checksum ledger to compare the two repositories. None is kept by design.

## Edge Cases

- Ambiguous input: "sync" could mean code sync or documentation parity. Selected documentation parity as the observed mechanism, and deferred repository-level sync to the next iteration.
- Contradictory evidence: none; the system note, the root contract and the vendoring record agree.
- Missing dependencies: the parity benchmark script was not run, so its coverage is documented rather than measured.
- Partial success: none.

## Sources Consulted

- `AI Systems/Product Owner/SYNC.md:9-17,44`
- `AGENTS.md:127-140`
- `AI Systems/Product Owner/claude project/kernel-review.json:1-14`
- `AI Systems/Product Owner/claude project/knowledge/` (37 files)
- `AI Systems/z — Knowledge/` (shared card library)

## Assessment

- New information ratio: 1.0
- Questions addressed: how the two repositories stay in step today.
- Questions answered: none fully; the current mechanism is established, the proposed path is not yet evaluated.

## Reflection

- What worked and why: reading the parity note before the Project package made the three-hop chain visible, because the note names each hop in order.
- What did not work and why: expecting a generated manifest wasted a step; its absence is the point.
- What I would do differently: pair the drift rule with the vendoring rule immediately, since together they explain why hand parity is fragile.

## Recommended Next Focus

Iteration 14: evaluate concrete low-friction sync options for an embedded copy: vendored copy with a byte-parity check, generated build output, git subtree or submodule, and a published package, scored against the three-hop chain and the two precedents already researched.
