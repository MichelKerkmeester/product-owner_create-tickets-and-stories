# Iteration 1: Checking the twelve implementations against the lines they came from

## Focus

Q1. Phases 017 to 028 each carry an `implementation-summary.md`. This iteration reads all twelve summaries, then re-reads the packet text each one changed beside the corpus line the earlier synthesis cited for it, and records where the shipped wording leaves out, overstates or misleads. It builds on `research.md` Section 4 (the twelve ranks), Section 2 (the protected behaviours) and Section 7 (the unverified claims).

## Actions Taken

1. Read the twelve implementation summaries, in four batches, and extracted each phase's stated limitation.
2. Re-read `sk-create-figjam/references/flow-mode.md` Sections 5 to 9, `references/quality-rubric.md` Sections 2, 3 and 6, `references/style-guide.md` Section 1, and the Story and Doc template board-link sentences.
3. Reread the two corpus files the accent, critic and label changes came from: Adobe's `diagram-house-style.md` lines 18 to 90.
4. Ran the router oracle on the four combined requests, two of which the dispatcher names as still broken.
5. Read the pair rule's code: `FIGJAM_SECOND_OUTPUT_RE`, `detect_framing`'s FLOW discard, and the DOC frame noun list.

## Findings

1. **The phase 018 pair rule cannot fire for either request the dispatcher names, and the cause is framing, not the pair regex.** The pair rides on a route whose intent is one of `TASK`, `BUG`, `DOC` or `STORY` [SOURCE: AI Systems/Product Owner/benchmark/router/route_contract.py:718], while `detect_framing` discards `FLOW` only when a second artifact frame already matched [SOURCE: AI Systems/Product Owner/benchmark/router/route_contract.py:648]. The oracle returns `intent: FLOW, source: framing, needs_disambiguation: false` for both "write a doc about onboarding and draw it on a figjam board" and "write a bug about it and add a figjam diagram", so no artifact intent exists to carry a `then`.

2. **"write a doc about onboarding ..." fails because the DOC noun alternation has no bare `doc`.** The list accepts `documentation|docs|document|guide|catalog|behavior reference|runbook|...` but not `doc` [SOURCE: AI Systems/Product Owner/benchmark/router/route_contract.py:305], so `write a doc` matches no DOC frame; the FLOW pattern for `figjam board` then owns the request [SOURCE: AI Systems/Product Owner/benchmark/router/route_contract.py:330]. The generic compound-name frame does not rescue it either, because its noun group repeats the same list [SOURCE: AI Systems/Product Owner/benchmark/router/route_contract.py:339].

3. **"write a bug about it ..." fails because BUG framing needs a report noun or a symptom, not the word bug.** Every BUG frame either names `bug report`/`defect report` [SOURCE: AI Systems/Product Owner/benchmark/router/route_contract.py:261] or a failure symptom such as a crash, a blank value or a 4xx code [SOURCE: AI Systems/Product Owner/benchmark/router/route_contract.py:298]. "write a bug about it" contains neither, and framing runs before the semantic topic scorer, so the bug topic's own `bug` synonym never gets a vote.

4. **The phase 018 limitation understates the gap it records.** It says the two phrasings "still route FLOW, because the DOC and BUG framings do not match those phrasings. This predates the phase." [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/018-artifact-plus-board-pair/implementation-summary.md:96]. The dependency is structural: a route can only carry `then` when an artifact intent wins first, and a request whose only frame is FLOW can never reach that branch. Any future phrasing that names a board strongly enough to frame FLOW is lost the same way, so the recorded limitation is not a phrasing accident.

5. **The tag instruction does not say where the list of created nodes comes from.** It says to "tag every node the write created in one more `use_figma` call" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:188]. A fresh `use_figma` call starts from page state, so it can only find those nodes if the write's response returned their ids or if it filters by something stable. The packet states neither, and its own rollback rule meanwhile treats "no returned id" as a stop condition [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:190]. A model reading this must invent the discovery step.

6. **The tag paragraph mixes the stable key and the per-run value, which breaks the cross-session case it exists for.** One sentence packs "one namespace, with the diagram's name and a run id" together [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:188], while the next paragraph relies on a later session recognising "this work's tag" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:190]. If the run id is part of the key, a new session's key differs and the tag cannot be found, which is the exact revision failure rank 6 was meant to fix. The text never says which of the three is the key and which is the value.

