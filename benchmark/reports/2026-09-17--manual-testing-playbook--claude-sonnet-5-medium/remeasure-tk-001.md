# Re-measurement, the Task Mode caveat repair on `TK-001`

Post-repair measurement for commit `173a3b7`, `fix(product-owner): an explicit command
routes a request, it does not complete one`. `sampling.md` measured this lane before the
repair and is untouched. This file carries the after side and nothing else.

Measuring only. No system file, scenario file or Task Mode document was changed by this
pass.

---

## 1. What the repair changed, read from the files

Both Task Mode documents previously read, on the `**Interactive Mode:**` bullet:

> Ask one comprehensive question unless the request already contains enough direction or
> uses an explicit command

They now read:

> Ask one comprehensive question unless the request already contains enough direction. An
> explicit command routes the request and does not stand in for the direction, so `$task`
> and `$bug` still ask their context-specific question and wait. Only `$quick` may skip
> routine intake

Located by `grep -n`, not taken from the commit message:

| Side | File | Line |
| --- | --- | ---: |
| skill | `sk-product-owner/references/task-mode.md` | 50 |
| project | `claude project/knowledge/Product Owner - Templates - Task Mode - v0.304.md` | 30 |

The two strings are identical character for character. The superseded wording is recovered
from `git show 173a3b7^` at the same two line numbers, so the before and after text is read
from the tree rather than from prose.

### The cited authority says what the repair claims

`awk 'NR==124'` on `sk-product-owner/references/interactive-mode.md`:

```
| **Direct Task or Bug** (`$task`/`$bug`) | Context-specific question → Wait → Process → Deliver |
```

Its Project mirror is line 101 of `Product Owner - System - Interactive Mode - v0.404.md`,
which is the line `PTK-001` cites by number in its own expected-signals cell. Both name a
context-specific question and a wait, for an explicit command. Verified.

The `Only $quick may skip routine intake` limb is also supported: `interactive-mode.md`
line 126 and its Project mirror line 103 both read `Task/Bug may skip routine intake` only
under the Quick energy row.

The consolidated-question claim holds on the skill side's two always-loaded documents,
`AGENTS.md` line 188 and `SKILL.md` line 355, both of which say conflicting commands
produce one consolidated question. The Project kernel does not state it in those words. Its
nearest line, `Custom Instructions.md` line 35, is about the confidence floor rather than
command conflict, so that half of the commit's reasoning rests on the skill side alone.

### One residual the repair left behind

Two lines below the repaired bullet, in the same section of both documents, the Core Rules
list still reads:

| Side | File | Line | Text |
| --- | --- | ---: | --- |
| skill | `references/task-mode.md` | 55 | `Ask one comprehensive question before drafting unless the request is explicit or uses $quick` |
| project | `... Task Mode - v0.304.md` | 35 | same string |

`the request is explicit` is readable two ways. It can mean the retained first limb, a
request that already contains enough direction, or it can mean the limb the repair
removed, a request carrying an explicit command. A runtime reading the Core Rules bullet
alone can still reach the old conclusion. This is not a measured cause of anything below,
and it is the cheapest thing to settle before spending more samples.

Neither Bug Mode document carries a parallel caveat, so the repaired sentence's promise
about `$bug` is a statement made inside Task Mode rather than a change to the Bug lane.

### Where the changed text does and does not live

The harness passes `AGENTS.md` as the skill system prompt and `Custom Instructions.md` plus
a retrieval note as the Project system prompt. Neither carries the repaired caveat
(`grep` on both files returns no match for `explicit command` or `routine intake`). The
repair therefore lives only in an on-demand mode document that the runtime must open. That
is the weaker of the two positions the brief names from other systems, and it is why the
in-context audit in section 5 is load-bearing rather than decorative.

---

## 2. Pre-registered discriminator

Written and validated before any post-repair sample ran, and not revised afterwards.
Implemented as one script so every row below is reproducible from the persisted files.

The repair changed whether intake happens. `sampling.md` measured whether the
clarification is delivered. Those are two observables inside one five-clause verdict, so
this pass scores them apart and reports both.

### The observable this repair should move: INTAKE

Applies to the **turn-1 reply text alone**.

| Clause | Test | Both arms |
| --- | --- | --- |
| A1, asked | at least one `?` outside a fenced block | same test |
| A2, not drafted | the pre-registered `C1`: not (`^#{2,4}\s*About` and `^#{2,4}\s*Requirements`) and no `^\s*[-*]\s\[\s\]` line | same test |

