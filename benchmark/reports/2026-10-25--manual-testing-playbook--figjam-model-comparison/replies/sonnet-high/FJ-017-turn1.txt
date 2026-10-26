Before I draw anything, this is how I read the request.

**Type:** a state diagram, because the question is which statuses a booking has and what moves it between them.
**Question:** which statuses does a Roamstay booking pass through, and who sets Cancelled and No-show?
**Outcome:** support can follow a booking's status and knows who to ask about a Cancelled or a No-show.
**Target:** the existing file <draft-file-key>, as a new section beside what it holds. No new file is created, so the Barter drafts fallback does not apply.

**Outline, in drawing order**
- Start into Pending
- Pending to Confirmed on "card authorised"
- Confirmed holds Upcoming and In stay, and Upcoming moves to In stay on "check in"
- Confirmed to Completed on "check out", from In stay
- Pending to Cancelled and Confirmed to Cancelled, each on "guest cancels"
- Confirmed to No-show on "missed check-in", from Upcoming
- Completed, Cancelled and No-show end the booking
- Two notes: "Set by the guest" beside Cancelled and "Set by the hotel" beside No-show

**Settled by your request:** every state and move above except the two assumed ones. The two notes come from "a guest can cancel" and "the hotel marks No-show".

**Assumed**
- Check in moves Upcoming to In stay. You name check-in only through the missed one, so the trigger is my reading
- Check out leaves from In stay and missed check-in leaves from Upcoming, because those are the only inner states where each can happen

**Defaults:** balanced detail, a mixed audience and a laptop reading distance.

**Must not do:** invent a state or a move nobody stated, such as a refund or a hotel-side cancel. I recommend this because support will read the board as fact.

**Left out:** a failed card authorisation, because nothing you wrote says where Pending goes then.

**Still open**
- Cancel leaves from Confirmed, so the board reads as allowing it during In stay too. Recommended: draw it as you stated it. Tell me if cancel should stop at check-in
- Nothing says whether the hotel or the system can also cancel. Recommended: keep "Set by the guest" as stated and report the gap as a finding

**Framing:** one full machine with every exit and both notes, or the happy path only with the exits as notes. I recommend the full machine, because support's question is about the two exits.

Is this the right reading of the board?