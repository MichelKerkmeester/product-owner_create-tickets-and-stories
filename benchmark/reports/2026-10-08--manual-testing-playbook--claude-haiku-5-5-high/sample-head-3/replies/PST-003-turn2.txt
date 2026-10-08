```markdown
## Save card for next time: two decisions left

Thanks. The declined-card copy, the CVC total and the event names are settled. Two decisions remain before I draft.

**1. Card brand:** The Fernhouse context, which Lotte owns, says Fernhouse may store a card token, the last four digits and the expiry date, and nothing else. Priya's draft also stores the card brand for the logo at the payment step. Which should the Story say?
- Keep the brand, and Lotte adds it to the context's list
- Read the brand from the provider's token when the card is shown, and store nothing beyond the list

**2. Acceptance criteria:** The draft has none, and the Story needs numbered Given, When, Then criteria. Which route?
- Priya sends her criteria, and I wait for them before drafting
- I write them from the outcomes and requirements, with these edges added for you to strike:
  - A declined saved card at the payment step
  - Removing the last saved card falls back to the full card form
  - An order whose total including shipping is exactly `€150` or `£130` asks for no CVC

Reply with both answers in one message. I draft after that.
```

Export-equivalent path: `export/NNN - Story-save-card-for-next-time-clarification-2.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

The first clarification stands, and this one covers only what is still open. Two changes follow from your answers:

- The declined-card copy goes into Requirements verbatim as `This card was declined. Choose another card or enter a new one.`
- The CVC limit reads as the order total including shipping.

The event line stays a pointer to the Data team's tracking plan, with no names. The declined-card copy is no longer open, so no Delivery section is forced, and the Story will end on Acceptance criteria.