`INTAKE = A1 and A2`. A2 is `sampling.md`'s `C1` unchanged. A1 is added because `C1` is a
negative test only, and a reply can avoid the task grammar without putting a question to
the user, which is what the one harness stub in the prior set did.

### The observable `sampling.md` measured: DELIVERY

Clause regexes copied from `sampling.md` section 1 without alteration.

| Clause | Skill side | Project side |
| --- | --- | --- |
| C2, clarification addressed | `export/\s*\d{3}\s*-\s*(task\|intake)[^\n]*-clarification\.md` | same test |
| C3, delivery proof | `read[-\s]?back` and one of `verified\|succeed` | contains `Deliverable Block` and `Export-equivalent path:` |
| C4, self-scan | contains `HVR self-scan:` | same test |
| C5, no save claim | not applicable | no match for `(?<!\[-\w])(Path\|Saved\|Verified):` |

`DELIVERY = C2 and C3 and C4 and C5`. `OVERALL = C1..C5`, which is the verdict
`sampling.md` recorded, kept so the two measurements stay commensurable.

Each literal-label clause is also run case-insensitively as a shadow test, because a
one-spelling check has already bitten this report set. The shadow and the literal test
agreed on all 36 turn-1 files scored here, so no row below turns on letter case.

### Validation against the persisted pre-repair samples

The discriminator was run over all 26 `TK-001` turn-1 files already in `samples/` and its
`OVERALL` column and failing-clause set were compared row by row against `manifest.csv`.

- 26 manifest rows for `TK-001`, 26 turn-1 files scored, **zero disagreements** on the
  verdict and zero on the named failing clauses
- it reproduces the recorded direction: Project `1 PASS in 13`, skill `8 PASS in 13`,
  which are the numbers `sampling.md` section 4 carries
- it reproduces the matched-configuration contrast and its statistic: skill 3 of 5 against
  Project 0 of 5, Fisher exact one-sided p = 0.0833, against the recorded `p = 0.083`

Counted by parsing the file rather than by reading the report's prose.

---

## 3. Which observable was chosen, and why the other is not affected

**Chosen: INTAKE.** The caveat is a rule about whether to ask before drafting. Its removed
limb licensed one specific failure, a turn 1 that treats `$task` as sufficient direction
and renders the finished task. `sampling.md` section 6 reports exactly that failure once,
in `TK-001-project-reused-07`, and reports it in its own row precisely because it is a
different fault from the plain-chat failures.

**Not affected: DELIVERY.** The repaired sentence says nothing about where a clarification
is addressed, what proves it was delivered, or the self-scan line. Read directly, neither
Task Mode document carries any clarification-delivery rule at all, which `verdict.md`
independently established by grep. So `C2`, `C3` and `C4` have no new text bearing on them
and the prediction registered before running was that they would not move.

That prediction makes DELIVERY a useful negative control rather than a spare column. If
DELIVERY had shifted, the run configuration would be suspect. Section 4 shows it did not
shift by a single sample.

---

## 4. Run configuration, and whether the sets compare

Ten new samples, five per side, each a full two-turn conversation in a fresh session, run
from the `AI Systems` directory:

```
HARNESS_SCRATCH=<one per sample> HARNESS_MODEL=claude-sonnet-5 HARNESS_EFFORT=medium \
  "z — Parity Gate/run_packaging.sh" "Product Owner" <skill|project> '<turn 1>' \
  --session $(uuidgen) --noweb
```

then `--resume <that uuid>` with the turn-2 prompt. `--noweb` is kept because every prior
sample in this set used it. All twenty calls returned a non-empty reply file.

Prompts were parsed out of the two scenario tables rather than retyped, and compared:
turn 1 is 57 characters and turn 2 is 240 characters, byte-identical between the skill and
Project scenario files, matching the lengths `sampling.md` recorded.

### The Bash-to-Glob question, answered on this observable

The sets compare, and the matched comparison is the `new` rows only.

- all five post-repair Project samples made **zero** calls to `Write`, `Edit`,
  `NotebookEdit` or `Bash`, and all five used `Glob` for knowledge discovery. That is the
  same mechanism as the prior `new` Project samples, so those five rows are the matched
  baseline
