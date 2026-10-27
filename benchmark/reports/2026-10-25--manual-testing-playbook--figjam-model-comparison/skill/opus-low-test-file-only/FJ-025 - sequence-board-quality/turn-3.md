I'll take that as <figma-plan-1>, the plan I recommended. Your yes picked the plan but didn't approve a write, because I hadn't asked for one yet. Here is the write I'm proposing. Nothing goes to Figma until you approve it.

**What the board answers:** what happens, in order, when a guest pays for a Roamstay booking, and what changes when the card is declined.
**Outcome:** one sequence diagram of the checkout payment, with the authorised and declined paths.

**What a reader takes in, in order**
- **First:** the declined branch. The Booking API releases the hold and returns 402 to the Guest app
- **Second:** the authorised branch. The Booking API confirms the hold, notifies the Partner hub and returns 201
- **Last:** the opening steps (post booking, hold room, authorise card)

**What gets written**
- **Plan:** <figma-plan-1> (`team::<plan-id>`)
- **File:** a new FigJam board, created by this write, titled **"Roamstay checkout payment"**. File `<test-file-key>` isn't touched
- **Contents:** one sequence diagram with four participants (Guest app, Booking API, Payment provider, Partner hub), the eight steps you confirmed, and the authorised/declined split with its two branches labelled
- **Extras:** none, so no sticky notes, pins or legend
- **Figma calls:** five in total. One to create the board, one to start a session on it, two to load Figma's FigJam guidance, one to draw the diagram and one to read the board back. All count against <figma-plan-1>'s Pro allowance, not the Starter limit

**Undo:** the board is a new, separate file. To remove it, delete the "Roamstay checkout payment" board in <figma-plan-1> Nothing else in the plan changes.

Should I create this board in <figma-plan-1> and draw the diagram?

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.