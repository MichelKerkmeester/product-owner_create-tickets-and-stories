---
title: Deep Research Strategy - Interactive FigJam Intake
description: Runtime strategy for the deepseek fan-out lineage researching an interactive intake loop for sk-product-owner and sk-create-figjam.
importance_tier: normal
contextType: planning
---

# Deep Research Strategy - Interactive FigJam Intake

## 1. OVERVIEW

### Purpose

Track the fan-out lineage that designs an interactive intake for `sk-product-owner` and `sk-create-figjam`: a confidence model, a stop rule and round cap, a question bank, a sparring step and the kernel parity that carries it.

### Usage

- **Per iteration:** the executor reads Next Focus, writes one iteration narrative, one delta file, hands one canonical iteration record to the append gateway, then runs the reducer.

---

## 2. TOPIC
Design an interactive intake for both sk-product-owner and sk-create-figjam that keeps asking the user questions until it is confident it understands the feature well enough to produce the FigJam output, and that spars with the user on what the board should convey and how it should look. Study the current behaviour first: sk-product-owner's Interactive Mode and its question templates, the router's clarification path, sk-create-figjam's gate and its ambiguity recovery, and the kernel's Interactive Mode. Then research: a confidence model with named facts the intake must know before drawing (the reader, the question the board answers, scope, entry and exit, actors, decisions, states, sources) and a threshold, a stop rule and a round cap so it never interrogates without end, how to ask few high-value questions per round, how to propose rather than only ask (a draft outline, two alternative framings, a Mermaid sketch before the board), how to challenge a brief that asks for too much or the wrong diagram type, how to record answers so later turns build on them, how this works when the user says just do it, how energy levels such as Quick and Standard change it, and how the Claude Project kernel would carry it.

---

<!-- ANCHOR:key-questions -->
## 3. KEY QUESTIONS (remaining)
- [x] What do sk-product-owner Interactive Mode, the router clarification path, sk-create-figjam's gate and the kernel do today, and where does the flow stop short of a board?
- [x] Which named facts must a board intake establish before drawing, and what confidence model, threshold and stop rule make it confident enough to draw?
- [x] How should the intake spar with the user through proposals - a draft outline, two alternative framings, a Mermaid sketch - instead of only asking questions?
- [x] How should intake answers persist across turns, and what changes when the user says just do it or selects Quick energy?
- [x] How should the intake challenge an over-broad brief or the wrong diagram type, and how does the Claude Project kernel carry the loop?

<!-- /ANCHOR:key-questions -->

---

## 4. NON-GOALS
- Redesigning the Figma write routes, the checker rules, the palette or the read-back contract; earlier research already landed those.
- Re-proposing any change already implemented from phase 009, 016 or their follow-up phases.
- Opening `AI Systems/Product Context`, any screenshot or image file, any figma.com board URL or any containment folder, and quoting Barter product flows.
- Implementing code changes; this lineage reports research and ranked changes only.

---

## 5. STOP CONDITIONS
- Five iterations complete, then synthesis. The stop policy is `max-iterations`; convergence is off and its ratio is telemetry only.
- Every iteration must either widen the sources or deepen a named earlier iteration.

---

<!-- ANCHOR:answered-questions -->
## 6. ANSWERED QUESTIONS
- What do sk-product-owner Interactive Mode, the router clarification path, sk-create-figjam's gate and the kernel do today, and where does the flow stop short of a board?
- Which named facts must a board intake establish before drawing, and what confidence model, threshold and stop rule make it confident enough to draw?
- How should the intake spar with the user through proposals - a draft outline, two alternative framings, a Mermaid sketch - instead of only asking questions?
- How should intake answers persist across turns, and what changes when the user says just do it or selects Quick energy?
- How should the intake challenge an over-broad brief or the wrong diagram type, and how does the Claude Project kernel carry the loop?

<!-- /ANCHOR:answered-questions -->

---

<!-- MACHINE-OWNED: START -->
<!-- ANCHOR:what-worked -->
## 7. WHAT WORKED
- reading the contract files in the order a request actually travels (router band, Interactive Mode state machine, Flow Mode workflow, gate, kernel) exposed the structural gap. The one-question rule is not an oversight in one file; it is stated in five places, so a loop needs an explicit exception. (iteration 1)
- reading the corpus's only multi-round skill (project plan) was the highest-yield move, because it shows rounds, batching, proposals, stored answers and skips in one working flow. (iteration 2)
- the coverage-guarantee method supplied the two missing concepts in one document — a named-dimension completeness contract and the assumed-versus-unasked distinction. Both are about the record, not the conversation, which is why they translate to a checklist the packet can hold. (iteration 3)
- reading `sk-prompt` as a sibling skill rather than as part of the topic paid off, because it already solved both problems this iteration needed — energy-scaled rounds and a never-ask path with flagged assumptions. (iteration 4)
- checking the hub and ROUTER leaf loading settled the placement question before any design work, and it changed the answer: the loop cannot live in Interactive Mode. (iteration 5)

