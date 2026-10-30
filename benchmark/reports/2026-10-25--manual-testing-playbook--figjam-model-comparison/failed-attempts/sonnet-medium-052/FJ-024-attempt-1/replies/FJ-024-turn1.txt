I'm not drawing yet. This is intake round one. Your message settles several rows, and four things need your answer first.

**What your message settles**
- **Type:** architecture. You ask which parts make up block sync and how they connect, and that is the question this type answers.
- **Target:** a new section in file `<test-file-key>`, beside what the file already holds. Nothing already there changes. The write gate will name the Loomlist Engineering plan as the one you gave, because the file's plan can't be checked from my side.
- **Sources:** your message and the platform doc facts you quoted. I haven't seen the doc itself, so I'm taking those facts as current behavior, marked assumed.
- **Stated connections:**
  - Clients to gateway, as a live two-way socket.
  - Sync-service to blocks database.
  - Sync-service to change stream.
  - Change stream to push worker.
  - Push worker to Apple's push service.
- **Inferred, not stated:** gateway to sync-service. I'm assuming the gateway routes requests there, and the source line will say so.
- **Not drawable as an arrow:** Apple's push service waking the iOS device. An architecture board has no edge from an outside system to a client, so that hop goes into the push worker's edge label and under `Left out:`.

**Round one**

Reading: no source names who reads this board or what they ask of it. Your parts and the retention numbers suggest engineers following the sync path.
Question: who is the reader, what question do they bring and what should they be able to decide afterwards?
Recommended: engineers new to the sync path ask "how does a block change reach every device, and how does a sleeping iPhone get woken?" and leave knowing which part to look at when a change doesn't arrive.
Why: that is the question your two paragraphs answer, and it is the only one the board needs to win.

Reading: the platform doc facts are specific numbers (30 days of block history, 7 days of stream events, one wake-up per device per minute) and exact service names.
Question: what are the detail level, audience and reading distance?
Recommended: Balanced detail, so each part carries its rule in a short body such as "keeps 30 days of block history". Engineer audience, so exact names and numbers stay. Laptop distance.
Why: the numbers are what a reader can't guess, and Balanced is the level that keeps them.

Reading: you listed 10 parts, and the architecture budget is 9 parts. File storage is the odd one out because no source says which part reads or writes it. Every part on the board needs a connection, and I won't invent a call.
Question: what must this board not do?
Recommended: it must not draw a call no source states, and it must not turn into a message-order sequence. That leaves file storage off this board, named under `Left out:` as having no stated connection, and the board holds 9 parts. If you tell me what talks to file storage, I'll draw it and split the board in two instead.
Why: that keeps the board to the connections the doc states, and it stays within budget without dropping a part you named for a reason other than a missing edge.

Take the recommended answers, or correct any of them?