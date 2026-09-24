# Payout pause toggle

### About

---

Brands can pause a pending payout for 24 hours, which buys a window to hold the money while a question about the payout is settled. The pause requires a reason, so every paused payout carries a record of why it stopped. Creators see the pause too, because a payout that quietly stops moving otherwise looks like a failure.

This task delivers three things: the pause toggle, the required reason and the creator banner.

### Requirements

---

1.  **Pause toggle on pending payouts**

---

A brand can pause a payout that is pending, and the payout stays paused for 24 hours. While the pause is active, the payout shows its paused state so nobody has to guess why the money is not moving.

**Checklist**

- [ ] A brand can pause a payout that is in the pending state
- [ ] The payout stays paused for 24 hours after the brand pauses it
- [ ] While paused, the payout shows its paused state
- [ ] Pause is only available for payouts in the pending state

---

2.  **Required reason**

---

Pausing a payout requires a reason from the brand. The reason is required, not optional, so every paused payout ends up with a why attached.

**Checklist**

- [ ] A payout cannot be paused without a reason
- [ ] The reason the brand entered is saved with the payout

---

3.  **Creator banner**

---

A creator whose payout is paused sees a banner, so they know the payout is held rather than lost. The banner disappears when the payout is no longer paused.

**Checklist**

- [ ] A creator sees a banner while their payout is paused
- [ ] The banner no longer shows once the payout is no longer paused

