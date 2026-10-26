<figma-plan-1> is set as the plan. Your "yes" settled where the board goes. It doesn't approve the write, so here is what the write would do. Nothing has been written to Figma yet.

**What the board answers:** which services sit behind Loomlist block sync, and how a block change gets from a client through sync-service to the blocks database, the change stream and a sleeping iPhone. A reader should be able to follow one change end to end without the model beside them.

**What a reader sees first, second and last**
- **First:** the change stream, which I've set as the focus. It's where one write fans out to the rest of the system.
- **Second:** sync-service writing every change to the blocks database and publishing it to the stream.
- **Last:** the three client sockets to the gateway, and the push worker waking iOS through Apple's push service.

**Where it goes:** a new FigJam file named "Loomlist block sync" in the <figma-plan-1> plan (Pro, Full seat). It does not go into `<test-file-key>`, which I can't write into because I didn't create it.

**What gets written:** one architecture diagram with 9 boxes and 8 arrows, with no extra notes or pins. The check script passed it, after two changes from the reading you confirmed:
- **File storage is left out of the drawing.** The check script won't accept a box with no arrows. Earlier I said I'd draw it unconnected, but that isn't possible. It's named in the board's source line instead.
- **There's no separate arrow from Apple's push service to iOS.** The script doesn't allow an arrow straight from an outside service to a client, so the push worker's arrow carries the label "Wakes sleeping iOS".

**Figma calls it would use:** 4. One creates the file, one opens a working session on it, one draws the diagram and one reads the board back to check it. The Pro plan has no monthly limit that this would come close to.

**Undo:** delete the new file. Nothing else in the plan is touched.

Shall I write this board to a new file in <figma-plan-1>?