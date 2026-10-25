Nothing has been written to the board. This is round one of the intake, and the model and the write gate come after it.

**Settled so far, from your request**
* Entry: the booking page, where the guest taps Change dates (captured)
* Exit: the guest sees the updated booking (captured)
* Actors: the guest picks dates, and the system checks the room and compares prices (captured)
* Decisions: whether the room is free on the new dates, and whether the new price is higher, lower or the same (captured)
* Target: a new framed board section in the existing file `<test-file-key>`, in the Roamstay Product plan. No new file is created (captured)
* Still open: the reader, the question, the outcome, scope, and the class of your source (unasked)
* Also open: your request does not say what the guest does after seeing other rooms. I'll ask that in round two

**1. Reader, question and outcome**
* Reading: the request names no reader. It walks one guest through the steps
* Recommended: the reader is the Booking squad (product manager, designer and engineers). The question is "Which screens does a guest pass through to change dates, and where does the price decide what they pay?" The outcome is that the reader can see the no-room path and all three price outcomes and agree on them
* Why: that is the shape of the steps you gave, and a user flow answers it

**2. What the board must not do**
* Reading: the request covers one main path with two branch points
* Recommended: leave out failed payments, cancellation, the 30-night and 365-day stay limits, and any Guest Support handoff
* Why: none of them appear in your request, and each would add branches the question does not need

**3. Type and look**
* Reading: the request is a person's path through screens with choices, so a user flow fits. By my count it needs 9 nodes, which is the user-flow budget. The Pay, Credit and No charge outcomes would each go straight to the updated booking
* Recommended: a user flow, left to right, balanced detail, mixed audience, read on a laptop, with no zones
* Why: it keeps the main path on one line and puts the price decision in view

If you skip any of these, the recommended answer stands and I mark it assumed in the playback before the gate. The write calls happen only after the gate reply, and I won't read the existing board before then.