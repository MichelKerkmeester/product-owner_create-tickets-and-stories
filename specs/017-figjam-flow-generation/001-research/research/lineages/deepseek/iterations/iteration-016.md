# Iteration 16: The gates that will judge the embedded skill

## Focus

Read the Product Owner gate definitions to state exactly what an embedded skill, a new command and a new Project knowledge document must pass. This opens the verification question, because a hub conversion that cannot pass these checks is not finishable no matter how clean the design is.

## Findings

1. The parity gate is shared and lives outside the Product Owner repository: `AI Systems/z — Claude Project Sync Loop/` decides whether the hand-authored Project package matches its skill sources, and PO's `benchmark/parity/` holds only five wrappers that hand over a system id or directory and exec into it. [SOURCE: AI Systems/Product Owner/benchmark/parity/README.md:15]
2. Pair declarations come from the shared `systems.py`, and the gate reads 38 declared pairs for `product-owner`; a new skill-to-knowledge pair must be declared there, which makes the shared declaration a third surface beyond the two repositories. [SOURCE: AI Systems/Product Owner/benchmark/gates/README.md:22] [SOURCE: AI Systems/Product Owner/benchmark/gates/README.md:113]
3. Rule parity counts verbatim spans on both sides of every declared pair with a per-rule floor, and the gate names six rules with the exact phrases that carry them; a new mirrored rule needs a grep-stable span and a floor, not a paraphrase. [SOURCE: AI Systems/Product Owner/benchmark/gates/README.md:23] [SOURCE: AI Systems/Product Owner/benchmark/gates/README.md:38]
4. Example lint validates every worked example and every Project example mirror, then reads each worked reply for its required lines, so a new mode that ships examples inherits that linter's shape requirements. [SOURCE: AI Systems/Product Owner/benchmark/gates/README.md:27]
5. Receipts are a required check: under `--receipts` a missing or stale dated upload receipt is a finding and the run exits 1, so a green gate never proves deployment on its own. [SOURCE: AI Systems/Product Owner/benchmark/parity/README.md:31] [SOURCE: AI Systems/Product Owner/benchmark/parity/README.md:48]
6. The shared residency check holds every declared kernel statement to the kernel or to its declared home, so a rule that moves into a new knowledge document requires updating the declaration rather than only the prose. [SOURCE: AI Systems/Product Owner/benchmark/parity/README.md:34]

## Ruled Out

- Treating the PO repo as the whole verification surface. Two of the required declarations live in the shared Sync Loop folder outside it.
- Shipping examples for a new mode without the reply-shape lines the example linter reads.

## Dead Ends

- Looking for a gate that reads the skill source and the Project mirror for semantic equivalence. Rule parity counts declared phrases only; everything else is a reviewer obligation.

## Edge Cases

- Ambiguous input: "gates" could mean the shared gate or the local runners. Selected both and described which owns what.
- Contradictory evidence: none.
- Missing dependencies: none of the gates were executed here, so their pass/fail behavior is documented rather than observed.
- Partial success: none.

## Sources Consulted

- `AI Systems/Product Owner/benchmark/parity/README.md:15-48`
- `AI Systems/Product Owner/benchmark/gates/README.md:22-38,113`

## Assessment

- New information ratio: 1.0
- Questions addressed: which checks an embedded skill must pass.
- Questions answered: the verification surface is now known at file level.

## Reflection

- What worked and why: reading the gate READMEs by section (declaration, rules, receipts) produced a checklist in the order a change would hit it.
- What did not work and why: assuming all parity logic lived in the PO repo was wrong; the wrappers are deliberately thin.
- What I would do differently: start with `systems.py` location, since every pair depends on a declaration in a third location.

## Recommended Next Focus

Iteration 17: assess the risk register. Read the public-repository and licensing posture plus the auth and runtime assumptions of the Figma path, then rank risks by whether the research can reduce them or only name them.