<!-- /ANCHOR:what-worked -->

---

<!-- ANCHOR:what-failed -->
## 8. WHAT FAILED
- trying to derive a confidence model from Interactive Mode's quality dimensions failed because those dimensions score phrasing, not feature understanding. (iteration 1)
- a broad grep for "clarifying question" across all 22 repos returned mostly the Figma redistributions, which are byte copies and not independent evidence. (iteration 2)
- the Gause–Weinberg PDF was an image, so the primary source on context-free questions could not be quoted; the secondary material was not strong enough to stand as evidence. (iteration 3)
- hunting for an existing place to store the brief failed, and the failure is itself the finding: the export contract forbids an answer in the clarification file and Flow Mode writes nothing. (iteration 4)
- looking for a script-level home for a brief check failed for a structural reason, since the checker's input is the finished model. (iteration 5)

<!-- /ANCHOR:what-failed -->

---

<!-- ANCHOR:exhausted-approaches -->
## 9. EXHAUSTED APPROACHES (do not retry)
### **A script rule in `flow_check.py` for brief completeness.** The check's input is the model, and the brief is settled before the model [SOURCE: AI Systems/Product Owner/sk-create-figjam/SKILL.md:170]. -- BLOCKED (iteration 5, 1 attempts)
- What was tried: **A script rule in `flow_check.py` for brief completeness.** The check's input is the model, and the brief is settled before the model [SOURCE: AI Systems/Product Owner/sk-create-figjam/SKILL.md:170].
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **A script rule in `flow_check.py` for brief completeness.** The check's input is the model, and the brief is settled before the model [SOURCE: AI Systems/Product Owner/sk-create-figjam/SKILL.md:170].

### **Adding a new packet or a new Knowledge file for the loop.** The loop is a step inside Flow Mode, and the kernel's Knowledge table already names Flow Mode as owning "intake" [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:207]. A new file would double the parity surface for no gain. -- BLOCKED (iteration 5, 1 attempts)
- What was tried: **Adding a new packet or a new Knowledge file for the loop.** The loop is a step inside Flow Mode, and the kernel's Knowledge table already names Flow Mode as owning "intake" [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:207]. A new file would double the parity surface for no gain.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Adding a new packet or a new Knowledge file for the loop.** The loop is a step inside Flow Mode, and the kernel's Knowledge table already names Flow Mode as owning "intake" [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:207]. A new file would double the parity surface for no gain.

### **Adopting a fixed 15-question budget as the round cap.** The figure counts questions, and the brief's unit is a round; a round may carry one to three questions, so the budget has to be expressed in rounds and in no-new-information answers [SOURCE: https://raw.githubusercontent.com/microsoft/devsquad-copilot/main/.github/plugins/devsquad/skills/deep-clarification/SKILL.md]. -- BLOCKED (iteration 3, 1 attempts)
- What was tried: **Adopting a fixed 15-question budget as the round cap.** The figure counts questions, and the brief's unit is a round; a round may carry one to three questions, so the budget has to be expressed in rounds and in no-new-information answers [SOURCE: https://raw.githubusercontent.com/microsoft/devsquad-copilot/main/.github/plugins/devsquad/skills/deep-clarification/SKILL.md].
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Adopting a fixed 15-question budget as the round cap.** The figure counts questions, and the brief's unit is a round; a round may carry one to three questions, so the budget has to be expressed in rounds and in no-new-information answers [SOURCE: https://raw.githubusercontent.com/microsoft/devsquad-copilot/main/.github/plugins/devsquad/skills/deep-clarification/SKILL.md].

### **Copying `approved_sections` as a literal mechanism.** It stores a set of board sections; the intake needs a set of facts with a status each. The precedent is the stored answer object, not its schema. -- BLOCKED (iteration 2, 1 attempts)
- What was tried: **Copying `approved_sections` as a literal mechanism.** It stores a set of board sections; the intake needs a set of facts with a status each. The precedent is the stored answer object, not its schema.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Copying `approved_sections` as a literal mechanism.** It stores a set of board sections; the intake needs a set of facts with a status each. The precedent is the stored answer object, not its schema.

