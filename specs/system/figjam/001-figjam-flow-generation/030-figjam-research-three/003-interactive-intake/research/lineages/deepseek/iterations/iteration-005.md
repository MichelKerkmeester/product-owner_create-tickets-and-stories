# Iteration 5: Challenging the brief, carrying the loop, and testing it

## Focus

Complete the loop's remaining half and settle where it lives. Read the packet's challenge ladder for the wrong request (pre-drawing test, nearest drawable type, budgets and split order), the remove test's dependence on `userIntent`, the hub and `ROUTER.md` leaf loading for a Flow route, the kernel's routing row, Knowledge table and Flow Mode Delivery, and the manual-testing scenario contract. Builds on iteration 4 finding 6 (Quick never skips the gate), iteration 4 finding 8 (the kernel cannot hold state) and iteration 3 finding 4 (the negative-space pass).

## Actions Taken

1. Re-read `references/flow-mode.md` Sections 3, 5, 6 and 9 and `references/quality-rubric.md` Sections 2 and 3.
2. Read the hub `SKILL.md` routing rules and `ROUTER.md` leaf sets for FLOW and INTERACTIVE.
3. Read the kernel's routing table, Resource Domains list, Knowledge table and Flow Mode Delivery.
4. Re-read `manual-testing-playbook/boundaries/command-conflict-asks.md` and listed the playbook groups.

## Findings

1. **The challenge ladder for a wrong or oversized request already exists, and it is complete once a type is named.** It asks whether a list, table or paragraph would serve better [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:89], maps an undrawable kind to the nearest drawable type and says so plainly [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:93], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:95], keeps a per-type budget and splits rather than shrinks [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:162], and runs cuts in a fixed order [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:170]. What it cannot do is challenge a brief that names no type at all, because the ladder starts at the type.

2. **The nearest-type mapping is already a proposal rather than a question, which is the sparring pattern in miniature.** The packet offers the kind that answers the same question instead of asking what the user meant [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:95]. That is the shape the whole intake should take: propose an interpretation, let the user accept or correct it.

3. **The type table is written as the reader's questions, so the question bank's type fact already exists.** Each row is a question a reader could ask, from "which screens does a person pass through" to "which tasks and phases are active when", with the type that answers it [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:79], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:85]. The intake can ask which question the board answers by quoting these rows rather than inventing vocabulary.

4. **The remove test depends on a sentence the intake never establishes, so an over-broad brief cannot be diagnosed before the model exists.** The rubric says every node must serve the `userIntent` sentence and that a node which cannot be removed without losing a step stays [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:38], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:37]. That sentence is only composed at the write call [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:186]. Settling it in the intake would let the rubric's first test run on the outline instead of after the model.

5. **A Flow request loads only the Flow leaf pair, so an intake that lives in Interactive Mode would never load on a Flow route.** One dominant intent routes one leaf set, and two intents that tie take the INTERACTIVE set and its one question [SOURCE: AI Systems/Product Owner/ROUTER.md:37]. FLOW's leaves are `flow-mode.md` and `flow-templates.md` [SOURCE: AI Systems/Product Owner/ROUTER.md:91], [SOURCE: AI Systems/Product Owner/ROUTER.md:92]. The hub starts `$flow` in the `sk-create-figjam` packet directly [SOURCE: AI Systems/Product Owner/SKILL.md:53]. The intake loop therefore belongs in `flow-mode.md`, with only the shared rules pointing at it.

6. **The kernel can carry policy but not a state machine, and it already says what to do when a detail is missing.** It states that when a Knowledge detail is unavailable, the Project should "state the assumption and ask one comprehensive question rather than inventing a parameter" [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:57]. It cannot write files and renders a Deliverable Block only because it cannot [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:234]. So the kernel carries the cap, the protected facts, the one-confirmation rule and the replay sentence, while the round mechanics stay in the mirrored Flow Mode knowledge.

7. **The kernel's Flow row and Flow Mode Delivery would each need one sentence, and its Knowledge table already has the two mirrors the loop must edit.** The routing table's Flow row names sources and output but no intake [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:126]. Flow Mode Delivery lists the gate facts and the reply lines but no rounds [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:254]. The Knowledge table names "Templates - Flow Mode" as covering type choice, intake, shared rules, the gate and read-back, and "System - Interactive Mode" for ambiguity and one-question intake [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:207], [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:210]. A kernel change is therefore a two-sentence edit plus a hand-written mirror update in the two knowledge files, which is the manual parity method.

