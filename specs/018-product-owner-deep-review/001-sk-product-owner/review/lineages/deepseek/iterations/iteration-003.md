# Review Iteration 003 — Maintainability (templates and examples)

- Session: `fanout-deepseek-1792580414886-kf3maf` (generation 1, lineageMode new)
- Iteration: 3 of 5
- Dimension: maintainability
- Stop policy: `max-iterations` (convergence is telemetry only)
- Review target: `AI Systems/Product Owner/sk-product-owner`

## Files Reviewed

- `AI Systems/Product Owner/sk-product-owner/assets/story-template.md:20-90` — house-format Story scaffold.
- `AI Systems/Product Owner/sk-product-owner/assets/epic-template.md:38-126` — Epic scaffold and optional Delivery close.
- `AI Systems/Product Owner/sk-product-owner/assets/task-templates.md:36-226` — canonical task, parent task and subtask scaffolds.
- `AI Systems/Product Owner/sk-product-owner/assets/bug-report-template.md:53-141` — bug scaffold.
- `AI Systems/Product Owner/sk-product-owner/assets/doc-templates.md:672-777` — quick adaptation, refinement overlay, source-conflict hold, template quality check.
- `AI Systems/Product Owner/sk-product-owner/assets/interactive-response-templates.md:152-207` — Delivery Reply Shape, line order, Open items grammar.
- `AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:377-420` and `references/story-mode.md:353-400` — delivery standards and the nested-task bundle.
- All 22 worked examples under `assets/examples/{bug,doc,story,task}`, measured for word count outside code fences and scanned for bullet, checkbox and divider grammar.
- `AI Systems/Product Owner/sk-product-owner/references/routing.md:1-12` — preamble fields.
- `AI Systems/Product Owner/sk-product-owner/references/quality-scoring.md:106-190` — the imported index blocks.

## Findings by Severity

### P0 Findings

None.

### P1 Findings

None raised this iteration. Two P1 findings from iterations 1 and 2 remain active and keep this iteration's verdict at CONDITIONAL.

### P2 Findings

1. **Three worked examples break the packet's own word caps** -- `AI Systems/Product Owner/sk-product-owner/assets/examples/doc/doc-example-how-it-works.md:10` -- `SKILL.md:175` (ALWAYS 17) caps a Doc or Story at 1,400 words counted outside code blocks, and allows an overage only "when supplied values, requirements or criteria need the room". Measured outside code fences: `doc-example-how-it-works.md` is 2,313 words (65% over), `doc-example-behavior-reference.md:10` is 1,641 (17% over) and `story-example-complete.md:12` is 1,519 (8% over). The other 19 examples sit inside their caps (task 705/900, subtask 578/750, bug 580/800, epic 986/1,000, story 1,025/1,400). Because the examples are the imitation target — `assets/interactive-response-templates.md:156` states that "Models copy a worked reply more closely than they follow a rule" — an over-cap example teaches the breach it is meant to illustrate. Doubt stated: the three may carry supplied values that the rule exempts, but two of them are authored reference documents with no supplied source in sight.

```
Finding class: example-budget
Scope proof: Every example in the declared target measured by the same method; only these three exceed their cap.
Affected surface hints: assets/examples/doc/doc-example-how-it-works.md, assets/examples/doc/doc-example-behavior-reference.md, assets/examples/story/story-example-complete.md (fix targets), SKILL.md:175 (the cap they break)
Case: A model learns the Doc shape from doc-example-how-it-works.md and ships a 2,300-word guide, then fails the packet's own cap check with no rule to appeal to.
```

2. **The router contract repeats its own opening paragraph and its Section 1 payload** -- `AI Systems/Product Owner/sk-product-owner/references/router-contract.md:33` -- The sentence "The Smart Router expressed as running Python, one level below the prose routing rules in `../SKILL.md` Section 2 and `routing.md`…" appears at `:17` and again verbatim at `:33`, and the preamble block at `:20-26` (Loading Condition through Hands Off To) is immediately followed by `## 1. OVERVIEW` whose Purpose section restates the same sentence a third time. Every edit to that claim has to be made in two places, and the file already carries one drifted claim (iteration 2, P1), which is what duplicated authority costs in practice.

```
Finding class: duplicated-text
Scope proof: Both occurrences are in the same file inside the declared target.
Affected surface hints: references/router-contract.md (fix target)
Case: A maintainer corrects the "never drifts" claim in one of the two opening paragraphs and ships a file that contradicts itself.
```

3. **The quality rubric carries kernel-owned index fragments, including a delivery-prohibition list that starts at item 7** -- `AI Systems/Product Owner/sk-product-owner/references/quality-scoring.md:183` -- Four blocks in this reference are written from the kernel's point of view and point outward: ":106 The kernel points here for the six-dimension gate", ":139 … for these gate behaviours", ":143 … for the pre-reply quality checklist", ":183 … for these delivery prohibitions". The last block then lists only items `7.`, `8.` and `9.` (:184-187) with no items 1-6 anywhere in the file, so the enumeration is unreachable in the skill runtime and unverifiable without opening the kernel. The same paragraphs also carry the Project-only delivery wording recorded as iteration 1's P1; this finding covers the maintainability defect — wrong authorship and a dangling enumeration — not that contradiction.

```
Finding class: mixed-authorship
Scope proof: All four blocks are inside the declared target; the kernel was read only to establish that items 1-6 live there.
Affected surface hints: references/quality-scoring.md (fix target: keep the rubric, drop or relink the kernel pointers)
Case: A maintainer counts the quality gates in this file and finds three numbered prohibitions belonging to a list whose first six items exist only in another packaging.
```

