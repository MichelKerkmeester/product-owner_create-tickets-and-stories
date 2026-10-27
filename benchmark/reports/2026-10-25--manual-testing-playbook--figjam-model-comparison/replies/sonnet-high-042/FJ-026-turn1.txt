Before I draw anything, this is how I read the request.

**Question:** which statuses can a Roamstay booking be in, and what moves it between them?
**Outcome:** support can read every booking status and spot the three a booking ends in.
**Type:** a state diagram. The words "plan" and "Product plan" in your message don't make this a schedule, because you're asking about statuses and what moves a booking between them.
**Source:** your message is the only source. I read its statuses as current behavior, which is assumed. A link to the doc that states them would settle it.
**Destination:** a new section in the FigJam file you named. Nothing already on the file changes, and no new file is created.

**Outline**
* States: Pending, Confirmed (a section holding Upcoming and In stay), Completed, Cancelled and No-show
* Pending to Confirmed: card authorised
* Confirmed opens on Upcoming
* Upcoming to In stay: check in
* Confirmed to Completed: check out, guarded `[from In stay]`
* Pending to Cancelled and Confirmed to Cancelled: guest cancels
* Confirmed to No-show: missed check-in, guarded `[from Upcoming]`

I read two parts of that from your wording rather than from a stated line. Confirmed opens on Upcoming because check-in moves Upcoming to In stay. Check-out leaves from In stay because it ends the stay.

**Colour:** Completed, Cancelled and No-show are the states the booking ends in. The composer draws every such state light gray with a heavier outline, and the key names them "Final state". Upcoming and In stay stay white, because leaving Confirmed is what ends a booking, not reaching them. A state diagram can't take a custom colour per end state, so red for Cancelled would be a hand edit in FigJam. Recommended: the light gray as drawn, because it needs no extension and the key explains it.

**Two framings**
1. A full status map with every exit, so each way a booking ends and the status it leaves from are both visible. Recommended, because spotting end states is the point.
2. Only the path to Completed, with the other two ends left for a second board. It reads shorter but hides two of the three ends.

**What the board must not do:** show anything your message doesn't state. That means no card-decline path, no Pending expiry and no refund or payment states, all of which will appear under `Left out:`. Recommended: keep them out.

**Look**
* One accent: on Cancelled, with the key reading "In focus: two statuses lead here". Cancelled is the end with two ways in. Without an accent, Pending reads first. Recommended: Cancelled.
* Title "Booking status", with the subtitle "Every status a Roamstay booking passes through, and what moves it on"
* Your words as labels: "In stay" and "No-show", not `InStay` and `NoShow`
* Balanced detail, mixed audience and the Laptop reading distance, all assumed

**Still open:** cancelling is drawn from the whole Confirmed section, so it reads as open during In stay too. That is what "while Pending or Confirmed" says. If a guest can't cancel once in stay, the move gets a `[from Upcoming]` guard. Recommended: draw it as you wrote it.

Is this the right reading of the board?