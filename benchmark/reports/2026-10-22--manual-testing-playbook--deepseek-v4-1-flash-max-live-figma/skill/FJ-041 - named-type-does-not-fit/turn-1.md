**The reading**
The board shows the states of one thing, the return request, from an open order to the confirmation. A state diagram fits because the split between refund and store credit is the decision the flow exists to explain, and a list would flatten it.

| Row | Reading |
|---|---|
| Reader | Fernhouse Product team, assumed |
| Question | Which states does a return request pass through, and what moves it between them? |
| Outcome | Agree the state set and the split between refund and store credit before stories or screens are written, assumed |
| Scope | An open order to the confirmation. Post-confirmation handling sits outside this board |
| Entry | An order is open and the customer can start a return |
| Exit | Confirmation shown |
| Actors | Customer, with the system showing the confirmation. A state diagram labels events, not lanes |
| Decisions and states | Reason picked, then refund or store credit, then confirmed |
| Sources and class | Your description and the Fernhouse context. Class: proposal |

The Fernhouse context, updated 18 September, says "There is no self-serve return today" and describes returns created by CS in Admin. That is why the class is proposal, and why the title will say "proposed". If the flow is live, say so and the word goes.

The board must not present the flow as live behavior, and it stops at the confirmation.

**The outline**
- OrderOpen to ReturnStarted: tap Return an item
- ReturnStarted to ReasonSelected: pick a reason
- ReasonSelected to RefundSelected: choose refund
- ReasonSelected to StoreCreditSelected: choose store credit
- RefundSelected to Confirmed: confirmation shown
- StoreCreditSelected to Confirmed: confirmation shown

Six states and eight transitions with the entry and exit arrows. The pre-write check passes. The one assumed edge is "confirmation shown", because you did not name a separate submit tap.

The 30-day return window and the delivered-order condition are left out, because the request starts from an open order.

The alternative framing is the current CS-led return. That is who does what across customer, CS agent and warehouse, so it is a process rather than a state diagram.

**The gate**
The board answers which states a return request passes through, and what moves it between them. The reader can then agree the state set and the split before build.

- First glance: the split at ReasonSelected into refund and store credit
- Second glance: the path from OrderOpen into ReturnStarted
- Last glance: Confirmed

Plan: open. "Fernhouse Product" is not on the connected Figma account. The plans are <figma-plan-3> (Starter, View), <figma-plan-1> (Pro, Full) and <figma-plan-2> (Pro, member). I recommend <figma-plan-1>, because its Full seat can run the write and the read-back. The personal plan is Starter with a View seat, which caps tool calls at six a month. If Fernhouse Product is a project inside one of these plans, name the plan that holds it.

File: a new FigJam file, which the first call creates
Writes: one state diagram, six states and eight transitions, named "Fernhouse return request states (proposed)", with a title text above it. No extension and no colour
Reads: whoami is done. One get_figjam read-back after the write
Rollback: delete the new file. Nothing existing is touched

Name the plan and say write it, and I'll draw the board.