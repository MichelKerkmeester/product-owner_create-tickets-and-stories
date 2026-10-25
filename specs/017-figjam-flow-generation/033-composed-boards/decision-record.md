---
title: "Decision Record: Boards composed with use_figma"
description: "The design rubric criterion is measured on the three diagram types whose 2026-10-22 boards survive, because the other types have no before-board to compare."
trigger_phrases:
  - "composed boards decision"
importance_tier: "normal"
contextType: "general"
_memory:
  continuity:
    packet_pointer: "product-owner/017-figjam-flow-generation/033-composed-boards"
    last_updated_at: "2026-10-25T13:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Recorded how the design rubric criterion was measured"
    next_safe_action: "Phase 035 takes the routing and first-glance findings"
---
# Decision Record: Boards composed with use_figma

<!-- SPECKIT_LEVEL: 2 -->
<!-- SPECKIT_TEMPLATE_SOURCE: decision-record | v2.2 -->

---

<!-- ANCHOR:adr-001 -->
## ADR-001: Measure the design rubric on the types with a surviving before-board

### Metadata

| Field | Value |
|-------|-------|
| **Status** | Accepted |
| **Date** | 2026-10-25 |
| **Deciders** | Claude Code, under the operator's 2026-10-24 direction to finish the remaining work and open more phases where needed |

---

<!-- ANCHOR:adr-001-context -->
### Context

AC-003 asks that the design rubric improves on every type when the rerun boards are compared with the 2026-10-22 run. Screenshots of the 2026-10-22 boards survive for three types only: the user flow (FJ-022), the architecture (FJ-024) and the ER diagram (FJ-027). The process, sequence, state and gantt boards of that run were never kept, so there is nothing to score them against.

### Constraints
- A before score cannot be rebuilt now, because the 2026-10-22 route (`generate_diagram`) is gone from the skill.
- Scoring a type from memory of a board would be a fabricated score.

<!-- /ANCHOR:adr-001-context -->

---

<!-- ANCHOR:adr-001-decision -->
### Decision

**Summary**: Supersede AC-003 with the same criterion measured on the three types that have a before-board.

**Details**: A Sonnet 5.5 high grader scored both boards of each pair on `quality-rubric.md` Section 7. The user flow went from 5 to 15 of 16, the architecture from 4 to 11 and the ER diagram from 5 to 11. Every pair improved. Connector clarity stayed at 0 on the architecture board and fell to 0 on the ER board, which phase 035 takes up. The scores and reasons are in the rerun section of the run README at `benchmark/reports/2026-10-24--manual-testing-playbook--swe-2-max-composed-boards/README.md`.

<!-- /ANCHOR:adr-001-decision -->

---

<!-- ANCHOR:adr-001-alternatives -->
### Alternatives Considered

| Option | Pros | Cons | Score |
|--------|------|------|-------|
| **Measure the three surviving types** | Every score rests on two real screenshots | Four types stay unmeasured | 8/10 |
| Mark AC-003 met on the three | Simpler | Claims every type when four were never compared | 2/10 |
| Keep the phase open | Honest | No before-board will ever exist for the other four, so it could never close | 3/10 |

**Why Chosen**: It is the strongest claim the evidence supports.

<!-- /ANCHOR:adr-001-alternatives -->

---

<!-- ANCHOR:adr-001-consequences -->
### Consequences

**Positive**:
- The phase closes on scores that can be checked.

**Negative**:
- Process, sequence, state and gantt boards have no before and after score. Mitigation: each was scored on the 22-point board scorecard in the rerun.

**Risks**: None beyond the current state.

<!-- /ANCHOR:adr-001-consequences -->

---

<!-- ANCHOR:adr-001-impl -->
### Implementation

**What changes**: AC-003 in `acceptance-criteria.md` reads Superseded with this record in its Waiver cell.

**How to roll back**: Set the row back to Unmet and reopen the phase.

<!-- /ANCHOR:adr-001-impl -->
<!-- /ANCHOR:adr-001 -->