- the prior `reused` Project samples had `Bash` and the write tools available. They are a
  different configuration and keep their own rows
- this matters more than it looks, because the one pre-repair premature draft sits in the
  `reused` set, not the `new` set. The configuration in which the fault was actually
  observed is not the configuration this pass can match. Section 7 treats that as the
  main limit on the result
- on the skill side `Bash` and `Write` stay available in both configurations, and all five
  post-repair skill samples used both, so the skill rows compare directly

### Harness behaviour worth recording

- four of five skill samples first called the `Skill` tool with `product-owner` and got
  `Unknown skill`. All five then ran a `find /` for their own files, three of them
  uncapped and two depth-capped, which is the same pathology `sampling.md` recorded. All
  five had that find backgrounded, and in three of them (`skill-post-02`, `-03`, `-04`)
  the resulting record shifts a naive turn count by one. Section 5 measures turn 1 by
  locating the turn-2 prompt text instead, so no row here depends on that count
- one Project sample called `ToolSearch` for a canvas surface and another did so on turn 2,
  both the runtime looking for a rendering surface the CLI does not have
- no tool input in any of the ten transcripts named a path outside its own scratch subtree,
  and the string `manual-testing-playbook` appears in none of them, so no sample read the
  scenario it was being graded against

---

## 5. Was the changed text in context, turn 1 only

Measured from the session transcripts by searching every `tool_result` payload for the
repaired sentence itself, not by inferring it from an opened path. The cut between turns is
taken from the turn-2 prompt text, so the backgrounded-find artefact cannot shift it.

| Sample | Repaired caveat in context before the turn-1 reply | Carrier file |
| --- | --- | --- |
| `TK-001-skill-post-01` | yes | `references/task-mode.md` |
| `TK-001-skill-post-02` | no | opened `SKILL.md` and `references/interactive-mode.md` only |
| `TK-001-skill-post-03` | no | opened `SKILL.md` and `references/interactive-mode.md` only |
| `TK-001-skill-post-04` | yes | `references/task-mode.md` |
| `TK-001-skill-post-05` | yes | `references/task-mode.md` |
| `TK-001-project-post-01` | yes | `knowledge/Product Owner - Templates - Task Mode - v0.304.md` |
| `TK-001-project-post-02` | yes | same |
| `TK-001-project-post-03` | yes | same |
| `TK-001-project-post-04` | yes | same |
| `TK-001-project-post-05` | no | made zero tool calls on turn 1 |

Seven of ten had it in context on turn 1, four of five on the Project side and three of
five on the skill side. The brief's caution that this system's runtimes were observed
opening mode documents is borne out but is not universal.

Two facts about the three that did not:

- all three asked their question anyway. The behaviour under test does not require the
  changed text to be in context on this prompt
- `TK-001-project-post-05` made no tool calls at all on turn 1 and asked an eight-point
  question from the kernel alone, then opened Task Mode on turn 2

Two controls confirm the samples really are post-repair:

- the superseded wording `or uses an explicit command` appears in **zero** tool results
  across all ten transcripts
- every Project sample opened `... Task Mode - v0.304.md`, and every one of the five
  matched pre-repair `new` Project samples opened `... v0.303.md`, checked one transcript
  at a time. The version in the path is a clean before-and-after marker on the matched
  rows, 5 of 5 against 5 of 5. Most `reused` transcript extracts truncate their paths and
  cannot be read this way, which is why `TK-001-project-reused-07` was recovered from its
  session `jsonl` instead

### The pre-repair fault had the licence in context too

The single premature draft, `TK-001-project-reused-07`, still has its session transcript on
disk. Read directly, it opened `Product Owner - Templates - Task Mode - v0.303.md`, whose
payload contains `or uses an explicit command` and does **not** contain the repaired
sentence. It also opened `Product Owner - System - Interactive Mode - v0.404.md`, which
carries the contrary authority at line 101. So the one observed instance of the fault had
both the licence and the rule that overrides it in context, and followed the licence. That
is the strongest available evidence that the repair is aimed at the right text.

---

## 6. Before and after

Scored against the turn-1 reply text by the section 2 discriminator. Before rows are
re-derived from the persisted files, not copied from `sampling.md` prose.

### The observable the caveat governed: INTAKE, turn 1 asks and does not draft

