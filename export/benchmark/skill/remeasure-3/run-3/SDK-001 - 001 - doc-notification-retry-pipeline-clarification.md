# Clarification: notification retry pipeline documentation

Before I draft, please confirm:

- **Engineering notes:** paste the notes, and say whether they are the only source or whether another source (code, a design doc, a teammate's writeup) governs where they are silent
- **Authority and status:** who owns these notes, and whether they describe current production behavior, approved direction, a proposal, retired material or a mix
- **Shape:** a behavior reference (how retry states, timing and outcomes work, so support can predict what happens), a troubleshooting runbook (ordered steps support follows when deliveries fail), or something else
- **Scope:** what stays out, if anything, such as the broader notification system, delivery channels or configuration
- **Depth:** how much technical detail support needs, enough to explain outcomes to customers, or deeper, including identifiers and internals
