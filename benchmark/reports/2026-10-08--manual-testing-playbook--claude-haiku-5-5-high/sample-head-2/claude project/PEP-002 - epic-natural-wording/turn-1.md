```markdown
# Offline mode epic, clarification before drafting

I can draft the Epic from Oskar's brief. The brief already settles the problem, goal, the four scope areas, the Q1 2027 target and the two success measures. Three points stay open, and I need your answer to all of them before I draft.

1. Child story split. Should the child stories follow Oskar's four areas (offline reading, offline editing and creation, sync on reconnect, offline indicator and storage settings), or one set per platform covering iOS, Android and Desktop?

   - Four areas: offline reading and the indicator can start before the conflict decision lands, as the brief notes
   - One set per platform: the mobile apps and Desktop ship on separate schedules, but every story covering editing or sync waits for the conflict decision

2. Conflict decision timing. Joana decides how sync-service handles conflicting edits on 2026-10-09. Should I draft now and mark the child stories that depend on it as waiting, or hold the whole Epic until that decision lands?

3. Desktop local copy. The brief leaves Web out because a browser tab cannot keep a local copy between visits. Desktop wraps the web client in a native window, but the brief does not say how Desktop keeps its offline copy. Should Desktop use the native shell's storage, or the web client as it runs today? Which applies, or is it still open?

Reply with your answer to all three points, or with any other direction you want the Epic to take.
```

Export-equivalent path: export/NNN - Epic-offline-mode-clarification.md

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

The Epic comes next once you answer. I haven't drafted it yet because the split and the conflict timing would change its structure.