# Doc Mode Teachings — Panel Synthesis

Three independent reviewers (GPT 5.6 Sol high fast, GLM 5.2 max, Fable 5 high via the claude2 account, all read-only) analyzed the Public README, the sk-doc create-readme packet and the sk-doc shared quality backbone, then gap-analyzed Product Owner Doc Mode v0.102. Full reports: `report-sol.md` (241 lines), `report-glm.md` (162), `report-fable-5.md` (123).

## Unanimous verdicts

All three agree on the same asymmetry, stated sharpest by Fable: the teaching sources have **measurement**, Doc Mode has **epistemics**. Doc Mode's source-safety architecture (five claim classes, scoped authority, conflict hold, refinement fidelity) is stronger than anything in the teaching sources and must not be touched. What Doc Mode lacks is output-facing quality machinery.

## Convergent recommendations (all three reviewers, or two with no dissent)

1. **Opening contract per shape** (Sol 2, GLM R1, Fable R4). The first screen must let a no-context reader answer "what is this, who is it for, do I need it". Each shape gets a 2-3 sentence contract for what its opening establishes. Only Narrative overview has this today. Effort small.
2. **Include-When section contracts** (Sol 4, Fable R1). Replace "omit optional sections" prose with a 2-column `Section | Include when` table per shape. Converts template-completion bias into a checkable rule. Effort medium.
3. **Two-register voice rule** (Sol 3, GLM R3, Fable R6). Name the narrative register (full sentences, why-before-what: overviews, rationale, history) and reference register (definition bullets, tables, identifiers: enumerable content), assign them per shape, and state that a section switches register, never a paragraph mid-thought. Effort small.
4. **Reader-simulation questions in the quality check** (Sol 7, GLM R2, Fable R5). One question per shape answered against the draft (Guide: can the audience complete the process without another document? Proposal: could a candidate item be mistaken for shipped behavior on a skim?). The only check type that tests the artifact against the reader's job. Effort small.
5. **Narrative overview completion** (Sol 8, Fable R3). The fifth shape has no worked example (4 fixtures for 5 shapes), no Quick adaptation block. A `doc-example-narrative-overview.md` fixture plus a Quick block. Effort medium, carries one new mirror.
6. **Expected-result convention for procedural Guides** (Sol 6, Fable R7). Verification-bearing steps carry a source-backed expected result or an explicit unverified flag. Imports the install-guide checkpoint idea without the 5-STOP-block quota. Effort small.
7. **Dimensioned quality verdict in the response** (Fable R2, Sol 5). Define the currently-undefined "compact quality summary" as one pass/attention line per dimension (source safety, shape fit, layout, readability, voice). Reporting contract, no numeric scores, no scripts. Effort small-medium.
8. **Output-verification checklist items** (GLM R2, GLM R7). Add artifact-facing checks (takeaway-first sections hold, no scaffold text or `{...}` placeholders survive export) beside the existing process checks. Effort small.

## Divergent or single-voice items

- **Shape selection decision tree** (GLM R4 only): deterministic routing when a request fits two shapes. Cheap, plausible.
- **Named table patterns** (GLM R5): name the three 2-column patterns already in use (Index, Options and trade-offs, Conditions and outcome). Cheap.
- **Analogy budget + personality pointer for Narrative overview** (GLM R6): connects existing HVR personality rules to the prose-first shape. Cheap.
- **FAQ as an earned element** (Fable R8, Sol 7 variant): only when sources show repeated questions.
- **Example table reshaping** (Sol 1): catalog and proposal fixtures carry 5-column tables. CONFLICT: an earlier phase-001 decision exempted fixture-mandated ClickUp scaffold matrices from the 2-column rule. Sol's reshape (labeled line breaks inside a 2-column table) is workable but reverses that decision. Needs an owner call, not a silent fix.

## Do NOT import (unanimous)

TOC and ANCHOR comments (ClickUp noise, forbidden by the teaching packet itself), numbered ALL-CAPS headings / `---` / `&nbsp;` (competing layout grammar), DQI mechanical point sources (word counts reward bulk and would fight adaptive shapes), the script validation pipeline (cannot run in the claude.ai mirror, splits the dual package), quantified content floors (fabrication pressure under source-safety rules), marketing openers and badges, frontmatter on export artifacts, and sk-doc's HVR copy (the PO already holds the canonical superset).

## Defects found and already fixed

Fable found two stale enumerations from the v0.101 rollout, both verified and fixed in place (mirrors resynced): `doc-templates.md` §8 said "Quick uses the same four shapes" and `doc-mode.md` §12's recovery question omitted Narrative overview.

## Suggested implementation order

Wave 1 (small, high leverage): opening contracts, two-register rule, reader-simulation questions, output-verification items, expected-result convention, quality verdict definition. Wave 2 (medium): include-when tables, Narrative overview fixture + Quick block. Wave 3 (owner decisions): example table reshaping vs the fixture exemption, decision tree, table patterns, analogy budget, FAQ element. Cross-mode wave: the four small suggestions each reviewer listed (task include-when, bug expected-vs-actual per step, story reader question, interactive three-slot fallback).
