# FJ-012 turn 3 transcript

**User:** Use your recommended answers.

**Assistant:**

Round two is settled. This is round three, the last one. Nothing has been written to Figma.

**Settled so far**
- **Reader, question and outcome:** as you accepted in round one
- **Start and end:** the board starts with a block edit on any client. It ends when the edit is saved in the blocks database and has reached the other clients, with iOS notified through APNs
- **Connections:** the seven you accepted. They came from my suggestion, which you confirmed, so they aren't based on a document
- **Split:** two diagrams in one file
  - **1. Block edit sync:** 8 parts and 6 connections
  - **2. iOS push:** 6 parts and 5 connections
- **Branches and states:** none. An architecture diagram shows parts and connections, so it has no decision points
- **Target:** a new FigJam file in <figma-plan-1>, left in drafts with no project

**Round three: sources and status**

1. **Today's system or a proposal?**
   - What I see: your message describes the parts as they are, but nothing confirms that's how it runs today.
   - Question: is this how Loomlist block sync runs now, or a planned design?
   - My suggestion: describe it as the current system, based on your message and not checked against code. That note goes in each diagram's source line.
   - Why: a reader can tell at a glance how far to trust the board.

2. **Anything to check the names against?**
   - What I see: the only source is your message.
   - Question: is there an engineering doc, a service list or a repo I should check the names and connections against?
   - My suggestion: no. Draw from your list and keep the names exactly as you wrote them.
   - Why: it saves a round, and the source line makes the limit clear.

3. **What the eye lands on first**
   - What I see: every path in the question goes through sync-service.
   - Question: which part should each diagram highlight?
   - My suggestion: sync-service in **1. Block edit sync** and the push worker in **2. iOS push**.
   - Why: each one owns most of the steps in its path, so it's the first place to look when an edit fails to sync.

After this round I'll send one full summary for you to confirm. Then I'll ask, separately, whether to write the board.
