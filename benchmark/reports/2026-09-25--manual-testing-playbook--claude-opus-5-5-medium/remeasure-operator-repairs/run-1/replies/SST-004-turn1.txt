I haven't drafted the Story yet. `$story` requires me to ask its intake question first, and the sources leave several decisions open that I shouldn't guess. I saved those questions as a single clarification file.

Path: `export/001 - Story-order-tracking-clarification.md`
Verified: read-back succeeded; 27 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

**Artifact kind:** Story, with its tasks in one folder. The folder will be `export/002 - Story-order-tracking/` once you answer.

**What I need from you:**
1. **Task split:** confirm the six tasks from the brief. I've proposed titles in Fernhouse's naming pattern and put the DATA task before the FE tasks, because the company context requires a DATA task before any FE task sends an event.
2. **Carrier link:** the DATA task counts taps on a carrier link, but the brief never puts one on the order page. Is there one?
3. **Parcel points:** Yusuf's notes say a `DL` event arrives when the parcel is dropped at a parcel point, before the customer collects it. Should that still show `Delivered`, and does the 90-day tracking retention period start then?
4. **Delivery failed:**
   - What should customers see for `ADDRESS_PROBLEM`, `DAMAGED` and `REFUSED`? The carrier only retries after `NOT_HOME`.
   - Should the page show the reason? That's Hamid's open question: has he decided, or should the Story mark it as open?
5. **Missed events:** a dropped event is lost for good and there's no tracking history to fall back on. A missed `DL` would leave a parcel on its last status indefinitely. Accept that as a known limitation, or require a fallback?
6. **Web design:** only the apps have a mock so far. Should the Web task follow the app mock or wait for the web layout?
7. **Mixed orders:** how should an order with both parcel and pallet items look?
8. **Guest orders:** should guest orders get tracking too, or only signed-in customers?

Once you reply, I'll write the Story and its task files in one folder.