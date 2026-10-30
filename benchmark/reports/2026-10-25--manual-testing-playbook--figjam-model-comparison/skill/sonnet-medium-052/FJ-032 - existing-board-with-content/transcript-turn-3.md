# FJ-032 turn 3 transcript

**User:** Yes, that reading is right.

**Assistant:**

Playback, before any model is written:

**Question and outcome**
- **Question:** Which statuses can a Roamstay booking be in, and what moves it between them?
- **Outcome:** the retro team agrees what each status means and what moves a booking between them.
- **Dials:** Balanced detail, Mixed audience, Meeting screen distance (transition labels under 32 characters).

**What the sources settled (your message and the three quoted doc lines)**
- **States:** Pending, Confirmed (a section holding Upcoming and In stay), Completed, Cancelled and No-show.
- **Moves:** card authorised takes Pending to Confirmed, and check-out takes In stay to Completed. A guest cancel leaves Pending or Confirmed for Cancelled. A missed check-in lets the hotel mark No-show.
- **Notes:** Pending carries "15 minutes at most while the card is checked". No-show carries "from 6 hours after the check-in time".
- **Target:** a new section beside what `<test-file-key>` already holds, with nothing there changed.

**Assumed, with what would settle each**
- **Source class:** the doc lines are current behavior. The attached doc would settle it.
- **Check-in:** the Upcoming to In stay move is labelled "check-in". A source naming the trigger would settle it.
- **The 48 hour rule:** the first-night price sits on the cancel from Confirmed only. The doc's wording on a Pending cancel would settle it.
- **Reader and outcome:** these are the retro team and the agreement above. You confirmed them, and no source states them.

**Still open, so left out**
- The exit when the 15 minutes pass without an authorised card.
- Refund amounts, payment retries and the failed-card path.

**Outline**
1. The board answers the question above. Seven states are drawn, two of them inside Confirmed.
2. The start dot enters Pending. Moves run Pending to Confirmed, Pending to Cancelled, Confirmed to Cancelled, Upcoming to In stay, In stay to Completed and Upcoming to No-show.
3. Completed, Cancelled and No-show end the machine.
4. The No-show move names Upcoming as its guard, since only a booking that has not checked in can miss the check-in.

**Two framings**
- **Full lifecycle (recommended):** every exit is drawn, so the retro sees all three endings. It costs a few more connectors. It fits a status field that needs agreeing.
- **Happy path with exits beside it:** the board reads faster. It hides which statuses can still be cancelled.

**Look**
- **Zones:** Confirmed is the only section, because it is the one composite.
- **Title:** "Roamstay booking status lifecycle".
- **Subtitle:** "From Pending to Completed, Cancelled or No-show, for the retro team".
- **Source line:** names your message and the booking doc lines, with the left-out items.
- **Emphasis:** I recommend no state emphasis, since the request names none.

Is this reading right, or should any row change?
