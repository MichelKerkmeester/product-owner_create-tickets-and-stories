Here is the full playback of the reading. Nothing is drawn or written yet.

**What the board answers**
* Question: who does what, in which order, and where does a damaged-item claim change hands between the customer, CS and the warehouse?
* Outcome: the product team can see where a claim leaves CS for the warehouse and what each team does at that point
* Dials: Balanced, Mixed, Laptop

**What each source settled**
* The support runbook (current behavior) gave the three actors, the entry through the help form, the CS decision with its two exits, the warehouse steps in order, the three timings and the claims table
* Your request gave the first glance, the handoff to the warehouse
* The under 20 euro pickup skip is a proposal because the pilot is not live, so it stays off the board

**Rows I assumed**
* Reader and outcome: the product team
* The pilot is left off the board
* The dials above
* The customer sends the second photo. The runbook says CS asks for it, so the customer step and its loop back to the photo check are my reading
* Still open: a photo with no damage, a second photo that is still unclear, an inspection that does not match, and whether the refund waits on the inspection result. They stay undrawn

**The outline**
Nodes, in drawing order, with the lane and the Brief row each answers:
1. Customer reports damage: start, Customer lane (Entry)
2. Check the photo: CS agent (Actors)
3. Damage clear?: decision, CS agent (Decisions)
4. Ask for a second photo: CS agent (Decisions)
5. Send second photo: Customer, assumed (Actors)
6. Approve the claim: CS agent, the step in focus (First glance)
7. Claims table: store (Sources)
8. Book courier pickup: Warehouse operator (Actors)
9. Inspect on arrival: Warehouse operator (Actors)
10. Refund released: end, Warehouse operator (Exit)

Connectors, 10 in all:
* Customer reports damage to Check the photo
* Check the photo to Damage clear?
* Damage clear? to Approve the claim, labelled Clear
* Damage clear? to Ask for a second photo, labelled Unclear
* Damage clear? to Claims table, labelled Decision logged
* Ask for a second photo to Send second photo
* Send second photo back to Check the photo
* Approve the claim to Book courier pickup, labelled Claim queued
* Book courier pickup to Inspect on arrival
* Inspect on arrival to Refund released

The warehouse queue is a label on the handoff connector, not a node, because it only carries the claim from one lane to the next. The remove test cut nothing else. The board is 10 nodes against a lane budget of 12.

**Two framings**
* Lanes by actor: the handoff is a connector that crosses from the CS lane to the warehouse lane, and the timings sit in lane notes. It costs a little width. Recommended, because who hands to whom is the question
* Stages without lanes: Report, Check and Warehouse as zones. It is more compact but hides who acts, so the handoff reads as a zone change

**The look**
* Accent: Approve the claim, with the reason "claim leaves CS for warehouse", and Refund released named as the goal
* Title: Damaged-item refund. Subtitle: From a damage report to a released refund, for the product team
* Lane notes: Customer shows "Help form asks: order number, photo, short description". CS agent shows "Answers within 1 working day" and "Every decision is logged in the claims table". Warehouse shows "Books the pickup for the next working day" and "Refund within 5 working days of the inspection"
* Bodies: Book courier pickup shows "Next working day". Inspect on arrival shows "Held against the customer's photo"
* Source line: the support runbook. Left out: the under 20 euro pilot, the three silent paths and the refund-after-inspection condition

Is this reading right, or should I change any row before I model it?