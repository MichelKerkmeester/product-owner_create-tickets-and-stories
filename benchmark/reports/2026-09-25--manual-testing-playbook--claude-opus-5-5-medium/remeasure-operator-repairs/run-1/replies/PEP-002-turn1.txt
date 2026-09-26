```markdown
I'll write the offline mode epic from Oskar's brief. The brief covers the problem, goal, platforms, target, success signals and exclusions. Before I draft, I need a few decisions in one reply.

**1. Child stories:** `## Scope` lists the child stories, so this sets how the epic is built. Which split do you want?
- By area, following Oskar's brief: Offline reading, Offline editing and creation, Sync on reconnect, and Offline indicator and storage settings. This follows the dependency. Reading and the indicator can start now, and the two editing and sync stories wait for Joana's decision on 2026-10-09
- By platform: iOS, Android and Desktop, plus a sync-service story. The context page says Desktop wraps the web client and gets web changes with no Desktop release. That makes the Desktop story web client work, even though Web is out of scope. With this split, the conflict decision blocks every story
- A mix: one story per area, with the iOS, Android and Desktop work split out as tasks inside each story
- Or your own set of stories

**2. The conflict decision:** Offline editing and Sync on reconnect can't be finalised before 2026-10-09. Should I:
- Draft now and mark the conflict handling decision as open in the epic, or
- Wait and write the epic once Joana has decided

The context page also says a protocol change needs every client on a version that speaks the new one. That includes Web, which is out of scope for offline. Should the epic mention this, or leave it to the Sync on reconnect story?

**3. Who it covers:** The brief says "a member". Should guests with edit access also be able to read and edit offline, or is it members only? This sets the title: `Epic - Member - Offline mode` or `Epic - Platform - Offline mode`.

**4. Delivery section:** Do you want a `## Delivery` section with Estimation, Rabbit holes and No-gos? It would hold the Q1 2027 target and Oskar's out-of-scope list. Without it, the target goes in Goal and the exclusions go in Solution.

**5. Links:** Do you have URLs for the brief, the #sync-eng conflict thread or Marta's `lost-edit` tickets? If not, I'll leave References out rather than invent links.

**6. Desktop measure:** Both of Oskar's success signals are measured on mobile sessions or on Support tickets. Is there a Desktop measure to add, or should the release-level criteria cover Desktop through the tickets signal only?
```

Export-equivalent path: `export/001 - Epic-offline-mode-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

I haven't drafted the epic yet. You said you weren't sure how to split the child stories, and that choice decides the whole Scope section. So I've asked it together with the other open points above rather than choosing a split for you.

When you reply, I'll write the epic as `export/002 - Epic-offline-mode.md`. The ClickUp connector isn't available in this session, so I can't offer to push it to ClickUp.