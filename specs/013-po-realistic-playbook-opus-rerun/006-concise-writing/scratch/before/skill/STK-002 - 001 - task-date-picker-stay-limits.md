# FE - Guest app - SRCH - Date picker stay limits

### About

---

Today the Guest app date picker lets a guest select any range. search-service then turns down anything over 30 nights, and the guest sees a generic "Something went wrong" after tapping Search. Guest Support logged 23 chats about it in August, mostly from guests booking long stays for work.

This task makes the date picker stop a range it can't search before the guest taps Search, and tell the guest why. It is one FE task for the Guest app on iOS, Android and web together, on the search form and on the property page. The Search squad takes it into the 8.13.0 train.

The frames are final and the copy was signed off by Hana on 2026-09-11. If the build can't match the frame, raise it with Ines in the Search squad channel before working around it.

Not in this task: flexible dates, weekend presets, prices per night inside the calendar and any tracking change. Date selection isn't tracked today and this task adds no events. search-service stays as it is, because its own 30-night check remains the backstop behind the picker.

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

These limits apply everywhere the date picker opens. They match what search-service accepts, so any range the picker allows can be searched.

**Checklist**

- [ ] Check-in and check-out can't be the same day, so a stay is at least 1 night
- [ ] A stay is at most 30 nights, the same limit search-service applies
- [ ] Past days are disabled, and today can be picked as check-in
- [ ] Check-in can be at most 365 days from today. Later days show in the calendar but are disabled
- [ ] Check-out may land past the 365-day mark, because only check-in is limited
- [ ] The 30-night maximum and the 365-day window come from search-service config. No platform hard-codes them

2.  **Property minimum stay**

---

On the property page the picker also applies the property's minimum stay. Partners set it in Partner Hub, anywhere from 1 night to 14 nights.

**Checklist**

- [ ] On the property page, the picker applies the property's minimum stay on top of the limits in group 1
- [ ] The property minimum applies on the property page only
- [ ] The minimum comes with the property details and isn't hard-coded
- [ ] Any minimum from 1 night to 14 nights works

---

### **States and copy**

---

3.  **Picker states**

---

The frame shows three states for picking a range. The button at the bottom only becomes active once the range is valid.

**Checklist**

- [ ] State 1, nothing picked: the button reads `Select check-in date` and is disabled
- [ ] State 2, check-in picked: days that would make the stay too short or longer than 30 nights turn grey, and the button reads `Select check-out date` and stays disabled
- [ ] State 3, valid range picked: the range is highlighted, the nights count sits under it and the button reads `Show prices`
- [ ] The nights count matches the Roamstay stay definition, so check-in on a Monday and check-out on a Thursday shows 3 nights

4.  **Helper text on grey days**

---

A grey day can still be tapped. The tap selects nothing and shows helper text under the calendar, which is the only way the guest learns why the day is grey.

**Checklist**

- [ ] State 4: tapping a grey day past the 30-night limit selects nothing and shows `Stays can be up to 30 nights`
- [ ] State 5, property page only: tapping a day inside the property's minimum stay selects nothing and shows the property's own number, for example `This property has a 3-night minimum`
- [ ] The helper text stays until the guest picks a valid day
- [ ] The helper text never covers the calendar

5.  **Copy keys**

---

Hana has sent all six keys for translation. The numbers in the helper text are placeholders filled from the live limits, so the frames' `30` and `3` are examples of the rendered copy rather than fixed values.

| Key | en-GB copy | Where |
|-----|------------|-------|
| `datepicker.cta.checkin` | Select check-in date | Button, state 1 |
| `datepicker.cta.checkout` | Select check-out date | Button, state 2 |
| `datepicker.cta.show_prices` | Show prices | Button, state 3 |
| `datepicker.helper.max_stay` | Stays can be up to {max} nights | Helper text, state 4 |
| `datepicker.helper.min_stay` | This property has a {n}-night minimum | Helper text, state 5 |
| `datepicker.nights` | {count} night, {count} nights | Under the range |

**Checklist**

- [ ] All six keys are used as listed, with no hard-coded strings
- [ ] `{max}` comes from the search-service maximum and `{n}` from the property's minimum stay
- [ ] `datepicker.nights` uses the singular form for 1 night and the plural form otherwise
- [ ] A missing translation falls back to `en-GB`
- [ ] The button copy fits in `de-DE`, where strings run about 30% longer than English

---

### **Edge cases and accessibility**

---

6.  **Changing and restoring dates**

---

These cases were walked through with Oskar and Hana and have a defined outcome.

**Checklist**

- [ ] With check-in picked, tapping a day before it makes that day the new check-in, and the button goes back to `Select check-out date`
- [ ] Opening the picker with dates from an earlier search shows the range as picked, in state 3
- [ ] Dates from an earlier search that break a limit are cleared and the picker opens in state 1, for example a saved 45-night search from before this change
- [ ] A 30-night range across two months keeps the highlight across the month break

7.  **Screen readers**

---

A screen reader user gets the same explanation a sighted guest gets from the helper text.

**Checklist**

- [ ] Screen readers announce a grey day as unavailable, followed by the same helper text as states 4 and 5

---

### **Platforms**

---

8.  **Calendar layout per platform**

---

The number of months on screen depends on the platform and screen size.

**Checklist**

- [ ] iOS and Android use the design system calendar component, never the system date picker
- [ ] Web on desktop shows two months side by side
- [ ] Mobile web and the apps show one month at a time and scroll vertically
- [ ] The week starts on Monday, except in `en-US`, where it starts on Sunday

---

### **Sign-off**

---

9.  **QA sign-off**

---

QA signs the task off on each platform and locale separately, so a pass on one platform doesn't stand in for another.

**Checklist**

- [ ] QA signs off groups 1 to 8 on iOS in `en-GB` and in `en-US`
- [ ] QA signs off groups 1 to 8 on Android in `en-GB` and in `en-US`
- [ ] QA signs off groups 1 to 8 on web in `en-GB` and in `en-US`, on desktop and on mobile web
