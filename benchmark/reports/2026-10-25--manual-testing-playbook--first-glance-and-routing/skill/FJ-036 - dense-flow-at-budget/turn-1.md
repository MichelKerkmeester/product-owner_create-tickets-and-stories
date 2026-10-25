Nothing is written yet. This is round one of the intake, and I haven't touched the file.

**What I have so far**

* Type: user flow, because the question is which screens and choices a guest passes through
* Entry: the booking page, where the guest taps Change dates
* Exit: the updated booking
* Actors: the guest picks the dates, and I read the room check and the price comparison as automatic system steps
* Decisions: room free or not, then new price against current price with three exits (higher, lower, same)
* Price outcomes: higher means the guest pays the difference, lower means the difference comes back as credit, same means nothing is charged
* Target: a new board in `<test-file-key>`, with no new file. I read "Roamstay Product plan" as the plan that file sits in. I can't confirm that from here, so the write gate will name it as you gave it.

**Question 1: who reads this board, and what do they decide afterwards?**

Reading: your request doesn't say who the board is for.
Recommended: the Booking squad's product manager and designer. The question is "What does a guest see and pay at each outcome of changing dates?" Afterwards they agree the three price outcomes and the other-rooms step before building.
Why: the Roamstay context file puts Trips and booking changes under the Booking squad, and a screens-and-choices board suits that conversation.

**Question 2: what must this board not do?**

Reading: you described the main path and the three price outcomes. You didn't describe a failed payment, a cancellation, a desktop and mobile split, or Pay at property versus Pay now.
Recommended: draw only what you described. The board shows none of those cases, and the reply lists them on its `Left out:` line.
Why: each one needs a source I don't have, and the flow already sits close to the 9-node limit for a user flow.

If you don't answer, I'll proceed on both recommendations and mark them assumed in the full playback before the gate.

**Still open for the next rounds**

* What the guest does after seeing other rooms. My reading is that they pick a room and rejoin at the price comparison
* Whether your description is current behavior, approved direction or a proposal. A proposal would carry that status in its label

After those, I'll show the outline and a sketch in chat. The write waits for your yes to a separate gate reply that names the file, the calls it will spend and the rollback.