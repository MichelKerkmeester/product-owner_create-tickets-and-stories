I've taken "use your recommended answers" as accepting the round-two outline as written. Barter material hasn't confirmed any of these steps, so the board's source line will say so. Here's everything I've understood. Nothing gets written to the file until you confirm this and then give a separate yes.

**The board**
- **Reader:** Support, Warehouse and Finance leads
- **Question:** who does what in a refund, and where does the work move from one team to the next?
- **Outcome:** the leads agree who owns each handoff and can see where refunds get stuck
- **Scope:** how refunds work today. No payment-provider internals and no planned changes.
- **Entry:** Support receives a refund request
- **Exits:** refund complete, refund declined, or the item fails inspection and the case goes back to Support

**Outline:** 3 lanes (Support, Warehouse, Finance), 10 boxes and 9 arrows

1. Support: Refund request received (start)
2. Support: Eligible under refund policy?
   - No → Refund declined, customer told (end)
   - Yes → Send return label
3. Send return label → Warehouse: Receive and inspect return (*first handoff*)
4. Warehouse: Item passes inspection?
   - Fail → Support: Failed inspection, case back to Support (end, *handoff*)
   - Pass → Finance: Issue refund (*handoff*)
5. Finance: Issue refund → Support: Tell customer refund is done (*handoff*)
6. Support: Refund complete (end, the goal)

**Two ways to draw it**
- **Recommended: process with lanes.** The successful path runs straight across the board and the two exits branch off beside it. Every move from one team's lane to another is visible, which answers the reader's question directly.
- **Alternative: a diagram of refund statuses** (requested, approved, returned, refunded). It shows status clearly but hides which team owns each step, so I don't recommend it.

**Layout and wording**
- **Highlighted box:** "Refund complete", the goal. I don't have delay data showing which handoff is slowest, so highlighting a step would suggest a problem the sources don't show.
- **Detail and size:** balanced detail and plain team terms, sized to read on a laptop screen
- **Grouping:** the three lanes are the only groups
- **Title:** "Refund process: Support, Warehouse, Finance"
- **Subtitle:** "Who handles each refund step and where work changes teams"
- **Source line:** "Outline accepted in chat on 26 Oct 2026, not checked against a Barter runbook"

**Assumptions to check before I draw**
- Lane order, Support then Warehouse then Finance, follows the order the work reaches each team
- All the steps come from my own outline, not a Barter source. Partial refunds, refunds without a return and Finance approval limits are left out.
- It isn't known what Support does after a failed inspection, so the board stops there. That gap will be listed under "Left out" when I deliver.

Is this how refunds work at Barter today? Reply "yes" to move on, or correct any line above.