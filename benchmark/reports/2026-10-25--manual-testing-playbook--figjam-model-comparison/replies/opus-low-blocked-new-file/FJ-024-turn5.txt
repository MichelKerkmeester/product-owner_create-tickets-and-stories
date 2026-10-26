<figma-url>
Read-back: 9 of 9 nodes, 8 of 8 connectors. The change stream may not show first, because Figma's automatic layout can't mark a focus.
Left out: file storage, which had no read or write you could name. Live updates to awake desktop and web clients, which weren't described.
Finding: The arrow between the change stream and the push worker points the wrong way. Its arrowhead sits on the change stream, so it reads as the push worker writing to the stream rather than reading from it. The label still says "Consumes". Flip that arrow by hand in FigJam.
Finding: Figma returned this link as a file to claim. Open it and check that the board sits in <figma-plan-1> and not in your drafts. I couldn't confirm the plan from the read-back.
Finding: The board doesn't use our own board style, key, title or source lines, because Figma laid it out automatically. Any change to the look has to be made by hand in FigJam.
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.