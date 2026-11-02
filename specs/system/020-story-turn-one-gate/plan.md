---
title: "Implementation Plan: Story turn-one gate and reply linter fixes"
description: "Close the reading that lets an explicit command's question collapse to nothing, by keeping its Validation field on every explicit command, and bound the reply linters' phrase matching. Release it as hub v1.0.16.0 and prove it with four Pi reruns."
trigger_phrases:
  - "story turn one gate plan"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.4 -->
# Implementation Plan: Story turn-one gate and reply linter fixes

<!-- SPECKIT_LEVEL: 1 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|--------|-------|
| **Language/Stack** | Markdown instruction files, Python 3 linters |
| **Framework** | The Product Owner skill and its claude.ai Project mirror |
| **Storage** | None |
| **Testing** | `benchmark/gates/run_gates.sh`, the output format gate and Pi playbook reruns |

### Overview
The kernel already makes an explicit command ask first, but the question templates let a model find nothing left to ask. Each template now keeps its Validation field on an explicit command, because no source can answer it, and the kernel, `AGENTS.md`, `SKILL.md` and Story Mode say the same. The linters get word-bounded phrase matches and the `TBD...` exemption the Human Voice card grants.
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
- [x] `bash benchmark/gates/run_gates.sh` prints `all 15 gates pass`, and PST-003 and PST-004 ask first in 4 Pi runs
- [x] Docs updated (spec/plan/tasks)
<!-- /ANCHOR:quality-gates -->

---

<!-- ANCHOR:architecture -->
## 3. ARCHITECTURE

### Pattern
Other: an instruction kernel with hand-written knowledge mirrors of the skill sources

### Key Components
- **Kernel and skill rule**: the ESCALATE IF sentence, `AGENTS.md` Section 5 and `SKILL.md` Clarification Protocol state when a question is asked
- **Question templates**: the Story and Doc templates name which fields the question carries
- **Reply linters**: `hvr_lint.py` in five systems and the Sales Direct Communication export gate

### Data Flow
A request with an explicit command routes to its mode, which asks the template's question and waits. The playbook harness captures each reply, and the linter scans it for hard blockers.
<!-- /ANCHOR:architecture -->


---

<!-- ANCHOR:phases -->
## 4. IMPLEMENTATION PHASES

Follow the ordered tasks in `tasks.md`. It owns the Setup, Implementation and Verification phase checkboxes and task state.
<!-- /ANCHOR:phases -->

---

<!-- ANCHOR:testing -->
## 5. TESTING STRATEGY

PST-003 and PST-004 rerun twice on Pi with DeepSeek V4.1 Flash high, the route the defect was found on, so the turn 1 result compares with the five earlier runs. Each sibling system's own gate suite runs after its linter change.
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

The Pi CLI with the llmgateway route for DeepSeek V4.1 Flash, used for the rerun only.
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

Revert the release commit in Product Owner and the linter commit in the outer repository. The vendor pull reverts with `git checkout` of `mcp-figma/`, `mcp-click-up/` and `vendor.json` from the commit before it.
<!-- /ANCHOR:rollback -->

---
