---
title: "Interactive Intake for sk-product-owner and sk-create-figjam: Research Synthesis"
description: "A confidence model, stop rule, question bank and sparring step for a FigJam board intake, with ranked changes by Product Owner file."
version: 1.0.0.0
---

# Interactive Intake for sk-product-owner and sk-create-figjam: Research Synthesis

This synthesis covers the five-iteration DeepSeek fan-out lineage `fanout-deepseek-1792563734045-t20sb9` in `research/lineages/deepseek`. It designs an intake that keeps asking until it understands a feature well enough to draw, spars with the user about what the board conveys and how it looks, and stops.

Every claim below was checked against the cited Product Owner line, corpus line or public page. Where a claim is inference from two sources it is marked `[INFERENCE]`. Section 11 names the Product Owner file each ranked change edits. The earlier research in `AI Systems/Product Owner/specs/017-figjam-flow-generation/009-figjam-skill-research/` and `016-figjam-improvement-research/` was read first; its implemented changes are treated as fixed and are not re-proposed.

---

## 1. Summary

The packet does not need a new interviewer. It needs a definition of done for understanding, and a loop that runs until that definition is met or must stop.

1. **Today the intake is one question and then a draft.** Interactive Mode's own contract asks for all unresolved information at once and forbids a second round except for a source conflict, a promised missing source or a decision the user calls unsettled [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:58], [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:519]. Flow Mode has no intake loop at all: it asks only when two types fit, two orders fit, no source wins, the plan is unclear or the read-back differs, and then asks one question [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:75], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:274].
2. **The confidence model should be a nine-row Brief, not a feeling.** Each row is a fact the board cannot be drawn without, and each has one status: captured, corrected, assumed or unasked. A row may be assumed only when the supplied sources cannot answer it, and the assumption must name what would settle it; "`assumed` is for unobtainable answers, never for unasked questions" [SOURCE: https://github.com/svenroth-ai/shipwright/blob/main/shared/requirement-elicitation.md].
3. **The stop rule is a floor and a ceiling.** Draw when the Brief is complete; stop asking when two consecutive rounds change nothing; cap the loop at three rounds for Standard and five for Deep, with one confirmation and no rounds for Quick. Public practice supplies both poles: premature convergence causes underspecified features, and probing past a convergence signal is an anti-pattern [SOURCE: https://raw.githubusercontent.com/microsoft/devsquad-copilot/main/.github/plugins/devsquad/skills/deep-clarification/SKILL.md].
4. **Every question carries a recommended answer, and every round ends with a proposal.** The packet already does this in miniature when it offers the nearest drawable type instead of asking what the user meant [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:95]. The full sparring step adds an outline, two framings and a Mermaid sketch before the board.
5. **The loop belongs in `flow-mode.md`, not in Interactive Mode.** A Flow request loads only the Flow leaf pair, so an intake living in Interactive Mode would never load on a Flow route [SOURCE: AI Systems/Product Owner/ROUTER.md:37], [SOURCE: AI Systems/Product Owner/ROUTER.md:91]. Interactive Mode keeps its one-question rule for artifact ambiguity, with one named exception for a board intake.
6. **The loop is cheap to carry and expensive to leave out.** Eight ranked changes and one contract sentence; the kernel needs two sentences plus a hand-written mirror update, because a Project cannot hold a state machine or write a file [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:234].

---

## 2. What the packets already do well

These are protected. No change below removes them, and the synthesis is written so a reviewer can check nothing good was traded away.

- **The one-question ceiling at the gate.** The write gate asks once, with the plan, file, effect, extensions, read calls and rollback in one message [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:65]. The loop adds rounds before the gate and never turns the gate into another interview.
- **The nearest-drawable-type offer.** The packet says plainly that Figma cannot draw a journey, timeline, class, C4, pie, mindmap, Venn, quadrant or git graph, and offers the nearest kind that answers the same question [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:93], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:95].
- **The pre-drawing test.** Before any model, the packet asks whether a list, table or paragraph would serve the reader better [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:89].
- **Never invent.** A missing step, service, field or date is asked about or left as a named gap, and a diagram of a real partial system beats a polished invented one [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:144].
- **The two dials with defaults.** Detail level defaults to Balanced and audience to Mixed, and each is a stated choice [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:150], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:151].
- **The type table as the reader's questions.** Every row is a question a reader could ask, with the type that answers it [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:79]. This is the question bank's backbone.
- **The check, the rubric, the budget and the split order.** The model must pass `flow_check.py` before the gate [SOURCE: AI Systems/Product Owner/sk-create-figjam/SKILL.md:170], the remove test decides whether each node earns its place [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:37], and an over-budget diagram splits rather than shrinks [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:162].
- **Quick never skips the write safeguards.** Flow Mode says Quick "skips nothing here, because the check and the gate guard a write to a shared Figma plan" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:51].
- **The provenance table and the omission line.** Every drawn item has a source and a source class, and everything left out is named with its reason [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/flow-templates.md:110], [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/flow-templates.md:137].
- **The bounded repair loop.** After two attempts at one diagram the packet stops and asks [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:262].
- **The never-infer fact.** The Figma plan is must-ask and never inferred from a file key [SOURCE: research/corpus/figma__mcp-server-guide/skills/figma-spec/SKILL.md:9].

