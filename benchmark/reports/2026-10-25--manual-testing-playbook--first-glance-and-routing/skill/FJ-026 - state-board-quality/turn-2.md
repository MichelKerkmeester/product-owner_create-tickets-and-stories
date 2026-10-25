The model passes the pre-write check, and the board code is composed locally. Nothing has been written to Figma.

```text
Question: which statuses can a Roamstay booking have, and what moves it between them?
Outcome: support can read every booking status and spot the three statuses a booking ends in.
First glance: the end states, Completed, Cancelled and No-show, drawn in light gray.
Second glance: the events that lead into them, check out, guest cancels and missed check-in.
Last glance: Pending, where every booking starts.
Plan: Roamstay Product, as you named it. I haven't checked it against the file.
File: the existing FigJam file <test-file-key>, with no new file created.
Writes: one composed board, 7 states and 12 transitions, with a title, a key and a source line, at the Laptop reading distance. It lands 400 pixels to the right of the existing content, and nothing already there is changed. Check-out, No-show and cancel leave from Confirmed as a whole, as agreed.
Extensions: none.
Calls: create_session, one use_figma and one get_figjam read-back. On a Starter plan or a View or Collab seat, Figma caps tool calls at six a month, so these three count against that.
Rollback: delete the one board section the write returns. I'd do that only after a separate yes from you.
Write it?
```