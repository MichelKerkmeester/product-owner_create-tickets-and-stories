# Product Owner - Claude Project Packaging

Hand-maintained local package for the Product Owner claude.ai Project. The kernel and every knowledge file are written by hand from the authoritative skill sources; `Custom Instructions.md` remains hand-synthesized. The live claude.ai Project is a separate manual upload because its UI has no repository lock.

---

## 1. OVERVIEW AND STRUCTURE

```text
claude project/
|-- Custom Instructions.md        <- synthesized Project kernel v1.17.0 (routing authority, SKILL.md is not loaded in this Project)
|-- README.md                     <- upload manifest and hand-authored parity note
`-- knowledge/                    <- upload all thirty-eight files as Project Knowledge
    |-- Product Owner - System - Interactive Mode - v0.407.md
    |-- Product Owner - System - Router Contract - v0.100.md
    |-- Product Owner - Templates - Task Mode - v0.306.md
    |-- Product Owner - Templates - Bug Mode - v0.204.md
    |-- Product Owner - Templates - Doc Mode - v0.111.md
    |-- Product Owner - Templates - Story Mode - v0.404.md
    |-- Product Owner - Assets - Task Templates - v0.102.md
    |-- Product Owner - Assets - Bug Report Template - v0.101.md
    |-- Product Owner - Assets - Interactive Response Templates - v0.103.md
    |-- Product Owner - Assets - Doc Templates - v0.108.md
    |-- Product Owner - Assets - Story Template - v0.100.md
    |-- Product Owner - Assets - Epic Template - v0.101.md
    |-- Product Owner - Rules - Human Voice Core - v0.100.md
    |-- Product Owner - Rules - Human Voice - EN - v0.210.md
    |-- Product Owner - Rules - Conciseness - v0.100.md
    |-- Product Owner - Rules - Conciseness - On Demand Rationale - v0.100.md
    |-- Product Owner - Rules - Quality Scoring - v0.100.md
    |-- Product Owner - Examples - Task - ... (5 files)
    |-- Product Owner - Examples - Bug - ... (4 files)
    |-- Product Owner - Examples - Doc - ... (7 files)
    `-- Product Owner - Examples - Story - ... (5 files)
```

## Custom Instructions = Skill Kernel, Project-Adapted

`Custom Instructions.md` v1.17.0 is the synthesized claude.ai kernel aligned to **Product Owner Skill v1.14.0**. It is the routing authority for this Project because `SKILL.md` is no longer mirrored into Project Knowledge. The kernel carries the full smart-routing prose, energy-scaled quality gates, backlog WHAT/WHY boundaries, source-backed technical HOW, product and engineering Doc routing, Quick as a separate energy override, Human Voice Rules, source authority, conflict blocking, ClickUp formatting, refinement fidelity and export-equivalent delivery.

CLI-only mechanics are adapted: filesystem export becomes the **Deliverable Block**, direct resource loading becomes Project Knowledge consultation, and the response reports an export-equivalent path. Refinements keep delivery metadata outside preserved content unless equivalent metadata already exists in the source.

## Source-to-Mirror Map

| Source | Project Knowledge mirror |
| --- | --- |
| `sk-product-owner/references/interactive-mode.md` | `Product Owner - System - Interactive Mode - v0.407.md` |
| `sk-product-owner/references/task-mode.md` | `Product Owner - Templates - Task Mode - v0.306.md` |
| `sk-product-owner/references/bug-mode.md` | `Product Owner - Templates - Bug Mode - v0.204.md` |
| `sk-product-owner/references/doc-mode.md` | `Product Owner - Templates - Doc Mode - v0.111.md` |
| `sk-product-owner/references/story-mode.md` | `Product Owner - Templates - Story Mode - v0.404.md` |
| `sk-product-owner/assets/task-templates.md` | `Product Owner - Assets - Task Templates - v0.102.md` |
| `sk-product-owner/assets/bug-report-template.md` | `Product Owner - Assets - Bug Report Template - v0.101.md` |
| `sk-product-owner/assets/interactive-response-templates.md` | `Product Owner - Assets - Interactive Response Templates - v0.103.md` |
| `sk-product-owner/assets/doc-templates.md` | `Product Owner - Assets - Doc Templates - v0.108.md` |
| `sk-product-owner/assets/story-template.md` | `Product Owner - Assets - Story Template - v0.100.md` |
| `sk-product-owner/assets/epic-template.md` | `Product Owner - Assets - Epic Template - v0.101.md` |
| `sk-product-owner/references/hvr-core.md` | `Product Owner - Rules - Human Voice Core - v0.100.md` |
| `sk-product-owner/references/conciseness.md` | `Product Owner - Rules - Conciseness - v0.100.md` |
| `sk-product-owner/references/human-voice-rules.md` | `Product Owner - Rules - Human Voice - EN - v0.210.md` |
| `sk-product-owner/references/conciseness-rationale.md` | `Product Owner - Rules - Conciseness - On Demand Rationale - v0.100.md` |
| `sk-product-owner/references/quality-scoring.md` | `Product Owner - Rules - Quality Scoring - v0.100.md` |
| `sk-product-owner/references/router-contract.md` | `Product Owner - System - Router Contract - v0.100.md` |

