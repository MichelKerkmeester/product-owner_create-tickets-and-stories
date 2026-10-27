# Reader notes: FJ-032 page (reader b)

The page holds two sections side by side. The right section is the diagram, a state diagram titled "Booking status". The left section is a retro board: six grey sticky notes in a two by three grid with no title of its own.

## Reading order (overview)

1. The large title "Booking status" at the top of the right section (start of the frame: title block).
2. The subtitle under it, naming Roamstay bookings and the team reading the retro board.
3. The pale blue "Confirmed" group box across the top of the diagram.
4. The white "Upcoming" state inside Confirmed.
5. The white "In stay" state inside Confirmed.
6. The filled blue "Pending" state on the left below Confirmed.
7. The three grey final states on the right: "Completed", "No-show" and "Cancelled".
8. The black start dots on the left (one inside Confirmed and one before Pending) and the ringed end dots on the far right.
9. The connector labels: "check in", "card authorised", "check out [from In stay]", "missed check-in [from Upcoming]" and the two "guest cancels" lines.
10. The "Key" box along the bottom of the right section (frame: key).
11. The small source line under the key.
12. Last, the six grey sticky notes on the left section: "Standups ran long", "Design review was useful", "Too many hotfixes", "Pairing helped onboarding", "Release notes were late" and "Try a demo every Friday".

Frame position: the title block comes first and the key comes near the end, after the states and lines. There are no lanes or zones. The only grouping inside the diagram is the Confirmed box. The retro section is a separate frame to the left.

## Three questions

Q1: Which states end a booking?
Completed, No-show and Cancelled. Each is grey (the key's "Final state") and each leads to a ringed End dot on the far right. Sure, high. Found on the right edge of the diagram and in the key.

Q2: What moves a booking from Pending to Confirmed?
"card authorised". The line leaves the top of Pending, runs left and up and enters the left edge of the Confirmed box. Sure, high. Found just above Pending on the left.

Q3: Is the retro content still readable?
Yes. All six sticky notes on the left are intact and their one line headings are legible at 100%. The notes hold only that one line each, so there is nothing more to read on them. Sure, high. Found in the left section of the page.

## 1 Title and the question this board answers

The title is "Booking status". It answers: which statuses does a Roamstay booking pass through and what moves it from one to the next.

## 2 Main path or structure from start to end

A booking starts at the black start dot on the left and enters Pending (blue, the first state). When the card is authorised it moves into the Confirmed group. Inside Confirmed it starts at an inner start dot and goes to Upcoming, then on "check in" to In stay, then a line runs right to an inner end dot at the right of the Confirmed box. From In stay, "check out [from In stay]" leaves the top of Confirmed and goes to Completed, which then leads to an End dot. The happy path is Pending, Upcoming, In stay, Completed.

## 3 Every decision or branch and where each exit goes

There are no decision diamonds. Branches come out of states and the group:
- Pending: "card authorised" goes to Confirmed. "guest cancels" goes to Cancelled.
- Upcoming: "check in" goes to In stay. "missed check-in [from Upcoming]" leaves the right side of the Confirmed box and goes to No-show.
- In stay: "check out [from In stay]" goes to Completed. A plain unlabelled line also goes to the inner end dot of Confirmed.
- Confirmed as a whole: "guest cancels" leaves the bottom of the box and goes to Cancelled.
- Completed, No-show and Cancelled each go to their own End dot.

## 4 What the key says

The key lists: black dot is Start, blue filled rounded box is First state, white rounded box is State, grey rounded box is Final state, black dot with a grey ring is End and a thin arrow is Leads to. Not every mark is in the key. The pale blue Confirmed group box is not explained. The grey text labels on the lines and the bracketed "[from ...]" notes are not explained either, though they read naturally as triggers and sources. The left retro section is outside the key, which is fine because it is not part of the diagram.

## 5 Anything unreadable, unclear or ambiguous

- The inner end dot inside Confirmed (right end of the In stay line) is confusing. It suggests Confirmed finishes there, but the real exits to Completed and No-show leave from the box edge with "[from ...]" notes instead of from the states themselves. I had to rely on the bracket text to know which state each exit belongs to.
- "check out [from In stay]" starts from the top edge of Confirmed roughly above In stay, then loops round the far right to Completed. It is long and crosses near the "missed check-in" line on the right edge, so the two are easy to mix up.
- "guest cancels" from Confirmed leaves the bottom edge below In stay, so it is unclear whether a guest can cancel from both Upcoming and In stay or only from one. I read it as from anywhere in Confirmed.
- The line from Completed to its End dot goes down, right and back up, which looks odd next to the straight lines for No-show and Cancelled.
- The source line notes that declined or expired cards, refunds and booking edits are left out, so a Pending booking that never gets authorised has no exit other than guest cancels.

## 6 Could I act on this board without asking anyone

Mostly yes: the states, final states and triggers are clear, but I would ask whether guests can cancel during In stay and what the inner end dot inside Confirmed means before building on it.
