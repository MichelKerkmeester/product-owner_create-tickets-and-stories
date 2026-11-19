---
title: "Feature Specification: Story turn-one gate and reply linter fixes"
description: "A DeepSeek V4.1 Flash high story test drafted on turn 1 after `$s` and `$story`, because the Story question template let the model decide the question had nothing left to ask. The reply linter also flagged the sanctioned TBD placeholder and phrases inside longer words."
trigger_phrases:
  - "story turn one gate"
  - "story turn one gate and reply linter fixes"
  - "explicit command asks first"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.4 -->
# Feature Specification: Story turn-one gate and reply linter fixes

<!-- SPECKIT_LEVEL: 1 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 1 |
| **Priority** | P1 |
| **Status** | Complete |
| **Created** | 2026-10-28 |
| **Branch** | `main` |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Five story runs of the Product Owner Project on DeepSeek V4.1 Flash high, through Devin and again through Pi, drafted on turn 1 in PST-003 (`$s`) and PST-004 (`$story`) on both harnesses. The kernel already says an explicit command asks first "however much context the request carries", but the Story question template says "Populate only unresolved fields", and the model read the two together as a question that collapses to nothing when the sources look complete. The reply linter also flagged the `TBD...` Delivery placeholder the Human Voice card grants and matched "acts as" inside "contacts as", and the same substring matching sits in four sibling systems' linters.

### Purpose
An explicit artifact command asks its question and waits on turn 1 however complete the sources look, and the reply linters report only real blockers.
<!-- /ANCHOR:problem -->

<!-- ANCHOR:measured-behavior -->
### Measured Behavior
```text
Pi run pi-a, PST-004 events-turn-1.jsonl, the model's reasoning before it drafted:
- "Maybe the Story question is specifically about the task split, and since the split is named, the question collapses."
- "still ask their mode's context-specific question", but the context-specific question template collapses to nothing when every field is resolved.
- "This looks like the "bench" designed to test whether the model asks a needless clarification or drafts."

Turn 1 ask-first across five runs per harness (grades.md and pi-grades.md):
Devin asked first in 2 of 5 (PST-001 twice). Pi asked first in 3 of 5 (PST-001 twice and PST-002).
PST-003 and PST-004 drafted on turn 1 on both harnesses.

lint_replies.py on the Pi runs:
PST-003 more_than_one_ellipsis, every hit the TBD... Delivery placeholder
PST-004 copula:acts as, the match is "contacts as WISMO"
```
<!-- /ANCHOR:measured-behavior -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- State in the kernel, `AGENTS.md` and `SKILL.md` that sources which look complete do not answer an explicit command's question
- Keep the Validation field in the Story and Doc question templates on an explicit command, in the skill and in its Project mirror
- Close the same reading in Story Mode's Interactive behavior line and Step 1, in the skill and in its Project mirror
- Exempt `TBD...` from the ellipsis count and bound every phrase match in the Product Owner reply linter, and bound the phrase matches in the Copywriter, Deal Templates, Sales Direct Communication and Sales HubSpot linters and the Sales Direct Communication export gate
- Release hub v1.0.16.0, `sk-product-owner` v1.2.6.0 and kernel v1.2.16, then rerun PST-003 and PST-004 twice on Pi

### Out of Scope
- A rule change for the PST-002 No-gos - Story Mode already says unknown Delivery values stay `TBD...` "rather than an inferred estimate, risk or exclusion", so the filled No-gos fail an existing rule
- Routing read cost - the repeat reads are the harness reading files, which a claude.ai Project does differently
- The recap inside a clarification block - the kernel already says it carries the question and nothing else

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `claude project/Custom Instructions.md` | Modify | ESCALATE IF sentence, H1 v1.2.16 |
| `AGENTS.md`, `sk-product-owner/SKILL.md` | Modify | The same rule |
| `sk-product-owner/assets/interactive-response-templates.md` and its Project mirror | Modify | Validation field always stays |
| `sk-product-owner/references/story-mode.md` and its Project mirror | Modify | Interactive behavior and Step 1 |
| `benchmark/grader/hvr_lint.py` | Modify | `TBD...` exemption and bounded phrases |
| Four sibling `benchmark/grader/hvr_lint.py` files and Sales Direct Communication `benchmark/gates/export_blockers.py` | Modify | Bounded phrases |
| Version files, `changelog/`, `SYNC.md`, `README.md`, `claude project/README.md` | Modify, Create | The release |
| `mcp-figma/`, `mcp-click-up/`, `vendor.json` | Modify | Vendor pull the vendor sync gate asked for |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

REQ ids run in one sequence across the P0 and P1 tables. A new requirement takes the highest REQ id plus one. validate.sh does not link ids between files.

### P0 - Blockers (MUST complete)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-001 | The kernel, `AGENTS.md`, `SKILL.md`, both question templates and Story Mode say an explicit command asks and waits however complete the sources look | `rg -n "Validation(\*\*)? field|settle every field|all four are established"` prints at least one line in each of the seven files |
| REQ-002 | The Product Owner gates and format gate pass | `run_gates.sh` prints `all 15 gates pass` and the format gate prints `validation passed` |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-003 | The linters skip `TBD...` and match phrases as whole words | A one-off check: "contacts as" gives no copula hit, three `TBD...` give no ellipsis hit, "bij dezelfde" gives no Sales phrase hit |
| REQ-004 | PST-003 and PST-004 ask first on turn 1 on Pi | Two Pi runs each, turn 1 holds one question and no draft |
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: In 4 Pi runs of PST-003 and PST-004 on v1.0.16.0, turn 1 asks one Story question and renders no draft in every run
- **SC-002**: `run_gates.sh` passes in Product Owner, Copywriter, Deal Templates and Sales HubSpot, and the Sales Direct Communication gates pass
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | The llmgateway route for DeepSeek V4.1 Flash on Pi | The rerun cannot run | Retry once, then report the run as blocked |
| Risk | A model that still argues past the rule | Med | The rerun measures it, and a miss is recorded as a known limitation rather than a pass |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:questions -->
## 7. OPEN QUESTIONS

- None
<!-- /ANCHOR:questions -->

---
