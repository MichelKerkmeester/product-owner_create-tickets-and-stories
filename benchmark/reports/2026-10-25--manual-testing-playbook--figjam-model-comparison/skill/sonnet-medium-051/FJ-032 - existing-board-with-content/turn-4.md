Here is the full reading, before I draw anything.

**Question and outcome**
* Question: which statuses can a Roamstay booking be in, and what moves it between them?
* Outcome: the product and engineering team agree the status values and allowed moves before a story is written
* Dials: Balanced detail, Mixed audience, Laptop distance
* Source: your message, treated as current behaviour

**What your message settled**
* States: Pending, Confirmed containing Upcoming and In stay, Completed, Cancelled, No-show
* Moves: card authorised, guest cancels from Pending or Confirmed, check-out ending in Completed, and a missed check-in ending in No-show, marked by the hotel

**What I assumed**
* Reader, outcome and the three dials come from my recommendations
* Every booking starts at Pending, and Completed, Cancelled and No-show are final
* `check-in` moves Upcoming to In stay, because you named no trigger
* A guest can cancel during In stay, because Confirmed contains it
* The state is named Cancelled

**Still open**
* What happens when the card authorisation fails. The board will not show it

**Outline**
1. The board answers: which statuses can a Roamstay booking be in, and what moves it between them?
2. A start dot enters Pending
3. Pending moves to Confirmed on `card authorised`
4. Confirmed is a section holding Upcoming and In stay, entered at Upcoming
5. Upcoming moves to In stay on `check-in`
6. Confirmed moves to Completed on `check-out [from In stay]`
7. Confirmed moves to No-show on `missed check-in [from Upcoming]`
8. Pending moves to Cancelled on `guest cancels`
9. Confirmed moves to Cancelled on `guest cancels`
10. Completed, Cancelled and No-show each end in a dot

That is 7 states and 11 transitions, within the 9 and 12 a state board allows. Cutting any step would lose a status or a move you named.

**Two framings**
* Confirmed as a section: cancel is one move from Confirmed, and the grouping you described stays visible. Check-out and no-show need an inner-state guard each
* Flat, with Upcoming and In stay as top-level states: no guards, but cancel needs two moves and the Confirmed grouping disappears
* Recommended: the section, because you grouped Upcoming and In stay under Confirmed and the single cancel move matches your wording

**The look**
* Title: Roamstay booking status lifecycle
* Subtitle: From a new Pending booking to Completed, Cancelled or No-show, for the product and engineering team
* Source line: the team's description of the booking statuses, with authorisation failure, refunds and booking changes left out because nothing states them
* First glance: Pending, the entry state. Then Upcoming and In stay inside their section. The three end states come last. Recommended: no state is picked out, since your request doesn't single one out
* Zones: the Confirmed section only

Is this reading right, or do you want to correct any of it?