**Write gate**

**User intent:** How does a Fernhouse customer start a return in the app, and where does the 30-day limit direct them?

**Outcome:** The reader can follow the path from the order list to a QR code confirmation, or to Contact support after 30 days of delivery.

**First glance:** Return confirmed, QR code  
**Second glance:** Drop-off or pickup  
**Last glance:** Contact support

```mermaid
flowchart LR
    %% title: Start a return in the app
    %% subtitle: How a Fernhouse customer follows the app flow from an order to QR confirmation
    %% source: User-confirmed app and returns-doc summary. The no-self-serve claim in Fernhouse context is superseded for this flow. Left out: exact reason labels and free pickup over €100 (proposal under review).
    %% zone: Find the order: orders, detail
    %% zone: Request the return: window, support, reason, method, dropoff, pickup
    %% zone: Done: confirmed
    orders([Order list]) -->|"Open an order (assumed)"| detail["Order detail: Start a return"]
    detail -->|"Tap Start a return"| window{Within 30 days of delivery?}
    window -->|Yes| reason[Choose a return reason]
    window -->|No| support([Contact support])
    reason --> method{Drop-off or pickup?}
    method -->|Drop-off| dropoff[Choose a drop-off point]
    method -->|Pickup| pickup[Choose a courier pickup]
    dropoff --> confirmed([Return confirmed, QR code])
    pickup --> confirmed
    style confirmed fill:#CDF4D3,stroke:#66D575
```

The pre-write check passed: 9 nodes, 9 connectors, 4 labelled decision exits, 0 crossings. The assumption that a customer opens an order to reach its detail is marked in the flow. Exact reason labels and the proposed free pickup stay out of the current-behavior path.

**Plan:** Fernhouse Product, as supplied  
**File:** Existing FigJam file `<test-file-key>`  
**Write:** Add one section titled “Start a return in the app,” placed to the right of existing page content. The existing “Start a return” section remains intact.  
**Extensions:** None  
**Calls:** One `use_figma` composition call and one `get_figjam` read-back  
**Rollback:** Delete only the new section after a separate explicit yes naming it

Write this section to the existing file?