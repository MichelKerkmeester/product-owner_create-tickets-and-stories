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

---

<!-- ANCHOR:operator-decisions -->
## Operator Decisions

| ID | Decided | Why | Supersedes | Carried by |
|----|---------|-----|------------|------------|
| Q001 | The Alex scope doc is not pushed to ClickUp yet. | Not stated. | None | Alex board work in FigJam file 1wnDhiAc8bTRsLrilq4oKo, no packet task |
| Q002 | The first FigJam file holds one combined board. | Not stated. | None | Alex board work in FigJam file 1wnDhiAc8bTRsLrilq4oKo, no packet task |
| Q003 | Alex reads the board, shared on a call. | Not stated. | None | Alex board work in FigJam file 1wnDhiAc8bTRsLrilq4oKo, no packet task |
| Q004 | Each board step carries balanced detail. | Not stated. | None | Alex board work in FigJam file 1wnDhiAc8bTRsLrilq4oKo, no packet task |
| Q005 | The reading of the first board was confirmed. | Not stated. | None | Alex board work in FigJam file 1wnDhiAc8bTRsLrilq4oKo, no packet task |
| Q006 | The board goes into a new FigJam file in the Barter B.V. team. | Not stated. | None | Alex board work in FigJam file 1wnDhiAc8bTRsLrilq4oKo, no packet task |
| Q007 | The reading of the three boards was confirmed. | Not stated. | None | Alex board work in FigJam file 1wnDhiAc8bTRsLrilq4oKo, no packet task |
| Q008 | The request handling board follows Rafael flow plus park and decline outcomes. | Not stated. | None | Alex board work in FigJam file 1wnDhiAc8bTRsLrilq4oKo, no packet task |
| Q009 | All three boards are written into the existing FigJam file. | Not stated. | None | Alex board work in FigJam file 1wnDhiAc8bTRsLrilq4oKo, no packet task |
| Q010 | Boards 1 and 2 are redrawn with joined arrows and the section name tabs are cleared. | Not stated. | None | Alex board work in FigJam file 1wnDhiAc8bTRsLrilq4oKo, no packet task |
| Q011 | The old board 3 (6:394) is deleted and the combined board stays. | Not stated. | Earlier board versions | Alex board work in FigJam file 1wnDhiAc8bTRsLrilq4oKo, no packet task |
| Q012 | Export 002 is updated to match the boards. | Not stated. | None | Alex board work in FigJam file 1wnDhiAc8bTRsLrilq4oKo, no packet task |
| Q013 | The What Alex no longer does board gets more detail and a better layout. | Not stated. | None | Alex board work in FigJam file 1wnDhiAc8bTRsLrilq4oKo, no packet task |
| Q014 | The old 6-card board 22:584 is deleted. | Not stated. | Earlier board versions | Alex board work in FigJam file 1wnDhiAc8bTRsLrilq4oKo, no packet task |
| Q015 | Board 4 returns to the card layout with arrows. | Not stated. | None | Alex board work in FigJam file 1wnDhiAc8bTRsLrilq4oKo, no packet task |
| Q016 | The new page holds one merged timeline, made a lot clearer and more readable. | Not stated. | None | Alex board work in FigJam file 1wnDhiAc8bTRsLrilq4oKo, no packet task |
| Q017 | All four bundles of FigJam skill changes are applied. | Not stated. | None | REQ-010, AC-010, T010, T011 |
| Q018 | The session answers are recorded in packet 052. | Not stated. | None | decision-record.md |
| Q019 | The board lane note keeps "Project Manager / Owner". | Not stated. | None | Alex board work in FigJam file 1wnDhiAc8bTRsLrilq4oKo, no packet task |
| Q020 | The single board is replaced by dedicated boards for request handling, project manager scope and Product Owner scope. | The user called the combined board bad. Evidence: open_value, option not_applicable, overlap 3, imperative false, shift false. | The one combined board answer | Alex board work in FigJam file 1wnDhiAc8bTRsLrilq4oKo, no packet task |
<!-- /ANCHOR:operator-decisions -->

---

<!-- ANCHOR:operator-answers-verbatim -->
## Appendix: Verbatim Operator Answers

Each appendix item uses the same id as its operator decision. The options are included so the record preserves the full offered choice set.

### Q001
<!-- source: claude:88e2233f-4654-4867-a184-17ec8ed1436b:toolu_017GhXUAZEPkHVR7UMgGk5Th:0 -->

Question:
```text
Where in ClickUp should the Alex scope and responsibilities doc go?
```

Options:
```text
Private ClickUp doc (Recommended)
Product Wiki
Don't push yet
```

Answer:
```text
Don't push yet
```

### Q002
<!-- source: claude:88e2233f-4654-4867-a184-17ec8ed1436b:toolu_016hQ2136o3Kyys6HcfcsXKn:0 -->

