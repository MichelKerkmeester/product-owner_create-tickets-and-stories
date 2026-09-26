---
title: "Product Owner - Templates - Bug Mode - v0.205"
description: "Product Owner bug-mode workflow, delivery standards and QA handoff rules for defect reports."
version: "0.205"
contextType: reference
importance_tier: high
trigger_phrases:
  - "bug mode"
  - "$bug defect report"
  - "reproduction steps"
  - "observed expected behavior"
  - "bug evidence QA"
---

# Product Owner - Templates - Bug Mode - v0.205

Bug-mode guidance for isolated defects. The workflow captures context, observed behavior, reproduction steps, expected behavior and the QA checklist needed before handoff.

**Loading Condition:** ON-DEMAND
**Purpose:** Provides bug-mode workflow, standards and QA handoff rules for isolated defects when `$bug`, `$b`, `bug report`, `defect`, `broken` or similar language is detected
**Scope:** Bug mode overview, delivery standards, quality checklist, error recovery and bug report template usage pointer
**Output Path:** `export/[###] - bug-[description].md`
**Loads With:** `assets/bug-report-template.md` as the paired scaffold, beside the always-loaded `references/hvr-core.md` and `references/conciseness.md`
**Routed By:** `$bug`, `$b`, bug framing, symptom wording that names no defect noun, and the bug semantic topic. UI feedback carrying fix language routes to Task Mode instead, because this mode is reserved for unexpected system behavior
**Hands Off To:** `references/interactive-mode.md` when evidence or reproduction steps are too thin to write from outside Quick energy, which returns here once the user answers

---

## 1. OVERVIEW

### Purpose

Provides the bug-mode workflow, delivery standards and QA handoff rules for isolated defects. Bug Mode creates bug reports with context, reproduction steps and a QA checklist, always delivered as a `text/markdown` artifact and processed at Standard energy unless the user explicitly requests another mode.

### When to Use

Use Bug Mode for:
- Isolated, standalone bug reports
- Bugs requiring detailed reproduction steps
- Bugs with clear observed behavior and expected behavior
- Bugs supported by screenshots, screen recordings, logs or design references

Use Task Mode instead for:
- Grouped bugs or refinement tasks
- Bug consolidation tickets
- Bug fixes combined with feature work
- Tasks titled `Refinement + Bugs`

### Command: `$bug`

- **Short Alias:** `$b`
- **Purpose:** Create bug reports with context, reproduction steps and QA checklist
- **Output:** Always as `text/markdown` artifact
- **Thinking:** Standard energy unless the user explicitly requests another mode
- **Interactive Mode:** Handled by Interactive Mode file when the issue details are too ambiguous
- **Structure:** Fixed bug report structure with flexible evidence placement
- **Key Feature:** Uses `About`, `Bug` and optional `BDD Scenarios`

### Critical rules

- Do not create an artifact until the user responds to the comprehensive question unless the request carries no command and contains enough bug context to proceed. An explicit command routes the request and does not stand in for the direction, so `$bug` and `$b` still ask their context-specific question and wait. Only `$quick` or `$q` may skip routine intake
- Do not answer your own questions when clarification is required
- Stopping to ask still produces a file. Export the question as `export/[###] - bug-[description]-clarification.md`, holding the question and nothing else, so the request is not lost between sessions. The artifact takes the next number in the lane once the user answers
- Do not include a table of contents in generated bug reports
- Keep one bug per report unless the user explicitly requests grouped bugs
- Preserve the fixed template order
- Capture screenshots, screen recordings, logs and references where they fit the reported bug
- Do not invent missing details. Use `Not provided` when a field matters but no value was supplied
- Keep the checklist exactly as defined in the template
- Stay in WHAT and WHY, not HOW

### Difference from Task Mode

- **Structure**
  - Task Mode: Auto-scaled by task complexity
  - Bug Mode: Fixed bug structure
- **Requirements**
  - Task Mode: Variable feature requirements
  - Bug Mode: Observed behavior and expected behavior
