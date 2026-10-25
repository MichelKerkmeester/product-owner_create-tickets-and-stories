I've read the Flow Mode rules and the Fernhouse context. Nothing is written to the board yet, because Flow Mode needs your answers on the reading and then a separate yes before any write.

**Flow Mode, intake round one**

Type: user flow, since the question is which screens a customer passes through and where they choose. I expect 7 nodes against a budget of 9.

Settled from your message:
* Entry is the order list and the exit is the confirmation with a QR code
* Path: order list, order detail with Start a return, return reasons, drop-off point or courier pickup, confirmation
* Branch: returns are open 30 days after delivery, after that the app shows Contact support
* Free pickup for orders over 100 euros is a proposal under review, so it is not drawn as app behavior
* Target is the existing file <test-file-key>, with the board added beside what is already there and no new file created. Your message also says "new board in our Fernhouse Product plan". I read the file key as the stronger instruction, because a plan only matters when a file is created
* I have no screenshots or returns doc text in this session, only your description, so labels use your wording

**1. Reader and outcome**

Reading: the customer is the actor, but no reader of the board is named.
Question: who opens this board, and what do they decide or do afterwards?
Recommended: the Post-purchase team and design, to agree the return start path and the 30-day branch. The board leaves out refunds, the warehouse check and the CS-created return, and does not show free pickup as live.
Why: the company context puts returns (RET) under Post-purchase, and the board then answers one question only.

**2. A source clash**

Reading: `fernhouse-context.md`, updated 2026-09-18 after the 4.8 releases, says there is no self-serve return today. The customer contacts CS and an agent creates the return in Admin. Your message describes a self-serve start inside the app.
Question: is the in-app flow live now, or new since that note, for example in 4.9.0?
Recommended: your description governs and is drawn as current behavior, marked assumed. The reply's `Left out:` line names the clash with both sources.
Why: you cite the app and the returns doc directly, and the note is five weeks old. If the flow is not live yet, it is approved direction, and the board's subtitle says so.

**3. Where the 30-day check sits**

Reading: you say the app shows Contact support after 30 days, but not where.
Question: does the order detail swap Start a return for Contact support, or does the button show and then lead to Contact support?
Recommended: a choice "Within 30 days of delivery?" after the order detail. Yes goes on to the return reasons and No goes to Contact support.
Why: it matches your wording and adds no screen you did not mention.

Answer 1 to 3, or say "use the recommendations". I will then play back the full reading before anything is drawn.