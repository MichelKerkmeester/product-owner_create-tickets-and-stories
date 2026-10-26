### Round 2 — connections

**Reading:** The clients hold live sockets to the API gateway, and sync-service handles block changes.

**Question:** Should the API gateway route that socket traffic to sync-service?

**Recommended:** Yes, label the connection “Routes block sync.”

**Why:** The architecture needs a link from the gateway to the service handling block changes.

**Reading:** The push worker reads the change stream and wakes sleeping iOS devices. Apple Push Service is listed as a component.

**Question:** Should the push worker send wake notifications through Apple Push Service?

**Recommended:** Yes, show that connection and label it “Apple Push Service: Wakes iOS.”

**Why:** This connects the stated worker and wake outcome through the named push service.