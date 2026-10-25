Nothing is written to the board. The pre-write check rejects the model as it stands, and I need one more answer.

Failed check: the model draws Desktop, Web and iOS calling the Sync Platform directly. The architecture type only allows apps to reach a service through a gateway, with this message:

```text
edge desktop to sync runs client to service as a forward edge, which is not in the allowed-edge table: a service mediates
```

Your request and `context/loomlist-context.md` name no gateway, so adding one would mean inventing a part for leadership to read as fact.

**Question:** is there an entry point between the apps and the sync platform, such as an API gateway or a socket endpoint?

- **If yes:** give me the name, and I'll draw it as the one gateway node.
- **If no:** I'd switch to a sequence diagram. That's my recommendation, because it shows the same story with no gateway rule: an app sends a change, the platform stores it, and Apple's push service wakes the iPhone.
- **Why:** both options leave the board with no invented parts. The sequence costs you the "architecture" label you asked for, so it is your call.

Your yes also settled the other two points, so I'm proceeding on them and will name them as assumed at the gate:
- **Push sender:** the sync platform sends the wake itself. Your description governs, and the context page's "push only for mentions, replies and shares" line is treated as out of date on this point.
- **Store label:** "Change Store".

Once you answer, the next message is the write gate. It names the file, what will be written, the calls it will spend and the rollback, and it asks for your yes. I still won't write before that yes.