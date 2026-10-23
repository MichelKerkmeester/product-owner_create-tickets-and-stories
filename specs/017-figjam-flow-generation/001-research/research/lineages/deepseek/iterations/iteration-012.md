# Iteration 12: What the Moneybird hub conversion actually cost

## Focus

Read the hub conversion phase and its follow-up correction phase for measured cost, defects and review findings, so the Product Owner conversion plan inherits the corrections rather than the diagram. This deepens the hub anatomy into an account of what the conversion broke.

## Findings

1. Hub conversion is a routing move with a small surface: a routing-only root `SKILL.md` picks the packet, `mode-registry.json` and `hub-router.json` name the packets and signals, each packet's former section 2 moves to a `ROUTER.md`, and each packet `SKILL.md` section 2 becomes a short pointer; the whole change shipped as one commit. [SOURCE: AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/017-parent-hub-and-router/implementation-summary.md:54]
2. The first design used one root `ROUTER.md` for all three packets and was rejected on a measured token cost: an accountant request rose from 9,635 to 16,664 `o200k_base` tokens, an increase of roughly 73 percent, so the operator chose one router per packet and the move was rebuilt. [SOURCE: AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/017-parent-hub-and-router/implementation-summary.md:74]
3. A fresh reviewer found four P1 defects in that build: an `AGENTS.md` read order that contradicted the hub, a write-contract check that lost the accountant `SKILL.md` pointer line, four checks that passed with nothing to test, and about fifty stale pointers to `SKILL.md` section 2. [SOURCE: AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/017-parent-hub-and-router/implementation-summary.md:74]
4. The blast radius is tooling rather than prose: every script that read routing had to read `ROUTER.md`, including the route table checker, route replay, exit-code parity, write-contract check, English-first and word-count checks, fragment checks, reference index, token baseline, eval runner and regression-trailer check, each with tests. [SOURCE: AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/017-parent-hub-and-router/implementation-summary.md:54]
5. Hub scoring needed its own evidence: the follow-up phase rewrote stage-one resolution, added 19 HUB gold rows, and made the write-contract check hold `AGENTS.md`, the accountant `ROUTER.md` and the CLI `SKILL.md` to the contract each on its own; its review found prefix matching ("Jortt clients" hitting `jortt cli`) and a double handoff. [SOURCE: AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/018-hub-scoring-and-contract-gaps/implementation-summary.md:54] [SOURCE: AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/018-hub-scoring-and-contract-gaps/implementation-summary.md:78]
6. The audit surfaced structural metadata debt: nine phase folders lacked `description.json` and `graph-metadata.json` and gained them in the follow-up phase. [SOURCE: AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/018-hub-scoring-and-contract-gaps/implementation-summary.md:58]

## Ruled Out

- One shared router file for every packet. It was measured at +73 percent tokens on a default-path request and removed.
- Declaring the conversion done once the files exist. Two review rounds found P1s and unmatched mutants after the first green build.

## Dead Ends

- Looking for a hub conversion that avoided touching scripts. Every routing reader had to move; there is no compatibility shim in the record.

## Edge Cases

- Ambiguous input: "cost" could mean tokens or effort. Selected both and reported the measured token cost separately from the review effort.
- Contradictory evidence: none; the follow-up phase and the first phase agree on what was missing.
- Missing dependencies: the checker scripts were not run here, so defect examples are quoted from the record.
- Partial success: none.

## Sources Consulted

- `AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/017-parent-hub-and-router/implementation-summary.md:54,74`
- `AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/018-hub-scoring-and-contract-gaps/implementation-summary.md:54,56,58,78`

## Assessment

- New information ratio: 1.0
- Questions addressed: Moneybird hub lessons and mistakes.
- Questions answered: the Moneybird half of the lessons question.

## Reflection

- What worked and why: reading the phase record's review paragraph instead of only its file table produced the token measurement and the P1 list, which are the transferable parts.
- What did not work and why: expecting the hub to be a two-file change was only half right; the files are small but the readers are many.
- What I would do differently: read the follow-up phase before the first phase, since the corrections are the durable lesson.

## Recommended Next Focus

Iteration 13: establish the current sync reality between the two repositories. Read how Product Owner's Claude Project package is kept in parity with its skill and how the shared rule cards are vendored, so the sync path proposal starts from what already exists rather than from a green field.
