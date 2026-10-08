```markdown
Thanks. I have the declined card copy, the CVC threshold and the event names. Before drafting, I still need the decisions below in one response:

- **Card brand:** The draft stores the card brand and shows the brand logo at the payment step. Company context lets Fernhouse keep only the token, the last four digits and the expiry date. Keep the brand as a stated exception to that rule, or drop the brand and the logo?
- **Account screen owner:** The draft puts the Account > Payment methods screen in this Story. Company context gives the account area to Storefront through accounts-service. Is that screen Checkout work, Storefront work or both?
- **Shape and title:** Confirm `Customer - Checkout - Save card for next time`. Do you want the tasks as separate files too, or the Story alone?
- **Figures:** Give the source and period for the 17% and 9% drop-off figures, or I carry them as Priya's figures.
- **App release timing:** Should the Story name the app store release as an external dependency with its date `TBD...`? That adds a Delivery section. Or leave it out?
```

Export-equivalent path: `export/NNN - Story-save-card-for-next-time-clarification-2.md`

The first clarification block stays as it stands. The Story takes the next number once you answer.

Recorded from your answers:
- The declined card copy is `This card was declined. Choose another card or enter a new one.`
- The `€150` and `£130` CVC threshold uses the order total including shipping.
- The three DATA events stay unnamed and point at the Data team.

Company context says a new event needs a row in the Data tracking plan and a DATA task before any FE task sends it. The FE tasks therefore depend on the Data team naming the events.

I have not drafted yet. The card brand decision conflicts with company context, and the account screen owner decides whether that screen belongs in this Story.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `TBD...`, quoted from the source draft.