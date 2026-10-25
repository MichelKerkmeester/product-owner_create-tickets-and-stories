The model passes the pre-write check and composes, so nothing is left but your yes. I have not written to the file.

**Playback**
- Question: which statuses can a Roamstay booking have, and what moves it between them?
- Outcome: Guest Support can find the three end states at a glance.
- Type: state diagram, drawn at balanced detail for a mixed audience at laptop distance.
- 7 states: Pending, Confirmed (containing Upcoming and In stay), Completed, Cancelled and No-show.
- 12 transitions: card authorised, check in, check out, guest cancels (from Pending and from Confirmed) and hotel marks no-show.
- Assumed: Cancelled is my name for the state a guest cancel leads to, because your brief says "cancel" but names no state. Tell me if support uses a different word.
- Colour: the composer draws every state the booking ends in as light gray. That covers Completed, Cancelled and No-show, and the key calls them "Final state". The other states are white, except Pending, which is light blue as the first state.
- The three end states share one colour, so only their labels tell them apart. A separate colour for each, such as green for Completed and red for the other two, is a hand edit in FigJam after the write.
- Left out: the 30-minute expiry of a Pending booking, which is in `context/roamstay-context.md` but not in your brief. It would add an Expired state if you want it.
- Limit: Mermaid moves leave a composite as a whole, not from one state inside it. So "check out", "guest cancels" and "hotel marks no-show" all leave Confirmed and read as possible from either Upcoming or In stay. Your brief ties no-show to a missed check-in, which only an Upcoming booking can have, and the board cannot show that.

**Glances**
- First: the three gray end states.
- Second: the guest cancels and no-show moves that lead into them.
- Last: the source line and the left-out expiry.

**Gate**
- Plan: Roamstay Product, as you named it. I cannot check it, because `whoami` lists your plans but not which plan owns a file.
- File: the existing FigJam file `<test-file-key>`. No new file is created. The board goes in as a new section 400 pixels right of what is already there and touches nothing else.
- Writes: one board titled "Booking status", with a subtitle, a key and a source line. No extensions.
- Calls: `create_session`, Figma's `figma-use` and `figma-use-figjam` skill loads, one `use_figma` and one `get_figjam` read-back. If the plan is on Starter or a View or Collab seat, the six calls a month cap applies.
- Rollback: delete the one board section the write returns. I will only do that after a separate yes from you.

Write it?