Before I draw anything, this is how I read the request.

**Type:** a state diagram. Your question is which statuses a booking has and what moves it between them.

**Question:** which statuses does a Roamstay booking pass through, and who sets Cancelled and No-show?
**Outcome:** support can read every status, see which ones end a booking and know who to ask about Cancelled and No-show.
**Reader and dials:** support, balanced detail, a mixed audience and laptop distance. You named none of the dials, so all three are assumed.

**Outline, from your message:**
- Pending is where every booking starts, until the card is authorised
- Confirmed is a section around Upcoming and In stay, entered on "card authorised"
- Upcoming moves to In stay on "check in" (assumed, see below)
- Completed follows In stay on "check out"
- Cancelled follows Pending or Confirmed on "guest cancels"
- No-show follows a "missed check-in" from Upcoming, set by the hotel
- Completed, Cancelled and No-show each end the booking

That is 7 states and 12 transitions, inside the budget of 9 and 12.

**Notes:** two single stickies, one beside Cancelled reading "Set by the guest, while the booking is Pending or Confirmed" and one beside No-show reading "Set by the hotel after a missed check-in". They are an extension, so the gate will name them.

**Look:** the title is "Booking status", the subtitle "Every status a Roamstay booking passes through, and what moves it on", and the source line names your description. Pending reads first and the end states last. I set no accent, because both noted states matter equally.

**Framing:** I recommend Confirmed as a section around Upcoming and In stay, because it uses your word and support already says "Confirmed". The alternative is flat states with no Confirmed section. Each arrow would then name one state, but the board would lose that word.

**Destination:** a new file in your drafts with no project, as you set it. The gate confirms it.

**Assumed:**
- The source class is current behavior, because your message doesn't say whether this is live or planned.
- The triggers "check in" and "check out" are inferred from "missed check-in" and from Confirmed covering Upcoming and In stay. The "[from Upcoming]" and "[from In stay]" guards are inferred the same way.

**Not drawn:** a declined card, a hotel-side cancellation and a refund. Your message states none of them, so any arrow for them would be invented.

**Still open:** you wrote that a guest can cancel while Confirmed, and Confirmed covers In stay, so as written a guest can cancel mid-stay.
Recommended: draw it as you wrote it, with one Cancelled arrow from Confirmed. A guard I added would invent a rule. If cancelling only works before check-in, tell me and I'll guard it with "from Upcoming".

Is this the right reading of the board, taking the recommended answers?