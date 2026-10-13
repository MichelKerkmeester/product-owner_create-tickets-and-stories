---
title: "Feature Specification: Product Owner Story and Epic Templates"
description: "Align Product Owner story PRDs with the approved Onboarding examples, add a separate epic template and route, and keep Delivery as the shared closing section."
trigger_phrases:
  - "product owner story and epic templates"
  - "product owner prd template update"
  - "product owner epic template"
  - "prd estimation rabbit holes no-gos"
importance_tier: "high"
contextType: "specification"
_memory:
  continuity:
    packet_pointer: "005-product-owner-prd-delivery"
    last_updated_at: "2026-08-13T16:00:00Z"
    last_updated_by: "codex"
    recent_action: "Expanded the Delivery-only packet into the approved Story and Epic template contract"
    next_safe_action: "Implement authoritative Product Owner story and epic template sources"
    blockers: []
    key_files:
      - "AI Systems/Product Owner/sk-product-owner/SKILL.md"
      - "AI Systems/Product Owner/sk-product-owner/assets/prd-templates.md"
      - "AI Systems/Product Owner/sk-product-owner/references/prd-mode.md"
      - "AI Systems/Product Owner/benchmark/router/"
    completion_pct: 20
    open_questions: []
    answered_questions:
      - "The four dated Onboarding stories define the new Story or PRD house shape"
      - "The dated Onboarding epic defines a separate Epic shape with Goal and Scope"
      - "Requirements are omitted from epics by default because child stories own them"
---
# Feature Specification: Product Owner Story and Epic Templates

<!-- SPECKIT_LEVEL: 2 -->
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->

---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|---|---|
| **Level** | 2 |
| **Priority** | P1 |
| **Status** | Draft |
| **Created** | 2026-08-13 |
| **Updated** | 2026-08-13 |
| **Branch** | Current worktree, no branch created |
| **Packet note** | The legacy folder name is retained to preserve packet identity and continuity |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement

The Product Owner PRD template does not match the approved stories now used by the Barter team. It still teaches tier-driven Simple, Medium and Complex shapes, requirement checklists and a `PRD -` title convention. The approved stories instead use one stable story shape with concise requirement bullets, optional acceptance-criteria groups and a shared Delivery close.

The Product Owner system also has no dedicated Epic contract. An epic has a Goal and Scope, keeps acceptance criteria at release level and normally leaves detailed requirements to its child stories. Forcing an epic through the story template produces the wrong structure and repeats detail that belongs lower in the hierarchy.

### Purpose

Use the four approved Onboarding stories as the structural basis for Story or PRD output. Add a separate Epic template and routing path based on the approved Onboarding epic. Keep Delivery as the closing section shared by both artifact kinds.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:source-evidence -->
## 3. SOURCE EVIDENCE

### Approved Story Sources

| Source | Structural evidence |
|---|---|
| `Product Context/Tasks & Stories/Stories/Onboarding/26-08-13 - Creator - Onboarding v2 - Password reset.md` | One story preamble, concise requirements, ungrouped acceptance scenarios and Delivery |
| `Product Context/Tasks & Stories/Stories/Onboarding/26-08-13 - Creator - Onboarding v2 - Sign-up - Post-Approval.md` | Requirement screenshots, grouped acceptance scenarios and Delivery |
| `Product Context/Tasks & Stories/Stories/Onboarding/26-08-13 - Creator - Onboarding v2 - Sign-up - Pre-Approval.md` | Several requirement blocks, grouped acceptance scenarios and Delivery |
| `Product Context/Tasks & Stories/Stories/Onboarding/26-08-13 - Creator - Onboarding v2 - Welcome & Sign-in.md` | Short About opening, natural requirement bullets, grouped acceptance scenarios and Delivery |

The four stories share this order:

1. Story title and two-line story preamble
2. `## About`, `### Problem` and `### Solution`
3. `#### **Expected outcomes**` and `#### **References**`
4. Optional supplied visual and a major-section spacer
5. `## Requirements` with bold requirement names and natural `*   ` bullets
6. `## Acceptance criteria` with optional H4 groups and numbered Given/When/Then scenarios
7. `## Delivery` with Estimation, Rabbit holes and No-gos

