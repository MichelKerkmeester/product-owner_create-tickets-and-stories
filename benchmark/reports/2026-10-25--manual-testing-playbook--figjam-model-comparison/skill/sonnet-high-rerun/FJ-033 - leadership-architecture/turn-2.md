Here is how I read the board, before any model or write.

**Question the board answers:** how does a block change get from one Loomlist app to the others, including a sleeping iPhone?

**Outcome:** leadership can see that all three apps share one sync platform, that it stores every change and that it wakes sleeping iPhones through Apple's push service. No decision is asked of them.

**What settled each row**
- Reader and question: your request
- Parts and calls: your description, which names the three apps, the sync platform, the stored changes and Apple's push service
- Target: the existing file `<test-file-key>`, as a new section, with nothing already on it changed

**Assumed**
- Source class: your message is the only source, so I treat the path as current behavior. A doc or a "this is a proposal" from you would change that.
- Two part names: the layout needs an entry point between the apps and the platform, and a store for the changes. I name them "Entry point" and "Change store" by what they do, and the source line says so.
- Must not show: message order, queues, workers, replicas and any speed or reliability claim.

**Outline, in drawing order**
1. Desktop App, Web App and iOS App sit in the Clients lane
2. Entry point sits in the Edge lane, as the assumed gateway
3. Sync Platform sits in the Services lane
4. Change Store sits in the Stores lane
5. Apple Push sits in the External lane
6. Each app sends block changes to the Entry point, three connectors
7. The Entry point routes changes to the Sync Platform
8. The Sync Platform stores every change in the Change Store
9. The Sync Platform calls Apple Push to wake sleeping iPhones, a dashed connector

That is 7 nodes and 6 connectors in 5 lanes, inside the budget of 9 and 12. The events lane stays out because no queue is named.

**Two framings**
- Parts and connections, the architecture you asked for. It shows the whole system at a glance but not the order of a sync. I recommend this one.
- Order of one sync, as a sequence. It would show the wake-up step by step, but it answers a different question than the one leadership brought.

**The look**
- First glance: Sync Platform, where every change is stored and the wake-up starts. Second glance: Apple Push. Last glance: the three apps.
- Detail and audience: balanced, written for leadership, so labels name capabilities and no protocols or status codes appear.
- Reading distance: meeting screen, labels cut to 32 characters, since leadership updates are usually shown on a call. Laptop is the alternative.
- Zones: the five lanes are the zones, with no extra grouping.
- Title: "Block sync". Subtitle: "How a block change reaches every Loomlist app, including a sleeping iPhone". The source line names your description and the two assumed names.

**Left out**
- How an awake app receives changes back. Your description doesn't say, and the layout can't draw a connector from an outside system to an app, so the wake-up reaches the iPhone only through the label on the Apple Push connector.

Is this the right reading of the board?