### **Copying the seven-dimension checklist wholesale.** Its dimensions are requirement-shaped (glossary, ADR rationale). The board model needs its own nine facts, borrowing the coverage rule rather than the rows [SOURCE: https://github.com/svenroth-ai/shipwright/blob/main/shared/requirement-elicitation.md]. -- BLOCKED (iteration 3, 1 attempts)
- What was tried: **Copying the seven-dimension checklist wholesale.** Its dimensions are requirement-shaped (glossary, ADR rationale). The board model needs its own nine facts, borrowing the coverage rule rather than the rows [SOURCE: https://github.com/svenroth-ai/shipwright/blob/main/shared/requirement-elicitation.md].
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Copying the seven-dimension checklist wholesale.** Its dimensions are requirement-shaped (glossary, ADR rationale). The board model needs its own nine facts, borrowing the coverage rule rather than the rows [SOURCE: https://github.com/svenroth-ai/shipwright/blob/main/shared/requirement-elicitation.md].

### **Mapping "just do it" to Raw energy.** Raw is reachable only by explicit "skip depth" language and skips the phase flow, which would skip the check and the gate that Flow Mode protects [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:75], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:51]. -- BLOCKED (iteration 4, 1 attempts)
- What was tried: **Mapping "just do it" to Raw energy.** Raw is reachable only by explicit "skip depth" language and skips the phase flow, which would skip the check and the gate that Flow Mode protects [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:75], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:51].
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Mapping "just do it" to Raw energy.** Raw is reachable only by explicit "skip depth" language and skips the phase flow, which would skip the check and the gate that Flow Mode protects [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:75], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:51].

### **Putting the brief on the board as a sticky or a section.** It is a write outside the diagram and needs its own yes, because an extension the gate did not name is not covered by the first yes [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md:168]. -- BLOCKED (iteration 4, 1 attempts)
- What was tried: **Putting the brief on the board as a sticky or a section.** It is a write outside the diagram and needs its own yes, because an extension the gate did not name is not covered by the first yes [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md:168].
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Putting the brief on the board as a sticky or a section.** It is a write outside the diagram and needs its own yes, because an extension the gate did not name is not covered by the first yes [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md:168].

### **Putting the intake in `sk-product-owner/references/interactive-mode.md`.** A Flow route does not load it, and the hub starts `$flow` in the other packet [SOURCE: AI Systems/Product Owner/SKILL.md:53], [SOURCE: AI Systems/Product Owner/ROUTER.md:37]. -- BLOCKED (iteration 5, 1 attempts)
- What was tried: **Putting the intake in `sk-product-owner/references/interactive-mode.md`.** A Flow route does not load it, and the hub starts `$flow` in the other packet [SOURCE: AI Systems/Product Owner/SKILL.md:53], [SOURCE: AI Systems/Product Owner/ROUTER.md:37].
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Putting the intake in `sk-product-owner/references/interactive-mode.md`.** A Flow route does not load it, and the hub starts `$flow` in the other packet [SOURCE: AI Systems/Product Owner/SKILL.md:53], [SOURCE: AI Systems/Product Owner/ROUTER.md:37].

### **Reading the router's 0.85 band as an intake confidence.** It scores artifact intent from keywords, so a request can route to FLOW at HIGH confidence with a one-line brief [SOURCE: AI Systems/Product Owner/sk-product-owner/references/routing.md:38]. Routing confidence and board confidence are different scales. -- BLOCKED (iteration 1, 1 attempts)
- What was tried: **Reading the router's 0.85 band as an intake confidence.** It scores artifact intent from keywords, so a request can route to FLOW at HIGH confidence with a one-line brief [SOURCE: AI Systems/Product Owner/sk-product-owner/references/routing.md:38]. Routing confidence and board confidence are different scales.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Reading the router's 0.85 band as an intake confidence.** It scores artifact intent from keywords, so a request can route to FLOW at HIGH confidence with a one-line brief [SOURCE: AI Systems/Product Owner/sk-product-owner/references/routing.md:38]. Routing confidence and board confidence are different scales.

