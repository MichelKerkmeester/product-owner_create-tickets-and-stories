`Loomlist Engineering` is not one of the three Figma plans this account returns:

*   <figma-plan-1>, Pro, Full seat
*   <figma-plan-2>, Pro, Full seat
*   <figma-plan-3>, Starter, View seat

A new board takes a plan key, and a board in the wrong plan is visible to that plan's members as soon as it lands. Nothing has been written.

Reading: this is an architecture. The model holds nine nodes, eight connectors and six lanes. Desktop, web and iOS each hold a live socket to the API Gateway. The gateway routes to Sync Service, which writes Blocks DB and publishes to Change Stream. The Push Worker consumes the stream and calls Apple Push to wake iOS. File storage has no stated connection to sync, so it stays off the board and would be named under Left out.

Question: which plan should own the new board, and is Loomlist Engineering a project inside it? Recommended: <figma-plan-1>, the Pro plan where this account holds a Full seat. If Loomlist Engineering is a project folder, send its name or URL and the file goes there. Once the plan is settled I will show the write gate before anything lands.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.