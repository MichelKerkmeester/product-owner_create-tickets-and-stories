```markdown
Thanks. The declined copy, the CVC rule and the event handling are recorded. Before I draft, these remaining decisions are needed in one response:

**1. Acceptance criteria:** Still missing. Either list the outcomes you want guaranteed, or reply "derive". With "derive", I'll write them from her Expected outcomes and requirements, cover web, iOS and Android, and name each criterion as my addition so you can strike it.

**2. Card brand:** Still open. The draft stores the card brand and shows its logo at the payment step, but the Fernhouse context allows only the token, the last four digits and the expiry date to be stored. Which applies?
- Drop the brand from storage and get the logo from the payment provider when it is shown
- Keep the brand, and Lotte updates the storage rule in the context before the build
- Drop the logo

**3. Analytics events:** I'll write one analytics requirement covering the events for card saved, card removed and order paid with a saved card, with the names marked open until the Data team supplies them. An open line also adds a Delivery section. Confirm, or say how you want it carried.

**4. Title:** Still to confirm. I'll use `Customer - Checkout - Save card for next time`. Confirm, or name another persona.
```

Export-equivalent path: `export/NNN - Story-save-card-for-next-time-clarification.md` (next number in the Story lane)

Recorded from your reply:
- The declined copy is `This card was declined. Choose another card or enter a new one.`, carried verbatim.
- The €150 and £130 CVC threshold applies to the order total including shipping.
- The event names stay out of the Story.

Nothing is drafted until the four items above are answered. Artifact kind stays Story.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.