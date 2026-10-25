<figma-url>
Read-back: 9 of 9 nodes, 8 of 8 connectors, 6 of 6 lanes, first glance: sync-service
Left out: file storage, no call to or from it was named. Apple push service to the iOS device is not drawn, because the architecture lanes have no edge from an outside system back to a client
Findings from the overview:
- **"Live socket" from iOS client:** the connector leaves the left of the iOS client, runs up the left edge of the Clients zone and across the top of the board to the API gateway. It crosses no node, but it is the longest line and the other two sockets are short. The composer chose the route, and the only levers are declaration order and the edge set. One fix is to recompose with the iOS client declared first, which may or may not move the route. I would do that only on your yes, and it adds a second board beside this one until you approve deleting the old one.
- **"Publishes changes" and "Consumes":** the six lanes run in a fixed order, so Events sits after External. Both stream edges therefore pass through the External zone, one along its top edge just above its title and one along its bottom edge. No model change moves a lane, so the fix is a hand edit in FigJam, or leaving it.
- **First glance:** an architecture takes no accent colour, so nothing on the board marks sync-service. Its position mid-board is all that draws the eye.
- **Not confirmed by `get_figjam`:** it doesn't return connector labels or dashes. I checked those, and the three dashed async or outside edges, on the composing call's screenshot only.

Not done: Figma's `figma-use` and `figma-use-figjam` skills weren't loaded before the write, because this session has no tool to read them. The write ran without errors or warnings.

The new section sits to the right of the existing content in the file, and nothing existing was touched. The temporary model and code files are deleted, and nothing was saved to `export/`.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.