### Approved Epic Source

`Product Context/Tasks & Stories/Stories/Onboarding/26-08-13 - Epic - Creator - Onboarding v2.md` establishes a different contract:

1. `# Epic - ...` title without the story preamble
2. `## About`, followed by `### Problem`, `### Goal` and `### Solution`
3. `#### **References**` and an optional supplied visual
4. `## Scope` with child-story groups and an optional `Added Later` group
5. No Requirements section by default
6. `## Acceptance criteria` limited to release-level outcomes
7. The same `## Delivery` close used by stories

### Authority Boundary

These five documents govern structure, section purpose, markdown grammar and writing density for this change. Their onboarding-specific claims, links, images and copy are examples, not reusable template content. The implementation must not modify them.
<!-- /ANCHOR:source-evidence -->

---

<!-- ANCHOR:scope -->
## 4. SCOPE

### In Scope

- Replace tier-selected Story or PRD templates with one stable Story shape
- Add explicit Story versus Epic artifact-kind selection inside PRD Mode
- Add exact `$epic` and `$e` commands that route to PRD Mode with Epic shape
- Route natural requests such as "create an epic" or "refine this epic" to Epic shape
- Keep `$prd`, `$p`, `$story` and `$s` on Story shape unless the request explicitly asks for an epic
- Add a dedicated Epic scaffold with Goal and Scope and no Requirements section by default
- Change Story requirements from checkbox lists to concise natural bullets
- Allow optional H4 acceptance-criteria groups when related scenarios benefit from grouping
- Keep Given/When/Then scenarios specific and observable
- Keep Delivery as the final standard section for both Story and Epic artifacts
- Update examples, routing fixtures, bootstrap instructions, README, Claude kernel and generated mirrors

### Out of Scope

- Editing the five approved Product Context sources
- Retrofitting existing exports or unrelated Product Context stories
- Copying onboarding-specific requirements, links or images into generic templates
- Changing Task, Bug or Doc templates
- Changing ClickUp write consent or markdown transport
- Adding detailed requirements to every Epic

### Files to Change During Implementation

| File Path | Change Type | Description |
|---|---|---|
| `AI Systems/Product Owner/sk-product-owner/assets/prd-templates.md` | Modify | Define canonical Story and Epic scaffolds and shared Delivery block |
| `AI Systems/Product Owner/sk-product-owner/references/prd-mode.md` | Modify | Replace tier selection with Story or Epic artifact-kind logic |
| `AI Systems/Product Owner/sk-product-owner/SKILL.md` | Modify | Add Epic commands, framing, routing metadata and house-format gates |
| `AI Systems/Product Owner/AGENTS.md` | Modify | Add Epic commands and loading behavior to the project bootstrap |
| `AI Systems/Product Owner/sk-product-owner/assets/examples/prd/` | Modify | Replace obsolete tier examples with canonical Story and Epic examples |
| `AI Systems/Product Owner/benchmark/router/` | Modify | Add positive, negative and conflict fixtures for Epic routing |
| `AI Systems/Product Owner/sk-product-owner/README.md` | Modify | Describe both artifact kinds and their commands |
| `AI Systems/Product Owner/sk-product-owner/changelog/` | Create | Record the released contract change with observed verification results |
| `AI Systems/Product Owner/claude project/Custom Instructions.md` | Modify | Hand-synthesize the same Story and Epic behavior for Claude |
| Compiler-owned mirrors and package metadata | Regenerate | Apply the Product Owner sync workflow after source changes |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 5. REQUIREMENTS

### P0 - Blockers

