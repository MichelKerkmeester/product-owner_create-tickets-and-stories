# FE - Guest app - SRCH - Date picker stay limits

### About

---

The Guest app date picker accepts any range, but search-service rejects stays over 30 nights, and the guest sees a generic "Something went wrong" after Search. Guest Support logged 23 chats about it in August. The picker should block such ranges before Search, and say why.

One FE task covers iOS, Android and web, search form and property page, in the Search squad's 8.13.0 train. search-service doesn't change, because its own 30-night check stays the backstop. Flexible dates, weekend presets, per-night calendar prices and tracking changes are out, and date selection isn't tracked today and gets no events.

The frames are final and Hana signed off the copy on 2026-09-11, so raise any mismatch with Ines in the Search squad channel before working around it.

**References**

---

Page

- `Date picker / Stay limits` frame in the Guest app search design file, with Ines's handover notes pinned to it

Components

- Calendar component from the design system, used on iOS and Android

### Requirements

---

### **Limits**

---

1.  **Stay length and check-in window**

---

The limits match search-service, so any allowed range can be searched.

**Checklist**

- [ ] A stay is 1 to 30 nights, so check-in and check-out can't be the same day
- [ ] Past days are disabled, and today can be check-in
- [ ] Check-in is at most 365 days from today, and later days show but are disabled
- [ ] Check-out may land past the 365-day mark
- [ ] The 30-night maximum and the 365-day window come from search-service config, never hard-coded

2.  **Property minimum stay**

---

Partners set the minimum stay in Partner Hub.

**Checklist**

- [ ] The picker applies the property's minimum stay on top of group 1, on the property page only
- [ ] The minimum, 1 to 14 nights, comes with the property details and isn't hard-coded

---

### **States and copy**

---

3.  **Picker states**

---

**Checklist**

- [ ] State 1, nothing picked: the disabled button reads `Select check-in date`
- [ ] State 2, check-in picked: days making the stay too short or over 30 nights turn grey, and the disabled button reads `Select check-out date`
- [ ] State 3, valid range picked: the range is highlighted, the nights count sits under it and the button reads `Show prices`
- [ ] Nights follow the Roamstay stay definition, so Monday to Thursday shows 3 nights

4.  **Helper text on grey days**

---

A grey day stays tappable, because its helper text under the calendar says why it is grey.

**Checklist**

- [ ] State 4: tapping a grey day past the 30-night limit selects nothing and shows `Stays can be up to 30 nights`
- [ ] State 5, property page only: tapping a day inside the minimum stay selects nothing and shows the property's number, like `This property has a 3-night minimum`
- [ ] The helper text stays until a valid day is picked and never covers the calendar

5.  **Copy keys**

---

Hana has sent all six keys for translation. The frames' `30` and `3` are examples, since helper numbers fill from the live limits.

| Key | en-GB copy | Where |
|-----|------------|-------|
| `datepicker.cta.checkin` | Select check-in date | Button, state 1 |
| `datepicker.cta.checkout` | Select check-out date | Button, state 2 |
| `datepicker.cta.show_prices` | Show prices | Button, state 3 |
| `datepicker.helper.max_stay` | Stays can be up to {max} nights | Helper text, state 4 |
| `datepicker.helper.min_stay` | This property has a {n}-night minimum | Helper text, state 5 |
| `datepicker.nights` | {count} night, {count} nights | Under the range |

**Checklist**

- [ ] All six keys are used, with no hard-coded strings
- [ ] `{max}` comes from the search-service maximum and `{n}` from the property's minimum stay
- [ ] `datepicker.nights` is singular for 1 night and plural otherwise
- [ ] A missing translation falls back to `en-GB`
- [ ] The button copy fits in `de-DE`, where strings run about 30% longer than English

---

### **Edge cases and accessibility**

---

6.  **Changing and restoring dates**

---

Oskar and Hana defined these outcomes.

**Checklist**

- [ ] With check-in picked, tapping an earlier day makes it the new check-in, and the button returns to `Select check-out date`
- [ ] Reopening with dates from an earlier search shows the range picked, in state 3
- [ ] Saved dates breaking a limit, such as a 45-night search from before this change, are cleared, opening in state 1
- [ ] A 30-night range across two months stays highlighted across the month break

7.  **Screen readers**

---

**Checklist**

- [ ] Screen readers announce a grey day as unavailable, then the helper text of states 4 and 5

---

### **Platforms**

---

8.  **Calendar layout per platform**

---

**Checklist**

- [ ] iOS and Android use the design system calendar component, never the system date picker
- [ ] Desktop web shows two months side by side
- [ ] Mobile web and the apps show one month at a time, scrolling vertically
- [ ] The week starts on Monday, or on Sunday in `en-US`

---

### **Sign-off**

---

9.  **QA sign-off**

---

**Checklist**

- [ ] QA signs off groups 1 to 8 on iOS, Android and web, each in `en-GB` and `en-US`, with web on desktop and mobile
