# Product Owner Skill Alignment — Detailed Summary

How the Product Owner package at `AI_Systems/Barter/Product Owner/` was brought into line with the Public repo's skill standards: the sk-* folder convention, sk-doc's create-skill authoring standard, the system-skill-advisor's metadata expectations and the repo's documentation house style. This records what changed, why, in what order and how each step was verified. Written 2026-07-16 at the close of phases 015 through 017.

---

## 1. WHERE THIS STARTED

Before alignment the package looked like this: a folder named `skill/` holding a 1188-line SKILL.md grown by accretion, no skill README, no advisor metadata JSONs, a flat sync manifest without the repo's section standard, a hand-written root README duplicating package prose, and two packagings (CLI + claude.ai Project) kept in step by a manual checksum manifest. The skill worked, and a 43-check router regression suite proved its behavior, but nothing about its packaging matched how the Public repo's own skills are built.

The alignment goal: make the package read and route like a first-class sk-* skill without changing a single routing behavior.

---

## 2. THE FOLDER RENAME (skill -> sk-product-owner)

The folder `Product Owner/skill/` became `Product Owner/sk-product-owner/`, matching the repo's sk-* naming family (sk-doc, sk-code, sk-design).

Mechanics that mattered:

- 98 path references were rewritten across five files: AGENTS.md (33), SYNC.md (26), claude project/README.md (18), the root README (14) and SKILL.md itself (7, including strings inside the executable router pseudocode).
- The replacement pattern was `skill/` not preceded by a letter, so `skills/` paths pointing at the mcp-tooling packet survived untouched.
- `references/human-voice-rules.md` is a relative symlink three levels up into the repo's shared knowledge (`z — Knowledge/Rules - Human Voice - EN - v0.210.md`). The rename preserved its depth, so it still resolves with no edit.
- The frontmatter `name: product-owner` was deliberately kept. The folder name is packaging, the invocation name is a separate contract, and the user asked for a folder rename only.
- Zero residual `skill/` references were verified by sweep after the rewrite, and the router fixture suite was re-extracted from the new path and passed 43/43.

---

## 3. FILE NAMING CONVENTIONS

Two naming layers were already in place from earlier phases and carried through alignment unchanged:

- **Source files** are hyphenated (`doc-mode.md`, `story-templates.md`, `bug-report-template.md`), from the phase-010 hyphenation sweep that renamed twelve files and two directories from underscores.
- **Knowledge mirrors** are named by each source's frontmatter title plus `.md`, the `Product Owner - {Class} - {Name} - v{X.Y.Z}.md` convention. A version bump therefore renames the mirror, and the old mirror is deleted rather than retained beside the new one.
- **Exports** use exactly four artifact prefixes: `task-`, `bug-`, `doc-`, `story-` (`export/[###] - {prefix}[description].md` for new artifacts, the original basename for refinements). The alignment audit caught AGENTS.md still showing invented `subtask-` and `acceptance-criteria-` prefixes in its examples and corrected both to `task-` forms.

The version state at the close of alignment:

| File | Version |
| --- | --- |
| SKILL.md | 1.4.0 |
| Custom Instructions kernel | 1.2.0, aligned to Skill 1.4.0 |
| task-mode.md | 0.302 |
| task-templates.md | 0.101 |
| bug-mode.md | 0.201 |
| bug-report-template.md | 0.100 |
| doc-mode.md | 0.105 |
| doc-templates.md | 0.106 |
| story-mode.md | 0.102 |
| story-templates.md | 0.102 |
| interactive-mode.md | 0.404 |
| interactive-response-templates.md | 0.102 |
| depth-framework.md | 0.201 |
| human-voice-rules.md | 0.210 (shared symlink) |
| 17 worked examples | 0.100 each |

---

## 4. SKILL.MD REWRITTEN TO THE CREATE-SKILL STANDARD (v1.4.0)

A fresh Sonnet agent rewrote SKILL.md against sk-doc's create-skill packet, with the 43-check regression suite as a hard gate it ran itself after every draft.

What changed:

- **Structure**: frontmatter, a `<!-- Keywords: ... -->` comment (previously missing), then seven numbered ALL-CAPS sections with `---` separators: WHEN TO USE, SMART ROUTING, HOW IT WORKS, RULES, REFERENCES, SUCCESS CRITERIA, INTEGRATION POINTS.
- **Length**: 1188 lines to 741. All cut content already lived in the mode references and template assets, so nothing moved, only duplication died. The natural-language trigger list collapsed from one bullet per phrase to grouped lines, and the RULES sections went from 29+29 verbose items to 15+14 denser ones covering the same ground.
- **Router consolidation**: four separate Python fences became one. The agent proved by grep that `INTENT_MODEL`, `ENERGY_MODEL`, `FALLBACK_CHAINS`, `DOCUMENT_MAP` and unused `SEMANTIC_TOPICS` keys were decoration nothing executed, and deleted them. The surviving fence carries only what runs: `SEMANTIC_TOPICS`, `RESOURCE_MAP` and the nine routing functions (token detection, `$task --subtask` before `$task`, conflict collection, artifact-framing precedence, semantic scoring with the 0.85 override, the UI-refinement Task override, STORY subject and negation tie-breaks, Quick as energy, the Doc gate). Scattered prose that stated the same rules three ways became one nine-step Detection Sequence plus one ALWAYS/CONDITIONAL/ON_DEMAND resource table with the one-example-max rule inline.
- **Line-count honesty**: the 350-550 target was not reached because the executable router is roughly 450 lines and the fixture suite extracts every python fence from SKILL.md, so the router cannot leave the file. Behavior parity outranked the line target.
- **Verification**: the agent finished at 43/43 and the orchestrator re-ran the suite independently after handoff, also 43/43.

Preserved non-negotiables, in compact form: identity adoption, the export read-back receipt (`Verified: read-back succeeded; N lines`, failed read-back forbids `Path:`), the ClickUp transport table and consent rules, refinement fidelity, the ClickUp grammar and balanced heading ladder for Doc and Story artifacts, the quality gates and the HVR pointer.

---

## 5. ADVISOR METADATA (description.json, graph-metadata.json)

Two companion JSONs were created next to SKILL.md in the leaf-skill shape the system-skill-advisor expects, modeled on sibling schemas rather than invented:

- `description.json`: name, description, version (1.4.0.0), importance tier, keywords, trigger examples, supported surfaces.
- `graph-metadata.json`: schema version, skill id, family, category, edges, domains, intent signals and the derived block (trigger phrases, key topics, key files, entities, causal summary).

Content models the five intents, the command vocabulary, ClickUp handoff and DEPTH/HVR terminology, cross-linked as a sibling of sk-doc and an enhancer of mcp-tooling. Being a hub-less standalone skill, it carries no mode-registry.json and no hub-router.json.

---

## 6. THE SKILL README

`sk-product-owner/README.md` went through three deliberate iterations:

1. **First draft** by an agent following create-skill's standalone-skill README template (the agent correctly chose it over the thinner hub-packet style). Orchestrator fact-check fixed a wrong claim that the HVR symlink is skipped from mirroring (it is mirrored dereferenced), reshaped a 3-column table to the 2-column house rule and removed semicolons.
2. **Descriptive rewrite** on user feedback, borrowing the Public root README's mechanisms: a core-layer value table opener, a problem-story overview and an FAQ.
3. **Reference rewrite** on further feedback ("section 1 doesn't make sense, wrong diagram styling, more detail"): the abstract story replaced with concrete folder anatomy, the flow diagram redrawn in the repo's box-drawing style, and the weight shifted to reference detail. A final "bit more detailed" pass added artifact skeleton fences for Task and Bug, the five status labels verbatim, a Connextra plus Scenario snippet, the DEPTH phase table, precedence-by-example routing, the ClickUp push shape, a rendered quality-verdict example and all 17 fixtures named individually.

Final shape: 449 lines, eleven numbered sections (Overview with diagram, Quick Start, The Five Modes, Output Format, ClickUp Delivery, Export and Receipts, Examples Library, Dual Packaging, FAQ, Troubleshooting, Related Documents), 2-column tables throughout, HVR-clean.

**Root README**: the old package-level guide at `Product Owner/README.md` was removed (user decision, confirmed via question) and replaced by a relative symlink `README.md -> sk-product-owner/README.md`, making the skill README the single canonical readme. The skill README's self-referential related-documents row was removed at the same time.

---

## 7. AGENTS.MD

