# Product Owner Reliability Refinement Proposal

## Recommendation

Apply five small source edits: make CLI delivery produce a read-back receipt, make explicit user counts authoritative, turn Simple scenario count into a blocking invariant, and give the Claude kernel equivalent guards for its no-filesystem runtime.
These edits add no artifact type, template, tool, file, or version change.

## Diagnosis

1. **False delivery claim:** The current text names the desired state, "verify," but not an observable action or evidence token. A smaller model can collapse intent, a successful-looking path, and actual persistence into one mental step, then satisfy the response pattern from its draft rather than from tool output. Because no receipt is required, the final answer looks compliant even when Write or read-back never occurred.

2. **Tier signal override:** The current rules identify requirement count as a signal but do not define source precedence for that count. A smaller model tends to atomize verbs, clauses, states, and acceptance checks because more structure feels more complete. It therefore treats "One requirement" as prose and its own decomposition as the count, even though the user's explicit cardinality should outrank inference.

3. **Scenario-count drift:** The Simple notes say one or two, but the shared template rule permits one to three per requirement and the quality checklist checks scenario shape rather than cardinality. A smaller model follows the familiar normal, edge, guarantee triad and reads the limit as guidance, not a release gate.

## Exact Edits

### Edit 1: CLI Bootstrap Read-Back Receipt
**Target:** `Product Owner/AGENTS.md`
**Anchor:**
```text
6. Verify the file saved successfully and that supplied source material remains unchanged.
7. Only then respond with the file path, quality summary and a 2-3 sentence summary.
```
**Replacement:**
```text
6. Read the saved artifact back from the exact export path. Verification passes only when Read returns non-empty content at that path; a planned path, a Write result, or memory of the draft is not verification. Use the final line number returned by Read as `N`. If read-back fails, retry the save once; if it still fails, do not claim delivery or print a `Path:` line. Report that export is blocked. Confirm supplied source material remains unchanged.
7. Only after that read-back, respond with the file path, `Verified: read-back succeeded; N lines`, quality summary and a 2-3 sentence summary.
```

### Edit 2: Skill-Level Export Gate
**Target:** `Product Owner/skill/SKILL.md`
**Anchor:**
```text
Verify the file exists before responding.

Never paste the full deliverable in chat after filesystem export.

Respond with path, quality summary and a brief next step.
```
**Replacement:**
```text
After saving, Read the exact export path and require non-empty returned content. A path string, planned write, or Write result alone does not pass verification.

Use the final line number returned by Read as `N`. If read-back fails, retry the save once; if it still fails, do not print a `Path:` line or claim delivery. Report that export is blocked.

Never paste the full deliverable in chat after filesystem export.

Only after successful read-back, respond with path, `Verified: read-back succeeded; N lines`, quality summary and a brief next step.
```

### Edit 3: Authoritative Counts and a Blocking Simple Gate
**Target:** `Product Owner/skill/references/story-mode.md`
**Anchor:** `Inference rules:`
**Add immediately after the anchor:**
```text
- When the user explicitly states a requirement count, that count is authoritative unless the user later changes it. Clauses, actions, states, edge cases and acceptance checks inside a stated requirement do not create extra requirements. If supplied source explicitly labels a conflicting set of separate requirements, include the conflict in the one consolidated intake question; never silently override the user's count.
- Mid-draft tier switches remain required when the governing signals actually change. When count was inferred, discovery may still change it; shared machinery may still switch Medium and Complex. Scenario pressure alone is not a count change and cannot override an explicit count.
```
**Second anchor:** the checklist item beginning `- Validate ClickUp grammar:`
**Add immediately after that checklist item:**
```text
- Count `**Scenario:**` headings before export. Simple must have one or two in the entire artifact. If it has three or more, remove padding or merge overlapping proof; re-tier only when the requirement-count rule establishes a genuine second requirement. Otherwise block export.
```

### Edit 4: Remove Template Ambiguity
**Target:** `Product Owner/skill/assets/story-templates.md`
**Anchor:** the bullet beginning `- Acceptance criteria are named **Scenario:** blocks`
**Replace that full bullet with:**
```text
- Acceptance criteria are named **Scenario:** blocks with `*   **Given/When/Then/And**` ClickUp bullets, three to five steps, and observable outcomes. Scenario count is a blocking tier invariant: Simple has one or two in the entire artifact; Medium has three per requirement, with a fourth only for a genuinely separate edge; Complex has three per requirement. A Simple artifact with three scenarios is invalid and cannot be exported.
```
**Second anchor:** `Requirement count and shared machinery are the ONLY tier signals.`
**Add immediately before that paragraph:**
```text
An explicit user-stated requirement count outranks model decomposition. Keep actions, variants, states, edges and acceptance checks under the stated requirement; when the count is inferred, the mid-fill discovery rules below still apply.
```

### Edit 5: Claude Kernel Equivalence
**Target:** `Product Owner/claude project/Custom Instructions.md`
**Anchor:** `12. Use Interactive when artifact type or essential inputs are unclear. Ask one comprehensive question, then wait.`
**Add immediately after:**
```text
**Story tier guard:** An explicit user-stated requirement count outranks model decomposition. Actions, variants, states, edge cases and acceptance checks do not increment it. Mid-draft switches remain valid when an inferred count or shared-machinery signal actually changes. A Simple story must contain one or two scenarios total; three is a blocking delivery failure unless a genuine second requirement is established.
```
**Second anchor:** ``The human reconciles `NNN` when saving outside the Project. Never claim the Project wrote a local file.``
**Add immediately after that paragraph:**
```text
In this runtime, label the path only as `Export-equivalent path:`. Because the Project cannot write or read back local files, never use `Path:`, `Saved:` or `Verified:` for that path; the rendered Deliverable Block is the delivery evidence.
```

## Deliberately Not Changed

- No versions, frontmatter, mirrors, checksums, examples, or export numbering rules change; they do not cause these failures.
- No new validator script or tool is proposed. Read-back plus a receipt is cheaper and available in the CLI tool contract.
- The three tier definitions and legitimate signal-driven mid-draft switches remain intact; only explicit-count precedence and scenario-pressure limits are added.
- Scenario wording, Given/When/Then grammar, and Medium or Complex content remain unchanged.
- Task, Bug, Doc, ClickUp transport, and refinement-fidelity rules remain untouched because the evidence does not implicate them.
