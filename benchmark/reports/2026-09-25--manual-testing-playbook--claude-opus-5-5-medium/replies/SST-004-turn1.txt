I've saved the order tracking Story and its six tasks as one folder. Hamid's brief already names the task split and Yusuf's notes don't contradict it, so I wrote it without asking you anything first.

Path: `export/001 - Story-order-tracking/001 - Story-order-tracking.md`
Verified: read-back succeeded; 205 lines

Path: `export/001 - Story-order-tracking/001.1 - task-tracking-webhook.md`
Verified: read-back succeeded; 86 lines

Path: `export/001 - Story-order-tracking/001.2 - task-packed-status.md`
Verified: read-back succeeded; 36 lines

Path: `export/001 - Story-order-tracking/001.3 - task-web-tracking-timeline.md`
Verified: read-back succeeded; 75 lines

Path: `export/001 - Story-order-tracking/001.4 - task-ios-tracking-timeline.md`
Verified: read-back succeeded; 74 lines

Path: `export/001 - Story-order-tracking/001.5 - task-android-tracking-timeline.md`
Verified: read-back succeeded; 74 lines

Path: `export/001 - Story-order-tracking/001.6 - task-tracking-timeline-events.md`
Verified: read-back succeeded; 39 lines

HVR self-scan: 1 hard blocker. Fixed: "offers" (a copula, changed to "has") in a Story rabbit hole. Kept with reason: `TBD...` in Estimation (a fixed Story Mode placeholder), "etc." in the ClickUp story preamble (fixed house text copied word for word), `Order page / Tracking timeline` (the design frame's own name).

**What's in it**
- **Story:** seven acceptance criteria. Every value from both sources is in Requirements, grouped the way the brief and Yusuf's notes group them: status mapping, estimate strings, `90 days`, `30 kg` / `120 cm`, the pallet line, six locales, the signature, the `5 seconds` timeout, the retry schedule, and the ~`43,000` peak events.
- **Open questions:** the brief's two open questions (whether `Delivery failed` gives a reason, and the missing web layout) are marked Open. That is why the Story ends with a Delivery section.
- **Tasks:** they follow Hamid's split and the `{Discipline} - {Surface} - TRACK - {Title}` naming in the company context.
- **Web task:** it states that it waits for the web design.

**Things I added that neither source says (delete any you don't want)**
- The reason in Solution for not guessing an estimate: a wrong guessed day sends the customer back to CS.
- Three rabbit holes:
  - A `DL` for a parcel point shows `Delivered` before the customer has collected it.
  - The brief doesn't say whether each `IT` hub scan is its own timeline step.
  - After a failed attempt, the delivery window from that attempt may still be on screen.
- The webhook task stores `exception_code` and `delivered_to`, so the open question about failure reasons can be answered later.
- The brief only mentions the carrier link in the DATA task. The Story treats it as an event to track and doesn't say where the link sits on the page.

**Left out on purpose:** Yusuf's example JSON body, and his notes that `PU` comes once at the 18:00 collection and `IT` 2 to 4 times per parcel. None of them changes what gets built.

Next step: Hamid decides whether `Delivery failed` gives a reason, and Design delivers the web layout. Those two answers would let me remove both Open lines and trim the Delivery section.