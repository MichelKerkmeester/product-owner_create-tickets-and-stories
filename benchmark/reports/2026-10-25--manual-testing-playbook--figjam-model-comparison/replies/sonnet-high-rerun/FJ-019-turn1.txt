Before I draw anything, this is how I read the request. Nothing has been created yet.

**Type:** architecture. You listed deployable parts and asked how they connect, so the board answers "which parts make up block sync and how do they connect?". A sequence would answer the order of one sync instead. I'd draw that only if you ask.

**Settled by your request:** ten parts, which fit the board's six lanes like this:
* Clients: desktop, web and iOS
* Edge: API gateway
* Services: sync-service and push worker
* Stores: blocks database and file storage
* Events: change stream
* External: Apple's push service

**Not settled:** no source says which part calls which. I won't invent connections on a shared board, so I need them before modelling.

**Plan:** the connected Figma account holds three plans: <figma-plan-3> (Starter, view seat), <figma-plan-1> and <figma-plan-2> There is no Loomlist Engineering plan, so I can't create the board there. I read your fallback as <figma-plan-1> (the only Barter plan), as a new file in drafts with no project. The write gate will name the plan again before anything is created. If Loomlist Engineering lives under another Figma login, tell me and I'll stop.

**1. Reader, question and outcome**
* Reading: no reader is named. The board maps the sync path for people who need to see what a block change passes through.
* Question: who reads it, and what should they be able to decide or do afterwards?
* Recommended: Loomlist engineers and the product owner, who can name every part a block change touches and see which parts are outside the system.
* Why: that is all the part list supports, and it works for both audiences.

**2. What the board must not do**
* Reading: ten parts and no stated purpose beyond "the services behind block sync".
* Question: what should the board refuse to show?
* Recommended: no call order, payloads or deployment detail (regions, replicas), and no connection you haven't confirmed.
* Why: order belongs on a sequence diagram, and a guessed connection reads as fact once it is on the board.

**3. The connections and the budget**
* Reading: an architecture board holds at most 9 nodes and 12 connectors. Ten parts is one over, so one part has to go or the board splits.
* Question: which parts call which, and does anything touch file storage?
* Recommended (every edge stays marked assumed until you confirm it):
  * the three clients call the API gateway
  * the gateway routes to sync-service
  * sync-service writes the blocks database and publishes to the change stream
  * the push worker consumes the change stream and calls Apple's push service
  * file storage comes off this board as off the sync path, listed under `Left out:`, with a second board for file handling offered
* Why: that is the usual shape for this set of parts and it keeps one board on one question. If file storage is on the sync path, say what calls it. Then I'll split into two boards, or you pick what to cut.
* Add the transport per client (WebSocket, HTTPS) if you know it. I'll leave it off otherwise.

Reply "use your recommendations" to accept all three. Otherwise correct what's wrong and I'll run the playback again over those rows before the gate.