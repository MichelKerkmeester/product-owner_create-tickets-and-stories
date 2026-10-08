```markdown
# Offline mode epic, clarification

I'll write the offline mode Epic. Before drafting, I need three decisions in one response.

**1. Child story split**

Your brief names four areas: offline reading, offline editing and creation, sync on reconnect, and the offline indicator with storage settings. Which split should the child stories follow?

- Four areas, with each story covering iOS, Android and Desktop
- One story per platform, with each story covering all four areas

A mix is also possible if the platforms diverge, for example a separate Desktop story. Two facts bear on the choice. The house Epic groups child stories by part of the lifecycle, so the four areas avoid writing the same queue and sync rules once per platform. Desktop wraps the web client, and a web change reaches Desktop users with no Desktop release. Does Desktop's offline storage live in the web client code or in the native shell?

**2. Conflict decision timing**

Joana decides how sync-service handles conflicting edits on 2026-10-09, which is tomorrow. Should I wait for that decision before drafting the offline editing and sync stories? Or should I draft them now and mark them as waiting on her decision? Either way, the Epic will say which stories depend on it.

**3. Success measure**

The 23% figure counts sessions that started without a connection or lost it within the first minute. The 8-week target counts mobile sessions that hit the no-connection screen. Which measure should the target use, and what is its current baseline?

**Title**

Unless you say otherwise, the Epic title is `Epic - Platform - Offline mode`, since the work spans iOS, Android and Desktop.

Reply with the answers in one message, and I will draft the Epic.
```

Export-equivalent path: export/NNN - Epic-offline-mode-clarification.md

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

I have not drafted the Epic yet. The child story split is still open, and the brief leaves conflict handling unsettled until 2026-10-09, so the editing and sync stories depend on that decision. I read Oskar's brief, the product context, the Epic template and the Story Mode guidance. Once you answer, the Epic takes the next number in the Epic lane.