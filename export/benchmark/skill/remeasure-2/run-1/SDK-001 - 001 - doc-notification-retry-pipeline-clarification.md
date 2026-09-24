# Doc intake: notification retry pipeline

Before I draft, please paste the engineering notes and confirm the rest of the intake in the same reply:

1. Paste the notes: the engineering notes are the source material and the document cannot be drafted without them
2. Status: do the notes describe current production behavior, approved-but-unshipped direction, proposals, retired material, or a mix? If they mix, say which parts are which
3. Shape: support teams usually need either a troubleshooting/runbook guide (ordered steps: what to check when a retry fails) or a behavior reference (how the pipeline works: states, rules, outcomes). Which fits how the support team will actually use it, or should I judge from the notes once they arrive?
4. Scope: anything to leave out, for example implementation internals the support team never touches, or specific topics like monitoring, credentials or rate limits
5. Depth: how technical should it be, given the support team, since that decides whether code-level identifiers, queues and configuration keys are explained or kept

I will draft once your reply clears these. One question, one answer, then the document.
