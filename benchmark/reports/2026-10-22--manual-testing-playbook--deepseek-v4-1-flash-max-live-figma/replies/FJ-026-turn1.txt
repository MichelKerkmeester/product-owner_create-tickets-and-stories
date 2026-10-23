Nothing is written yet. The account has no plan called Roamstay Product, so the target needs settling before the write gate can open.

**Reading**
- Reader: support, checking which bookings have ended
- Question: which statuses a booking passes through, and what moves it between them
- Outcome: support tells a live booking from an ended one at a glance
- Entry: Pending, before the card is authorised
- Exit: Completed, Cancelled and No-show
- States: Pending, Confirmed with Upcoming and In stay inside it, Completed, Cancelled, No-show
- Moves: card authorised, check in, check out, guest cancels, missed check-in
- Source: your request, read as how bookings work today

State diagram, 7 states and 12 transitions. `Confirmed` is a composite, so check out and no-show leave the composite because Mermaid will not draw a move from a substate to an outside state. The pre-write check passes.

**Plan.** The account has three plans: <figma-plan-3> (Starter, View seat), <figma-plan-1> (Pro, Full seat) and <figma-plan-2> (Pro, Full seat). None is Roamstay Product. Which one should own the new board? <figma-plan-1> is the recommendation, because it is the Pro plan you administer. The Starter plan's View seat caps tool calls at six a month, and one write plus its read-back can use that up. If Roamstay Product is a project inside a team, name the team, because the diagram tool creates the board in the plan and not in a project folder.

**Declined card.** The request says Pending until the card is authorised and says nothing about a failed authorisation. Recommended: leave it out and name it as a gap rather than invent a state. Say if support needs a Payment failed or Expired state.

**Colour.** The end states read as Completed, Cancelled and No-show. One light gray tint with a dashed stroke goes behind each, and a one-entry key names the group `Ended`. Gray reads as closed, so the three end states do not compete as three separate alerts.

Tell me which plan should own the board and I'll bring the write gate with the file, the extension and the rollback.