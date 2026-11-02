# Epic - Offline mode, clarification

I'll write the offline mode epic from Oskar's brief. The Problem, Goal, platforms, success signals and exclusions are all in the brief. Before drafting, I need the decisions below in one reply.

**Child-story split:** Which way should `## Scope` split the child stories?

A. Oskar's four areas, which are Offline reading, Offline editing and creation, Sync on reconnect plus Offline indicator and storage settings. This matches the dependency in the brief. Reading and the indicator can start now, and only two stories wait on the 2026-10-09 conflict decision

B. One story per platform: iOS, Android and Desktop. Each story would hold all four areas, so the conflict decision blocks every story. Desktop wraps the web client, and a web client change reaches Desktop with no Desktop release. That makes the Desktop story web client work, even though Web is out of scope

C. Four area stories, with platform differences written inside each story instead of as separate stories

**Conflict handling:** Joana decides on 2026-10-09 how sync-service handles conflicting edits. Should I draft now and name that decision as open in the two stories it blocks, or wait until it lands?

**Web and the sync protocol:** The context page says a protocol change needs every client on a version that speaks it. If Joana's decision changes protocol v3, does the Web client update count as part of this epic, or as work outside it, even though offline mode stays out of scope on Web?

**Who gets offline access:** The brief says "a member". Should Guests with view or edit access to a page also get offline access to it, or is this epic for Members, Admins and Owners only?