---

## 3. What the intake does today

The audit found a single-shot contract stated in five places, and a Flow packet with no interview at all.

- **Single question, one wait, then draft.** The architecture is `Start -> Single Question (ALL info) -> Wait -> Process -> Deliver` [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:54]. The only legal second round is a source conflict with no authority winner, a promised missing source or an unsettled decision [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:58], and the MUST NOT list repeats it [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:519]. The kernel repeats the rule for the Project [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:9].
- **One template for every artifact kind.** The comprehensive question asks the same six blocks, with the energy choice first and "assumptions to challenge" last [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/interactive-response-templates.md:53], [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/interactive-response-templates.md:81]. Nothing in it asks for the reader, the board's question or its outcome.
- **No confidence measure.** The state machine's question state waits once and proceeds [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:188]. The quality dimensions score the question, not the understanding: clarity, completeness, assumption challenge, perspective diversity and mechanism depth, each 8 or above [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:431].
- **Routing confidence is not board confidence.** HIGH routes at 0.85, LOW from 0.40 enters Interactive Mode, and below 0.40 falls back with one question [SOURCE: AI Systems/Product Owner/sk-product-owner/references/routing.md:38], [SOURCE: AI Systems/Product Owner/sk-product-owner/references/routing.md:41]. A one-line brief can route to FLOW at HIGH.
- **Flow Mode asks in five situations only.** Two types fit [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:75], two orders fit or no source wins [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:111], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:121], the plan or file is unclear [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:274], or the read-back differs [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:258]. Its escalation is a pointer to Interactive Mode and still one question [SOURCE: AI Systems/Product Owner/sk-create-figjam/SKILL.md:65], [SOURCE: AI Systems/Product Owner/sk-create-figjam/SKILL.md:185].
- **The gate confirms the write, not the understanding.** Its facts are plan, file, effect, extensions, read calls and rollback [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:65]. None is the reader or the message.
- **The test contract forbids a second question.** FJ-020 fails a run that asks more than one question [SOURCE: AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/boundaries/command-conflict-asks.md:29].

**Why it matters for a board.** A board drawn from a one-line brief passes every check the packet has. The type can be right, the model can be valid, the gate can be answered and the read-back can match, while the board answers no question its reader actually has. The packet has no step that would catch that.

---

## 4. What the corpus adds

The corpus supplied the only working multi-round board flow in public Figma practice, plus the precedent that asking is upstream behaviour already.

- **Figma's own diagram skill asks one or two questions when the brief is thin, and says "one good question beats one wasted diagram"** [SOURCE: research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:69]. The packet quotes the same line [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:144]. The loop has to go past upstream, not match it.
- **Figma's project-plan skill runs typed rounds.** Every step is Research, Confirm or Write, and a Confirm step is a user decision with no board writes [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:227], [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:229]. Its self-check may loop: "If not, loop back and ask" [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:255].
- **Its readiness test is per item, not a score:** `ready` or a specific non-empty gap list [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:298], and each gap must be an answerable question rather than "tell me more" [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:295].
- **It caps a round's width at four questions** and stores the approved set, marks skips and re-asks after an edit [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:276], [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:320]. It never caps the number of rounds.
- **A board plan can carry a purpose sentence.** `ompug`'s plan gives each diagram a `purpose` — "one sentence: what question this diagram answers" — plus notes and skipped reasons [SOURCE: research/corpus/ompug__diagram-codebase/docs/DESIGN.md:157], [SOURCE: research/corpus/ompug__diagram-codebase/docs/DESIGN.md:148].
- **The asking that exists is scope-bounding.** A FigJam builder asks which sections matter for a 200+ node board instead of reading it all [SOURCE: research/corpus/prasantloki__figjam-builder/SKILL.md:417]; Figma's diagram skill asks which variation to keep and remembers the answer for the session [SOURCE: research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:112].
- **The only cap upstream is on regenerating, not asking.** Adobe stops after two regenerations and asks what is wrong [SOURCE: research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/SKILL.md:161].

**Verdict.** The corpus proves the pieces work in isolation: batched questions, proposed cards, stored approvals, purpose sentences. None of the public skills applies them to a diagram's content and look, and none bounds the loop.

---

## 5. What public practice adds

Three practices supplied the missing theory: a coverage contract from requirements elicitation, stop rules from a clarification skill, and a staged critique from design review.

