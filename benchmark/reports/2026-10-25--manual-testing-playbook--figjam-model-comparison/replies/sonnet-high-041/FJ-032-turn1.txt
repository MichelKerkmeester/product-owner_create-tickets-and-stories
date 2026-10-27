I haven't drawn anything yet. I need three answers first, and each has a recommended answer, so replying "use your recommendations" is enough.

**Board read:** `<draft-file-key>` holds one section, "Sprint retro", with six stickies. Nothing on it is titled "Booking status". The new board would sit beside it as its own section, and nothing already there would change.

**How I read the request:** this is a state diagram, because you're asking which statuses a booking has and what moves it between them.

**Outline I'd draw (7 states, 12 transitions):**
* Start into Pending
* Pending to Confirmed on "card authorised"
* Confirmed groups Upcoming and In stay, and Upcoming to In stay is "check in"
* Confirmed to Completed on "check out [from In stay]"
* Pending to Cancelled and Confirmed to Cancelled, both "guest cancels"
* Confirmed to No-show on "missed check-in [from Upcoming]"
* Completed, Cancelled and No-show each end the booking

**Assumed so far:**
* Detail is balanced, the audience is mixed, and the board is read at laptop distance
* Cancelled is a status of its own, because your message names the move but not the state
* Cancelling from Confirmed also covers a guest who is already In stay, because you gave the rule at the Confirmed level

**Questions:**

1. **Reader and outcome.** Your message doesn't name them, and this is a retro board.
   * Reading: the team is looking at the lifecycle to agree it, and the board answers "which statuses exist and what moves a booking between them".
   * Recommended: the retro team, who should come away able to say what each status means and which ones end a booking. The board doesn't show how long each status lasts or who sees it in the app.
   * Why: that's all four rules in your message give us, and anything more would be invented.

2. **Source class.** Are these rules how Roamstay works today, or a proposal?
   * Reading: your message states them as fact, but names no doc.
   * Recommended: current behavior, with the source line reading "Source: the Roamstay booking status rules, as given in the request".
   * Why: a proposal would carry its status in the labels, so I'd rather know now.

3. **Moves your message leaves open.**
   * Reading: it gives "after a missed check-in" as the trigger for No-show, so a check-in event exists. It never says what moves Upcoming to In stay, and it says nothing about a Pending booking whose card is declined or never authorised.
   * Recommended: draw "check in" as the Upcoming to In stay move, marked assumed. Leave the declined-card path off, and name it under `Left out:` as a later addition.
   * Why: the first is the only reading your own wording supports, and the second has no source at all.

Once you've answered, I'll check the model and then ask for your yes before writing anything to the board.