AGENTS.md remains the CLI entry point and enforcement wrapper: boundary rules, the strict load sequence (SKILL.md, HVR, DEPTH, one routed mode pair), the export receipt procedure, the ClickUp handoff rules and the resource DAG.

Alignment touched it twice:

- The rename sweep rewrote its 33 path references to `sk-product-owner/`.
- The drift audit (section 9) verified its read-back procedure, ClickUp transport, resource DAG and one-example-max rule all match SKILL.md v1.4.0, and fixed the one confirmed bug: export-naming examples with prefixes canon never defined.

---

## 8. SYNC.MD

Restructured from a flat manifest to the sk-doc section standard: YAML frontmatter, an H1 plus tagline blockquote, and eight numbered ALL-CAPS sections with dividers: Overview, When to Sync, Manual-Load Contract, Source-to-Mirror Inventory, Sync Workflow, Required Parity, Drift Checks, Related Documents.

Content changes riding along: the stale "all four shapes" drift check became five, the balanced heading ladder entered both the Required Parity list and the fixture drift check, Story joined the regression check, and semicolons were removed. The inventory pins were updated through the alignment: Skill 1.4.0, kernel 1.2.0 aligned to 1.4.0, thirty knowledge files (thirteen core plus seventeen examples).

---

## 9. THE CLAUDE PROJECT PACKAGING

The derived packaging in `claude project/` was aligned in two waves.

**Version cascade**: the kernel's alignment line moved to Skill v1.4.0, the Skill mirror renamed to `Product Owner - System - Skill - v1.4.0.md`, and the manifest README's tree, map and checksum rows followed. Every mirror was recopied and the sha256-16 table rebuilt from final bytes.

**Drift audit fixes** (independent Sonnet auditor, findings-only brief, every claim byte-verified by the orchestrator before any edit):

- Kernel §4 listed four Doc shapes while its own knowledge table said five: a Narrative overview bullet was added so claude.ai routes README, status and handover requests to the right shape without filesystem access.
- Kernel rule 26 lacked the balanced heading ladder even though SYNC's Required Parity names it as something both packagings must agree on. The rule now states: H1 title only, H2 anchors major sections and stays a minority, H3 and H4 carry the rest with bold leads below.
- Kernel rule 31 reported a generic "quality status". It now specifies the Doc dimensioned verdict: one pass-or-attention line each for Source safety, Shape fit, ClickUp layout, Readability and Voice, with attention lines naming the specific item.
- The manifest README's smoke matrix pinned Task Mode at v0.301 against its own v0.302 tree: corrected, and two smoke lines added for the heading ladder and the dimensioned verdict.

**Accepted deferrals** (audited and judged fine as is): the Opening Contract, the two-register rule, the Readability Floor and single-group task numbering stay in the uploaded knowledge mirrors rather than the kernel, consistent with how the kernel defers every other craft detail and with SYNC's parity list.

The package holds 30 knowledge files: 13 core mirrors plus 17 example mirrors (task 4, bug 4, doc 6 including the README-style Narrative overview and Quick fixtures, story 3). The live claude.ai Project predates all of this and needs a full refresh: kernel paste plus a 30-file knowledge upload per the manifest.

---

## 10. HOW EVERYTHING WAS VERIFIED

Three verification layers ran after every mutating step, all green at close:

| Check | Result |
| --- | --- |
| Router regression suite (extracts every python fence from SKILL.md) | 43/43, run independently after the agent's own run |
| Mirror byte-identity (symlinks resolved with realpath) | 30/30 |
| sha256-16 manifest rows against final bytes, kernel included | 31/31 |

Process rules that held throughout: external and agent findings were verified against actual file bytes before acceptance (this caught my own validator errors twice as well as agent mistakes), version bumps always renamed mirrors and refreshed checksum rows in the same pass, and no mirror was ever edited directly, only recopied from its source.

---

## 11. WHAT DELIBERATELY DID NOT CHANGE

- Routing behavior: byte-level proof via the fixture suite before and after the SKILL.md rewrite.
- The skill invocation name `product-owner`.
- The HVR symlink and its shared source in `z — Knowledge/`.
- Task, Bug and Interactive artifact house formats (H3 sections, `---` dividers), which were already compliant.
- The kernel's deferral model: compact rules inline, craft detail in uploaded mirrors.
