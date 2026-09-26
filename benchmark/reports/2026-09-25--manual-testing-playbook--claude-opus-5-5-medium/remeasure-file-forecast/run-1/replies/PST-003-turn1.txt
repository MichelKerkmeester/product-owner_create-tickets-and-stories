````markdown
I'll bring Priya's save card draft into the house Story format. The draft doesn't settle the points below, so please answer them together in one reply before I start.

**1. Title and header line**
- I plan to title it `Customer - Checkout - Save card for next time`. Is that right?
- Should I drop the export line above the title ("Exported from the Checkout team space on 2026-09-22...")?

**2. Card brand conflict**
- The draft stores "token, brand, last four and expiry" and shows the brand logo at the payment step
- The company context says Fernhouse may store a card token, the last four digits and the expiry date "and nothing else"
- Which of these wins? Brand could be fetched from the payment provider when the card is shown, the storage rule could have an approved exception, or the logo could be dropped

**3. Build checklist**
- The house Story doesn't use a checklist. I'd move the items that contain a rule or a string into Requirements: the service refuses a sixth card, the fields that get stored, and the remove button with its `Remove this card?` confirmation. The per-platform FE lines would move to the tasks. Is that OK?
- The three DATA events have no names yet. Our analytics rules need `object_action` names and a tracking plan row before any FE work. Do you have the names from the Data team, or should the requirement point to the tracking plan and leave the names open?

**4. Declined saved card**
- Its copy is `TBD...`. I'd mark it as an `**Open:**` line, and that also adds a `## Delivery` section (Estimation, Rabbit holes and No-gos). Who decides the copy? Is there an estimate or an exclusion to add?
- Beyond the copy, what does the customer do next? For example, do they choose another card or type one in?

**5. Gaps the acceptance criteria will expose**
- Are expired cards shown in `Account > Payment methods` so they can be removed? Do they count towards the limit of 5?
- For "Orders over `€150`", does "over" mean strictly above? Is the amount the order total including shipping?
- Is a card saved only once payment is authorised, or also when it is declined?
- At the payment step, is the saved card preselected, or only listed first?
- Is a card saved on web available in the apps, and the other way round?

**6. Evidence**
- The company context doesn't include the 17% app drop-off and the 9% web drop-off at the payment step. Is there a dashboard link I can add to References?
- Should Expected outcomes get target numbers, or stay descriptive?
````

Export-equivalent path: `export/NNN - Story-save-card-for-next-time-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `TBD...` is quoted from the source's own placeholder.

I haven't drafted the Story yet. `$s` asks its intake question and waits, and a few points in the draft could be read two ways.

- **Card brand:** The biggest issue is the conflict with the company's card data rule. The draft stores the card brand, but the company context lists what Fernhouse may store (token, last four digits, expiry date) and says nothing else. I won't choose between them for you.
- **Acceptance criteria:** The draft has none. Most of the other questions cover gaps that would otherwise make me invent behavior when I write them.

Once you answer, I'll restructure the draft into the house Story format. I'll keep the draft's original filename, and I'll list anything I add that isn't in Priya's draft so you can remove it.