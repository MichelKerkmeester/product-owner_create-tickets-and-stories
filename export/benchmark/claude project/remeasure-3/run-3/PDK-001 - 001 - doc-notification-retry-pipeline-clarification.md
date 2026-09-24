# Doc clarification: notification retry pipeline

I'll create the document. Purpose and audience are already fixed: a reference explaining how the notification retry pipeline behaves, written for the support team. Before drafting, I need the decisions below in one response:

**Source set:** Paste the engineering notes. They are the only source so far, and nothing gets drafted before they arrive

**Authority:** Do the notes govern every claim, or does another document, a dashboard, a teammate or your own judgement win where they disagree? If the notes contradict themselves, name the claim that wins

**Status:** Should the result read as current behavior, approved direction, proposal, retired material, or a mix? Notes often mix statuses. I will keep each claim's own label, so flag which parts carry which

**Scope:** What belongs in the document, and what stays out? Incident history, internal identifiers, queue infrastructure and unreleased retry changes are the usual exclusion candidates

**Technical depth:** How much implementation HOW does support need? Three levels, pick one:

- Behavior only: what happens, when it happens, what the customer sees and what triggers a retry
- Behavior plus troubleshooting: the level above, plus what support can check and the symptoms worth recognizing
- Full implementation detail: identifiers, retry counts, timings, queue names, code

**Shape:** The wording suggests a behavior reference, meaning states, rules, outcomes and boundaries a reader can predict. Lock that in with a one-word answer, or let the notes decide once they arrive

Answer these together with the pasted notes and I draft.

* * *
