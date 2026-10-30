# Product Owner - Claude Project Packaging

Hand-maintained local package for the Product Owner claude.ai Project. The kernel and every knowledge file are written by hand from the authoritative skill sources; `Custom Instructions.md` remains hand-synthesized. The live claude.ai Project is a separate manual upload because its UI has no repository lock.

---

## 1. OVERVIEW AND STRUCTURE

```text
claude project/
|-- Custom Instructions.md        <- synthesized Project kernel v1.2.16 (routing authority, SKILL.md is not loaded in this Project)
|-- README.md                     <- upload manifest and hand-authored parity note
|-- kernel-review.json            <- dated record of one kernel review, read by no tool
|-- templates/                    <- Product Owner - Local - Push Targets.md, filled and uploaded per user, never shared
|-- local/                        <- gitignored home for a filled push targets copy
`-- knowledge/                    <- upload all 66 files as Project Knowledge
    |-- Product Owner - System - Interactive Mode.md
    |-- Product Owner - Templates - Task Mode.md
    |-- Product Owner - Templates - Bug Mode.md
    |-- Product Owner - Templates - Doc Mode.md
    |-- Product Owner - Templates - Story Mode.md
    |-- Product Owner - Templates - Flow Mode.md
    |-- Product Owner - Templates - Flow Type - User Flow.md
    |-- Product Owner - Templates - Flow Type - Process.md
    |-- Product Owner - Templates - Flow Type - Architecture.md
    |-- Product Owner - Templates - Flow Type - Sequence.md
    |-- Product Owner - Templates - Flow Type - State.md
    |-- Product Owner - Templates - Flow Type - ER.md
    |-- Product Owner - Templates - Flow Type - Gantt.md
    |-- Product Owner - Templates - Flow Hybrid Workflow.md
    |-- Product Owner - Assets - Task Templates.md
    |-- Product Owner - Assets - Bug Report Template.md
    |-- Product Owner - Assets - Interactive Response Templates.md
    |-- Product Owner - Assets - Doc Templates.md
    |-- Product Owner - Assets - Story Template.md
    |-- Product Owner - Assets - Epic Template.md
    |-- Product Owner - Assets - Flow Board Composer.md
    |-- Product Owner - Assets - Flow Board Design.md
    |-- Product Owner - Assets - Flow Templates.md
    |-- Product Owner - Assets - Flow Templates - Process.md
    |-- Product Owner - Assets - Flow Templates - Architecture.md
    |-- Product Owner - Assets - Flow Templates - Sequence.md
    |-- Product Owner - Assets - Flow Templates - State.md
    |-- Product Owner - Assets - Flow Templates - ER.md
    |-- Product Owner - Assets - Flow Templates - Gantt.md
    |-- Product Owner - Rules - Human Voice Core.md
    |-- Product Owner - Rules - Human Voice - EN.md
    |-- Product Owner - Rules - Conciseness.md
    |-- Product Owner - Rules - Conciseness - On Demand Rationale.md
    |-- Product Owner - Rules - Quality Scoring.md
    |-- Product Owner - Rules - Flow Style Guide.md
    |-- Product Owner - Rules - Flow Quality Rubric.md
    |-- Product Owner - Reference - Connector Setup.md
    |-- Product Owner - Examples - Task - ... (5 files)
    |-- Product Owner - Examples - Bug - ... (4 files)
    |-- Product Owner - Examples - Doc - ... (7 files)
    |-- Product Owner - Examples - Story - ... (5 files)
    `-- Product Owner - Examples - Flow - ... (8 files)
```

## Custom Instructions = Skill Kernel, Project-Adapted

`Custom Instructions.md` v1.2.16 is the synthesized claude.ai kernel aligned to **Product Owner Skill v1.2.6.0**. It is the routing authority for this Project because `SKILL.md` is no longer mirrored into Project Knowledge. The kernel carries the full smart-routing prose, energy-scaled quality gates, backlog WHAT/WHY boundaries, source-backed technical HOW, product and engineering Doc routing, Quick as a separate energy override, Human Voice Rules, source authority, conflict blocking, ClickUp formatting, refinement fidelity and export-equivalent delivery.

