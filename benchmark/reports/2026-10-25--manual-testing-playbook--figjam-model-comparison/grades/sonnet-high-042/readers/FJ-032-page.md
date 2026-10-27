# Fresh reader: FJ-032 page

The page holds two sections. The diagram is the larger white frame on the right titled "Booking status". It is a state diagram of the booking lifecycle. The other section is a smaller frame at the top left holding six grey sticky notes that read like a team retro: "Standups ran long", "Design review was useful", "Too many hotfixes", "Pairing helped onboarding", "Release notes were late" and "Try a demo every Friday". It has no title and no link to the diagram.

## Quick questions

Q1: Which states end a booking?
Completed, No-show and Cancelled end a booking. Each is a grey pill marked "Final state" in the key and each has an arrow into an End dot on the far right of the diagram frame. Sure, high. One extra End dot also sits inside the Confirmed box after In stay, which I read as the end of the inner stay flow rather than a fourth final state.

Q2: What moves a booking from Pending to Confirmed?
"card authorised". The line leaves the top of the blue Pending pill, runs left and up and enters the left edge of the Confirmed box. Sure, high.

Q3: Is the retro content still readable?
Yes for what is there. All six sticky headings in the top left frame are legible at 100% and in the overview. The bodies of the stickies are empty, so there is nothing more to read. Sure, high.

## 1 Title and the question this board answers

The title is "Booking status" with the subtitle "Every status a Roamstay booking passes through, and what moves it on". It answers: what statuses can a booking be in and which event moves it from one to the next.

## 2 What you see first, and what second

First the large bold title and the wide light blue "Confirmed" box across the top of the diagram with Upcoming and In stay inside it. Second the solid blue Pending pill on the left, then the three grey final pills stacked on the right (Completed, No-show, Cancelled). The retro stickies at the top left are visible but clearly a separate frame.

## 3 The main path from start to end

A Start dot leads to Pending (blue pill, the first state). From Pending, "card authorised" leads into the Confirmed box. Inside Confirmed a Start dot leads to Upcoming (white pill), "check in" leads to In stay (white pill) and In stay leads to an End dot at the right of the box. From the Confirmed box, "check out [from In stay]" leads to Completed (grey pill) and Completed leads to an End dot.

## 4 Every branch and where each exit goes

From Pending there are two exits: "card authorised" into Confirmed and "guest cancels" along the bottom into Cancelled.
From Confirmed there are three exits, all drawn from the edge of the box rather than from the inner states:
"check out [from In stay]" leaves the top of the box and goes to Completed.
"missed check-in [from Upcoming]" leaves the right edge of the box and goes to No-show.
"guest cancels" leaves the bottom of the box and goes to Cancelled.
Completed, No-show and Cancelled each lead only to an End dot. Nothing comes back out of them.

## 5 The key

The key lists: black dot = Start, blue pill = First state, white pill = State, grey pill = Final state, black dot with a grey ring = End, thin arrow = Leads to.
Not every mark is in the key. The light blue rounded box labelled "Confirmed" that groups Upcoming and In stay is not explained, so a reader has to infer that it is a parent state. The bracketed notes such as "[from In stay]" and "[from Upcoming]" are not explained either, though they read as "only from this inner state". The edge labels themselves are self explanatory. All lines are solid, so there is no line style to miss.
A footer note says the source is the product owner's description and lists what is left out: payments and refunds, hotel-side screens and a timing rule for No-show.

## 6 Anything unreadable, hard to follow or ambiguous

The three exits from Confirmed start at the box edge, not at the inner state they belong to. The bracket text fixes this, but the eye has to read the label to know that check out only applies from In stay and missed check-in only from Upcoming. This sits along the top and right edges of the Confirmed box.
The End dot inside Confirmed after In stay is ambiguous. It suggests the inner flow ends there, yet the real exit to Completed is the separate check out line from the box top. It is not clear whether In stay reaching that dot means anything on its own.
"guest cancels" from Confirmed leaves the bottom of the box below In stay, so it is unclear whether a guest can cancel during In stay or only from Upcoming. No bracket qualifies it. This sits in the middle of the diagram near the vertical line under In stay.
The line from Completed to its End dot loops down and round rather than going straight across, which is a little harder to follow than the other two. Far right, beside Completed.
The retro frame at the top left has no title or date, so I cannot tell which sprint or team it belongs to or why it sits on this page.

## 7 Could I act on this board without asking anyone

Mostly yes: the states, the triggers and the three final states are clear enough to build or spec from, but I would ask whether a guest can cancel during In stay and what the inner End dot means before I committed.
