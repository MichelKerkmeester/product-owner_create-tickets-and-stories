Nothing is written to FigJam yet. Flow Mode confirms the reading first and then asks for a separate yes to write. The scratch check I ran on a draft model passed, and I deleted it.

```text
Before I draw anything, this is how I read the request.

Question: which screens does a Fernhouse customer pass through to start a return in the app, and where do they give up?
Outcome: a reader can follow a return from the order list to a confirmed return and see the three places support says customers give up.
Must not: draw the free pickup over 100 euros as live behavior, or pin anything beyond the three places.

Settled by your message:
- Screens: order list, order detail with Start a return, a list of return reasons, a drop-off or pickup choice, a confirmation with a QR code
- Returns are open 30 days after delivery, then the app shows Contact support
- The three give-up points as support reports them: too many reasons, an unclear pickup fee, no warning before day 30
- Left out: the free pickup over 100 euros, a proposal under review

Source conflict, needs your answer:
The Fernhouse company context, last updated 2026-09-18, says there is no self-serve return today. Customers contact CS and an agent creates the return in Admin. Your request describes a Start a return button in the app. Both agree on the 30 days.
Recommended: the app and the returns doc govern, because they are specific and the context note may predate them. Unanswered, I proceed on that, mark it assumed and flag the note in the reply.

No screenshots or returns doc reached this session, so every screen and rule rests on your description. If you attach them, I re-read the labels against them.

Assumed:
1. Reader: the Fernhouse Product team, deciding what to change in the returns flow. A one-line correction settles it
2. The 30 day check sits after Order detail, with Contact support as the exit when it fails. Your text says the app shows Contact support after day 30 but not on which screen. The returns doc section or a screenshot of an expired order settles it

Not added: your list has one drop-off or pickup choice, so both answers lead to the confirmation. I add no "pick a drop-off point" or "book a pickup" screen. If they exist, they come in as two more nodes and the board stays at 9.

Outline, 7 nodes and 7 connectors:
1. Order list to Order detail
2. Order detail to Within 30 days?
3. Within 30 days? No, to Contact support
4. Within 30 days? Yes, to Return reasons
5. Return reasons to Drop-off or pickup?
6. Drop-off or pickup? Drop-off point, to Return confirmed
7. Drop-off or pickup? Courier pickup, to Return confirmed

Two framings:
A (recommended): one board, the main line from order list to confirmation, Contact support beside it and three numbered pins on the give-up places. It keeps the path and the friction side by side.
B: two boards, the path first and the give-up points on a second one. It costs a second write and splits what a reader compares.

Look, all proposed:
- First glance: Return confirmed, the goal, in green with the pink outline. Second glance: the three pins. Last glance: Contact support
- Balanced detail, mixed audience, the app's own words, Laptop reading distance
- Three zones: Find the order, Request the return, Done
- Title "Start a return", a one-sentence subtitle and a source line naming your description and the left-out proposal
- Pins on Return reasons, Drop-off or pickup? and Within 30 days?, each note opening with "Support:" so it reads as reported friction and not app behavior

Is this the right reading of the board, including that the app and returns doc govern over the context note?
```