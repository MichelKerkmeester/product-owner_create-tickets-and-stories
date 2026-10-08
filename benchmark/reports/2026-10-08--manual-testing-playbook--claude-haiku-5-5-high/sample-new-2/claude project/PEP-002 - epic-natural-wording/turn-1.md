The brief settles most of the Epic: the four areas, the platforms, the exclusions, the Q1 2027 target and the two success measures. I need your answers on the open points before drafting, so this first reply is the question only.

```markdown
I'll write the offline mode epic from Oskar's brief. The brief settles the four areas, the platforms, the exclusions, the Q1 2027 target and the two success measures, so this question covers only what it leaves open. Please answer all of it in one response.

**0. How should I work this?**
- Quick - lean pass on the brief and product context, with defaults where the brief is silent
- Deeper - read both sources closely and check every child story against the brief's scope

**1. Child-story split:**
- Four areas, as the brief gives them: offline reading, offline editing and creation, sync on reconnect, and the offline indicator with storage settings
- One child per platform: iOS, Android and Desktop

My lean is the four areas. A per-platform split repeats the same behavior three times, while the four areas keep the conflict dependency in two children and let reading and the indicator start first, as the brief allows.

**2. Desktop:**
- Desktop wraps the web client, and the brief does not say whether its offline store lives in that client or in the native shell
- The answer decides whether Desktop belongs in the platform children or needs its own

**3. Conflict handling:**
- Joana decides how sync-service handles conflicting edits on 2026-10-09
- Should I draft now and name that decision as an open dependency in Scope, or wait until it lands?

**4. Title:**
- The scope spans iOS, Android and Desktop, so I would use `# Epic - Platform - Offline mode`
- Name another segment if you prefer one
```

Export-equivalent path: `export/NNN - Epic-offline-mode-clarification.md`

I read Oskar's brief and the product context. The Epic comes after you answer, and I have not drafted it yet.