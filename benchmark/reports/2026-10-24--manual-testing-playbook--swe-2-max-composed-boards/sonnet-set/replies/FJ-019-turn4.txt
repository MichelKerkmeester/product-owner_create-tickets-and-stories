<figma-url>
Read-back: 9 of 9 nodes, 8 of 8 connectors, 6 of 6 lanes, 3 of 3 dashed async or outside edges, first glance: sync-service
Left out: file storage, no call stated
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

The "Block sync" section is in the existing file `<test-file-key>`, 400 pixels right of the earlier content. The write returned no warnings.

Findings from the overview screenshot, each fixable only by reshaping the model and recomposing after your yes:
- **"Edge" zone label:** the Web Client connector arcs over the top of the zone and runs through the "Edge" title before it reaches API Gateway. The two "Syncs blocks" labels also sit close together at the left.
- **"Events" zone label:** the Consumes connector leaves the top of Change Stream through the "Events" title.
- **"Consumes" label:** the Consumes route crosses the Publishes line, and its label sits on that crossing.
- **Focal node:** no node carries the accent colour, so sync-service doesn't win by colour. Marking it would make it the first glance on the board.

My fix for the crossing is to declare Push Worker before sync-service in the Services lane. I'd also mark sync-service as the focus node. It is an attempt, not a guarantee, and I have two attempts before I stop and ask.

The connectors, their direction and lane membership were matched against the model from the outline `get_figjam` returned. The connector labels were read from the compose return and the screenshot. All 8 calls on the board are the ones you confirmed. No source states them.

Do you want me to recompose with the reordering and the focus mark? If so, I'll ask separately before deleting the current section (id `47:1934`).