CLI-only mechanics are adapted: filesystem export becomes the **Deliverable Block**, direct resource loading becomes Project Knowledge consultation, and the response reports an export-equivalent path. Refinements keep delivery metadata outside preserved content unless equivalent metadata already exists in the source.

## Source-to-Mirror Map

| Source | Project Knowledge mirror |
| --- | --- |
| `sk-product-owner/references/interactive-mode.md` | `Product Owner - System - Interactive Mode.md` |
| `sk-product-owner/references/task-mode.md` | `Product Owner - Templates - Task Mode.md` |
| `sk-product-owner/references/bug-mode.md` | `Product Owner - Templates - Bug Mode.md` |
| `sk-product-owner/references/doc-mode.md` | `Product Owner - Templates - Doc Mode.md` |
| `sk-product-owner/references/story-mode.md` | `Product Owner - Templates - Story Mode.md` |
| `sk-product-owner/assets/task-templates.md` | `Product Owner - Assets - Task Templates.md` |
| `sk-product-owner/assets/bug-report-template.md` | `Product Owner - Assets - Bug Report Template.md` |
| `sk-product-owner/assets/interactive-response-templates.md` | `Product Owner - Assets - Interactive Response Templates.md` |
| `sk-product-owner/assets/doc-templates.md` | `Product Owner - Assets - Doc Templates.md` |
| `sk-product-owner/assets/story-template.md` | `Product Owner - Assets - Story Template.md` |
| `sk-product-owner/assets/epic-template.md` | `Product Owner - Assets - Epic Template.md` |
| `sk-create-figjam/references/flow-mode.md` | `Product Owner - Templates - Flow Mode.md` |
| `sk-create-figjam/assets/flow-templates.md` | `Product Owner - Assets - Flow Templates.md` |
| `sk-create-figjam/assets/compose-board.js` | `Product Owner - Assets - Flow Board Composer.md` |
| `sk-create-figjam/assets/figjam-design.md` | `Product Owner - Assets - Flow Board Design.md` |
| `sk-create-figjam/references/types/user-flow.md` | `Product Owner - Templates - Flow Type - User Flow.md` |
| `sk-create-figjam/references/types/process.md` | `Product Owner - Templates - Flow Type - Process.md` |
| `sk-create-figjam/references/types/architecture.md` | `Product Owner - Templates - Flow Type - Architecture.md` |
| `sk-create-figjam/references/types/sequence.md` | `Product Owner - Templates - Flow Type - Sequence.md` |
| `sk-create-figjam/references/types/state.md` | `Product Owner - Templates - Flow Type - State.md` |
| `sk-create-figjam/references/types/er.md` | `Product Owner - Templates - Flow Type - ER.md` |
| `sk-create-figjam/references/types/gantt.md` | `Product Owner - Templates - Flow Type - Gantt.md` |
| `sk-create-figjam/references/hybrid-workflow.md` | `Product Owner - Templates - Flow Hybrid Workflow.md` |
| `sk-create-figjam/references/style-guide.md` | `Product Owner - Rules - Flow Style Guide.md` |
| `sk-create-figjam/references/quality-rubric.md` | `Product Owner - Rules - Flow Quality Rubric.md` |
| `USER-GUIDE.md` | `Product Owner - Reference - Connector Setup.md` |
| `sk-create-figjam/assets/templates/process.md` | `Product Owner - Assets - Flow Templates - Process.md` |
| `sk-create-figjam/assets/templates/architecture.md` | `Product Owner - Assets - Flow Templates - Architecture.md` |
| `sk-create-figjam/assets/templates/sequence.md` | `Product Owner - Assets - Flow Templates - Sequence.md` |
| `sk-create-figjam/assets/templates/state.md` | `Product Owner - Assets - Flow Templates - State.md` |
| `sk-create-figjam/assets/templates/er.md` | `Product Owner - Assets - Flow Templates - ER.md` |
| `sk-create-figjam/assets/templates/gantt.md` | `Product Owner - Assets - Flow Templates - Gantt.md` |
| `sk-create-figjam/assets/examples/user-flow-fernhouse-return.md` | `Product Owner - Examples - Flow - User Flow.md` |
| `sk-create-figjam/assets/examples/process-fernhouse-refund.md` | `Product Owner - Examples - Flow - Process.md` |
| `sk-create-figjam/assets/examples/process-fernhouse-commission.md` | `Product Owner - Examples - Flow - Process Commission.md` |
| `sk-create-figjam/assets/examples/architecture-loomlist-sync.md` | `Product Owner - Examples - Flow - Architecture.md` |
| `sk-create-figjam/assets/examples/sequence-roamstay-checkout.md` | `Product Owner - Examples - Flow - Sequence.md` |
| `sk-create-figjam/assets/examples/state-roamstay-booking.md` | `Product Owner - Examples - Flow - State.md` |
| `sk-create-figjam/assets/examples/er-roamstay-stays.md` | `Product Owner - Examples - Flow - ER.md` |
| `sk-create-figjam/assets/examples/gantt-loomlist-offline.md` | `Product Owner - Examples - Flow - Gantt.md` |
| `sk-product-owner/assets/examples/task/` (5 files) | `Product Owner - Examples - Task - ...`, one mirror per example |
| `sk-product-owner/assets/examples/bug/` (4 files) | `Product Owner - Examples - Bug - ...`, one mirror per example |
| `sk-product-owner/assets/examples/doc/` (7 files) | `Product Owner - Examples - Doc - ...`, one mirror per example |
| `sk-product-owner/assets/examples/story/` (5 files) | `Product Owner - Examples - Story - ...`, one mirror per example |
| `sk-product-owner/references/hvr-core.md` | `Product Owner - Rules - Human Voice Core.md` |
| `sk-product-owner/references/conciseness.md` | `Product Owner - Rules - Conciseness.md` |
| `sk-product-owner/references/human-voice-rules.md` | `Product Owner - Rules - Human Voice - EN.md` |
| `sk-product-owner/references/conciseness-rationale.md` | `Product Owner - Rules - Conciseness - On Demand Rationale.md` |
| `sk-product-owner/references/quality-scoring.md` | `Product Owner - Rules - Quality Scoring.md` |

