<figma-url>
Read-back: 7 of 7 states, 12 of 12 transitions, 6 of 6 transitions labelled (labels read visually from the composing screenshot, because `get_figjam` returns no connector text), first glance: Cancelled
Left out: what happens to a Pending booking whose card is never authorised, because the request is silent
Finding: the "missed check-in [from Upcoming]" label sits 8 px above Completed. At a glance it can read as Completed's move. A fix is to declare No-show before Completed in the model and compose again, which needs your yes and then a second yes to delete this section.
Finding: Cancel is drawn from the whole Confirmed section, as written, so it reads as open from In stay as well as Upcoming. If a guest cannot cancel mid-stay, I would guard it as "from Upcoming" and compose again.
Finding: Completed, Cancelled and No-show are all light gray and keyed as Final state, and Cancelled also has the pink outline. The composer cannot give each end state its own colour, so a red for Cancelled and No-show would be a hand edit in FigJam.
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.