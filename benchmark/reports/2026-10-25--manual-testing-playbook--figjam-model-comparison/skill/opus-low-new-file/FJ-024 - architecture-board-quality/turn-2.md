The model is ready and passes the pre-write check. Before I can ask you to approve the write, I need you to pick the plan: your Figma account has no plan called **Loomlist Engineering**. It holds these three:

- **<figma-plan-3>**: Starter tier, View seat. That seat is limited to six Figma tool calls a month, so this board would use most of them
- **<figma-plan-1>**: Pro tier, Full seat, you're an admin
- **<figma-plan-2>**: Pro tier, Full seat, you're a member

Loomlist Engineering may be a team inside one of these, or a plan this account doesn't belong to. A board in the wrong plan is visible to that plan's members as soon as it lands, so I won't guess.

Finding: To stay within the nine-node limit, Desktop and web share one client node. iOS stays separate because it's the device that push wakes.

Finding: The two-way live socket shows changes going back out to clients. The board doesn't show how the gateway receives changes for that fan-out, because nothing in your description says so. The check also doesn't allow a link from the change stream to the gateway.

Finding: The push worker's link points to Apple's push service and is labelled "Wakes iOS devices". The check doesn't allow a direct link from Apple's push service to the iOS client.

**Which plan should the new board go in: <figma-plan-1>, <figma-plan-2>, or another plan Loomlist Engineering belongs to?**