### **Reusing the clarification export file as the intake record.** The contract forbids the file holding anything but the question, and a project-side run cannot write it at all [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:97], [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:234]. -- BLOCKED (iteration 4, 1 attempts)
- What was tried: **Reusing the clarification export file as the intake record.** The contract forbids the file holding anything but the question, and a project-side run cannot write it at all [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:97], [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:234].
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Reusing the clarification export file as the intake record.** The contract forbids the file holding anything but the question, and a project-side run cannot write it at all [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:97], [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:234].

### **Treating Google's stage list as a schema.** It describes a review conversation's focus, not the intake's stored state [SOURCE: https://design.google/library/reviewing-the-design-review]. -- BLOCKED (iteration 3, 1 attempts)
- What was tried: **Treating Google's stage list as a schema.** It describes a review conversation's focus, not the intake's stored state [SOURCE: https://design.google/library/reviewing-the-design-review].
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Treating Google's stage list as a schema.** It describes a review conversation's focus, not the intake's stored state [SOURCE: https://design.google/library/reviewing-the-design-review].

### **Treating Interactive Mode's five quality dimensions as the confidence model.** They score the question's phrasing, and each can be 8+ while the reader, scope and board message stay unknown [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:431]. The confidence model has to score understanding of the feature, not the question text. -- BLOCKED (iteration 1, 1 attempts)
- What was tried: **Treating Interactive Mode's five quality dimensions as the confidence model.** They score the question's phrasing, and each can be 8+ while the reader, scope and board message stay unknown [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:431]. The confidence model has to score understanding of the feature, not the question text.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Treating Interactive Mode's five quality dimensions as the confidence model.** They score the question's phrasing, and each can be 8+ while the reader, scope and board message stay unknown [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:431]. The confidence model has to score understanding of the feature, not the question text.

### **Treating the four-questions-per-call limit as the round cap.** It caps one message's width, and the project-plan skill loops without a round bound [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:276], [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:255]. -- BLOCKED (iteration 2, 1 attempts)
- What was tried: **Treating the four-questions-per-call limit as the round cap.** It caps one message's width, and the project-plan skill loops without a round bound [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:276], [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:255].
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: **Treating the four-questions-per-call limit as the round cap.** It caps one message's width, and the project-plan skill loops without a round bound [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:276], [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:255].

### A search for a numeric confidence threshold on clarification in requirements engineering returned no authoritative number. Practice states completeness and stop conditions, not a calibrated score. -- BLOCKED (iteration 3, 1 attempts)
- What was tried: A search for a numeric confidence threshold on clarification in requirements engineering returned no authoritative number. Practice states completeness and stop conditions, not a calibrated score.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: A search for a numeric confidence threshold on clarification in requirements engineering returned no authoritative number. Practice states completeness and stop conditions, not a calibrated score.

### Adobe's Spectrum diagram material is a house-style critic, not an intake. It adds no question structure beyond the two-attempt stop [SOURCE: research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/SKILL.md:161]. -- BLOCKED (iteration 2, 1 attempts)
- What was tried: Adobe's Spectrum diagram material is a house-style critic, not an intake. It adds no question structure beyond the two-attempt stop [SOURCE: research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/SKILL.md:161].
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Adobe's Spectrum diagram material is a house-style critic, not an intake. It adds no question structure beyond the two-attempt stop [SOURCE: research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/SKILL.md:161].

### Search for a confidence score or numeric threshold in the corpus. The only numbers are node, edge and attempt budgets; no skill scores its own understanding. Corpus-wide search returned no match. -- BLOCKED (iteration 2, 1 attempts)
- What was tried: Search for a confidence score or numeric threshold in the corpus. The only numbers are node, edge and attempt budgets; no skill scores its own understanding. Corpus-wide search returned no match.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Search for a confidence score or numeric threshold in the corpus. The only numbers are node, edge and attempt budgets; no skill scores its own understanding. Corpus-wide search returned no match.

### Search for a state file in `sk-create-figjam`. The packet has no persistent state outside the model and the provenance table, by design. -- BLOCKED (iteration 4, 1 attempts)
- What was tried: Search for a state file in `sk-create-figjam`. The packet has no persistent state outside the model and the provenance table, by design.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Search for a state file in `sk-create-figjam`. The packet has no persistent state outside the model and the provenance table, by design.

### Search for an existing intake test in the playbook: all 25 scenario files cover routing, board creation, board quality, board writes and boundaries; none covers an under-specified brief. -- BLOCKED (iteration 5, 1 attempts)
- What was tried: Search for an existing intake test in the playbook: all 25 scenario files cover routing, board creation, board quality, board writes and boundaries; none covers an under-specified brief.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Search for an existing intake test in the playbook: all 25 scenario files cover routing, board creation, board quality, board writes and boundaries; none covers an under-specified brief.

