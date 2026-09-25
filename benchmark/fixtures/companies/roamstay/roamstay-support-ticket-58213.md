# Guest Support ticket 58213, Android total lower than the charge

Source: ticket export from the Guest Support queue in the support desk tool, escalated to the Booking squad
Opened on 2026-09-21 from in-app chat. Escalated by Maren, Guest Support agent (Tier 2), on 2026-09-21

| Field | Value |
|-------|-------|
| Ticket | 58213 |
| Status | Escalated to Booking squad |
| Priority | High |
| Channel | In-app chat, Android |
| Booking reference | RS-7Q4K2M |
| Booked on | 2026-09-20, with Pay now |
| Stay | 3 nights, 2 adults, 1 room |
| Property | 40217, city tax €3.00 per adult per night |
| Guest app | Android 8.12.1, app language en-GB |
| Tags | price-mismatch, android, confirmation-screen |

## Chat

Guest, 09:12
Hi, I booked a hotel yesterday for 3 nights. Your app said Total €387.00 on the confirmation but my bank took €405.00. That's €18.00 more than you told me. What is the extra?

Maren, 09:15
Hi, thanks for writing in. I'm checking booking RS-7Q4K2M for you now.

Guest, 09:16
Screenshot attached.

Maren, 09:24
Thanks. The room is €387.00 for the 3 nights, and the property charges a city tax of €3.00 per adult per night, so €18.00 for 2 adults over 3 nights. The charge of €405.00 is the full price with the city tax, and it is the only charge on your card. The Android app left the city tax out of the total on the confirmation screen. I'm sorry for the confusion. I'm emailing you the full breakdown now.

Guest, 09:27
OK, that makes sense. The app should show the right number though.

Maren, 09:28
Agreed. I'm passing it to the team that owns that screen.

## Internal notes

Maren, 09:35
Back office for RS-7Q4K2M shows one Pay now charge of €405.00, captured on 2026-09-20. Breakdown in Back office:

| Line | Amount |
|------|--------|
| Room, 3 nights at €129.00 | €387.00 |
| City tax, €3.00 per adult per night, 2 adults, 3 nights | €18.00 |
| Total | €405.00 |

The guest's screenshot of the Android confirmation screen shows Total €387.00. The confirmation email for the same booking says Total €405.00. So the charge matches the booking and the app screen shows less than we took.

Maren, 10:02
Tried it on the Guest Support Android test phone, app 8.12.1, same property, Pay now, 2 adults, with the team's test card:

- 2 nights: the payment step showed the City tax line and €270.00. After Pay now, the confirmation screen showed Total €258.00. Back office has the charge at €270.00, which is €258.00 for the room plus €12.00 city tax
- 1 night: the confirmation screen showed Total €135.00, which matches the charge of €129.00 plus €6.00 city tax

Same 3-night booking on the iOS test phone, app 8.12.0: the confirmation screen shows Total €405.00, which is right. Cancelled all three test bookings inside free cancellation straight after.

Maren, 10:20
Searched the queue for chats tagged price-mismatch since the release on 2026-09-16 (iOS 8.12.0, Android 8.12.1). 14 chats, all from Android 8.12.1, all Pay now bookings of 2 nights or more. None from iOS or web. I can't tell whether Pay at property bookings show the same thing. Those guests aren't charged until they arrive, and nobody has written in about one yet.

## Escalation to the Booking squad

Maren, 10:31
Priority High. Every Pay now guest on Android with a stay of 2 nights or more sees a total on the confirmation screen that is lower than the charge on their card, and they read it as an overcharge. 14 chats in five days so far, and the Android rollout only reached everyone today.

What we need: the Android confirmation screen showing the same total we charge. Until then we answer these chats with the Back office breakdown. The confirmation email is right, so we point guests to it as well.
