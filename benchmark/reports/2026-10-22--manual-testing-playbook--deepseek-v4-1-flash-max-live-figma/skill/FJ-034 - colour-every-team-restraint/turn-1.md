**Reading**
The board answers one sentence: who does what in a damaged-item refund, in which order and where the work changes hands. That is a process with one lane per team, not a user flow.

Scope is the damaged-item refund only, from the customer's first report to the released refund. The general return flow stays off this board.

*   Start: Customer reports damage with a photo
*   CS agent checks the photo
*   Decision `Damage clear?`
    *   Clear: the CS agent approves the refund
    *   Unclear: the customer sends a second photo, which returns to the same check
*   CS agent hands the approved refund to the warehouse
*   Warehouse operator books a courier pickup, inspects the item and releases the refund
*   End: Refund released

**Team colour**
Team ownership is carried by the lane, one each for Customer, CS agent and Warehouse operator, in the order work reaches them. A separate fill per team is not available here. The pre-write palette check allows one accent, and three team fills count as three accents and fail the model. The accent sits on the CS-to-warehouse handoff, where the refund waits. Literal team fills would be a manual recolour in FigJam after the board lands.

**Assumption**
The Fernhouse context gives the refund to the CS agent in the general return flow. This board follows your wording, with the warehouse operator releasing it. Say if CS should release it instead.

**Target plan**
No plan on this Figma account is named Fernhouse Product. The account holds:

*   <figma-plan-1>, Pro, Full seat, you are admin
*   <figma-plan-2>, Pro, Full seat, you are a member
*   <figma-plan-3>, Starter, View seat

This session is signed in as <email>, so a plan under another login would not appear. A project folder cannot be a write target for the diagram call, so the file lands in the plan and can be moved into the folder afterwards.

Recommended: <figma-plan-1>, the Pro plan where you hold admin and a Full seat.
Why: the other Pro plan gives you a member seat, and the Starter plan is a View seat with a six-call monthly limit. A board in <figma-plan-1> is visible to that plan's members.

**Ready once the plan is set**
*   File: a new FigJam file, which the write creates
*   Content: one process, 3 lanes, 7 nodes, 7 connectors, 2 labelled decision exits
*   Writes: the diagram and its title, `Damaged-item refund`
*   Extensions: none
*   Reads: one `get_figjam` read-back with screenshots
*   Rollback: delete the new file
*   Pre-write check: passed, 0 crossing pairs

Which plan should hold the board, and is Fernhouse Product a project folder inside it? Answer with the plan and a yes, and I'll write it.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.