- **Evidence**
  - Task Mode: Optional inline support
  - Bug Mode: Included where provided
- **Checklist**
  - Task Mode: Task-specific acceptance requirements
  - Bug Mode: Fixed QA checklist before handoff
- **Quick Mode**
  - Task Mode: Supported for quick tasks
  - Bug Mode: Supported. Quick is an energy override rather than an intent, so it narrows a Bug artifact the same way it narrows a Task
- **BDD**
  - Task Mode: Often used for feature behavior
  - Bug Mode: Optional when it clarifies the bug flow

### Note on feature requests

For feature development or enhancements, use `$task` and reference **Templates - Task Mode**.

---

## 2. DELIVERY STANDARDS

### Universal requirements

- **Artifact Type:** Always use `text/markdown`, never `text/plain`
- **Single Artifact:** Deliver the complete bug report as one artifact
- **Energy Processing:** Apply the detected energy level's rigor and perspective minimums
- **Template Compliance:** Use the structure exactly
- **No Anchors in Output:** Never include `<!-- ANCHOR -->` comments in generated deliverables. Conditional comments in the template are template-internal only

### Bug-specific standards

- **Fixed Structure:** All bugs use the same About and Bug section structure
- **Output Focus:** Only deliver what the user reported
- **No Scope Expansion:** One bug per report unless the user explicitly asks for a multi-bug artifact
- **Evidence Placement:** Put screen recordings, screenshots and logs inside the Bug section near the reproduction context
- **Root Cause Tracking:** Keep root cause identification as a checklist item before QA handoff

### Mandatory structure elements

#### Section hierarchy

- **H1:** Bug title only
- **H2:** `About`. **H3:** `Bug` and optional `BDD Scenarios`
- **Bold numbered labels:** `1. Observed Behavior` and `2. Expected Behavior` inside `### Bug`

#### Structure order

1. Title as `# {Bug Title}`
2. `## About` with short description, field table and references
3. `### Bug`
4. `1. Observed Behavior`
5. `Steps to Reproduce:`
6. Screen recording or relevant visual evidence
7. `2. Expected Behavior`
8. Checklist
9. Optional `### BDD Scenarios`

#### Formatting standards

- Use `---` between major sections and template blocks
- Use `-` for bullets
- Use `- []` for checklist items, with no space between the brackets
- Use numbered lists for reproduction steps
- Use fenced code blocks for logs or error messages when needed
- Use inline images for screenshots when available
- Do not include a generated table of contents
- Do not end checklist or bulleted list items with `.`

### Content guidelines

**About section:**
- Describe the bug and where it occurs in 1-2 sentences
- Include the field table with frequency, severity, platform, device, OS, browser and browser version
- Add flow and component references when provided
- Add a `**Design review**` line when a design comparison was the evidence and no link was supplied

**Bug section:**
- Describe what happens when the bug is triggered
- List what the user sees, any error message the ticket, log or user supplied and incorrect data or behavior. With no error message supplied, the line reads `Not provided` or is left out, and it never asserts that no error message appears
- Include reproducible steps
- Include screen recording, screenshots or logs when provided
- Describe what should happen instead
- Include design specifications, previous working behavior and user expectations when known

**Checklist:**
- Keep the four fixed checklist items exactly as written
- Do not add implementation tasks to the checklist
- Treat the checklist as the QA handoff gate

**BDD Scenarios:**
- Include this section only when it clarifies the user flow or expected state
- Remove the conditional comments from generated bug reports
- Use Given/When/Then format

### Assumptions

- Never add `[Assumes: ...]` in bug exports
- If uncertainty matters, write it plainly as `Not provided` or place it in the relevant field

---

## 3. QUALITY CHECKLIST

### Pre-creation validation

- [ ] Detected energy level's rigor and perspective minimums applied?
- [ ] User provided enough issue context or responded to the comprehensive question?
- [ ] Bug description clear and specific?
- [ ] Location, screen or flow identified when available?
- [ ] Scope limited to the reported defect?

