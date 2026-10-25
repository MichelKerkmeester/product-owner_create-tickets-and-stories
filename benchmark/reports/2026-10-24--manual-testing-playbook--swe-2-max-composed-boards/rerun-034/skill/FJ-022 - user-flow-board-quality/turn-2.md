The reading is settled, and the model passed the pre-write check and composed cleanly. This is the write gate, a separate question from the reading.

```text
Question: which screens does a Fernhouse customer pass through to start a return in the app, and where do they choose?
Outcome: a reader can follow a return from the order list to a confirmed return and see where the 30 day window ends it.
First glance: the confirmed return, the goal the flow reaches.
Second glance: the drop-off or pickup choice that leads to it.
Last glance: Contact support, the exit after 30 days.
Plan: Fernhouse Product, as you gave it. I haven't verified it against the file.
File: the existing FigJam file <test-file-key>. No new file is created, and the board is added as a new section.
Writes: one composed board, 9 nodes and 9 connectors in three zones (Find the order, Request the return, Done), with a title, a key and a source line, at the Laptop reading distance. It lands to the right of whatever is already on the page, and nothing existing is moved or edited.
Extensions: none.
Calls: two Figma skill reads that the server requires, create_session, one use_figma and one get_figjam read-back.
Rollback: delete the one board section the write returns, only after you say yes to that deletion. The rest of the file stays as it is.
Write it?
```

Left out: the free pickup for orders over €100, a proposal under review. It goes on the board's source line, not as a step.

If this file's plan is on a Starter plan or you have a View or Collab seat, Figma allows six tool calls a month. This write uses most of them.