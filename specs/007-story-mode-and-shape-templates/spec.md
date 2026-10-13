---
title: "Feature Specification: Story Mode and Per-Shape Templates"
description: "PRD Mode is renamed Story Mode, and its single 556-line template file is split so each artifact shape carries its own scaffold. Shared grammar stays in one place rather than being copied three ways, and a request loads only the shape it asked for."
trigger_phrases:
  - "rename prd mode to story mode"
  - "dedicated story draft template"
  - "dedicated epic template"
  - "split prd-templates"
  - "story mode shapes"
importance_tier: "high"
contextType: "specification"
_memory:
  continuity:
    packet_pointer: "007-story-mode-and-shape-templates"
    last_updated_at: "2026-09-02T00:00:00Z"
    last_updated_by: "claude"
    recent_action: "Scoped the rename and the three-way template split across 20 files"
    next_safe_action: "Implement the split, keeping shared grammar in the mode reference rather than duplicating it per template"
    blockers: []
    key_files:
      - "sk-product-owner/references/prd-mode.md"
      - "sk-product-owner/assets/prd-templates.md"
      - "sk-product-owner/SKILL.md"
      - "benchmark/router/route_contract.py"
    completion_pct: 5
    open_questions:
      - "Do the back-compat aliases $prd and $p survive the rename, or retire on a deprecation notice"
    answered_questions:
      - "Shared grammar lives once in the mode reference, never duplicated into the three templates"
      - "A request loads only the shape template its command resolved, not all three"
---
# Feature Specification: Story Mode and Per-Shape Templates

<!-- SPECKIT_LEVEL: 2 -->
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->

---

## 1. METADATA

| Field | Value |
| --- | --- |
| Spec ID | 040 |
| Level | 2 |
| Status | Planned |
| Created | 2026-09-02 |
| Related to | 006-human-voice-and-conciseness-enforcement |
| Systems touched | Product Owner only |

---

## 2. PROBLEM & PURPOSE

### 2.1 Problem statement

The mode is called PRD Mode but it produces three artifacts, and only one of them is a PRD. A Story, an Epic and a Story Draft all route through it. The name describes neither the majority case nor the shared thing.

All three scaffolds also live in one 556-line file, `assets/prd-templates.md`. The loading contract pairs one reference with one template, so a Story request loads the Epic and Story Draft scaffolds it will never use. Story Draft was added as a third shape inside a file whose shared-rules section opens by saying it governs "every Story and every Epic", then carves the draft out, which is a shape bolted into a structure built for two.

### 2.2 Purpose

Name the mode after what it makes, give each shape its own scaffold, and load only the shape that was asked for.

### 2.3 Non-goals

- Changing any artifact's house format. This is a packaging change, not a grammar change
- Changing the routing behaviour of any command. The same input resolves to the same shape before and after
- Touching the other eight systems. This is Product Owner only

---

## 3. REQUIREMENTS

### R1 — Rename the mode

* * *

PRD Mode becomes Story Mode throughout.

- `references/prd-mode.md` becomes `references/story-mode.md`
- The intent key, the resource lane and every prose reference follow
- `$story` and `$s` become the primary commands. `$prd` and `$p` stay as back-compat aliases, since existing prompts and habits use them
- Routing behaviour is unchanged. Every input that resolved to a shape before resolves to the same shape after

### R2 — One template per shape

* * *

Split `assets/prd-templates.md` into three scaffolds:

- `assets/story-template.md`
- `assets/epic-template.md`
- `assets/story-draft-template.md`

Each carries its own scaffold and nothing else.

### R3 — Shared grammar lives once

* * *

The rules common to the shapes stay in `references/story-mode.md`, not copied into each template.

Copying the Given/When/Then contract, the divider rules and the bullet grammar into three files recreates the drift this system spent a full packet eliminating. One authority, three scaffolds that follow it.

The mode reference keeps: shared rules, artifact-kind selection, the promotion rule, the optional enrichments, the worked-example pointers and the export contract.

### R4 — Load only the resolved shape

* * *

The command already distinguishes the shapes before any file is read. `$story` and `$prd` select Story, `$epic` selects Epic, `$draft` selects Story Draft.

CONDITIONAL loading becomes `references/story-mode.md` plus the one template the command resolved. A Story request stops loading the Epic and Draft scaffolds.

### R5 — Every surface follows

* * *

The rename and the split touch twenty files. All of them move together or the system contradicts itself:

`SKILL.md`, `AGENTS.md`, `claude project/Custom Instructions.md`, `SYNC.md`, `claude-project.sync.json`, `benchmark/router/route_contract.py`, `benchmark/router/fixtures.json`, `benchmark/router/differential.py`, `benchmark/router/README.md`, `benchmark/format/validate-output-format.cjs`, `sk-product-owner/README.md`, `sk-product-owner/graph-metadata.json`, `sk-product-owner/description.json`, `claude project/README.md`, `references/interactive-mode.md`, and the compiler-generated mirrors.

Changelogs are historical and keep the old names.

---

## 4. RISKS

| Risk | Mitigation |
| --- | --- |
| A renamed file breaks the mirror map and the knowledge count | The sync compiler owns the mirrors. Run it, never hand-edit them |
| The differential harness compares two routers that renamed at different times | Rename both in one pass, then run the harness before anything else |
| Splitting drops a rule that only existed in the shared section | Diff the three new templates plus the mode reference against the original file, and account for every line |
| `$prd` habits break | Keep the aliases. The mode name changes, the commands do not |

---

## 5. VERIFICATION

- `bash benchmark/router/run_fixtures.sh`, fixtures and differential both green
- `node benchmark/format/validate-output-format.cjs` and `bash benchmark/format/run_fixtures.sh`
- The 67 artifacts from the four model runs still pass, since none of their formats changed
- Every input in the fixture corpus resolves to the same shape it did before the rename
- Sync compiler run, mirrors consistent, knowledge count correct
