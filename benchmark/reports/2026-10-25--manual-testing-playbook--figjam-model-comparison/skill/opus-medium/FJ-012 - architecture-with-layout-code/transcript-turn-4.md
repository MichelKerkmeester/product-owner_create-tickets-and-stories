# FJ-012 turn 4 transcript

**User:** Use your recommended answers.

**Assistant:**

Here is the full summary of the board. Confirm it or correct any line before I build it.

**What the board is for**
- **Question:** which services does a block edit pass through to reach the other clients, and how does iOS get notified?
- **Outcome:** a Loomlist engineer new to block sync can name which service owns each step and knows where to look when an edit fails to sync

**1. Block edit sync** (8 parts, 6 connections; sync-service is highlighted)
- Desktop, web and iOS each keep a live two-way connection to the API gateway
- The API gateway sends the edit to sync-service
- sync-service writes the block to the blocks database
- sync-service stores attachments in file storage
- sync-service publishes the change to the change stream

**2. iOS push** (6 parts, 5 connections; the push worker is highlighted)
- The iOS app keeps a live two-way connection to the API gateway
- The API gateway sends the edit to sync-service
- sync-service publishes the change to the change stream
- The push worker reads the change from the change stream
- The push worker asks APNs to notify the iOS app

**Where each fact comes from**
- **Your request:** the parts and their names, kept exactly as you wrote them
- **Your yes to my suggestions:** the reader, the question, the outcome, the start and end, the connections, the split and what each diagram highlights

**Assumed, and how to settle it**
- **It's the current system.** Each diagram's source line will say it's based on your message and not checked against code. An engineering doc or a look at the code would settle this.
- **APNs reaching the iOS app.** The diagram can't draw an arrow from an outside service to a client, so the last step appears only in the label "APNs: Notify iOS". Nothing settles this, because the diagram type doesn't allow that arrow.

**Not on the board:** sign-in, first load and anything that happens after a client receives the change.

Is this the system you want on the board?
