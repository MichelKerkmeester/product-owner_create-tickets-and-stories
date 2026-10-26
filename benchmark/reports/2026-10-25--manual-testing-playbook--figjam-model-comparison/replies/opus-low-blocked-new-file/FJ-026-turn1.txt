**Intake round 1 of 3: Roamstay booking status lifecycle (state diagram).** Nothing has been written to Figma yet.

**What you've told me so far**
- **Type:** a state diagram. The question is "what status can a booking be in, and what moves it on?"
- **Reader:** support. They need to spot the end states at a glance.
- **States:** Pending; Confirmed, which contains Upcoming (where it starts) and In stay; then Completed, Cancelled and No-show.
- **Moves:**
  - Pending to Confirmed when the card is authorised.
  - Upcoming to In stay at check-in.
  - In stay to Completed at check-out.
  - Pending or Confirmed to Cancelled when the guest cancels.
  - Upcoming to No-show when the hotel marks a missed check-in.
- **End states, coloured:** Completed, Cancelled and No-show.

**Questions (each has my recommendation, so you can just say "use your recommendations")**

1. **Where the board goes.** You asked for a new board in the Roamstay Product plan, and also asked me to write into the existing file `<test-file-key>`. Flow Mode only writes to a file it creates itself or a board this work has already written. It won't add to an existing file it didn't make, because it can't check what's already on that board or who can see it.
   - **Recommended:** create a new FigJam file in the Roamstay Product plan.
   - If it must go in `<test-file-key>`, I can draw it in a new file and you can copy the section across. You could also tell me why that file is safe to write to, and I'll flag it at the write step.
2. **Cancelling during In stay.** "Confirmed" includes In stay. Can a guest cancel once checked in?
   - **Recommended:** no. Cancel only from Pending and Upcoming, since after check-in the stay ends at check-out.
3. **Card authorisation fails.** Does a declined card leave the booking in Pending, or move it to Cancelled or Failed?
   - **Recommended:** leave it out and list it as a gap, because none of what you've told me covers it.
4. **What the board shouldn't show.** **Recommended:** statuses only, with no refunds, fees or notifications.

Once you've answered, I'll replay the full reading for your sign-off. The write step comes after that and needs its own yes.