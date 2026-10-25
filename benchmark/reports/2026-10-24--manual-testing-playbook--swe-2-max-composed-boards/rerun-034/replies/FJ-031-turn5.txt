The reading is settled. Here is the write gate again with the changed exit, and it asks only about the write.

```text
Question: which screens does a Fernhouse customer pass through to start a return in the app, and where do they choose?
Outcome: the Post-purchase team and design can agree the start path and the 30-day branch.
First glance: Confirmation with QR code, the goal the flow reaches.
Second glance: the Drop-off or courier pickup choice that leads to it.
Last glance: Request an exception, the option after 30 days.
Plan: Fernhouse Product, as you named it. I have not verified it, because the file already exists and keeps the plan it was made in.
File: the existing FigJam file <test-file-key>. No new file is created.
Writes: one framed board section named "Start a return". It holds 7 nodes and 7 connectors, with a title, a subtitle, a key and a source line, at Laptop reading distance. The check passed on this model.
Placement: 400 pixels to the right of everything already on the page, so no existing content is covered or touched.
Extensions: none.
Calls: create_session, one use_figma that composes the board, and one get_figjam read-back.
Rollback: delete the one board section the write returns. That runs through use_figma and only after you say yes to the deletion.
```

Figma limits a Starter plan and a View or Collab seat to six tool calls a month. If your seat falls under that limit, the read-back may be refused. I would then report `Read-back: not possible` and not call the board done.

Write it?