8. **The test contract needs a carve-out before it can test the loop, because one scenario fails a run that asks twice.** FJ-020 passes if exactly one question names both artifacts and fails if more than one question is asked [SOURCE: AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/boundaries/command-conflict-asks.md:29]. That is correct for an artifact conflict and wrong for a board intake, so the pass condition needs to distinguish "one question to settle the artifact" from "rounds to settle the board", and the exception has to be named in the scenario rather than assumed.

9. **The playbook is organised by group, so the loop's scenarios have a home and a naming pattern already.** Scenarios are grouped as `boundaries/`, `board-creation/`, `board-quality/` and `board-write/`, with one file per scenario and a pass/fail line [SOURCE: AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/boundaries/command-conflict-asks.md:29]. At least four new scenarios are implied by the research: a thin brief, an over-broad brief, the wrong type, and just-do-it at Quick energy.

10. **[INFERENCE] A brief-completeness check cannot live inside `flow_check.py`, because that check reads Mermaid and the brief precedes the model.** The check runs on the model before the write gate [SOURCE: AI Systems/Product Owner/sk-create-figjam/SKILL.md:170], and its self-test proves each rule fails on a planted model [SOURCE: AI Systems/Product Owner/sk-create-figjam/SKILL.md:198], [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/flow_check.py:206]. The brief therefore needs its own rubric walk, in the same "judged by hand" position the quality rubric occupies before the gate, not a new script rule.

11. **[INFERENCE] The ranked changes that follow are eight, and only three touch more than one file.** They are: the nine-fact confidence model with captured/assumed/corrected states; the round cap and stop rule keyed to energy; the question bank with recommended answers; the sparring step with three proposals; the challenge rules for an over-broad brief and a wrong type; the Brief block and per-round replay; the just-do-it and Quick rules; and the kernel plus test-contract parity. The three multi-file ones are the confidence model (flow-mode, rubric, kernel), the Brief block (flow-mode, flow-templates, Interactive Mode knowledge) and the parity pair (kernel, two knowledge files).

## Ruled Out

- **Putting the intake in `sk-product-owner/references/interactive-mode.md`.** A Flow route does not load it, and the hub starts `$flow` in the other packet [SOURCE: AI Systems/Product Owner/SKILL.md:53], [SOURCE: AI Systems/Product Owner/ROUTER.md:37].
- **Adding a new packet or a new Knowledge file for the loop.** The loop is a step inside Flow Mode, and the kernel's Knowledge table already names Flow Mode as owning "intake" [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:207]. A new file would double the parity surface for no gain.
- **A script rule in `flow_check.py` for brief completeness.** The check's input is the model, and the brief is settled before the model [SOURCE: AI Systems/Product Owner/sk-create-figjam/SKILL.md:170].

## Dead Ends

- Search for an existing intake test in the playbook: all 25 scenario files cover routing, board creation, board quality, board writes and boundaries; none covers an under-specified brief.
- Search for any state file or cache in `sk-create-figjam`: none exists, by design.

## Edge Cases

- Ambiguous input: "challenge" can mean challenge the type or challenge the scope. Both are covered, and they land on different evidence: the type table for one, the remove test and budget for the other.
- Contradictory evidence: none new. The test-contract conflict from finding 8 is real and is recorded, not smoothed.
- Missing dependencies: the playbook's group list was read from the directory listing plus one scenario; the count of scenario groups rests on those names.
- Partial success: the eight-change ranking is inference at this stage and is refined in the synthesis with per-file citations.

## Sources Consulted

- `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md`
- `AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md`
- `AI Systems/Product Owner/sk-create-figjam/SKILL.md`
- `AI Systems/Product Owner/sk-create-figjam/scripts/flow_check.py`
- `AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/boundaries/command-conflict-asks.md`
- `AI Systems/Product Owner/SKILL.md`
- `AI Systems/Product Owner/ROUTER.md`
- `AI Systems/Product Owner/claude project/Custom Instructions.md`

## Assessment

- New information ratio: 0.55
- Questions addressed: key questions 3 and 5, completed.
- Questions answered: "How should the intake challenge an over-broad brief or the wrong diagram type, and how does the Claude Project kernel carry the loop?"

## Reflection

- What worked and why: checking the hub and ROUTER leaf loading settled the placement question before any design work, and it changed the answer: the loop cannot live in Interactive Mode.
- What did not work and why: looking for a script-level home for a brief check failed for a structural reason, since the checker's input is the finished model.
- What I would do differently: read the ROUTER's leaf loading in iteration 1, because it determines where every later change lands.

## Recommended Next Focus

Synthesis: rank the changes, name the Product Owner file each changes, and write the convergence report. No further iteration; the cap is reached.
