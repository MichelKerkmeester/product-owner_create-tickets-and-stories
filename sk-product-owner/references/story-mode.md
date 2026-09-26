---
title: "Product Owner - Templates - Story Mode - v0.404"
description: "Workflow, shared house grammar, artifact-kind selection (Story or Epic), the optional-enrichment catalog, refinement fidelity and delivery standards for creating and refining Barter house-format artifacts: Stories (story preamble, an About umbrella with Problem, Solution, Expected outcomes and References, an optional Requirements section holding only hard constraints, a few outcome-led Given/When/Then acceptance criteria, and an opt-in Delivery close produced only on request or where the artifact forces it) and Epics (About with Problem, Goal and Solution, a Scope of child stories, release-level acceptance criteria, the same opt-in Delivery close, and no Requirements). Each shape carries its own scaffold in assets, and this file is the single authority for everything the shapes share."
version: "0.404"
contextType: reference
importance_tier: high
trigger_phrases:
  - "Story mode"
  - "write a user story"
  - "write an epic"
  - "PRD with acceptance criteria"
  - "story vs epic"
  - "refine this PRD"
---

# Product Owner - Templates - Story Mode - v0.404

Story-mode guidance for the two Barter house-format artifact kinds: **Stories** and **Epics**. A Story covers one feature area with a few outcome-led acceptance criteria and, where the delivery has hard constraints, a Requirements section that holds only those. An Epic frames an initiative split across child stories, with a Goal, a Scope and release-level acceptance criteria, and no requirements of its own. Both stay prose-first, share the same ClickUp grammar and the same opt-in `## Delivery` close, and reach for heavier machinery (a User Story promise block, per-requirement value lines, exact Rule blocks, Definition of Ready/Done gates) only as optional enrichment.

Each shape carries its own scaffold and nothing else: [story-template.md](../assets/story-template.md) and [epic-template.md](../assets/epic-template.md). Everything the shapes share lives here, so a rule has one authority rather than two copies that drift apart.

**Loading Condition:** ON-DEMAND
**Purpose:** Provides the workflow, shared grammar, artifact-kind selection and delivery standards for `$story`, `$s`, `$prd`, `$p`, `$epic`, `$e` and clear natural-language Story or Epic requests
**Scope:** New Stories and Epics, and source-safe refinement of existing ones
**Output Path:** `export/[###] - Story-[description].md` for a new Story, `export/[###] - Epic-[description].md` for a new Epic, or `export/[original-source-filename].md` for a refinement
**Loads With:** the one scaffold the resolved shape names and never more than one, `assets/story-template.md` or `assets/epic-template.md`, beside the always-loaded `references/hvr-core.md` and `references/conciseness.md`
**Routed By:** `$story`, `$s`, `$prd`, `$p` for the Story shape, `$epic`, `$e` for the Epic shape, Story-lane framing read most specific first, a role denied a capability, initiative-scale wording, and the prd semantic topic on its 0.85 override
**Hands Off To:** `references/interactive-mode.md` when the role, user value, requirement shape or artifact kind cannot be inferred safely, which returns here once the user answers

---

## 1. OVERVIEW

### Purpose

Story Mode turns an outcome and its requirements into a narrative artifact in the Barter house format. It stays prose-first. The `## About` umbrella opens the artifact before any structured detail, with scope and value in prose, then `### Problem` and `### Solution`. The conventional elements it carries (numbered outcome-led acceptance criteria, and for a Story its hard requirements) sharpen the narrative. They never replace it.

### When to Use

Use Story Mode for:

- A new **Story** covering one feature area with one or more requirements that become implementation tasks
- A new **Epic** framing an initiative split across child stories, with a Goal and a Scope
- Converting product notes, briefs or a parent epic into a Story or Epic with acceptance criteria
- A targeted refinement of an existing Story or Epic: adding requirements, acceptance criteria, scope items or gates without restructuring it
- A natural-language request such as "write a user story for X", "turn this into a PRD", "write an epic for X" or "make a draft for X"

Use another mode when the requested artifact is different:

- A single implementation unit is Task Mode
- A defect with evidence and reproduction steps is Bug Mode
- Knowledge documentation (guides, catalogs, behavior references, proposals) is Doc Mode
- "Create a task from this PRD" is Task Mode using the PRD as source context

Research and feasibility spikes: work whose deliverable is a decision rather than shipped behavior is usually Task Mode, or Doc Mode when the deliverable is a written recommendation. When the team prefers to keep a spike on the Story surface, write it as a Story with acceptance criteria that assert the documented decision.

### Commands

- **Story commands:** `$story` (primary) and `$s` (short alias). `$prd` and `$p` are kept back-compat aliases for the same Story intent, because existing prompts and habits use them
- **Epic commands:** `$epic` (primary), `$e` (short alias) select Story Mode with the Epic shape
- **Energy override:** `$quick` or `$q` may accompany any of these
- **Output:** One markdown artifact in the Barter house format
- **Thinking:** Rigor scales with the selected energy
- **Interactive behavior:** With no command, ask one consolidated question only when role, value, requirement shape or artifact kind cannot be established safely. An explicit command routes the request and does not stand in for the direction, so `$story`, `$s`, `$prd`, `$p`, `$epic` and `$e` still ask their context-specific question and wait. Only `$quick` or `$q` may skip routine intake
- Stopping to ask still produces a file. Export the question in this mode's lane as `export/[###] - {artifact}-[description]-clarification.md`, holding the question and nothing else, so the request is not lost between sessions