Every knowledge file is hand-authored from its skill source for Project retrieval, so it carries the decision rules and examples without the skill-only mechanics. The four shared rule files under `references/` are byte copies of cards in the shared knowledge folder, and their Project counterparts are byte copies of the same cards rather than hand-written documents.

## Paired-Version + Checksum Table

Knowledge files are hand-authored for Project retrieval, so the checksum table the retired AI System Sync Compiler generated here is gone and no hash ledger is kept. Drift is watched by the read-only commit-timestamp comparison of the manual parity method instead.


## ClickUp Connector Delivery

When the Project has the claude.ai ClickUp connector, the kernel offers ClickUp delivery after every export and writes nothing without explicit approval in that conversation. Approved pushes preserve formatting through the connector's markdown-aware parameters:

- Task create and update: `markdown_description` on `clickup_create_task` / `clickup_update_task`
- Documents and pages: markdown content with the markdown (`text/md`) content format
- Task read-back: `clickup_get_task` with `include: ["description"]`
- Never the plain `description` field — ClickUp stores it literally and the task shows raw `## About` / `**Checklist**` / `- []` text

Push shape: artifact H1 becomes the task name, Deliverable Block framing and processing metadata stay out of ClickUp, and the body travels verbatim.

Push targets come from a private Knowledge file, `Product Owner - Local - Push Targets.md`, which each user fills from `templates/` and uploads to their own Project only. It names ClickUp lists and docs by team. A filled copy belongs in the gitignored `local/` folder, where the skill reads the same file. When one list or doc fits, the offer names it, when several could fit it asks which, and a document lands as a new page in the named doc through `clickup_create_document_page`. Otherwise it asks where and recommends a private doc, which takes two calls: `clickup_create_document` with `visibility: "PRIVATE"` and `create_page: false`, then `clickup_create_document_page` with the artifact as `content` and `content_format: "text/md"`.

