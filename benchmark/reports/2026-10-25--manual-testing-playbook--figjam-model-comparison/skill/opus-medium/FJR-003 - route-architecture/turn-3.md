Reading confirmed. This is the write gate, and nothing has been written yet.

**What the board answers:** which services a block edit passes through on protocol v3 today. After reading it, someone can say where a block edit goes and which service decides which version is kept.

**What should catch the eye, in order**
- First: sync-service, the service that decides which version of a block is kept (marked as the focus node)
- Second: the path from the two client nodes through Entry point into sync-service, then on to pages-service
- Last: Block storage and the source line, which name the two assumed parts and what was left out

**The write**
- Plan: <figma-plan-1> (`team::1297132374291579406`), where you have a Full seat on Pro. It goes to your drafts, with no project
- File: a new FigJam file named "Loomlist block sync on protocol v3", not `<test-file-key>`
- Board: one framed architecture with 6 nodes and 5 connectors across four lanes: Clients, Edge, Services and Stores. It has a title, subtitle, key and source line, and the source line names Entry point as assumed and Options A, B and C as left out. It passed the pre-write check and the composer, at 48,513 of the 50,000 characters one call allows
- Extensions: none
- Calls: `create_new_file`, `create_session`, one `use_figma` to compose the board and one `get_figjam` to read it back. That's 4 calls
- Rollback: delete the new file. Nothing outside it is touched

Shall I create the file and write the board?

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.