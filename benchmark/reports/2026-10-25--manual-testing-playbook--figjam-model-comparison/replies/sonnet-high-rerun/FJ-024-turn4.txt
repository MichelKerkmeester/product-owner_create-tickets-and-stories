<figma-url>
Read-back: 9 of 9 nodes, 8 of 8 connectors, 6 of 6 lanes, first glance: sync-service
Left out: file storage, no stated connection and over the node budget. The Apple Push to iOS connector, because an architecture has no edge from an outside service back to a client, so the last edge's label carries that hop
Finding: `get_figjam` reports connector endpoints and arrow caps but not connector text or dash style. I checked the edge labels and the three dashed edges (Publishes changes, Consumes changes, Apple Push: Wakes iOS devices) on the overview screenshot
Finding: the "Writes blocks" connector runs over the top of the Events lane to reach Blocks database, because that lane stands between Services and Stores. It crosses no node or connector, and the lane order is fixed by the composer, so only a different model would change it
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.