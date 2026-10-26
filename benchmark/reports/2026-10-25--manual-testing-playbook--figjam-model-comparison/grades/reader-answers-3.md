# Reader 3 answers

## FJ-022
- Q1: Contact support (the "Within 30 days?" decision goes No to Contact support, which leaves the flow)
- Q2: Drop-off (choose a drop-off point) or pickup (book a courier pickup)
- Q3: No, it is left out of the board as a proposal under review
- Hard to read: none

## FJ-023
- Q1: The warehouse operator (Book a courier pickup sits in the Warehouse operator lane)
- Q2: The claim goes down the Unclear branch and the customer is asked to send a second photo, which returns to the "Damage clear?" decision
- Q3: Between the CS agent and the warehouse operator, at the "Claim queued" link from Approve the claim to Book a courier pickup
- Hard to read: the long line from Send a second photo back to the decision loops around other lines, and the Claim queued label sits in a gap between two lanes

## FJ-024
- Q1: API Gateway (Desktop App and Web Client by WebSocket, iOS App by HTTPS)
- Q2: Push Worker consumes the change from the Change Stream, then Apple Push wakes the device
- Q3: The dashed async or outside-call links: Publishes, Consumes and Apple Push: Wakes device
- Hard to read: the Writes Blocks line leaves Sync Service from the top and loops far over to Blocks DB

## FJ-025
- Q1: PaymentProvider (it gets Authorise card and replies Authorised)
- Q2: BookingCreated, the blue async message from BookingApi to PartnerHub
- Q3: Board 1: 201 Booking confirmed. Board 2 (declined card): 402 Payment declined
- Hard to read: none

## FJ-026
- Q1: Expired, Completed, No-show and Cancelled (the grey final states, each with an end dot)
- Q2: Pending and Confirmed (Upcoming and In stay), both with a guest cancels arrow to Cancelled
- Q3: check in
- Hard to read: the lines from the Confirmed box for check out, missed check-in and guest cancels run close together and cross other lines, so it is hard to tell which inner state each starts from. The guest cancels label near Expired sits next to the wrong line

## FJ-027
- Q1: One (Booking has a single roomId, linked to Room by "is reserved by (1 to 0..n)")
- Q2: Property (publishes 1 to 1..n Rate Plan)
- Q3: Yes, Booking holds (1 to 1..n) Payments
- Hard to read: the direction of the 1 to 0..n wording is not obvious, and the Rate Plan to Booking line "prices" runs a long way round

## FJ-028
- Q1: Desktop and iOS integration (1 week, critical)
- Q2: Sync engine (ends 23 Nov) and Conflict screen build (ends 30 Nov), both end by the 30 Nov start. No dependency arrows are drawn
- Q3: 21 Dec
- Hard to read: no arrows show what depends on what, so the order has to be read from the dates
