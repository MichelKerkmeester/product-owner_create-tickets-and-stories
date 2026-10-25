Nothing is written yet. Three things from your list need your answer before I can draw it.

**Settled from your message**
- **Type:** architecture. You asked for the services and how they connect.
- **Target:** the existing FigJam file `<test-file-key>` in the Loomlist Engineering plan. The board goes in as a new section on its one page, so I won't create a file or call `whoami`.

**1. Which calls join the parts**
- **Reading:** you named ten parts but no calls. Your files also don't state the sync path. `loomlist-context.md` only says sync-service keeps devices on the same block version and that push goes through each mobile platform's push service.
- **Question:** is this the path?
  - Each client calls the API gateway.
  - The gateway routes to sync-service.
  - Sync-service writes the blocks database and publishes to the change stream.
  - The push worker consumes the stream and calls Apple's push service to wake the device.
- **Recommended:** yes, drawn as above and marked assumed until you confirm it.
- **Why:** I won't invent a call, and this is the minimum that connects every part except file storage.
- **Also check:** `loomlist-context.md` says pages-service owns blocks and every other service reads block data through it. Does sync-service write the blocks database directly, or through pages-service? I'd draw it directly unless you say otherwise.

**2. File storage**
- **Reading:** no source says which part calls it. Ten parts also go over the architecture budget of nine nodes, and a node with no connector fails the pre-write check.
- **Question:** which part reads or writes file storage?
- **Recommended:** if you don't know, I leave it off and list it as `Left out: file storage, no call stated`. If you name the caller, I split into two boards in the same file: the sync path, and the push wake-up with file storage on its own path.
- **Why:** splitting keeps your ten parts without shrinking the board or guessing a connection.

**3. Reader, question and what to leave off**
- **Reading:** the sources point at the Sync team, led by Joana. The conflict-handling options (A, B or C) are undecided until 2026-10-09.
- **Question:** who reads this board, and what should it not show?
- **Recommended:**
  - **Reader:** Sync and Mobile engineers.
  - **Question:** which parts carry a block change from one client to the others.
  - **Left off:** conflict handling and offline behavior, since neither is decided.
- **Why:** an undecided option drawn as a box would read as current behavior.

If you skip any of these, I proceed on the recommended answers and name them as assumed in the playback before the write. After that I'll send one yes-or-no gate. Its calls are `create_session`, one `use_figma` and one `get_figjam` read-back, and its rollback is deleting the one section I add, only after you say yes.