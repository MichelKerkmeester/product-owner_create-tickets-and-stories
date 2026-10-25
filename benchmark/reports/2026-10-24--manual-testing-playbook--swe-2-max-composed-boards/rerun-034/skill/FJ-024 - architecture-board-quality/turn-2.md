The model passes the check and composes at 9 nodes and 8 connectors, in 47,794 of the 50,000 characters one `use_figma` call takes. The glance lines below set what the board must win.

**Question:** which parts carry a block change from one client to the others, and how does a sleeping iOS device get woken?
**Outcome:** an engineer can see every part a block change passes through and where the iOS wake-up branches off.
**First glance:** sync-service, where every block change is written and published.
**Second glance:** the change stream that carries each change on to the push worker.
**Last glance:** Apple push service, the outside hop that wakes sleeping iOS devices.
**Plan:** Loomlist Engineering, as you named it. I can't confirm from here which plan owns the file, because `whoami` lists the plans an account holds and not who owns a board.
**File:** the existing FigJam file `<test-file-key>`. No new file is created.
**Writes:** one composed board named "Block sync" with 9 nodes and 8 connectors in 6 lanes, plus a title, a subtitle, a key and a source line, at the laptop reading distance. It lands 400 pixels to the right of everything already on the page, so existing content isn't touched.
**Extensions:** none.
**Calls:** `create_session` for the file, one `use_figma` that composes the board, and one `get_figjam` read-back. No `whoami` or `create_new_file`. If the plan is a Starter plan or the seat is View or Collab, these three calls count against the monthly allowance of six.
**Rollback:** delete the one board section the write returns. That removes everything drawn inside it, and it happens only on a separate yes from you.

Write it?