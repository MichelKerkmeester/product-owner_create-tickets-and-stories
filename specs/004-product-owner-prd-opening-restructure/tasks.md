---
title: "Tasks: Product Owner PRD Opening Restructure"
description: "Actionable breakdown for the template restructure, example updates, kernel parity and sync verification."
contextType: "reference"
importance_tier: "normal"
level: 2
---

# Tasks: Product Owner PRD Opening Restructure

## Track 1 — Authoritative sources (`sk-product-owner/`)

- [ ] **T1. `assets/prd-templates.md`** — rewrite the house shape (section 3) opening to `## About` narrative (+ optional lifecycle map), `### Problem`, `### Solution`, `### References`, `### Expected Outcomes`; update §1 shared rules (narrative first, heading scheme, User Story block optional, References replaces Documentation link); add the optional/redundant guidance from spec §4; drop enrichment 4.1 (Documentation link) into References; record the owner decision that `### Coming up` stays out of the house format
- [ ] **T2. `references/prd-mode.md`** — Step 3 draft shape lists the new opening blocks; quality checklist narrative item names About/Problem/Solution/References/Expected Outcomes; delivery standards mention References and Expected Outcomes
- [ ] **T3. Four PRD examples** — `prd-example-{simple,medium,complex,complete}.md` openings rewritten to the new shape (Simple keeps a trimmed opening; Complex/Complete show References + Expected Outcomes where they earn their place)
- [ ] **T4. Changelog** — new `changelog/v0.7.0.2.md` entry documenting the opening restructure and the optional/redundant review; version pins reused per SYNC.md unreleased-correction rule

## Track 2 — Parity surfaces

- [ ] **T5. `claude project/Custom Instructions.md`** — update PRD house-format prose: new opening structure; fix pre-existing drift where the kernel says `### About` … anchored at H3 (authoritative contract is H2 for PRD major sections, matching SKILL.md and prd-templates.md)
- [ ] **T6. `SKILL.md`** — verify no shape reference drifted; routing untouched
- [ ] **T7. `AGENTS.md`** — verify no change needed (identity/routing/delivery unchanged)

## Track 3 — Sync and verification

- [ ] **T8.** `node "AI Systems/z — Sync Skill to Claude Project/ai-system-sync.cjs" sync --system product-owner --write`
- [ ] **T9.** `check --system product-owner --run-validators` → clean
- [ ] **T10.** `bash benchmark/router/run_fixtures.sh` → PASSED 26/26
- [ ] **T11.** Kernel/skill parity grep: no `### About` H3 drift; opening sections consistent across kernel and templates
- [ ] **T12.** No stray files: `git status --short -- "AI Systems/Product Owner"` clean; knowledge dir = 31 files

## Sequencing

T1 → T2 → T3 (authoritative sources first), then T5/T6/T7 (parity), then T8–T12 (sync + verification). T4 last, after verification numbers are real.
