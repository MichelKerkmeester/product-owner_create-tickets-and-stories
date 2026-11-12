---
title: "Implementation Plan: Design copy pointer requirements"
description: "Edits two Story rule files and their two Project mirrors with the same sentences, releases the change as patch steps and proves it with the gate runner and the residency check."
trigger_phrases:
  - "design copy pointer requirements plan"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.4 -->
# Implementation Plan: Design copy pointer requirements

<!-- SPECKIT_LEVEL: 1 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|--------|-------|
| **Language/Stack** | Markdown, JSON |
| **Framework** | Product Owner hub, `sk-product-owner` and its Claude Project package |
| **Storage** | None |
| **Testing** | `benchmark/gates/run_gates.sh`, `benchmark/parity/run_residency.sh`, `rg` counts and strict packet validation |

### Overview
Change the Story verbatim rule in `story-mode.md` and `story-template.md`, then carry the same sentences into the two knowledge mirrors by exact replacement. Bump the hub and the skill one patch step each and write both release notes and the parity note. Prove it by rerunning all gates against the baseline of 19 passing.
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
- [x] `bash benchmark/gates/run_gates.sh` prints `all 19 gates pass`
- [x] Docs updated (spec/plan/tasks)
<!-- /ANCHOR:quality-gates -->

---

<!-- ANCHOR:architecture -->
## 3. ARCHITECTURE

### Pattern
Source then mirror

### Key Components
- **`sk-product-owner/references/story-mode.md`**: owns the rule on which strings travel verbatim
- **`sk-product-owner/assets/story-template.md`**: repeats the rule where the writer fills Requirements
- **`claude project/knowledge/`**: two hand-written mirrors that carry the same sentences

### Data Flow
The skill source is edited first. The same replacement runs on its mirror, and a `diff` of the changed lines proves the pair matches.
<!-- /ANCHOR:architecture -->


---

<!-- ANCHOR:phases -->
## 4. IMPLEMENTATION PHASES

Follow the ordered tasks in `tasks.md`. Setup records the gate baseline. Implementation edits the two sources, the two mirrors and the release files. Verification reruns the gates, the residency check and the sentence counts.
<!-- /ANCHOR:phases -->

---

<!-- ANCHOR:testing -->
## 5. TESTING STRATEGY

`bash benchmark/gates/run_gates.sh` must print `all 19 gates pass` and `bash benchmark/parity/run_residency.sh` must print `PASSED`. No model run is part of this packet, so the behavior change itself is unproven until a Story is written from a design.
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

`python3`, `node`, `rg` and the shared Sync Loop folder one level above this repository. No new package.
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

Trigger: a Story drops a typed value or a changed string it should have quoted. Revert the one commit that carries this packet, in this repository and in the Barter repository.
<!-- /ANCHOR:rollback -->

---
