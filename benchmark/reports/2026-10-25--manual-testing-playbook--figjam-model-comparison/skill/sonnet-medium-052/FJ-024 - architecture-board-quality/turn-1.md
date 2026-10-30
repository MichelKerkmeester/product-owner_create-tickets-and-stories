Round 1 of 3. This is how I read the request so far.

- **Type:** architecture. You asked which parts make up block sync and how they connect. A sequence would answer the order of one sync, which you didn't ask for.
- **Destination:** the existing file `<test-file-key>`, as a new section beside what it already holds. It is already in Loomlist Engineering, so I create no new file and change nothing already on it.
- **Sources:** your description and the platform doc facts you quoted, read as current behavior. I haven't seen the doc itself.
- **Assumed:** the doc doesn't say what the gateway forwards to sync-service. I would draw `Routes sync requests` on that edge and mark it assumed. A sync-service doc excerpt would settle it.

**Question 1: who reads the board, and what do they decide?**
Reading: no source names a reader. The request reads as an overview of how a block change reaches other devices.
Question: who is it for and what should they be able to do afterwards?
Recommended: Loomlist Engineering. The question is "which parts take part in block sync and how do they connect?" Afterwards they can tell which part to open for a problem with writes, delivery or wake-ups.
Why: it matches the engineering plan the file sits in and the parts you listed.

**Question 2: which detail level, audience and reading distance?**
Reading: you added five rules that sit on single parts. The gateway checks session tokens and keeps sockets open. sync-service merges edits to the same block. The blocks database keeps 30 days of history. The change stream keeps events for 7 days. The push worker sends at most one wake-up per device per minute.
Question: should those rules go on the board, and in whose words?
Recommended: Balanced detail with each rule as a short body under its part. Audience Engineer, so names stay exact (`sync-service`, `API gateway`). Laptop distance.
Why: Balanced is the level that carries a rule under a one-line label, and Engineer keeps your spelling.

**Question 3: what must this board leave out?**
Reading: you named ten parts and an architecture board holds nine. File storage is the odd one out. No source says which part reads or writes it, and every node needs a connector, so drawing it would mean inventing a call.
Question: what should the board not do, and is file storage the part to leave off?
Recommended: leave file storage off and list it under `Left out:` as having no stated call. The board also doesn't show message order or any file upload path.
Why: that keeps all nine parts on one board with eight stated calls, and nothing is invented to fill the gap. If file storage does connect to something, tell me what and I'll split by request path instead.

Take the recommended answers, or correct any of them?