---
title: "Decision Record: FigJam model comparison"
description: "Four decisions for the three-model FigJam run: one harness for all three models, one adaptive operator, graders that are none of the models under test and the rule that picks the gallery board of each type."
trigger_phrases:
  - "figjam model comparison decision"
importance_tier: "normal"
contextType: "general"
_memory:
  continuity:
    packet_pointer: "017-figjam-flow-generation/038-figjam-model-comparison"
    last_updated_at: "2026-10-26T01:45:00Z"
    last_updated_by: "claude-code"
    recent_action: "Recorded the four decisions and the as-run reader note"
    next_safe_action: "None, the decisions are closed"
---
# Decision Record: FigJam model comparison

<!-- SPECKIT_LEVEL: 2 -->
<!-- SPECKIT_TEMPLATE_SOURCE: decision-record | v2.2 -->

---

<!-- ANCHOR:adr-001 -->
## ADR-001: All three models through the Devin CLI

### Metadata

| Field | Value |
|-------|-------|
| **Status** | Accepted |
| **Date** | 2026-10-25 |
| **Deciders** | The orchestrator on 2026-10-25, from the operator's "cli devin mostly" and "GLM 5.3 flash max (glm llmgateway)" |

---

<!-- ANCHOR:adr-001-context -->
### Context

The operator named GLM 5.3 Flash max on the llmgateway route and asked for the Devin CLI first. A probe on OpenCode 2 showed llmgateway refuses `max` for GLM 5.3 Flash: "reasoning_effort must be one of none, low, medium, high". Devin lists `swe-2-max`, `deepseek-v4-1-flash-1017-max` and `glm-5-3-flash-max`, and a Figma whoami probe answered on each.

### Constraints
- A result should compare models, so as few harnesses as possible.
- The operator asked for max on every model.

<!-- /ANCHOR:adr-001-context -->

---

<!-- ANCHOR:adr-001-decision -->
### Decision

**Summary**: Run all three models through the Devin CLI at their max variants.

**Details**: One runner builds every sandbox, so the three models differ in nothing but the model. GLM on llmgateway at `high` stays a possible follow-up run.

<!-- /ANCHOR:adr-001-decision -->

---

<!-- ANCHOR:adr-001-alternatives -->
### Alternatives Considered

| Option | Pros | Cons | Score |
|--------|------|------|-------|
| **All three on Devin at max** | One harness, every model at max | GLM does not take the llmgateway route the operator named | 9/10 |
| GLM on llmgateway at high | The route the operator named | Not max, and a second harness | 5/10 |
| GLM on both | Answers both readings | Seven more runs | 6/10 |

**Why Chosen**: It keeps max on every model and makes the comparison one of models alone.

<!-- /ANCHOR:adr-001-alternatives -->

---

<!-- ANCHOR:adr-001-consequences -->
### Consequences

**Positive**:
- The three models compare on the model alone.

**Negative**:
- GLM does not run on llmgateway. Mitigation: the README says so and offers that run as a follow-up.

**Risks**: None beyond the current state.

<!-- /ANCHOR:adr-001-consequences -->

---

<!-- ANCHOR:adr-001-impl -->
### Implementation

**What changes**: The driver takes the Devin model id.

**How to roll back**: Rerun GLM through OpenCode 2 at `high`.

<!-- /ANCHOR:adr-001-impl -->
<!-- /ANCHOR:adr-001 -->

---

<!-- ANCHOR:adr-002 -->
## ADR-002: One adaptive operator for every run

### Metadata

| Field | Value |
|-------|-------|
| **Status** | Accepted |
| **Date** | 2026-10-25 |
| **Deciders** | The orchestrator on 2026-10-25 |

---

<!-- ANCHOR:adr-002-context -->
### Context

Each scenario scripts three turns: the prompt, a yes to the playback and a yes to the gate. The playbook tells the operator to answer an intake round with the recommended answers. A model that stops more often than the script reaches the end of its turns with no board, and a board-quality scenario with no board cannot be graded.

### Constraints
- Every model must be driven the same way.
- Any turn the script does not hold must be visible to a grader.

<!-- /ANCHOR:adr-002-context -->

---

<!-- ANCHOR:adr-002-decision -->
### Decision

**Summary**: Send the scripted turns in order, the recommended-answers turn after an intake round, at most twice, and "Yes, go ahead." after the last turn while no board exists, at most three times.

**Details**: A small Claude Haiku classifier labels each reply's stop, as in the phase 035 run. Every extra turn is labelled `adaptive` or `supplementary` in `meta.json`, and the gallery tie-break prefers fewer.

<!-- /ANCHOR:adr-002-decision -->

---

<!-- ANCHOR:adr-002-alternatives -->
### Alternatives Considered

| Option | Pros | Cons | Score |
|--------|------|------|-------|
| **Adaptive with labelled extras** | Every model reaches a board when it can | Extra turns to grade | 8/10 |
| Scripted turns only | Matches the scenario files exactly | A model that stops once more draws nothing | 4/10 |

**Why Chosen**: It measures the boards, which is what the operator asked, and keeps the stops visible.

<!-- /ANCHOR:adr-002-alternatives -->

