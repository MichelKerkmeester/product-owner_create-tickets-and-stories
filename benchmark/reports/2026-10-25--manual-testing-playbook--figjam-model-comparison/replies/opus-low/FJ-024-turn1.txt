I haven't written anything yet. Before I draw, here's how I read your request.

**What I checked**
- **Your Figma plans:** your account holds three plans: <figma-plan-3> (Starter, View seat), <figma-plan-1> (Pro, Full seat) and <figma-plan-2> (Pro). None of them is called "Loomlist Engineering", so I can't place the board there.
- **File `<test-file-key>`:** Flow Mode only writes into a new file or into a board it created earlier in this work. That file already existed and I didn't create it, so I won't write into it.
- **Where the board would go:** your fallback applies. I'd create a new FigJam file in the **<figma-plan-1>** plan and leave it in drafts, with no project. I'd only create it after you say yes to the write, which I'll ask about separately.

**The question the board answers:** which services carry a Loomlist block change from one client to every other device, including a sleeping iPhone?

**Outline (nodes):**
- **Clients:** Desktop client, Web client, iOS client
- **Edge:** API gateway
- **Services:** sync-service, Push worker
- **Data:** Blocks database, File storage, Change stream
- **External:** Apple Push Notification service (APNs)

**Outline (connectors):**
1. Desktop, Web and iOS → API gateway: live socket, drawn two-way. You stated this.
2. API gateway → sync-service: block changes. This step is implied, not stated.
3. sync-service → Blocks database: writes every block change. You stated this.
4. sync-service → Change stream: publishes each change. You stated this.
5. Push worker ← Change stream: reads the stream. You stated this.
6. Push worker → APNs → iOS client: wakes sleeping devices. You stated this.
7. File storage: **assumed** to be reached from sync-service, labelled "files attached to blocks". You named file storage but not what connects to it. The alternative is to show it with no connector and a note.
8. Change stream → sync-service → gateway, fanning changes out to other live clients: **assumed** and **left out**. You didn't say how awake clients receive changes.

**Two framings**
- **Architecture by zones (recommended):** Clients | Edge | Services | Data | External, laid out left to right. It answers "what talks to what" in one glance.
- **Sequence of one edit:** shows the order of steps, but it hides the database and file storage roles.

**Look**
- **Title:** "Loomlist block sync, services"
- **First glance:** the Change stream, because it's where the write path hands off to the push path.
- **Labels:** every assumed edge is marked as assumed on the board.

**Please confirm or correct these four points:**
1. A new file in the <figma-plan-1> plan, in drafts.
2. Where file storage connects.
3. Whether to draw the fan-out to live clients.
4. The architecture framing.

Once you've confirmed, I'll send the checked diagram model and ask you separately to approve the write.