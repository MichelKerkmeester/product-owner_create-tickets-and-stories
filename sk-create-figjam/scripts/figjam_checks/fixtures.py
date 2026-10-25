#!/usr/bin/env python3
# ───────────────────────────────────────────────────────────────
# COMPONENT: SELF-TEST FIXTURES
# ───────────────────────────────────────────────────────────────

"""Good models that must pass, and planted models that each break one rule.

Each planted model names the message its failure must print, so a rule that
stops firing, or fires with a message that no longer says what is wrong,
fails the self-test.
"""

GOOD = {
    "a user flow with one accent": """flowchart TD
    start([Open settings]) --> pick[Pick an option]
    pick --> saved{"Saved (to the account)?"}
    saved -->|Yes| done([Option shown])
    saved -->|No| retry[Show the error]
    retry --> pick
    %% a comment may hold `backticks`
    style done fill:#CDF4D3,stroke:#66D575
    style pick stroke:#66D575
    linkStyle 2 stroke:#66d575
""",
    "a left-to-right user flow in shorthand hex": """flowchart LR
    a([Open settings]) --> b["Pick an option: Brand™"]
    b --> c([Option shown])
    style c fill:#cdf4d3
""",
    "a laned process": """%% type: process
flowchart LR
    subgraph customer ["Customer"]
        ask([Return asked])
        label[/Print the label/]
    end
    subgraph agent ["CS agent"]
        review{Within 30 days?}
        approve[Approve the return]
        decline([Return declined])
    end
    subgraph warehouse ["Warehouse"]
        receive[Receive the parcel]
        orders[(Orders)]
        refund([Refund sent])
    end
    ask --> review
    review -->|Yes| approve
    review -->|No| decline
    approve --> label
    approve -.->|"Logs"| orders
    label --> receive
    receive --> refund
    style customer fill:#F5F5F5,stroke:#B3B3B3
    style approve fill:#C2E5FF,stroke:#3DADFF
""",
    "an architecture": """%% type: architecture
flowchart LR
    subgraph client ["Client Apps"]
        web[Web App]
    end
    subgraph gateway ["API Layer"]
        edge[API Gateway]
    end
    subgraph service ["Core Services"]
        orders[Order Service]
        payments[Payment Service]
    end
    subgraph datastore ["Data Stores"]
        db[Orders DB]
    end
    subgraph external ["External"]
        psp[Card Processor]
    end
    subgraph async ["Events"]
        queue[Order Events]
    end
    web <-->|"HTTPS"| edge
    edge -->|"Routes /orders"| orders
    orders <---|"Refund"| payments
    orders -->|"Writes Orders"| db
    payments -.->|"Card Processor: Charges"| psp
    orders -.->|"Produces"| queue
    queue -.->|"Consumes"| payments
""",
    "a sequence": """sequenceDiagram
    title Checkout payment
    participant GuestApp
    participant BookingApi
    participant PaymentProvider
    GuestApp->>BookingApi: POST /bookings
    BookingApi->>PaymentProvider: Authorise card
    PaymentProvider-->>BookingApi: Authorised
    BookingApi--)GuestApp: Booking confirmed
""",
    "a state machine": """stateDiagram-v2
    direction LR
    [*] --> Pending
    Pending --> Confirmed: pay
    state Confirmed {
        [*] --> Upcoming
        Upcoming --> InStay: check in
        InStay --> [*]
    }
    state Settle <<choice>>
    Confirmed --> Settle: check out
    Settle --> Completed: paid in full
    Settle --> Disputed: charge disputed
    Pending --> Cancelled: cancel
    Completed --> [*]
""",
    "an ER model": """erDiagram
    Guest ||--o{ Booking : makes
    Property ||--|{ Room : offers
    Room ||--o{ Booking : "is booked in"
    Guest {
        string id PK
        string email UK
    }
    Booking {
        string id PK
        string guestId FK
        string roomId FK
        date checkIn
    }
    Property["Listed Property"] {
        string id PK
        string city
    }
    Room {
        string id PK
        string propertyId FK
    }
""",
    "a gantt chart": """gantt
    title Offline mode launch
    dateFormat YYYY-MM-DD
    section Build
    Sync engine :active, sync, 2026-11-02, 3w
    Conflict screen :screen, after sync, 2w
    section Launch
    Beta :beta, after screen, 2w
    Release :milestone, after beta, 0d
""",
    "a sequence beside a user flow": """```mermaid
flowchart TD
    a([Open]) --> b([Done])
    style b fill:#CDF4D3,stroke:#66D575
```

```mermaid
sequenceDiagram
    participant GuestApp
    participant BookingApi
    GuestApp->>BookingApi: GET /trips
    BookingApi-->>GuestApp: Trip list
```
""",
}

