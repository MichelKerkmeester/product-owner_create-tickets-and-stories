# Product Owner - Examples - Briefing - Single App

Instantiates Design Briefing Template section 2. Shows one app with no audience labels, both link blocks and every closing section.

---

# Briefing - Shopper - Order Reviews - Star Rating & Photo Reviews

## About
* * *
Shoppers can only leave a star rating after an order. Merchants say the rating alone does not tell them what went well, and new shoppers say they do not trust a store with a few bare ratings. Since June, about 6,500 orders were rated and fewer than 5 percent carried any comment.

Shoppers can add a short text and photos to their rating. The review then shows on the store page.

## Briefing
* * *
*   The design starts from the rating sheet shown after delivery and adds a text field and a photo row below the stars
*   It reuses the photo picker and the star control from the order flows
*   The reviews list on the store page is new and follows the existing store card style
*   Replies from merchants are out of scope for design and are listed under Dev Handover

#### **References**
* * *
*   [Ordly order | Rate your order](https://www.figma.com/design/EXAMPLE/Ordly-Shopper?node-id=0-3)
*   [Ordly store | Header](https://www.figma.com/design/EXAMPLE/Ordly-Shopper?node-id=0-4)
*   `RV1 - Rate Your Order` notification concept

#### **Related tasks**
* * *
*   `Briefing - Shopper & Merchant - Returns - Return Requests & Refund Status`
*   `Briefing - Merchant - Store Setup - Welcome Checklist`


## Requirements
* * *
**Display**
- [] The rating sheet keeps the stars first and adds a text field and a photo row beneath
- [] The text field has a placeholder that invites a short opinion
- [] The store page shows a reviews list under the store header, newest first
- [] Each review shows the stars, the text, the photos and the date
- [] A review with photos shows them as a row that opens a full size view

**Validation**
- [] The text field is limited in length, with a counter that appears near the limit
- [] The photo row accepts images only, with a message for any other file

**Existing Reviews**
- [] A rating left before the release shows as stars only, with no empty text or photo area
- [] A shopper can open an older rating and add text or photos to it

**Notification & Email**
- [] `RV1 - Rate Your Order` is rewritten so it also invites a short opinion
- [] The email CTA opens the rating sheet for that order

**Visibility**
- [] The reviews list shows only when the store has at least one review
- [] The photo row in a review hides when the review has no photos

**Contrast**
- [] Review text stays readable over the photo row and over the card background


## Deliverables
* * *
- [] The rating sheet empty, filled and in error
- [] The store page with the reviews list empty, with one review and with many
- [] A review with and without photos, and the full size photo view


## Copy
* * *
*   Design writes placeholder copy for the placeholder, the counter and the empty reviews list
*   Copywriter writes the final copy for the notification and the email


## Open Questions
* * *
*   Can a shopper edit a review after sending it, and for how long
*   Who decides whether reviews with photos need a moderation step


## Success Signal
* * *
*   More ratings carry text or photos


## Dev Handover
* * *
*   How the average rating is worked out and shown on the store page
*   How a merchant reply attaches to a review
