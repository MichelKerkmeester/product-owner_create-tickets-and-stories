<figma-url>
Read-back: 9 of 9 nodes, 8 of 8 connectors, both live sockets drawn two-way, every connector joins the right two services in the right direction, first glance: the Change stream
Left out: the push to awake desktop, web and iOS clients, because the brief doesn't say how they receive changes
Left out: a connector from Apple's push service to the iOS client, because the diagram check doesn't allow an external service to connect straight to a client. The Push worker connector's label says it wakes sleeping iOS devices instead
Finding: two lines cross. The line from sync-service to File storage crosses the line from the Change stream to the Push worker, just right of the Services area. Reshaping the model and redrawing would fix it. Reply if you want that.
Finding: "Stores block files" is an assumption: you didn't say what reaches File storage. Tell me which service writes to it and I'll correct the board.
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.