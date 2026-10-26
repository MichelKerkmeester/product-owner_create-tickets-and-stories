I've read the request as an architecture diagram. Nothing has been written yet. Please check what I took from it before I build the model.

**What the board answers:** which services sit behind Loomlist block sync, and how a block change gets from one client to every device, including a sleeping iPhone.

**What your message settles**
- Clients: desktop, web and iOS
- Clients → API gateway: each client holds a live socket to the gateway
- Sync-service → blocks database: it writes every block change
- Sync-service → change stream: it publishes every change
- Push worker ← change stream: it reads the stream
- Push worker → Apple's push service → iOS: it wakes sleeping iOS devices

**What I've assumed (each one is drawn only if you confirm it)**
- Gateway → sync-service carries the block changes. You didn't name this link, but nothing else connects them
- Sync-service → file storage, for attachments. You listed file storage but gave it no connection. Without a source I'd leave it unconnected, or leave it off
- Changes reach other online clients back through the gateway's socket. You didn't say so, so I won't draw a stream-to-gateway link unless you confirm it
- Zones: Clients · Edge (gateway) · Services (sync-service, push worker) · Data (database, file storage, change stream) · External (Apple's push service)
- First glance: sync-service publishing to the change stream

**Problem with the target file:** I can't write into `<test-file-key>`. Flow Mode only writes to a new file it creates, or to a board this work already wrote. That file is neither, so a write could change content someone else owns. Your message also asks for both "a new board" and "the existing file", and those can't both happen. My suggestion is a new FigJam file in the Loomlist Engineering plan. I'll check that plan exists before asking you to approve the write.

**One question:** are the three assumptions right (gateway → sync-service, how file storage connects, the live fan-out back through the gateway), and is a new file in Loomlist Engineering OK instead of the existing file?