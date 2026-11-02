---
title: "Decision Record: Knowledge retrieval"
description: "The knowledge set keeps its 13 repeated sentences, because each lets a retrieved file stand on its own."
trigger_phrases:
  - "knowledge retrieval decision"
importance_tier: "normal"
contextType: "general"
_memory:
  continuity:
    packet_pointer: "019-runtime-and-project-optimization/003-knowledge-retrieval"
    last_updated_at: "2026-10-21T21:30:00Z"
    last_updated_by: "claude-code"
    recent_action: "Recorded why no duplicate was removed"
    next_safe_action: "Start phase 004, behavior check"
---
# Decision Record: Knowledge retrieval

<!-- SPECKIT_LEVEL: 2 -->
<!-- SPECKIT_TEMPLATE_SOURCE: decision-record | v2.2 -->

---

<!-- ANCHOR:adr-001 -->
## ADR-001: Keep the repeated sentences in the knowledge set

### Metadata

| Field | Value |
|-------|-------|
| **Status** | Accepted |
| **Date** | 2026-10-21 |
| **Deciders** | Claude Code, under the operator's "All of it" scope |

---

<!-- ANCHOR:adr-001-context -->
### Context

The phase was planned to remove duplicated text across the 62 knowledge files. Measured, the set holds 578,636 bytes, one repeated paragraph of 275 bytes and 13 sentences that appear in more than one file, 2,104 extra bytes in all, under 0.4% of the set.

### Constraints
- A Project retrieves knowledge by relevance, so a file is often read without its neighbours.
- Each knowledge file mirrors one skill source, and a mirror that drops source lines needs a declared adaptation in the Sync Loop.

<!-- /ANCHOR:adr-001-context -->

---

<!-- ANCHOR:adr-001-decision -->
### Decision

**Summary**: Remove nothing, and record REQ-001 and REQ-002 as answered by the measurement.

**Details**: Every repeat carries a rule its own file needs when retrieved alone. The Story and Epic templates each carry the Delivery opt-in rule, the Doc and Story mode files each carry the clarification and Open items rules, and the board-link rule sits in each template that links a board. The Story acceptance-criteria line repeated across four examples is house text inside the artifact, and the fixture sentence repeated across three Flow examples names the fictional company each one uses.

<!-- /ANCHOR:adr-001-decision -->

---

<!-- ANCHOR:adr-001-alternatives -->
### Alternatives Considered

| Option | Pros | Cons | Score |
|--------|------|------|-------|
| **Keep every repeat** | Each retrieved file stays complete | 2,104 bytes stay | 9/10 |
| Keep each repeat in one owning file | 2,104 bytes less | A file retrieved alone loses a rule, and each cut needs a source edit and a declared adaptation | 3/10 |

**Why Chosen**: The saving is too small to pay for the rules a lone retrieved file would lose.

<!-- /ANCHOR:adr-001-alternatives -->

---

<!-- ANCHOR:adr-001-consequences -->
### Consequences

**Positive**:
- No knowledge file, skill source or Sync Loop row changes.

**Negative**:
- The set does not get smaller in this phase. Mitigation: the kernel, which loads on every turn, got 6,407 bytes smaller in phase 002.

**Risks**: None beyond the current state.

<!-- /ANCHOR:adr-001-consequences -->

---

<!-- ANCHOR:adr-001-impl -->
### Implementation

**What changes**: Nothing in the package.

**How to roll back**: Not needed, since nothing changed.

<!-- /ANCHOR:adr-001-impl -->
<!-- /ANCHOR:adr-001 -->
