I've written the board and cleaned up, and I'm sending the delivery reply now.

<figma-url>
Read-back: 7 of 7 states, 12 of 12 transitions, 6 of 6 transitions labelled (labels read visually), first glance: Confirmed
Left out: a declined or unauthorised card on a Pending booking, because no source states it
Finding: `get_figjam` returns no connector label text, so I checked the 6 transition labels on the overview screenshot from the composing call. It showed none cut off or touching, and no connector crossing another.
Finding: "check in" as the Upcoming to In stay move is assumed, because your message names no trigger for it.
Finding: Cancelled as a status of its own is assumed, because your message names the move and not the state.
Finding: "guest cancels" leaves Confirmed as a whole, so the board also allows cancelling while In stay. I drew it at the Confirmed level, as you gave the rule, so tell me if In stay should not allow it.
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.