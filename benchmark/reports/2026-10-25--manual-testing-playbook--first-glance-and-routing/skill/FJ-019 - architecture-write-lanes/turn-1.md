I haven't written anything to the file yet. Your request names the ten parts, but it doesn't say which part calls which. An architecture board needs those calls, and I won't invent them. Here are the three questions that settle the board.

**1. Reader, question and outcome**
- Reading: the request names no reader, and the Loomlist context page doesn't say who asks for this board.
- Recommended: the board is for engineers and product people on the Sync team. The question is "which parts take part in block sync and how do they connect?" The outcome is that they can see which part carries a block change from one client to the others.
- Why: that is the question an architecture answers. The board would not show the order of one sync, which is a sequence, or any endpoint detail.

**2. The calls between the parts**
- Reading: no source for the wiring is in this session. The context page has `sync-service` but none of the other parts you named. It also says `pages-service` owns block data and `notifications-service` owns push.
- Recommended: this wiring, drawn from the lane rules and the packet's worked example. It is not Loomlist fact, and I would mark it assumed on the board unless you confirm it:
  - Desktop, Web and iOS call the API gateway
  - The gateway routes to sync-service
  - sync-service writes to the blocks database and publishes to the change stream
  - The push worker consumes the change stream
  - The push worker calls Apple's push service to wake iOS devices
- Why: these are the only edges the lane rules allow between those parts. If you have a sync doc or can correct the list, that source wins. Should `pages-service` sit between sync-service and the blocks database?

**3. Ten parts against a budget of nine**
- Reading: an architecture holds at most 9 nodes. Your list has 10, and file storage is the only part with no call in the wiring above.
- Recommended: if sync never touches file storage, draw nine parts and name file storage under `Left out:`. If it does touch it, I'd split into two boards in the same file and offer both together.
- Why: a split keeps every part you named, while a cut drops one, so I want your answer before choosing.

I'll write into the existing file `<test-file-key>` as a new board section. That means no new file, and the board stays in the Loomlist Engineering plan you named. Once you answer, I'll play back the full reading for one more check. Then I'll ask separately whether to write, naming the file, the plan and the calls.