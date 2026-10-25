The model passed the pre-write check and composed cleanly. This is the write gate, and it covers the write only.

**Question:** which screens does a customer pass through to start a return in the app, and where do they give up?
**Outcome:** a reader can follow a return from the order list to a confirmed return and see the three places support says customers drop out.
**First glance:** the confirmation with the QR code, the goal the flow reaches.
**Second glance:** the three numbered pins on the places customers give up.
**Last glance:** Contact support after day 30, and the source line.

**Plan:** Fernhouse Product, as you named it. I can't confirm which plan owns the file from here.
**File:** the existing FigJam file `<test-file-key>`. No new file is created.

**Writes:** one new composed board section beside any existing content. It has 7 nodes and 7 connectors in three zones, with a title, a subtitle, a key and a source line, at Laptop reading distance. The 4 decision exits are labelled.
* Screens: Order list, Order detail, Within 30 days?, Return reasons, Drop-off or pickup?, Confirmation with QR code and the Contact support exit
* The free pickup over €100 appears only in the source line

**Extensions:** three numbered pins with a legend column inside the board, each note naming support as its source and giving no figures:
1. On Within 30 days?: "Support says customers give up here because the app shows no warning before day 30."
2. On Return reasons: "Support says customers give up here because the list has too many reasons."
3. On Drop-off or pickup?: "Support says customers give up here because the pickup fee is unclear."

**Calls:** `create_session`, one `use_figma` to compose the board, one `use_figma` for the pins and `get_figjam` for the read-back. I'll load Figma's `figma-use` and `figma-use-figjam` skills first. If the plan is Starter or the seat is View or Collab, Figma allows six tool calls a month and reads count against that. This write uses about five.

**Rollback:** delete the one board section the write returns. The pins and notes sit inside it, so they go with it, and nothing already in the file is touched. I delete only after a separate yes from you.

Write it?