Command recognition belongs to the Product Owner router. `$story`, `$s`, `$prd`, `$p`, `$epic` and `$e` are exact, standalone tokens. Strings such as `$stories`, `$prds`, `$epics`, `$sort`, `$email`, `$e.md`, or text that merely contains `$s` or `$e` are not Story Mode commands.

### Core Rules

The house grammar every Story and Epic follows sits in section 3. These are the mode-level rules on top of it:

- An Epic drafted before its child stories exist names each intended child story in `## Scope` as plain text. Never invent a link to make a Scope bullet look finished
- A requirement that is agreed in outcome but undecided in one part carries an `**Open:**` line under its name, so a developer reading Requirements and Acceptance criteria alone can see it. The same question is repeated in Rabbit holes, which is why an `**Open:**` line opts the `## Delivery` section in even when nobody asked for one: the delivery view has to agree with the requirement view
- Supplied hard values travel into Requirements verbatim. A number, a size, a spacing, a heading level, a limit, a token, a button order or an exact string the source states is copied into a constraint bullet with its value intact, in the source's own units and notation, inside backticks. Never generalise a supplied value into a description of itself: `32px` never becomes updated spacing, and `Link Instagram` never becomes updated copy. A generalised value is not a shorter requirement, it is a different and false claim, that the change is still unspecified. This binds copy the source shows as much as copy it types. A sheet whose screenshot reads `We noticed your Instagram isn't linked yet.` has supplied that string, so the bullet quotes it, and writing that the sheet states Instagram is not linked is the same generalisation failure as writing `32px` as updated spacing
- Where the source organises its values by screen, surface or component, Requirements mirrors that organisation: one bold-lead group per screen, named as the source names it, holding that screen's values and nothing else. The group holds as many bullets as the screen has supplied values, reuse entries and rules, and never more. A screen heading with one prose line under it is a one-bullet group, and an empty container is never filled from the design. The grouping is supplied information in its own right, because it is what tells a developer which screen each value lands on
- Where the source states which flows reuse a screen, that reuse map is a constraint bullet in the same group, naming each flow the source names. It is a constraint rather than background, because it is what makes the change land once on a shared screen instead of once per flow, and a developer who cannot see it will restyle per flow
- A change the source names without giving its content, such as updated copywriting with no text supplied, is carried as a constraint pointing at the design or the party that settles it. Never invent the string, and never drop the line: an unsupplied value is an open constraint, not an absent one. What travels is the pointer, not the source sentence rewritten. A source line saying a new sheet explains the situation yields one bullet naming the screen and the design that settles it, never a group of bullets recounting what the sheet says
- Every line of the source is accounted for, not only the lines under a screen heading. Accounted for means the change the line names lands in the draft, never that the line's own wording lands in Requirements. A line that gives a value is accounted for by that value, and a line that names a screen without giving one is accounted for by a single bullet pointing at the design. A change stated above the first heading, in a preamble, or for a surface the headings never name, such as the modal that opens the flow or a global change to all screens, is a supplied value like any other. It gets its own bold-lead group named for the surface it changes, and it is never folded into a neighbouring screen or dropped because the source did not give it a heading
- Source prose is material, never copy. The Human Voice rules apply to what the artifact says, so a hedge, an opener, a filler phrase or a vague qualifier in the source is rewritten as a fact, an open constraint or a plain condition. Only exact product copy, identifiers, values and an open question the source words itself are carried verbatim, inside backticks, so an `**Open:**` line quotes the source's question and then names who settles it. A source that hedges whether a flow will run again and whether other flows will pick up its screens becomes an artifact that states the flow can run again and its screens are reused, because the hedges belonged to the author's uncertainty, not to the product
- The default shape is lean. The optional enrichments in section 6 (value lines, Rule blocks, Which-means-that, Definition of Ready/Done, User Story promise block) are added only when the artifact earns them
- User-supplied context is the main source of truth. Never invent requirements, evidence or links. An edge case, assumption or other addition the user did not supply is allowed only when the chat response names it as an addition, so the user can strike it. An addition the response does not name is an invented requirement, and naming one never makes invented evidence or a link acceptable
- Apply every gate under Quick energy

---

### What a described screen becomes

The rule above is the one a source most often pulls against, because a draft
written by a person describes screens in prose and every line of it has to be
accounted for. Accounting for those lines is not copying them. A source section
reading:

```text
#### 2. Initial Instagram Sheet
*   Completely new sheet that explains the situation
*   A bottom sheet over the presentation screen with the page still visible behind it
*   It says Instagram is not linked, explains that quick connect now works without
    logging in again, and carries one action, "Link Instagram".
