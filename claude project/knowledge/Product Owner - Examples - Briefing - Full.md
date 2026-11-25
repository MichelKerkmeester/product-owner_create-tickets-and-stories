# Product Owner - Examples - Briefing - Full

Instantiates Design Briefing Template section 2. Shows a briefing across two apps and a design system block, with every optional section, every facet type and a Why facet of plain bullets.

---

# Briefing - Shopper & Merchant - Returns - Return Requests & Refund Status

## About
* * *
Shoppers have no way to return an item inside the app. They write to support, and merchants then chase the details by email. Since September, about 1,900 return requests reached support by email or chat, and support says roughly a third of them had no order number or photo.

Shoppers start a return from a delivered order and follow the refund in the app. Merchants get the request in one place and answer it there.

## Briefing
* * *
*   The design starts from the order detail screen in both apps and adds a return flow beside the existing help link
*   It reuses the order row, the photo picker and the status chip, so no new patterns are needed
*   It drops the support email as the return channel, because the request now carries its own details
*   The refund payout itself is out of scope for design and is listed under Dev Handover

#### **References**
* * *
*   [Ordly order | Detail](https://www.figma.com/design/EXAMPLE/Ordly-Shopper?node-id=0-1)
*   [Ordly order | Merchant overview](https://www.figma.com/design/EXAMPLE/Ordly-Merchant?node-id=0-2)
*   `RF2 - Refund Sent` notification concept

#### **Flows**
* * *
*   [Ordly returns | Return flow](https://www.figma.com/board/EXAMPLE/Ordly-Returns-Flow?node-id=0-1)

#### **Related tasks**
* * *
*   `Briefing - Shopper - Order Reviews - Star Rating & Photo Reviews`
*   `Briefing - Merchant - Store Setup - Welcome Checklist`


## Requirements
* * *
#### SHOPPER
* * *
**Display**
- [] The order detail screen shows a `Return an item` action under the delivery row
- [] The return flow lists the items of the order and lets the shopper pick one or more
- [] Each picked item asks for a reason from a short list and offers an optional note
- [] A summary step shows the items, the reason and the expected refund before sending
- [] A sent return gets its own row in the order history

**Validation**
- [] The note is limited in length, with a counter that appears near the limit
- [] The photo picker accepts images only, with a clear message for any other file
- [] A photo that fails to upload shows a retry action on that photo, not on the whole form

**Refund Pending**
- [] The state starts when the merchant accepts the return and ends when the refund is sent
- [] The status chip reads as in progress and the order row shows the expected refund amount
- [] The shopper can still open the return and read the merchant's reply
- [] The state clears into `Refunded` once the refund is sent

**Visibility**
- [] The `Return an item` action shows only on delivered orders
- [] The action hides on an order whose items are all returned already
- [] The expected refund amount hides until the merchant has accepted the return

**Contrast**
- [] The status chips stay readable over the order card, in light and dark mode


#### MERCHANT
* * *
**Display**
- [] A new returns list sits beside the open orders list, newest request first
- [] Each request shows the order, the items, the reason and the shopper's photos
- [] The merchant can accept or decline from the request, and a decline needs a short reply

**Existing Orders**
- [] Orders delivered before the release can also be returned
- [] Older orders without item photos show the item name only, never an empty frame

**Notification & Email**
- [] A new merchant notification is sent when a shopper sends a return
- [] A new shopper notification is sent when the merchant accepts or declines
- [] `RF2 - Refund Sent` is rewritten so it names the item and the amount
- [] Each email CTA opens the return itself, not the order list


#### DESIGN SYSTEM
* * *
**Return Components**
- [] The reason picker, the photo grid and the return summary each get their own component
- [] Each component keeps the same layers in both apps, like `Return | Reason` and `Return | Photos`
- [] The status chip gains a refund variant set instead of a new chip

**Why**
*   A return flow will grow, so each step can change on its own
*   Both apps stay in step because they share one component
*   It adds components now, but later steps need no rework

**Cleanup**
- [] `Help | Contact Support` is removed from the order detail footer


## Deliverables
* * *
- [] Shopper return flow, with the picker empty, filled and in error
- [] Shopper order detail with the action shown and hidden
- [] Shopper order history with a return in progress and a refunded return
- [] Merchant returns list and a single request, accepted and declined
- [] The new notifications and their emails
- [] The dedicated return components


## Copy
* * *
*   Design writes placeholder copy for the flow, the chips and the merchant reply
*   Copywriter writes the final copy for the notifications and the emails


## Open Questions
* * *
*   Does a partial return of an order refund the delivery cost, and who decides
*   Can a shopper cancel a return after sending it


## Success Signal
* * *
*   Fewer return requests reach support by email or chat
*   More requests arrive with an order number and a photo


## Dev Handover
* * *
*   The rule for which orders and items can still be returned
*   How a refund amount is worked out and when it is sent
*   Which statuses move a return from sent to refunded
