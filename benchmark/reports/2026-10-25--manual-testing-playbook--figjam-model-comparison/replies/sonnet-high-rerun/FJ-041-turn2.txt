Type settled as user flow, so the state diagram is out. Here is my reading before I model anything, with every row you haven't confirmed marked assumed.

**Question the board answers:** which screens does a customer pass through to return an item, and where do they choose between refund and store credit?

**Rows**
* Reader: the Fernhouse team reviewing the return journey. Assumed, you can correct it
* Question: as above. Captured, from the type you picked
* Outcome: the reader sees the whole path and its one choice. Assumed
* Entry: the customer opens an order. Captured
* Exit: the confirmation is shown. Captured
* Actors: the customer takes each step and the confirmation appears on screen. Captured
* Decision: refund or store credit, two exits. Captured
* Scope: the happy path only, from an open order to the confirmation. Assumed
* Source and class: your request alone, with no screenshots or doc. I'm reading it as current behavior. Assumed, and it flips to a proposal if you tell me the flow isn't live
* Exits: both land on the same confirmation, because you described one. Assumed, and it changes if refund and store credit show different confirmations

**What the board must not do:** show back-out paths, eligibility rules, failures or screens beyond your five steps. You supplied none of them, so drawing them would invent them. Assumed.

**List or board:** a list would carry five steps. The board earns its place through the choice with two labelled exits.

**Outline, in drawing order**
1. Open an order (start)
2. Tap Return an item
3. Pick a reason
4. Refund or store credit? (decision)
5. Confirmation shown (goal)

Connectors run 1 to 2, 2 to 3, 3 to 4, then 4 to 5 twice, labelled Refund and Store credit. That is 5 nodes and 5 connectors. The remove test cuts nothing, because each step is one you named. If the check refuses two exits into one node, a merge dot takes them and adds a sixth node.

**Two framings**
* A, recommended: the happy path alone. It reads in tap order and nothing competes with the choice, but it doesn't show where a customer can back out
* B: the happy path plus the ways out, such as backing out, no reason fitting or an item that can't be returned. It shows every exit but needs a source for each, and you gave none

**Look**
* First glance: the "Refund or store credit?" decision, with the pink outline. It is the only place the customer chooses, which is what the question asks
* Second glance: the two labelled exits and the green confirmation they reach
* Last glance: the start pill and the source line
* Zones: none, since five steps need no grouping
* Title: Fernhouse return flow
* Subtitle: how a customer returns an item from an open order, ending on the confirmation
* Source line: the request. Not in it: back-out paths, eligibility rules and failures
* Detail balanced, audience mixed, read on a laptop

Does this reading hold? Say yes to move on, or name the row to change.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.