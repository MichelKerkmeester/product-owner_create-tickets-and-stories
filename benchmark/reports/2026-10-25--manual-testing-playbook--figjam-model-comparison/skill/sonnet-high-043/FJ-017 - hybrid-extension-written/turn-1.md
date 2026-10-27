Before I draw anything, this is how I read the request.

**Question:** which statuses does a Roamstay booking pass through, what moves it between them, and who sets Cancelled and No-show?
**Reader and outcome:** support can read every booking status and knows who to ask when a booking is Cancelled or No-show.
**Type:** a state diagram. Seven states with branching exits is more than a list shows.

Outline, in drawing order:

```text
Start to Pending
Pending to Confirmed: card authorised
Confirmed is one section holding Upcoming and In stay
  inside it: start to Upcoming, Upcoming to In stay: check in
Confirmed to Completed: check out [from In stay]
Pending to Cancelled: guest cancels
Confirmed to Cancelled: guest cancels
Confirmed to No-show: missed check-in [from Upcoming]
Completed, Cancelled and No-show each end the booking
```

That is 7 states and 12 transitions.

**Settled by your request:** every status, the Confirmed section, and who can cancel and when. Each is current behavior as you state it.

**Notes:** two single stickies beside their states, no pins. They are added after the board lands.
* Cancelled: "Set by the guest, while the booking is Pending or Confirmed"
* No-show: "Set by the hotel, after a missed check-in"

**Assumed, two rows:**
1. Cancelled and No-show end the booking, like Completed. You said only that check-out ends it as Completed, and nothing in your lines moves a booking out of the other two. This is settled by you telling me if either can reopen.
2. The move from Upcoming to In stay is "check in". You named the missed check-in but not the move that follows it. This is settled by your own word for it.

**Left out:** card authorisation failing or expiring, and cancellation by anyone but the guest. Neither is in your lines, so the board shows neither and the Cancelled note says the guest sets it. If the hotel can cancel too, tell me and I'll change the move and the note.

**One reading to check:** "guest cancels" leaves the whole Confirmed section, so the board shows it as open during In stay as well as Upcoming. That follows your words. If a guest cannot cancel mid-stay, I'll label it [from Upcoming].

**What the board must not do:** I recommend nothing beyond the statuses you named, so no payment-failure or refund states, because none of them is in your lines.

**Look, all recommended:**
* Framing: the full state map with Confirmed as a section, so every exit is visible. The alternative is seven flat states, which drops "Confirmed covers Upcoming and In stay" and splits cancel and no-show into separate arrows per state.
* Marked node: Cancelled, the state with two moves arriving.
* Title: "Booking status". Subtitle: "Every status a Roamstay booking passes through and what moves it on, for support".
* Detail is balanced, the audience is mixed and the board is read on a laptop.

The file's location comes at the next step, with the write gate.

Is this the right reading of the board?