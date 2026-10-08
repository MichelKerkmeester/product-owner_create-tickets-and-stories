Three of the five answers are in, so two remain. I'm asking only those two, and I'm not drafting yet.

```markdown
I have three of your five answers, so two remain. Before drafting, I need these in one response:

**1. Card brand:** Fernhouse context allows storing only the card token, the last four digits and the expiry date. Priya's build item also stores the brand, and the saved card shows a brand logo. Which should I write?
- Keep brand, after Lotte updates the company constraint
- Drop brand, and show a generic card icon
- The payment provider returns the brand on each request, and nothing is stored

**2. Acceptance criteria:** The draft has no Given, When and Then criteria. Should I write them from the outcomes and requirements, naming each one I add, or will Priya supply them?

Reply with both answers together, so I can draft once.
```

Export-equivalent path: `export/NNN - Story-save-card-for-next-time-clarification.md`, the next number in the Story lane after the first clarification, which stays as it stands.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

Quality status: not scored, because no artifact has been drafted yet.

**Recorded for the draft:**
- The declined-card copy is quoted verbatim in backticks: `This card was declined. Choose another card or enter a new one.`
- The €150 and £130 CVC limits apply to the order total including shipping.
- Event names are left out, as you asked. I'll add the Fernhouse rule that a new event needs a Data tracking-plan row before FE sends it. That is an addition, so you can strike it.

**Still waiting on:** the brand decision, because it conflicts with Fernhouse's storage rule, and the acceptance criteria. Once you answer both, I'll draft the Story.