Before I draw anything, here's how I've read your request. Please confirm or correct it first. Nothing has been written to Figma yet.

**What the board answers:** which services sit behind Loomlist block sync, and how a block change gets from the client that made it to the database, the change stream and a sleeping iPhone.
**Diagram type:** architecture.

**What your description settles**
- **Clients:** desktop, web and iOS, each holding a live socket to the API gateway
- **Edge:** the API gateway
- **Services:** sync-service and the push worker
- **Data:** the blocks database, file storage and the change stream
- **External:** Apple's push service
- sync-service writes every block change to the blocks database
- sync-service publishes every block change to the change stream
- The push worker reads the change stream and sends through Apple's push service to wake sleeping iOS devices

**Assumed until you correct me**
- **Gateway to sync-service:** you didn't name this link. I've assumed the gateway forwards block changes to sync-service.

**Still open**
- **File storage has no link.** You listed it but didn't say which service reads or writes it. If you don't tell me, I'll draw it as an unconnected box rather than guess a link.
- **How awake clients get changes.** Nothing you gave says how a change reaches the other desktop and web clients. It might be the gateway or sync-service reading the change stream and pushing down the sockets. I'll leave that link out unless you name it.

**Where the board goes (to settle before I write)**
- **This conflicts with the drawing rules.** You asked for a new board in the Loomlist Engineering plan, and also asked me to write into the existing FigJam file `<test-file-key>`. The rules allow only two write targets: a new file in a named plan, or a board this work already wrote. An existing file I didn't create isn't one of those, so I can't write into it. My recommendation is a new FigJam file in the Loomlist Engineering plan. If it has to be that file, you'll need to confirm you're overriding the rule. I'll put this to you again when I ask for the go-ahead to write.

Is this reading right, and what reads and writes file storage?