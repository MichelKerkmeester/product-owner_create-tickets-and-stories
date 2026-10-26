Round one is settled, so here is round two of three. Nothing has been written to Figma.

**Settled so far**
- **Reader:** Loomlist engineers new to block sync, during onboarding or a design review (assumed from my suggestion)
- **Question:** which services does a block edit pass through to reach the other clients, and how does iOS get notified? (assumed)
- **Outcome:** the reader can name which service owns each step and knows where to look when an edit fails to sync (assumed)
- **Parts:** the 10 you listed, each placed in its lane
- **Target:** a new FigJam file in <figma-plan-1>, left in drafts with no project

**Round two: start, end and connections**

1. **Start and end**
   - What I see: the question follows one block edit.
   - Question: where does the board start and end?
   - My suggestion: it starts with a block edit on any client. It ends when the edit is saved in the blocks database and has reached the other clients, with iOS notified through APNs.
   - Why: that follows the question exactly and leaves out sign-in and first load.

2. **Which part calls which**
   - What I see: you named the parts but not the connections, and I won't make those up.
   - Question: is this list right?
     - Desktop, web and iOS each keep a live two-way connection to the API gateway
     - The API gateway sends the edit to sync-service
     - sync-service writes the block to the blocks database
     - sync-service stores attachments in file storage
     - sync-service publishes the change to the change stream
     - The push worker reads the change from the change stream
     - The push worker asks APNs to notify the iOS app
   - My suggestion: use the list as written, and correct any line that's wrong.
   - Why: it's the usual path for these parts, but none of it comes from you yet, so every line counts as assumed until you confirm it.
   - Can't be drawn: an arrow from APNs to the iOS app, because the diagram can't link an outside service straight to a client. I'll show that step in the APNs arrow's label instead.

3. **Ten parts is one too many for one diagram**
   - What I see: one diagram holds at most 9 parts, and you listed 10.
   - Question: should I split it into two diagrams in the same file?
   - My suggestion: yes, two diagrams. **1. Block edit sync** shows the three clients, the gateway, sync-service, the blocks database, file storage and the change stream (8 parts). **2. iOS push** shows the iOS app, the gateway, sync-service, the change stream, the push worker and APNs (6 parts).
   - Why: each diagram follows one path and keeps every part you asked for. The other option is to leave one part out.

As before, a skipped question takes my suggestion and is listed as assumed in the summary I send before asking to write.