PLANTED = {
    # Every kind
    "an unsupported kind": ("""pie
    "Yes" : 10
""", "a pie block: Flow Mode does not draw it"),
    "an unknown flowchart type": ("""%% type: swimlane
flowchart TD
    a([Start]) --> b([Done])
""", "is no flowchart type"),
    "a type comment that contradicts its header": ("""%% type: state
sequenceDiagram
    participant GuestApp
    participant BookingApi
    GuestApp->>BookingApi: Ping
""", "the header already names the kind"),
    "an emoji": ("""flowchart TD
    a([Start \U0001f680]) --> b([Done])
""", "carries an emoji"),
    "markdown emphasis in a label": ("""flowchart TD
    a([Start]) --> b["**Done**"]
""", "carries markup"),
    "single-star emphasis in a label": ("""flowchart TD
    a([Start]) --> b["*Done*"]
""", "carries markup"),
    "an html tag in a label": ("""flowchart TD
    a([Start]) --> b["<b>Done</b>"]
""", "carries markup"),
    "a literal backslash-n in a label": ("""flowchart TD
    a([Start]) --> b[Two\\nlines]
""", "literal \\n"),
    # User flow
    "a four-exit decision": ("""flowchart TD
    a([Start]) --> d{Which plan?}
    d -->|Free| b([Free])
    d -->|Basic| c([Basic])
    d -->|Pro| e([Pro])
    d -->|Team| f([Team])
""", "exits, at most 3"),
    "an unlabelled decision exit": ("""flowchart TD
    a([Start]) --> d{Valid?}
    d -->|Yes| b([Done])
    d --> c([Fix it])
""", "has no label"),
    "a decision with no exit": ("""flowchart TD
    a([Start]) --> d{Valid?}
""", "has no exit"),
    "a shape a user flow does not use": ("""flowchart TD
    a([Start]) --> h{{Prepare}}
    h --> b([Done])
""", "which this diagram does not use"),
    "a merge dot with a label": ("""flowchart TD
    a([Start]) --> m((Join here))
    m --> b([Done])
""", "merge dot m carries the label"),
    "a stadium mid-flow": ("""flowchart TD
    a([Start]) --> s([Middle])
    s --> b([Done])
""", "sits mid-flow"),
    "a step with no way out": ("""flowchart TD
    a([Start]) --> b[Dead end]
""", "has no way out"),
    "a step with no way in": ("""flowchart TD
    a([Start]) --> b([Done])
    c[Orphan source] --> b
""", "has no way in"),
    "a 10-node user flow": ("flowchart TD\n    n1([Start]) --> n2[Step 2]\n"
                            + "".join(f"    n{i}[Step {i}] --> n{i + 1}[Step {i + 1}]\n" for i in range(2, 9))
                            + "    n9[Step 9] --> n10([End])\n", "10 nodes, at most 9"),
    "a 13-connector user flow": ("""flowchart TD
    s([Start]) --> a[Pick items]
    a --> d1{"Which return?"}
    d1 -->|"Refund"| b[Refund card]
    d1 -->|"Exchange"| c[Pick size]
    d1 -->|"Credit"| e[Store credit]
    b --> f[Print label]
    c --> f
    e --> f
    f --> d2{"More items?"}
    d2 -->|"Yes"| a
    d2 -->|"No"| z([Done])
    b --> z
    c --> z
""", "13 connectors, at most 12"),
    "a line break in a label": ("""flowchart TD
    a([Start]) --> b[Two<br/>lines]
    b --> c([Done])
""", "label carries a line break"),
    "an unquoted parenthesis": ("""flowchart TD
    a([Start]) --> b([Pick a plan (monthly)])
""", "put it in double quotes"),
    "an unquoted colon in an edge label": ("""flowchart TD
    a([Start]) --> d{Paid?}
    d -->|Yes: card| b([Done])
    d -->|No| c([Stop])
""", "put it in double quotes"),
    "a right-to-left flow": ("""flowchart RL
    a([Start]) --> b([Done])
""", "direction RL"),
    "two directions in one flow": ("""```mermaid
flowchart TD
    a([Start]) --> b([Hand off])
```

```mermaid
flowchart LR
    b([Hand off]) --> c([Done])
```
""", "run LR and TD"),
    "a fill outside the FigJam palette": ("""flowchart TD
    a([Start]) --> b([Done])
    style b fill:#00ff00
""", "is not a FigJam light fill"),
    "a stroke outside the FigJam palette": ("""flowchart TD
    a([Start]) --> b([Done])
    linkStyle 0 stroke:#123456
""", "is not a FigJam palette stroke"),
    "a fill with another pair's stroke": ("""flowchart TD
    a([Start]) --> b([Done])
    style b fill:#CDF4D3,stroke:#FF7556
""", "but FigJam pairs it with #66d575"),
    "a connector in a second colour": ("""flowchart TD
    a([Start]) --> b([Done])
    style b fill:#CDF4D3,stroke:#66D575
    linkStyle 0 stroke:#FF7556
""", "2 accent colours"),
    "a user flow with no accent": ("""flowchart TD
    a([Start]) --> b([Done])
""", "the model has no accent"),
    "a process whose only colour is a connector": ("""%% type: process
flowchart LR
    subgraph one ["Customer"]
        a([Ask])
    end
    subgraph two ["Agent"]
        b([Answer])
    end
    a --> b
    linkStyle 0 stroke:#66d575
""", "the model has no accent"),
    "a second fill after a semicolon": ("""flowchart TD
    a([Start]) --> b([Done]); style a fill:#CDF4D3; style b fill:#FFCDC2
""", "2 accent colours"),
    "a saturated fill": ("""flowchart TD
    a([Start]) --> b([Done])
    style b fill:#66D575,stroke:#3E9B4B
""", "is not a FigJam light fill"),
    "a reserved node id": ("""flowchart TD
    a([Start]) --> end([Done])
""", "is reserved"),
    "an underscore in a node id": ("""flowchart TD
    my_start([Start]) --> b([Done])
""", "holds an underscore"),
    "a hyphen in a node id": ("""flowchart TD
    my-start([Start]) --> b([Done])
""", "is not camelCase"),
    "a dotted connector in a user flow": ("""flowchart TD
    a([Start]) -.-> b([Done])
""", "is not a one-way arrow this diagram draws: write -->,"),
    "a long connector": ("""flowchart TD
    a([Start]) ---> b([Done])
""", "long or invisible connector"),
    "an invisible link": ("""flowchart TD
    a([Start]) --> b([Done])
    a ~~~ b
""", "long or invisible connector"),
    "a node with no connector": ("""flowchart TD
    a([Start]) --> b([Done])
    c[Loose step]
""", "node c has no connector"),
    "a label over 40 characters": ("""flowchart TD
    a([Start]) --> b([Review every setting on the account page now])
""", "at most 40"),
    "a subgraph in a user flow": ("""flowchart TD
    subgraph group [Group]
        a([Start]) --> b([Done])
    end
""", "a user flow has no subgraphs"),
    "one label on four connectors": ("""flowchart TD
    a([Start]) -->|then| b[Pick]
    b -->|then| c[Check]
    c -->|then| d[Send]
    d -->|then| e([Done])
""", "4 connectors carry the label 'then'"),
    # Process
    "one lane": ("""%% type: process
flowchart LR
    subgraph team ["Team"]
        a([Start]) --> b([Done])
    end
""", "1 lanes, a laned process has 2 to 6"),
    "a step outside every lane": ("""%% type: process
flowchart LR
    subgraph left ["Left"]
        a([Start])
    end
    subgraph right ["Right"]
        b([Done])
    end
    a --> c[Loose]
    c --> b
""", "sits outside every lane"),
    "nested lanes": ("""%% type: process
flowchart LR
    subgraph outer ["Outer"]
        a([Start])
        subgraph inner ["Inner"]
            b([Done])
        end
    end
    subgraph other ["Other"]
        c([Also done])
    end
    a --> b
    a --> c
""", "lanes do not nest"),
    "an edge to a lane": ("""%% type: process
flowchart LR
    subgraph left ["Left"]
        a([Start])
    end
    subgraph right ["Right"]
        b([Done])
    end
    a --> right
    a --> b
""", "joins the lane right"),
    "a lane in an accent colour": ("""%% type: process
flowchart LR
    subgraph left ["Left"]
        a([Start])
    end
    subgraph right ["Right"]
        b([Done])
    end
    a --> b
    style left fill:#C2E5FF,stroke:#3DADFF
""", "a lane takes the neutral pair"),
    "a thick connector in a process": ("""%% type: process
flowchart LR
    a([Start]) ==> b([Done])
""", "write --> or -.->"),
    "a 10-node process without lanes": (
        "%% type: process\nflowchart TD\n    n1([Start]) --> n2[Step 2]\n"
        + "".join(
            f"    n{i}[Step {i}] --> n{i + 1}[Step {i + 1}]\n" for i in range(2, 9)
        )
        + "    n9[Step 9] --> n10([End])\n",
        "10 nodes, at most 9",
    ),
    "a 13-node laned process": ("%% type: process\nflowchart LR\n    subgraph one [\"One\"]\n        n1([Start])\n"
                                + "".join(f"        n{i}[Step {i}]\n" for i in range(2, 7))
                                + "    end\n    subgraph two [\"Two\"]\n"
                                + "".join(f"        n{i}[Step {i}]\n" for i in range(7, 13))
                                + "        n13([End])\n    end\n"
                                + "".join(f"    n{i} --> n{i + 1}\n" for i in range(1, 13)),
                                "13 nodes, at most 12"),
    # Architecture
    "an architecture running top to bottom": ("""%% type: architecture
flowchart TD
    subgraph service ["Services"]
        a[Alpha Service]
        b[Beta Service]
    end
    a -->|"Calls"| b
""", "an architecture runs left to right"),
    "an architecture lane with an unknown id": ("""%% type: architecture
flowchart LR
    subgraph services ["Services"]
        a[Alpha Service]
    end
""", "lane services is not one of"),
    "an architecture node outside a lane": ("""%% type: architecture
flowchart LR
    subgraph service ["Services"]
        a[Alpha Service]
    end
    loose[Loose Node]
    a -->|"Calls"| loose
""", "the layout cannot place it"),
    "styling in an architecture": ("""%% type: architecture
flowchart LR
    subgraph client ["Clients"]
        web[Web App]
    end
    subgraph gateway ["Edge"]
        lb[Load Balancer]
    end
    web -->|"HTTPS"| lb
    style web fill:#CDF4D3
""", "the architecture layout colours each lane itself"),
    "a client reaching a service directly": ("""%% type: architecture
flowchart LR
    subgraph client ["Clients"]
        web[Web App]
    end
    subgraph service ["Services"]
        api[Api Service]
    end
    subgraph datastore ["Stores"]
        db[Main DB]
    end
    web -->|"Calls"| api
    api -->|"Reads"| db
""", "the missing lane goes in between: a gateway between a client and a service"),
    "a solid edge to an external system": ("""%% type: architecture
flowchart LR
    subgraph service ["Services"]
        api[Api Service]
    end
    subgraph external ["External"]
        psp[Card Processor]
    end
    api -->|"Card Processor: Charges"| psp
""", "write it dotted"),
    "an unlabelled external edge": ("""%% type: architecture
flowchart LR
    subgraph service ["Services"]
        api[Api Service]
    end
    subgraph external ["External"]
        psp[Card Processor]
    end
    api -.->|"Charges"| psp
""", 'label it "Service: Purpose"'),
    "a forward cycle in an architecture": ("""%% type: architecture
flowchart LR
    subgraph service ["Services"]
        a[Alpha Service]
        b[Beta Service]
    end
    a -->|"Calls"| b
    b -->|"Calls back"| a
""", "form a cycle"),
    "two edges between one pair": ("""%% type: architecture
flowchart LR
    subgraph client ["Clients"]
        web[Web App]
    end
    subgraph gateway ["Edge"]
        lb[Load Balancer]
    end
    web -->|"HTTPS"| lb
    web <-->|"WebSocket"| lb
""", "repeats a pair already joined"),
    "a service with no way out": ("""%% type: architecture
flowchart LR
    subgraph gateway ["Edge"]
        lb[Load Balancer]
    end
    subgraph service ["Services"]
        api[Api Service]
    end
    lb -->|"Routes"| api
""", "needs a way in and a way out"),
    # Sequence
    "a participant alias": ("""sequenceDiagram
    participant Api as "Booking API"
    participant Guest
    Guest->>Api: Book
""", "which the generator drops"),
    "an actor keyword": ("""sequenceDiagram
    actor Guest
    participant BookingApi
    Guest->>BookingApi: Book
""", "write participant"),
    "a note in a sequence": ("""sequenceDiagram
    participant Guest
    participant BookingApi
    Guest->>BookingApi: Book
    Note over Guest: waits
""", "a note is dropped by the generator"),
    "a loop fragment": ("""sequenceDiagram
    participant Guest
    participant BookingApi
    loop Every minute
    Guest->>BookingApi: Poll
    end
""", "a loop fragment is dropped"),
    "an activation shorthand": ("""sequenceDiagram
    participant Guest
    participant BookingApi
    Guest->>+BookingApi: Book
""", "is an activation, which is dropped"),
    "a cross arrow": ("""sequenceDiagram
    participant Guest
    participant BookingApi
    Guest-xBookingApi: Book
""", "the cross is not drawn"),
    "an unlabelled message": ("""sequenceDiagram
    participant Guest
    participant BookingApi
    Guest->>BookingApi:
""", "has no label"),
    "a semicolon in a message": ("""sequenceDiagram
    participant Guest
    participant BookingApi
    Guest->>BookingApi: Items a, b; c
""", "holds a semicolon"),
    "a cryptic participant id": ("""sequenceDiagram
    participant p1
    participant BookingApi
    p1->>BookingApi: Book
""", "is what the board shows"),
    "an undeclared third participant": ("""sequenceDiagram
    participant Guest
    participant BookingApi
    Guest->>BookingApi: Book
    BookingApi->>Payments: Charge
""", "participant Payments is not declared"),
    "six participants": ("sequenceDiagram\n" + "".join(f"    participant Party{i}\n" for i in range(1, 7))
                         + "".join(f"    Party{i}->>Party{i + 1}: Step {i}\n" for i in range(1, 6)),
                         "6 participants, at most 5"),
    "thirteen messages": ("sequenceDiagram\n    participant Guest\n    participant BookingApi\n"
                          + "".join(f"    Guest->>BookingApi: Step {i}\n" for i in range(1, 14)),
                          "13 messages, at most 12"),
    # State
    "the legacy state header": ("""stateDiagram
    [*] --> Draft
""", "write stateDiagram-v2"),
    "a note in a state machine": ("""stateDiagram-v2
    [*] --> Draft
    Draft --> Review: submit
    note right of Draft: editable
""", "phantom states"),
    "styling in a state machine": ("""stateDiagram-v2
    [*] --> Draft
    Draft --> Review: submit
    classDef bad fill:#FFCDC2
""", "phantom states"),
    "a machine with no entry": ("""stateDiagram-v2
    Draft --> Review: submit
""", "start it with [*]"),
    "an unlabelled transition": ("""stateDiagram-v2
    [*] --> Draft
    Draft --> Review
""", "name the event that triggers it"),
    "a nested composite": ("""stateDiagram-v2
    [*] --> Outer
    state Outer {
        [*] --> Inner
        state Inner {
            [*] --> Deep
            Deep --> [*]
        }
    }
""", "draw the inner machine as its own diagram"),
    "a transition into another composite": ("""stateDiagram-v2
    [*] --> Active
    state Active {
        [*] --> Working
        Working --> [*]
    }
    Paused --> Working: resume
    Active --> Paused: pause
""", "reaches into another composite"),
    "a one-exit choice": ("""stateDiagram-v2
    [*] --> Review
    state Gate <<choice>>
    Review --> Gate: decide
    Gate --> Approved: approve
""", "a choice has 2 to 3"),
    "an unguarded choice exit": ("""stateDiagram-v2
    [*] --> Review
    state Gate <<choice>>
    Review --> Gate: decide
    Gate --> Approved: approve
    Gate --> Rejected
""", "has no guard label"),
    "ten states": ("stateDiagram-v2\n    [*] --> S1\n"
                   + "".join(f"    S{i} --> S{i + 1}: next\n" for i in range(1, 10)), "10 states, at most 9"),
    # ER
    "an alias in a relationship line": ("""erDiagram
    Guest["Hotel Guest"] ||--o{ Booking : makes
""", "an alias inside a relationship line"),
    "an undocumented cardinality": ("""erDiagram
    Guest ||--x{ Booking : makes
""", "is not one Figma documents"),
    "an unlabelled relationship": ("""erDiagram
    Guest ||--o{ Booking :
""", "has no label"),
    "an unquoted two-word relationship label": ("""erDiagram
    Room ||--o{ Booking : booked in
""", "put it in double quotes"),
    "an entity with no PK": ("""erDiagram
    Guest ||--o{ Booking : makes
    Guest {
        string email
    }
""", "lists attributes but no PK"),
    "an underscore in an entity id": ("""erDiagram
    LINE_ITEM ||--o{ Order : "belongs to"
""", "holds an underscore"),
    "two spellings of one type": ("""erDiagram
    Guest ||--o{ Booking : makes
    Guest {
        string id PK
    }
    Booking {
        String id PK
    }
""", "is spelled String and string"),
    "styling in an ER model": ("""erDiagram
    Guest ||--o{ Booking : makes
    style Guest fill:#CDF4D3
""", "styling, which the generator drops"),
    "an entity in no relationship": ("""erDiagram
    Guest ||--o{ Booking : makes
    Invoice {
        string id PK
    }
""", "takes part in no relationship"),
    "eleven attributes": ("erDiagram\n    Guest ||--o{ Booking : makes\n    Guest {\n        string id PK\n"
                          + "".join(f"        string field{i}\n" for i in range(1, 11)) + "    }\n",
                          "lists 11 attributes, at most 10"),
    "a malformed attribute": ("""erDiagram
    Guest ||--o{ Booking : makes
    Guest {
        string id PRIMARY
    }
""", "an attribute is written type name"),
    # Gantt
    "a gantt with no dateFormat": ("""gantt
    Kickoff :k1, 2026-01-05, 3d
""", "has no dateFormat"),
    "a gantt in an odd date format": ("""gantt
    dateFormat DD/MM/YYYY
    Kickoff :k1, 05/01/2026, 3d
""", "write YYYY-MM-DD"),
    "styling in a gantt": ("""gantt
    dateFormat YYYY-MM-DD
    axisFormat %d %b
    Kickoff :k1, 2026-01-05, 3d
""", "axisFormat is stripped or ignored"),
    "a gantt anchored on a dependency": ("""gantt
    dateFormat YYYY-MM-DD
    Design :d1, after k1, 5d
""", "the first task needs a date"),
    "a dependency on an undefined task": ("""gantt
    dateFormat YYYY-MM-DD
    Kickoff :k1, 2026-01-05, 3d
    Build :b1, after d9, 5d
""", "after d9 names no task"),
    "minutes on a date chart": ("""gantt
    dateFormat YYYY-MM-DD
    Kickoff :k1, 2026-01-05, 3m
""", "is in minutes on a date chart"),
    "a milestone with a duration": ("""gantt
    dateFormat YYYY-MM-DD
    Kickoff :k1, 2026-01-05, 3d
    Ship :milestone, after k1, 2d
""", "a milestone has a zero duration"),
    "the vert tag": ("""gantt
    dateFormat YYYY-MM-DD
    Freeze :vert, 2026-01-05, 0d
""", "the vert tag"),
    "a start in the wrong format": ("""gantt
    dateFormat YYYY-MM-DD
    Kickoff :k1, 09:00, 3d
""", "does not match dateFormat"),
    "thirteen tasks": ("gantt\n    dateFormat YYYY-MM-DD\n    section One\n    T1 :t1, 2026-01-05, 1d\n"
                       + "".join(f"    T{i} :t{i}, after t{i - 1}, 1d\n" for i in range(2, 8))
                       + "    section Two\n"
                       + "".join(f"    T{i} :t{i}, after t{i - 1}, 1d\n" for i in range(8, 14)),
                       "13 tasks, at most 12"),
    "nine tasks in one section": ("gantt\n    dateFormat YYYY-MM-DD\n    T1 :t1, 2026-01-05, 1d\n"
                                  + "".join(f"    T{i} :t{i}, after t{i - 1}, 1d\n" for i in range(2, 10)),
                                  "group a chart over 8 tasks into sections"),
    "six parallel bars": ("gantt\n    dateFormat YYYY-MM-DD\n    section Build\n"
                          + "".join(f"    Track {i} :t{i}, 2026-01-05, 2w\n" for i in range(1, 7)),
                          "runs 6 bars at once, at most 5"),
    # Layout, measured on every flowchart profile
    "a rank of five steps": ("""flowchart TD
    a([Start]) --> b[Pick one]
    a --> c[Pick two]
    a --> d[Pick three]
    a --> e[Pick four]
    a --> f[Pick five]
    b --> g([Done])
    c --> g
    d --> g
    e --> g
    f --> g
""", "a rank holds 5 steps, at most 4"),
    "a chain of nine steps": ("flowchart TD\n    n1([Start]) --> n2[Step 2]\n"
                              + "".join(f"    n{i}[Step {i}] --> n{i + 1}[Step {i + 1}]\n" for i in range(2, 8))
                              + "    n8[Step 8] --> n9([End])\n", "9 steps, at most 8"),
    "connectors that swap sides": ("""flowchart TD
    s([Start]) --> a[Pick one]
    s --> b[Pick two]
    s --> c[Pick three]
    x[Send one]
    y[Send two]
    z[Send three]
    a --> z
    b --> y
    c --> x
    x --> e([Done])
    y --> e
    z --> e
""", "3 connector pairs swap sides"),
    "labels that run long": ("""flowchart TD
    a([Open the account settings page]) --> b[Review every notification setting]
    b --> c([Save the account settings])
""", "labels average 29 characters"),
    "a graph joined more than it reads": ("""flowchart TD
    s([Start]) --> a[Load the order]
    a --> b[Check the stock]
    b --> c[Save the order]
    c --> s
    s --> b
    b --> a
    a --> s
    c --> a
    s --> c
""", "9 connectors for 4 steps"),
}
