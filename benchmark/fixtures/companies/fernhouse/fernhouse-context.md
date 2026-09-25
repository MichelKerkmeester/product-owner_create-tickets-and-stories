# Fernhouse company context

Owned by Lotte, Head of Product, and kept in the Product space. Every team reads it before writing a ticket, and the owning team updates it when a surface, service or convention changes. Last updated 2026-09-18, after the 4.8 app releases.

Fernhouse sells its own range of cookware, tableware, kitchen textiles, storage and small furniture direct to consumers in five markets: the Netherlands, Belgium, Germany, France and the UK. There are no shops and no resellers. Everything ships from one warehouse in the Netherlands.

## Product and surfaces

Customers buy on three surfaces, and staff work in a fourth.

| Surface | Used by | What it covers |
|---------|---------|----------------|
| `Web` | Customers | The storefront: search, category pages, product pages, cart, checkout, account, order history and wishlist. One responsive build for desktop and mobile browsers |
| `iOS` | Customers | The Fernhouse app, with the same shopping flows as web plus push notifications for promotions and for a shipped order |
| `Android` | Customers | The same app scope as iOS, released on the same two-week cycle |
| `Admin` | Staff | The back office for orders, refunds, returns, customers, the catalog and promotions. Desktop web only |

Web takes about 61% of revenue and the apps about 39%. The apps carry more repeat business: returning customers place 68% of app orders against 44% on web.

A banner at the top of every web page and above the cart in the apps shows the free-shipping threshold for the market. It reads `Free shipping on orders over €50` in the four euro markets and `Free shipping on orders over £45` in the UK. Copy is written in English first and then translated, so those two lines are the source strings for every locale.

The cart icon in the web header and in the app tab bar carries a badge with the number of units in the cart, not the number of lines. Above 99 units it shows `99+`.

## Personas and roles

| Role | Works in | What they do |
|------|----------|--------------|
| `Customer` | Web, iOS, Android | Browses, buys, tracks orders and asks for returns. Can check out as a guest or with an account |
| `CS agent` | Admin and the helpdesk | Answers contacts by email and chat, looks up orders, issues refunds and creates returns |
| `Warehouse operator` | Admin and the warehouse system | Picks, packs and labels orders, and hands parcels and pallets to the carriers |
| `Merchandiser` | Admin | Maintains products, prices, sale prices, collections and promotions |

Admin permissions follow the job. A CS agent can refund up to €200 per order, and a CS lead approves anything above that. Only merchandisers can create or change a promotion. Warehouse operators see orders and shipments but no payment details.

A signed-in customer has an account with saved addresses and order history. A guest gives an email address at checkout and gets the order emails, but has no order history to come back to.

## Glossary

| Term | Meaning |
|------|---------|
| Market | One of NL, BE, DE, FR or UK. Sets currency, VAT, shipping fees and the banner copy |
| Unit | One item in the cart. A line with quantity 3 is 3 units |
| Subtotal | The sum of the lines after promotions and before shipping |
| Automatic promotion | A discount that applies without a code, set up by a merchandiser in Admin |
| Discount code | A code the customer types in the cart or at checkout |
| Sale item | A product whose `compare_at` price is higher than its price, shown struck through |
| Dispatch cut-off | `15:00` Amsterdam time on a working day. Orders paid before it leave the warehouse the same day |
| Collection | The parcel carrier's daily pickup at the warehouse, 18:00 on working days |
| Parcel item | An item within the parcel carrier's limits of `30 kg` and `120 cm` on the longest side |
| Pallet item | An item over either limit. It ships by the pallet carrier, which books a delivery slot with the customer by phone |
| Label | The parcel carrier's shipping label for one parcel. Every label the carrier creates is charged |
| WISMO | Where is my order, the helpdesk tag for order status contacts |
| Return window | `30 days` from delivery |

## Services and integrations

Internal services are owned by the team named in the table. Each service has its own database and talks to the others over HTTP and the event queue.