```

becomes one group with the supplied strings quoted and nothing else:

```markdown
**Initial Instagram Sheet**
* * *
*   A new sheet on the Highlights onboarding flow, per the linked design
*   The single action reads `Link Instagram`
```

Three source lines, two bullets. "Explains the situation" names nothing a build
could get wrong. "A bottom sheet with the page visible behind it" is presentation
the design settles, and the source named no alternative it rules out. "It says
Instagram is not linked" and "quick connect works without logging in again" are
copy the source paraphrased rather than quoted, so they are dropped and the
design carries them, and they return as bullets the day the source supplies the
strings. What survives is the one exact string the source did give.

---

## 2. ARTIFACT-KIND SELECTION

Resolve the shape before drafting. Story and Epic are artifact **kinds**, not size tiers: detail scales with the supplied scope, the section order never changes. They differ in three places: the About sub-sections (Story has `#### **Expected outcomes**`, Epic has `### Goal`), the middle section (Story has `## Requirements`, Epic has `## Scope`) and the altitude of the acceptance criteria (Story verifies screens, Epic states release outcomes). Everything else is shared.

- **Story:** one feature area with a few outcome-led acceptance criteria and hard requirements where the delivery has them. Selected by `$story`, `$s`, `$prd`, `$p`, "write a PRD/story", "write a draft", "draft for PM", or a plain `# {Persona} - {Area} - {Feature}` H1. Carries `#### **Expected outcomes**` and, only when there are hard constraints to state, `## Requirements`
- **Epic:** an initiative split across child stories, where requirements live in the children. Selected by `$epic`, `$e`, "write an epic", or an `# Epic - …` H1. Carries `### Goal` and `## Scope`, keeps acceptance criteria at release level, and has **no** `## Requirements` section by default

Selection rules:

- An explicit artifact command wins over framing. `$epic` or `$e` selects Epic. `$story`, `$s`, `$prd` or `$p` selects Story. An Epic noun inside a Story command's subject does not override the command: `$story for the onboarding epic` stays a Story, and `$epic based on these stories` stays an Epic. If both a Story and an Epic signal appear together (for example `$prd $epic`), the explicit Epic signal selects the Epic shape. An explicit Epic signal is `$epic`/`$e`, epic framing, or an `Epic -` H1
- With no command, natural framing decides: "write/create/refine an epic" selects Epic, and "write a PRD / user story / turn this into a PRD" selects Story. Draft wording ("write a draft", "draft for PM", "give the PM a draft") also selects Story, because the pre-PM draft is retired and a Story is what such a request now wants
- One qualifier inside a phrase never changes the shape. "Write a full story" is the same request as "write a story", and "turn this into a quick PRD" the same as "turn this into a PRD"
- A zero-requirements request is valid: it signals the Epic shape, not a malformed Story. Only ask for a concrete requirement when the request clearly wants a Story but supplies none
- An explicitly stated requirement count or child-story set is authoritative. Clauses, actions, states, edge cases and acceptance checks inside a stated requirement do not create extra requirements. If supplied source labels a conflicting set, include the conflict in the one consolidated intake question. Never silently override the user's count
- Shared machinery is described once inside `### Solution` (Story) or `## Scope` (Epic). It does not spawn a separate template or tier
- When the artifact kind is genuinely unclear, fold it into the one consolidated intake question. Do not ask a separate round
- Quick energy biases toward the leanest honest shape. It never drops a gate the artifact genuinely needs

State the chosen artifact kind (Story or Epic) in the delivery response.

---

## 3. HOUSE GRAMMAR

These apply to every Story and every Epic:

