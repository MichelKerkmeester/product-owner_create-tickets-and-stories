Reading: an ER diagram for Guest Support. Six tables. Guest, Booking and Payment sit on the guest side. Property, Room and RatePlan sit on the partner side. A guest makes bookings. A booking reserves one room under one rate plan and holds its payments. A property offers rooms and publishes rate plans. The model passes the pre-write check at 6 entities and 6 relationships. The grouping needs two tints behind the tables, because Mermaid cannot draw ER groups.

Two gaps block the write:

- This Figma account has no plan named Roamstay Product. It holds <figma-plan-3> (Starter, View), <figma-plan-1> (Pro, Full) and <figma-plan-2> (Pro, member). Recommended: <figma-plan-1>, the only plan with a Full seat for a new board. If Roamstay Product lives on another account, send its plan key or invite this account.
- The schema note is not attached. I have the tables and relationships, not the column list. Recommended support set: Guest id, email, country. Booking id, guestId, roomId, ratePlanId, checkIn, checkOut, status. Payment id, bookingId, amount. Property id, city. Room id, propertyId, capacity. RatePlan id, propertyId, refundable. Add a booking reference if the note has one.

Question: use <figma-plan-1> and that column set, or name the correct plan and columns?