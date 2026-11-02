# Iteration 9: deepening iteration 2 and 7 — the publish protocol that makes sections, idempotency and rollback concrete

## Focus

Deepen iteration 2's section/rollback finding and iteration 7's `id_map` claim by reading the `ompug` Figma driver: the only corpus code that publishes a Mermaid model through the **hybrid** `generate_diagram` + `use_figma` sequence the topic names. This closes Q2 with the full route/read-back matrix and tests Flow Mode's page rollback one more time.

## Actions Taken

1. Read `ompug__diagram-codebase/.../figma/driver.py` (1428 lines): publish order, pending-action protocol, verification and deletion.
2. Read `.../figma/scripts.py` (336 lines): the `use_figma` section-placement script and its idempotency contract.
3. Traced the label-ratio verification (`expected_labels`, `label_ratio`, threshold) and the obsolete-section deletion path.
4. Compared the protocol with Flow Mode's page-based rollback and with iteration 2's section rule.

## Findings

1. The driver defines a fixed publish order: confirm, `whoami` for the plan key, then per diagram `generate_diagram` followed by `use_figma place_section`, then legend, deletion of obsolete sections, `get_figjam` verification and `get_screenshot` for mismatches [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/driver.py:9] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/driver.py:11]. This is the concrete hybrid sequence Flow Mode's write step describes only as "hosted first, `fj` when not connected" [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:64].

2. The FigJam root is addressed as node `0:1`, and the placement script forbids `figma.createPage` and `figma.notify` outright [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/driver.py:44] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/scripts.py:5]. This is the third independent implementation decision against page-based targeting, after the official warning and iteration 2's API notes.

3. Section placement is idempotent by content hash: `place_section` returns an existing section already tagged with the same diagram, run and content hash instead of creating a duplicate [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/scripts.py:14] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/scripts.py:16]. Flow Mode's re-run has no idempotency key, which is why it needs user agreement before a second write [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:159].

4. Every counted action is persisted as `pending_action` **before** it is returned, so a crash leaves an explicitly *uncertain* action that must be reconciled with `get_figjam`, or with a user question when no file exists yet, before any retry [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/driver.py:5] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/driver.py:7] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/driver.py:260]. Flow Mode has no uncertain state: a failed hosted call is indistinguishable from a call that landed.

5. Deletion is scoped and auditable: only diagrams whose status is `obsolete` and whose `section_id` is known are deleted, in one `remove obsolete sections` action, and a failure is recorded as a warning rather than retried blindly [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/driver.py:674] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/driver.py:684]. This is the concrete form of the "delete the nodes the write created" rollback Flow Mode promises but does not operationalize [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:117].

6. Read-back is quantified: expected labels are extracted from the diagram spec or Mermaid source, and a diagram passes when at least 60% of them appear in its section subtree; missing labels are returned for reporting [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/driver.py:32] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/driver.py:1191] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/driver.py:1371]. Flow Mode's exact "8 of 8" is stricter and better for a nine-node cap; the transferable part is the **missing-label list**, which Flow Mode's read-back sentence cannot express [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:140].

7. `get_screenshot` is targeted, not routine: it runs for diagrams whose text verification mismatched, or for all diagrams only with `--verify-visual` [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/driver.py:711] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/driver.py:718]. Flow Mode always asks for a screenshot check on the board, which is safe but costs a visual step even when counts already match [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:65].

8. Each action declares which official skills must be loaded before it runs — `generate_diagram` needs `figma-generate-diagram`; `use_figma` and both read tools need `figma-use-figjam` [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/driver.py:29] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/driver.py:39]. This is a second independent implementation of iteration 1's pre-load requirement, applied per tool rather than once.

9. Sections are named with a stable prefix and supplemented by a legend section, one palette colour per row, with at least 48px padding [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/scripts.py:26] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/scripts.py:28]. Flow Mode's board has no naming convention and no legend, so a multi-diagram flow is navigable only by position [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:99].

10. Verification work is bounded: at most 40 expected labels are compared per diagram [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/driver.py:33]. At Flow Mode's nine-node cap the bound never binds, but it shows the corpus treats read-back as a budgeted operation rather than an unbounded diff.

## Ruled Out

- Adopting the 60% label-ratio threshold into Flow Mode: at nine nodes, partial label coverage is a defect, not a pass.
- Adopting the `pending_action` ledger as a Flow Mode mechanism: Flow Mode has no persistent run state of its own; the principle (record intent before the call, reconcile before retry) can still be stated as guidance.

## Dead Ends

- Searching the driver for a page-based rollback: none exists; every cleanup path is section-scoped. Confirms iteration 2's conclusion rather than adding a new option.

## Edge Cases

- Ambiguous input: none.
- Contradictory evidence: 60% threshold versus Flow Mode's exact matching; resolved as a scale difference (40-label cap versus 9-node cap), not a contradiction.
- Missing dependencies: none.
- Partial success: none.

## Questions Answered

- Q2: the route/read-back matrix is complete. Hosted `generate_diagram` (official, rocket-path, Flow Mode) has no read-back of its own; `use_figma` plugin API (IamTheLime, southleft) verifies by screenshot, board read and connection graph; the Labor tool route verifies by screenshot plus structural checklist; the F-MCP bridge verifies by short returns and targeted reads; Mermaid Jam verifies by parser diagnostics before generation and renders into sections; ompug's driver verifies after publication by label ratio and targeted screenshots. Flow Mode sits at the strong end (counted read-back) but is the only strong route without a missing-item list, uncertain-action reconciliation, or idempotent re-run.

## Questions Remaining

- Q5 (limits verdict) remains open; iterations 10–12 will test the five limits against the corpus and then broaden to new sources.

## Sources Consulted

- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/driver.py`
- `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/scripts.py`
- `AI Systems/Product Owner/sk-product-owner/references/flow-mode.md`

## Assessment

- New information ratio: 0.88 (8 new, 2 partial — page and pre-load findings deepen iterations 1–2)
- Questions addressed: Q2 (answered), Q3 (reconfirmed with implementation evidence)
- Questions answered: Q2

## Reflection

- What worked and why: reading a publish protocol rather than a skill description produced the only crash-safety and idempotency model in the corpus.
- What did not work and why: nothing failed; the driver is long but the publish order header made the target sections obvious.
- What I would do differently: read a driver's module docstring first; it named the entire protocol in eleven lines.

## Recommended Next Focus

Iteration 10: test Flow Mode's five deliberate limits (TD only, 9 nodes, 3 decision exits, one accent, four shapes) against the accumulated corpus evidence, then widen to a new source found by `gh search` for a FigJam or Mermaid diagram skill not yet in the corpus.
