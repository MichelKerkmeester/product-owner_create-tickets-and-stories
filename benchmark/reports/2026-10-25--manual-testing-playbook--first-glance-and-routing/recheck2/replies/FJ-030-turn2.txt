The model passes the check and composes. This is the gate. It asks about the write only.

```text
Question: which screens does a Fernhouse customer pass through to start a return in the app, and where do they give up?
Outcome: a reader can follow a return from the order list to a confirmed return and see the three places support says customers give up.
First glance: Return confirmed, the goal the flow reaches.
Second glance: the three numbered pins on the give-up places.
Last glance: Contact support, the exit after 30 days.

Sketch, checked: 7 nodes and 7 connectors, 0 crossings
  Order list > Order detail > Within 30 days?
  Within 30 days? No > Contact support
  Within 30 days? Yes > Return reasons > Drop-off or pickup?
  Drop-off or pickup? Drop-off point > Return confirmed
  Drop-off or pickup? Courier pickup > Return confirmed

File: the existing FigJam file <test-file-key>, no new file. The board lands as a new section 400 pixels right of what is already there, and nothing existing is touched.
Plan: Fernhouse Product, as you named it. I cannot confirm it from here, because whoami lists the plans on your account and not which plan owns a file.
Writes: one composed board in three zones (Find the order, Request the return, Done), with a title, a subtitle, a key and a source line, at Laptop reading distance.
Extensions: 3 numbered pins with a 3-sticky legend, numbered in flow order so they read left to right.
  1. on Within 30 days?: "Support: customers give up at the 30 day cut-off, there is no warning before day 30"
  2. on Return reasons: "Support: customers give up at the reason list, there are too many reasons"
  3. on Drop-off or pickup?: "Support: customers give up at the drop-off or pickup choice, the pickup fee is unclear"
Calls: create_session, one use_figma to compose the board, one use_figma for the pins and legend, and one get_figjam read-back. No whoami and no create_new_file. If the file sits on a Starter plan or a View or Collab seat, those calls count against Figma's six per month.
Rollback: delete the one board section the write returns, which removes the pins and legend inside it. It happens only after you say yes to the deletion.

Write it?
```