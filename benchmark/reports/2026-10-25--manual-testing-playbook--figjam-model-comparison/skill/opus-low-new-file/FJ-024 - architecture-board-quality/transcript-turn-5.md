# FJ-024 turn 5 transcript

**User:** Use your recommended answers.

**Assistant:**

I'll take that as **<figma-plan-1>**, the one recommendation I gave. Nothing is written yet. This is the write step, and it needs its own yes.

**What the board answers:** which services sit behind Loomlist block sync, and how a block change gets from one client to every device, including a sleeping iPhone.

**Glances**
- First: sync-service, which writes every change and publishes it to the change stream
- Second: the change stream feeding the push worker, which wakes iOS devices through Apple's push service
- Last: the stores (blocks database, file storage) and the client sockets

**Target:** a new FigJam file called "Loomlist block sync" in the **<figma-plan-1>** plan (Pro). It won't touch file `<test-file-key>`.

**What will be written:** one architecture diagram in a framed board with a title, a subtitle, a source line and a colour key. The diagram has 9 nodes and 8 connectors in 6 zones: Clients (Desktop and web, iOS), Edge (API Gateway), Services (sync-service, Push worker), Stores (Blocks database, File storage), Events (Change stream) and Outside (Apple Push Service). No extensions are planned.

**Calls:** `create_new_file` for the board, one `use_figma` call to draw it and one `get_figjam` call to read it back. <figma-plan-1> is a Full seat, so the six-calls-a-month limit doesn't apply.

**Rollback:** delete the new file. Nothing else changes.

**Write this board to a new file in <figma-plan-1>?**
