I haven't written the epic yet. You haven't picked how to split the child stories, and the epic's Scope section is built on that split, so I've saved one question for you instead.

Path: `export/001 - Epic-offline-mode-clarification.md`
Verified: read-back succeeded; 18 lines
HVR self-scan: 1 hard blocker. Fixed: Oxford comma in the four-area list. Kept with reason: none.

**Quality:** This is an Epic, and the file holds only the question. Oskar's brief already covers the problem, goal, platforms, success measures and exclusions, so the question only asks about what's still open.

**On the split, the sources point one way.** Oskar's four areas match his own dependency note. Offline reading and the offline indicator can start now, and only two stories wait on Joana's conflict-handling decision on 2026-10-09. A per-platform split would put that decision in front of every story. It would also make the Desktop story mostly web-client work, because Desktop wraps the web client, even though Web is out of scope.

The file also asks three things neither source settles:
- Should I draft now and mark Joana's decision as open, or wait until it lands?
- If her decision changes sync protocol v3, is the Web client update part of this epic? The context page says every client needs a version that speaks the new protocol.
- Do Guests get offline access, or only members?

Answer these in one reply and I'll write the epic as `002 - Epic-offline-mode.md`.