| Service | Owner | Does |
|---------|-------|------|
| `cart-service` | Checkout | Carts for guests and signed-in customers, the badge count, line prices after automatic promotions |
| `checkout-service` | Checkout | Address, shipping method, the payment session and order creation |
| `promotions-service` | Merchandising tools | Automatic promotions, discount codes and the free-shipping threshold |
| `orders-service` | Post-purchase | Orders, order status, refunds and the returns CS agents create |
| `shipping-service` | Fulfilment | The parcel and pallet split, parcel labels and tracking numbers |
| `accounts-service` | Storefront | Sign-in, addresses and the web wishlist |
| `catalog-service` | Merchandising tools | Products, prices, `compare_at` prices and stock synced from the warehouse system |

Third parties appear by role only:

- Payments go through the payment provider: cards, wallet payments and local bank payment methods, through hosted fields on web and its SDK in the apps
- Stock, picking and packing run in the warehouse system. orders-service sends it each paid order, and it reports back when the order is packed
- Every parcel in all five markets goes with the parcel carrier. shipping-service creates labels through its API and receives label events by webhook
- Pallet items go with the pallet carrier. shipping-service sends it a booking file once a day at 16:00, and it sends back no tracking events
- Order, shipping and refund emails go out through the email delivery provider
- Every CS contact sits in the helpdesk, tagged by topic

## Teams and discipline codes

Six teams build the product: Storefront (web and app shopping flows), Checkout, Post-purchase (orders, tracking and returns), Fulfilment (shipping-service and the carrier and warehouse integrations), Merchandising tools (Admin catalog and promotions) and Data. A small design system group sits with Storefront.

Every task and bug carries one discipline code.

| Code | Discipline |
|------|------------|
| `FE` | Front end: web, iOS or Android client work |
| `BE` | Back end: a service, a job or an integration |
| `BO` | Back office: Admin screens and tools |
| `FS` | Full stack: one change across client and service, or a parent task over platform subtasks |
| `DATA` | Tracking plans, events and dashboards |
| `DS` | Design system components and tokens |

Task and bug titles follow `{Discipline} - {Surface} - {Feature code} - {Title}`, where the surface is `Web`, `iOS`, `Android` or `Admin`. Back-end and data work that no single surface owns drops the surface segment. Examples: `FE - Android - CHK - Postcode field rejects spaces`, `BO - Admin - RET - Return reason picker` and `BE - SHIP - Pallet booking file retries`.

Story and epic titles carry no discipline code. A story is `{Persona or platform} - {Area or initiative} - {Feature}` and an epic is `Epic - {Persona or platform} - {Area or initiative}`, for example `Customer - Account - Address book` and `Epic - Customer - Delivery slots`.

## Feature codes

| Code | Area | Main service |
|------|------|--------------|
| `CART` | Cart, mini cart and the cart badge | cart-service |
| `CHK` | Checkout: address, shipping method, payment, confirmation | checkout-service |
| `PROMO` | Automatic promotions, discount codes and the free-shipping banner | promotions-service |
| `SHIP` | Parcel and pallet split, labels, dispatch | shipping-service |
| `TRACK` | Order status and tracking after dispatch | orders-service, shipping-service |
| `RET` | Returns and refunds | orders-service |
| `ACCT` | Sign-in, account, addresses and order history | accounts-service |
| `WISH` | Wishlist on web and in the apps | accounts-service, app storage |

A ticket takes the code of the area where the customer sees the change. Work that spans two areas takes the code of the area that owns the data.

## Platforms and app versions

| Platform | Current version | Released | Supported |
|----------|-----------------|----------|-----------|
| iOS | `4.8.0` | 2026-09-08 | iOS 16 and later |
| Android | `4.8.2` | 2026-09-15 | Android 9 and later |
| Web | Deployed continuously | Several times a day | The two latest versions of each major browser |

Both apps ship on a two-week cycle, on Tuesdays. Android went out as 4.8.0 on 2026-09-08 together with iOS, then took two hotfixes: 4.8.1 on 2026-09-10 for a checkout crash on some devices, and 4.8.2 on 2026-09-15 for push notification taps that opened the home screen. iOS has had no hotfix since 4.8.0. The next app release is 4.9.0.

