Saved as an Epic: `export/001 - Epic-self-serve-returns.md`

Verified: read-back succeeded; 127 lines
HVR self-scan: 1 hard blockers. Fixed: none in the saved draft. Kept with reason: `TBD...` (fixed house placeholder: the Estimation slot and the External dependencies date, both inside the Delivery section, where Story Mode 6.9 requires an undated date to stay open).

Quality summary: Quick energy. All six dimensions clear their floors. The figures (1,900 requests a month, 6-day refunds, the 30-day window, the €200 limit) and the order-page behaviour trace to `context/fernhouse-context.md`, which is unchanged.

This Epic adds a Delivery section, which you did not ask for, because the store review of the app releases is an undated external constraint. I also added the following, so strike any you don't want:
- The external store-review dependency, from the context's app-release note.
- Two Rabbit holes from the context: whether the €200 CS refund limit applies to refunds that skip a CS agent, and charges on labels that never ship.
- Criterion 5, which turns your 60% goal into a measurable outcome.
- The Scope grouping, and the wording of the Problem and Goal.

Two points need a decision before the child stories are drafted. The context says the order page status never changes after dispatch, so the return status on that page changes what customers see after shipment. Also, the brief does not say whether the €200 per-order CS limit applies to refunds issued after the warehouse check, or who decides. I did not resolve either point.