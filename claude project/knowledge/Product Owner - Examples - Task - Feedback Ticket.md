# Product Owner - Examples - Task - Feedback Ticket

Instantiates Task Templates section 6, Feedback Ticket. Shows one app's UI/UX review round grouped by screen, a Code and Figma screenshot pair and a Logic-style item with steps.

---

# MD - Booking Flow MVP - Feedback #1 - Guest: UI/UX

## About

---

Feedback from Round #1 of product review on Booking Flow MVP (Guest).
This feedback is release blocking.

#### **References**

---

**Flows**

---

*   [Guest booking flow](figma-url)

###   

## Feedback

---

### **Booking: Date Picker**

---

1\. **Today state**

---

Today renders as an outlined ring instead of the filled current state in Figma.

**Checklist**

- [] Set today's `btn | date picker` to the `Enabled | Current` state
- [] Use design system units in the date picker instead of `px` values
- [] Show time on a 24-hour clock

Code
![](https://cdn.example.com/review/date-picker-built.png)

[Figma](figma-url)
![](https://cdn.example.com/review/date-picker-figma.png)

2\. **Calendar footer**

---

**Checklist**

- [] Fill the last calendar row with dates from the next month
- [] Remove the `(optional)` text from the time label

###   

### **Booking: Summary**

---

3\. **Price breakdown after a date change**

---

**What happened?**

1. I picked two nights and opened the summary
2. I went back and changed the stay to three nights
3. The summary still showed the two-night price until I refreshed the page

**Checklist**

- [] Changing the dates updates the price breakdown without a page refresh
- [] Can the summary show a loading state while the new price is fetched?

Recording
[https://cdn.example.com/review/summary-price.mov](https://cdn.example.com/review/summary-price.mov)
