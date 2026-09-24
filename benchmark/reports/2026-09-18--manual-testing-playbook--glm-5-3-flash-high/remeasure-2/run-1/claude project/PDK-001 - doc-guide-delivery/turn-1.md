**Deliverable Block** — clarification, Doc lane

```markdown
I'll document how the notification retry pipeline works for the support team. Before I draft, I need the unresolved decisions below in one response, together with the engineering notes:

**Source set & authority:** Paste the engineering notes. Are they the single governing source for this document, or do other materials (incident retros, design docs, runbooks, messages) also speak to the pipeline? If more than one, which controls any conflict between them?

**Document status:** Do the notes describe current production behavior, approved direction, a proposal, or a mix? Flag anything the notes themselves mark draft, legacy, proposed or unverified.

**Scope & exclusions:** What should the document cover and what should it leave out? For example: retries only, or also initial delivery,DLQ/dead-letter handling and configuration? Should internals the support team never touches be excluded?

**Shape:** Your wording suggests a behavior reference (states, retry rules, timing, boundaries and outcomes a support agent can use to predict what the pipeline will do). If the support team instead needs to follow an ordered troubleshooting procedure, say so and it becomes a guide. I will otherwise infer the shape once I can read the notes against this question.

**Detail depth & gaps:** How technical should it be for this audience (state names, identifiers, error codes, no code)? And which behavior in the notes, if any, is explicitly unresolved, contradictory or not yet verified?
```

---

Export-equivalent path: `export/001 - doc-notification-retry-pipeline-clarification.md`

Purpose (how the notification retry pipeline works) and audience (the support team) are settled, so the question only covers what the notes must still decide: source authority, status, scope, shape and depth. Answer it and paste the notes in the same reply, and I draft the document next, as `export/002`.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: the `Status:`-shaped wording in the status question is the sanctioned status-label shape, and the question's bullets are Interactive intake, which uses the dash grammar rather than the Doc contract.