The model passes the pre-write check and both diagrams compose. Before anything is written, here's what the write would do.

**Purpose**
- **Question:** which services does a block edit pass through to reach the other clients, and how does iOS get notified?
- **Outcome:** a Loomlist engineer new to block sync can name which service owns each step and knows where to look when an edit fails to sync

**What the eye should land on**
- **First:** sync-service in **1. Block edit sync** and the push worker in **2. iOS push**
- **Second:** the arrows from sync-service to the blocks database and the change stream, which show where an edit is saved and where it's sent on
- **Last:** the source line under each key, saying the board isn't checked against code

**Correction to my summary:** diagram 1 has 7 connections, not 6. I miscounted the three client connections as two. The connections themselves haven't changed.

**What gets written**
- **Where:** a new FigJam file named "Loomlist block sync" in the <figma-plan-1> plan, left in drafts with no project. You have a Full seat on a Pro plan there, so Figma's six-calls-a-month limit doesn't apply.
- **1. Block edit sync:** 8 parts, 7 connections and 5 lanes, with a title, subtitle, key and source line
- **2. iOS push:** 6 parts, 5 connections and 5 lanes, with a title, subtitle, key and source line. It sits to the right of diagram 1.
- **Extras:** none. No notes or pins.

**Figma calls (5 in total)**
- `create_new_file` to make the FigJam file
- `create_session` for that file
- `use_figma` once per diagram, so twice
- `get_figjam` to read the board back

**How to undo it:** delete the new file. Nothing outside it changes, and the file `<test-file-key>` isn't touched.

Shall I create the file in <figma-plan-1> drafts and draw both diagrams?