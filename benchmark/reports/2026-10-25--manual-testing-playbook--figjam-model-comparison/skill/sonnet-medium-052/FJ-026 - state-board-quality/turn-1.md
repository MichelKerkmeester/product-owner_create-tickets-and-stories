Before I draw anything, this is how I read the request so far.

- **Type:** a state diagram, since you're asking which statuses exist and what moves a booking between them.
- **Destination:** a new section in the existing FigJam file `<test-file-key>`, not a new file. I'll read the file once before the write gate so the board lands beside what's already there.
- **Source:** the booking doc as you relayed it, with each line treated as current behavior.
- **Colour:** the composer already draws every end state in light gray with the key entry "Final state", so I can't pick a custom colour. Completed, Cancelled and No-show get that gray automatically. One end state can also take a pink focus outline.

**1. Reader, question and outcome**
Reading: the reader is support, who need to spot the end states.
Question: what question should the board answer, and what should support be able to do after reading it?
Recommended: "Which statuses exist, what moves a booking between them, and which ones are final?" Support can then tell at a glance that a booking is over. Detail level Balanced, audience Mixed, reading distance Laptop. The pink focus outline goes on Cancelled.
Why: the end states are the only part you asked to stand out, and Cancelled is the one with a money rule attached.

**2. What the board must not do**
Reading: your doc lines mix statuses with rules. The 15-minute limit, the date changes, the room charges, the 48-hour rule and the 6-hour No-show window are rules, not statuses.
Question: what should the board refuse to become?
Recommended: not a cancellation or refund policy chart. The rules sit as short lines inside the state they belong to. Pending shows the 15-minute limit, Upcoming the date changes, In stay the room charges, Cancelled the 48-hour first-night rule and No-show the 6-hour window. None of them becomes an extra state or branch.
Why: that keeps it at 7 states and about 11 transitions, so it reads on one screen. The doc doesn't say what happens when Pending passes 15 minutes, so I'd list that under `Left out:` rather than invent an exit.

**3. Cancelling during the stay**
Reading: the doc says a guest can cancel while Pending or Confirmed, and Confirmed includes In stay. I also assume the cancelled status is called Cancelled, since the doc never names it.
Question: can a guest cancel while In stay, or only before check-in?
Recommended: draw it as the doc says, from Confirmed, and name this as an open point in the reply.
Why: limiting it to Upcoming would be my guess, not the doc's.

Take the recommended answers, or correct any of them?