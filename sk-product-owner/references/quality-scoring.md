---
title: "Product Owner - Rules - Quality Scoring - v0.101"
description: "The six-dimension quality rubric behind the blocking floors in SKILL.md Section 6: what each dimension measures, the test that separates a floor-clearing score from a near miss, the three bands, how each dimension reads against Task, Bug, Doc, Story and Epic, how the two always-loaded layers meet the floors, and the revision ladder a failing score follows."
version: "0.101"
contextType: reference
importance_tier: critical
trigger_phrases:
  - "quality scoring"
  - "six-dimension quality gates"
  - "how do I score an 8"
  - "quality floor"
  - "revision cycle"
  - "scoring bands"
---

# Product Owner - Rules - Quality Scoring - v0.101

The rubric behind the six blocking floors. Each dimension states what it measures, the one test that separates a clear pass from a near miss, and how it reads against each artifact shape the system now produces.

**Loading Condition:** ON-DEMAND
**Purpose:** Provides the scoring definitions, bands, per-shape readings and revision ladder behind the six blocking floors that `SKILL.md` Section 6 states, for a scorer who needs to settle a borderline dimension or name what a revision cycle must fix
**Scope:** The six dimensions and their measures, the pass-versus-near-miss test per dimension, the three scoring bands, the per-shape reading across Task, Bug, Doc, Story and Epic, the relationship between the floors and the two always-loaded layers, the revision ladder and the return target per dimension
**Output Path:** None. This file scores an artifact another file writes, and produces none of its own
**Loads With:** nothing. The six floors and their pass-versus-near-miss tests sit inline in `SKILL.md` Section 6, so a delivery scores without this file, and this file is opened when a dimension sits on its boundary or a revision cycle needs a named target
**Routed By:** nothing automatic. The Test phase opens it when a score is borderline, when a shape's reading is in doubt, or when a revision cycle needs to name the phase that owns the weak dimension
**Hands Off To:** nothing. A failing dimension returns to the phase named for it in section 6, and `references/conciseness.md` owns the reconstruction test that section 5 borrows for Relevance

---

## 1. OVERVIEW

### Purpose

Six dimensions on a ten-point scale, scored against every deliverable before export. Five carry a floor of 8. Accuracy carries 9.

A floor is blocking, not advisory. A dimension under its floor stops the export and names the work, which is why every dimension below carries a test a scorer can actually run rather than an adjective to agree with.

### What a score is not

The score is internal. Two-layer transparency puts a plain quality summary in the chat response and never a Quality Score header inside the artifact, exactly as a Mode, Template, Perspectives or Energy header never enters one. For a Doc refinement the fidelity invariant makes that absolute, since injecting scoring metadata into preserved source structure is itself a fidelity break.

Scoring is also not a substitute for the hard blockers. A Human Voice blocker is binary and blocking on its own, so it never trades against a dimension that scored well.

---

## 2. THE SIX DIMENSIONS

Each entry names its floor, what it measures, and the test that separates a floor-clearing score from a near miss. The near miss is written at 6, one band below, because that is the score a competent draft lands on when a dimension is nearly right. Accuracy is written at 7, since its bands sit one point higher.

**Completeness, floor 8.** Measures whether every section the resolved shape requires is present and populated from supplied material, with dependencies, edge cases, error states, empty states, loading states and permission boundaries named wherever they bear on acceptance.

At 6 every required section exists and at least one carries a placeholder, a restated heading, or a single generic line where the shape expects substance. At 8 an implementer could work from it without asking which section was skipped. The test: name the section a reader would have to ask you about. Naming one puts the score at 6.

**Clarity, floor 8.** Measures whether each requirement and each acceptance criterion resolves to exactly one reading.

At 6 a sentence is understandable and two competent implementers would still build different things from it, usually because a quantity, a boundary, a subject or a state was left to the reader. At 8 the disagreement has nowhere to live. The test: hunt for one sentence two implementers could split on. Finding one puts the score at 6.

