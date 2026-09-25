<!-- Mode: bug | Template: Bug Report Template v0.100 | Energy: standard -->
# Payout pause toggle shows off after page refresh

### About

---

On the web brand wallet, the payout pause toggle shows off after a page refresh, while the pending payout still shows as paused. The toggle no longer matches the payout state.

| Field           | Value                                        |
| --------------- | -------------------------------------------- |
| Frequency       | Always (every attempt, per reporter)         |
| Severity        | Not provided                                 |
| Platform        | Web                                          |
| Device          | Not provided                                 |
| OS Version      | Not provided                                 |
| Browser         | Chrome                                       |
| Browser Version | 126                                          |

**References:**

**Flows**
- Not provided

**Components**
- Not provided

---

### Bug

---

**1. Observed Behavior**

---

After the payout is paused and the page is refreshed, the pause toggle shows off. The payout itself still shows as paused.

- The toggle shows off after the refresh
- The payout status still shows paused after the refresh
- No error message was reported
- The toggle and the payout status disagree, so the brand cannot tell from the toggle that the payout is paused

Steps to Reproduce:
1. Open a brand wallet that has a pending payout
2. Switch the payout pause toggle on
3. Refresh the page
4. Observe that the toggle shows off while the payout still shows paused

Screen recording: Not provided

Screenshots: Not provided

---

**2. Expected Behavior**

---

After a refresh, the toggle stays on while the payout is paused, and it stays on until the brand resumes the payout.

- The toggle and the payout status always show the same state
- Previous working behavior: Not provided
- Design specifications: Not provided

Checklist
- [ ] Root cause identified
- [ ] Fix implemented
- [ ] Bug no longer reproducible
- [ ] No regressions introduced

---

### BDD Scenarios

---

**Scenario:** Pause toggle keeps its state after a refresh
- **Given** a brand wallet with a pending payout that is paused with the toggle on
- **When** the brand refreshes the page
- **Then** the toggle shows on and the payout shows paused until the brand resumes the payout