### Search for an existing per-turn recap in the packet. Section 8 lists the reply's lines from the board URL to the HVR self-scan, and none of them is a brief [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:235], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:240]. -- BLOCKED (iteration 4, 1 attempts)
- What was tried: Search for an existing per-turn recap in the packet. Section 8 lists the reply's lines from the board URL to the HVR self-scan, and none of them is a brief [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:235], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:240].
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Search for an existing per-turn recap in the packet. Section 8 lists the reply's lines from the board URL to the HVR self-scan, and none of them is a brief [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:235], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:240].

### Search for any state file or cache in `sk-create-figjam`: none exists, by design. -- BLOCKED (iteration 5, 1 attempts)
- What was tried: Search for any state file or cache in `sk-create-figjam`: none exists, by design.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Search for any state file or cache in `sk-create-figjam`: none exists, by design.

### Searching `sk-create-figjam` for an existing intake questionnaire found only the type/order/plan questions listed in finding 5. The packet's intake is source reading (Section 4), not interviewing. -- BLOCKED (iteration 1, 1 attempts)
- What was tried: Searching `sk-create-figjam` for an existing intake questionnaire found only the type/order/plan questions listed in finding 5. The packet's intake is source reading (Section 4), not interviewing.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Searching `sk-create-figjam` for an existing intake questionnaire found only the type/order/plan questions listed in finding 5. The packet's intake is source reading (Section 4), not interviewing.

### The Gause–Weinberg context-free-question extract returned an image-only PDF of 148 characters, so its examples could not be quoted directly; the secondary descriptions of context-free questions were read from the search index instead and are not used as evidence here. -- BLOCKED (iteration 3, 1 attempts)
- What was tried: The Gause–Weinberg context-free-question extract returned an image-only PDF of 148 characters, so its examples could not be quoted directly; the secondary descriptions of context-free questions were read from the search index instead and are not used as evidence here.
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: The Gause–Weinberg context-free-question extract returned an image-only PDF of 148 characters, so its examples could not be quoted directly; the secondary descriptions of context-free questions were read from the search index instead and are not used as evidence here.

<!-- /ANCHOR:exhausted-approaches -->

---

