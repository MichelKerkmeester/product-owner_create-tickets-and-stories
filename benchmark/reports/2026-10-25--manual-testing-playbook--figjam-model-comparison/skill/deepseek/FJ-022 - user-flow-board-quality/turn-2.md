Question: which screens does a Fernhouse customer pass through to start a return in the app, and where do they choose?

Outcome: a reader can follow a return from the order list to a confirmed return with a QR code, and see where the 30 day window ends it.

First glance: the confirmed return with its QR code, the goal the flow reaches.

Second glance: the drop-off or courier pickup choice that leads to it.

Last glance: Contact support, the exit after 30 days.

Plan: Fernhouse Product, as you named it. File: the existing FigJam file `<test-file-key>`, which I read before this gate.

Writes: one composed board section named Start a return, 9 nodes and 9 connectors in three zones, with a title, a subtitle, a key and a source line, at the Laptop reading distance. The composer places it 400 pixels right of the rightmost section already on the page, which puts it about 138,000 pixels from the left edge, so a reader scrolls right past every existing section to reach it.

Already there: 46 sections and 66 top level nodes, including a hand drawn Start a return flow and eight sections named Start a return. This write adds one board and moves, resizes or deletes none of them.

Plan check: `whoami` returned <figma-plan-3>, <figma-plan-1> and <figma-plan-2> and no plan named Fernhouse Product, so the file's own plan is unconfirmed. Writing into the existing file leaves that plan as it is.

Extensions: none.

Calls: one `use_figma` to compose the board and one `get_figjam` to read it back, after the three reads already spent on the session, `whoami` and the file.

Rollback: delete the one board section this write returns, which removes everything drawn inside it, and only on a separate yes.

Write it?