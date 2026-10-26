Round one of the intake is below. Nothing has been written to Figma.

**What your request already gives me**
- **Type:** an architecture diagram, showing which parts make up block sync and how they connect
- **Lanes:**
  - Clients: desktop, web and iOS
  - Gateway: the API gateway
  - Services: sync-service and the push worker
  - Async: the change stream
  - Stores: the blocks database and file storage
  - External: Apple's push service (APNs)
- **Connections:** none given yet. Round two asks which part calls which.

**Where the board goes**
- **The existing file is out.** I can't draw into `<test-file-key>`, because a new diagram can only go on a new board or on one this work created. I can only add notes on top of an existing file I didn't make.
- **The Loomlist Engineering plan isn't on your account.** Your account has three plans: your personal Starter plan, <figma-plan-1> and <figma-plan-2>
- **So I'll use your fallback.** The board goes in a new FigJam file in the <figma-plan-1> plan, left in drafts with no project. If that's wrong, tell me now. I'll confirm it again before writing anything.

**Round one: reader, question, outcome**

1. **Reader**
   - What I see: the request says "Loomlist Engineering," so the readers are engineers.
   - Question: who opens this board, and when?
   - My suggestion: Loomlist engineers new to block sync, during onboarding or a design review.
   - Why: that decides how much each box needs to explain.

2. **What the board answers**
   - What I see: the request lists the parts but not what the diagram should make clear.
   - Question: what is the one question the diagram must answer?
   - My suggestion: "Which services does a block edit pass through to reach the other clients, and how does iOS get notified?"
   - Why: one request path keeps the board readable and tells me which connections to draw.

3. **Outcome**
   - What I see: nothing in the request says this yet.
   - Question: what should the reader be able to do after reading it?
   - My suggestion: name which service owns each step and know where to look when an edit fails to sync.
   - Why: that tells me which connections need labels.

If you skip a question, I'll go with my suggestion and list it as assumed in the summary I send before asking to write.