# FJ-026 turn 2 transcript

**User:** Use your recommended answers.

**Assistant:**

**Here's the full reading for your sign-off.** Nothing has been written to Figma yet.

**What the board answers:** what status a Roamstay booking can be in and what moves it on. Support should be able to spot the end states at a glance.

**Settled from your request**
- **Type:** a state diagram.
- **States:** Pending; Confirmed, which contains Upcoming (where it starts) and In stay; then Completed, Cancelled and No-show.
- **Moves:**
  - Pending to Confirmed when the card is authorised.
  - Upcoming to In stay at check-in.
  - In stay to Completed at check-out.
  - Upcoming to No-show when the hotel marks a missed check-in.
- **End states:** Completed, Cancelled and No-show, each in its own end-state colour, with a small key that names them.

**Taken from my recommendations (treated as assumptions)**
- **Board location:** a new FigJam file in the Roamstay Product plan. It will not go into `<test-file-key>`, though you can copy the section across afterwards.
- **Cancelling:** a guest can cancel from Pending and from Upcoming, but not once In stay.
- **Declined card:** not drawn. It will be listed under "Left out" as a gap your request didn't cover.
- **Scope:** statuses only, with no refunds, fees or notifications.

**Still open:** nothing.

**First thing a reader should see:** the three end states.

Is this reading right? If you confirm it, I'll build and check the model. Then I'll come back with the exact write (plan, file, calls and how to undo it) for a separate yes.
