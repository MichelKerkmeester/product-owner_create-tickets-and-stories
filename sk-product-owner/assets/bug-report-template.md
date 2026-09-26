---
title: "Product Owner Bug Report Template - v0.101"
description: "Copy/apply template for Product Owner bug reports with evidence, reproduction and QA handoff."
version: "0.101"
contextType: asset
importance_tier: high
trigger_phrases:
  - "bug report template"
  - "defect evidence template"
  - "steps to reproduce"
  - "expected behavior template"
  - "QA handoff checklist"
---

# Product Owner Bug Report Template - v0.101

Copy/apply template for isolated Product Owner bug reports.

**Loading Condition:** CONDITIONAL, with `references/bug-mode.md` whenever Bug intent is selected
**Purpose:** Provides the bug report scaffold a new defect report is copied from
**Scope:** Context, observed and expected behavior, reproduction steps, the evidence fields and the QA handoff checklist
**Output Path:** `export/[###] - bug-[description].md`

---

## 1. OVERVIEW

### Purpose

Provides a reusable markdown scaffold for defect reports that need observed behavior, reproduction steps, expected behavior and QA handoff criteria.

### Usage

Load this asset with Bug Mode. Copy the template, fill only user-supported facts, write `Not provided` where required details are missing and remove conditional comments before delivery. Do not end a newly authored or rewritten bullet item with a full stop.

### Frequency

`Frequency` records what the source states about how often the bug occurs. It is not derived from a count. The allowed values are `Always`, `Sometimes`, `Rarely` and `Not provided`, and the inference the field permits stops here:

- `Always` needs the source to say it happens every time, or evidence that reproduced on every attempt across more than one account, device or session
- `Sometimes` needs the source to call the bug intermittent, or to describe both a failing and a passing attempt of the same action
- `Rarely` needs the source to say it is rare. Nothing else supports it
- `Not provided` is the answer for everything else, including a raw count with no frequency claim attached to it

Raw counts do not convert. Three support tickets are three reports, not a frequency, and they may not even be the same defect. Two failures in five attempts is `Sometimes` only when the source calls it intermittent, and otherwise stays `Not provided` with the count preserved in Observed Behavior where a reader can weigh it. When a count genuinely supports the label, keep it in the cell beside the label rather than discarding it, as in `Always (reproduced on two separate accounts, per reporter)`.

### Design evidence with no link

A Figma comparison, a design review or a spec walkthrough supplied without a shareable URL is still evidence, and dropping it loses the only account of what the bug was measured against. Record it under `**Design review**` in References as one line naming what was reviewed, which screen or frame it covers, and who reviewed it when known, closed with `(link not provided)`. Never fabricate a Figma destination to make the reference resolve, and never move the review into prose where a reader scanning References will miss it.

---

## 2. BUG REPORT TEMPLATE

Worked example: [`examples/bug/bug-example-frontend-visual.md`](examples/bug/bug-example-frontend-visual.md) shows a visual stacking defect supported by cross-browser evidence, exact design tokens and a focused BDD scenario.

Worked example: [`examples/bug/bug-example-mobile-crash.md`](examples/bug/bug-example-mobile-crash.md) shows crash-log evidence and an explicitly labelled memory-pressure hypothesis instead of an asserted root cause.

Worked example: [`examples/bug/bug-example-backend-api.md`](examples/bug/bug-example-backend-api.md) shows a concurrency-sensitive API defect with paired request evidence and conditional reproduction.

Worked example: [`examples/bug/bug-example-quick.md`](examples/bug/bug-example-quick.md) shows the compact form, honest missing environment data and an unverified route hypothesis.

````markdown
# {Bug Title}

### About

---

{1-2 sentence description of the bug and where it occurs in the application.}

| Field           | Value                                     |
| --------------- | ----------------------------------------- |
| Frequency       | {Always / Sometimes / Rarely / Not provided} |
| Severity        | {Critical/High/Medium/Low}    |
| Platform        | {iOS/Android/Web}             |
| Device          | {Device name/model}           |
| OS Version      | {OS version}                  |
| Browser         | {Browser name - if web}       |
| Browser Version | {Browser version - if web}    |

**References:**

**Flows**
- [{Flow name}]({figma-url})

**Components**
- [{Component name}]({figma-url})

**Design review**
- {What was reviewed, on which screen or frame, and by whom when known} (link not provided)

---

### Bug

---

**1. Observed Behavior**

---

{ Describe what happens when the bug is triggered }
- { What the user sees }
- { Any error message the ticket, log or user supplied. With none supplied, write `Not provided` or leave this line out, never that no error message appears }
- { Incorrect data or behavior }

Steps to Reproduce:
1. { First action to take }
2. { Second action to take }
3. { Third action to take }
4. { Continue until bug is triggered }
5. { Observe the bug }


{ Screen Recording }



---

**2. Expected Behavior**

---

{ Describe what should happen instead. }
- { Design specifications }
- { Previous working behavior }
- { User expectations }

Checklist
- [ ] Root cause identified
- [ ] Fix implemented
- [ ] Bug no longer reproducible
- [ ] No regressions introduced

---

<!-- IF BDD applicable -->
### BDD Scenarios

---

**Scenario:** [Bug behavior scenario]
- **Given** [precondition describing the buggy state]
- **When** [action that triggers the bug]
- **Then** [expected correct behavior after fix]

<!-- END IF -->

````
