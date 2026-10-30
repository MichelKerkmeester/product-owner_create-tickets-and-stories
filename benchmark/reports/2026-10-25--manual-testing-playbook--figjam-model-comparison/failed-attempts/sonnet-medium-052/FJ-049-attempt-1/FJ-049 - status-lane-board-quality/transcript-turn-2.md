# FJ-049 turn 2 transcript

**User:** Use your recommended answers.

**Assistant:**

Round 2 of the intake. Your answers to round 1 stand, and I'm marking them assumed until the playback:

* Reader: Roamstay support and product
* Dials: Faithful detail, Mixed audience, Laptop distance
* Must not: show the 25 euro waiver as current behavior, or invent what happens after 7 days of silence. Both go under Left out

Three gaps remain, all in the policy's own wording.

Asking the hotel for more photos
Reading: the policy says support asks the hotel for more photos when the photos do not show the damage. It names no step and no status change. The only place it says support reads the photos is the dispute review.
Question: where does that request sit?
Recommended: a detail line on the review step ("Asks the hotel for more photos if they miss the damage"), with no loop back to the hotel lane
Why: a loop needs a return edge and a status rule the policy never states, and the review step is the one place it ties support to the photos.

Who charges the card
Reading: both the accepted path and the upheld path say the claim is charged to the card on file. Neither names who does it.
Question: which lane holds the charge?
Recommended: one shared "Charge card on file" step in the support lane, reached from the guest's accept and from the upheld verdict, carrying "Upheld claim: within 2 working days"
Why: support is the only Roamstay party in the flow, and one shared step avoids a duplicate node.

What the day counts run from
Reading: the policy gives the guest 7 days, support 5 working days and the charge 2 working days. It states no start point for any of them.
Question: should the board name a start point?
Recommended: no. The cards use the policy's words ("7 days to accept or dispute", "Decides within 5 working days") and the reply carries a Finding that the start points are unstated
Why: any start point would be mine and not the policy's.

Take the recommended answers, or correct any of them?
