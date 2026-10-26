<figma-url>
Read-back: 9 of 9 nodes, 8 of 8 connectors, first glance: sync-service writing and publishing every change
Left out: a direct link from Apple's push service to the iOS client, which the architecture check doesn't allow; the push worker's link carries the "Wakes iOS devices" label instead
Left out: how the gateway receives changes to send out to other online clients, which your description doesn't state
Finding: The dashed push worker → Apple Push Service link crosses the Stores zone, just above File storage. The board is still correct, but that line reads less cleanly than the others. I can move it if you'd like.
Finding: Each client-to-gateway socket is labelled "Live socket, both ways" but has an arrowhead only at the gateway end.
Finding: Desktop and web share one client node so the diagram stays within nine nodes.
Finding: The board is a new file in <figma-plan-1> File `<test-file-key>` was not touched.
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.