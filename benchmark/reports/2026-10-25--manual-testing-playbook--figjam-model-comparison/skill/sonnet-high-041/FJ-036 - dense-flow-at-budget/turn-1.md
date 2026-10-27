Intake round one for the change-dates board. Nothing has been written to Figma yet. I haven't opened the file or spent a tool call on it.

**Settled so far**
* Type: user flow, because the question is which screens a guest passes through and where they choose
* Entry: booking page, the guest taps Change dates
* Exit: the updated booking is shown
* Choices: room free on the new dates (yes or no), then new price against old (higher, lower or same)
* System steps: the availability check and the price comparison, drawn as automatic and not as guest actions
* Source: your message, read as current behavior
* Target: existing file `<draft-file-key>`, as a new section beside what it already holds
* Size: about 8 nodes, so one board fits the 9-node budget

**Round one**

1. Reader and outcome
   * Reading: nothing in the message says who opens this board
   * Question: who reads it, and what do they decide afterwards?
   * Recommended: the Roamstay product and design team, deciding whether the flow covers every price outcome before build
   * Why: the file is in a product plan, and the three price outcomes are the part most likely to be argued over

2. What the board must not do
   * Reading: your message gives one main path and two branches. It doesn't mention a payment failing, the guest backing out or booking rules such as cancellation windows
   * Question: should the board leave those out?
   * Recommended: yes, leave them out and name them under `Left out:` as later boards
   * Why: drawing them would add behavior your description doesn't state

3. After the other rooms are shown
   * Reading: the message says the guest sees other rooms and stops there
   * Question: what does the guest do next?
   * Recommended: pick a room, and the flow rejoins at the price comparison
   * Why: the price outcome depends on the room, and the other option (pick different dates) loops back to the date picker

Any question you skip stands on its recommended answer, marked assumed, and I'll name it in the full playback before anything is written. Do you accept all three recommendations, or which would you change?