7. **The `setPluginData` hedge leaves the choice open rather than bounded.** The packet writes the tag "because `use_figma` may refuse `setPluginData`" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:188]. Phase 022 softened this deliberately, and its limitation still records the question as open [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/022-created-node-tags/implementation-summary.md:96]. A "may" gives a model no rule for which call to make first, so the wrap-everything instruction becomes the only guidance.

8. **The screenshot critic implemented four of Adobe's five checks and skipped the two the packet cannot otherwise verify.** Adobe's critic checks clutter, weak visual hierarchy, accent misuse, redundant labels and caption match [SOURCE: research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md:85]. The shipped board section checks stretching, overlap, label cut-off, crossings, wrong-join edges, accent placement and the `userIntent` answer [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:78], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:79]. Redundant labels and weak hierarchy are absent.

9. **The repeated-label rule therefore has no verification path at all.** Phase 027 added the four-or-more rule to the rubric and both type references, and its limitation records that "the check script does not count repeated labels, so the rule is checked by hand" [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/027-repeated-edge-labels/implementation-summary.md:95]. With the critic pass also not naming labels [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:78], no script, checklist screenshot or hand pass would catch a board that breaks it.

10. **The hosted-route paragraph states an unverified Code Mode fact as settled.** It says "every manual Code Mode holds here is stdio and none reaches an HTTP server" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:180]. The earlier synthesis listed that as unverified and sourced it only to the vendored wiring guide's own inspection [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/research.md:286]. The implementation promoted a limitation into a fact.

## Ruled Out

- Re-reading all twelve changed files in full. The summaries name the exact anchors, and reading the four areas the summaries flag as uncertain concentrated the evidence.
- Treating the phase 018 limitation as authoritative. Its own wording ("predates the phase") was contradicted by the code path, so the code won.
- Judging the accent (rank 4) or the self-edit guidance (rank 10) as incomplete. Both match the corpus lines: Adobe's "if a reader could only take away one node" test and its "split it or pick one" tie rule sit in the corpus [SOURCE: research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md:22], [SOURCE: research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md:32].

## Dead Ends

- Searching the packet for a script that counts connector labels. None exists, which confirms finding 9 rather than resolving it.
- Looking for a `doc` token in the DOC frame list under another name: `docs` matches only the plural, so the singular is genuinely missing.

## Edge Cases

- Ambiguous input: the dispatcher's two example prompts could be read as requests for the artifact with a decorative board. The oracle's `FLOW` answer shows the router does not even reach that distinction, so the narrow reading (router defect) is the one recorded.
- Contradictory evidence: the phase 018 summary and the code disagree about whether the remaining gap is lexical. Both are recorded above, with the code path preferred.
- Missing dependencies: no live Figma MCP, so findings 5 to 7 stay textual and the tool-output questions move to iteration 2.
- Partial success: eight of twelve phases were checked against a corpus line; phases 023, 024, 025 and 026 were checked only against their summaries.

## Sources Consulted

- `AI Systems/Product Owner/specs/017-figjam-flow-generation/017-board-link-in-artifact` to `028-readback-direction`, each `implementation-summary.md`
- `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md`, `references/quality-rubric.md`, `references/style-guide.md`
- `AI Systems/Product Owner/sk-product-owner/assets/story-template.md`, `assets/doc-templates.md`
- `AI Systems/Product Owner/benchmark/router/route_contract.py`
- `research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md`
- `AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/research.md`

## Assessment

- New information ratio: 1.0
- Questions addressed: Q1
- Questions answered: Q1

## Reflection

- What worked and why: running the oracle before reading the routing code turned two vague complaints into one root cause, because the oracle's `source: framing` field named the layer where the loss happens. Reading each summary's Known Limitations first was the cheapest index of where the implementation is weakest.
- What did not work and why: reading the Adobe file for the accent and label rules also surfaced the critic's full list, which showed a gap (finding 8) that the summaries had not flagged; the batch read was still worth it, but it means the summaries under-report their own omissions.
- What I would do differently: check the framing code path before accepting any implementation summary's account of why a routing case still fails.

## SCOPE VIOLATIONS

None. Every write stayed inside `research/lineages/deepseek-extension/`.

## Recommended Next Focus

Q2. Settle from public documentation and the corpus what the hosted Figma MCP actually exposes: the tool list, `whoami`, the fields `get_figjam` returns, and whether `use_figma` permits `setPluginData` or `setSharedPluginData`. Findings 5 to 7 above are the three that need those answers.
