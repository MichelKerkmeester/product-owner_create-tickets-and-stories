# Iteration 4: The integration gaps that survive the twelve phases

## Focus

Q4, building on iteration 1 findings 1 to 4 and iteration 2 finding 5. The twelve phases closed the artifact link, the ordered pair, the kernel parity sentence, the delivery pointers and the plan lookup. This iteration reads the four integration surfaces that decide whether a user actually gets those behaviours: the kernel's router copy and Flow row, the claude.ai Project's Flow mirror, the ClickUp push contract, and the playbook's boundary scenarios. It asks one question of each: what still breaks after the twelve?

## Actions Taken

1. Read the kernel's Flow row, router copy, Flow Mode Delivery bullet and ClickUp connector contract.
2. Compared the kernel's DOC frame noun list with the router oracle's copy.
3. Read the Project's Flow Mode knowledge file for the tag step, the `whoami` step and the plan question.
4. Listed the playbook's boundary scenarios and read `FJ-037` beside `figjam-as-task-subject.md`.
5. Searched the routing gold rows and fixtures for either failing phrasing.
6. Read the ClickUp tool list's attachment entries.

## Findings

1. **The pair rule's framing blindness is replicated in the kernel, so the fix is a three-copy change.** The kernel's router carries the same DOC noun alternation with no bare `doc` [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:559], matching the oracle's copy [SOURCE: AI Systems/Product Owner/benchmark/router/route_contract.py:305], and the same `FLOW` discard that only fires on a second match [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:601]. Any correction has to land in the oracle, the Router Contract copy and the kernel together, or the differential fails.

2. **The hub promises a doc-sourced board while the router never makes the doc.** The Flow row lists "a doc" among the sources Flow draws from [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:126]. A request that asks for the doc and the board together is routed to FLOW alone [SOURCE: AI Systems/Product Owner/benchmark/router/route_contract.py:648], so the promised doc never exists and Flow has no source to draw from. The row and the route contradict each other for exactly the case the dispatcher names.

3. **Nothing in the routing gate tests either failing phrasing.** The gold rows and router fixtures contain no request that pairs a Doc or a Bug with a FigJam output; the closest pair row is the Story form [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/018-artifact-plus-board-pair/implementation-summary.md:86]. Without a gold row the regression is invisible to the gate, which is why phase 018 could ship a limitation instead of a fix.

4. **The playbook covers the Story pair and the Task-subject negative, and no Doc or Bug pair.** Four boundary scenarios exist, and the pair scenario is the Story one [SOURCE: AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/boundaries/artifact-plus-board-pair.md:15]. A tester following the playbook cannot reach the two phrasings that fail, so the playbook reports a clean run for a rule with a hole in it.

5. **The ordered pair hands the ClickUp offer to the user before the board URL exists.** The kernel says the artifact is "delivered first in its own reply shape" and Flow Mode then runs [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:256], while the artifact's reply shape closes on the ClickUp offer [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:236], [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:296]. A user who accepts that offer pushes the artifact before the board URL is written back, so the pushed copy carries no link and the pair's whole point is lost on the push path.

6. **A board cannot be attached to ClickUp, so the body link is the only route and that makes the sequencing gap matter more.** The attachment tools take a local file: `clickup_request_attachment_upload` attaches "a LOCAL file" and `clickup_attach_task_file` attaches a file to a task [SOURCE: AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:150], [SOURCE: AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:151]. A FigJam board is not a file, so rank 1's body link is correct, and the only defence against finding 5 is to delay or repeat the offer.

7. **The Project's Flow mirror carries every phase 022 to 025 change, so the no-connector path is not the gap.** The mirror names the tag step and its wrap rule [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:163], the rollback and its tag-aware replacement rule [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:165], the `whoami` step [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:158] and the plan question [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:229]. The Project path inherits iteration 2's plan-versus-file confusion and nothing worse.

8. **The ClickUp push itself does carry the link once it exists, because the body travels verbatim.** The connector contract says the remaining body travels "verbatim, already ClickUp-ready" [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:248], so a board URL written into the artifact body reaches ClickUp with no extra tooling. That confirms rank 1's mechanism and moves the defect entirely onto ordering.

## Ruled Out

- Proposing a ClickUp attachment or a Figma embed for the board. The tool list has no board-attach path, and the earlier synthesis already rejected an attachment [SOURCE: AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:130].
- Treating the kernel as the only copy to fix. The differential ties three copies together.
- Reading the Project's no-connector path as the remaining integration gap. Its mirror is current.

## Dead Ends

- Searching the playbook for a Doc-plus-board scenario. None exists under any name.
- Looking for a gold row with "figjam" and "doc" in one request. The gold set holds no such row.

## Edge Cases

- Ambiguous input: "the claude.ai Project's Flow path" can mean the connector path or the no-connector path. Both were read; only the connector path carries a residual defect, inherited from iteration 2.
- Contradictory evidence: the hub's Flow row and the router disagree about whether a doc-sourced board is reachable. Both are recorded; the router's behaviour is the evidence.
- Missing dependencies: no live ClickUp connector, so finding 5 is a sequencing argument from the written contracts rather than an observed push.
- Partial success: eight findings, all from written contracts; nothing was executed.

## Sources Consulted

- `AI Systems/Product Owner/claude project/Custom Instructions.md`
- `AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md`
- `AI Systems/Product Owner/benchmark/router/route_contract.py`
- `AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/boundaries/artifact-plus-board-pair.md`
- `AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md`
- `AI Systems/Product Owner/specs/017-figjam-flow-generation/018-artifact-plus-board-pair/implementation-summary.md`

## Assessment

- New information ratio: 0.92
- Questions addressed: Q4
- Questions answered: Q4

## Reflection

- What worked and why: reading the pair's delivery sentence beside the artifact's closing offer exposed a sequencing defect that neither file shows alone, which is the same seam-reading method that worked in the earlier synthesis's integration iteration. Listing the playbook's four scenarios took one call and settled the coverage question.
- What did not work and why: searching for a gold row assumed one might exist under different wording; none does, so the absence had to be established by listing rather than searching for a phrase.
- What I would do differently: read the delivery and click-through contracts before the routing code when the question is "what breaks for the user", because the user-visible failure is in the ordering, not the classification.

## SCOPE VIOLATIONS

None. Every write stayed inside `research/lineages/deepseek-extension/`.

## Recommended Next Focus

Q5. Recheck the earlier synthesis's rejected ideas and unverified claims against what iterations 1 to 4 established, decide which rejections still stand, and rank the further improvements that are not among the twelve.
