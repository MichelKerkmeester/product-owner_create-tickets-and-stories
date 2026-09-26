# FE - Guest app - SRCH - Date picker stay limits

### About

---

Today the Guest app date picker lets a guest select a range longer than 30 nights. search-service turns those stays down, so the guest only finds out after tapping Search, and then sees a generic "Something went wrong". Guest Support logged 23 chats about it in August, mostly about long work stays.

This task makes the picker block any range that search can't run before the guest taps Search, and tell them why. It covers iOS, Android and web together. The Search squad takes it into the 8.13.0 train. search-service is unchanged, and its own 30-night check stays in place as the backstop.

Not in this task: flexible dates, weekend presets, prices per night inside the calendar and any tracking change. Date selection isn't tracked today, and this work adds no tracking.

**References**

---

Page

- `Date picker / Stay limits` frame in the Guest app search design file, with Ines's handover notes pinned to it (2026-09-14). The frames are final, and any mismatch goes to Ines in the Search squad channel before anyone works around it

### Requirements

---

### **Limits**

---

1.  **Stay length and check-in window**

---

The picker applies the same limits search-service does, so a range the guest can select is a range search accepts. Check-out isn't bound by the 365-day window. Only check-in is.

**Checklist**

- [ ] A stay is at least 1 night, so check-in and check-out can't be the same day
- [ ] A stay is at most 30 nights
- [ ] Check-in is at most 365 days from today. Later days still show in the calendar but are disabled
- [ ] Past days are disabled, and today can be picked as check-in
- [ ] Check-out can land past the 365-day mark
- [ ] On the property page, the picker also applies the property's minimum stay, which partners set in Partner Hub from 1 to 14 nights

---

2.  **Where the limit values come from**

---

The limits change in config or in Partner Hub, not in an app release. If the apps hard-coded a limit, it could stop matching search.

**Checklist**

- [ ] The 30-night maximum and the 365-day window come from search-service config
- [ ] The property's minimum stay comes with the property details
- [ ] No app or web client hard-codes any of the three values

---

### **Picker states**

---

3.  **Button and range states**

---

The button at the bottom of the picker tells the guest the next step, and it only becomes active once the range is valid.

**Checklist**

- [ ] With nothing picked, the button reads `Select check-in date` and is disabled
- [ ] Once check-in is picked, days that would make the stay too short or longer than 30 nights turn grey. The button reads `Select check-out date` and stays disabled
- [ ] With a valid range, the range is highlighted, the nights count sits under it and the button reads `Show prices`
- [ ] The nights count uses `{count} night` for 1 night and `{count} nights` for more

---

4.  **Tapping a grey day**

---

A grey day can still be tapped. The helper text it shows is the only way the guest learns why the day is grey.

**Checklist**

- [ ] Tapping a grey day past the 30-night limit selects nothing and shows `Stays can be up to 30 nights` under the calendar
- [ ] On the property page, tapping a day inside the property's minimum stay selects nothing and shows the helper text with that property's number, such as `This property has a 3-night minimum`
- [ ] The helper text stays until the guest picks a valid day
- [ ] The helper text never covers the calendar

**User Story**

- **Given:** a guest has picked a check-in date
- **When:** they tap a grey day 35 nights later
- **Then:** nothing is selected and `Stays can be up to 30 nights` shows under the calendar

---

5.  **Copy keys**

---

Hana signed the copy off on 2026-09-11 and has sent all six keys for translation. The frames show real numbers where the keys hold placeholders.

| Key | en-GB copy | Where |
| --- | --- | --- |
| `datepicker.cta.checkin` | Select check-in date | Button, nothing picked |
| `datepicker.cta.checkout` | Select check-out date | Button, check-in picked |
| `datepicker.cta.show_prices` | Show prices | Button, valid range |
| `datepicker.helper.max_stay` | Stays can be up to {max} nights | Helper text, past the 30-night limit |
| `datepicker.helper.min_stay` | This property has a {n}-night minimum | Helper text, inside the property minimum |
| `datepicker.nights` | {count} night, {count} nights | Under the range |

**Checklist**

- [ ] Every picker string comes from these six keys
- [ ] `{max}` and `{n}` are filled from the limit values, not written into the string

---

### **Edge cases**

---

6.  **Dates already set and re-picking**

---

Dates from an earlier search can break the new limits, for example a saved 45-night search from before this change. The picker must never open with a range that search would turn down.

**Checklist**

- [ ] Opening the picker with valid dates from an earlier search shows the range as picked, with `Show prices` active
- [ ] Opening the picker with earlier dates that break a limit clears them and opens with nothing picked
- [ ] After check-in is picked, tapping a day before it makes that day the new check-in, and the button goes back to `Select check-out date`
- [ ] A 30-night range across two months keeps the highlight across the month break

---

7.  **Screen readers**

---

**Checklist**

- [ ] Screen readers announce a grey day as unavailable, followed by the same helper text a sighted guest sees when tapping it

---

### **Platforms and QA**

---

8.  **Platform layout**

---

**Checklist**

- [ ] iOS and Android use the design system calendar component, never the system date picker
- [ ] Web on desktop shows two months side by side
- [ ] Mobile web and the apps show one month at a time and scroll vertically
- [ ] The week starts on Monday, except in `en-US`, where it starts on Sunday

---

9.  **QA sign-off**

---

QA signs the task off on iOS, Android and web, in both `en-GB` and `en-US`. The two locales start the week on different days, so each one needs its own check.

**Checklist**

- [ ] Every requirement above passes on iOS, Android and web in `en-GB`
- [ ] Every requirement above passes on iOS, Android and web in `en-US`
- [ ] The week start, the 30-night grey days and the month-break highlight are checked in both locales
