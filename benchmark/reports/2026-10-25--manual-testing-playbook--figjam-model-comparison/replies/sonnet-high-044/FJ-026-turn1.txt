Before I draw anything, this is how I read the request. Nothing is written yet.

**Question:** which statuses can a Roamstay booking be in, and what moves it between them?
**Outcome:** support can read every status and spot the three a booking ends in.
**Type:** state diagram, because the question is about statuses and what moves a booking between them.
**Settled by your request:** Pending is the entry, Confirmed covers Upcoming and In stay, and Completed, Cancelled and No-show are the ends. Every move has a trigger.
**Assumed:**
- The lifecycle is current behavior. A bookings doc or the status field in code would settle it
- Check-out leaves from In stay only and a missed check-in leaves from Upcoming only, because neither can happen from the other state. The board would show these as guards
- Balanced detail, a mixed audience and a laptop reading distance
**Left out:** nothing so far

**Outline** (7 states, 12 transitions, all from the "Decisions and states" row)
- Start to Pending
- Pending to Confirmed: card authorised
- Inside Confirmed: start to Upcoming, Upcoming to In stay on check-in, In stay to end
- Confirmed to Completed: check-out, from In stay
- Pending to Cancelled: guest cancels
- Confirmed to Cancelled: guest cancels
- Confirmed to No-show: missed check-in, marked by the hotel, from Upcoming
- Completed, Cancelled and No-show each to end

**Two framings**
- A status map with Confirmed as a section around Upcoming and In stay, and all three ends on the right. It keeps "Confirmed covers Upcoming and In stay" visible and shows every exit. I recommend this one
- A flat happy path with Confirmed dropped. It reads faster, but it loses that grouping and draws cancel from two states instead of one

**Look**
- Colour: the composer draws every end state light gray with a heavy outline and names it "Final state" in the key. In-stay and Upcoming stay white
- First glance: a pink accent on Cancelled, the end reached from two states
- Title "Booking status", with the subtitle "Every status a Roamstay booking passes through, and what moves it on"
- Source line: "Source: the booking status lifecycle described in the request"
- The four critique questions come with the sketch at the gate

**Three questions**

1. What must this board not do?
   Reading: the request covers statuses only.
   Recommended: leave out payment retries, refunds, booking changes and any hotel action other than marking no-show.
   Why: none of them is in your description.
2. Can a guest cancel during In stay?
   Reading: Confirmed covers In stay, so cancel from Confirmed applies to both Upcoming and In stay.
   Recommended: draw it as you stated it, with no guard.
   Why: a guard would be a rule you did not give. If cancel is pre-check-in only, say so and I add `[from Upcoming]`.
3. Is light gray enough "colour" for the end states?
   Reading: all three ends share that one colour. A separate hue per end, such as red for Cancelled, is not something the composer can set on a state diagram. It would be a hand edit in FigJam after the write, or a change to the shared board design.
   Recommended: take the light gray, with the pink accent on Cancelled to pick one out.
   Why: gray plus a heavy outline and a "Final state" key entry marks the ends without touching the design every board shares.

Is this the right reading of the board, taking the recommended answers unless you change them?