# Product Owner - Examples - Task - Design Briefing

Instantiates Task Templates section 7, Design Briefing. Shows a briefing across two apps and a design system block, with every optional section and a Why facet of plain bullets.

---

# Briefing - Partner & Creator - Barter Deals - Desired Collab Amount & Reach Pause

## About
* * *
This task makes sure creators only see deals that are still relevant and open to them. It also helps partners whose deals get fewer applications, so they are no longer hurt by partners who ghost creators or collect lots of applications without reviewing them.

The partner sets how many collaborations they want. Once applications pass a threshold based on that number, the feed shows the deal less (or not at all) until the partner accepts or rejects applicants.

## Briefing
* * *
*   The design starts from the rejected Creator Capacity concept and reuses its layout, reasons and creator row
*   It drops the `Unlimited` option and the closing of the deal, because the number is now a target
*   The feed logic is out of scope for design and is listed under Dev Handover

#### **References**
* * *
*   [Barter deal | Creator Limit](https://www.figma.com/design/MKARl3Qh6qLJfvHFPQxACT/%E2%80%A2-App---Creator?node-id=753-103821&t=L3XpEl8uzHxTQqO3-1)
*   `PR6 - Deal Reached Creator Capacity` notification concept

#### **Related tasks**
* * *
*   `Briefing - Partner - Barter Deals - Required Target Audience`

## Requirements
* * *
### PARTNER
* * *
**Display**
- [] Deal create and edit flows ask for the number of collaborations the partner wants
- [] Labels, explanation and helper copy speak about a target number, never a limit

**Validation**
- [] The field is required, with no `Unlimited` option and no default
- [] The field accepts 1 up to about 1,000 collaborations
- [] Create and save are blocked until a number is entered, with an error on the field
- [] The partner can still accept more creators than the number

**Existing Deals**
- [] When the partner edits a deal without a number, the field is empty
- [] Validation blocks saving that deal until the partner enters a number

**Reach Paused**
- [] The deal overview and the applicants list show the paused state, with the number of applicants waiting
- [] The deal stays live and open to applications while reach is paused
- [] The state covers both a deal shown less and a deal hidden from the feed
- [] The state clears once the partner has reviewed enough applicants
- [] The copy frames the pause as a threshold, never a penalty

**Notification & Email**
- [] A new partner notification is sent when a deal reaches its threshold and reach pauses
- [] It sends once per pause, and again only after the deal has cleared and paused once more
- [] The copy names the deal and the number of applicants waiting, and frames the pause as a threshold
- [] The email CTA opens the applications list, pre-filtered to that deal
- [] `PR6 - Deal Reached Creator Capacity` is retired or rewritten, because the deal no longer closes

### CREATOR
* * *
**Display**
- [] The deal details show the number as a row beside target audience and motivation, like the creator limit row
- [] The info icon on the row opens the explainer sheet
- [] The row and sheet show creators their chance of success after applying, not a limit
- [] The copy drops `Creator limit`, `spots left` and `Once every spot's taken, the deal closes`
- [] The sheet keeps the reasons brands set a number and that only creators the brand accepts count

**Visibility**
- [] The row and sheet show only once applicants waiting for review reach 95% to 100% of the number
- [] Once the partner's accepts and rejects drop it below 95%, the row and sheet hide again

### DESIGN SYSTEM
* * *
**Partner Form Components**
- [] Each form variant used in Barter deal and company creation gets its own dedicated form component
- [] Each component uses detached content, input and group layers, like `Form | Location` and `Form | Preview`
- [] The update stays simple and quick, with no redesign of the forms

**Why**
*   Each form can be edited on its own
*   Nothing breaks over time when a shared component changes
*   It adds more components, but these forms never need refactoring again

**Cleanup**
- [] `Page | Content` is removed from the Barter deal and company creation pages

## Deliverables
* * *
- [] Partner deal create and edit, with the field empty, filled and in error
- [] An existing deal opened for edit with no number set
- [] Partner deal overview and applicants list, live and with reach paused
- [] The new partner notification and its email
- [] Creator deal details with the row hidden and shown, plus the explainer sheet
- [] The dedicated partner form components

## Copy
* * *
*   Design writes placeholder copy for the field, the paused state, the creator row and the sheet
*   Copywriter writes the final copy for the notification and the email

## Open Questions
* * *
*   What is the exact upper limit for the number, given the about 1,000 in Validation?
*   Does the creator row stay visible once applicants waiting pass 100% of the number?

## Success Signal
* * *
*   Fewer live deals hold applicants nobody has reviewed
*   Deals from partners who review their applicants keep their place in the feed

## Dev Handover
* * *
*   The threshold that pauses reach, as a rule on the desired number
*   When the feed shows a paused deal less and when it hides it fully
