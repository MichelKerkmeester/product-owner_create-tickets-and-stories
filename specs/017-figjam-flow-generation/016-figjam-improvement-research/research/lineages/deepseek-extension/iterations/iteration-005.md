# Iteration 5: Re-testing the rejections and the unverified claims

## Focus

Q5, building on `research.md` Sections 5 and 7 and on iterations 1 to 4. The earlier synthesis rejected fifteen ideas and left eleven claims unverified. Four of those claims were settled in iteration 2, and iterations 1, 3 and 4 changed the evidence under several rejections. This iteration re-tests each rejection against what the run now knows, marks which claims are settled, and closes with a provisional ranking of the further improvements for the synthesis.

## Actions Taken

1. Re-read Section 5's fifteen rejections and Section 7's eleven unverified claims against the evidence gathered in iterations 1 to 4.
2. Counted `pluginData` mentions in the pinned `figma-use` skill and its gotchas beside the copy that carries the prohibition, to test the "older copy" claim.
3. Read the packet's architecture reference against the layout's own hard rules in the OpenAI distribution of Figma's diagram skill.
4. Checked the ClickUp tool surface for any board-capable attach path.

## Findings

1. **Fourteen of Section 5's fifteen rejections still stand, and one needs a qualification rather than a reversal.** "Counting redistributions as separate evidence" is right about independence: a redistribution is one design decision, not three [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/research.md:230]. It is wrong about currency. A discounted copy is one of the few places a changed rule can appear, which is exactly how iteration 2 settled the plugin-data question.

2. **The "lightspeedwp is an older copy" claim is refuted by content, not by date.** The pinned `figma-use` skill and its gotchas contain no `pluginData` mention at all [SOURCE: research/corpus/figma__mcp-server-guide/skills/figma-use/SKILL.md:1], while the copy carries the prohibition as Critical Rule 3a [SOURCE: research/corpus/lightspeedwp__.github/plugins/figma/figma-use/SKILL.md:28]. A copy that holds a newer rule is newer, whatever the file dates say.

3. **The call-shape claim should change label rather than stay open.** Section 7 recorded "which `generate_diagram` call shape the live server accepts" as unknown [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/research.md:280]. The pinned tree holds both shapes side by side, so the honest label is a documented contradiction, and the packet's run-time confirmation rule is the only safe instruction.

4. **The run-manifest rejection is stronger now that the tag mechanism is verified.** Section 5 rejected a disk manifest because the packet leaves no file [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/research.md:226]. With `setSharedPluginData` documented as supported, the board can carry its own record, so a manifest would duplicate a mechanism that works.

5. **The ClickUp rejection was right about attachments and too broad about offers.** It rejected "a ClickUp offer or attachment from the Flow reply" together [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/research.md:227]. The attachment half is confirmed by the tool surface, and the offer half is where iteration 4's sequencing defect lives, so the rejection should split rather than stand whole.

6. **The packet's architecture reference already matches the layout's hard rules, so lane guidance is not a gap.** The layout accepts `flowchart LR` only and requires subgraph ids from a fixed six-value set [SOURCE: research/corpus/openai__plugins/plugins/figma/skills/figma-generate-diagram/references/architecture.md:46], [SOURCE: research/corpus/openai__plugins/plugins/figma/skills/figma-generate-diagram/references/architecture.md:48]. The packet states the same six ids, the same direction and the no-styling rule, and its checker enforces them [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/architecture.md:78], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/architecture.md:87]. A proposal to add architecture guidance would duplicate text that is already correct and enforced.

7. **The one Section 7 claim that became a defect is the Code Mode sentence.** Every other open claim stays open. The claim that Code Mode holds no HTTP manual was recorded as unchecked beyond the vendored guide [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/research.md:286], and phase 019 then wrote it into the packet as settled fact [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:180]. That is the only place where an unverified claim hardened into instruction.

## Provisional Ranking for the Synthesis

Ranked by how certain the gap is, how many requests it touches and the size of the edit. None of these is among the twelve.

1. Make the pair reachable for a Doc or a Bug, and gate it: fix the DOC noun list and add a BUG subject frame in all three copies, then add gold rows, fixtures and playbook scenarios. Evidence: iterations 1 and 4.
2. Rewrite the tag step around the verified call: `setSharedPluginData` with a fixed namespace, the diagram name as key and the run id as value, created-node ids from the tool's return or a page-children scan. Evidence: iterations 1, 2 and 3.
3. Separate the plan the account holds from the plan that owns the file, and name `planKey` and its format. Evidence: iteration 2.
4. Treat an architecture write as a page-level node set in the tag, rollback and read-back. Evidence: iteration 3.
5. Give the screenshot critic a source and the two missing checks, and verify the repeated-label rule on the screenshot. Evidence: iterations 1 and 2.
6. Hold the ClickUp offer until the pair finishes writing the board URL back. Evidence: iteration 4.
7. Name the cap vocabulary and the dangling-connector rule in the read-back. Evidence: iterations 2 and 3.
8. Name the two servers and the read-call allowance in the gate, and say the draft-file cost of a `fileKey`-less retry. Evidence: iterations 2 and 3.

## Ruled Out

- Reversing a rejection on the strength of a single file. Only the "older copy" claim reversed, and only because a newer rule is present in one copy and absent in the pin.
- Adding architecture lane guidance. The packet is already exact, so the change would be duplication.
- Keeping the pair gap as a recorded limitation. The gate can test it, so it is fixable within the phase-018 pattern.

## Dead Ends

- Looking for a Section 7 claim that a public page settles to the packet's detriment. Only the Code Mode sentence qualified, and that is a wording defect rather than a factual one.

## Edge Cases

- Ambiguous input: "Section 5 rejected" covers both a rejected idea and a rejected framing. Both were re-tested under the same question: does new evidence change the decision?
- Contradictory evidence: file dates suggest the copy is older, content shows it is newer. Content wins, and the reasoning is recorded.
- Missing dependencies: no live server, so the call-shape contradiction cannot be resolved by observation.
- Partial success: this iteration is analysis over existing evidence, so its status is `insight` rather than `complete`.

## Sources Consulted

- `AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/research.md` Sections 5 and 7
- `research/corpus/figma__mcp-server-guide/skills/figma-use/SKILL.md`
- `research/corpus/lightspeedwp__.github/plugins/figma/figma-use/SKILL.md`
- `research/corpus/openai__plugins/plugins/figma/skills/figma-generate-diagram/references/architecture.md`
- `AI Systems/Product Owner/sk-create-figjam/references/types/architecture.md`
- `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md`

## Assessment

- New information ratio: 0.85
- Questions addressed: Q5
- Questions answered: Q5

## Reflection

- What worked and why: counting occurrences in both copies turned a date argument into a content argument in one call. Reading the packet's architecture reference last prevented a spurious improvement, because the layout's own hard rules were already adopted verbatim.
- What did not work and why: nothing failed outright; the weak point is that rejection 1's qualification rests on one example, so it is stated as a method caveat rather than a rule change.
- What I would do differently: re-test the rejections before ranking, not after, because two ranked candidates collapsed once the packet's existing text was read.

## SCOPE VIOLATIONS

None. Every write stayed inside `research/lineages/deepseek-extension/`.

## Recommended Next Focus

Synthesis. Rank the eight candidates, name the Product Owner file each changes and the source it comes from, and list every implemented change found wanting with its evidence.
