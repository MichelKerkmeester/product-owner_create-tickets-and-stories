[Block sync board](<figma-url>

Read-back: 9 of 9 nodes, 8 of 8 connectors, 2 of 6 lanes drawn as sections, 1 of 8 connectors reversed

One connector is wrong and two things render weaker than the model.

The Consumes connector runs from Change Stream to Push Worker with its arrowhead at the Change Stream end, so it reads as the worker feeding the stream rather than reading it. You can see it at the lower right of the screenshot.

Only Clients and Services became lane sections. The other four lanes hold one node each, so the API Gateway, Blocks DB, Change Stream and Apple Push sit loose inside the Block sync section. Their labels still carry the meaning, there is just no container around them.

The three client connectors share one vertical trunk into the API Gateway, so both WebSocket labels and the HTTPS label stack on a single line and stop saying which client uses which.

The title is on the board, 73 pixels above the diagram.

A redraw is the only move open to me here, because the generator owns the layout and the model gives me no lever over that arrow beyond declaration order. It may land the same way. If it does, dragging that connector end in FigJam takes a moment and changes nothing the board says.

Left out: file storage, because no source states a call from Sync Service to it and the nine node budget was already full

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.