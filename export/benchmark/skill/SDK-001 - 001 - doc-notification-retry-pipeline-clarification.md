# Notification retry pipeline doc: intake question

Before I draft, please send the engineering notes together with the answers to these questions, so one round settles everything:

*   **Source set:** Which notes, files or links should the document draw on, and is anything meant to be excluded?
*   **Authority:** If the notes disagree with each other or with other material, which source governs, and for which part of the pipeline?
*   **Status:** Do the notes describe current behavior, approved direction, a proposal, retired material or a mix? If a mix, which parts are which?
*   **Shape:** Should the support team get a behavior reference (how the pipeline moves a notification through states and retries, so they can predict an outcome), a troubleshooting guide or runbook (steps to follow when a notification does not arrive), a catalog (lookup of retry rules, error codes or states) or a narrative overview? The wording of your request suggests a behavior reference, but I will not choose until you confirm or the notes make the support team's use clear.
*   **Scope and depth:** Which questions must the support team be able to answer from it (for example how many retries happen, how long the gaps are, when a notification is dropped, what a customer sees) and how much engineering detail such as queue names, config keys or code identifiers belongs in it versus plain-language behavior?
*   **Subjects the notes may not cover:** If the notes are silent on something support will need, such as retry limits or dead-letter handling, should I leave it marked unknown or ask you for a source?