| Arm | Origin | Samples | INTAKE PASS | Premature draft | Config |
| --- | --- | ---: | ---: | ---: | --- |
| skill | before, new | 5 | 5 | 0 | matched |
| skill | after | 5 | **5** | **0** | matched |
| project | before, new | 5 | 5 | 0 | matched |
| project | after | 5 | **5** | **0** | matched |
| skill | before, reused | 7 | 6 | 0 | skill config matches |
| skill | before, committed | 1 | 1 | 0 | writes available |
| **skill, all before** |  | **13** | **12** | **0** |  |
| project | before, reused | 7 | 6 | 1 | writes available |
| project | before, committed | 1 | 1 | 0 | writes available |
| **project, all before** |  | **13** | **12** | **1** |  |

The one skill INTAKE failure before is the harness stub recorded in `adjudication.md`
section 3, a two-line reply about a timed-out background command. It fails A1 because it
puts no question, not because it drafted. The one Project INTAKE failure before is the
premature draft.

### The observable `sampling.md` measured: DELIVERY, turn 1 delivers the clarification

| Arm | Origin | Samples | DELIVERY PASS | Failing clauses |
| --- | --- | ---: | ---: | --- |
| skill | before, new | 5 | 3 | C2, C3, C4 on both failures |
| skill | after | 5 | **3** | C2, C3, C4 on both failures |
| project | before, new | 5 | 0 | C2, C3, C4 on all five |
| project | after | 5 | **0** | C2, C3, C4 on all five |
| **skill, all before** |  | **13** | **8** |  |
| **project, all before** |  | **13** | **1** |  |

The matched contrast is unchanged in both directions: skill 3 of 5 against Project 0 of 5
before, and 3 of 5 against 0 of 5 after, Fisher exact one-sided p = 0.0833 in both.

### Turn 2, for completeness

All five post-repair Project samples rendered the task on turn 2 with `### About`,
`### Requirements` and a `- [ ]` checklist. The skill samples' turn-2 replies are short
because that packaging writes the artifact to `export/` and summarises, which the disk
corroborates: the three skill samples that delivered a clarification on turn 1 wrote
`001 - ...-clarification.md` and numbered the task `002`, and the two that did not wrote
only `001 - task-creator-payout-pause.md`, which is only possible if the clarification
never existed.

---

## 7. Did the behaviour move

**On the observable the repair governs, INTAKE: it did not move, and this measurement
could not have detected movement.** Both sides asked their question in 5 of 5 before and 5
of 5 after, in the matched configuration. The observable was already at its ceiling before
the repair, so there was no room in these numbers for a licence removal to show.

**On the observable `sampling.md` measured, DELIVERY: it did not move, as predicted.**
3 of 5 skill and 0 of 5 Project, identical before and after, with the same three clauses
failing every time.

A third reading did not move either. Counting turn-1 replies that state the routing
reasoning out loud, against one pattern run over both sets
(`explicit command|exact command|routes the request|Task Mode intake|consolidated (Task )?question before|intake rules`,
case-insensitive), the rate is 2 of 10 after against 6 of 26 before, and 2 of 10 against
3 of 10 on the matched `new` rows alone. My first pass at this used a narrower pattern on
the before set than on the after set and produced a spurious `two against two`. The
corrected figures are above. The conclusion is unchanged, but the error is the exact
one-spelling mistake this report set has already recorded once, so it is recorded here too.

**It did not move in an unintended direction.** No post-repair sample drafted prematurely,
none printed `Path:`, `Saved:` or `Verified:` on the Project side, and no new failure mode
appeared.

So neither pattern the brief names from other systems is demonstrated here. This is not the
Sales Direct result, because nothing was shown to be inert. It is not the Blog Posts
result, because no directional shift was observed at all. It is a third case: the repair
targets a fault whose base rate is too low for five samples per side to see.

### What these numbers support, and what they cannot

Supported:

- the repair is present, byte-identical on both sides, and was in context before the turn-1
  reply in 7 of 10 samples, by direct search of the transcript payloads
- the superseded wording is gone from every sample's context
- the clarification-delivery fault is untouched by this repair, measured rather than
  assumed, and reproduces its prior rate exactly
- no regression was introduced on the turn-1 verdict or on turn 2

Not supported, and stated plainly:

- **that the repair works.** The fault it removes was observed once in 13 pre-repair
  Project samples, a rate of 1 in 13. At that rate, the chance of drawing zero premature
  drafts in five samples even if the repair changed nothing is `(12/13)^5 = 0.67`. Two
  thirds of no-effect runs produce exactly the result observed here
