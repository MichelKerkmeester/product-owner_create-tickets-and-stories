The revised model passes the check (7 nodes, 6 connectors, 0 crossings) and composes into one `use_figma` call. Here is what the write would do.

**Question:** which screens does a Fernhouse customer pass through to start a return in the app, and where do they choose?
**Outcome:** a reader can follow a return from the order list to a confirmed return and see where the 30 day window sends the customer to Request an exception.
**First glance:** Return confirmed with QR code, the goal the flow reaches.
**Second glance:** Drop-off point or courier pickup, the choice that leads to it.
**Last glance:** Request an exception, the exit after 30 days.
**Plan:** Fernhouse Product, as you stated.
**File:** the existing FigJam file `<test-file-key>`.
**Writes:** one new composed board named "Start a return", added to the right of everything on the page. It has the same 7 nodes, 6 connectors and three zones as the board I wrote earlier. The one change is the No exit, which now reads "Request an exception". The source line also gains "The 30 day exit follows a later update". Board `96:3371` is not edited, because a composed board is never changed in place.
**Extensions:** none.
**Calls:** one `use_figma` to compose the board and one `get_figjam` to read it back. This reuses the open session.
**Rollback:** delete the one board section the write returns.

After the read-back I will ask separately whether to delete `96:3371`. Until you say yes to that, both boards stay, and the six older boards with the same title are never touched.

Write it?