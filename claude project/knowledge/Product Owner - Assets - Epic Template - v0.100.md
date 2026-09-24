# Product Owner - Assets - Epic Template - v0.100

An Epic frames an initiative and delegates requirements to its child stories.

---

## 1. OVERVIEW

### Purpose

Same grammar and the same opt-in `## Delivery` close as a Story, with three differences: `### Goal` replaces `#### **Expected outcomes**`, `## Scope` replaces `## Requirements`, and the acceptance criteria stay at release level.

### Usage

Use this scaffold together with Story Mode guidance. The shared house grammar, the artifact-kind selection and the optional enrichments live in the Story Mode reference.

---

## 2. EPIC TEMPLATE

```markdown
# Epic - {Persona or platform} - {Area or initiative}

* * *
## About
* * *
{Epic-level narrative: the product change and that it is split into several child stories.}

### Problem
* * *
{The current problem and why it matters.}

**The following issues rise from that:**
*   {Observable failure}
*   {Observable failure}
###   

### Goal
* * *
{The primary product or business goal.}

**Direct user/Barter benefits:**
*   {Direct benefit}
*   {Direct benefit}
###   

### Solution
* * *
In order to get there, we will:
*   {High-level direction}
*   {High-level direction}

#### **References**
* * *
{Supplied links only.}
Components
*   [{link}]({url})
Flows
*   [{link}]({url})

## Scope
* * *
Each child story owns one part of the lifecycle and carries its own detailed requirements and acceptance criteria.

#### {Scope group}
* * *
*   [{Child story}]({url})
*   {Child story named as plain text, when no link exists yet}

#### Added Later
* * *
{Capabilities that belong to the epic but do not block the first release.}

**{Capability}**
*   {What it will do}
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1\. **{Release-level outcome}**
* * *
*   **Given** {release-level precondition}
*   **When** {a completed capability or cross-story event}
*   **Then** {observable release outcome}
*   **And** {additional outcome, only when needed}
* * *
- [ ] _Mark as done, if the criteria are met_
* * *
##   
```

### Notes For Use

- An Epic has **no** `## Requirements` section by default. Add requirements only when the supplied epic carries genuine standalone scope that no child story owns. Keep them in the Story shape's bold-lead hard-constraint form and flag why they live at epic level
- `## Scope` lists the child stories grouped by lifecycle part, with an optional `#### Added Later` group for capabilities that do not block the first release
- A first-drafted Epic usually has no child-story links at all, because the stories do not exist yet. That is the normal case and it does not block the Scope section. Name each intended child story as plain text in its own `*   ` bullet, written in the shape its Story H1 will take (`{Persona or platform} - {Area or initiative} - {Feature}`), and add the link when the story is created. Never invent a ClickUp or Figma URL to make a bullet look finished, and never drop a child story because it has no link. A group that mixes linked and unlinked bullets is normal and needs no explanatory note
- Release-level acceptance criteria describe outcomes a completed release guarantees. Screen-level detail belongs in the child stories
- The Mark-as-done checkbox is the final line of each criterion block. Start the next criterion after one blank line and no divider. The last criterion in the section is the exception: a `* * *` closes Acceptance criteria on the line above the `##   ` spacer, exactly as the `#### Added Later` group's last bullet is closed before Scope's spacer

---

## 3. OPTIONAL DELIVERY CLOSE

Append this block only when the requester asked for a delivery view, or when a requirement carries an `**Open:**` line or an undated external constraint forces one. Otherwise the scaffold above is the whole artifact and its trailing `##   ` spacer is the last line of the file.

```markdown
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
