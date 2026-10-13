---
title: "Research: User-Story and PM-Story Formats for Cutting Tickets"
description: "Synthesized, cited findings on how the industry formats user stories and project-management stories that get turned into development tickets."
importance_tier: "normal"
contextType: "general"
---

# Research: User-Story and PM-Story Formats

This document summarizes how user stories and project-management (PM) stories are written and turned into developer-ready tickets. It is evidence-based: every URL in the [Sources](#sources) section was fetched during this research run, except those explicitly marked as not reachable. Findings are synthesized with short attributed quotes only; no long passages are reproduced.

The companion `examples/` files turn these formats into copyable, ticket-ready templates.

## 1. The dominant story format: Connextra

The near-universal default is the three-part Connextra template. Mountain Goat Software states it as:

> "As a < type of user >, I want < some goal > so that < some reason >."

Mountain Goat frames the written line as a placeholder rather than a complete specification: "every user story is a placeholder for a future conversation." Atlassian gives the same template in bracketed form — "As a [user], I want [goal] so that [reason]." — and calls a user story "the smallest unit of work in an Agile framework... expressed from the software user's perspective."

The three parts map to role (who), capability (what), and benefit/value (why). Two cautions recur across sources:

- Write the role from the end user's or customer's perspective, not the product owner's. Mountain Goat notes you "don't see any user story, 'As a product owner, I want...'" because the product owner is a stakeholder, not the end user.
- The benefit clause ("so that") keeps the story value-oriented and is what makes it negotiable and testable.

See `examples/connextra-user-story.md`.

## 2. Card, Conversation, Confirmation

Mountain Goat attributes a three-ascept model to Ron Jeffries (2001):

- **Card** — the written description, used for planning and as a reminder.
- **Conversation** — the discussion that fleshes out details.
- **Confirmation** — the tests that show when the story is complete.

Bill Wake reinforces this on XP123: stories in XP have "three components: Cards... Conversation... and Confirmation (tests that verify them)." The practical takeaway for ticketing is that the card text is intentionally incomplete — acceptance criteria and the back-and-forth carry the real specification.

## 3. INVEST: what makes a story "good"

Wake's INVEST acronym (XP123, 2003) is the standard quality checklist for backlog items. Good stories are:

- **I**ndependent — schedulable and implementable in any order.
- **N**egotiable — a starting point for co-creation, "not an explicit contract for features."
- **V**aluable — valuable to the customer; when splitting, "slice vertically through the layers" so each piece delivers value rather than a bare technical layer.
- **E**stimable — understandable and sized well enough to rank and schedule.
- **S**mall — "at most a few person-weeks" of work; smaller stories estimate more accurately.
- **T**estable — you can state how you would confirm it; "requiring customer tests before implementing a story" tends to improve productivity.

Wake pairs INVEST with **SMART** for the tasks a story breaks into: Specific, Measurable, Achievable, Relevant, Time-boxed. The distinction matters for ticketing: a story describes an outcome, while tasks describe activities ("design this, code that, test this").

## 4. Job stories (a situation-first alternative)

Job stories are the main recognized alternative to role-based stories. They shift the opening from *who* the person is to *the situation* they are in, following Jobs-to-be-Done thinking. The widely-reproduced structure is:

- When [situation] ...
- I want to [motivation] ...
- so I can [expected outcome].

This is a real, established format in industry practice. The canonical source is Alan Klement's article on jtbd.info proposing it as a replacement for the role-based story; **that page was not reachable during this research (timed out on repeated attempts), so it is cited below as not reachable and no quotation is reproduced from it.** The structure above is presented as generally known industry convention, not as a fetched quotation.

See `examples/job-story.md`.

## 5. Acceptance criteria: Given-When-Then (Gherkin)

Acceptance criteria are how a story becomes "confirmation." The most codified form is the Gherkin Given-When-Then structure (Cucumber). From the Cucumber Gherkin reference:

- **Given** steps "put the system in a known state before the user... starts interacting" — the preconditions.
- **When** steps "describe an event, or an action" by a person or external system.
- **Then** steps "describe an expected outcome, or result," ideally on an "observable output."

Cucumber recommends 3-5 steps per scenario and warns that outcomes should be observable (e.g., a UI change, report, or message) rather than buried in a database. Supporting keywords let you structure multiple cases cleanly: `Background` for shared preconditions, and `Scenario Outline` + `Examples` table to run one scenario across several data rows.

Mountain Goat calls these high-level acceptance tests "conditions of satisfaction."

See `examples/gherkin-acceptance-criteria.md`.

## 6. Epic-to-story splitting

Epics are large stories that must be decomposed before a sprint. Mountain Goat's guidance is the clearest fetched source:

- Definition: "Story splitting is the practice of breaking a large user story into smaller user stories that still represent meaningful progress toward an outcome."
- Split by value, not by technical layer. Splitting into UI / backend / database / testing stories "rarely helps the team finish anything meaningful" because "nothing can be demonstrated as a working user flow." Instead, cut a vertical slice that delivers a narrower working capability end to end.
- The **SPIDR** prompts offer five ways to find a split: **S**pike (a short investigation), **P**aths (alternate workflow paths), **I**nterfaces (UI/platform/channel), **D**ata (type/amount/source/complexity), **R**ules (business rules/validations/exceptions).
- Sizing signal: the "90% syndrome" — "software is 90% done for 90% of the schedule." Be wary of bringing a story into a sprint if it could consume half or more of the sprint.
- Split collaboratively, roughly two sprints ahead, during backlog refinement. Product Owners bring outcomes; developers bring technical knowledge of where the real complexity sits.

See `examples/epic-splitting.md`.

## 7. Definition of Ready and Definition of Done

These two shared checklists gate the lifecycle of a story. Both definitions come from the fetched Atlassian pages.

**Definition of Ready (DoR):** "allows you to evaluate work before your team starts on it." It defines what a backlog item needs so the team can act immediately — e.g., a clear description, acceptance criteria written, dependencies identified, sized, and small enough for a sprint.

**Definition of Done (DoD):** "a set of criteria that a product increment must meet for the team to consider it complete and ready for customers." Atlassian stresses it is team-owned and a living document, and draws a sharp line from acceptance criteria: "the definition of done is not the same thing as acceptance criteria." The DoD is a team-wide quality bar (e.g., code reviewed, tests added, deployed to staging); acceptance criteria describe the specific behavior of one story.

See `examples/definition-ready-done.md`.

## 8. How mainstream trackers structure ticket-ready stories

Trackers do not invent a new story format — they wrap the formats above in structured fields and a hierarchy.
