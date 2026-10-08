Priya's draft is saved as a rough PRD, and it can't go straight into the house format yet. Your `$s` command asks one consolidated question before drafting, and the draft has real gaps. I've put that question in a clarification block.

```markdown
I'll bring Priya's save card draft into the house Story format. Before drafting, I need the decisions below in one response:

**1. Card brand:** Fernhouse context allows storing only the card token, the last four digits and the expiry date. Priya's build item also stores the brand, and the saved card shows a brand logo. Which should I write?
- Keep brand, after Lotte updates the company constraint
- Drop brand, and show a generic card icon
- The payment provider returns the brand on each request, and nothing is stored

**2. CVC threshold basis:** Does "orders over €150, or £130 in the UK" mean the subtotal, which is after promotions and before shipping, or the order total including shipping?
- Subtotal, after promotions and before shipping
- Order total, including shipping

**3. Declined saved card copy:** The draft leaves this copy open. Supply the copy, or confirm it stays open and name who settles it. An open copy line also brings a Delivery section into the Story.

**4. Event names:** The DATA item names three events in words only: card saved, card removed and order paid with a saved card. Give the exact names, in the snake_case object_action form Fernhouse uses for events.

**5. Acceptance criteria:** The draft has no Given, When and Then criteria. Should I write them from the outcomes and requirements, naming each one I add, or will Priya supply them?

Reply with all five answers together, so I can draft once.
```

Export-equivalent path: `export/NNN - Story-save-card-for-next-time-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

Quality status: not scored, because no artifact has been drafted yet.

**Artifact kind:** Story. The draft has hard requirements and no child-story set, so the Epic shape doesn't apply. I'm treating it as a refinement of Priya's draft, with the restructuring you asked for. The planned title is `Customer - Checkout - Save card for next time`, with no PRD prefix.

**Why it waits:** The brand line conflicts with Fernhouse's rule on what card data may be stored, and the saved card display needs a brand logo to work. The CVC threshold could mean two different amounts. The declined-copy line is open. The three events have no names. The draft has no acceptance criteria.

**Assumptions to correct:** I read "restructure whatever it needs" as permission to reshape the draft. I took the persona as Customer, from the draft's "signed-in customers".

**Next step:** Answer the five questions in this conversation. This session has no ClickUp connector, so I have no push to offer.