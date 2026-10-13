---
title: "Implementation Plan: Story Drafts two-pass rewrite"
description: "Two passes over the sixteen Product Owner Story Drafts: three parallel lanes of DeepSeek V4 Flash at max thinking through /agent-router product owner $story, each draft rewritten in place from itself and its context.md, then a second pass over the three stories whose criteria described UI mechanics, plus a separate one-request benchmark of the hardened Story shape across three models."
trigger_phrases:
  - "story drafts rewrite plan"
  - "three parallel rewrite lanes"
  - "criteria cleanup second pass"
  - "story shape benchmark models"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.2 -->
# Implementation Plan: Story Drafts two-pass rewrite

<!-- SPECKIT_LEVEL: 1 -->
---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|--------|-------|
| **Language/Stack** | Bash scripts calling `pi -p`; TSV result rows; Story markdown |
| **Framework** | `/agent-router product owner $story`, DeepSeek V4 Flash at max thinking on the llmgateway provider |
| **Storage** | The draft files themselves, overwritten in place; no generated export tree |
| **Testing** | The Story format gate, per-story acceptance-criteria counts, and one separate single-request benchmark |

### Overview
One draft per router call, rewritten in place from that draft and the `context.md` beside it if there is one, three lanes over sixteen folders. The three stories whose criteria described UI mechanics were then run again from the same source with one extra sentence of steer.
<!-- /ANCHOR:summary -->

---

<!-- ANCHOR:quality-gates -->
## 2. QUALITY GATES

### Definition of Ready
- [x] Problem statement clear and scope documented
- [x] Success criteria measurable
- [x] Dependencies identified

### Definition of Done
- [x] All acceptance criteria met
- [x] Tests passing (if applicable)
- [x] Docs updated (spec/plan/tasks)
<!-- /ANCHOR:quality-gates -->

---

<!-- ANCHOR:architecture -->
## 3. ARCHITECTURE

### Pattern
Three lanes of one router call per draft, then a targeted second pass over the stories that failed on criteria.

### Key Components
- **`run.sh`**: reads `files.txt` and splits the draft paths round-robin across lanes 1, 2 and 3
- **`rerun3.sh`**: the same model and router for the three flagged stories, with one extra sentence of steer
- **TSV records**: `results.tsv`, `rerun3.tsv` and `story-benchmark-results.tsv`
- **`README.md`**: the reading guide for those files and for the two-pass result

### Data Flow
`files.txt` into the round-robin split, then one `pi -p --provider llmgateway --model deepseek-v4-flash:max` call per draft through the router, then an in-place overwrite of that exact path, then one row per run in the TSV beside the script.
<!-- /ANCHOR:architecture -->

---

<!-- ANCHOR:phases -->
## 4. IMPLEMENTATION PHASES

Follow the ordered tasks in `tasks.md`. It owns the Setup, Implementation and Verification phase checkboxes and task state.
<!-- /ANCHOR:phases -->

---

<!-- ANCHOR:testing -->
## 5. TESTING STRATEGY

The first pass is read against the gate and the criteria counts: 16 of 16 exported in place, 15 of 16 gate-clean. The second pass is the harder check, because it runs again from the original drafts and context files only and is read for the same gate plus the absence of unasked Delivery sections, image references, design values in criteria and copied hedges. The benchmark is separate: one request on the hardened Story shape, one row per model, with a validity verdict.
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

DeepSeek V4 Flash at max thinking on the llmgateway provider through the agent router; `files.txt` for the first pass, which the README states is not committed; and the hardened Story shape from `Specs/030-system-hardening/product-owner.md`, commits `84bba2e` through `1d70181`, which had landed before the second pass.
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

Restore the drafts from the pre-rewrite backup that `README.md` names, `~/story-drafts-backup-20260908/story-drafts-pre-rewrite.tgz`, which holds all sixteen drafts. Neither pass wrote a numbered export, so there is no generated tree to remove.
<!-- /ANCHOR:rollback -->

---