---

<!-- ANCHOR:adr-002-consequences -->
### Consequences

**Positive**:
- Every model gets the same chances to reach a board.

**Negative**:
- A model that needs more turns is not penalised on the scorecard. Mitigation: the README counts each model's extra turns.

**Risks**: None beyond the current state.

<!-- /ANCHOR:adr-002-consequences -->

---

<!-- ANCHOR:adr-002-impl -->
### Implementation

**What changes**: The driver and its classifier.

**How to roll back**: Rerun with the extras off.

<!-- /ANCHOR:adr-002-impl -->
<!-- /ANCHOR:adr-002 -->

---

<!-- ANCHOR:adr-003 -->
## ADR-003: Graders that are none of the models under test

### Metadata

| Field | Value |
|-------|-------|
| **Status** | Accepted |
| **Date** | 2026-10-25 |
| **Deciders** | The orchestrator on 2026-10-25 |

---

<!-- ANCHOR:adr-003-context -->
### Context

Twenty-one boards need grading on the 22-point scorecard and a fresh reader. Delegated bulk review in this repository usually goes to DeepSeek V4.1 Flash max, which is one of the three models under test.

### Constraints
- A model must not grade its own boards.
- The phase 035 run used Sonnet 5.5 high graders, so the scores compare with it.

<!-- /ANCHOR:adr-003-context -->

---

<!-- ANCHOR:adr-003-decision -->
### Decision

**Summary**: Fresh Claude Sonnet 5.5 agents grade, one per diagram type across all three models, and one fresh reader per model answers the questions from the colour renders alone.

**Details**: A grader per type sees the three boards of one scenario side by side, so the scores rank them on one scale. A reader per model never sees two boards of one scenario, so one board cannot answer another's questions.

**As run**: The three readers were rotated across the models instead, each answering one board of every scenario, so every reader saw two or three boards of each model. No reader saw two boards of one scenario, which is what this decision protects, and one reader's skill no longer lands on a single model's Clarity.

<!-- /ANCHOR:adr-003-decision -->

---

<!-- ANCHOR:adr-003-alternatives -->
### Alternatives Considered

| Option | Pros | Cons | Score |
|--------|------|------|-------|
| **Sonnet 5.5 graders and readers** | No self-grading, comparable with phase 035 | Not the usual DeepSeek bulk route | 9/10 |
| DeepSeek graders | The usual bulk route | DeepSeek grades its own boards | 2/10 |

**Why Chosen**: It removes self-grading and keeps the scale of the phase 035 run.

<!-- /ANCHOR:adr-003-alternatives -->

---

<!-- ANCHOR:adr-003-consequences -->
### Consequences

**Positive**:
- Scores rank the three models fairly.

**Negative**:
- Seven graders and three readers cost more than one pass. Mitigation: each reads only its own boards.

**Risks**: None beyond the current state.

<!-- /ANCHOR:adr-003-consequences -->

---

<!-- ANCHOR:adr-003-impl -->
### Implementation

**What changes**: The grading briefs in `grades/`.

**How to roll back**: Regrade with another neutral model.

<!-- /ANCHOR:adr-003-impl -->
<!-- /ANCHOR:adr-003 -->

---

<!-- ANCHOR:adr-004 -->
## ADR-004: The best board of each type

### Metadata

| Field | Value |
|-------|-------|
| **Status** | Accepted |
| **Date** | 2026-10-25 |
| **Deciders** | The orchestrator on 2026-10-25 |

---

<!-- ANCHOR:adr-004-context -->
### Context

The gallery keeps one board per type and every caption names its score.

### Constraints
- The choice must be repeatable from `results.jsonl`.

<!-- /ANCHOR:adr-004-context -->

---

<!-- ANCHOR:adr-004-decision -->
### Decision

**Summary**: The best board is the highest scorecard total, then a pass over a fail, then fewer supplementary turns, then fewer adaptive turns.

**Details**: A board that fails its scenario is still eligible when it is the best of its type, and its caption says it failed and why.

<!-- /ANCHOR:adr-004-decision -->

---

<!-- ANCHOR:adr-004-alternatives -->
### Alternatives Considered

| Option | Pros | Cons | Score |
|--------|------|------|-------|
| **Total, then pass, then fewer extras** | Repeatable and favours the cleaner run | A failing board can win a weak type | 8/10 |
| Pass first | Never shows a failing board | A type with no pass would have no image | 5/10 |

**Why Chosen**: Every type gets an image and the rule needs no judgement.

<!-- /ANCHOR:adr-004-alternatives -->

---

<!-- ANCHOR:adr-004-consequences -->
### Consequences

**Positive**:
- The gallery shows the best the skill drew.

**Negative**:
- A failing board may sit in the gallery. Mitigation: its caption says so.

**Risks**: None beyond the current state.

<!-- /ANCHOR:adr-004-consequences -->

---

<!-- ANCHOR:adr-004-impl -->
### Implementation

**What changes**: The gallery images and captions.

**How to roll back**: Restore the previous images from git.

<!-- /ANCHOR:adr-004-impl -->
<!-- /ANCHOR:adr-004 -->
