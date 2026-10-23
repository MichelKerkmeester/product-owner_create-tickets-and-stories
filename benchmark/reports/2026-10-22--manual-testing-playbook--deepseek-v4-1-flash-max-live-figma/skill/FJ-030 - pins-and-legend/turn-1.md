I read this as a user flow, which is the type that answers "which screens does a person pass through, and where do they choose". The model passes the pre-write check before anything touches a board:

```text
diagram 1, user flow: ok, 9 nodes and 9 connectors, widest rank 2 steps,
longest path 7 steps, 1.0 connectors per step, labels average 17 characters, 0 crossing pairs
PASSED 1 diagram(s)
```

**What the board answers:** which screens a Fernhouse customer passes through to start a return in the app, and where they give up. The return team can then pick which drop-off point to fix first.

**Settled from your request**
* Entry: order list, tap an order row
* Order detail: Start a return
* Return window: 30 days after delivery, and No is the one exit that leaves the app, to Contact support
* Reason list, then a choice of drop-off point or courier pickup
* Exit: confirmation with a QR code
* Actors: the customer, and the app checking the window

**Assumed**
* Reader: the Fernhouse team that owns the return flow, with support. Nothing names the audience, so say if it is someone else
* Screens and rules come from your description rather than attached files. A read against the real screens could change a label

**Outline:** order list, order detail, within 30 days, contact support, pick a reason, drop-off or pickup, drop-off point, courier pickup, return confirmed with QR. Nine nodes, nine connectors, top to bottom. I kept the happy path with its exits beside it over a state map, because the request is about the screens a customer sees.

**Reading order:** the three numbered notes first, then the 30-day cut-off with its exit to support, then the confirmation. No accent colour, because the three drop-off points tie and colour on one would rank them.

**Pins**
1. Within 30 days: no warning before day 30
2. Pick a reason: too many reasons to choose from
3. Drop-off or pickup: the pickup fee is unclear. Free pickup over €100 is a proposal under review

Free pickup is not drawn as a step. It holds its proposal status in note 3 and nowhere else.

**One thing blocks the gate.** I checked the account before naming a plan, and there is no plan called Fernhouse Product. It holds three: <figma-plan-1> (pro, full seat), <figma-plan-2> (pro, member seat) and <figma-plan-3> (starter, view seat, six tool calls a month). A board in the wrong plan is visible to that plan as soon as it lands, so I am not guessing.

Reading: this is Fernhouse work and the named plan does not exist here. Recommended: **<figma-plan-1>**, the team plan where you hold a full seat, so the board can be written and shared without the starter limit. If Fernhouse Product should be its own plan, create it and give me the exact name.

**Gate, once the plan is set**
* File: a new FigJam file, created by the first write, titled Start a return
* Writes: one user flow, 9 nodes, 9 connectors, 4 labelled decision exits
* Extensions: 3 numbered pins, 3 note stickies in a column right of the diagram, 3 key stickies for the three shapes
* Calls: one `get_figjam` read-back, one `use_figma` for the pins and stickies, one tag pass so a later session can find what this write created
* Rollback: delete the new file, or the ids the extension returns

Tell me which plan, and say write.