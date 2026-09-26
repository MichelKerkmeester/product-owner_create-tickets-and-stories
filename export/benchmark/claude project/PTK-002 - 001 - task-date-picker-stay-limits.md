<!-- Mode: Task | Template: Task Templates v0.102 -->
# FE - Guest app - SRCH - Date picker stay limits

### About

---

The Guest app date picker accepts any range, but `search-service` turns down anything over 30 nights with only `Something went wrong`. Guest Support logged 23 chats about it in August. The picker should block an unsearchable range before Search, and say why.

It covers iOS, Android and web, search form and property page. The design frames are final, so raise any mismatch with Ines in the Search squad channel before working around it. Flexible dates, weekend presets, per-night calendar prices and tracking changes are out, and date selection isn't tracked today and gets no events.

**References**

---

Flows

- `Date picker / Stay limits` frame in the Guest app search design file

### Requirements

---

### **Limits**

---

1.  **Where the limits come from**

---

No limit is hard-coded, so changes need no app release.

**Checklist**

- [ ] The 30-night maximum and the 365-day check-in window come from `search-service` config
- [ ] On the property page, the minimum stay comes with the property details, set in Partner Hub from 1 to 14 nights
- [ ] Helper text fills `{max}` and `{n}` from these values

2.  **Which days can be picked**

---

**Checklist**

- [ ] Past days are disabled, and today can be check-in
- [ ] Days more than 365 days ahead show but are disabled as check-in
- [ ] Check-out may land more than 365 days ahead
- [ ] A stay is at least 1 night and at most 30 nights
- [ ] On the property page, a stay is also at least the minimum stay

### **Picker states**

---

3.  **Button and range states**

---

**Checklist**

- [ ] With nothing picked, the disabled button reads `Select check-in date` (`datepicker.cta.checkin`)
- [ ] With check-in picked, days making the stay too short or over 30 nights turn grey, and the disabled button reads `Select check-out date` (`datepicker.cta.checkout`)
- [ ] With a valid range, the range is highlighted, the nights count sits under it (`datepicker.nights`) and the button reads `Show prices` (`datepicker.cta.show_prices`)
- [ ] A 30-night range across two months stays highlighted across the month break

4.  **Helper text on a grey day**

---

A grey day stays tappable, because the tap shows why it is grey.

**Checklist**

- [ ] Tapping a grey day past 30 nights selects nothing and shows `Stays can be up to 30 nights` (`datepicker.helper.max_stay`)
- [ ] On the property page, tapping a day inside the minimum stay selects nothing and shows `This property has a 3-night minimum` (`datepicker.helper.min_stay`) with the property's number
- [ ] The helper text shows under the calendar, never covers it and stays until a valid day is picked
- [ ] Screen readers announce a grey day as unavailable, then its helper text

5.  **Changing and reopening dates**

---

**Checklist**

- [ ] With check-in picked, tapping an earlier day makes it check-in, and the button returns to `Select check-out date`
- [ ] Reopening with dates from an earlier search shows them picked, with `Show prices`
- [ ] Earlier dates that break a limit, like a 45-night search saved before this change, are cleared and the picker opens empty

### **Platforms**

---

6.  **Layout and locale**

---

**Checklist**

- [ ] iOS and Android use the design system calendar, never the system date picker
- [ ] Desktop web shows two months side by side
- [ ] Mobile web and the apps show one month at a time, scrolling vertically
- [ ] The week starts on Monday, or on Sunday in `en-US`
- [ ] All six `datepicker` keys are translated, falling back to `en-GB` for a missing string
