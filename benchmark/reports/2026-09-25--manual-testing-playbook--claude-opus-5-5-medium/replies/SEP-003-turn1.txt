I've written the Epic for self-serve returns and saved it.

Path: `export/001 - Epic-self-serve-returns.md`
Verified: read-back succeeded; 96 lines
HVR self-scan: 2 hard blockers. Fixed: Oxford comma in the Problem paragraph, Oxford comma in acceptance criterion 3. Kept with reason: none.

**Quality summary:** It follows the Epic layout: no Requirements section and no Delivery section, since you didn't ask for one and nothing required it. It has three release-level acceptance criteria. Every number comes from your request or the Fernhouse context: the 30-day window, the 60% target for Q1 2027, about 1,900 return requests a month and the 6-day average refund. The format-check script (`validate-output-format.cjs`) isn't in this workspace, so I checked the layout rules by hand.

The Epic sets out the current process where CS creates every return by hand, then the 60% goal and the four child stories. The stories are listed as plain text in two groups, starting a return and after the return is sent, with guest returns under Added Later. Pallet items stay with CS in every story.

**Additions you didn't state directly, so you can strike any of them:**
- The Problem bullets draw on the Fernhouse context, including that customers can't see where their return stands.
- Criterion 3 says returns outside the 30-day window, pallet items and guest orders all go through CS as they do today.
- The child story titles use a "Returns" segment, as in `Customer - Returns - Start a return from order history`.
- References links the context file, since you gave no Figma or ClickUp links.

**For the child stories:** the refund story will need to say who triggers the refund after the warehouse check. The context says a CS agent can refund up to €200, and anything above that needs a CS lead. Measuring the 60% target will also need a tracking-plan row and a DATA task. I haven't added either to the Epic.