**Pre-write check:** Passed. The model has 6 entities, 6 relationships, and 26 attributes. The composer reports no design warnings.

**Question and outcome:** Guest Support can trace a booking reference to its guest, room, rate plan, payment, and property tax context.

**Glance order**

- First: Booking
- Second: Booking’s links to Guest, Payment, Room, and Rate Plan
- Last: Property tax context and the assumed field names, types, and multiplicities

**Review**

- Booking is marked as the focal entity
- The relationship labels show that each Booking uses one Room and one Rate Plan
- Guest records and Partner records are in separate zones
- The source line identifies the assumptions and the omitted direct Room–Rate Plan link

**Destination:** Roamstay Product plan, existing FigJam file `<test-file-key>`. I’ll add one section titled **Roamstay Stays Model for Guest Support**, positioned to the right of existing content. No extensions are planned, and existing sections will stay as they are.

The write needs one `use_figma` call and one `get_figjam` read-back. The initial file read is already complete. Rollback would remove only the new section and would need separate confirmation.

```mermaid
%% title: Roamstay Stays Model for Guest Support
%% subtitle: Guest Support follows a booking from its reference to the payment and partner details that explain a stay
%% source: Sources: user schema summary, Roamstay context, Support ticket 58213. Assumed: key and support field names, types and multiplicities. Left out: direct Room to Rate Plan link, not named in schema summary.
%% zone: Guest records: Guest, Booking, Payment
%% zone: Partner records: Property, Room, RatePlan
%% focus: Booking
erDiagram
    direction LR
    Guest ||--o{ Booking : makes
    Booking ||--o{ Payment : holds
    Booking }o--|| Room : reserves
    Booking }o--|| RatePlan : uses
    Property ||--o{ Room : offers
    Property ||--o{ RatePlan : publishes
    Guest {
        unknown id PK
    }
    Booking {
        unknown id PK
        unknown guestId FK
        unknown roomId FK
        unknown ratePlanId FK
        unknown bookingReference
        unknown stayNights
        unknown adultCount
        unknown roomAmount
        unknown cityTaxAmount
        unknown totalAmount
    }
    Payment {
        unknown id PK
        unknown bookingId FK
        unknown amount
        unknown currency
        unknown status
    }
    Property {
        unknown id PK
        unknown cityTaxRule
    }
    Room {
        unknown id PK
        unknown propertyId FK
        unknown roomType
        unknown maxOccupancy
    }
    RatePlan {
        unknown id PK
        unknown propertyId FK
        unknown cancellationPolicy
        unknown paymentOption
    }
```

May I write this section to the existing FigJam file?