# Fresh reader notes: FJ-032 page (reader b)

The page holds two sections side by side. The right section is the diagram: a state diagram titled "Booking status". The left section is a separate retro board of six grey sticky notes ("Standups ran long", "Design review was useful", "Too many hotfixes", "Pairing helped onboarding", "Release notes were late", "Try a demo every Friday"). The retro has no title and no link to the diagram. The two sections are separated by a wide black gap.

## Reading order (overview)

1. The retro section at top left, because it sits in the corner where the eye starts (the frame of that section first, then its six stickies left to right, top row then bottom row)
2. The title "Booking status" at the top of the right section (the diagram frame starts here)
3. The subtitle "Every status a Roamstay booking passes through, and what moves it on"
4. The black start dot at the far left of the diagram
5. The blue state "Pending"
6. The line label "card authorised" running over the top
7. The pale blue group "Confirmed" (a frame inside the diagram)
8. Inside Confirmed: its own start dot, then "Upcoming", the label "check in", "In stay" and an end dot
9. The label "missed check-in [from Upcoming]" leading down to the grey state "No-show"
10. The label "check out [from In stay]" on the left vertical line leading to the grey state "Completed"
11. The grey state "Cancelled" with two incoming "guest cancels" lines, one from Pending at the bottom left and one from the right edge of Confirmed
12. The three end dots to the right of No-show, Completed and Cancelled
13. The Key box at the bottom of the diagram frame
14. The source note under the key: "Source: the booking lifecycle as described by the product owner. Left out: declined-card and expiry paths."

## The three questions

Q1: Which states end a booking?
No-show, Completed and Cancelled. Each is a grey "Final state" with an arrow to an end dot. Very sure. Found in the lower middle of the diagram and confirmed by the key (grey fill means Final state).

Q2: What moves a booking from Pending to Confirmed?
"card authorised". The line leaves Pending, runs over the top and drops into the Confirmed group. Very sure. Found on the top line between Pending and the Confirmed group.

Q3: Is the retro content still readable?
Yes. All six sticky texts can be read in the overview, though the text is small and the stickies are otherwise blank. Fairly sure. Found in the separate section at the top left of the page. The 100% image I was given shows only the diagram, so I read the retro at overview size only.

## 1 Title and the question this board answers

The title is "Booking status". The board answers which statuses a Roamstay booking goes through from creation to its end, and which event moves it from one status to the next.

## 2 Main path from start to end

A start dot leads to Pending (blue, the first state). "card authorised" moves it into the Confirmed group. Inside Confirmed a start dot leads to Upcoming, then "check in" leads to In stay. "check out [from In stay]" leaves the Confirmed group on its left side and leads to Completed, which leads to an end dot. That is the happy path: Pending to Upcoming to In stay to Completed.

## 3 Every decision or branch and where each exit goes

- From Pending: "card authorised" goes to Confirmed (into Upcoming). "guest cancels" goes down and along the bottom to Cancelled.
- From Upcoming: "check in" goes to In stay. "missed check-in [from Upcoming]" leaves the bottom of the Confirmed group and goes to No-show.
- From In stay: "check out [from In stay]" goes to Completed.
- From the Confirmed group as a whole: "guest cancels" leaves the right edge of the group and goes to Cancelled. I read this as a guest can cancel from either Upcoming or In stay.
- No-show, Completed and Cancelled each go to an end dot.

There are no diamond decision shapes. The branches are all labelled transitions.

## 4 What the key says

- Black filled dot: Start
- Pale blue rounded box with blue outline: First state
- White rounded box with grey outline: State
- Grey filled rounded box with thicker grey outline: Final state
- Black dot with grey ring: End
- Plain arrow: Leads to

Almost every mark is in the key. Not in the key: the pale blue Confirmed group box that holds Upcoming and In stay (a composite or parent state), and the bracketed text on labels such as "[from Upcoming]" and "[from In stay]", which I understood without a key entry. All lines look like the same solid style, so there is no dashed line to explain.

## 5 What I could not read, follow or found ambiguous

- Inside the Confirmed group, In stay has an arrow to an end dot at the right of the group. At the same time "check out [from In stay]" leaves the group on its left. It is unclear whether that inner end dot means the stay finishing and then leads to Completed, or is a separate ending. I took check out to Completed as the real exit.
- The "check out" and "missed check-in" lines start at the edges of the Confirmed group, not at the In stay or Upcoming boxes. The bracketed "[from ...]" text fixes this, but the line itself does not show it.
- The right side "guest cancels" line leaves the group as a whole, so the board implies a guest can cancel even during In stay. That may or may not be intended.
- The source note says declined-card and expiry paths are left out, so a Pending booking whose card is declined or that expires has no shown outcome.
- The retro section on the left has no title and nothing ties it to the diagram. It looks like an unrelated board sharing the page.

## 6 Could I act on this board without asking anyone

Yes for the main lifecycle, since every status and trigger is labelled and the final states are clear, but I would ask whether cancelling during In stay is allowed and what the inner end dot in Confirmed means before building on it.