Every knowledge file is hand-authored from its skill source for Project retrieval, so it carries the decision rules and examples without the skill-only mechanics. The four shared rule files under `references/` are byte copies of cards in the shared knowledge folder, and their Project counterparts are byte copies of the same cards rather than hand-written documents.

## Paired-Version + Checksum Table

Knowledge files are hand-authored for Project retrieval, so the checksum table the retired AI System Sync Compiler generated here is gone and no hash ledger is kept. Drift is watched by the read-only commit-timestamp comparison of the manual parity method instead.


## ClickUp Connector Delivery

When the Project has the claude.ai ClickUp connector, the kernel offers ClickUp delivery after every export and writes nothing without explicit approval in that conversation. Approved pushes preserve formatting through the connector's markdown-aware parameters:

- Task create and update: `markdown_description` on `clickup_create_task` / `clickup_update_task`
- Documents and pages: markdown content with the markdown (`text/md`) content format
- Never the plain `description` field — ClickUp stores it literally and the task shows raw `### About` / `**Checklist**` / `- [ ]` text

Push shape: artifact H1 becomes the task name, Deliverable Block framing and processing metadata stay out of ClickUp, and the body travels verbatim.

## Set Up the Live Project

1. Create or open a claude.ai Project named **Product Owner**.
2. Paste `Custom Instructions.md` into the Project custom instructions field.
3. Remove superseded Project Knowledge uploads.
4. Upload all thirty-eight files in `knowledge/` with filenames unchanged (seventeen core files plus the twenty-one Examples mirrors).
5. Run the smoke matrix below.
6. Confirm the Deliverable Block appears first and the reported path follows the create or refinement contract.

## Smoke Matrix

