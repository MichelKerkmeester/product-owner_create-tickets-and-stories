```markdown
I'll refine your PRD. Before drafting, I need the decisions below in one response. The operation is settled: a refinement with restructuring allowed, from `fernhouse-save-card-draft.md`.

**Requirements: card brand conflicts with the storage rule:** The Fernhouse context allows a card token, the last four digits and the expiry date, and nothing else. The draft also stores the card brand and shows its logo at the payment step. Which should the Story follow?
- Drop the brand and the logo
- Keep the brand as an open requirement until the owner of the context decides
- Show the logo from the payment provider at display time, with nothing stored

**Requirements: app release timing:** The iOS and Android parts ship in an app release. The next release is 4.9.0, and the context gives no date. Which release should they target, or should the date stay `TBD...`? An undated app-store dependency adds a Delivery section.

**Requirements: declined-card copy:** The draft leaves the copy for a declined saved card as `TBD...`. Do you have the wording? If not, name who settles it, and the requirement stays open with that owner.

**Acceptance criteria:** The draft has none. Which outcomes must the Story guarantee? I suggest starting from the three expected outcomes, with the save, pay and remove paths as the edges. Confirm that list or change it.

**Evidence and links:** Give the source and period for the 17% and 9% payment-step drop-off figures, since the company context has neither. The line that most people typing a card have done it before does not follow from 68%, which measures orders, so I will restate it as an order share unless you have a people figure. Add any design links for the card form, the payment step or Payment methods. Leave this blank if none exist.

**Validation:** I will check two assumptions. The BE, FE and DATA checklist leaves the Story, because build steps never sit in Requirements, so it moves to task work. The title becomes `Customer - Checkout - Save card for next time`, without the `PRD -` prefix. Tell me if either is wrong.
```

Export-equivalent path: `export/NNN - Story-checkout-save-card-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

Quality status: clarification only. No Story is drafted yet, because `$s` asks before drafting and the draft conflicts with the company storage rule.

Priya's draft is not in house format yet. Answer the question in one reply, and the Story comes next as its own Deliverable Block.