```markdown
## Save card for next time: intake before drafting

I'll bring Priya's draft into the house Story format. Before I draft, I need these three decisions in one reply.

**1. Card brand:** The Fernhouse context says Fernhouse may store a card token, the last four digits and the expiry date, and nothing else. Priya's draft also stores the card brand, which the logo at the payment step uses. Which should the Story say?
- Keep the brand, and Lotte adds it to the context's list
- Read the brand from the provider's token when the card is shown, and store nothing beyond the context's list

**2. Acceptance criteria:** The draft has none, and the Story needs numbered Given, When, Then criteria. Which route?
- Priya sends her criteria, and I wait for them before drafting
- I write them from the expected outcomes and requirements, with these three edges added for you to strike:
  - A declined saved card, with its copy still open
  - An order exactly at €150 or £130 asks for no CVC
  - Removing the last saved card at the payment step falls back to the full card form

**3. Declined saved-card copy:** The draft reads `Copy for a declined saved card TBD...`. Is it still open?
- Yes: the requirement carries an `**Open:**` line naming who settles the copy, and a Delivery section opens with Estimation, Rabbit holes and No-gos as `TBD...`
- No: paste the string and I use it verbatim

Reply with the three answers in one message. I draft after that.
```

Export-equivalent path: `export/NNN - Story-save-card-for-next-time-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

This is a Story: the draft has requirements and covers one feature. Before drafting, I need the answers above because the draft conflicts with the company context on card brand storage and has no acceptance criteria. Priya's draft will change in these ways once you answer:

- The title becomes `Customer - Checkout - Save card for next time`, without the `PRD -` prefix.
- The `Checklist` items are build steps (BE, FE, DATA), so they leave the Story. The Requirements section keeps only the hard constraints.
- The event line becomes a pointer to the Data team's tracking plan, because the draft names no event strings and I won't invent them.