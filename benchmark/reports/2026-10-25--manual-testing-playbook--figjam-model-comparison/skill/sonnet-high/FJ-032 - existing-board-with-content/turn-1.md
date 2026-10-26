I've read the Flow Mode rules and the matching Roamstay state example. Nothing has been read from or written to the board yet, because Flow Mode needs your answer to this reading before it drafts anything.

**Type:** a state diagram. Your question is which statuses a booking can be in and what moves it between them. A list would lose the two exits Confirmed has, so a diagram is worth drawing.

**Board lines I'll use:**

*   `userIntent`: the retro board's readers can see every booking status and what moves a booking between them
*   Reader (assumed): the team on the retro board
*   Entry: a booking starts as Pending
*   Exit: Completed, Cancelled and No-show end the booking
*   Actors: the guest cancels, the hotel marks No-show
*   Source: your message, taken as current behavior. No other doc was supplied

**Outline, in drawing order:**

1.  Start → Pending
2.  Pending → Confirmed, on card authorised
3.  Confirmed is one section holding Upcoming and In stay, entered at Upcoming
4.  Upcoming → In stay, on check-in
5.  Confirmed → Completed, on check-out [from In stay]
6.  Pending → Cancelled and Confirmed → Cancelled, both on guest cancels
7.  Confirmed → No-show, on missed check-in [from Upcoming]
8.  Completed, Cancelled and No-show → End

That is 7 states and 6 labelled moves, inside the 9-state budget.

**Two framings:**

*   **Recommended: Confirmed as one section.** It matches "Confirmed covers Upcoming and In stay", and the two cancel arrows stay as one each. The cost is that the exits from the section carry a guard, such as `[from In stay]`.
*   **Flat, with Upcoming and In stay as peers.** Each state gets its own exits and no guards are needed. The cost is that Confirmed stops reading as one status, and "cancel while Confirmed" needs two arrows.

**Look (all assumed):**

*   First glance: Confirmed, the one status that holds two
*   Second glance: the exits out of it
*   Last glance: Pending, where every booking starts
*   Detail and audience: balanced and mixed
*   Reading distance: laptop
*   The board is titled "Booking status"
*   The composer draws the end states in light gray

**What the board will not do:** draw payment failure, an expiry on Pending, refunds or any move your message doesn't state. It also won't touch anything already on the retro board.

**Gaps I'd close with my recommended answer, unless you correct them:**

1.  **Cancel target.** Your message says "cancel" but not where it lands.
    *   Recommended: a state named Cancelled.
2.  **End states.** Your message doesn't say whether Cancelled and No-show end the booking.
    *   Recommended: both end it, like Completed.
3.  **Upcoming → In stay trigger.** You name "check-in" only as the one that can be missed, and you name no event for the move itself.
    *   Recommended: label it `check-in`.
4.  **Cancelling during a stay.** Cancel is drawn from the whole Confirmed section, and Confirmed includes In stay, so the board will show a guest cancelling mid-stay.
    *   Recommended: draw it as you wrote it and report it back as a finding.

The file is `<test-file-key>`, an existing FigJam file, so I won't create a new one. The `<fileKey of the prepared board>` placeholder in your first line is ignored. The board would go in as a new section beside what's there, with nothing existing changed. The Barter team plan, drafts and no project apply only if that file turns out to be unwritable, and I'd stop and ask before creating one.

Is this the right reading of the board, including the four recommended answers above?