Within two weeks of a release about 80% of app sessions run the current version. Versions below 4.2 are forced to update. Web events carry the web build number in the same version field the apps use.

## Currencies and locales

| Market | Currency | Locales | Standard shipping | Free shipping threshold |
|--------|----------|---------|-------------------|-------------------------|
| Netherlands | `EUR` | `nl-NL` | `€4.95` | €50 |
| Belgium | EUR | `nl-BE`, `fr-BE` | €4.95 | €50 |
| Germany | EUR | `de-DE` | €4.95 | €50 |
| France | EUR | `fr-FR` | €4.95 | €50 |
| United Kingdom | `GBP` | `en-GB` | `£3.95` | £45 |

Prices include VAT at the market's rate. The storefront formats amounts for the locale, while tickets and internal documents write them in en-GB notation, as this table does. Every market also offers English through the language switcher, which shows en-GB copy with the market's own currency. Belgian customers pick Dutch or French on their first visit.

UK parcels cross a customs border. The parcel carrier clears them on its cross-border service with duties paid by Fernhouse, and they take one to two working days longer than parcels inside the EU.

## Key flows

1. **Browse and add to cart.** A customer adds items from a product page or a product card, and the badge updates at once. Carts of signed-in customers follow them across web and the apps. Guest carts stay on the device for 14 days.
2. **Checkout.** Guest or signed in. The customer gives an address, gets standard shipping (plus a pallet delivery note when a pallet item is in the cart), then pays through the payment provider. Card details are typed in full on every order today, signed in or not. The order exists once the payment is authorised.
3. **Promotions.** Automatic promotions show on product pages and in the cart. A discount code goes in the cart or at checkout. How they combine is set out in the Promotions rules note that Merchandising owns.
4. **Fulfilment.** orders-service sends each paid order to the warehouse system. When picking starts, shipping-service asks the parcel carrier for one label per parcel, and the label arrives by webhook, usually within a minute. Orders paid before the `15:00` cut-off on a working day leave with the 18:00 collection.
5. **After dispatch.** The customer gets a shipping email with the tracking number. The order page on web and in the apps shows `Order placed` until dispatch and `Shipped` after it, with the tracking number, and it never changes after that. Customers who want more go to the parcel carrier's own tracking page.
6. **Returns.** Customers have `30 days` from delivery. There is no self-serve return today. The customer contacts CS, a CS agent creates the return in Admin and emails a return label, the warehouse checks the item, and the agent refunds. CS handles about `1,900` return requests a month, and a refund takes `6 days` on average from the first contact.
7. **Wishlist.** A heart on product cards and product pages. On web the wishlist is saved to the account and needs sign-in. In the apps it is saved on the device and works without an account. Both hold up to 50 items.

## Known constraints

- The parcel carrier takes parcels up to `30 kg` and `120 cm` on the longest side. Anything over either limit goes by the pallet carrier, which has no API and no tracking events
- The parcel carrier's API allows 20 requests per second for the whole account, shared by every call shipping-service makes
- Every label is charged when the carrier creates it, whether or not the parcel ships
- Card data stays with the payment provider. Fernhouse may store a card token, the last four digits and the expiry date, and nothing else
- App changes reach most customers about a week after release, because of store approval and slow updates. A fix that must land the same day has to be server-side
- Admin runs on desktop web only and is not built for phones
- Working days are Monday to Friday minus Dutch public holidays, because the warehouse is in the Netherlands
- Discounts are worked out in promotions-service only. Clients show what it returns and never compute a discount themselves

## Analytics conventions

- Event names follow `object_action` in snake_case, with the verb in the past tense: `product_viewed`, `cart_item_added`, `checkout_started`, `order_placed`, `wishlist_item_added`
- Every event carries `platform` (`web`, `ios` or `android`), `app_version`, `market` (`nl`, `be`, `de`, `fr` or `uk`), `locale` and `customer_type` (`guest` or `account`)
- Money goes in minor units with the currency beside it, as `value_cents` and `currency`
- A new event needs a row in the Data team's tracking plan and a DATA task before any FE task sends it
- Reporting reads from the analytics tool, never from raw event tables
