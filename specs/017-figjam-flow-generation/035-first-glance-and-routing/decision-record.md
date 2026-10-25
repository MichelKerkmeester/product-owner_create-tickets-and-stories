---
title: "Decision Record: First glance, routing and reply fixes"
description: "The Composition criterion is waived for FJ-030, whose one lost point rests on a split judgment about zone tints that would change every zoned board to fix."
trigger_phrases:
  - "first glance and routing decision"
importance_tier: "normal"
contextType: "general"
_memory:
  continuity:
    packet_pointer: "product-owner/017-figjam-flow-generation/035-first-glance-and-routing"
    last_updated_at: "2026-10-25T16:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Recorded the operator's waiver of the FJ-030 Composition point"
    next_safe_action: "Weigh tinting only the first-glance zone in a later pass"
---
# Decision Record: First glance, routing and reply fixes

<!-- SPECKIT_LEVEL: 2 -->
<!-- SPECKIT_TEMPLATE_SOURCE: decision-record | v2.2 -->

---

<!-- ANCHOR:adr-001 -->
## ADR-001: Waive Composition on FJ-030 and keep the zone tints

### Metadata

| Field | Value |
|-------|-------|
| **Status** | Accepted |
| **Date** | 2026-10-25 |
| **Deciders** | The operator, who chose to waive and close when asked on 2026-10-25 |

---

<!-- ANCHOR:adr-001-context -->
### Context

AC-004 asks that Composition scores 2 on every scored board of the rerun. After the main run, the recheck and a second recheck, every scored board scores 2 except FJ-030 (board 107:4292), which scores 1 of 2 and 21 of 22 in total. Its grader found the wide orange Request the return zone and its two yellow diamonds reading before the pink-ringed Return confirmed in the narrow Done zone. The model's plan was right and the gate named it. The grader traced the loss to the composer's zone tint cycle and proposed tinting only the zone that holds the first-glance node.

### Constraints
- The grader called the ring and the zone close to a tie, resting on one fresh reader and its own look.
- The second Composition lens of the main run scored the same plan on FJ-030 a 2, and FJ-022 scores 2 from both lenses with the same zones and the same orange zone.
- Zone tints apply to every zoned board, and lanes on architecture boards depend on cycling tints so neighbouring lanes read apart (FJ-034 passes on that).

<!-- /ANCHOR:adr-001-context -->

---

<!-- ANCHOR:adr-001-decision -->
### Decision

**Summary**: Waive AC-004 for FJ-030 alone and keep the zone tint cycle as it is.

**Details**: Every other scored board meets the criterion and FJ-030 misses it by one point on a split judgment. Changing the tints would touch every zoned board on evidence from one reader, and would need FJ-022, FJ-023, FJ-029, FJ-030 and FJ-036 rerun to show nothing else regresses. Tinting only the first-glance zone stays a candidate for a later pass. The grades are `grades/g11-035-fj030.md` and `grades/g8-035-composition-second-lens.md` in `benchmark/reports/2026-10-25--manual-testing-playbook--first-glance-and-routing/`.

<!-- /ANCHOR:adr-001-decision -->

---

<!-- ANCHOR:adr-001-alternatives -->
### Alternatives Considered

| Option | Pros | Cons | Score |
|--------|------|------|-------|
| **Waive and close** | Closes on scores that can be checked, with the miss named | FJ-030 stays a FAIL in the run record | 8/10 |
| Tint only the first-glance zone | Could lift FJ-030 to a full Composition | Changes every zoned board on one reader, needs five scenarios rerun | 5/10 |
| Keep the phase open | Honest | Blocks the parent on a near tie | 3/10 |

**Why Chosen**: The operator chose it, and it is the strongest claim the evidence supports.

<!-- /ANCHOR:adr-001-alternatives -->

---

<!-- ANCHOR:adr-001-consequences -->
### Consequences

**Positive**:
- The phase closes with every other scored board at Composition 2.

**Negative**:
- A wide saturated zone can still outweigh a small first-glance node. Mitigation: the candidate fix is named in the run README's Open section.

**Risks**: None beyond the current state.

<!-- /ANCHOR:adr-001-consequences -->

---

<!-- ANCHOR:adr-001-impl -->
### Implementation

**What changes**: AC-004 in `acceptance-criteria.md` reads Waived with this record in its Waiver cell.

**How to roll back**: Set the row back to Unmet and reopen the phase.

<!-- /ANCHOR:adr-001-impl -->
<!-- /ANCHOR:adr-001 -->