- `$task`, `$bug`, `$doc` and `$d` select their named artifact intents.
- `$quick $doc` and `$doc $quick` select Doc with Quick energy; `$quick` alone retains the Task fallback.
- `$document`, `$docs`, `$debug`, embedded `$d`, `$d.md` and `$doc/path` do not activate Doc; `$d,` does.
- `create a task to document X` stays Task, `bug report about documentation` stays Bug and `document bug behavior` becomes Doc.
- `write engineering documentation for Feed ranking`, `create API docs`, `create architecture docs`, `write a technical recommendation` and `write a configuration runbook` route to Doc.
- Modified artifact requests such as `create developer docs`, `draft endpoint reference`, `write a deployment guide`, `create a debugging guide`, `draft SDK documentation`, `write CLI docs`, `create integration documentation`, `draft infrastructure runbook` and `write service docs` route to Doc.
- `compare ranking approaches and document the recommendation`, `select an API pattern and document the decision` and `analyze the schema options and document it` route to Doc proposals or recommendations.
- `refine the Notification settings guide` and equivalent update or edit requests for a typed or titled document route to Doc refinement.
- `create a task to write engineering docs` stays Task and `bug report about incorrect API documentation` stays Bug.
- Architecture, debugging, operational, legal, compliance and security subject matter may be documented from supplied or verified material; those nouns alone do not trigger refusal.
- `$doc create a task explaining Feed v2` stays Doc because one explicit artifact command wins over natural-language actions.
- `create a task and create a guide` has two independent natural-language artifact actions and produces one consolidated question.
- Conflicting artifact commands produce one consolidated question and no artifact.
- Unresolved source authority, contradictory claims and current-versus-proposed ambiguity block Doc drafting under every energy.
- Guide, Catalog, Behavior reference, Proposal and Narrative overview requests use the matching adaptive shape.
- Source-backed technical HOW is retained. Technical proposals and recommendations remain clearly labelled; they never become current implementation, approved decisions or professional sign-off without authority.
- Proposal and retired labels remain visible; they never become current product or engineering facts.
- New Docs put one blank line between the document title and its first `* * *` divider, then put exact `* * *` dividers immediately after every non-title, non-empty content heading; they use `*   ` unordered bullets and `*   **Term** — definition` for compact definition lists, never `-` unordered bullets.
- A Doc refinement preserves the source's divider, bullet, heading and spacing style unless the user explicitly requests ClickUp normalization.
- A Doc refinement retains its original basename, structure, links, identifiers, tables, literal copy and status markers outside requested scope.
- New Docs report `export/NNN - doc-[description].md`; refinements report `export/[original-source-filename].md`.
- Task and Bug behavior remains compatible with the pinned v0.303 and v0.203 references.
- New Docs balance heading depth: H2 stays a minority of headings and H3/H4 carry the rest, with no all-H2 wall.
- Doc deliveries report their status in the chat reply beside the export-equivalent path, as a compact quality summary and the `HVR self-scan:` line, and never as a footer or verdict block inside the deliverable.
- `$story`, `$s`, `$prd` and `$p` select Story; `$stories`, `$prds`, `$sort` and embedded `$s` do not; `create a task to write a PRD` stays Task.
- A generated Story-Mode artifact names its artifact kind (Story or Epic), keeps the narrative first, uses Given/When/Then scenario bullets, closes with a Delivery section only when the requester asked for one or the artifact forces it, and carries no ticket header fields, story points or INVEST notes.
- With the ClickUp connector present, every export response offers ClickUp delivery and nothing is written to ClickUp without explicit approval in that conversation.
- An approved ClickUp push uses `markdown_description` (never plain `description`) and the created task renders real headings, bold and checkboxes with zero literal `###`, `**` or `- [ ]` text.
- `$task`, `$bug` and `$story` each consult only their own routed knowledge pair (Task Mode + Task Templates, Bug Mode + Bug Report Template, Story Mode + the one scaffold the resolved shape names) and load no unrelated mode resource. A `$story` request consults Story Template and never Epic Template.
- `skip depth` explicitly selects Raw energy and skips the phase flow. `$quick` never selects Raw, and Raw never fires without the explicit phrase.
- `$quick $story` and `$story $quick` (and the `$prd`/`$p` aliases, and `$epic`/`$e`) both select Story with Quick energy, matching the `$quick $doc` / `$doc $quick` order equivalence.
- New Task, Bug, Doc, Story and Epic exports report `export/NNN - {task|bug|doc|Story|Epic}-[description].md`. A Task source sync retains the existing task filename.
- A `$story` request that asks for its task breakdown renders one Deliverable Block per file, Story first, each with its own `Export-equivalent path:` inside `export/NNN - Story-[description]/`. The Story's `#### **Tasks**` block links each `NNN.[n] - task-[description].md`, each task's `**Story**` block links the Story, and one `HVR self-scan:` line covers the set.
- An approved task read-back uses `include_markdown_description=true` and confirms the rendered body matches the pushed artifact before delivery is reported complete.
- An approved ClickUp document or page create uses markdown content with the markdown `content_format` value, never the plain `description` field.
- New Doc artifacts use same-level empty spacer headings only in ClickUp-bound content, never in a file export. A PRD keeps its spacer headings in the export, because they belong to the Barter house format.

## Change Checklist

- Update the skill sources first, then hand-write the matching changes into `claude project/Custom Instructions.md` and the affected `claude project/knowledge/` files per the manual parity method, or record that no Project-facing change is needed and why
- Hand-write every affected knowledge file, examples included, and confirm the read-only drift list shows no skill file newer than its Project counterpart.
- Re-derive `Custom Instructions.md` when identity, routing, source safety, template handling, quality or delivery behavior changes.
- After a kernel change, record the review as a dated sentence in the system SYNC.md review notes: who reviewed, what changed, what was decided
- Before live upload, run this system's own checks from its root. The sync compiler was
  retired and `check --system` no longer exists, so nothing is verified by invoking it:
  - `bash benchmark/router/run_fixtures.sh`
  - `bash benchmark/format/run_fixtures.sh`
  - `bash benchmark/parity/run_parity.sh`
- Remove superseded mirror filenames and search for stale version references.
- Re-upload changed files to the live Project and run the smoke matrix.

## Known Notes

- Backlog artifacts remain WHAT/WHY focused. Docs may cover source-backed technical HOW, supplied implementation facts, architecture, APIs, schemas, debugging or operational procedures and clearly labelled technical proposals or recommendations. Never fabricate current facts, evidence, approval, authority or professional sign-off.
- Project Knowledge may be retrieved as chunks, so the kernel repeats the routing, source-safety and delivery gates.
- The local package is hand-maintained and the live claude.ai Project is manually uploaded, so local parity does not prove live deployment currency.
