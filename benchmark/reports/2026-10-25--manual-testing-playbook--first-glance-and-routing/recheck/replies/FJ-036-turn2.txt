Round 2 of 3. Your acceptance settles round 1, so those rows stand as recommended.

**Settled so far**
* Reader: the Roamstay product team, walking the flow together
* Question: what does a guest see and pay when they change their dates?
* Outcome: the reader can check that every price outcome has a screen and spot any case the app doesn't cover
* Stays out: payment failures, cancellations, host approval, and rules such as change fees or deadlines. These go under `Left out:`.
* Entry: the booking page, through Change dates
* Exit: the updated booking
* Actors: the guest picks dates (and pays when the price is higher), and the system checks the room and the price

Your request already answers entry, exit and actors, so round 2 asks only about the two gaps in the middle.

1. What happens after the guest sees other rooms?
   * Reading: your request stops at "they see other rooms". The price outcomes follow, but nothing says how the guest gets from the room list to a price.
   * Recommended: the guest picks one of the other rooms, and the price comparison runs on that room and those dates
   * Why: a different room usually has a different price, so the price outcomes still apply. The other option is a loop back to the date picker, which would add an edge your request doesn't state.

2. Is there a confirmation screen between picking dates and the price outcome?
   * Reading: your request goes straight from picking dates to the room and price checks, and names no confirm step
   * Recommended: draw none. Paying the difference is the guest's only action after the price check, and the credit and no-charge outcomes are automatic.
   * Why: a confirm screen would be invented. I'd mark the two automatic outcomes as system steps in their labels.

Reply "accept" or correct either line. Round 3 will ask whether this behaviour is live, approved or proposed, and I'll check the node count against the board's budget of nine.