Question:
```text
What should the FigJam file hold?
```

Options:
```text
Two boards (Recommended)
Request flow only
One combined board
```

Answer:
```text
One combined board
```

### Q003
<!-- source: claude:88e2233f-4654-4867-a184-17ec8ed1436b:toolu_016hQ2136o3Kyys6HcfcsXKn:1 -->

Question:
```text
Who reads the board, and where?
```

Options:
```text
Alex, shared on a call (Recommended)
Alex, on her laptop
Michel and Rafael only
```

Answer:
```text
Alex, shared on a call (Recommended)
```

### Q004
<!-- source: claude:88e2233f-4654-4867-a184-17ec8ed1436b:toolu_016hQ2136o3Kyys6HcfcsXKn:2 -->

Question:
```text
How much detail should each step carry?
```

Options:
```text
Balanced (Recommended)
Simplified
Faithful
```

Answer:
```text
Balanced (Recommended)
```

### Q005
<!-- source: claude:88e2233f-4654-4867-a184-17ec8ed1436b:toolu_01GHfqhCbxReCAGMDVPCGuMw:0 -->

Question:
```text
Is this reading of the board right?
```

Options:
```text
Yes, reading is right (Recommended)
Change the highlight
Split into two boards
```

Answer:
```text
Yes, reading is right (Recommended)
```

### Q006
<!-- source: claude:88e2233f-4654-4867-a184-17ec8ed1436b:toolu_016vBa51J6HP2MbqdE38CaFh:0 -->

Question:
```text
Write the board to a new FigJam file named 'Alex: from request to release'?
```

Options:
```text
Yes, in Barter B.V. (Recommended)
Yes, in my personal plan
Not yet
```

Answer:
```text
Yes, in Barter B.V. (Recommended)
```

### Q007
<!-- source: claude:88e2233f-4654-4867-a184-17ec8ed1436b:toolu_01DEV6pMa3CmNDydkH5qXqvR:0 -->

Question:
```text
Is this reading of the three boards right?
```

Options:
```text
Yes, reading is right (Recommended)
Drop 'Build the feature'
Separate file
```

Answer:
```text
Yes, reading is right (Recommended)
```

### Q008
<!-- source: claude:88e2233f-4654-4867-a184-17ec8ed1436b:toolu_01Kg8bAYa21k1ZdHX88LyQsg:0 -->

Question:
```text
Rafael's board sends every 'no impact' request to 'track it down until done', while the doc lets Alex park or decline it. Which should the request handling board follow?
```

Options:
```text
Rafael's flow + park/decline (Recommended)
Rafael's flow exactly
Rafael's flow, decline only
```

Answer:
```text
Rafael's flow + park/decline (Recommended)
```

### Q009
<!-- source: claude:88e2233f-4654-4867-a184-17ec8ed1436b:toolu_01KwtetRPpRqAUV26MnrP1Ad:0 -->

Question:
```text
Write the three boards (1. Request handling, 2. Project manager scope, 3. Product Owner scope) into the existing 'Alex: from request to release' FigJam file?
```

Options:
```text
Yes, write all three (Recommended)
Yes, in a new file
Not yet
```

Answer:
```text
Yes, write all three (Recommended)
```

### Q010
<!-- source: claude:88e2233f-4654-4867-a184-17ec8ed1436b:toolu_01DXF7PHwbNuGxR2nEqrk9ZL:0 -->

Question:
```text
Redraw boards 1 and 2 with joined arrows (four request sources into Checks, four arrows into Stakeholders informed) and clear the section name tabs on all three boards?
```

Options:
```text
Yes, redraw 1 and 2 (Recommended)
Only clear the tab names
Hold, I fix arrows by hand
```

Answer:
```text
Yes, redraw 1 and 2 (Recommended)
```

### Q011
<!-- source: claude:88e2233f-4654-4867-a184-17ec8ed1436b:toolu_01Eqw3NrovLhu6QYdQuE2riP:0 -->

Question:
```text
Boards 1, 2 and 3 are redrawn in the FigJam file. Two old boards are still on the page: the first version of board 3 ("3. Product Owner scope", 6:394) and the first combined board ("Alex: from request to release", 1:3). Which should I delete?
```

Options:
```text
Old board 3 (6:394) (Recommended)
Combined board (1:3)
```

Answer:
```text
Old board 3 (6:394) (Recommended)
```

### Q012
<!-- source: claude:88e2233f-4654-4867-a184-17ec8ed1436b:toolu_01Eqw3NrovLhu6QYdQuE2riP:1 -->

Question:
```text
The doc still says "record the reason where everyone can see it", and its Product Owner section doesn't have the new feature flow. Should I update export 002 to match the boards?
```

Options:
```text
Yes, update the doc (Recommended)
No, boards only
```

