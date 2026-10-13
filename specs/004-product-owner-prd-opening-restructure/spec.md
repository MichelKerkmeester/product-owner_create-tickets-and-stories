---
title: "Spec: Product Owner PRD Opening Restructure"
description: "Restructure the first part of a PRD / Story artifact to the team's real house opening — About narrative with lifecycle, Problem, Solution, References, Expected Outcomes — derived from the FS - Creator - Onboarding v2 epic, and review which current template sections become optional or redundant."
trigger_phrases:
  - "product owner prd opening restructure"
  - "story template update"
  - "about the problem our solution references expected outcomes"
  - "prd house format opening"
  - "story template opening"
importance_tier: "high"
contextType: "specification"
_memory:
  continuity:
    packet_pointer: "004-product-owner-prd-opening-restructure"
    last_updated_at: "2026-08-10T00:00:00Z"
    last_updated_by: "pi"
    recent_action: "Created spec for restructuring the PRD/Story house-format opening to the About / Problem / Solution / References / Expected Outcomes shape used by the real FS - Creator - Onboarding v2 epic"
    next_safe_action: "Apply the template and mode-reference edits, update the four PRD examples, propagate kernel parity, run sync --write + check --run-validators + router fixtures, add changelog entry"
---

<!-- SPECKIT_LEVEL: 2 -->
# Spec: Product Owner PRD Opening Restructure

## 1. Objective

Change the **first part of a PRD / Story artifact** in the Product Owner skill package from the current "About with Problem/Solution/User Story sub-blocks" shape to the structure the Barter team actually writes, as demonstrated by `FS - Creator - Onboarding v2.md`:

1. `## About` — narrative (what the epic covers, why it matters, value), optionally ending with the account-state / lifecycle map
2. `### Problem` — what breaks or is missing today
3. `### Solution` — the approach and its controls
4. `### References` — Components, Visuals, Flows (Figma links) and the governing spec when supplied
5. `### Expected Outcomes` — the measurable results the epic exists to produce

Second objective: **audit the current templates for sections that can be made optional or redundant**, so the house shape stays lean and the opening carries the epic-level narrative while Requirements/Acceptance criteria stay the buildable core.

## 2. Source Analysis — `FS - Creator - Onboarding v2.md`

`Product Context/Tasks & Stories/Stories/FS - Creator - Onboarding v2.md` is a real, team-written ClickUp epic export. Observed structure and grammar:

| Block | Observed form |
| --- | --- |
| About | `## About` + `* * *` divider, 2-3 paragraph narrative, then "The creator's account state controls the onboarding lifecycle:" with `*   ` bullets mapping state → experience (`Public` → Welcome..., `Sign-up — Pre-approval` → ..., etc.) |
| Problem | `### **Problem**` + divider, five `*   ` pain bullets |
| Solution | `### **Solution**` + divider, five `*   ` approach bullets |
| References | `**References**` bold label (not a heading), sub-labels `Components` / `Flows` with `*   [Name](figma-url)` links under each |
| Expected Outcomes | `### Expected Outcomes` + divider, five `*   ` outcome bullets |
| Expected Outcomes | `### Expected Outcomes` + divider, five `*   ` outcome bullets |

Grammar conventions confirmed: `* * *` dividers after every content heading, `*   ` unordered bullets, backticked identifiers/states, `* * *` divider between sections. The source also carries ClickUp artifacts we deliberately do **not** copy into the template: empty `####   ` spacer headings, H3-with-bold heading text, and a trailing typo ("flows a").

### Normalization decisions for the template (// DECISION:)

- **Promote Problem/Solution out of the About block.** The source treats them as sibling group sections, not sub-blocks inside About. Heading scheme stays inside the existing contract: `## About` at H2 (the opening umbrella), `### Problem`, `### Solution`, `### References`, `### Expected Outcomes` at H3 group headers, and bold paragraph leads (`**Components**`) for sub-labels inside References. No heading-ladder change.
- **References becomes a real section heading** (`### References`), normalizing the source's bold-label `**References**` so the divider rule applies uniformly.
- **Problem / Solution keep the plain names** (no bold inside heading text), matching the house heading contract that bans symbols/icons in headings.
- **User Story promise moves into the About narrative.** The source carries no separate User Story block; the promise is prose. The Connextra block becomes an optional enrichment (see §4).
- **Coming up is not part of the house format.** The source epic carries it, but the owner removed it from the template and examples before release (owner decision, recorded in changelog v0.7.0.2). Teams may still append it to a real epic; the template does not teach it.

## 3. Target House Opening (new template shape)

