# Offline mode epic, intake question

Before I draft the epic from Oskar's brief and the Loomlist context page, I need these decisions in one reply:

**1. How to split the child stories:**
- By area, one story for each of the brief's four areas (reading, editing and creation, sync on reconnect, indicator and storage settings). This matches the brief's dependency line. Reading and the indicator can start before Joana's conflict decision on 2026-10-09. The other two can't
- By platform, one story each for iOS, Android and Desktop. According to the context page, Desktop wraps the web client, so Desktop work ships as web client changes without a Desktop release. iOS and Android ship every two weeks with a 7-day rollout
- Both, with four area stories and iOS, Android and Desktop work as tasks under each
- A different split you have in mind

**2. Desktop versus the browser:**
- The brief puts Web out of scope, but Desktop runs the same web client. Should the epic say that a browser tab gets no offline behavior, or is that already settled somewhere else?

**3. The pending conflict decision:**
- Should I draft now and mark the conflict decision as pending under editing and sync, or wait until Joana decides on 2026-10-09?
- If the decision changes sync protocol v3, every client has to be on a version that supports the new protocol. Should the epic list that as a release condition for the Q1 2027 target?

**4. Release-level success:**
- The brief measures mobile sessions and `lost-edit` tickets. Should Desktop get its own success condition, or do those two measures cover the release?

**5. Links and a delivery view:**
- Can you send links to the brief, the #sync-eng thread and any design files for References?
- Do you want a Delivery section with estimation, rabbit holes and no-gos? If you do, the brief's out-of-scope list goes under no-gos
