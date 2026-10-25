The model passed the pre-write check (7 nodes, 7 connectors, 0 crossings) and composed cleanly, so this is the write gate. The check ran on a temp file outside the repository.

```text
Question: which screens does a customer pass through to start a return, and where do they give up?
Outcome: a reader can follow a return from the order list to a confirmed return, see where the 30 day window ends it and see the three places support says customers drop out.
First glance: the confirmed return with its QR code, the goal the flow reaches.
Second glance: the three numbered pins on the 30 day check, the reason list and the drop-off or pickup choice.
Last glance: Contact support, the exit after 30 days.
Plan: Fernhouse Product, as you named it. The tools cannot confirm which plan owns an existing file, so I rely on your word.
File: the existing FigJam file <test-file-key>. No new file is created.
Writes: one composed board titled "Start a return", 7 nodes and 7 connectors in three zones (Find the order, Request the return, Done), with a subtitle, a key and a source line, at the Laptop reading distance. The board lands 400 pixels right of whatever the file already holds.
Extensions: three numbered pins with a legend column of three stickies, all worded "Support reports ...":
  1. On "Within 30 days?": no warning before day 30
  2. On "Pick a reason": too many reasons
  3. On "Drop-off or pickup?": the pickup fee is unclear
Left out: the free pickup for orders over 100 euros, a proposal under review.
Assumed, as you confirmed: Contact support follows the order detail, the drop-off or pickup choice has two exits straight to the confirmation, and labels come from your wording.
Calls: create_session, one use_figma for the board, one use_figma for the pins and one get_figjam read-back. If the plan is on Starter, that is four of the six monthly tool calls.
Rollback: delete the one board section the write returns and the three pins and three stickies, through use_figma and only after your yes to the deletion. Nothing else in the file is touched.
Write it?
```