- Narrative first: the artifact opens with prose (`## About`) that carries scope and value before any structured detail. Prose is never replaced by ticket boilerplate
- `### Solution` is the product decision in prose: what changes for the user and why that shape answers the Problem. It restates neither the constraints in Requirements nor the outcomes in Acceptance criteria, and names no mechanism. Bullets appear only when several distinct changes need telling apart, one line each
- No ticket header fields (no Type/Epic/Priority/Estimate/Status), no story points, no INVEST notes anywhere
- Requirements hold hard requirements only: the formats, limits, platforms, integrations, compliance rules and performance floors the delivery has to satisfy whatever approach the developer takes. Each group is a bold-lead name, a divider and short `*   ` bullets, one constraint per bullet, stated as a fact or an instruction. Never a `**Checklist**` sub-block or `- [ ]` items, never a user outcome dressed as a constraint, and never a description of what a screen says, shows or contains. The output-format gate holds a narrow slice of that ban and a reader holds the rest: it fires on a bullet reading explains, states, tells or informs while quoting none of the copy, and any backtick in the bullet exempts it, because a bullet that quotes the copy has carried the value. The wider class is not mechanically separable from a constraint, so a bullet saying a screen shows or contains something is a defect the gate will not catch for you. Every bullet is a sentence a build can fail: it names a value, a limit, a condition, an effect or a named flow a build could get wrong, and a bullet that names none of those is description the design link already carries, struck rather than reworded. A bullet naming a presentation shape is a constraint only where the source itself named the alternative it rules out, because an alternative the writer supplies is an invented decision. The section is optional only where there is nothing hard to hold: omit it, spacer included, when the source names no hard constraint and the acceptance criteria say everything. One supplied hard value makes the section mandatory. Optionality is permission to omit an empty section and never permission to drop a value the source supplied, and Quick energy does not change that
- Acceptance criteria are numbered `1\.` bold-title blocks. Each holds `*   **Given/When/Then/And**` ClickUp bullets and closes with `- [ ] _Mark as done, if the criteria are met_`. No divider separates a Mark-as-done line from the next criterion, so one blank line is the whole separator. A criterion states what the user can rely on once the work ships and the quality it has to have, from the product's point of view, and leaves the mechanism to the developer: playback starts at once and adapts to the connection, not which player or bitrate ladder does it. Keep them few. One per outcome the story exists to guarantee, plus the edges that matter. The count grows only with the number of surfaces and considerations the story touches, never with its size or the number of requirements keep. Story criteria verify screen-level behavior, and Epic criteria stay release-level. A supplied hard value belongs in Requirements and not inside a Given/When/Then. A criterion names the outcome the value serves and leaves the value where it is stated once, so a spacing, a heading level, a token or an exact button order never becomes the Then clause. The test is mechanical: a criterion that would have to be edited when a design token changes is a criterion holding a constraint that belongs in Requirements. A criterion names the surface it verifies and does not re-list the flows that share it
- Section close: a `* * *` sits on the line directly above every `##   ` spacer heading and closes the H2 section that spacer ends. This is the one sanctioned divider after a Mark-as-done checkbox, and it is what closes Requirements, Scope and Acceptance criteria before the next H2 opens. An H3 sub-section's `###   ` spacer takes no divider above it. The close belongs to the section rather than to the gap between two sections, so an artifact that ends on Acceptance criteria still writes the `* * *` above its `##   ` spacer and that spacer is the file's last line. Only `## Delivery` closes on a bare `* * *` with no spacer after it, because nothing follows it. A refinement keeps whatever the source document does here
- Given, When, Then and And repeat verbatim in every criterion. They are fixed labels rather than prose, so the Human Voice synonym-cycling rule requires the repetition instead of penalising it. Never vary them for the sake of variety
- Bullet items never end with a full stop
- `## Delivery` is optional and opt-in. Write it only when the requester asks for it, or when the artifact forces it: a requirement carrying an `**Open:**` line, or a constraint outside the team's control that has no date. When it is written it closes the artifact and holds Estimation, Rabbit holes and No-gos, in that order, with unknown values left as `TBD...` rather than an inferred estimate, risk or exclusion. `TBD...` is a fixed house token and carries a named exemption on the Human Voice card, so three of them in one Delivery section is correct output, not three ellipses. When it is not written, `## Acceptance criteria` is the last section and nothing replaces Delivery. A section written unasked and filled with three `TBD...` slots is worse than an absent one, because it reads as a delivery view the team never took. The output-format gate reports an all-placeholder Delivery as advice and never blocks on it, because whether the requester asked lives in the request and never in the artifact, so the same three slots are correct output in one run and a section nobody asked for in the next
- What opts it in: a request naming the section or any of its parts (delivery section, estimation, estimate, sizing, how long, rabbit holes, no-gos, out of scope, scope exclusions, external dependencies), a request for the artifact to be sprint-ready or ready for planning, or one of the two content forcings above. Quick energy never opts it in on its own, and never drops it once one of those triggers fired
- A constraint the team does not control and cannot date (an app-store review, a partner integration, a legal or security sign-off, a contract that has to land first) belongs in an optional fourth Delivery sub-section, `#### External dependencies`, placed directly after Estimation because it qualifies the estimate. It is not a Rabbit hole, which names effort the team could waste, and not a No-go, which names scope the team is choosing to exclude. Name the external party, what it has to do, and what is blocked until it does. Leave its date `TBD...` rather than inventing one, and never convert an undated external constraint into a delivery date
- ClickUp-native grammar: `* * *` dividers immediately after each content heading, `*   ` unordered bullets for prose and Given/When/Then, `- [ ]` checklists only for the per-criterion Mark-as-done line, `1\.` numbering for acceptance criteria and same-level spacer headings (`##   `, `###   `) between major sections
- Spacer headings stay in a Story or Epic file export. They are part of the Barter house format rather than a paste-time affordance, so a Story and an Epic each keep every spacer the sections they actually carry produce, in the saved `.md` exactly as in ClickUp. This is the opposite of the Doc rule, where a spacer heading is a ClickUp-only affordance that a file export drops
- Heading depth: H1 is the title only. Major sections (`## About`, `## Requirements` or `## Scope`, `## Acceptance criteria`, `## Delivery`) anchor at H2. The opening group sections sit at H3 (`### Problem`, `### Solution`, `### Goal`), and scenario groups inside Acceptance criteria sit at H4 (`#### {Group}`). `#### **Expected outcomes**` and `#### **References**` sit at H4-bold. Requirement names use bold paragraph leads (`**{Requirement name}**`). Gates and spec sub-blocks use H4-bold headings (`#### **Rule**`). Sub-labels inside References are plain paragraph text (`Components`, `Flows`, `Lifecycle`), not bold. Nothing goes deeper than H4
- Preserve technical identifiers exactly, even when they look misspelled or use local notation (for example `Below 2.500 followers`). Flag oddities in prose instead of normalizing them
- Exact expressions, thresholds, field names and event names travel in backticks
- Links appear only when supplied. Never invent a Figma destination or a ClickUp link. Images are embedded in ClickUp after export, so a Story or Epic never carries an image, a screenshot reference or a file path to one

### The H1 title

The title is the plain, hyphen-joined path to the work, with no `PRD -` prefix and no `BO`/`BE`/`FE` short codes:

