Round 1 of 3. This is a user flow, because the board answers which screens a guest passes through and where they choose. The only source is your description, so each question gives my reading and a recommended answer. An unanswered question stands on the recommendation, marked assumed.

Settled from your request:
* Type: user flow
* Entry: the booking page, where the guest taps Change dates
* Exit: the guest sees the updated booking
* Decisions: is the room free on the new dates, and is the new price higher, lower or the same
* Target: a new section in the existing file <draft-file-key>. Nothing already in it changes, and no new file or plan lookup is needed

Open for later rounds:
* Where the guest goes after seeing other rooms
* Whether the description is current behavior or a proposal
* Who acts at the price step, the guest or the system

Size: the path comes to about 9 nodes, which is the limit for a user flow. I'm planning to carry the Change dates tap as the label on the connector out of the booking page, so it stays one board. I'll confirm that at the playback.

1. Reader and question
   * Reading: nothing says who opens the board or what they bring to it
   * Question: who reads it, and what do they want answered?
   * Recommended: the Roamstay product team (product, design and engineering), asking "which screens does a guest pass through to change dates, and where does it branch?"
   * Why: the request describes screens and choices, not teams or systems, so a user flow fits that reader

2. Outcome
   * Reading: the request gives the path but not what the reader does with it
   * Question: what should the reader be able to decide after reading?
   * Recommended: agree the branches (room not free, price higher, lower or same) before design and build
   * Why: the branches are the part of your description with more than one outcome

3. What the board must not do
   * Reading: the request covers the guest-facing path only, with no source for failures or policy
   * Question: what should the board leave out?
   * Recommended: leave out card entry and payment failures, cancellation, change fees and deadlines, and anything the guest does not see
   * Why: none of those appear in your description, so drawing them would invent behavior

Do you want to answer these, or say "use the recommended answers" and I'll move to round 2?