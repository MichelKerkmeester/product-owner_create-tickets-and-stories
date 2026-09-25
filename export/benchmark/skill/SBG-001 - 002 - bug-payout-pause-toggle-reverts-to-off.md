# Payout pause toggle shows off after refresh while the payout stays paused

### About

---

On the brand wallet, the payout pause toggle shows off after a page refresh even though the payout is still paused. The toggle and the payout state disagree.

| Field           | Value                                        |
| --------------- | -------------------------------------------- |
| Frequency       | Always                                       |
| Severity        | Not provided                                 |
| Platform        | Web                                          |
| Device          | Not provided                                 |
| OS Version      | Not provided                                 |
| Browser         | Chrome                                       |
| Browser Version | 126                                          |

**References:**

**Flows**
- Not provided

---

### Bug

---

**1. Observed Behavior**

---

After the pause is switched on and the page is refreshed, the toggle reverts to off without any action from the brand. The payout keeps showing as paused.
- The toggle shows off while the payout shows paused
- Error messages: Not provided
- The toggle state and the payout state contradict each other, so the brand cannot tell whether the payout is paused

Steps to Reproduce:
1. Open a brand wallet that has a pending payout
2. Switch the payout pause toggle on
3. Refresh the page
4. Observe the toggle. Expected: it stays on. Actual: it shows off while the payout still shows paused

Frequency is Always, per reporter.

Screen recording: Not provided

---

**2. Expected Behavior**

---

The toggle reflects the real payout state after a refresh. It stays on until the brand resumes the payout.
- The toggle and the payout status agree on every load of the wallet
- Only the brand resuming the payout turns the toggle off

Checklist
- [ ] Root cause identified
- [ ] Fix implemented
- [ ] Bug no longer reproducible
- [ ] No regressions introduced

---

### BDD Scenarios

---

**Scenario:** Pause toggle after refresh
- **Given** a brand wallet has a pending payout and the pause toggle is on
- **When** the brand refreshes the page
- **Then** the toggle still shows on until the brand resumes the payout
