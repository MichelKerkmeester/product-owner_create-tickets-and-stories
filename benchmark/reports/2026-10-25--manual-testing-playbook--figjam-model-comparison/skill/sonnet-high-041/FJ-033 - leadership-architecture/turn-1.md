Before I draw anything, this is how I read the request.

Reader: leadership, for the leadership update
Question: how does a Loomlist block change get from one app to the others, including an iPhone that is asleep?
Outcome: leadership can see that every change passes through the sync platform and is stored, and that Apple's push service is what wakes a sleeping iPhone
Type: architecture, because the question is about which parts connect. A sequence would answer the order of one sync, which you did not ask for

Settled by your request, seven parts and six connections:
* Apps: Desktop app, Web app, iOS app
* Sync platform
* Change store, where every change is kept
* Apple push service
* Each app to the sync platform, the sync platform to the change store, and the sync platform to Apple push service, labelled as the call that wakes sleeping iPhones

Source class: your description only, with no doc supplied. I treat it as current behavior as you stated it and say so on the board's source line. Send the sync doc if you want it cross-checked.

Assumed:
* Entry point: the architecture layout needs one gateway node between the apps and the platform, and you named none. I add a node called Entry point and mark it as added on the source line
* Arrows run from the apps toward the platform, labelled Syncs blocks, because you did not say whether the apps hold a live two-way channel. If they do, tell me and those arrows go two-way
* Executive audience with simplified detail, so no internals appear beyond the parts above. Reading distance is a meeting screen, so labels stay under 32 characters

Must not do (recommended): show any part you did not name, such as a queue, a worker or file storage, or suggest the apps talk to Apple directly. Tell me if the board should do something else.

Look:
* First glance: Sync platform, accented
* Second glance: Change store
* Last glance: Apple push service
* Title: How Loomlist block sync works
* Subtitle: How desktop, web and iOS apps share block changes through the sync platform, which wakes sleeping iPhones through Apple's push service

Finding: the architecture layout has no connector from an outside service back to an app. The step where Apple's push service reaches the iPhone therefore cannot be an arrow, and the wake-up is carried by the label on the arrow from the sync platform to Apple push service. I recommend keeping it that way. A sequence board could draw that step as a message later.

Left out: the order of one sync and the Apple-to-iPhone step as its own arrow, both for the reason in the finding above

Is this the right reading of the board?