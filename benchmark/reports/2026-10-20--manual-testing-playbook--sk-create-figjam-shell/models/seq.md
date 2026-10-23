```mermaid
sequenceDiagram
    participant G as GuestApp
    participant BookingApi
    G->>BookingApi: Post booking
    Note over BookingApi: holds the room
    BookingApi-->>G: 201 created
```
