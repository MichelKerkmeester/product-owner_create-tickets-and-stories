The model passed `flow_check.py` and composes cleanly. One edge label changed from the outline: "Apple: Wakes sleeping iPhones", so it fits the 32-character Meeting screen limit.

**Question:** how does block sync work, in the parts a leadership reader needs to follow?
**Outcome:** leadership can see that the sync platform stores every change and that sleeping iPhones are woken through Apple's push service.
**First glance:** Sync Platform, the one part every change passes through.
**Second glance:** the Change Store, which holds every change.
**Last glance:** Apple Push Service, the dashed outside hop that wakes sleeping iPhones.
**Plan and file:** Loomlist Product plan, in the existing FigJam file `<test-file-key>`. The board is added as a new section beside what the file already holds, and nothing already on it changes. No new file is created.
**Writes:** one composed board with 7 nodes and 6 connectors in 5 lanes, plus a title, a key and a source line, at Meeting screen distance.
**Extensions:** none.
**Calls:** `create_session`, one `use_figma`, one `get_figjam` read-back and, if the page already has content, one `get_figjam` read before the write. That is at most four tool calls, which matters if the file sits on a Starter plan or a View or Collab seat, since those allow six a month.
**Rollback:** delete the one board section the write returns, and only on your reply naming it.
**If the file cannot be written:** I stop and ask. I do not create a file unless you say so, and then it goes in the Barter team plan, in drafts, with no project.

Write it?