<figma-url>
Read-back: 7 of 7 states, 12 of 12 transitions, 6 of 6 transitions labelled (labels read visually), first glance: Cancelled
Left out: card decline, Pending expiry, and refund and payment states, because your message states none of them
Finding: the six transition labels were checked on the composing call's screenshot, because `get_figjam` returns connector names and end points but not label text. The 12 connectors match the model on both end points and arrow direction.
Finding: "missed check-in [from Upcoming]" runs along the top of the Completed box in the lower right, and the Completed to End connector loops under that box and up into the end dot. The write returned no warnings and both read cleanly. If you want either tidier, the fix is a model change composed again, which needs your yes, and the old section then goes only on a second yes that names it.
Finding: the cancel arrow from Confirmed leaves the whole section, so it reads as open during In stay too, as you wrote it. If a guest can't cancel once in stay, say so and it gets a `[from Upcoming]` guard.
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.