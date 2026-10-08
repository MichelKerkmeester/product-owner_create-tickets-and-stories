```markdown
I'll bring Priya's draft into the house Story format once you answer. Before drafting, I need the unresolved decisions below in one response:

**Shape and title:** I read this as one Story, not an Epic, because it covers one feature with hard requirements. I propose `Customer - Checkout - Save card for next time` as the title. Confirm it, or name a different persona or area. Priya's checklist is a task breakdown, so it leaves the Story body. Do you want the tasks as separate files too, or the Story alone?

- **Card brand:** The draft stores the card brand and shows the brand logo at the payment step. Company context lets Fernhouse keep only the token, the last four digits and the expiry date. Keep the brand as a stated exception to that rule, or drop the brand and the logo?
- **Account screen owner:** The draft puts the Account > Payment methods screen in this Story. Company context gives the account area to Storefront through accounts-service. Is that screen Checkout work, Storefront work or both?
- **Declined card copy:** The draft ends on `Copy for a declined saved card TBD...`. Supply the exact copy, or name the party who writes it.
- **Order threshold:** The draft asks for the CVC on orders over `€150` or `£130`. Company context defines the subtotal as the total after promotions and before shipping. Should the threshold use the subtotal or the total with shipping?
- **App release timing:** Company context says app changes reach most customers about a week after release. Should the Story name the app store release as an external dependency with its date `TBD...`? That adds a Delivery section.
- **Figures:** The Problem cites 17% and 9% drop-off for app and web. Give the source and period, or I carry them as Priya's figures.
```

Export-equivalent path: `export/NNN - Story-save-card-for-next-time-clarification.md`

I stopped before drafting, because `$s` asks its question first. The Story comes next once you answer.

Assumptions from the draft, to strike if wrong:
- This is a new Story built from Priya's draft. Her source file stays as it is.
- The persona is Customer, from the company roles.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `TBD...`, quoted verbatim from the source draft.