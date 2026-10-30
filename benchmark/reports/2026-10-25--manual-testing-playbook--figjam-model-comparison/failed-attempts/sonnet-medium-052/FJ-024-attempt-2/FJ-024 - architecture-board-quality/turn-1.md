I read this as an architecture: you named parts and the calls between them, not an order of messages. A sequence would answer the order of calls, which you didn't ask for. Nothing is written to the board yet.

**What I've settled from your message**
- **Target:** the existing file `<test-file-key>`. The board goes in as a new section beside what's there and nothing already on it changes. I won't create a file, and I take the Loomlist Engineering plan from you.
- **Source:** the platform doc as you quoted it. I treat it as current behavior.
- **Calls the doc states:**
  - All three clients hold a live socket to the gateway, which I'll draw as two-way for desktop, web and iOS alike.
  - The gateway routes to sync-service.
  - sync-service writes the blocks database and publishes to the change stream.
  - The push worker reads the stream and calls Apple's push service to wake iOS devices.
- **Rules I'd show under their parts:**
  - Gateway: checks the session token and keeps each socket open.
  - sync-service: merges edits to the same block.
  - Blocks database: keeps 30 days of history.
  - Change stream: keeps events for 7 days.
  - Push worker: sends at most one wake-up per device per minute.
- **Drawing limit:** the architecture layout has no edge from an outside system to a client. The iOS wake-up will be a labelled call from the push worker, not a line from Apple's push service to the iOS app.

**1. Reader and outcome**
Reading: no source names who this board is for.
Question: who reads it, and what should they be able to decide afterwards?
Recommended: engineers new to block sync. The board answers "which parts carry a block change from one client to the others, including a sleeping iOS device, and which part owns each rule?"
Why: the doc's facts are per-part rules, which is what an engineer needs to place.

**2. File storage and the node budget**
Reading: you named ten parts and the architecture budget is nine. The doc gives file storage no caller and no callee, and a node with no connector fails the pre-write check. I won't invent a call for it.
Question: does the doc say which part uses file storage?
Recommended: leave it off and name it as "no call stated in the doc", which puts the board at 9 nodes.
Why: if you give me the caller, ten parts means two boards, sync path and wake-up path, and I'll offer that split instead.

**3. Dials and what the board must not do**
Reading: you gave exact service names and retention numbers.
Question: are these settings right, and is there anything the board must not show?
Recommended:
- **Detail:** Balanced, so the five rules sit as short lines under their parts.
- **Audience:** Engineer, so `sync-service` keeps its exact name.
- **Distance:** Laptop.
- **Must not:** show the order of calls, draw the iOS wake-up as a separate line from Apple's push service, or add parts the doc doesn't name.

Why: Balanced and Engineer keep the numbers and names as written.

Take the recommended answers, or correct any of them?