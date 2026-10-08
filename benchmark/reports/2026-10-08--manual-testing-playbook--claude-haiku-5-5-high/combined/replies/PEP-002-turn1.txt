```markdown
# Clarification: offline mode Epic

I can draft this once you answer the points below in one reply.

**0. How should I work this?**
- Quick: a lean pass with smart defaults
- Deeper: a fuller pass with more source reconciliation
- No pick means Standard

**1. Child stories: four areas or per platform?**
- Four areas: offline reading, offline editing and creation, sync on reconnect, offline indicator and storage settings
- Per platform: one child each for iOS, Android and Desktop, with every child carrying the conflict dependency
- A mix, such as areas for shared logic and platform children for surface work. Name the mix
- Offline reading and the indicator do not depend on the conflict decision, so the area split lets them start first

**2. Does offline Desktop ship in the shared web client?**
- The product context says Desktop wraps the web client and adds only the capture shortcut
- Offline behavior built into that client would reach Web too, and the brief puts Web out of scope
- Say whether Desktop offline ships in the shared client (Web gets it) or only in the native shell (a separate build)

**3. How should the Epic treat conflict handling?**
- Joana decides on 2026-10-09, and the #sync-eng options were not supplied to me
- Paste the options from the thread, and the Epic names them as open choices
- Or confirm the Epic states conflict handling as open, naming no option
- Or wait for the decision, and I draft after it lands

**4. References**
- Carry the #sync-eng thread, Marta's `lost-edit` tickets or the cancellation survey as links? Without links, References is left out
```

Export-equivalent path: `export/NNN - Epic-offline-mode-clarification.md`

I read Oskar's brief and the product context, and I have not drafted the Epic yet. Two answers shape the structure: the child-story split, and whether Desktop offline sits in the shared web client. The brief excludes Web, but the product context describes Desktop as the web client in a native window, so those two scope lines need to agree before I write any child story. Joana's decision lands tomorrow, so option 3 may settle itself. Once you answer, the Epic comes next as its own block.