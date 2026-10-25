Nothing is on a board yet. This is the reading playback, before I build the model or ask to write.

```text
Question: which statuses can a Roamstay booking have, and what moves it between them?
Outcome: support can read every booking status and spot the three statuses a booking ends in.
Type: a state diagram, because the question is about statuses and the events between them.
Settled by your request: Pending until the card is authorised. Confirmed holds Upcoming and In stay, and check-in moves Upcoming to In stay. Check-out ends the booking as Completed. A guest can cancel from Pending or Confirmed. The hotel marks No-show after a missed check-in.
Where it lands: a new board in the existing file you named, with nothing already there touched.
Left out: nothing your request states. The board has no refunds, cancellation deadlines or the number of days before No-show, because you gave none.
Assumed: balanced detail, a support audience and a laptop reading distance.
```

Three points need your call. Each has a recommendation, and I'll proceed on it if you don't answer.

1. **End-state colour.** The composer draws every final state in the same light gray and labels it "Final state" in the key. Completed, Cancelled and No-show will therefore look alike, and I can't make Cancelled or No-show red or Completed green in the model. You can recolour them by hand in FigJam afterwards. Recommended: accept the gray, which still sets the three end states apart from the white states.
2. **Where check-out, No-show and cancel leave from.** The pre-write check refuses a move from inside Confirmed to outside it. Those three moves leave from Confirmed as a whole, not from Upcoming or In stay. The board will then read as if check-out and No-show could also happen from the other half of Confirmed, and as if a guest can cancel during In stay. Cancel from Confirmed is what you wrote. Recommended: draw it as written and report the check-out and No-show reading as a `Finding:` line in the final reply.
3. **State and trigger wording.** The board shows the ids `InStay` and `NoShow` unless I add a description. Recommended: use descriptions so the board reads "In stay" and "No-show". The No-show trigger will read "missed check-in".

Is this the right reading of the board?