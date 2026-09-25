```markdown
I'll write the offline mode epic from Oskar's brief. Before I draft it, please answer the points below in one reply:

**1. Child-story split:**
- A. Oskar's four areas: offline reading, offline editing and creation, sync on reconnect, and offline indicator and storage settings. Reading and the indicator can start before Joana's conflict decision on 2026-10-09. The other two wait for it
- B. One story per platform: iOS, Android and Desktop. Every story then contains work that waits for the 2026-10-09 decision. The Desktop story would mostly be web-client work, because Desktop wraps the web client that Web deploys
- C. The four areas as stories, with the platform split done at task level, where titles such as `FE - iOS - OFFL - ...` already name the platform
- Something else

**2. Web and the sync protocol:**
- If the 2026-10-09 decision changes the sync protocol, every client needs a version that supports the new protocol, and that includes Web. Should the epic include that client update as a child story, or will the Sync team handle it outside the epic?

**3. Guests:**
- The brief only mentions members. Should a guest with edit access be able to read and edit their shared pages offline, or should guests stay online only?

**4. Delivery view:**
- Should the epic end with a Delivery section (estimation, rabbit holes and no-gos)? If yes, the brief's out-of-scope list goes under No-gos and the pending conflict decision goes under Rabbit holes. If no, I'll put the out-of-scope list in Scope
```

Export-equivalent path: `export/001 - Epic-offline-mode-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

I'm treating this as an Epic, but I haven't drafted it yet. An epic's main job is to list its child stories, and you haven't picked the split, so I've asked the questions above instead of choosing one for you.

**What I found in the brief and the product context:**
- **Desktop is really web-client work.** Desktop runs the web client inside a native window. So a per-platform Desktop story would mostly be work for the web client, even though Web is out of scope.
- **Web may need a sync update anyway.** If Joana's decision changes the sync protocol, every client has to support the new version, Web included, even without offline mode.
- **The four-area split keeps early work moving.** Offline reading and the indicator don't depend on the 2026-10-09 decision, so they can start first. A per-platform split would put waiting work into every story.

Once you answer, I'll write the epic as the next file in this numbering.