# FJ-032 page: fresh reader notes

The page holds two sections. The diagram is the large white frame on the right, titled "Booking status". The other section is a smaller white frame at the top left with six grey sticky notes in two rows of three: "Standups ran long", "Design review was useful", "Too many hotfixes", "Pairing helped onboarding", "Release notes were late" and "Try a demo every Friday". It has no title and reads like an unrelated team retrospective. Nothing connects it to the diagram.

## 1 Title and the question this board answers

The title is "Booking status" with the subtitle "Every status a Roamstay booking passes through, and what moves it on". It answers the question: which statuses can a booking be in, and which event moves it from one status to the next until it ends?

## 2 What you see first, and what second

First the bold title and subtitle at the top left of the right frame. Second the light blue "Pending" pill on the left, which is the only filled blue state and sits on the start line. After that the eye goes to the pale blue "Confirmed" group box across the top right and then to the three grey states stacked below it.

## 3 The main path or structure from start to end

This is a state diagram. A black start dot on the far left leads to Pending, a blue rounded pill. From Pending a line labelled "card authorised" rises, runs right along the top and drops onto the top edge of the Confirmed group box. Inside Confirmed there is its own start dot that leads to Upcoming, a white rounded pill. Upcoming leads to In stay, another white pill, by the label "check in". In stay leads to an end dot inside the Confirmed box. The happy path then leaves Confirmed by the line labelled "check out [from In stay]" and reaches Completed, a grey rounded pill, which leads to an end dot.

## 4 Every decision or branch and where each exit goes

There are no diamond decisions. The branches are transitions out of states.

- Pending has two exits. "card authorised" goes into Confirmed and "guest cancels" runs down and right to Cancelled.
- Upcoming has two exits. "check in" goes to In stay and "missed check-in [from Upcoming]" goes down from the bottom of the Confirmed box to No-show.
- In stay has the exit "check out [from In stay]" to Completed, plus the arrow to the inner end dot.
- Confirmed as a whole has the exit "guest cancels", which leaves from its right edge, runs down the right side and comes back left into the top of Cancelled.
- No-show, Completed and Cancelled are grey final states and each leads straight to its own end dot.

## 5 What the key says, and whether every mark is in the key

The key at the bottom lists six items. A plain black dot is Start. A blue filled pill with a blue outline is First state. A white pill with a grey outline is State. A grey filled pill with a darker grey outline is Final state. A black dot with a ring around it is End. A thin grey arrow is Leads to.

Not every mark is in the key. The pale blue Confirmed group box that holds Upcoming and In stay has no key entry, so a reader has to guess that it is a parent status containing sub statuses. The bracket notation in labels such as "[from Upcoming]" and "[from In stay]" is not explained. The sticky notes on the left frame are also not in the key, but they are not part of the diagram. A footnote under the key reads "Source: the Roamstay booking status rules, as given in the request. Left out: a declined or unauthorised card on a Pending booking."

## 6 Anything I could not read, could not follow or found ambiguous

- The "check out [from In stay]" line does not start at In stay. It starts at the left edge of the Confirmed box near the inner start dot, so only the bracket text says where it comes from. The same is true of "missed check-in [from Upcoming]", which leaves the bottom middle of the Confirmed box rather than Upcoming.
- In stay leads to an end dot inside Confirmed, and check out also leads to Completed. It is unclear whether these are the same event or whether the inner end means something separate.
- The "guest cancels" line from the right edge of Confirmed does not say whether a guest can cancel during In stay or only while Upcoming.
- Small labels such as "check in", "card authorised" and "guest cancels" are tiny at overview size and only readable when zoomed in. The "check in" arrowhead is very short.
- The Start dot and End dot differ only by a thin ring, which is hard to tell apart at overview size.
- The unrelated retrospective sticky notes on the same page could make a reader wonder whether they belong to this board.
- What happens to a declined card on Pending is explicitly left out, so that path is unknown.

## 7 Could a product manager act on this board without asking anyone?

Mostly yes for the main lifecycle, but no for the edges, because the declined card case is missing and the from-labels on lines that leave the Confirmed box rather than the named state leave cancellation during a stay and the inner end dot open to question.