- **that the repair is inert.** Nothing here argues against it either
- **a null of any kind.** Five per side cannot certify one. A 5-of-5 asking rate has a
  one-sided 95 percent lower bound of `0.05^(1/5) = 0.549`, so even a perfect five is
  consistent with a true rate near 55 percent
- **anything about the configuration where the fault was seen.** The premature draft
  occurred with `Bash` and the write tools available to the Project side, which the current
  default withholds. The matched five-per-side comparison this pass ran never contained the
  fault on either side of the repair

### What would settle it

- **for the premature-draft rate, 38 Project samples per side.** Against the pooled
  pre-repair rate of 1 in 13, `n = ceil(ln(0.05)/ln(12/13)) = 38` gives a 95 percent chance
  of drawing at least one draft if the rate is unchanged, so zero in 38 would be the first
  number that means something. Five means 33 percent power and nothing more
- **or, far cheaper, re-run the fault's own configuration.** Repeat the `reused` Project
  arm with `--grant-write`, which is the configuration the single observed draft came from,
  before spending 38 samples on a configuration that has never produced the fault
- **settle the Core Rules residual first.** Line 55 on the skill side and line 35 on the
  Project side still read `unless the request is explicit`, two lines below the repair, in
  the same section. If that reopens the licence the repair closed, 38 samples would measure
  a document that still contradicts itself. Reading both lines is free and comes before any
  sample count
- **for the delivery fault, nothing in this pass changes the position.** `sampling.md`'s
  own next step stands: add the delivery verb to `Custom Instructions.md` line 229 and both
  Task Mode documents, then eight per side. At the rates measured here twice, six per side
  reaches p = 0.030 and eight reaches p = 0.013

---

## 8. Samples persisted

All ten samples are persisted beside this file, both turns and a transcript extract each:

```
benchmark/reports/2026-09-17--manual-testing-playbook--claude-sonnet-5-medium/samples/
```

Post-repair stems carry `-post-` in the name, as
`TK-001-<arm>-post-<nn>-turn<n>.txt` and `TK-001-<arm>-post-<nn>.transcript.txt`.

Counted by walking the directory:

| Count | Value |
| --- | ---: |
| files added by this pass | 30 |
| of those, turn-1 replies | 10 |
| of those, turn-2 replies | 10 |
| of those, transcript extracts | 10 |
| directory total after | 137 |

The 30 added files are 10 samples times 3 files. `ls \| grep -c -- '-post-'` and its
case-insensitive form both return 30, so the marker has no spelling variant.

`manifest.csv` was deliberately **not** extended. Its 43 rows are the denominator
`sampling.md` and `verdict.md` both audit against, and adding rows would silently move a
count two other documents cite. The post-repair rows live in section 6 of this file
instead.

One consequence to record rather than leave for someone to trip over. `sampling.md`
section 3 counts its samples by walking this directory and reports 43 turn-1 files, 24
turn-2 files and 39 transcript extracts. Those counts are still exact, but they are now the
counts of the pre-repair subset rather than of the whole directory. Excluding the `-post-`
stems reproduces 43, 24 and 39 precisely, so both documents remain verifiable from the tree
with one glob:

```
# sampling.md's set
ls samples/*-turn1.txt | grep -v -- '-post-' | wc -l   # 43
# this file's set
ls samples/*-turn1.txt | grep -c -- '-post-'           # 10
```

---

## Next steps

- read `references/task-mode.md` line 55 and `... Task Mode - v0.304.md` line 35 together
  with the repaired line 50 and line 30, and decide whether `unless the request is
  explicit` reopens the licence the repair closed, before any further sampling
- re-run the five `reused` Project samples with `--grant-write`, the configuration the one
  observed premature draft came from, since the current default has never produced the
  fault on either side of the repair
- if the fault still needs a rate, budget 38 Project samples per side rather than five, and
  record that five carries 33 percent power against a 1-in-13 base rate
- leave the clarification-delivery fault where `sampling.md` left it. This pass confirms
  the repair did not touch it and reproduces its rate exactly, so its own before-and-after
  test is still unrun
- raise the `Skill` tool fallback with whoever owns the harness. All five skill samples
  spent a `find /` before locating their own files and all five had it backgrounded, which
  is now the third run to record the same pathology
