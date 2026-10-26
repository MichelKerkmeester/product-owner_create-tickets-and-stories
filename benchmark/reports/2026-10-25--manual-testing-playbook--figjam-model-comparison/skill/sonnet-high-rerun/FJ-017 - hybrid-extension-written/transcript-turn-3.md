# FJ-017 turn 3 transcript

**User:** Use your recommended answers.

**Assistant:**

Gate for the write. A yes to this message creates the file, so nothing has been created yet.

Question: which statuses can a Roamstay booking have, what moves it between them, and who sets Cancelled and No-show?
Outcome: support can read the lifecycle and knows who to ask when a booking shows Cancelled or No-show.
First glance: Cancelled, in focus with the key reason "guest sets it". I picked it as the first of the two statuses you named, and I can switch it to No-show.
Second glance: the two notes on Cancelled and No-show, and the events that lead into them, guest cancels and missed check-in.
Last glance: Pending, where every booking starts, and the source line.
Plan: <figma-plan-1> (Pro, Full seat), taken as the Barter team plan. File: a new FigJam file named "Booking status", created in drafts with no project.
Writes: one composed board with 7 states and 12 transitions, a title, a key and a source line, at the laptop reading distance.
Extensions: two single stickies, `note:1` beside Cancelled reading "Set by the guest, from Pending or Confirmed" and `note:2` beside No-show reading "Set by the hotel, after a missed check-in".
Calls: `create_new_file`, `create_session`, two `use_figma` calls (the board, then the notes) and one `get_figjam` read-back.
Rollback: delete the new file. The notes can also be removed alone by deleting the two sticky ids the extension returns.

Write it?