- **The coverage guarantee.** A named dimension set must be covered wherever a requirement is elicited, and a requirement is not finished until every row is captured or explicitly recorded as an unconfirmed assumption; a silently blank row is forbidden [SOURCE: https://github.com/svenroth-ai/shipwright/blob/main/shared/requirement-elicitation.md].
- **Assumed versus unasked.** A row may be marked assumed only where the answer cannot be obtained, with what would settle it named; marking something assumed while someone who could answer is present is declining to ask [SOURCE: https://github.com/svenroth-ai/shipwright/blob/main/shared/requirement-elicitation.md].
- **The outcome spine.** Criteria that describe steps "read as thorough and verify nothing"; the outcome needs a fit criterion answerable yes or no [SOURCE: https://github.com/svenroth-ai/shipwright/blob/main/shared/requirement-elicitation.md].
- **The negative-space pass.** Before confirming, ask what the work should guarantee that it does not, read the request as a promise and check both halves, and ask what it must refuse [SOURCE: https://github.com/svenroth-ai/shipwright/blob/main/shared/requirement-elicitation.md].
- **Playback before action.** The shared understanding — capability, boundaries, failure behaviour, open assumptions — is played back and confirmed before anything is written [SOURCE: https://github.com/svenroth-ai/shipwright/blob/main/shared/requirement-elicitation.md].
- **Evidence before questions.** Look the fact up first; if the source answers it, state the finding and ask only whether it is still current [SOURCE: https://raw.githubusercontent.com/microsoft/devsquad-copilot/main/.github/plugins/devsquad/skills/deep-clarification/SKILL.md].
- **A recommended answer on every question** [SOURCE: https://raw.githubusercontent.com/microsoft/devsquad-copilot/main/.github/plugins/devsquad/skills/deep-clarification/SKILL.md].
- **Stopping rules.** Two consecutive no-new-information answers, a hard question budget, and a user stop all end the session; both premature convergence and probing past a convergence signal are named anti-patterns [SOURCE: https://raw.githubusercontent.com/microsoft/devsquad-copilot/main/.github/plugins/devsquad/skills/deep-clarification/SKILL.md].
- **Probe set for vague answers:** concrete scenario, edge case, contradiction, terminology, scale, failure mode, boundary [SOURCE: https://raw.githubusercontent.com/microsoft/devsquad-copilot/main/.github/plugins/devsquad/skills/deep-clarification/SKILL.md].
- **Review starts with the problem and changes by stage.** Google's design review guidance says to articulate and agree on the problem first, and maps early work to the problem, mid-stage to the solution and late stage to implementation [SOURCE: https://design.google/library/reviewing-the-design-review].
- **Critique questions for the look:** where the eye goes first, whether that is the most important element, whether spacing groups what belongs together, and the squint test [SOURCE: https://thecrit.co/resources/design-critique-questions]. Critique teaching orders the moves describe, then purpose, then evaluate, and forbids prescribing [SOURCE: https://pages.graphics.cs.wisc.edu/VisSnacks/tutorials/4-critique/].
- **The repo's own precedent.** `sk-prompt` scales internal rounds by energy, has a non-interactive path that proceeds on stated assumptions, and escalates below a stated 50% confidence [SOURCE: .skilled/skills/sk-prompt/SKILL.md:341], [SOURCE: .skilled/skills/sk-prompt/SKILL.md:340], [SOURCE: .skilled/skills/sk-prompt/SKILL.md:378].

---

## 6. The confidence model: nine facts a board intake must know

The Brief has nine rows. Each row is one fact, one value, one status and one source. The status vocabulary is `captured`, `corrected`, `assumed` or `unasked`. The model is deliberately smaller than a requirements checklist and larger than the two dials, because a board needs a reader, a message and a shape before it needs an audience dial.

| # | Fact | What it must answer | Status source |
|---|---|---|---|
| 1 | **Reader** | Who reads this board, and what do they already know? | Chosen from the type's audience dial: Mixed, Engineer or Executive [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:151] |
| 2 | **Question** | The one sentence the board answers, written as a question a reader would ask | The type table is already phrased this way [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:79] |
| 3 | **Outcome** | What the reader can decide or do after seeing it, answerable yes or no | The outcome spine from elicitation practice [SOURCE: https://github.com/svenroth-ai/shipwright/blob/main/shared/requirement-elicitation.md] |
| 4 | **Scope** | What is in the board and, explicitly, what is out | The out-of-scope dimension [SOURCE: https://github.com/svenroth-ai/shipwright/blob/main/shared/requirement-elicitation.md], and the packet's `Left out:` line [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/flow-templates.md:137] |
| 5 | **Entry** | The trigger that starts the flow, or the boundary where the board begins | The type sections require a start or trigger [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:134] |
| 6 | **Exit** | The end state, the merge point or the success condition | The user-flow merge dot and end shapes [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md:45] |
| 7 | **Actors** | Who performs each step, or which parties exchange messages | Per-type needs, process lanes and sequence participants [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:135], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:137] |
| 8 | **Decisions and states** | Every branch point with its labelled exits, and the state set where the type is a state diagram | Decision exits are question-and-answer labels [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/flow-templates.md:36], and states with their transitions are a type need [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:138] |
| 9 | **Sources and their class** | Which supplied source backs each fact, and whether it is current behaviour, approved direction, proposal, retired or unknown | The five source classes and the authority order [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:120] |

**Statuses, defined.**

- `captured` — the user stated it, or a supplied source states it and the packet found it by reading first [SOURCE: https://raw.githubusercontent.com/microsoft/devsquad-copilot/main/.github/plugins/devsquad/skills/deep-clarification/SKILL.md].
- `corrected` — the intake proposed a value and the user changed it. A corrected row counts as settled, because the correction is the strongest evidence in the Brief.
- `assumed` — no supplied source and no answer can settle it, and the row names what would settle it. Permitted only for facts 3 to 9, at most two rows, never for the reader or the question [SOURCE: https://github.com/svenroth-ai/shipwright/blob/main/shared/requirement-elicitation.md].
- `unasked` — nobody has asked and no source covers it. This is the only status that blocks the board, and it is the one the current packet cannot see [SOURCE: https://github.com/svenroth-ai/shipwright/blob/main/shared/requirement-elicitation.md].

**The two never-assume rows borrow the strongest rule the corpus has.** Figma's plan is must-ask and never inferred; the reader and the question are the board's plan [SOURCE: research/corpus/figma__mcp-server-guide/skills/figma-spec/SKILL.md:9].

**Why nine and not the packet's two dials.** The dials decide how much and for whom, and they already work [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:146]. They cannot say what the board is about. The Brief sits before the dials and sets them: a captured reader selects the audience dial, and a captured outcome sets the detail level.

---

## 7. The threshold, the stop rule and the round cap

**The threshold.** The board is draw-ready when all nine rows have a status, no row is `unasked`, at least seven are `captured` or `corrected`, the reader and the question are among them, and any `assumed` row names its settlement.

This is a completeness threshold and not a probability. Public practice states completeness, and a search found no authoritative calibrated confidence number for elicitation; the only numeric precedent in the repo scores intent detection, not understanding [SOURCE: .skilled/skills/sk-prompt/SKILL.md:378]. The packet should not invent a percentage it cannot compute.

**The stop rule, in order.**

1. **Complete.** All nine rows are set, the threshold holds, and the intake plays the Brief back for one confirmation before the model or the gate.
2. **Diminishing returns.** Two consecutive rounds where no row changes status end the questions. The remaining rows become `assumed` with settlements, and the confirmation states them. Public practice's three-question version is adapted to two because a board has fewer facts than a requirement [SOURCE: https://raw.githubusercontent.com/microsoft/devsquad-copilot/main/.github/plugins/devsquad/skills/deep-clarification/SKILL.md].
3. **User stop.** "That is enough", "just do it", "no questions" or any clear instruction to proceed moves the intake to the proposal path in Section 10 immediately.
4. **Round cap.** Standard stops at three rounds, Deep at five, Quick at zero. The cap is a hard stop for asking, not for drawing: at the cap the packet either draws with the remaining `assumed` rows named under `Left out:` and in the confirmation, or says plainly that the sources cannot support the board and offers a Doc or a table instead. It never keeps interrogating and it never invents.

**Why a cap is safe.** The packet already has a no-route branch that offers the checked model and refuses to render a stand-in board [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:209]. A Brief that cannot be completed can take that branch rather than burn rounds.

**What the cap counts.** Rounds, not questions. A round carries one to three questions, so a Standard intake asks at most nine questions in three rounds and a Deep intake at most fifteen in five. Figma's project plan caps a round at four and never caps the rounds [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:276].

---

## 8. The question bank: few high-value questions per round

The bank is organised by Brief row, ordered by dependency, and every question ships with a recommended answer. A question without a recommendation is a form field, and the brief asks for sparring, not a form [SOURCE: https://raw.githubusercontent.com/microsoft/devsquad-copilot/main/.github/plugins/devsquad/skills/deep-clarification/SKILL.md].

**Round 1 — the three that decide everything.** The reader, the question, the outcome. They are independent of each other and every later question depends on them.

- **Reader (recommended: Mixed team).** "Who is this board for — the team building it, engineers reading exact names, or leadership reading outcomes? I would default to the mixed team, because the flow's labels usually carry it." Options come from the audience dial [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:151].
- **Question (recommended: quote the row from the type table).** "Which of these should the board answer: *which screens does a person pass through*, *who does what and where does work change hands*, *which states exist and what moves between them*?" The table supplies the wording [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:79].
- **Outcome (recommended: the decision the source implies).** "After seeing this, what should the reader be able to decide — approve the flow, spot where a hand-off fails, or see which states the record can reach?" The outcome must be answerable yes or no [SOURCE: https://github.com/svenroth-ai/shipwright/blob/main/shared/requirement-elicitation.md].

**Round 2 — shape and extent.** Entry, exit, actors. These depend on round 1's question, because a state diagram's actors are not lanes.

- **Entry and exit (recommended: from the trigger grammar).** "Where does this start, and what counts as done? The screenshots imply *dashboard open* as the start and *saved search confirmed* as the end."
- **Actors (recommended: the fewest the sources support).** "Who does each step — only the person, or the person plus the billing system?"

**Round 3 — the detail that changes the drawing.** Decisions and states, plus sources.

- **Decisions and states (recommended: the branches the source states).** "The source has two branch points: no results and a permission failure. Are there others, or should the board show those two and name the rest as out?" Decision exits are question-and-answer labels [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/flow-templates.md:36].
- **Sources and class (recommended: the authority order).** "I read the flow from the product doc and the schema. The doc is current behaviour; the schema is the source for the field names. Is the retry step approved direction or a proposal?" The five classes are already the packet's language [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:120].

**Round discipline.**

- One to three questions per round, never four or more, and never a question whose answer is already in a supplied source. Look first, then ask only whether the finding is current [SOURCE: https://raw.githubusercontent.com/microsoft/devsquad-copilot/main/.github/plugins/devsquad/skills/deep-clarification/SKILL.md].
- Independent facts may share a round; a fact that changes the next question may not. That reconciles the one-at-a-time doctrine with the batched practice [SOURCE: https://raw.githubusercontent.com/microsoft/devsquad-copilot/main/.github/plugins/devsquad/skills/deep-clarification/SKILL.md], [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:276].
- A vague answer is not an answer. Use the probe set: a concrete scenario, an edge case, a contradiction, a term, a scale, a failure mode or a boundary [SOURCE: https://raw.githubusercontent.com/microsoft/devsquad-copilot/main/.github/plugins/devsquad/skills/deep-clarification/SKILL.md].
- Suggested answers are stated as recommendations, never as decisions. The user can always correct one, and a correction is recorded as `corrected`.

---

## 9. The sparring step: propose, do not only ask

Three proposals, in increasing cost, each ending in one accept-or-edit question. They occur before `flow_check.py`, because a model that fails the check on a wrong premise wastes a round [SOURCE: AI Systems/Product Owner/sk-create-figjam/SKILL.md:170].

1. **The outline.** A plain list of the nodes and edges the board will carry, one line each, with its Brief row. It is not Mermaid, so it costs nothing and can be edited fast. The remove test can run on it: can a line go without losing a step the reader needs [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:37]? This is the point where an over-broad brief is cheapest to catch.
2. **Two framings.** Two ways the same sources can be drawn, each with one sentence on what it buys and what it costs. For a Fernhouse saved-search flow: *person-first* (screens and choices) versus *state-first* (which saved-search states exist and what moves them). Each answers a different reader question, which is exactly why the packet already asks when two types fit [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:75]. The intake recommends one and says why.
3. **The Mermaid sketch.** The chosen framing as a Mermaid block, shown in chat and not written to a board, with the provenance table's source class per node [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/flow-templates.md:110]. A sketch is the cheapest way to make the shape arguable before the gate, and public practice's preview-then-ask loop is the same move at section scale [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:319].

**The look, without taste assertions.** The look is settled with four concrete choices, each proposed:

- **The accent.** One node at most, chosen by the test the rubric already teaches: the node a reader would keep if they could keep only one, never the node that comes first [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:49]. The intake proposes the candidate and its reason.
- **The detail level and audience.** Proposed from the Brief: a captured reader picks the audience, and a captured outcome picks Balanced, Simplified or Faithful [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:150].
- **The grouping.** Whether the board needs sections at all, or a single flow; Figma's own layout is a generator decision the packet never overrides [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:164].
- **The critique questions, asked about the sketch.** Where does the eye go first, is that the most important node, do the groupings match the story, and does the board still read at a squint [SOURCE: https://thecrit.co/resources/design-critique-questions].

**What this is not.** It is not a redesign of the board by hand: the generator owns the layout, and no node is moved or restyled [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:164]. It is not an extension: the sketch is working data and the reply still carries only the five lines [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:235].

---

## 10. Challenging an over-broad brief or the wrong type

Both challenges are proposals with a reason, not refusals, and both use machinery the packet already has.

**Over-broad brief.** The ladder runs in this order, and each rung is cheaper than the next:

1. **The negative-space pass.** "What should this board *not* do?" and "what must it refuse to show?" Public practice asks these before confirming [SOURCE: https://github.com/svenroth-ai/shipwright/blob/main/shared/requirement-elicitation.md].
2. **The list test.** Would a list, table or paragraph serve better? The packet already asks this before drawing [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:89].
3. **The remove test on the outline.** No line that cannot go without losing a step the reader needs [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:37].
4. **The split.** Over the type's budget, split rather than shrink, and cut in the fixed order: decoration, duplicates, items that change no decision, cross-cutting items [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:162], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:170]. Offer an overview board plus a detail board rather than one dense board.
5. **The named omission.** Anything dropped is named with its reason, which the reply already has a line for [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/flow-templates.md:137].

**Wrong type.** The type table already answers this by asking which question the reader has; when two types fit, ask one question naming both [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:75]. When no drawable type answers the question, say so plainly and offer the nearest kind, or a table if none fits [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:95], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:101]. A request that names an undrawable kind, such as a journey or a mindmap, is challenged before the Brief is filled, because filling nine facts for an impossible board wastes the user's time.

**The sequencing rule.** Challenge the type first, then fill the Brief, then spar. A wrong type invalidates the facts: a state diagram's actors and a sequence's participants are different rows.

---

## 11. The Brief, energy levels, just-do-it and the kernel

### The Brief block

The Brief is a nine-row table in the working model, not a file and not a board node.

- **Not a file.** A clarification export may hold only the question, and Flow Mode writes no file at all [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:97], [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:85]. A Project cannot write one [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:234].
- **Not a board node.** A sticky or section added after the diagram landed needs its own yes, and would change the deliverable [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md:168].
- **Replayed every round.** Each round opens with a compact replay of the settled rows, so a later turn builds on them instead of re-asking. Public practice captures decisions inline and closes with a decisions table carrying a confidence per decision [SOURCE: https://raw.githubusercontent.com/microsoft/devsquad-copilot/main/.github/plugins/devsquad/skills/deep-clarification/SKILL.md].
- **Played back once, in full, before the model.** The confirmation states the nine rows, the assumed rows with their settlements, and the framing proposed. It waits for one answer. This is the playback step public practice requires before writing [SOURCE: https://github.com/svenroth-ai/shipwright/blob/main/shared/requirement-elicitation.md].
- **Carried into the gate.** The gate's existing facts gain one line: the Brief's question and outcome, so the yes covers the board's purpose as well as its destination.

### Energy levels

The ladder already exists; the intake should scale by it rather than invent a new one.

| Energy | Rounds | Sparring | Protected minimum |
|---|---|---|---|
| **Quick** (`$quick`, `$q`, "no questions", "just do it") | 0 questions | One message proposes all nine rows with defaults and asks for corrections | Reader, question and outcome are still proposed explicitly and confirmed once. Flow Mode already refuses to let Quick skip the gate, and the same reasoning protects the board's purpose [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:51] |
| **Standard** (default) | up to 3 | Outline plus two framings; sketch when the Brief is ambiguous | Full confidence rule |
| **Deep** | up to 5 | Outline, framings and sketch; alternatives always | Full confidence rule, plus the negative-space pass |
| **Raw / "skip depth"** | not available for Flow | not available | Raw skips the phase flow, which would skip the check and gate that Flow Mode protects [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:75] |

The round counts adapt `sk-prompt`'s energy ladder at human scale; its 10/3/0 counts internal passes, not questions [SOURCE: .skilled/skills/sk-prompt/SKILL.md:341].

### Just do it

"Just do it" is Quick energy with a proposal, not a silent guess. The path is:

1. Fill all nine rows from the sources and defaults.
2. Mark every inferred row `assumed` with what would settle it, or `corrected` if the user already stated it.
3. Send one message: the nine rows, the one-line framing, and "say nothing and I will draw this" — one confirmation, not a questionnaire.
4. On yes, run the check, rubric, gate and read-back unchanged.

This is `sk-prompt`'s non-interactive path, which proceeds on stated assumptions and flags each one rather than asking [SOURCE: .skilled/skills/sk-prompt/SKILL.md:340]. It is also the kernel's existing instruction to state the assumption and ask one comprehensive question rather than invent a parameter [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:57].

### The kernel

The Project cannot hold a state machine or write files, so it carries policy and points at the Knowledge that owns the mechanics.

- **Two sentences in the kernel.** The Flow row in the routing table says the intake runs before the type choice and stops at three rounds [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:126]. Flow Mode Delivery gains one sentence: before the gate, the Brief is replayed and confirmed once, and a Quick request gets one proposed Brief instead of rounds [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:254].
- **Two knowledge mirrors, hand-written.** "Templates - Flow Mode" already owns "intake", and "System - Interactive Mode" owns the one-question intake [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:207], [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:210]. Both mirror files are updated by hand from the skill sources, per the repo's manual parity method.
- **What the kernel must not gain.** A per-row table or a round counter. The Project cannot persist between turns, and a table in the kernel would drift from the skill.

---

## 12. Ranked changes

Ranked by how certain the gap is, how many FigJam requests the change touches, and the effort. Effort is small unless stated. Every change names the Product Owner file and the source it comes from.

### Rank 1. Add the nine-fact Brief with a status per row to Flow Mode

- **Changes:** `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md`, new Section 4A after Intake. Optionally one mirror paragraph in `AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md`.
- **Why:** Nothing today records what the board must know; the two dials decide how much and for whom, not what about [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:146]. The coverage guarantee supplies the contract [SOURCE: https://github.com/svenroth-ai/shipwright/blob/main/shared/requirement-elicitation.md].
- **Effort:** small; one table and four status definitions.
- **Preserves:** the type table, the dials, never-invent.

### Rank 2. Add the threshold, the stop rule and the energy-scaled round cap

- **Changes:** `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md` Section 2 workflow and its `$flow` energy line.
- **Why:** No stop rule exists anywhere in the packet, and Flow Mode's five asking situations are situational rather than confidence-driven [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:75]. The two stop rules are documented practice [SOURCE: https://raw.githubusercontent.com/microsoft/devsquad-copilot/main/.github/plugins/devsquad/skills/deep-clarification/SKILL.md].
- **Effort:** small; one threshold sentence, one ordered stop list, one table row per energy.
- **Preserves:** Quick's no-skip rule for the check and gate [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:51].

### Rank 3. Add the question bank with a recommended answer per question

- **Changes:** `AI Systems/Product Owner/sk-create-figjam/assets/flow-templates.md`, a new part after the type reply; `flow-mode.md` Section 4A points at it.
- **Why:** The type table is already question-shaped and unused as an interview [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:79]. Recommended answers are documented practice [SOURCE: https://raw.githubusercontent.com/microsoft/devsquad-copilot/main/.github/plugins/devsquad/skills/deep-clarification/SKILL.md].
- **Effort:** medium; three rounds of questions across nine rows, plus the probe set.
- **Preserves:** the query grammar and the type table wording.

### Rank 4. Add the sparring step: outline, two framings, sketch

- **Changes:** `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md` workflow steps 3 to 5; `references/quality-rubric.md` gains the outline pass.
- **Why:** The packet proposes only at the type level, and the remove test currently runs on a finished model [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:37]. The project-plan skill shows the preview-then-ask loop working [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:319], and Google's review guidance puts the problem before the solution [SOURCE: https://design.google/library/reviewing-the-design-review].
- **Effort:** medium; three artefacts and one question shape.
- **Preserves:** the check order, the gate, the no-hand-editing rule.

### Rank 5. Add the challenge rules for an over-broad brief and a wrong type

- **Changes:** `flow-mode.md` Sections 3 and 9; `references/quality-rubric.md` Section 2.
- **Why:** The nearest-type and split machinery exists but starts only after a type is named [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:95]. The negative-space pass is the missing first rung [SOURCE: https://github.com/svenroth-ai/shipwright/blob/main/shared/requirement-elicitation.md].
- **Effort:** small; an ordered ladder and a sequencing rule.
- **Preserves:** the nearest drawable type, the budgets and the split order.

### Rank 6. Add the Brief replay, the one confirmation, and the gate line

- **Changes:** `flow-mode.md` Section 8 and the `flow-templates.md` reply contract; `sk-product-owner/references/interactive-mode.md` gains one exception sentence for a board intake.
- **Why:** Playback before action is the practice, and the current gate confirms the destination only [SOURCE: https://github.com/svenroth-ai/shipwright/blob/main/shared/requirement-elicitation.md], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:65]. Interactive Mode's second-round ban needs one named exception [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:519].
- **Effort:** small; the exception is the only cross-packet edit.
- **Preserves:** the one-question rule for artifact ambiguity and the five-line Flow reply.

### Rank 7. Add the just-do-it and Quick rules to the protected-facts list

- **Changes:** `sk-product-owner/references/interactive-mode.md` protected list; `flow-mode.md` energy line; one kernel sentence.
- **Why:** Quick may skip routine intake and the protected facts are Doc-shaped [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:109]. `sk-prompt` shows the never-ask-with-flagged-assumptions path [SOURCE: .skilled/skills/sk-prompt/SKILL.md:340].
- **Effort:** small.
- **Preserves:** Quick's freedom to skip questions, and Flow Mode's refusal to skip the gate.

### Rank 8. Add the test carve-out and four scenarios

- **Changes:** `sk-create-figjam/manual-testing-playbook/boundaries/command-conflict-asks.md` pass condition; new scenarios under `boundaries/` for a thin brief, an over-broad brief, a wrong type and just-do-it.
- **Why:** The current scenario fails any run that asks twice [SOURCE: AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/boundaries/command-conflict-asks.md:29], and no scenario covers an under-specified brief.
- **Effort:** medium; four scenario files in the existing pattern.
- **Preserves:** FJ-020's artifact-conflict test unchanged in substance.

### Rank 9. Name the intake in the packet contract and the hub pointer

- **Changes:** `sk-create-figjam/SKILL.md` ALWAYS rule 5; `ROUTER.md` FLOW row.
- **Why:** A rule that lives only in a reference is easy to skip; the packet's ALWAYS list is where a reader learns the order [SOURCE: AI Systems/Product Owner/sk-create-figjam/SKILL.md:168], [SOURCE: AI Systems/Product Owner/sk-create-figjam/SKILL.md:169]. The FLOW leaf pair is what a Flow request loads [SOURCE: AI Systems/Product Owner/ROUTER.md:91].
- **Effort:** small.
- **Preserves:** the routing contract and the leaf map.

---

## Eliminated Alternatives

| Alternative | Why eliminated | Evidence |
|---|---|---|
| Let Figma's one-question doctrine stand as the ceiling | It is already the packet's doctrine and leaves a thin brief undetected; the loop must exceed upstream | [SOURCE: research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:69], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:144] |
| A numeric confidence score out of 100 | No authoritative calibration exists, and public practice states completeness, not probability; a fabricated number would violate the honesty rules | [SOURCE: https://github.com/svenroth-ai/shipwright/blob/main/shared/requirement-elicitation.md] |
| One question at a time, strictly | It contradicts Figma's batched practice and would cost a user nine messages for nine facts; dependency order resolves the conflict | [SOURCE: https://raw.githubusercontent.com/microsoft/devsquad-copilot/main/.github/plugins/devsquad/skills/deep-clarification/SKILL.md], [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:276] |
| Put the intake in Interactive Mode | A Flow request never loads that reference, so the loop would not run | [SOURCE: AI Systems/Product Owner/ROUTER.md:37] |
| Reuse the clarification export as the record | It may hold the question only, and a Project cannot write it | [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:97] |
| Store the Brief on the board as a sticky | It needs its own yes and changes the deliverable | [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md:168] |
| Map "just do it" to Raw energy | Raw skips the phase flow, including the check and gate Flow Mode protects | [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:75], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:51] |
| A new packet or Knowledge file for the intake | Doubles the parity surface; Flow Mode already owns intake in the kernel's table | [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:207] |
| A brief-completeness rule in `flow_check.py` | The check reads Mermaid and the Brief precedes the model | [SOURCE: AI Systems/Product Owner/sk-create-figjam/SKILL.md:170] |
| A 15-question budget as the cap | Counts questions, not rounds, and a round may carry three | [SOURCE: https://raw.githubusercontent.com/microsoft/devsquad-copilot/main/.github/plugins/devsquad/skills/deep-clarification/SKILL.md] |

---

## Divergence Map

No divergent pivot ran; convergence mode was off and the stop policy was `max-iterations`. The breadth record is the five focus angles, each deliberately different.

- **Completed pivots:** 0.
- **Failed pivots:** 0.
- **Audited overrides:** 0.
- **Saturated directions:** none recorded; every iteration widened the source set (packet, corpus, public practice, sibling skill, kernel and routing).
- **Remaining frontier:** what a live board intake would show. Whether users accept a three-round cap, whether a proposed Brief is corrected more often than accepted, and whether the outline catches over-broad briefs before modelling are all empirical and unmeasured here.
- **What breadth does not claim:** the synthesis does not claim the topic converged. It claims the design is specified and its sources are exhausted for a paper pass.

---

## 12. Open Questions

1. **Do users accept a three-round cap for a Standard board?** The number is chosen, not measured. It fits `sk-prompt`'s ladder at a lower scale, but no board-intake user has tried it.
2. **Will the outline actually catch over-broad briefs?** The remove test is specified for a model; applying it to a text outline is sound but untested on a real brief.
3. **Does a Project user read a replayed Brief, or skim it?** The kernel replay is a paragraph, and no user test exists.
4. **Should Quick ever ask a question?** This design says no: it proposes and asks once for corrections. If a Quick user routinely corrects the reader or the question, Quick should ask those two.
5. **How does the loop interact with an artifact pair?** The pair's first reply ends at the Flow gate [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:256]. Whether the intake rounds happen before or after the artifact is delivered is a sequencing decision this lineage did not test; the safer reading is after, because the artifact is the board's source.

### Claims not verified

- Whether a generated board's reader would agree the Brief captures what they needed. No user test ran.
- Whether the kernel's Knowledge mirrors can carry the Brief table without drifting; the parity method is manual and no mirror was edited here.
- Whether a state diagram's "actors" row is meaningful, or should read "owner of each transition"; the per-type needs table does not settle it [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:138].
- The exact Figma-side cost of a sketch, since the sketch is chat-only and no tool call is made; this is design intent, not measured.

---

## Convergence Report

- Stop reason: maxIterationsReached
- Total iterations: 5
- Questions answered: 5 / 5
- Remaining questions: 0
- Last 3 iteration summaries: run 3: public elicitation and critique (0.75); run 4: answer persistence, energy and just-do-it (0.6); run 5: challenge rules, kernel and tests (0.55)
- Convergence threshold: 0.05, convergence mode off; the ratio trend is telemetry only
- Divergence summary: no divergent pivots recorded

---

## Sources

### Product Owner sources read

- `AI Systems/Product Owner/sk-product-owner/SKILL.md`
- `AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md`
- `AI Systems/Product Owner/sk-product-owner/references/routing.md`
- `AI Systems/Product Owner/sk-product-owner/assets/interactive-response-templates.md`
- `AI Systems/Product Owner/sk-create-figjam/SKILL.md`
- `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md`
- `AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md`
- `AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md`
- `AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md`
- `AI Systems/Product Owner/sk-create-figjam/assets/flow-templates.md`
- `AI Systems/Product Owner/sk-create-figjam/scripts/flow_check.py`
- `AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/boundaries/command-conflict-asks.md`
- `AI Systems/Product Owner/SKILL.md` and `ROUTER.md`
- `AI Systems/Product Owner/AGENTS.md`
- `AI Systems/Product Owner/claude project/Custom Instructions.md`
- `.skilled/skills/sk-prompt/SKILL.md`

### Corpus, read directly

- `research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md`
- `research/corpus/figma__mcp-server-guide/skills/figma-spec/SKILL.md`
- `research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md`
- `research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/SKILL.md`
- `research/corpus/ompug__diagram-codebase/docs/DESIGN.md`
- `research/corpus/prasantloki__figjam-builder/SKILL.md`

### Public sources

- https://github.com/svenroth-ai/shipwright/blob/main/shared/requirement-elicitation.md
- https://raw.githubusercontent.com/microsoft/devsquad-copilot/main/.github/plugins/devsquad/skills/deep-clarification/SKILL.md
- https://design.google/library/reviewing-the-design-review
- https://thecrit.co/resources/design-critique-questions
- https://pages.graphics.cs.wisc.edu/VisSnacks/tutorials/4-critique/
- https://assets.ctfassets.net/bncv3c2gt878/4mvcQWNWhWQ0sgiKWCakEU/cce06a8bdc4d3e274ca47eb72d60fbe0/Gause_-_Context-Free_Questions.pdf (unreadable; not used as evidence)

### Lineage inputs

- `research/lineages/deepseek/iterations/iteration-001.md` to `iteration-005.md`
- `research/lineages/deepseek/deltas/iter-001.jsonl` to `iter-005.jsonl`
- `research/lineages/deepseek/findings-registry.json`
- `research/lineages/deepseek/resource-map.md`
- `AI Systems/Product Owner/specs/017-figjam-flow-generation/009-figjam-skill-research/research/research.md` and `.../016-figjam-improvement-research/research/research.md` (read first; their changes are treated as implemented)