- **Story:** `# {Persona or platform} - {Area or initiative} - {Feature}`
- **Epic:** `# Epic - {Persona or platform} - {Area or initiative}`

Worked house titles: `# Creator - Onboarding v2 - Password reset`, `# Creator - Onboarding v2 - Welcome & Sign-in`, `# Epic - Creator - Onboarding v2`. Segments follow the real hierarchy (persona, then the epic or area, then the specific feature). A feature name may itself hold a hyphenated sub-part, as in `# Creator - Onboarding v2 - Sign-up - Pre-Approval`.

**When the work spans every persona.** `{Persona or platform}` has a sanctioned value for platform-wide work, so nothing forces a false persona onto a cross-persona Epic. Use `Platform` when the initiative genuinely lands across the whole product, as in `# Epic - Platform - Consent and data retention`. Use the shared surface's own name when the change is bounded to one system that several personas touch, as in `# Epic - Notifications - Delivery rework`. Never stack personas into the segment (`Creator and Brand`), never drop the segment, and never pick one persona because it happens to be affected most. Pick the word a reader would search for.

### The story preamble

Every new **Story** opens with the native ClickUp preamble, verbatim, directly under the title's divider, as plain italic lines rather than a blockquote:

```markdown
* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._
```

An **Epic** omits this preamble. It goes straight from the title's `* * *` divider to `## About`.

---

## 4. CREATE WORKFLOW

### Step 1: Establish the Contract

Identify the artifact kind (Story or Epic), the user role and the value clause. For a Story, identify the outcomes the user has to be able to rely on, which surfaces they sit on, and any hard constraint the source names: a format, a limit, a platform, an integration, a rule, with its technical identifiers. For an Epic, identify the child-story set and the Goal. Also identify whether outcomes share a mechanism, any supplied evidence, links or source material, and the requested depth or Quick energy. If artifact kind, role, value or requirement shape cannot be established safely, ask the one consolidated question and wait.

Before drafting, list every hard value the source states, in the source's own grouping and notation: sizes, spacings, heading levels, limits, exact strings, button copy, type and order, toasts and other confirmations, platforms, integrations, and for each screen the flows the source says reuse it. Walk the source top to bottom and list a line that sits above the first heading or belongs to no screen section under the surface it changes, so the list has as many entries as the source has changes. That list is the input to Requirements. Account for every entry in the draft, either as a constraint bullet or as a line in the delivery response naming it deliberately out of scope. A supplied value that appears in neither is a defect rather than an editorial judgement. A screenshot the requester supplies is source material like any other line, and what it supplies is its exact copy, its labels and its values. It does not supply its layout, its composition or a paraphrase of what it communicates, because the design link already carries those and a bullet repeating them fixes nothing a build could get wrong.

### Step 2: Select the Shape

Apply the artifact-kind selection above. State the chosen kind in the delivery response, and load only that shape's scaffold.

### Step 3: Draft From the House Shape

- The `## About` umbrella: narrative scope and promise, then the opening group sections in the order the resolved shape's scaffold sets
- **Story:** `### Problem`, `### Solution`, `#### **Expected outcomes**`, `#### **References**` (supplied links only), then `## Requirements` only when the delivery has hard constraints to state, each group a bold name, a divider and one constraint per bullet. No outcomes there, no checklist, no images
- **Epic:** `### Problem`, `### Goal` (with direct benefits), `### Solution`, `#### **References**` (supplied links only, omitted when none are supplied, never left empty or given an invented link), then `## Scope` with child-story groups and an optional `#### Added Later` group. No `## Requirements`
- `## Acceptance criteria`: a few numbered Given/When/Then blocks, each an outcome the user can rely on with the how left open, and a Mark-as-done checkbox that no divider separates from the next criterion, closing with a `* * *` above the section's `##   ` spacer. Story criteria cover the surfaces the story touches (optional `#### {Group}` headers when it spans several). Epic criteria stay release-level
- `## Delivery`, only when the requester asked for it or an `**Open:**` line or an undated external constraint forced it: Estimation, Rabbit holes, No-gos, in that order, `TBD...` where unknown. Otherwise the artifact ends on Acceptance criteria
- Optional enrichments from section 6 (per-requirement value line, Rule block, Which-means-that, Definition of Ready/Done, User Story promise block, `← PRIO`) only where they earn their place

### Step 4: Validate and Export

- Run the quality checklist below and the Human Voice Rules
- Validate house grammar: the story preamble (Story only), `* * *` dividers after each content heading, `*   ` bullets for prose and Given/When/Then, no bullet item ending with a full stop, `1\.` numbering on acceptance criteria, the Mark-as-done line closing each criterion with no divider between it and the next criterion, a `* * *` section close directly above each `##   ` spacer heading, requirements carrying no `**Checklist**`, `## Delivery` present only where it was asked for or forced and closing the artifact when present, and at most one `← PRIO`
- Validate heading depth: H1 title only, major sections at H2, opening group sections at H3, Expected outcomes and References at H4-bold, requirement names as bold paragraph leads, and scenario groups and gates at H4
- Confirm every Story acceptance criterion traces back to a requirement and covers the normal path, the edges that matter and the guarantee the story keeps. Confirm every Epic criterion stays release-level
- Reconcile the Step 1 value list against the draft: every supplied hard value appears in `## Requirements` with its value, units and notation intact, grouped as the source grouped it, each shared screen's reuse map naming the flows the source names
- Confirm no supplied hard value survives only inside an acceptance criterion, and no criterion states a value that Requirements should hold
- Reconcile in the other direction as well: every bullet in `## Requirements` traces to a supplied value, a reuse entry, a rule or a design pointer. A bullet that traces to none of those is description, and it is struck rather than reworded
- Save using the export contract and verify the file exists before responding