## Set Up the Live Project

1. Create or open a claude.ai Project named **Product Owner**.
2. Paste `Custom Instructions.md` into the Project custom instructions field.
3. Remove superseded Project Knowledge uploads.
4. Upload all 66 files in `knowledge/` with filenames unchanged (37 core files plus the 29 Examples mirrors).
5. Run the smoke matrix below.
6. Confirm the Deliverable Block appears first and the reported path follows the create or refinement contract.
7. To deliver to ClickUp or draw on FigJam, add the two connectors and run their checks as `../USER-GUIDE.md` sets out.

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
- Task and Bug output keeps the shapes `Product Owner - Templates - Task Mode.md` and `Product Owner - Templates - Bug Mode.md` set out.
- New Docs balance heading depth: H2 stays a minority of headings and H3/H4 carry the rest, with no all-H2 wall.
- Doc deliveries report their status in the chat reply beside the export-equivalent path, as the quality line and the `HVR self-scan:` line of the Delivery Reply Shape, and never as a footer or verdict block inside the deliverable.
- `$story`, `$s`, `$prd` and `$p` select Story; `$stories`, `$prds`, `$sort` and embedded `$s` do not; `create a task to write a PRD` stays Task.
- `$flow`, `$figjam` and `put the launch plan on a FigJam gantt chart` select Flow Mode, which picks the diagram type from the reader's question, checks the model rule by rule and waits for a yes before any write. `write a task to tidy the figjam board labels` stays Task.
- `$figjam a mindmap of the launch themes` names the mindmap as a kind the Figma connector cannot draw and offers a table or a list, with no connector call.
- A `$flow` request replies in order: the intake or one proposed Brief, then a playback of the reading, then a gate as its own reply. A `Yes` to the Brief or the playback writes nothing, and only a `Yes` to the gate writes. The playback and the gate each end their turn on their question, with no status line after it
- A `$flow` request that names an existing FigJam file by its link gets a gate that names that file, with no plan and no `create_new_file`, and the board lands as a new section beside what the file holds, with nothing already on it changed
- A `$flow` request whose brief fits two types, such as an architecture and a sequence of one system, gets a first reply that asks only which type, naming both and the recommended one, and the reader round follows its answer
- A `$flow` request for one board that runs over its type's budget cuts the lowest-priority part, names it on the `Left out:` line and offers the split in the playback rather than drawing two boards
- With a Figma connector that lists `use_figma`, the board is composed in one `use_figma` call. Before it fills the model, the Project shows the composer code for the type came back whole: 143 lines and 42,665 characters for a graph board or 71 lines and 21,487 characters for a sequence or a gantt chart, a first line that starts `const MODEL=__MODEL__;const THEME=__THEME__;` and a last line that ends `createdCount:created.length};`. When it cannot show all three it writes through `generate_diagram` and says the board was generated rather than composed
- A thrown error that starts `nothing was drawn` is not retried with the same model and the board is not read. The Project regroups the zones, checks the model again and says the first compose drew nothing
- A revision of a written board composes the new board first, reads it back and asks for a second `Yes` before it deletes the old board section
- A generated Story-Mode artifact names its artifact kind (Story or Epic), keeps the narrative first, uses Given/When/Then scenario bullets, closes with a Delivery section only when the requester asked for one or the artifact forces it, and carries no ticket header fields, story points or INVEST notes.
- With the ClickUp connector present, every export response offers ClickUp delivery and nothing is written to ClickUp without explicit approval in that conversation.
- With no connector switched on in the chat, an export reply closes on `Want me to change anything?` with no push offer, and the first such reply of the conversation offers once, in its last sentence before Open items, to walk the user through adding the connectors.
- With no Figma connector, `$flow` gives the checked model as a Mermaid block and prints no `Read-back:` line.
- In claude.ai in a browser, with both connectors switched on, the ClickUp offer and the FigJam write gate behave as they do in Claude Desktop.
- An approved ClickUp push uses `markdown_description` (never plain `description`) and the created task renders real headings, bold and checkboxes with zero literal `###`, `**` or `- []` text.
- `$task`, `$bug` and `$story` each consult only their own routed knowledge pair (Task Mode + Task Templates, Bug Mode + Bug Report Template, Story Mode + the one scaffold the resolved shape names) and load no unrelated mode resource. A `$story` request consults Story Template and never Epic Template.
- `skip depth` explicitly selects Raw energy and skips the phase flow. `$quick` never selects Raw, and Raw never fires without the explicit phrase.
- `$quick $story` and `$story $quick` (and the `$prd`/`$p` aliases, and `$epic`/`$e`) both select Story with Quick energy, matching the `$quick $doc` / `$doc $quick` order equivalence.
- New Task, Bug, Doc, Story and Epic exports report `export/NNN - {task|bug|doc|Story|Epic}-[description].md`. A Task source sync retains the existing task filename.
- A `$story` request that asks for its task breakdown renders one Deliverable Block per file, Story first, each with its own `Export-equivalent path:` inside `export/NNN - Story-[description]/`. The Story's `#### **Tasks**` block links each `NNN.[n] - task-[description].md`, each task's `**Story**` block links the Story, and one `HVR self-scan:` line covers the set.
- An approved task read-back uses `clickup_get_task` with `include: ["description"]` and confirms the rendered body matches the pushed artifact before delivery is reported complete.
- An approved ClickUp document or page create uses markdown content with the markdown `content_format` value, never the plain `description` field.
- New Doc artifacts use same-level empty spacer headings only in ClickUp-bound content, never in a file export. A Story or Epic keeps its spacer headings in the export, because they belong to the Barter house format.

