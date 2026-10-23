# Iteration 4: Where answers live, and what changes when the user declines the loop

## Focus

Deepen iteration 3 finding 2 (assumed versus unasked) and finding 9 (recommended answers) into the packet's own machinery: how a later turn could build on earlier answers, what Quick and Raw energy already do, what "just do it" maps to, and how `sk-prompt` handles the same two problems. Read `sk-prompt`'s rules and fallback scenario, Interactive Mode's energy ladder and smart defaults, the clarification export contract, Flow Mode's energy line, and the kernel's no-file constraint. Builds on iteration 1 finding 8 and iteration 3 finding 9.

## Actions Taken

1. Read `.skilled/skills/sk-prompt/SKILL.md` Section 4 (Always, Never, Escalate) and its unknown-fallback playbook scenario.
2. Re-read Interactive Mode's energy list, command detection and smart-defaults table, and the clarification export contract.
3. Read Flow Mode's `$flow` energy line and the kernel's Deliverable Block and Flow Mode Delivery sections.
4. Compared the persistence options against what Flow Mode already keeps (provenance table, `Left out:` line, `userIntent`).

## Findings

1. **The repo already scales the number of internal rounds by energy, which is the precedent for an energy-scaled intake cap.** `sk-prompt` runs DEPTH for 10 rounds on text modes, 3 for `$short` and 0 for `$raw` [SOURCE: .skilled/skills/sk-prompt/SKILL.md:341]. The rounds are internal reasoning passes rather than user questions, so the mechanism transfers as a count that energy selects, not as a number to copy.

2. **The repo already has a non-interactive path that never asks and states every assumption instead.** `sk-prompt` says an agent or other non-interactive run "never asks: it proceeds on stated assumptions and flags each one in the transparency report", while `$raw` skips questions entirely [SOURCE: .skilled/skills/sk-prompt/SKILL.md:340]. That is the exact shape "just do it" needs: a draft with named defaults, not a refusal and not a silent guess.

3. **The repo already states a numeric escalation threshold on a detection confidence, which shows a threshold can live in a skill contract.** `sk-prompt` escalates when mode-detection confidence is under 50% and asks what type of prompt is being made [SOURCE: .skilled/skills/sk-prompt/SKILL.md:378], [SOURCE: .skilled/skills/sk-prompt/SKILL.md:379]. It is a threshold on intent detection, not on feature understanding, but it settles that a stated number is in keeping with the house style.

4. **"Just do it" already has vocabulary in Interactive Mode: `no questions` selects Quick, and `skip depth` is the only route to Raw.** Energy language maps quick, fast and no-questions wording to Quick, and `$quick` never changes artifact intent [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:237], [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:239]. Raw energy skips the phase flow only when the user explicitly requests "skip depth", and `$quick` never selects Raw [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:75]. So the intake loop needs no new command; it needs a rule for each existing level.

5. **Quick is allowed to skip routine intake, and the facts it may never skip are Doc-shaped, which leaves the board unprotected.** Quick may skip routine questions and use safe defaults but never bypasses Doc purpose, audience, source authority, contradictions or claim status [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:109], [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:305]. The kernel names the same protected set for Task, Bug, Story, Epic and Doc and has no board entry [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:9].

6. **Flow Mode already refuses to let Quick skip the write safeguards, which is the precedent for letting it skip rounds but never the confirmation.** Its `$flow` section says Quick energy "skips nothing here, because the check and the gate guard a write to a shared Figma plan" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:51]. Read against finding 5, the asymmetry is already deliberate: Quick may drop exploration, never the check, the gate or the read-back.

7. **The clarification export holds the question and nothing else, and Flow Mode saves nothing at all, so today an intake answer has no durable home.** A clarification file holds the question and no speculative draft, partial artifact or answer, and the later artifact is a new export under the next number [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:97], [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:98]. Flow Mode writes no file, so it saves nothing, including its question [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:85]. Any intake record must therefore be produced deliberately, not inherited from the clarification file.

8. **The kernel cannot save a file, so its intake record can only be the conversation and a re-rendered reply.** The kernel renders a Deliverable Block because the Project cannot write files, and Flow Mode renders none because its deliverable is a board [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:234], [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:252]. A Project-side intake record must be replayed in each reply, or restated in the Flow gate; it cannot be a Knowledge write.

9. **Some of the record already exists, but only for one turn: the provenance table, the `Left out:` line and the `userIntent` sentence.** The model carries a provenance table mapping each node to its source and source class [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/flow-templates.md:110], and the reply restates what was left out [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/flow-templates.md:137]. The `userIntent` sentence is sent with the write and never shown as a confirmed fact [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:186]. Each is discarded before the next request, so a second turn rebuilds the brief from scratch.

