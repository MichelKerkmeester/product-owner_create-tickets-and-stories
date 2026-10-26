I read the board but wrote nothing. It's an existing file with 97 top-level sections, and I can't tell yet what the board is for or who will read it, so there are three questions before I model anything.

Several sections already cover this topic: 10 are titled "Booking status", 6 "Booking status lifecycle", and there is one "Roamstay booking status" and one "Roamstay booking lifecycle for support". None were written in this conversation, so I won't change or delete any of them. The new board goes in as one new section beside what's there, and I'll propose a title that no section uses at the write gate.

**What I've read so far**
* Type: state diagram, because you're asking which statuses exist and what moves a booking between them
* States: Pending, Confirmed (containing Upcoming and In stay), Completed, Cancelled and No-show
* Moves you gave:
  * Pending to Confirmed when the card is authorised
  * In stay to Completed on check-out
  * Pending to Cancelled and Confirmed to Cancelled when the guest cancels
  * Upcoming to No-show when the hotel marks a missed check-in
* Source: your message only, so I'm treating all of it as current behavior

**Round one**

1. Reader and outcome
   * Reading: the board is for a retro, but your message doesn't say who reads it
   * Recommended: the product and support team, who leave agreeing the statuses and the moves between them
   * Why: that matches a retro and keeps the board to the lifecycle only

2. What the board must not do
   * Reading: you gave five statements and nothing on refunds, payment steps or when No-show is marked
   * Recommended: draw only those five, and name refunds, payment steps and No-show timing under `Left out:`
   * Why: a state you didn't state would read as fact

3. The trigger for Upcoming to In stay
   * Reading: you said Confirmed covers both but not what moves a booking from one to the other
   * Recommended: "check in", marked assumed
   * Why: it's the only event that fits between a booking not yet started and a stay in progress

Can I go ahead on these three recommended answers, or do you want to correct any of them?