Question: which screens does a customer pass through to start a return in the app, and where do they choose?
Outcome: a reader can follow a return from the order list to a confirmed return and see where the 30 day window ends it.
First glance: the confirmed return, the goal the flow reaches.
Second glance: the drop-off or pickup choice that leads to it.
Last glance: Contact support, the exit after 30 days.
Check: the model passed the pre-write check as a user flow, 7 nodes and 7 connectors, and it composes into one `use_figma` call.
Plan: Fernhouse Product, as you named it. File: the existing FigJam file `<test-file-key>`, with no new file created. I read "new board" as a new board section inside that file. The file keeps the plan it was made in, and I have not verified that this plan owns it.
Writes: one composed board in three zones, with a title, a key and a source line. It holds 7 nodes and 7 connectors, drawn at Laptop reading distance with balanced detail. It lands 400 pixels to the right of what the file already holds.
Extensions: none.
Calls: `create_session` on that file, one `use_figma` and one `get_figjam` read-back. That is 3 calls, and a Starter plan or a View or Collab seat has six a month.
Rollback: delete the one board section the write returns, only after you say yes to the deletion. The file stays.

Write it?