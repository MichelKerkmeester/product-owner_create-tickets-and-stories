Before I draw anything, this is how I read the request. Nothing is written yet.

Reader: leadership, for an update
Question: how does Loomlist block sync work?
Outcome (assumed): leadership can see that every change goes through the sync platform, is stored there and wakes a sleeping iPhone through Apple's push service
Type: architecture, since your sentence describes parts and how they connect
Destination: I read "new board" as a new board section inside the existing file you named, not a new file. Anything already in that file stays as it is
Settled by the sources: your request is the only source. It names the desktop, web and iOS apps, the sync platform, the store of every change and Apple's push service. No engineering doc was supplied, so I add nothing beyond them except the Entry point below

The board answers this sentence: "Show leadership how a block change from the desktop, web or iOS app reaches the sync platform, is stored and wakes a sleeping iPhone through Apple's push service."

Outline, 7 nodes and 6 edges
* Apps: Desktop app, Web app, iOS app
* Entry point (assumed)
* Sync platform
* Change store
* Apple's push service
* Each app to Entry point, labelled "Syncs blocks"
* Entry point to Sync platform, "Passes changes on"
* Sync platform to Change store, "Stores every change"
* Sync platform to Apple's push service, dashed, "Wakes sleeping iPhones"

Two framings
* Architecture (recommended): the map of parts you described, with the wake-up as one dashed edge. The cost is that an architecture has no arrow from an outside service back to an app, so the hop from Apple's push service to the iPhone sits in the edge label and not on its own arrow
* Sequence: one change walked step by step to the sleeping iPhone, which draws that last hop. The cost is that it answers "in what order" instead of "what parts", and the stored changes shrink to one message

Look, all proposals
* Marked node: Sync platform, where every change is stored and the wake-up starts
* Detail and audience: Simplified and Executive, taken from "leadership", so plain verbs and no protocols or internal services
* Distance: Laptop. Tell me if it is shown on a call
* Zones: the architecture's own lanes, named Apps, Entry, Platform, Storage and Outside
* Title "Block sync", with a one-sentence subtitle for the leadership update and a source line naming your request

What the board must not do: show internals leadership does not need, such as queues, workers, protocols or database names, or imply a tick-by-tick order. I recommend this because the reader is leadership

Assumed
* Outcome, settled by your confirming or correcting the sentence above
* Entry point: an architecture needs one gateway between the apps and the platform, so I add a node named in capability words and mark it assumed on the source line. A sync doc or the real component name settles it

Left out
* The hop from Apple's push service to the iPhone as its own arrow, because an architecture has no edge for it
* How the other apps receive a change, because your sentence gives no return path, so every arrow points away from the apps

Still open: nothing that blocks drawing.

Is this the right reading of the board, including the must-not line and the Entry point?