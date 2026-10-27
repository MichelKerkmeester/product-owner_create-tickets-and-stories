<figma-url>
Read-back: 7 of 7 states, 12 of 12 transitions, 6 of 6 transitions labelled, first glance: Cancelled
Extensions: 2 of 2 notes, 0 overlaps
Left out: card authorisation failing, because the request gives no move out of Pending for it. Anyone but the guest cancelling, because the request names only the guest.
Finding: the Cancelled note stands right of the cancel connector's corner, not beside the Cancelled state. A sticky is a fixed 240 pixel square and can't be resized, and the 176 pixel band between that connector and the key can't hold one. Both notes start with the state name so each reads as its own, so the wording differs slightly from the gate: "Cancelled: set by the guest, while the booking is Pending or Confirmed" and "No-show: set by the hotel, after a missed check-in".
Finding: `get_figjam` returns no connector or sticky text, so I read the 6 transition labels and both note texts on the screenshot. The label-wrap check also couldn't run on this machine, so I read the labels by eye and none has a word alone on its last line.
Finding: the subtitle has a serial comma, "passes through, what moves it on, and who sets". The fix is to drop the comma before "and", compose the board again and delete this board section on its own yes. Want that?
Finding: can anyone other than the guest set Cancelled, such as the hotel or the system? The note says "guest" only until you confirm.
HVR self-scan: 1 hard blockers. Fixed: none. Kept with reason: the serial comma in the subtitle, left on the board because removing it means composing the board again.