**Actionability, floor 8.** Measures whether the artifact states observable end states rather than intentions, in an order a reader can follow.

At 6 the work is described and the success condition restates the work, as in a criterion whose end state is that the filter works. At 8 every criterion names something a tester can observe without asking what counts as done. The test: read each criterion and answer what a tester would see. Any criterion that answers "the feature is built" puts the score at 6.

**Accuracy, floor 9.** Measures whether every claim traces to supplied material or carries its real status label: current behavior, approved direction, proposal, retired or unknown.

The floor sits a point above the rest because an invented fact reads exactly as confidently as a verified one and costs more downstream than any other defect in this list. At 7 the artifact is broadly right and carries at least one claim nobody supplied, most often a plausible platform detail, a root cause, or an approval that was never given. At 9 every claim either traces to a supplied line or wears its status. The test: take the three most specific claims and name the supplied line each rests on. A claim with no line puts the score at 7 whatever the other five dimensions reach.

**Relevance, floor 8.** Measures whether the artifact answers the request that was made and nothing adjacent to it.

At 6 the content is correct and some of it was never asked for, usually a section the shape permits and the request did not need. At 8 every section earns its place from the request or from the shape. The test: apply the reconstruction test in `references/conciseness.md` section by section. More than one section a reader could rebuild from what remains puts the score at 6.

**Mechanism Depth, floor 8.** Measures whether a reader learns why the change exists before what it does, deeply enough to derive a case the artifact never lists.

At 6 a Problem or rationale line exists and restates the solution in the past tense, so the reader derives nothing that was not already listed. At 8 the stated principle predicts the answer to an unlisted case. The test: invent one edge case the artifact does not mention and ask whether the stated WHY settles it. A WHY that does not settle it puts the score at 6.

---

## 3. THE THREE BANDS

Five dimensions share one band set. Accuracy shifts its boundaries up by one point, which is the only arithmetic difference the higher floor introduces.

| Band | Completeness, Clarity, Actionability, Relevance, Mechanism Depth | Accuracy |
| --- | --- | --- |
| Below the near miss | 0-4: required content absent, not merely thin | 0-5: a claim contradicts a supplied source, or an infeasible requirement stands |
| Near miss | 5-7: present and one named defect from section 2 stands | 6-8: broadly correct with an unsupplied claim standing |
| Clears the floor | 8-10: the section 2 test finds nothing | 9-10: every claim traces to a line or wears its status |

A 10 is not a target. It records that the test found nothing on a deliberate second pass, and chasing one past 8 spends effort the artifact does not return.

---

## 4. READING THE DIMENSIONS PER SHAPE

The artifact set is Task, Bug, Doc, and Story Mode's two shapes. A shape changes which dimension decides the delivery and can change what a dimension is even allowed to measure. Scoring a shape against another shape's contract is a rubric error, not a finding.

**Task.** Actionability decides it. Requirements are QA-checkable outcomes, so a checklist item with no observable end state is the standard 6. Mechanism Depth is satisfied by a user-value line rather than by implementation reasoning, since a task that explains HOW has drifted out of Product Owner scope and loses Relevance for it.

**Bug.** Accuracy decides it. An observed behavior, a reproduction step or a root cause that no evidence supports is the standard 7, and `Not provided` is the correct entry where an inference would otherwise go. Completeness is scored against the evidence supplied and never against a complete investigation, so a faithful report of thin evidence still reaches 8.

**Doc.** Accuracy and Relevance decide it, and the source-authority gate feeds Accuracy directly: a claim whose subject no supplied source covers scores 7 even when the ClickUp divider, heading and bullet contract is spotless. For a refinement, Completeness is scored on the requested change plus preserved fidelity, never on gaps the source already carried, because a refinement that fixes what the request did not name has failed Relevance rather than earned Completeness.

