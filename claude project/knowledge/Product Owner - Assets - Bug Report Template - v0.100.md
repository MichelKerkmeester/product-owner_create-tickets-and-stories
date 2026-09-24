# Product Owner - Assets - Bug Report Template - v0.100

The scaffold an isolated bug report is copied from, with the Frequency rules, the design-evidence rule and the QA handoff checklist that govern how it is filled.

---

## 1. OVERVIEW

### Purpose

Provides a reusable markdown scaffold for defect reports that need observed behavior, reproduction steps, expected behavior and QA handoff criteria. It holds the context block, the observed and expected behavior sections, the reproduction steps, the evidence fields and the QA handoff checklist.

### Usage

Use this scaffold with the Bug Mode document, which holds the wider Bug rules. Copy the template, fill only user-supported facts, write `Not provided` where required details are missing and remove conditional comments before delivery. Do not end a newly authored or rewritten bullet item with a full stop.

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

Four worked examples instantiate this scaffold:

- **Examples - Bug - Frontend Visual** shows a visual stacking defect supported by cross-browser evidence, exact design tokens and a focused BDD scenario
- **Examples - Bug - Mobile Crash** shows crash-log evidence and an explicitly labelled memory-pressure hypothesis instead of an asserted root cause
- **Examples - Bug - Backend API** shows a concurrency-sensitive API defect with paired request evidence and conditional reproduction
- **Examples - Bug - Quick Bug** shows the compact form, honest missing environment data and an unverified route hypothesis

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
- { Any error messages displayed }
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
