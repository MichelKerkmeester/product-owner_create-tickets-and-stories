Architecture is settled, and your go-ahead covers the type but not the reading. Nothing is written yet. This is how I read the brief.

| Row | Value | Source | Status |
|---|---|---|---|
| Reader | Someone writing a ticket who needs to know which part owns signup, returns and refunds, the warehouse handoff or billing | The context doc says every team reads it before writing a ticket | assumed |
| Question | Which part of Fernhouse handles signup, returns and refunds, the warehouse handoff and billing, and how do they connect? | Your request | captured |
| Outcome | The reader can name the owning service and the outside system it calls | None | assumed |
| Scope | The five areas on one overview board | Your answer | captured |
| Entry | Web, iOS and Android, and Admin | Surfaces table | captured |
| Exit | Payment provider and warehouse system | Services and integrations | captured |
| Actors | Customers, CS agents and warehouse operators | Personas table | captured |
| Decisions and states | None, because an architecture draws parts and calls | Type rule | captured |
| Sources and class | `context/fernhouse-context.md`, updated 2026-09-18, current behavior | Repo | captured |

**Outline.** The first line is the sentence the board answers: "Which part of Fernhouse handles signup, returns and refunds, the warehouse handoff and billing, and how do they connect?"

| Item | Source | Status |
|---|---|---|
| Web, iOS and Android (client) | Surfaces table | stated |
| Admin (client) | Surfaces table | stated |
| Entry point (gateway) | None | assumed |
| accounts-service | Services table | stated |
| checkout-service | Services table | stated |
| orders-service | Services table | stated |
| Accounts database (datastore) | "Each service has its own database" | assumed |
| Payment provider (external) | Integrations | stated |
| Warehouse system (external) | Integrations | stated |
| Both clients to Entry point ("Sends requests", "Sends staff requests") | None | assumed |
| Entry point to accounts-service, checkout-service, orders-service ("Routes sign-in", "Routes checkout", "Routes orders and returns") | Each service's job in the services table | stated |
| checkout-service to orders-service ("Creates orders") | checkout-service creates the order and orders-service holds it, but no call is stated | assumed |
| checkout-service to Payment provider ("Authorises payment") | Key flow 2 | stated |
| orders-service to Warehouse system ("Sends paid order") | Integrations | stated |
| accounts-service to Accounts database ("Reads and writes accounts") | The database line above | assumed |

That is 9 nodes and 9 connectors, inside the architecture budget of 9 and 12.

**Five assumed items:**
- **Entry point.** The source names no gateway, but an architecture needs one between a client and a service. I'd label it "Entry point" and say so on the board's source line.
- **Accounts database.** accounts-service needs a way out, and the source gives each service its own database. The other services' databases stay off the board for budget.
- **Checkout to orders call.** It is the only link between the order being created and orders-service holding it.
- **Signup.** The source says "sign-in", not "signup", so accounts-service is drawn as the owner and the edge reads "Routes sign-in".
- **Billing.** I read billing as payment at checkout. The source has no billing system and no invoices.

**Left out:**
- Signup steps and invoices, because no source states them.
- The refund payout to the payment provider, because no source states that path.
- shipping-service, the parcel and pallet carriers and label creation, which would take the board to 10 nodes.
- The event queue, the email delivery provider and the helpdesk.
- The warehouse system reporting back when an order is packed, because an architecture has no edge from an outside system into a service.

**Two framings:**
- **Recommended: one overview board.** It shows all five areas, and the warehouse is a single outside system. It cannot show how a parcel gets labelled and handed to a carrier.
- **Two boards by request path.** One covers order and billing, the other returns and the warehouse, with shipping-service and the carriers on the second. Each board is fuller, but the reader has to look at two to see the whole product, and the write costs two compose calls.

**The look:** I'd use Balanced detail, a Mixed audience and Laptop distance.
- **First glance:** orders-service, marked "Owns returns and refunds". It joins checkout, Admin and the warehouse.
- **Second glance:** the two outside systems and the call into each.
- **Last glance:** the Entry point and the Accounts database.
- **Title:** "Fernhouse product architecture".
- **Subtitle:** "Which services handle signup, returns and refunds, the warehouse handoff and billing, for anyone writing a ticket".
- **Source line:** the context doc, the assumed Entry point and the left-out list above.

**Reading:** The source settles every service and outside system on the board. The five assumed items above are the only places I filled a gap.

**Question:** Does this reading match what the board should say, with those five items as marked?

**Recommended:** Yes, and draw the one overview board.

**Why:** Each assumed item is the smallest reading that keeps the diagram connected, and the source line will name them. A correction now costs nothing, but one after the write means composing the board again.