---

## 5. REFINEMENT WORKFLOW

The existing artifact is the structural baseline. Adding conventional elements never restructures the document. This is the settled lesson from the Fv2.5 Rulesets review, where a full restructure into ticket blocks lost to the original narrative.

- Preserve the source's structure, headings, prose, requirement leads, identifiers, links, images and formatting outside the requested change
- Add requirements, scope items, acceptance criteria or gates in place, in the source's own grammar
- Keep known identifier oddities verbatim and flag them in prose
- Create-time shape checks do not fire on a source-preserving refinement. A source that still uses a build checklist, an old `PRD -` title or a different acceptance shape keeps it during an unrelated refinement. Do not normalize unasked. A source Epic that carries genuine standalone requirements keeps them. A source Story or Epic that carries a `## Delivery` section keeps it, populated slots and `TBD...` slots included. The section became opt-in for new artifacts, which is not a licence to strip it from an existing one, and removing it needs the same explicit authorization a restructure needs
- Fix only content the source clearly got wrong (a broken H1, a criterion with no backing requirement) and flag the fix
- Export a copy with the original source basename. Never overwrite the supplied source
- A refinement that requests restructuring or normalization to the new house shape needs explicit authorization, exactly as in Doc Mode

---

## 6. OPTIONAL ENRICHMENTS

Add these only when the artifact earns them. None is required. Most stories use none.

### 6.1 User Story promise block (optional)

The Connextra promise for the whole feature, added under `### Solution` only when several capabilities need explicit promise lines. The About narrative normally carries the promise already.

```markdown
#### **User Story**
* * *
As a {end-user or team role}:
*   I want {capability 1}, so that {benefit 1}
*   I want {capability 2}, so that {benefit 2}
```

### 6.2 Per-requirement value line (optional)

A Connextra value line under a requirement name, when the requirement's own "why" is not obvious from the About promise.

```markdown
**{Requirement name}**
* * *
**PRD:** As a {role} {using this specific part}, I want {capability}, so that {benefit in the user's terms}.

*   {Outcome bullet}
```

### 6.3 Rule / spec block (optional)

For a requirement that hinges on an exact threshold, expression or field. State each rule with the exact value in backticks and one plain-language line.

```markdown
#### **Rule**
* * *
**{Rule name}:** `{exact expression or threshold}`
{One plain-language line explaining it.}
* * *
```

### 6.4 Which means that (optional)

Implications drawn from a Rule block, stated from the user's view, to name a guarantee the acceptance criteria then prove.

```markdown
Which means that:
*   {The hard guarantee, from the user's view}
*   {Behavior when the normal path comes up short}
```

### 6.5 Definition of Ready (optional)

A readiness gate placed after `## About` or just before `## Requirements`. It never becomes the closing section: `## Delivery` closes the artifact where it is present, and Acceptance criteria closes it where Delivery is absent. Boxes reflect honest state. An unchecked sizing box means the work is not sprint-ready.

```markdown
#### **Definition of Ready**
* * *
Check off as met; pull requirements into a sprint only when every box is checked:
- [ ] Every acceptance criterion is agreed as an outcome, and every hard requirement is confirmed with the team that has to meet it
- [ ] Dependencies identified ({service, API or data this relies on is live, or confirmed absent})
- [ ] Sized by the team and each requirement fits comfortably in a sprint
##   
```

### 6.6 Definition of Done (optional)

A done gate placed after the acceptance criteria, before `## Delivery` where that section is present and as the artifact's last block where it is not, keeping its own `##   ` spacer as the file's last line.

```markdown
#### **Definition of Done**
* * *
Verify for every requirement above before its task closes:
- [ ] The requirement's acceptance criteria all pass against {the live system or realistic data}
- [ ] Tests added covering {each rule and guarantee stated above}; CI green
- [ ] Reviewed by a second engineer
```

### 6.7 Priority marker (optional)

When several requirements compete, mark exactly one `← PRIO` on its requirement name so the lead is unambiguous.

```markdown
**{Requirement name}** ← PRIO
```

### 6.8 Open question on a requirement (optional)

A requirement can be agreed in outcome and still have one part nobody has decided. Rabbit holes is the wrong place for it, because a developer who reads Requirements and Acceptance criteria and stops there would never see it, and the requirement reads as fully specified. Mark it where it is.

The `**Open:**` line sits directly under the requirement name's divider, above the constraint bullets, so it is read before the requirement is. Write the undecided part and what settles it. The constraint bullets then state only the settled constraints, and the matching acceptance criterion verifies only that part.

```markdown
**{Requirement name}**
* * *
**Open:** {the part that is not decided}. {Who decides it, or what evidence settles it.}

*   {Settled outcome sentence}
```

Rules that keep the marker honest:

