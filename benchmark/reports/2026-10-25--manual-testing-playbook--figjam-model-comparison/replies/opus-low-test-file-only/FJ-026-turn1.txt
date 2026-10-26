The diagram type is a state diagram, since you're asking which states a booking can be in and what moves it between them. Nothing has been written yet. Here's how I read your notes, and I need you to confirm it before I build the model.

**The diagram's question:** what states can a Roamstay booking be in, and which of them are final?
**What it's for:** support can find the three end states at a glance by their colour.

**What your message settled**
- A booking starts as **Pending** and becomes **Confirmed** once the card is authorised.
- **Confirmed** contains two states: **Upcoming** and **In stay**.
- **Check-in** moves Upcoming to In stay.
- **Check-out** moves In stay to **Completed**, which is an end state.
- **Guest cancels** moves Pending or Confirmed to **Cancelled**, which is an end state.
- **Hotel marks No-show** after a missed check-in, which ends the booking as **No-show**.
- Completed, Cancelled and No-show get an end-state colour and a key that explains it.

**What I assumed (correct anything that's wrong)**
- **Cancel during a stay:** "Confirmed" includes In stay, so taken literally a guest could cancel mid-stay. I'll draw the cancel line from Pending and Upcoming only.
- **No-show** can only come from Upcoming, because that's the only state with a check-in still to miss.
- **Card not authorised:** your notes don't say what happens, so the board leaves it out and I'll list it as left out.

**Where the board goes (to settle at the write step)**
You asked for a new board in the Roamstay Product plan, and also asked me to write it into file `<test-file-key>`. My rules only let me write to a new file I create, or to a board I've already written in this piece of work. That key is neither. When I ask for your go-ahead to write, I'll suggest a new file in the Roamstay Product plan. If it has to go into that existing file, tell me then and we'll sort it out before anything is written.

Is this reading right, in particular cancelling only from Pending and Upcoming, not mid-stay?

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.