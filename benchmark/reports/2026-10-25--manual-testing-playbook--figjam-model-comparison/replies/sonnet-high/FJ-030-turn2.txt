Check passed: 7 nodes, 7 connectors and 0 crossings. It composed locally and I deleted the scratch files. Nothing has gone to Figma yet.

- **Question:** Which screens does a Fernhouse customer pass through to start a return in the app, where do they choose, and where does support say they give up?
- **Outcome:** A reader can follow a return from the order list to the confirmation, see where the 30-day window ends it and find the three give-up steps with a note on each.
- **First glance:** Return confirmed, the goal the flow reaches.
- **Second glance:** The three numbered pins on the steps where customers leave.
- **Last glance:** Contact support, the exit after day 30.
- **Assumed, per your yes to my recommendations:** the flow is live and drawn as current behavior, the 30-day check sits on the order detail, and both exits reach one confirmation.
- **File:** The existing FigJam file `<draft-file-key>`, as a new section beside what it holds. Nothing already there changes.
- **Plans:** I'm creating no new file, so no plan applies. I haven't confirmed which plan the file belongs to. If the file can't be opened, I'll stop and ask rather than create one, because your two instructions name different plans (Fernhouse Product and Barter team).
- **Writes:** One composed board titled "Start a return", with 7 nodes and 4 labelled decision exits. It has three zones (Find the order, Request the return and Done), a key and a source line, at Laptop reading distance.
- **Extensions:** Three violet pins with a legend column of three stickies, numbered in flow order:
  1. On the 30-day decision: "Support says customers give up here: nothing warns them before day 30"
  2. On the reason list: "Support says customers give up here: too many reasons to choose from"
  3. On the drop-off or pickup choice: "Support says customers give up here: the pickup fee is unclear"
- **Calls:** `create_session`, one `get_figjam` read before the write, one `use_figma` for the board, one `use_figma` for the pins and stickies, and one `get_figjam` read-back. If the file's plan is Starter, that is most of the six tool calls Figma allows a month.
- **Rollback:** Delete the one board section the write returns, pins and stickies included. That happens only on your separate yes to a question that names the board.

Write it?