Answer:
```text
Yes, update the doc (Recommended)
```

### Q013
<!-- source: claude:88e2233f-4654-4867-a184-17ec8ed1436b:toolu_01BJfmMzm7y7PySyjLGPg2qE:0 -->

Question:
```text
You said a board needs a lot more detail and a better layout. Your screenshot (#12) didn't come through, so which board do you mean?
```

Options:
```text
What Alex no longer does
Overview
Board 3, Product Owner scope
Board 1 or 2
```

Answer:
```text
What Alex no longer does
```

### Q014
<!-- source: claude:88e2233f-4654-4867-a184-17ec8ed1436b:toolu_012FP5r8mvzRaACF5QJ6prr4:0 -->

Question:
```text
The detailed "What Alex no longer does" board (33:430) is built to the right of the old 6-card version (22:584). Should I delete the old board 22:584?
```

Options:
```text
Delete 22:584 (Recommended)
Keep both
```

Answer:
```text
Delete 22:584 (Recommended)
```

### Q015
<!-- source: claude:88e2233f-4654-4867-a184-17ec8ed1436b:toolu_012ngvS2xWcKgoHbsJh4gaks:0 -->

Question:
```text
Which earlier version of board 4 should I go back to?
```

Options:
```text
Card layout with arrows
Neutral grey tables
Tables, first colours
```

Answer:
```text
Card layout with arrows
```

### Q016
<!-- source: claude:88e2233f-4654-4867-a184-17ec8ed1436b:toolu_01VUDy1sEugjdNGpQhkkrNzx:0 -->

Question:
```text
For the new page, what should the one big board be?
```

Options:
```text
One merged timeline
All boards in one frame
Copy of the overview
```

Answer:
```text
go for 1 BUT MAKE A LOT CLEARER AND READABLE
```

### Q017
<!-- source: claude:88e2233f-4654-4867-a184-17ec8ed1436b:toolu_01QCcoxPnfX8LgjiJc3eLbe9:0 -->

Question:
```text
Which bundles of FigJam skill changes should I apply? The proposed bundles are: 1) a route for hand-edited boards with backup pages, a 660-pixel column grid and a fix to the wrong one-page rule, 2) arrow label rules (bold key, bold short labels, one line, placement), 3) copy checks (no single word alone on its own line, your forced line breaks treated as intent), 4) companion sync (.md and A4 pages) and Key arrow samples that render.
```

Options:
```text
1. Hand-edited boards
2. Arrow labels
3. Copy checks
4. Companions and Key
```

Answer:
```text
1. Hand-edited boards, 2. Arrow labels, 3. Copy checks, 4. Companions and Key
```

### Q018
<!-- source: claude:88e2233f-4654-4867-a184-17ec8ed1436b:toolu_01M7nyrCr62saHRBTUgYwogJ:1 -->

Question:
```text
The session hook reports 17 of your answers from this session that aren't in a decision record yet. Should I record them in packet 052 with /speckit:save?
```

Options:
```text
Save to packet 052 (Recommended)
Skip
```

Answer:
```text
Save to packet 052 (Recommended)
```

### Q019
<!-- source: claude:88e2233f-4654-4867-a184-17ec8ed1436b:toolu_01M7nyrCr62saHRBTUgYwogJ:2 -->

Question:
```text
The Alex lane note on the board still reads "Project Manager / Owner", while every doc says "Project Manager / Product Owner". Which should the board say?
```

Options:
```text
Product Owner (Recommended)
Keep "Owner"
```

Answer:
```text
Keep "Owner"
```

### Q020
<!-- source: claude:88e2233f-4654-4867-a184-17ec8ed1436b:chat:5a09ca42-915e-478b-8b3f-43c136e7f30f:cddfb32f-15cb-4b70-bcff-1747266e59c1 -->

Question:
```text
https://www.figma.com/board/1wnDhiAc8bTRsLrilq4oKo
Read-back: 9 of 9 nodes, 10 of 10 connectors, 4 of 4 decision exits labelled, 4 of 4 lanes in order (Requester, Alex, Michel, Rafael), first glance: Build it?
Left out: Learning the apps and back office, an ongoing duty rather than a step in the flow
Left out: Priority and QA as steps of their own, folded into the stories and kick-off cards to keep to one board. A two-board split stays available
Finding: The label "Which impact?" wraps with "impact?" alone on its second line, as named before the write
Finding: The doc `export/002 - doc-alex-scope-and-responsibilities.md` doesn't link to this board yet. Say if you want the link added under related references
Finding: The board is in the Barter B.V. plan, in your drafts. Before Alex sees it, move it to a shared project
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.
```

Options: none

Answer:
```text
Bad board.

We need a dedicated request handling board

We need a dedicated project manager scope board

And product owner scope board
```

<!-- /ANCHOR:operator-answers-verbatim -->
