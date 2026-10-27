Routing this as a Flow user flow. I've read the Flow skill and the Fernhouse notes in `context/`, and nothing is written to the board. This is the playback, before any model.

Question: which screens does a Fernhouse customer pass through to start a return in the app, and where do they choose?
Outcome: a reader can follow a return from the order list to the QR code confirmation and see where the 30 day window ends it with Contact support.
Target: the existing FigJam file <draft-file-key>, with the board added as a new section beside what it holds. I read "new board" and "existing file" as the same thing, so no new file is created and no plan question is open.
Settled by your description: the order list, the order detail with Start a return, the reasons list, the drop-off or courier pickup choice, the confirmation with a QR code, the 30 day window and Contact support after it.
Not received: the app screenshots and the returns doc did not reach me. Labels come from your wording, and only Start a return and Contact support are verbatim.

Open items, each with the answer I will take if you don't correct it:

1. Status
   Reading: `context/fernhouse-context.md`, updated 2026-09-18, says "There is no self-serve return today" and that CS creates returns in Admin. Your description has the customer starting one in the app, so both cannot be current behavior.
   Question: is the in-app flow live?
   Recommended: yes, your description governs.
   Why: the note is 39 days old, the apps ship every two weeks and up to three releases have landed since. You also name the app and the returns doc as the sources. If it is unreleased, the subtitle says so instead of drawing it as live.
2. Where the window check sits
   Reading: you say Contact support appears after 30 days, but not on which screen. You also name one choice screen and no screen after either option.
   Recommended: a "Within 30 days?" decision on Order detail, with Yes leading to the reasons and No to Contact support. Drop-off and courier pickup both lead straight to the confirmation.
   Why: Start a return lives on Order detail, so the app decides there whether to offer it. A map or slot screen after the choice would be one I made up.
3. Reader and what the board must not do
   Reading: no reader is named.
   Recommended: the Fernhouse Product team, mixed audience, balanced detail, laptop distance. The board draws nothing after the confirmation, such as the warehouse check, the refund or a CS-created return.
   Why: your question stops at starting a return.

Outline, in drawing order, 7 nodes and 7 connectors:
* Order list to Order detail
* Order detail to "Within 30 days?"
* No to Contact support, an exit beside the main line
* Yes to Return reasons, then to "Drop-off or courier pickup?"
* Each option to Confirmation with QR code, styled as the goal

Framings: the happy path with Contact support as the one exit beside it (recommended), against a map giving every exit equal weight, which loses the clear main line. Three zones: Find the order, Request the return and Done. Title "Start a return", subtitle "How a Fernhouse customer starts a return in the app, from the order list to a confirmation with a QR code".
Left out: anything after the confirmation.

Is this the right reading of the board, with the recommended answer taken on each open item unless you correct it?