<!-- ANCHOR:ruled-out-directions -->
## 10. RULED OUT DIRECTIONS
- **Reading the router's 0.85 band as an intake confidence.** It scores artifact intent from keywords, so a request can route to FLOW at HIGH confidence with a one-line brief [SOURCE: AI Systems/Product Owner/sk-product-owner/references/routing.md:38]. Routing confidence and board confidence are different scales. (iteration 1)
- **Treating Interactive Mode's five quality dimensions as the confidence model.** They score the question's phrasing, and each can be 8+ while the reader, scope and board message stay unknown [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:431]. The confidence model has to score understanding of the feature, not the question text. (iteration 1)
- Searching `sk-create-figjam` for an existing intake questionnaire found only the type/order/plan questions listed in finding 5. The packet's intake is source reading (Section 4), not interviewing. (iteration 1)
- **Copying `approved_sections` as a literal mechanism.** It stores a set of board sections; the intake needs a set of facts with a status each. The precedent is the stored answer object, not its schema. (iteration 2)
- **Treating the four-questions-per-call limit as the round cap.** It caps one message's width, and the project-plan skill loops without a round bound [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:276], [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:255]. (iteration 2)
- Adobe's Spectrum diagram material is a house-style critic, not an intake. It adds no question structure beyond the two-attempt stop [SOURCE: research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/SKILL.md:161]. (iteration 2)
- Search for a confidence score or numeric threshold in the corpus. The only numbers are node, edge and attempt budgets; no skill scores its own understanding. Corpus-wide search returned no match. (iteration 2)
- **Adopting a fixed 15-question budget as the round cap.** The figure counts questions, and the brief's unit is a round; a round may carry one to three questions, so the budget has to be expressed in rounds and in no-new-information answers [SOURCE: https://raw.githubusercontent.com/microsoft/devsquad-copilot/main/.github/plugins/devsquad/skills/deep-clarification/SKILL.md]. (iteration 3)
- **Copying the seven-dimension checklist wholesale.** Its dimensions are requirement-shaped (glossary, ADR rationale). The board model needs its own nine facts, borrowing the coverage rule rather than the rows [SOURCE: https://github.com/svenroth-ai/shipwright/blob/main/shared/requirement-elicitation.md]. (iteration 3)
- **Treating Google's stage list as a schema.** It describes a review conversation's focus, not the intake's stored state [SOURCE: https://design.google/library/reviewing-the-design-review]. (iteration 3)
- A search for a numeric confidence threshold on clarification in requirements engineering returned no authoritative number. Practice states completeness and stop conditions, not a calibrated score. (iteration 3)
- The Gause–Weinberg context-free-question extract returned an image-only PDF of 148 characters, so its examples could not be quoted directly; the secondary descriptions of context-free questions were read from the search index instead and are not used as evidence here. (iteration 3)
- **Mapping "just do it" to Raw energy.** Raw is reachable only by explicit "skip depth" language and skips the phase flow, which would skip the check and the gate that Flow Mode protects [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:75], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:51]. (iteration 4)
- **Putting the brief on the board as a sticky or a section.** It is a write outside the diagram and needs its own yes, because an extension the gate did not name is not covered by the first yes [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md:168]. (iteration 4)
- **Reusing the clarification export file as the intake record.** The contract forbids the file holding anything but the question, and a project-side run cannot write it at all [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:97], [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:234]. (iteration 4)
- Search for a state file in `sk-create-figjam`. The packet has no persistent state outside the model and the provenance table, by design. (iteration 4)
- Search for an existing per-turn recap in the packet. Section 8 lists the reply's lines from the board URL to the HVR self-scan, and none of them is a brief [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:235], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:240]. (iteration 4)
- **A script rule in `flow_check.py` for brief completeness.** The check's input is the model, and the brief is settled before the model [SOURCE: AI Systems/Product Owner/sk-create-figjam/SKILL.md:170]. (iteration 5)
- **Adding a new packet or a new Knowledge file for the loop.** The loop is a step inside Flow Mode, and the kernel's Knowledge table already names Flow Mode as owning "intake" [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:207]. A new file would double the parity surface for no gain. (iteration 5)
- **Putting the intake in `sk-product-owner/references/interactive-mode.md`.** A Flow route does not load it, and the hub starts `$flow` in the other packet [SOURCE: AI Systems/Product Owner/SKILL.md:53], [SOURCE: AI Systems/Product Owner/ROUTER.md:37]. (iteration 5)
- Search for an existing intake test in the playbook: all 25 scenario files cover routing, board creation, board quality, board writes and boundaries; none covers an under-specified brief. (iteration 5)
- Search for any state file or cache in `sk-create-figjam`: none exists, by design. (iteration 5)

<!-- /ANCHOR:ruled-out-directions -->

---

<!-- ANCHOR:divergence-frontier -->
## 10A. SATURATED DIRECTIONS AND DIVERGENCE FRONTIER
- Completed pivots: 0
- Failed pivots: 0
- Audited overrides: 0
- Saturated: none yet
- Pivot lineage: none yet
- Remaining frontier: none recorded

<!-- /ANCHOR:divergence-frontier -->

---

<!-- ANCHOR:carried-forward-open-questions -->
## 11A. CARRIED-FORWARD OPEN QUESTIONS
[None yet]

<!-- /ANCHOR:carried-forward-open-questions -->

---

<!-- ANCHOR:next-focus -->
## 11. NEXT FOCUS
[All tracked questions are resolved]

<!-- /ANCHOR:next-focus -->

---

<!-- MACHINE-OWNED: END -->
## 12. KNOWN CONTEXT

### Bounded Context Snapshot

- Packet sources: `AI Systems/Product Owner/sk-product-owner/`, `AI Systems/Product Owner/sk-create-figjam/`, the hub `SKILL.md`, `AGENTS.md`, `claude project/Custom Instructions.md`.
- Prior research to build on: `AI Systems/Product Owner/specs/017-figjam-flow-generation/009-figjam-skill-research/research/research.md` and `.../016-figjam-improvement-research/research/research.md` sections 1 to 9.
- Corpus of 22 public repos under `research/corpus/`, including Figma's own `figma__mcp-server-guide` skills.
- Question-asking method: `.skilled/skills/sk-prompt/`.

---

## 13. RESEARCH BOUNDARIES
- Max iterations: 5
- Convergence threshold: 0.05 (convergence mode off; telemetry only)
- Autonomy: no operator is present; conflicts are recorded as findings and the run continues
- Progressive synthesis: false; the workflow owns `research.md`
- Machine-owned sections: the reducer controls Sections 3, 6, 7-11A
- Started: 2026-10-21T08:30:00Z
