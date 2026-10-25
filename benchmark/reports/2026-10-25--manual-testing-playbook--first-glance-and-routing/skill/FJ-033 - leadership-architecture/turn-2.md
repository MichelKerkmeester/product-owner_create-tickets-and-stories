The model passed the pre-write check and composes cleanly. This is the gate, and nothing has been written yet.

**Question:** how does a block change travel from one Loomlist app to the others?
**Outcome:** leadership can see which parts carry a block change from one device to the rest.
**First glance:** Sync Platform, where every change from the apps arrives and is written.
**Second glance:** the three apps that send changes in through the Entry Point.
**Last glance:** the source line, which names what the board leaves out.

**Assumed, from your yes**
*   The context page governs current behavior, because question 1 went unanswered
*   Android is not drawn
*   Entry Point and Block Store are named in capability words, and the source line says the Entry Point is assumed
*   Executive audience at Laptop reading distance

**Left out:** the Apple push wake-up and the "every change" history, both contested by the context page and the #sync-eng thread. Android, since it was not named. Conflict-handling options and offline mode plans.

**File:** the existing FigJam file `<test-file-key>`, which you said sits in the Loomlist Product plan. I have not confirmed that plan from the file.
**Writes:** one new board section named "Block sync", with 6 nodes and 5 connectors in 4 lanes, a title, a subtitle, a key and a source line. The existing content stays untouched.
**Extensions:** none.
**Calls:** `create_session`, one `use_figma` and one `get_figjam` read-back.
**Rollback:** delete that one board section, and only after you say yes to the deletion.

Write it?