| Key | Requirement | Acceptance Criteria |
|---|---|---|
| REQ-01 | Artifact-kind selection | Every PRD request resolves to Story or Epic before template selection |
| REQ-02 | Story commands | `$prd`, `$p`, `$story` and `$s` produce Story shape unless Epic is explicit |
| REQ-03 | Epic commands | Exact `$epic` and `$e` commands produce Epic shape and embedded strings do not trigger them |
| REQ-04 | Story structure | Story output follows the approved seven-part order and does not add a `PRD -` title prefix |
| REQ-05 | Story requirements | Each requirement uses a bold name, divider and natural `*   ` bullets without a Checklist subheading or checkbox list |
| REQ-06 | Epic structure | Epic output includes Goal and Scope and omits Requirements by default |
| REQ-07 | Acceptance criteria | Story scenarios verify requirement detail while Epic scenarios remain release-level |
| REQ-08 | Delivery | Both shapes end with Estimation, Rabbit holes and No-gos in the approved order |
| REQ-09 | Refinement safety | Existing Story and Epic documents remain structural baselines unless normalization is requested |
| REQ-10 | Source authority | Authoritative `sk-product-owner/` sources change before derived mirrors or generated state |

### P1 - Required

| Key | Requirement | Acceptance Criteria |
|---|---|---|
| REQ-11 | Optional grouping | Acceptance criteria use H4 group headings only when two or more related scenarios benefit from grouping |
| REQ-12 | References and visuals | Links and images appear only when supplied, with no invented destinations or assets |
| REQ-13 | Unknown delivery inputs | Unknown values remain `TBD...` rather than inferred estimates, risks or exclusions |
| REQ-14 | Router precedence | Explicit commands beat framing, conflicting artifact commands clarify and subject mentions do not change artifact kind |
| REQ-15 | Example migration | Obsolete Simple, Medium and Complex examples no longer teach checklist or tier behavior |
| REQ-16 | Cross-runtime parity | CLI skill, bootstrap, templates, examples, README and Claude kernel describe the same two shapes |
| REQ-17 | Regression safety | Task, Bug, Doc, export and ClickUp consent behavior remain unchanged |

### Canonical Story Shape

```markdown
# {Platform or area} - {Feature} - {Name}

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
{Short narrative describing what this story covers.}

### Problem
* * *
{The problem or a link to the parent epic where the high-level problem is defined.}

### Solution
* * *
{The proposed product behavior, with concise bullets when several parts belong together.}

#### **Expected outcomes**
* * *
*   {User or business outcome}

#### **References**
* * *
{Supplied component, flow and lifecycle links grouped with plain labels. Omit when none are supplied.}

{Optional supplied overview visual}
##   

## Requirements
* * *
**{Requirement name}**
* * *
*   {Natural requirement sentence}
*   {Related requirement sentence}

{Optional supplied requirement visual}
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

#### {Optional scenario group}
* * *
1. **{Human scenario title}**
* * *
*   **Given** {precondition}
*   **When** {action or event}
*   **Then** {observable outcome}
* * *
- [ ] _Mark as done, if the criteria are met_
* * *
##   

## Delivery
* * *
#### Estimation
* * *
The delivery budget or expected size for the approved scope.

*   TBD...

#### Rabbit holes
* * *
Areas that could waste effort, create ambiguity or distract from the intended outcome.

*   TBD...

#### No-gos
* * *
Explicit scope exclusions and behaviors the delivery team must not introduce.

*   TBD...
* * *
```

### Canonical Epic Shape

```markdown
# Epic - {Platform or area} - {Feature}

* * *
## About
* * *
{Epic-level narrative describing the product change and why it matters.}

### Problem
* * *
{Current problem and its observable consequences.}
###   

### Goal
* * *
{The primary product or business goal.}

**Direct user/Barter benefits:**
*   {Direct benefit}
###   

### Solution
* * *
{The high-level product direction.}

#### **References**
* * *
{Supplied links only.}

{Optional supplied overview visual}

## Scope
* * *
Each child story owns one part of the outcome and carries its own detailed requirements and acceptance criteria.

#### {Scope group}
* * *
*   [{Child story}]({url})

#### Added Later
* * *
{Optional future capabilities that remain in the epic but do not block the current release.}
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1. **{Release-level scenario}**
* * *
*   **Given** {release-level precondition}
*   **When** {cross-story event or completed capability}
*   **Then** {observable release outcome}
* * *
- [ ] _Mark as done, if the criteria are met_
* * *
##   

{Use the same Delivery section as the Story shape.}
```
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:routing -->
## 6. ROUTING LOGIC

### Artifact-Kind Resolution