```markdown
# PRD - {Platform/Area} - {Feature} - {Name}

> _A story is used to define product requirements, acceptance criteria, etc._
> _Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
{Two or three short paragraphs: what this epic covers, why it matters, and the value it creates. Prose carries the user-story promise; never ticket boilerplate.}

{Optional: the controlling state or lifecycle map, as `*   ` bullets with backticked states:}
*   `{State}` → {experience at that state}
*   `{State}` → {experience at that state}
* * *

### Problem
* * *
{What breaks or is missing today}:
*   {Observable failure 1}
*   {Observable failure 2}
* * *

### Solution
* * *
{One line naming the change, then the controls or behaviors it introduces}:
*   {Change 1}
*   {Change 2}
* * *

### References
* * *
**Components**
*   [Page | {name}]({url})
**Flows**
*   [Welcome]({url})
*   [Sign in]({url})
* * *

### Expected Outcomes
* * *
*   {Outcome 1, measurable or clearly observable}
*   {Outcome 2}
* * *

## Requirements
...
## Acceptance criteria
...
```

## 4. Optional / Redundant Section Review (current templates)

| Current element | Verdict | Action |
| --- | --- | --- |
| Blockquote preamble | **Keep** — house-standard, ClickUp-native | unchanged |
| `#### **User Story**` block in About | **Redundant → optional** | the About narrative now carries the promise; keep the Connextra block only when a Complex/multi-capability epic needs explicit promise lines. Per-requirement `**PRD:**` value lines (enrichment 4.2) already cover requirement-level promises |
| `#### **Documentation**` link (enrichment 4.1) | **Redundant → folded into References** | References is now the single place for links (Components, Visuals, Flows, governing spec). Remove 4.1 as a standalone enrichment |
| `#### **Problem**` / `#### **Solution**` inside About | **Restructured** | promoted to `### Problem` / `### Solution` siblings of About |
| `### Problem` | **Optional at Simple** | a Simple copy-tweak PRD may have no current state to break; drop when there is genuinely nothing to describe |
| `### Expected Outcomes` | **Keep, required** | epic-level business/user outcomes; distinct from Acceptance criteria (requirement-level verification). State the split in the template so the two never duplicate |
| `### References` | **New, required when links exist** | Components/Visuals/Flows sub-groups; omit when the PRD has no external references |
| `### Coming up` | **Considered and dropped** | the source epic has it, but the owner removed it from the template and examples before release (see changelog v0.7.0.2); teams can still append it to a real epic |
| Mention line in Requirements | **Keep optional** (already) | unchanged |
| DoR / DoD / Rule / Which-means-that / value lines / shared-mechanism / `← PRIO` | **Keep optional** (already) | unchanged; tier guidance already governs |

## 5. Change Surface

Authoritative sources (`sk-product-owner/`):

1. `assets/prd-templates.md` (v0.200) — rewrite §1 shared rules + §3 house shape opening; fold 4.1 into References; add the optional/redundant guidance
2. `references/prd-mode.md` (v0.200) — update Step 3 draft shape, quality checklist item, delivery standards wording
3. `assets/examples/prd/prd-example-{simple,medium,complex,complete}.md` — rewrite openings to the new shape (four files)
4. `changelog/v0.7.0.2.md` — new entry (version pins reused per SYNC.md unreleased-correction rule)

Derived/parity surfaces:

5. `claude project/Custom Instructions.md` — PRD house-format prose (§5 formatting contract): new opening structure + fix the pre-existing H2/H3 drift (kernel line says `### About` … anchored at H3; authoritative sources say H2)
6. `SKILL.md` — only if a shape reference drifts; routing is unchanged, so no behavior change expected
7. `SYNC.md` inventory + `claude project/README.md` checksums + `package-lock.json` — regenerated by `sync --write`

Out of scope: Task/Bug/Doc templates, the router (`benchmark/router/`), tier logic, DEPTH, HVR.

## 6. Verification Gates

1. `ai-system-sync.cjs check --system product-owner --run-validators` → `clean`
2. `bash benchmark/router/run_fixtures.sh` → `PASSED 26/26`
3. All 31 knowledge mirrors byte-identical to sources (compiler check covers)
4. Kernel/skill parity grep: no `### About` H3 drift remains; opening sections consistent
5. No stray files in the product-owner tree (git status clean for `AI Systems/Product Owner`)
6. Spec folder validates: `validate.sh <034-folder> --strict` → exit 0

## 7. Related

- [`003-product-owner-story-format-audit`](../003-product-owner-story-format-audit/spec.md) — earlier audit of five stories vs the standard; verdict was "refine, don't re-guideline". This spec is a deliberate exception to that verdict: the team's real opening shape (FS - Creator - Onboarding v2) is a house convention the template does not yet teach, so the template changes, not the stories.
- `SYNC.md` — manual-load contract, inventory, required parity and drift checks for the Product Owner package.
