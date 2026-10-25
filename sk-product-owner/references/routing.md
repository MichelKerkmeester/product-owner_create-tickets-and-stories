---
title: "Product Owner - Routing"
description: "Phase detection, confidence thresholds, semantic topics and Story shape resolution for the Product Owner packet router."
trigger_phrases:
  - "product owner routing"
  - "semantic topics"
  - "confidence thresholds"
  - "story shape resolution"
importance_tier: important
contextType: general
version: 1.0.0.0
---

# Product Owner - Routing

The routing detail behind Section 2 of [`../SKILL.md`](../SKILL.md). Section 2 holds the command map and the resource loading levels, and this file holds the steps, the thresholds, the topic table and the Story shape rules a request passes through before it loads anything. [`router-contract.md`](router-contract.md) runs the same router as Python.

**Loading Condition:** ON-DEMAND
**Purpose:** Gives the routing steps, confidence thresholds, semantic topics and Story shape rules behind Section 2 of `../SKILL.md`
**Scope:** Phase detection, confidence bands, the semantic topic table and Story shape resolution
**Output Path:** None. It decides which resources load and writes no artifact
**Loads With:** nothing. It is read alone when a routing decision needs more than Section 2
**Routed By:** a reader who needs the routing detail, and `../../benchmark/router/differential.py`, which checks its topic table against the oracle
**Hands Off To:** `router-contract.md` for the exact algorithm

---

## 1. ROUTING STEPS

1. Normalize case. Resolve energy using the signal contract in `interactive-mode.md` Section 2, then detect artifact commands independently.
2. Detect `$task --subtask` before the bare `$task` command.
3. Collect every exact artifact command instead of stopping at the first match. More than one collected command is a conflict routed to one consolidated question. The Story and Epic commands both route to Story Mode, so they never conflict with each other: they only select the shape, and the shape selects the one scaffold that loads. Story-with-tasks and the `$story $task` conflict follow the contract in `story-mode.md` Section 7.
4. With exactly one command, it wins over any natural-language wording.
5. With no command, detect artifact framing ("write a task/bug/PRD/doc ...", "make a FigJam flow ..."). Framing beats subject nouns and semantic scores, and competing artifact framings conflict. FigJam beside another artifact is its subject unless an output verb requests a board. Paired output emits `then: "FLOW"` with the artifact first. Handoff, board gate, read-back and link placement follow `../sk-create-figjam/references/flow-mode.md` Section 8. A request to add notes to or update a FigJam board, including one that carries a figma.com/board link, is Flow, and the bare word "figma" is never Flow framing.
6. Apply the UI-refinement Task override only after commands and framing are checked: UI feedback and polish route to Task Mode even when "fix" or "broken" co-occurs with feedback language, because Bug Mode is reserved for unexpected system behavior. Grouped bugs, consolidation tickets and bug-fix tasks follow the Bug-to-Task contract in `bug-mode.md` Section 1.
7. With no command or framing, score semantic topics and route by confidence threshold.
8. Route every Doc selection through the source-authority and conflict gate before drafting, including under Quick energy.
9. Load only the resources the selected intent needs, and on the Story lane only the scaffold the resolved shape needs.

---

## 2. SCORING

### Confidence Thresholds

- HIGH `>= 0.85`: route directly, no clarification
- MEDIUM `>= 0.60`: route with a concise confirmation of the detected mode
- LOW `>= 0.40`: suggest the detected mode and clarify through Interactive Mode
- FALLBACK `< 0.40`: enter Interactive Mode with one comprehensive question. Quick uses the narrow Task fallback below this floor

Documentation and Story synonyms carry a 0.85 confidence override, so a genuine hit routes directly or through the Doc gate rather than falling into the LOW or FALLBACK bands.

### Semantic Topics

Step 7 scores these nine topics. Each word-boundary hit adds 0.25 up to a 0.95 ceiling, a topic carrying an override routes on a single hit, and table order breaks a tie. The vocabulary below is the trigger set a reader can apply directly, not the full synonym list, and `references/router-contract.md` carries every synonym with the exact regexes, the scoring arithmetic and the phrase-gap rules.

| Topic | Route | Trigger vocabulary | Override |
| --- | --- | --- | --- |
| bug | Bug | `bug`, `fix`, `issue`, `defect`, `error`, `broken`, `crash`, `failing`, `repro` | none |
| feature | Task | `capability`, `enhancement`, `functionality`, `new`, `add` | none |
| acceptance | Task | `criteria`, `definition of done`, `validation`, `success condition` | none |
| user_need | Task | `user need`, `persona`, `journey`, `workflow`, `as a user` | none |
| technical_task | Task | `refactor`, `optimize`, `debt`, `cleanup`, `update dependency` | none |
| integration | Task | `api`, `connect`, `sync`, `webhook`, `third-party` | none |
| ui_refinement | Task | `polish`, `tidy up`, `clean up`, `spacing`, `alignment`, `wording`, `label`, `consistent`, `inconsistent`, `casing`, `figma`, `visual QA` | 0.80 |
| documentation | Doc | `document how`, `write a guide`, `api reference`, `runbook`, `architecture document`, `technical proposal`, `decision record` | 0.85 |
| story | Story | `prd`, `user story`, `story`, `epic`, `acceptance scenarios`, `given when then`, `connextra`, `draft for pm`, `changing how` | 0.85 |

Three request shapes never name an artifact and never score well here, so they are caught one step earlier as framing: symptom wording with no defect noun ("freezes", "hangs", "shows a broken image", "returns a 500") routes to Bug, a role denied a capability ("brands cant filter by engagement rate") routes to Story, and initiative-scale wording ("the whole creator verification programme") routes to Story with the Epic shape.

---

## 3. SHAPES AND CONTRACT

### Shape Resolution (Story Mode)

The Story lane resolves one shape, Story or Epic, before any file loads, then loads only that shape's scaffold.

- Command wins first: `$story`/`$s`/`$prd`/`$p` select the Story shape, `$epic`/`$e` select the Epic shape
- With no command, framing wins, read most specific first: "write an epic", "epic for" and "refine this epic" select Epic, and "write a PRD", "user story", "story for", "turn this into a story" and draft wording ("draft for PM") select Story
- With no command and no framing match, the shape defaults to Story, since a semantic topic score names the lane rather than the shape

### Executable Contract

[`references/router-contract.md`](router-contract.md) carries this router as running Python, the exact algorithm `../../benchmark/router/route_contract.py` is checked against: the full token and phrase regexes, the semantic topic tables and scoring, and the shape-precedence patterns above. It is ON_DEMAND, read only when a request needs the precise implementation rather than the rule. Its `discover_markdown_resources` builds the resource inventory, and an unmatched request gets `UNKNOWN_FALLBACK_CHECKLIST` with its one question. Every Doc route also runs a source-authority gate there: `PENDING` before context is evaluated, `BLOCKED` on a missing field, an unresolved conflict or a claim subject no source covers, `READY` once every check clears.

### Mode Selection Notes

Task Mode covers features, acceptance criteria, technical tasks, integrations and UI refinement. Doc Mode has five adaptive shapes: Guide, Catalog, Behavior reference, Proposal and Narrative overview. Story and Epic are artifact kinds, not size tiers. Flow Mode draws a diagram of one of seven types on a FigJam board and lives in the `sk-create-figjam` packet. Flow handling, including a Flow request that reaches the default packet, follows the handoff contract in `../SKILL.md` Section 2. Interactive Mode handles ambiguity, conflicting commands and missing contract fields. Quick narrows the selected artifact and never bypasses a command conflict or a Doc gate.
