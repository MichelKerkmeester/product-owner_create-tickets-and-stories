Round 1 is settled on the recommended answers. They stay marked assumed, and nothing is written yet.

Settled so far:
* Reader: the Roamstay product team, assumed
* Question: which screens a guest passes through to change dates and where it branches, assumed
* Outcome: agree the branches before design and build, assumed
* Left out: card entry and payment failures, cancellation, change fees and deadlines, assumed
* Entry and exit: captured from your request. Entry is the booking page and exit is the updated booking

Entry and exit are already settled, so round 2 covers actors and the gaps your answers opened.

1. Actors
   * Reading: the guest taps, picks dates and pays. Nothing in the request says who runs the availability check, the price comparison or the credit
   * Question: who takes each step?
   * Recommended: the guest does Change dates, the date pick and the payment, and the system does the availability check, the price comparison, the credit and the no-charge case
   * Why: the system steps get marked automatic, so they are not read as missing guest actions

2. After other rooms
   * Reading: the request says the guest sees other rooms but not what happens next, and it doesn't cover the case where no other room is free
   * Question: what happens after the guest sees the other rooms?
   * Recommended: the guest picks one, as a single "Choose another room" screen, and the flow rejoins at the price comparison. The no-other-room case is not drawn and goes under Left out
   * Why: the price outcomes depend on the room and dates chosen, and this keeps the board at 9 nodes

3. Source class
   * Reading: the description is in the present tense, but no screens or spec came with it
   * Question: is this current behavior, approved direction or a proposal?
   * Recommended: current behavior, marked assumed, to be settled by a link to the screens or the spec. Labels use your wording (Booking page, Change dates)
   * Why: a proposal would have to carry its status in the node labels, so I'd rather you correct me now than after the board is drawn

If you answer these or say "use the recommended answers" again, the next reply is the full playback: the question, the outcome, the nodes and connectors as a checked model, and every assumed row, for your answer before the write gate.