Two notes give different release rules for the same behavior, and neither has authority over the other. Recency and note order can't settle it, so I've stopped before drafting and put the question in the block below.

````markdown
<!-- Mode: Doc | Clarification | Energy: Standard -->

I'll create the payout pause behavior reference. Before drafting, I need the unresolved decisions below in one response:

**Conflict to resolve:** The two notes disagree on how a payout pause ends.

*   **Note A:** the pause holds for 24 hours, then releases automatically
*   **Note B:** the pause holds until the brand clears it manually

Which note governs, and for what scope? Both could be true if they describe different cases, such as different pause triggers, plan types or time periods. If so, please say which case each covers.

**Authority:** Who or what makes that call? For example, a named owner, a shipped implementation, or a spec. I can't pick a winner by recency or by note order.

**Document status:** Should the reference describe current behavior, approved direction, a proposal, retired material or unknown? If one note describes an older or planned behavior, tell me which one and how to label it.

**Source set:** Are Notes A and B the only sources? Neither says what starts a pause, who can start one, what the brand sees, or what happens to the held payout. I won't invent those. Please supply a source or confirm they are out of scope.

**Audience and purpose:** Who will read this, and what should they be able to predict or decide after reading it?

**Shape:** You asked for a behavior reference, which fits a reader who needs to predict states and outcomes. Please confirm, or name another shape.

**Scope and depth:** What should be included or excluded, and how much technical detail does the audience need?
````

Export-equivalent path: `export/NNN - doc-payout-pause-behavior-reference-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none needed. Kept with reason: none.

Once you answer, I'll draft the behavior reference. If the answer is that the two notes describe different cases, I'll document both, each labelled with its own scope and status.