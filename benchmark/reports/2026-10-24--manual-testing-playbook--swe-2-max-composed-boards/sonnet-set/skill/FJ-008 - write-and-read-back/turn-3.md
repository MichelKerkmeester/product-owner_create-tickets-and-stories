<figma-url>
Read-back: 6 of 6 entities, 6 of 6 relationships, 12 of 12 attributes, first glance: Booking. The new board sits 400 px to the right of the first one in the same file, "Stays model". No connector crosses another connector or any entity.
Finding: I wrote the Guest link from the Booking side to remove the crossing. It now reads "is made by (0..n to 1)", where before it said "makes (1 to 0..n)". The fact is the same, but the wording is passive. I read the six cardinality labels from the screenshot, because the read tool returns no connector text. Their two ends were checked from the connector ids.
Finding: the Guest line starts on the same point of Booking as the "holds" line, then turns down. It forks from that line and reads as a branch. Fixing that would mean recomposing again, which is my second and last attempt at this board, and I'd rather you decide on it.
Left out: every non-key column, because you asked for keys only.
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

Two decisions for you:
* Should I delete the first board (section `1:3`) with the Guest line that crosses the others? I haven't touched it. If you say yes, I delete only that section.
* Do you want a Booking-to-Room junction, given the 8-rooms-per-booking note in `context/roamstay-context.md`?