**Story.** Clarity and Mechanism Depth decide it. Acceptance criteria are where Clarity is settled, and the Problem inside the About umbrella is where Mechanism Depth is settled. Requirements hold hard constraints only, so adding build steps or an outcome to one costs Relevance and buys no Actionability, and a criterion that prescribes the mechanism costs Clarity because it is no longer testable as an outcome. Three supplied-value failures score here rather than reading as style. A hard value the source supplied and the draft generalised into a description of itself, `32px` written as updated spacing, is an Accuracy failure at 7, because the artifact now states something the source did not: that the change is unspecified. A Requirements section that drops values the source supplied is a Completeness failure at 6, and the section a reader would have to ask about is the one holding the values. A value carried into an acceptance criterion instead costs Clarity, since the criterion is no longer testable as an outcome. A Requirements item that reports what a screen says, shows or contains, naming no value, limit, condition, effect or named flow, is a Relevance failure at 6, and it is scored per item rather than per section, because four such items sitting beside twelve real constraints leave the section as a whole still earning its place and the section-level reconstruction test scores it a pass.

**Epic.** Completeness reads against the Epic shape, which carries a Goal and a Scope of child stories and no requirements of its own. Scoring an Epic down for absent requirements is a rubric error. Actionability lives in the release-level acceptance criteria and in whether each child story named in Scope is separable enough to hand to someone. The same holds for Delivery. An absent `## Delivery` section is not a Completeness miss in either shape when nobody asked for one and no open question or undated external constraint forced one, exactly as an absent Requirements section is not one when the story carries no hard constraint. Scoring down a section the shape made optional is a rubric error. A Delivery section whose every slot is still `TBD...` is the opposite finding, and it costs Relevance.

---

The kernel points here for the six-dimension gate and its shape reading:

Apply the phase flow at the detected energy level and validate before delivery.

| Dimension       | Floor | Focus                                                                                                                                                        |
| -----------------| -------| --------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Completeness    | 8+    | Enough product or engineering context, scope, value, behavior and supporting detail for the artifact's audience.                                             |
| Clarity         | 8+    | Unambiguous language and a usable routed or preserved structure.                                                                                             |
| Actionability   | 8+    | Testable requirements or usable product or engineering guidance, with proposals and recommendations labelled rather than presented as current implementation. |
| Accuracy        | 9+    | Source facts, statuses, identifiers and literal material remain accurate, and unsupported claims are absent.                                                     |
| Relevance       | 8+    | Content stays inside the request and Product Owner boundary.                                                                                                 |
| Mechanism Depth | 8+    | The WHY, impact, outcome, behavior, constraints and source-backed technical HOW are sufficiently visible for the audience.                                   |

Read the dimensions against the resolved shape. Scoring one shape against another shape's contract is a rubric error rather than a finding.

- **Task:** Actionability decides it. A checklist item with no observable end state fails, and Mechanism Depth is satisfied by a user-value line rather than by implementation reasoning
- **Bug:** Accuracy decides it. An observed behavior, reproduction step or root cause that no evidence supports fails, `Not provided` is the correct entry where an inference would otherwise go, and Completeness is scored against the evidence supplied rather than against a complete investigation
- **Doc:** Accuracy and Relevance decide it, and the source-authority gate feeds Accuracy directly, so a claim whose subject no supplied source covers fails even when the ClickUp layout is spotless. For a refinement, Completeness is scored on the requested change plus preserved fidelity, never on gaps the source already carried

## 5. THE FLOORS AND THE TWO ALWAYS-LOADED LAYERS

Two layers load on every request and neither is a scored dimension. Knowing where each stops is what keeps the floors from double-counting them or, worse, trading against them.

`references/hvr-core.md` governs word choice. Its hard blockers are counted in the `HVR self-scan` line and are binary: a blocker blocks on its own and no dimension score buys it off. Nothing in this rubric raises or lowers that count.

`references/conciseness.md` governs quantity, structure and load-bearing-ness. Its cuts and keeps are edits rather than scored penalties, and they never enter the self-scan count either.