10. **Public practice treats the decisions summary as part of the deliverable, with a confidence beside each decision.** The deep-clarification skill captures decisions inline and closes with a table of decision, justification and confidence, plus assumptions and open items [SOURCE: https://raw.githubusercontent.com/microsoft/devsquad-copilot/main/.github/plugins/devsquad/skills/deep-clarification/SKILL.md]. It also requires a clarification summary before continuing, which is the playback step iteration 3 finding 5 named [SOURCE: https://github.com/svenroth-ai/shipwright/blob/main/shared/requirement-elicitation.md]. The packet has no equivalent recap anywhere in its Flow reply.

11. **[INFERENCE] The energy mapping that follows from findings 1, 4, 6 and 7 is: Quick draws after a single confirmation of proposed facts, Standard runs the loop to confidence, Deep adds the alternative framings and a sketch.** Quick would still confirm the reader and the board's question in one message, because finding 6 shows Flow Mode already protects the write; Standard would cap at three rounds; Deep would cap at five and add the sparring step. The counts are chosen to fit `sk-prompt`'s 10/3/0 ladder at a lower scale for a conversation with a person, not measured.

12. **[INFERENCE] A durable record should be a `Brief` block in the working model, replayed in every round and carried into the gate, never a board node.** An extension the gate did not name needs its own yes, so a brief sticky would cost a second gate and change the deliverable [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md:168], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:67]. A chat-only replay matches the kernel's constraint from finding 8, and in the CLI it can be written into the artifact's clarification lane once the export contract allows a filled brief rather than a question only (finding 7).

## Ruled Out

- **Reusing the clarification export file as the intake record.** The contract forbids the file holding anything but the question, and a project-side run cannot write it at all [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:97], [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:234].
- **Mapping "just do it" to Raw energy.** Raw is reachable only by explicit "skip depth" language and skips the phase flow, which would skip the check and the gate that Flow Mode protects [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:75], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:51].
- **Putting the brief on the board as a sticky or a section.** It is a write outside the diagram and needs its own yes, because an extension the gate did not name is not covered by the first yes [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md:168].

## Dead Ends

- Search for an existing per-turn recap in the packet. Section 8 lists the reply's lines from the board URL to the HVR self-scan, and none of them is a brief [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:235], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:240].
- Search for a state file in `sk-create-figjam`. The packet has no persistent state outside the model and the provenance table, by design.

## Edge Cases

- Ambiguous input: "record" can mean a file, a message or a board node. This pass keeps them separate and rules out the file and board variants on contract grounds.
- Contradictory evidence: Quick is described as able to skip routine intake and as skipping nothing in Flow Mode. Both hold because the two sentences protect different things: exploration versus the check, gate and read-back.
- Missing dependencies: the hybrid-workflow line cited for extensions was read in iteration 1; the exclusion rests on its "only when the gate named an extension" rule.
- Partial success: the energy mapping is inference, marked as such, and needs a synthesis-level decision rather than more evidence.

## Sources Consulted

- `.skilled/skills/sk-prompt/SKILL.md`
- `.skilled/skills/sk-prompt/manual-testing-playbook/smart-routing/unknown-fallback-checklist.md`
- `AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md`
- `AI Systems/Product Owner/sk-product-owner/SKILL.md`
- `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md`
- `AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md`
- `AI Systems/Product Owner/sk-create-figjam/assets/flow-templates.md`
- `AI Systems/Product Owner/claude project/Custom Instructions.md`
- https://raw.githubusercontent.com/microsoft/devsquad-copilot/main/.github/plugins/devsquad/skills/deep-clarification/SKILL.md
- https://github.com/svenroth-ai/shipwright/blob/main/shared/requirement-elicitation.md

## Assessment

- New information ratio: 0.6
- Questions addressed: key question 4, completed; key question 3, deepened.
- Questions answered: "How should intake answers persist across turns, and what changes when the user says just do it or selects Quick energy?"

## Reflection

- What worked and why: reading `sk-prompt` as a sibling skill rather than as part of the topic paid off, because it already solved both problems this iteration needed — energy-scaled rounds and a never-ask path with flagged assumptions.
- What did not work and why: hunting for an existing place to store the brief failed, and the failure is itself the finding: the export contract forbids an answer in the clarification file and Flow Mode writes nothing.
- What I would do differently: start from the export contract in iteration 1 when scoping persistence, because its "question and nothing else" clause decides the design early.

## Recommended Next Focus

Iteration 5: complete the loop's remaining half — how the intake challenges an over-broad brief or the wrong diagram type, what the kernel must carry, and how the loop is tested. Then rank the changes for synthesis. Build on finding 6, finding 8 and iteration 3 finding 4.
