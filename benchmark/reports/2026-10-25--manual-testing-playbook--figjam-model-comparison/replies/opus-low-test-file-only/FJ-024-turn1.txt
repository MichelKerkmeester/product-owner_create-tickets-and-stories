I've stopped before drawing anything, because your two instructions about where the board goes can't both be followed.

**Where the board goes.** You asked for a new board in the Loomlist Engineering plan, and also for the board to go into the existing file `<test-file-key>`. Flow Mode can write to only two kinds of target:
- a new file it creates in a named plan, or
- a board it already wrote earlier in this work.

`<test-file-key>` wasn't written by this work, so it isn't a target I can write into. I haven't made any Figma calls yet, so nothing has been written anywhere.

**What I'd draw** (an architecture diagram, answering "which services sit behind Loomlist block sync, and how does a block change reach each client?"):
- **Clients:** desktop, web and iOS, each holding a live socket to the API gateway.
- **Core:** API gateway → sync-service. Sync-service writes every block change to the blocks database and publishes it to the change stream.
- **Delivery:** the push worker reads the change stream and calls Apple's push service, which wakes sleeping iOS devices.
- **Storage:** the blocks database, file storage and the change stream.
- **Outside the system:** Apple's push service.

**Gaps I'd mark as assumed unless you correct them:**
- **File storage:** none of your notes says which service talks to it. I'd draw sync-service → file storage, marked assumed.
- **Gateway to sync-service:** I'd draw the gateway forwarding socket traffic to sync-service, marked assumed.
- **Awake clients:** none of your notes says how online clients get changes back, for example whether the gateway also reads the change stream. I'd leave that out and name it as a gap.

**Question:** Should I create a new board in the Loomlist Engineering plan and drop the existing file key? And is this reading right, including the three assumed or missing links? Once you answer, I'll come back with the exact plan, file, Figma calls and rollback, and wait for your yes before writing.

Finding: the request names both a new board and the existing file `<test-file-key>` as the target, which conflict.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.