- At most one `**Open:**` line per requirement. Two open questions on one requirement means the requirement is two requirements, or it is not ready
- Never write an acceptance criterion for the open part. A criterion asserts behavior, and the open part has none yet
- Carry the same open question into `## Delivery` under Rabbit holes, so the delivery view and the requirement view agree
- Resolve it or restate it on every refinement. An `**Open:**` line that outlives its decision is worse than none
- A Story where most requirements carry one is a Story that was written too early. Say that in the response rather than shipping it quietly

### 6.9 External dependencies in Delivery (optional)

The fourth Delivery sub-section, for a constraint the team does not control and cannot date. It goes directly after Estimation, because what it qualifies is the estimate. An undated external constraint is the second thing that opts `## Delivery` in without a request, because a constraint the team cannot date has nowhere else honest to sit.

```markdown
#### External dependencies
* * *
Constraints outside the team's control that gate delivery, with no date the team can set.

*   **{External party}** - {what they have to do}, {what stays blocked until they do}. Date: TBD...
```

Use it for an app-store review, a partner integration, a legal, security or compliance sign-off, or a contract that has to land first. Do not use it for work another internal team owes, which is ordinary scheduling and belongs in Estimation. Leave the date `TBD...` rather than guessing, and never let an undated external constraint become a delivery date.

---

## 7. DELIVERY STANDARDS

### Artifact Rules

- One complete house-format markdown artifact per request, except the Story with nested Tasks bundle below
- No ticket header blocks, story points or INVEST notes anywhere
- Acceptance-criteria steps carry observable outcomes. Internal state belongs in a requirement's prose or an optional Rule block
- The H1 is the plain hyphen-joined path: a Story is `{Persona or platform} - {Area or initiative} - {Feature}`. An Epic is `Epic - {Persona or platform} - {Area or initiative}`. No `PRD -` prefix and no `BO`/`BE`/`FE` short codes

### Export Contract

New Story:

```text
export/[###] - Story-[description].md
```

New Epic:

```text
export/[###] - Epic-[description].md
```

Refined Story or Epic:

```text
export/[original-source-filename].md
```

Never overwrite the supplied source.

### Story With Nested Tasks

A new Story asked for together with its task breakdown, such as `$story` with "break it into tasks", is one dependent deliverable rather than two independent artifacts, so it needs no question about which artifact to make. Two explicit artifact commands such as `$story $task` stay a conflict. The bundle applies to a new Story only, because a refined Story keeps its source filename.

It saves as one folder under one number:

```text
export/[###] - Story-[description]/
  [###] - Story-[description].md
  [###].1 - task-[description].md
  [###].2 - task-[description].md
```

- `n` in `[###].[n]` counts from 1 in the Story's task order. A Story with one task is still a bundle, with `[###].1` alone
- A split the request names is authoritative, one task per named part. With none named, the one consolidated Story question asks for it, and nothing is drafted until the user answers. Quick energy may skip routine intake, and it still writes the whole bundle
- A clarification asked first keeps the Story lane at the top of `export/`, as `export/[###] - Story-[description]-clarification.md`. The folder takes the next number, and the clarification stays outside it, untouched
- The Story lists its tasks in a `#### **Tasks**` block inside `## About`, after `#### **References**`, one bullet per task in `n` order, each linking the sibling task file. It never uses `## Scope` for this, because `## Scope` marks the Epic kind
- Each task uses the Canonical Task template from `assets/task-templates.md`, read under the skill's ON_DEMAND allowance for one template asset, so the one-scaffold rule still governs the Story. Each task names its Story in a `**Story**` block between `**Epic**` and `**Parent task**`, and carries no `**Parent task**` block for it, because a Story is not a task

```markdown
#### **Tasks**
* * *
*   [{Task H1}](<[###].1 - task-[description].md>)
*   [{Task H1}](<[###].2 - task-[description].md>)
```

### Response Contract

Respond with the saved path, the artifact kind (Story or Epic), a compact quality summary and a brief next step. Validate the house grammar and honest Delivery state, save, then verify before reporting. In a Claude Project runtime, deliver one markdown artifact with the export-equivalent path. When ClickUp tooling is available, offer ClickUp delivery and wait for explicit approval, per the skill's ClickUp handoff rule.

For a Story with nested Tasks, read back every file in the folder, then reply with every path, Story first, each with its own `Verified: read-back succeeded; N lines` line, and one `HVR self-scan:` line counted across the whole bundle. A file whose read-back still fails after one retry gets no `Path:` line, and the reply says the bundle is blocked rather than delivered. In a Claude Project runtime, render one Deliverable Block per file, Story first, each followed by its own `Export-equivalent path:` inside the folder, then one `HVR self-scan:` line for the set.

---

## 8. WORKED EXAMPLES

