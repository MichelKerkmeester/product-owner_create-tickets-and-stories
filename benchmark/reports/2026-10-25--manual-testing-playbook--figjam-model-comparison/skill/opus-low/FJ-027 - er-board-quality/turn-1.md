Before I draw anything, here's how I read the request. Please check it.

**Question the board answers:** how the Roamstay stays tables relate, with the partner side kept apart from the guest side, so support can follow a booking back to its guest, room, rate plan and payments.

**What your schema summary settles**
- Guest zone: `guests`, `bookings`, `payments`
- Partner zone: `properties`, `rooms`, `rate_plans`
- One guest has many bookings
- One booking reserves exactly one room
- One booking uses exactly one rate plan
- One booking has many payments
- One property has many rooms
- One property has many rate plans

**What I've assumed (correct anything that's wrong)**
- Primary keys are `guest_id`, `booking_id`, `payment_id`, `property_id`, `room_id` and `rate_plan_id`.
- The foreign keys follow the relationships above: `bookings.guest_id`, `bookings.room_id`, `bookings.rate_plan_id`, `payments.booking_id`, `rooms.property_id` and `rate_plans.property_id`.
- There's no link between `rooms` and `rate_plans`, because the summary doesn't state one. I'll leave it off rather than guess.

**Still open**
- **Columns support asks about:** your message summarizes the schema note but doesn't include it, so I don't have actual column names. I won't invent columns like `status` or `amount`. My recommendation is that you paste the note or list the columns for each table. If you don't, the board will show keys only, and I'll mark that as a gap.

I'll confirm where the board goes in a separate step before anything is written. Your message gives three different destinations (a new board in the Roamstay Product plan, the existing file `<test-file-key>`, or a drafts file in the Barter team plan), and I'll ask you to pick one then.

Is this reading right, and which columns should each table show?