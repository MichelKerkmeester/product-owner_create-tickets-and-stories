<figma-url>
Read-back: 7 of 7 states, 12 of 12 transitions, 6 of 6 transitions labelled (labels read off the screenshot), first glance: the end state a booking reaches
Left out: how long after check-in a no-show is marked, because no source states it
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

The board section "Booking status lifecycle" is on your retro board. It sits 400 pixels right of the existing content, so nothing there moved. I wrote it with one `use_figma` call and read it back with `get_figjam`. The write returned no warnings.

- **Edge cases:** Pending to Cancelled is drawn through two connector legs, which I counted as one transition.
- **Finding, not fixed:** The "guest cancels" line from Pending crosses the "missed check-in" connector, just left of No-show. It also runs along the same vertical trunk that leaves Confirmed. Both are readable, but they are not clean.
- **Fix, if you want it:** I'd reorder the end states in the model, put Cancelled above No-show, and compose again. That needs your yes. The old section would only be deleted after a second, separate yes from you.