- [`examples/story/prd-example-simple.md`](../assets/examples/story/prd-example-simple.md): a small Story with one requirement, a flat acceptance-criteria list and no Delivery section, so the artifact ends on Acceptance criteria
- [`examples/story/prd-example-medium.md`](../assets/examples/story/prd-example-medium.md): a Story with several independent requirements and grouped acceptance criteria, and no Delivery section
- [`examples/story/prd-example-complex.md`](../assets/examples/story/prd-example-complex.md): a Story whose requirements share one mechanism, described once in Solution, with a `← PRIO` marker
- [`examples/story/prd-example-complete.md`](../assets/examples/story/prd-example-complete.md): the maximal Story, every optional enrichment populated, as a reference for what is available
- [`examples/story/prd-example-epic.md`](../assets/examples/story/prd-example-epic.md): an Epic with a Goal, a Scope of child stories and an Added Later group, release-level acceptance criteria and no Requirements
- The four live Onboarding v2 stories and the Onboarding v2 epic (under `Product Context/Tasks & Stories/Stories/Onboarding/`) are the team-written reference for the Story and Epic shapes

Load at most one worked example per request.

---

## 9. QUALITY CHECKLIST

- [ ] Artifact kind resolved (Story or Epic) and named in the response?
- [ ] Narrative present: the `## About` umbrella (scope and promise in prose, then Problem and Solution) opens the artifact before any structured detail, and Solution reads as a decision rather than a preview of Requirements or the criteria?
- [ ] Story: `#### **Expected outcomes**` present, and `## Requirements`, if present, holds only hard constraints with no outcomes, no screen description, no `**Checklist**` and no images?
- [ ] Epic: `### Goal` and `## Scope` present and no `## Requirements` unless the source needs it?
- [ ] Acceptance criteria numbered `1\.`, few, each an outcome the user can rely on with the how left to the developer, closed with a Mark-as-done checkbox that no divider separates from the next criterion?
- [ ] Each H2 section closed with a `* * *` directly above its `##   ` spacer heading, and every spacer heading retained in the export?
- [ ] An Epic Scope with no child-story links yet names each intended child story as plain text instead of inventing a URL or dropping it?
- [ ] A cross-persona Epic H1 uses `Platform` or the shared surface's own name rather than a stacked or arbitrarily chosen persona?
- [ ] An externally driven, undated constraint sits in `#### External dependencies` after Estimation rather than in Rabbit holes or No-gos?
- [ ] A requirement with one undecided part carries its `**Open:**` line under the requirement name, with no acceptance criterion asserting the open part?
- [ ] Story criteria cover each surface the story touches without multiplying beyond them, no artifact references a screenshot or image path, and Epic criteria stay release-level?
- [ ] No newly authored or rewritten bullet item ends with a full stop?
- [ ] `## Delivery` written only where the requester asked for it or an `**Open:**` line or an undated external constraint forced it, and closing the artifact with Estimation, Rabbit holes and No-gos, `TBD...` where unknown, when it is written?
- [ ] With no Delivery section, Acceptance criteria is the last section, closed with the `* * *` above its `##   ` spacer, and no `TBD...` placeholder survives anywhere in the file?
- [ ] Every hard value the source supplied appears in `## Requirements` with its value, units and notation intact, including any change stated above the first heading or outside every screen section?
- [ ] No hedge, opener or filler phrase from the source survives in the artifact's prose, so the Human Voice gate passes on a Story written from hedged notes?
- [ ] Requirements mirrors the source's own screen or surface grouping, one bold-lead group per screen under the source's own name, where the source is organised that way?
- [ ] Each shared screen's reuse map names the flows the source names, as a constraint in that screen's group rather than as prose in About?
- [ ] No supplied hard value sits only inside an acceptance criterion, and no criterion would need editing if a design token changed?
- [ ] Optional enrichments present only where they earn their place?
- [ ] No ticket fields, points or INVEST anywhere?
- [ ] House grammar and heading depth pass?
- [ ] Identifiers preserved exactly?
- [ ] Links and images only where supplied?
- [ ] Refinement preserved the source structure and basename?
- [ ] Reader simulation passes: a developer could cut a ticket from each Story requirement without a follow-up question?
- [ ] Export exists and was verified before the response?

---

## 10. ERROR RECOVERY

- **Unclear artifact kind:** fold Story versus Epic into the one consolidated question. Never ask it as a second round
- **Requirements arrive mid-draft for an Epic:** keep them in the child stories where possible. Add an epic-level requirement only when it is genuinely standalone, and say so
- **A Story request with no requirements:** ask for the outcome and at least one concrete requirement. A zero-requirement request that reads like an initiative is an Epic, not a broken Story
- **Research or feasibility spike:** decide/confirm/document work with no buildable behavior usually routes to Task Mode, or Doc Mode for a written recommendation
- **Source artifact conflicts with supplied context:** user context wins. Flag the difference in prose rather than silently merging

Final reminders: resolve the shape first, across Story and Epic, and load only that shape's scaffold. Narrative comes first. Acceptance criteria prove the promise and trace to requirements (Story) or state release outcomes (Epic). Requirements never carry a build checklist. `## Delivery` is opt-in and closes the artifact where it is written. Export first and verify.
---

The kernel points here for the Story Mode consultation rule:

16. Consult Story Mode plus the one scaffold the resolved shape names for Story work, resolve the artifact kind (Story or Epic) before consulting any scaffold and name it in the delivery response, keep requirements free of build checklists, and add a Delivery close only where the requester asked for it or the artifact forced it.

The kernel points here for this PRD prohibition:

14. Never put ticket header fields, story points or INVEST notes in a PRD artifact, never add a build checklist to a PRD requirement, and never restructure an existing PRD when the request is only to add PRD elements.