### Structure validation

- [ ] Title uses H1 and appears first?
- [ ] About section uses `## About`?
- [ ] About section includes the field table?
- [ ] References appear under About when provided?
- [ ] Bug section uses `### Bug`?
- [ ] Observed Behavior appears before Expected Behavior?
- [ ] Steps to Reproduce uses a numbered list?
- [ ] The decisive reproduction step pairs expected with actual when the evidence supplies both?
- [ ] Checklist includes the exact four required items?
- [ ] Optional BDD section is included only when useful?

### Format validation

- [ ] Using `text/markdown` artifact type?
- [ ] Lists use `-` bullets?
- [ ] Checkboxes use the `- []` format?
- [ ] Dividers use `---`?
- [ ] No generated table of contents?
- [ ] No template-internal comments remain in generated output?

### Bug-specific validation

- [ ] Observed behavior describes what happens when the bug is triggered?
- [ ] Observed behavior describes what the user sees?
- [ ] Supplied error messages are included, and with none supplied the line reads `Not provided` or is left out rather than asserting that none appears?
- [ ] Incorrect data or behavior is described?
- [ ] Steps are numbered and reproducible?
- [ ] Screen recording, screenshots or logs are included when provided?
- [ ] Expected behavior states what should happen instead?
- [ ] Design specifications are included when provided?
- [ ] Previous working behavior is included when known?
- [ ] User expectations are included?
- [ ] Root cause tracking remains in the checklist?

---

## 4. ERROR RECOVERY

### Missing steps to reproduce

Add a numbered list of exact steps to trigger the bug. If the user did not provide every step, use only the steps directly supported by the reported flow. When the evidence supplies it, pair the decisive step with what was expected and what actually happened, so the steps are self-verifying rather than narrative. Never invent an expected result the evidence does not support.

### Vague observed behavior

Replace vague wording with specific user-visible behavior. Describe the screen state, missing data, stale state, incorrect action or error message.

### Missing screen recording

Write `Not provided` in the screen recording area when a recording matters but was not supplied.

### Missing screenshots or logs

Include screenshots or logs when provided. Do not create a separate Evidence section. Place evidence in the Bug section near the reproduction context.

### Wrong section structure

Update the report to use `## About`, `### Bug` and optional `### BDD Scenarios`.

### Missing environment table values

Use `Not provided` for unknown field table values. Do not invent platform, device, OS or browser data.

### Frequency inferred from a count

`Frequency` reports what the source says about recurrence, never what a count implies. `Always` needs an every-time claim or a reproduction that held on every attempt across more than one account, device or session. `Sometimes` needs the source to call the bug intermittent, or to show a failing and a passing attempt of the same action. `Rarely` needs the source to say rare. Everything else is `Not provided`, with the count kept in Observed Behavior. Three tickets are three reports, not a frequency, and they may not be one defect. **Fix:** restore `Not provided` and move the count into Observed Behavior, or keep the count in the cell beside a label the source actually supports, as in `Always (reproduced on two separate accounts, per reporter)`.

### Design review supplied without a link

A Figma comparison or design review with no shareable URL is evidence, and it belongs in References under `**Design review**`: what was reviewed, which screen or frame, who reviewed it when known, then `(link not provided)`. **Fix:** add the line rather than fabricating a Figma destination or dropping the evidence into prose.

### Implementation drift

Remove solution instructions. Keep the report focused on what is broken, how to reproduce it and what outcome must be true after the fix.

---

Templates: see **Assets - Bug Report Template**.

---

## 5. FINAL REMINDERS

1. Keep the About and Bug structure fixed
2. Preserve user-provided screenshots, screen recordings, logs and Figma references
3. Use `Not provided` for unknown field values instead of inventing details
4. Keep the checklist as the fixed QA handoff gate
5. Remove template comments from generated bug reports
6. Stay in WHAT and WHY, not HOW