## Change Checklist

- Update the skill sources first, then hand-write the matching changes into `claude project/Custom Instructions.md` and the affected `claude project/knowledge/` files per the manual parity method, or record that no Project-facing change is needed and why
- Hand-write every affected knowledge file, examples included, and confirm the read-only drift list shows no skill file newer than its Project counterpart.
- Re-derive `Custom Instructions.md` when identity, routing, source safety, template handling, quality or delivery behavior changes.
- After a kernel change, record the review as a dated sentence in the system SYNC.md review notes: who reviewed, what changed, what was decided
- Before live upload, run this system's own checks from its root. The sync compiler was
  retired and `check --system` no longer exists, so nothing is verified by invoking it:
  - `bash benchmark/gates/run_gates.sh`, which runs the router and format fixtures, rule parity, the example lint and the other 11 of its 15 gates
  - `bash benchmark/parity/run_parity.sh`
- Remove superseded mirror filenames and search for stale version references.
- Re-upload changed files to the live Project and run the smoke matrix.

## Known Notes

- Backlog artifacts remain WHAT/WHY focused. Docs may cover source-backed technical HOW, supplied implementation facts, architecture, APIs, schemas, debugging or operational procedures and clearly labelled technical proposals or recommendations. Never fabricate current facts, evidence, approval, authority or professional sign-off.
- Project Knowledge may be retrieved as chunks, so the kernel repeats the routing, source-safety and delivery gates.
- The Flow Board Composer file is 77,116 bytes and holds two code blocks, 42,665 characters on 143 lines for graph boards and 21,487 characters on 71 lines for sequence and gantt boards, so retrieval may return it in chunks. The split keeps room for a model whose zones carry notes and whose steps carry bodies: the call takes at most 50,000 characters, which leaves 7,353 for a graph model JSON and the `THEME` line written compact, and the largest shipped example model, Examples - Flow - Process Commission, runs 2,822. Whether claude.ai retrieval returns the code block whole is UNKNOWN until the live Project test runs, and the guide's whole-file test and the `generate_diagram` fallback cover a miss
- The local package is hand-maintained and the live claude.ai Project is manually uploaded, so local parity does not prove live deployment currency.
