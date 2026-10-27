I've read the board and haven't written anything to it. The read showed one section, "Sprint retro", with six stickies. Nothing on it shares the title I'd use, "Booking status". The new board will go in as its own section beside Sprint retro, and nothing already there changes.

**Replay of what's settled**
* Type: state diagram, because your question is which statuses exist and what moves a booking between them.
* States (captured): Pending, Confirmed containing Upcoming and In stay, Completed, Cancelled and No-show. That is 7 states, inside the budget of 9.
* Entry (captured): Pending.
* Moves (captured): card authorised takes Pending to Confirmed, check-out takes the booking to Completed, a guest can cancel from Pending or Confirmed, and the hotel marks No-show after a missed check-in.
* Actors (captured): the guest cancels, the hotel marks No-show, and the card authorisation moves Pending on.
* Assumed: Cancelled and No-show are end states, because your lines don't say so. No-show is reached from Upcoming, because a check-in can only be missed before it happens. I've treated your lines as current behavior, since you gave no source document.
* Still open, for the next round: what moves Upcoming to In stay, whether a guest can cancel during the stay, and what happens to a Pending booking whose card is declined.

**Round 1 of 3**

1. **Reader, question and outcome**
   * Reading: the board is a sprint retro, and your request names no reader.
   * Question: who reads this, and what should they be able to decide afterwards?
   * Recommended: the product, engineering and support team, asking "which statuses exist and what moves a booking between them?", so they can agree every status and its exits before the next story is written.
   * Why: it is the standard question a state diagram answers, and it fits a retro audience.

2. **What the board must not do**
   * Reading: your five statements cover the happy path, cancellation and No-show, and nothing about payment failure, expiry or refunds.
   * Question: what should this board refuse to show?
   * Recommended: no status or move beyond the seven states and the moves you stated, so no declined-card, expiry or refund paths, and no edits to the Sprint retro section.
   * Why: a diagram of the partial system you described beats a polished one with guessed paths.

Reply "use the recommended answers" to accept both. After that I'll ask round 2, which covers the open items above. Then I'll send the full playback, and the write gate comes last.