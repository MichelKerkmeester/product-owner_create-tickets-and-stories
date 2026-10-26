<figma-url>
Read-back: 7 of 7 nodes, 6 of 6 connectors, 5 of 5 lanes, first glance: Sync Platform
Left out: Apple's hop from its push service to the phone, because the architecture layout allows no arrow from an outside system back to an app, so the edge label "Apple: Wakes sleeping iPhones" carries it
Finding: the file already holds an older "Block sync" board (`119:5058`), aimed at engineers. I left it untouched, so the file now has two block sync boards, and you may want to retitle one.
Finding: "Entry Point" is an assumed node, because the layout needs a gateway between the apps and the sync platform. The source line on the board says so, and the engineering owner can confirm the real name.
Finding: the edge label is "Apple: Wakes sleeping iPhones", not the "Apple Push: …" form in the outline, so it fits the 32-character Meeting screen limit.
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.