---
title: "Decision Record: FigJam boards that teach the reader something"
description: "The one-row key criterion is waived for boards too narrow to hold every key entry on one row, which wrap to a second row of 144 pixels."
trigger_phrases:
  - "figjam boards that teach decision"
importance_tier: "normal"
contextType: "general"
_memory:
  continuity:
    packet_pointer: "017-figjam-flow-generation/052-figjam-boards-that-teach"
    last_updated_at: "2026-10-30T10:30:00Z"
    last_updated_by: "claude-code"
    recent_action: "Recorded Michel's waiver of the one-row key on narrow boards"
    next_safe_action: "Close the phase after the push"
---
# Decision Record: FigJam boards that teach the reader something

<!-- SPECKIT_LEVEL: 2 -->
<!-- SPECKIT_TEMPLATE_SOURCE: decision-record | v2.2 -->

---

<!-- ANCHOR:adr-001 -->
## ADR-001: Let a narrow board's key wrap to a second row

### Metadata

| Field | Value |
|-------|-------|
| **Status** | Accepted |
| **Date** | 2026-10-30 |
| **Deciders** | Michel, who chose to waive for narrow boards when asked on 2026-10-30 |

---

<!-- ANCHOR:adr-001-context -->
### Context

AC-006 asks that a composed board's key is one row at most 104 pixels tall. Eleven of the twelve boards of the rerun draw a one-row key of 88 pixels. FJ-025's second board, the declined card, is three participants wide, so its key band is narrower than its five entries and the In focus entry wraps to a second row, which makes the band 144 pixels.

### Constraints
- The key band is never wider than the board, so a narrow board has less room for its entries than a wide one.
- Shrinking the key's type on a narrow board would put it under the small type size the design sets for every board.

<!-- /ANCHOR:adr-001-context -->

---

<!-- ANCHOR:adr-001-decision -->
### Decision

**Summary**: Waive AC-006 for boards too narrow to hold every key entry on one row, and keep the wrap.

**Details**: A board wide enough for its entries keeps one row of 88 pixels, as eleven of twelve boards in the rerun do. A narrower board wraps to a second row, and its band runs 144 pixels. The renders are `renders/sonnet-medium-052-FJ-025-1-3.png` and `renders/sonnet-medium-052-FJ-025-2-151.png` in `benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison/`.

<!-- /ANCHOR:adr-001-decision -->

---

<!-- ANCHOR:adr-001-alternatives -->
### Alternatives Considered

| Option | Pros | Cons | Score |
|--------|------|------|-------|
| **Waive for narrow boards** | Closes on what the renders show, with the case named | A narrow board keeps a taller key | 8/10 |
| Fix the composer first | Could hold one row everywhere | Shrinks type under the design's floor or widens the key past the board, and needs FJ-025 rerun | 5/10 |
| Leave AC-006 Unmet | Honest | Holds the phase open on one narrow board | 3/10 |

**Why Chosen**: Michel chose it, and a wrapped key on a narrow board still reads at the design's type sizes.

<!-- /ANCHOR:adr-001-alternatives -->

---

<!-- ANCHOR:adr-001-consequences -->
### Consequences

**Positive**:
- The phase closes with every wide board at a one-row key of 88 pixels.

**Negative**:
- A narrow board's key takes 56 pixels more. Mitigation: the case is named in this record and in report section 8.17's grades.

**Risks**: None beyond the current state.

<!-- /ANCHOR:adr-001-consequences -->

---

<!-- ANCHOR:adr-001-impl -->
### Implementation

**What changes**: AC-006 in `acceptance-criteria.md` reads Waived with this record in its Waiver cell.

**How to roll back**: Set the row back to Unmet and reopen the phase.

<!-- /ANCHOR:adr-001-impl -->
<!-- /ANCHOR:adr-001 -->