4. **The routing reference omits the preamble fields the packet requires of every reference** -- `AI Systems/Product Owner/sk-product-owner/references/routing.md:1` -- `SKILL.md:227` sets the standard: "Every reference and asset opens on Loading Condition, Purpose, Scope and Output Path." `references/routing.md` carries a frontmatter block and an opening paragraph but none of the four fields, while the other eleven packet-authored references and all six assets carry all four. `references/human-voice-rules.md` also omits three of them, but `SKILL.md:215` declares that file a copy that is "never edited from this system", so it is exempt; routing.md is authored here and is not.

```
Finding class: doc-standard-gap
Scope proof: Field presence checked across all 13 references and 6 assets in the target; only routing.md and the declared external copy fail.
Affected surface hints: references/routing.md (fix target), SKILL.md:227 (the standard)
Case: A reader scanning reference preambles to learn what loads and what it writes finds routing.md silent while every sibling answers, and files a bug against the standard instead.
```

## Traceability Checks

| Protocol | Level | Status | Evidence |
|----------|-------|--------|----------|
| `spec_code` | core | partial | `specs/product-owner/018-product-owner-deep-review/001-sk-product-owner/spec.md:7` asks whether "templates agree with the rules that govern it, and examples obey the templates"; this iteration answers it with 22 example measurements and six scaffold reads. |
| `checklist_evidence` | core | fail | Carried from iteration 2: the drift invariant at `SKILL.md:44` still fails. Iteration 3 adds no new checklist failure. |
| `skill_agent` | overlay | partial | `SKILL.md:227`'s preamble standard was tested against every reference and asset; one authored reference fails. |
| `agent_cross_runtime` | overlay | notApplicable | No runtime mirror inside the target. |
| `feature_catalog_code` | overlay | notApplicable | No feature catalog in this packet. |
| `playbook_capability` | overlay | deferred | Playbook scenario-to-capability mapping is iteration 5's focus. |

## Integration Evidence

- `assets/interactive-response-templates.md:156` is cited as the packet's own statement of why example fidelity outranks prose rules, which is what raises the word-cap overage from cosmetic to behavioral.
- `references/doc-mode.md:377-404` and `references/story-mode.md:353-390` restate the delivery standards by reference rather than re-deriving the reply shape, so the single-shape rule at `assets/interactive-response-templates.md:152-154` holds.

## Edge Cases

- **Epic template `##   ` spacers.** `assets/epic-template.md:55`, `:64` and `:112` carry spacer headings with only whitespace after the hashes. That is the documented house grammar (`references/story-mode.md:215` and `SKILL.md:193` refer to a `##   ` spacer), not a malformed heading. Ruled clean.
- **Task template `---` density.** `assets/task-templates.md` uses 13 `---` dividers inside the canonical task scaffold. `SKILL.md:168` requires `---` between required Task and Bug sections, and NEVER 12 restricts dividers only in new Doc artifacts. Consistent.
- **Doc template quality check uses `- [ ]`.** `assets/doc-templates.md:753-763` is an author checklist under Section 11, not artifact content, so the `[]`-without-space rule for delivered checkboxes does not reach it. Not a finding.

## Confirmed-Clean Surfaces

- Every Doc example uses `*   ` bullets and `* * *` dividers with zero hyphen bullets and zero body `---` dividers; every Story example uses `*   ` prose bullets and `- []` only for requirement items, exactly as `SKILL.md:168` requires.
- No worked example ends a bullet with a full stop, in any of the four modes.
- Story H1s all follow `{Persona or platform} - {Area or initiative} - {Feature}` and the Epic example follows `Epic - {Persona or platform} - {Area or initiative}`, as `references/story-mode.md:362` sets out.
- The Story scaffold's section order, `**Expected outcomes**` label, `#### **References**` H4, `- []` requirements, `1 )` acceptance numbering and no-divider Mark-as-done rule all match `references/story-mode.md:205-215`.
- The Epic scaffold's `## About` umbrella with `#### Problem` / `#### Goal` / `#### Solution` / `#### **References**`, then `## Scope` and an optional `#### Added Later`, matches `references/story-mode.md:210` and carries no `## Requirements`.
- The Delivery Reply Shape's seven-line order (`assets/interactive-response-templates.md:158-166`) is the only place the order is defined; `references/doc-mode.md:403-407` and `references/story-mode.md:353-390` point at it rather than restating it.
- The manual-testing playbook's internal arithmetic is consistent: 8 tasks + 3 bugs + 5 stories + 4 epics + 4 docs + 1 flow = 25 per set, two sets = 50, and the twelve category folders it names are the six `project-*` plus six `skill-*` folders on disk.

## Ruled Out

- **Six-dimension duplication between `SKILL.md` and `references/quality-scoring.md`.** `SKILL.md:252-259` is a floor table that routes to the rubric for definitions, not a second authority. Ruled out.
- **`[ ]` spacing inside bug and task scaffolds.** Neither scaffold contains a spaced checkbox; the only occurrences are the Doc author checklist noted above. Ruled out.
- **Example count guidance.** `SKILL.md:223` says "four to seven per mode"; the folder counts are bug 4, task 5, story 5 and doc 7. Ruled out.

## Next Focus

- Dimension: security
- Focus area: secrets handling for the ClickUp push targets, the packet's treatment of untrusted pasted material, and the router's path guard
- Reason: iterations 1-3 covered correctness, traceability and template consistency; the packet reads environment values, accepts pasted tickets and attachments, and hands text to an external system, none of which has been examined against exposure or injection risk
- Rotation status: correctness, traceability and maintainability covered; security next, playbook capability at iteration 5
- Required evidence: `[SOURCE: path:line]` for each exposure or guard
- Recovery note: none

---

Review verdict: CONDITIONAL