Where the layers meet the floors, two rules settle it. The reconstruction test is the operational test for Relevance, borrowed rather than restated, so Relevance and the cut rules cannot disagree. Over-compression is a Clarity failure and never a Relevance win: cutting a semantic connective, a scope qualifier, a caveat, a number, or the one example that makes a rule usable raises nothing and lowers Clarity. Relevance read alone rewards cutting without limit, and Clarity is the counterweight that stops it.

---

The kernel points here for these gate behaviours:

If any floor fails, revise before delivering. Keep assumption analysis internal. Never output `[Assumes: ...]` tags. After three improvement cycles, deliver the best version with a clear quality note. Quick reports the gate as checked instead of presenting a long rationale, but it still must satisfy scope, routed template or refinement fidelity, HVR and factual safety.

The kernel points here for the pre-reply quality checklist:

- Artifact intent is Task, Bug, Doc, Story or valid Interactive intake. Energy is tracked separately
- Exact commands, natural framing and tie-break rules resolve consistently, and conflicting commands or framing produced one consolidated question, not a draft
- User value, audience and outcome are clear or safely clarified
- Project Knowledge consultation matches the routed path and stays inside the smallest safe set
- A new artifact follows the active template, and a refinement preserves the supplied structure
- Doc claims retain source classification and unresolved conflicts have blocked drafting
- Backlog content stays WHAT/WHY focused, and documentation may include source-backed technical HOW and clearly labelled technical proposals or recommendations
- Identifiers, links, tables, literal copy and lifecycle labels remain faithful where supplied
- No fabricated current requirements, evidence, root causes, platform details, implementation facts, approvals or sign-off appear
- New Docs and PRDs follow the ClickUp divider/`*   ` bullet contract and the Barter house format respectively, and refinements preserve source formatting unless normalization was requested
- Every new Doc heading is sentence case, and every PRD H2 section closes with a `* * *` directly above its `##   ` spacer
- The Doc gate blocked when a requested claim's subject was absent from the supplied sources, not only when a contract field was missing
- A PRD names its artifact kind (Story or Epic), keeps requirements to hard constraints free of build steps and carries every supplied hard value verbatim, references no screenshot or image path, carries a Delivery section only where it was requested or forced, and carries no ticket header fields, story points or INVEST notes
- HVR has no hard blockers, and the self-scan line reports the real count
- Six-dimension floors pass. Quick narrows the artifact, never the floors, so a Quick delivery reports the same gate as checked
- The Deliverable Block appears before commentary and is the only claimed delivery evidence
- Response gives the correct export-equivalent path, quality status and summary only, adding one ClickUp delivery offer when ClickUp tooling is connected
- No write happened to ClickUp or another external system without explicit approval in this conversation

## 6. THE REVISION LADDER

Count the dimensions under their floors, then act on the count rather than on the worst single score.

| Dimensions under floor | Status | Action |
| --- | --- | --- |
| None | PASS | Proceed to Harmonize and export |
| Exactly one | REVISION NEEDED | Fix that dimension at the phase named below and re-score |
| Two or more | REJECTED | Return to Engineer and rebuild the shape rather than patching lines |

A single failure is a repair. Two or more say the shape was wrong before the wording was, and patching sentences on a wrong shape produces an artifact that scores well and answers the wrong request.

Each dimension returns to the phase that owns it. Completeness and Relevance return to Discover, because both are decided by what was gathered and scoped. Actionability and Accuracy return to Engineer, where end states and feasibility are set. Clarity and Mechanism Depth return to Prototype, where the words are chosen.

Three cycles is the ceiling. After the third, deliver the best version with a plain one-line note naming the dimension still short and why, and never open a fourth. The note goes in the chat response, alongside the export path and the self-scan line, never into the artifact.
---

The kernel points here for these delivery prohibitions:

7. Never skip mechanism explanations, user-value justification, or edge cases that affect acceptance.
8. Never show full methodology transcripts or overwhelm the user with internal processing detail.
9. Never skip the Deliverable Block, template compliance or quality scoring. Never claim a deliverable exists without rendering it.