1. Detect exact artifact commands before natural-language framing.
2. `$epic` or `$e` selects PRD Mode with `artifact_kind=EPIC`.
3. `$prd`, `$p`, `$story` or `$s` selects PRD Mode with `artifact_kind=STORY`.
4. Natural framing such as "create an epic" selects Epic. Natural framing such as "write a story" or "write a PRD" selects Story.
5. An explicit Epic noun in a Story command's subject does not override the command. For example, `$story for the onboarding epic` remains Story.
6. Two conflicting artifact commands trigger the existing consolidated clarification flow.

### Depth Logic

Story and Epic are artifact kinds, not size tiers. The amount of detail scales with supplied scope, but the section order does not change. Shared mechanics may be explained once inside Solution or Scope without creating a separate tier or template.
<!-- /ANCHOR:routing -->

---

<!-- ANCHOR:success-criteria -->
## 7. SUCCESS CRITERIA

- Story output matches the approved Onboarding story structure without requirement checklists or tier labels
- Epic output matches the approved Onboarding epic structure with Goal and Scope and no default Requirements section
- Story and Epic outputs share the same Delivery close
- Exact Epic commands, natural Epic framing, conflicts and false positives have router fixtures
- Product Owner sync reports no mechanical drift after mirror regeneration
- Existing Task, Bug and Doc router fixtures retain their passing results
- The five approved Product Context sources remain unchanged
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 8. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|---|---|---|---|
| Risk | Retiring tier logic removes a familiar sizing label | Delivery responses may lose a shorthand | Report artifact kind and quality instead of Simple, Medium or Complex |
| Risk | `$e` may be overmatched inside other tokens | Unrelated requests could route to Epic | Reuse the exact-token boundary contract and add negative fixtures |
| Risk | Epics with genuine standalone requirements exist | Omitting Requirements could hide scope | Allow Requirements only when the supplied epic or user explicitly needs them |
| Risk | Source files contain ClickUp export quirks | Template could copy accidental formatting | Copy the repeated contract, not isolated typos or inconsistent numbering escapes |
| Risk | Existing PRD refinements use the old structure | Normalization could rewrite user content | Preserve source structure unless the user asks for the new house shape |
| Dependency | Product Owner sync compiler | Mirrors cannot be regenerated safely without it | Run plan, sync and check commands from `SYNC.md` |
| Dependency | Human kernel review | Compiler parity does not prove semantic kernel quality | Record human review only after final bytes exist |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Consistency

- Story and Epic labels, section order and markdown grammar must remain consistent across source templates, examples and runtime summaries
- New prose must pass Product Owner Human Voice Rules

### Maintainability

- Canonical scaffolds live once in `prd-templates.md`
- Routing owns artifact-kind selection without duplicating template content
- Generated mirrors remain compiler-owned

### Safety

- The change must not alter export paths, ClickUp consent or markdown-aware transport
- Product-specific source documents remain read-only fixtures
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Story and Epic Refinements

- A source with the old `PRD -` title keeps it unless the user requests normalization
- A source with requirement checklists keeps them during an unrelated refinement
- A source Epic with Requirements keeps them when they represent approved standalone scope
- A missing References block or visual is omitted rather than filled with placeholders

### Delivery Inputs

- Unknown estimate, rabbit holes or no-gos use `TBD...`
- A supported explicit none-known statement may replace `TBD...`
- Definition of Ready or Done remains optional and must not displace Delivery as the closing standard section

### Routing

- `$story for the onboarding epic` remains Story
- `$epic based on these stories` remains Epic
- `$task to write an epic` remains Task because explicit artifact commands win
- `$epics`, `$email` and filename-like `$e.md` tokens do not trigger Epic
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|---|---:|---|
| Scope | 23/25 | Core contract, bootstrap, examples, router fixtures, kernel and generated mirrors |
| Risk | 16/25 | New artifact kind and command aliases introduce routing and parity risk |
| Research | 13/20 | Five approved production documents establish both shapes |
| **Total** | **52/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 11. OPEN QUESTIONS

None. The approved source set establishes the Story and Epic shapes, the user confirmed that Epics normally omit Requirements and the existing Delivery decision remains in force.
<!-- /ANCHOR:questions -->
