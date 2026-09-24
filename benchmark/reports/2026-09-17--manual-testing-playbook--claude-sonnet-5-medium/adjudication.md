# Twin divergence adjudication, Product Owner, 2026-09-17 run

Two pairs disagreed in this run, both skill PASS against Project FAIL. Confirmed
with `benchmark/grader/twin_divergence.py` against this directory: `BG-001` and
`TK-001`, 5 agreed, 2 disagreed, 0 not settled, 0 unpaired.

| Pair | Category | Cause |
| --- | --- | --- |
| `TK-001` | runtime fault | shared, reproduces on both packagings |
| `BG-001` | runtime fault | same defect, same shared cause |

One cause, not two. Neither pair is a rule gap and neither is a parity gap.

---

## 1. The rule, quoted on both sides

The behavior at issue is turn 1 of both scenarios: the runtime asks one
consolidated question and must deliver that question through its packaging's own
delivery channel, not as plain chat.

The rule exists in three places on each side, in matching terms.

**Always-loaded layer.** The skill's `Resource Loading Levels` table names
`sk-product-owner/SKILL.md` as ALWAYS (`SKILL.md` line 133), and `AGENTS.md`
line 144 requires reading it "before processing any request".

- `sk-product-owner/SKILL.md` line 208: "A clarification is exported too, in the
  routed artifact's lane, as `export/[###] - {task|bug|doc|PRD|Epic}-[description]-clarification.md`,
  using `intake` in place of the artifact word when no artifact was resolved. It
  holds the question and nothing else: no draft, no partial artifact, no answer"
- `claude project/Custom Instructions.md` line 229: "Clarification:
  `export/NNN - {task|bug|doc|PRD|Epic}-[description]-clarification.md`, using
  `intake` in place of the artifact word when no artifact was resolved. It
  carries the question and nothing else, and the artifact later takes the next
  number in that lane"

The Project entry is weaker in form. It names the label where the skill names the
act, and its framing sentence at line 222 calls the list "a naming convention
rather than paths the Project wrote". It is not absent, and section 4 shows the
runtime reading it as binding.

**Mode layer, `$bug` only.** Both sides carry the render-the-question rule inside
the Bug lane's own mode document, which a `$bug` request conditionally loads.

- `sk-product-owner/references/bug-mode.md` line 63: "Stopping to ask still
  produces a file. Export the question as
  `export/[###] - bug-[description]-clarification.md`, holding the question and
  nothing else, so the request is not lost between sessions"
- `claude project/knowledge/Product Owner - Templates - Bug Mode - v0.203.md`
  line 46: "Stopping to ask still produces a deliverable. Render the question as
  its own Deliverable Block, labelled
  `export/[###] - bug-[description]-clarification.md`, holding the question and
  nothing else, so the request is not lost between sessions"

Neither Task Mode document carries it. `references/task-mode.md` and
`Product Owner - Templates - Task Mode - v0.303.md` each contain zero
occurrences of `clarif` in any inflection. That silence is symmetric, so it is
not a parity finding.

**Interactive layer, both lanes.** Both sides carry a section headed
`Export Contract For A Clarification`, opening on the same sentence with the
delivery verb swapped for the packaging.

- `sk-product-owner/references/interactive-mode.md` line 85: "A clarification is
  exported like any other deliverable. The skill's export-before-respond rule has
  no exception"
- `claude project/knowledge/Product Owner - System - Interactive Mode - v0.404.md`
  line 62: "A clarification is delivered like any other deliverable. The
  render-before-respond rule has no exception"

Both documents open on the same trigger. Their `When to Use` lists both include
"Artifact type, scope, user value, acceptance conditions or bug evidence are
missing", which a low-context `$task` or a one-line `$bug` satisfies. The routing
row the two playbook files cite is byte-identical: skill
`references/interactive-mode.md` line 124 and the Project knowledge document
line 101 both read "**Direct Task or Bug** (`$task`/`$bug`) | Context-specific
question → Wait → Process → Deliver".

So the rule reached both packagings, through the same trigger, with the same
force. That closes the parity-gap option by the standard it is defined on: there
is no side that lacks it.

`Custom Instructions.md` lines 88 and 182 are not the binding text for a
clarification turn and never were. Line 88 reads "Render the Deliverable Block
before any commentary, since this Project cannot save a local file", and line 182
is the same instruction as delivery-protocol step 6. Neither mentions a
clarification. What binds is line 229 read against line 222, plus lines 89, 92
and 242, and the two knowledge documents above.

---

## 2. What the replies did

Counted by reading each file, not from a note. Markers checked in both
spellings each time: `Export-equivalent path`, `export/NNN` inline, a fenced
block, a `## Deliverable Block` heading, `self-scan` and `self scan`, `Path:`,
`read-back`.

`replies/PTK-001-turn1.txt`: seven numbered prose questions. Zero occurrences of
`Deliverable Block`, `Canvas`, `export`, `export-equivalent`, `self-scan`,
`HVR`, `Path:` or `Verified`. Turn 2 is a correct task block with a label and a
self-scan, which does not repair turn 1.

`replies/PBG-001-turn1.txt`: seven prose evidence questions. Same zero counts on
every marker. Turn 2 renders the bug inside a Deliverable Block with a label and
a self-scan.

`replies/STK-001-turn1.txt` and `replies/SBG-001-turn1.txt`: both carry the
export path, the read-back line and the self-scan line, and both created no
draft.

The observation in the results notes is sound. The category is not what the notes
say.

---

## 3. Second direction: reproduce both lanes on both packagings

Same harness, same prompts character for character, `HARNESS_MODEL=claude-sonnet-5`,
`HARNESS_EFFORT=medium`, `--noweb`, one `HARNESS_SCRATCH` per sample, turn 1 only.
Ten new skill runs and fourteen new Project runs, the two probes in section 4
included. Every reply was classified against the same marker set, and every reply
whose markers were not unanimous was then read in full.

**`TK-001` lane, prompt `$task I need a task for the creator payout pause feature.`**

| Packaging | Compliant | Plain chat, no delivery | Other |
| --- | ---: | ---: | ---: |
| skill, 8 samples including the committed one | 5 | 2 | 1 inconclusive |
| project, 8 samples including the committed one | 1 | 6 | 1 premature draft |
| project, retrieval line withheld, 3 samples | 1 | 2 | 0 |

The two skill defects are the finding that settles this. Both are the exact
recorded Project failure, produced by the skill packaging:

- one skill sample asked the consolidated context question in plain chat, wrote
  nothing to `export/`, printed no path, no read-back and no self-scan line, and
  the scratch tree's `export/` is empty
- a second skill sample did the same and closed by offering a fast path on
  defaults

The inconclusive skill sample wrote the clarification file to disk but its
captured final reply is a two-line stub about a timed-out background command, so
its reply cannot be graded either way.

The Project side is not uniformly incapable. One sample opened on a
`## Deliverable Block` heading with `**Export-equivalent path:**
export/001 - task-creator-payout-pause-clarification.md` and closed on the
self-scan line, which is full compliance with `PTK-001`'s turn 1 contract.

The premature-draft sample is a different defect worth naming: it skipped the
question entirely and rendered a complete five-group task with a label and a
self-scan on turn 1. Both Task Mode documents license that reading, identically,
at skill line 50 and Project line 30: "Ask one comprehensive question unless the
request already contains enough direction or uses an explicit command". `$task`
is an explicit command. That ambiguity is symmetric and is a real rule gap, but
it is not the gap either of these two pairs turns on.

**`BG-001` lane, prompt `$bug The payout pause toggle silently reverts to off.`**

| Packaging | Compliant | Plain chat, no delivery |
| --- | ---: | ---: |
| skill, 3 samples including the committed one | 3 | 0 |
| project, 4 samples including the committed one | 3 | 1 |

All three new Project samples rendered the clarification with the
`Export-equivalent path:` label and the self-scan line, two of them inside a
fenced block. The committed `PBG-001` failure does not reproduce in three
attempts. It is the outlier, not the pattern.

---

## 4. Third direction: does the always-loaded Project kernel bind on its own

Two probes, both pointed at the open question rather than at the behavior.

**Neutral rule-knowledge probe, both packagings.** Prompt: "when your next reply
will only ask a clarifying question and deliver no finished artifact, what does
your contract require that reply to contain? Quote the governing sentences
verbatim and name the document each one came from."

The Project runtime answered from `Custom Instructions.md` alone, quoting line
229, ALWAYS items 13, 14 and 17, and the self-scan shape, and concluded: "since a
clarifying question is not a finished artifact, it still renders as a Deliverable
Block (containing only the question, per the 'carries the question and nothing
else' clause), labeled with the `-clarification.md` export-equivalent path ...
the self-scan line and export-equivalent path are still mandatory." It cited no
knowledge document.

The skill runtime answered by quoting `references/interactive-mode.md` lines 85
to 98 and `AGENTS.md` steps 6 to 8, and concluded that a clarification-only reply
must still be exported, read back, and reported with the path, the read-back line
and the self-scan line.

Both runtimes state the rule correctly when asked. Neither reads its own wording
as permitting plain chat. That closes the rule-gap option.

**Retrieval line withheld.** Three Project `$task` samples run with
`--no-retrieval`, so no knowledge document was pointed at by any wording. One of
the three still produced `Export-equivalent path:
export/001 - intake-creator-payout-pause-clarification.md` and the self-scan
line, using the `intake` fallback that appears nowhere but line 229 and the
Interactive Mode document it never opened. The always-loaded Project kernel binds
a clarification turn on its own, empirically, not only on a careful reading.

---

## 5. Verdicts

**`TK-001`: runtime fault.** The rule is stated in the skill's always-read
`SKILL.md` at line 208, in the Project's always-loaded kernel at line 229, and in
the matching `Export Contract For A Clarification` section on both sides. Both
runtimes state it correctly on request. Both omit it on live turns: the skill
2 of 8 and the Project 6 of 8. The committed pair caught the shared defect on one
side and not the other, which is a sampling outcome rather than a packaging
property.

**`BG-001`: runtime fault.** Same rule, carried additionally in each side's own
Bug Mode document at skill line 63 and Project line 46, both naming the delivery
act outright. The Project side honoured it in 3 of 3 re-runs of the identical
prompt. The single committed failure is the runtime acting against a rule it had
in the lane document it loads for that command.

**One cause, not two.** Both pairs are the same defect on the same turn type: a
clarification turn delivered as chat instead of through the packaging's delivery
channel. The rate differs by lane because the Bug lane restates the rule in its
mode document and the Task lane does not, on both sides. The Task lane's higher
Project failure rate is consistent with the Project kernel naming the label where
the skill kernel names the act, but that is a robustness difference in redundancy,
not a rule that failed to arrive, and it cannot be the pair's category while the
skill side reproduces the same failure.

**Not the capability leak.** `capability-leak.md` covers a Project runtime given
`Write`, satisfying the delivery rule by saving a file and handing back a path.
That mechanism is absent here. Every Project sample in both lanes, committed and
new, wrote zero files: `find` over each scratch tree's `export/` returns nothing
for all fourteen Project runs, and the failing replies render nothing at all
rather than substituting a path for a deliverable. Different cause.

---

## 6. Defects found in the report

- `README.md` section 7 claims "the skill runtime reliably wraps its
  clarification in the export-plus-self-scan contract and the Project runtime did
  not". Both halves are wrong. The skill omits the export entirely in 2 of 8
  samples of the same prompt, and the Project applies the contract in 3 of 3
  `$bug` re-runs. The section's conclusion, "a packaging-specific consistency
  gap", does not survive a second sample
- `README.md` section 6 says the kernel "states, in the kernel itself, that a
  clarification is one of the Deliverable Block types (line 229 ...)" and that
  "None of this is behind a `knowledge/` pointer". Line 229 states a naming
  convention, under a framing sentence at line 222 that says so explicitly. The
  sentence that actually states a clarification is delivered like any other
  deliverable is in `knowledge/`, at Interactive Mode line 62 and Bug Mode line
  46. The report reached the right category for the wrong reason, and the
  next-steps entry built on it ("the rule is already in the kernel and just needs
  consistent application") understates what a fix would have to touch
- `README.md` section 6 folds `PTK-001` and `PBG-001` into one bullet as the same
  miss. They share a category but not an exposure: the Bug lane restates the rule
  in the document that command loads and the Task lane does not, and the
  reproduction rates separate accordingly, 3 of 4 against 1 of 8
- Not a defect, checked and cleared: section 3's claim that the harness rebuilds
  the scratch tree on `--resume` was true of the harness in force during the run,
  at commit `0cb24d9`, where `build_skill` and `build_project` ran unguarded. The
  `REBUILD` guard landed in `ff2f2d1`, the commit that recorded this report. The
  note is stale against today's script and accurate about the run
- Not a defect, checked and cleared: `hvr-lint.csv` holds 28 rows with exactly 3
  `clean=True`, matching section 8, and `knowledge/` holds 38 files, matching
  section 1's correction of the runtime's own count of 40

## 7. Defects found in the framing given to me

- The framing names `Custom Instructions.md` lines 88 and 182 as the kernel's
  statement of the Deliverable Block requirement and asks whether those bind a
  clarification turn. Neither line mentions a clarification, so neither can
  settle it either way. The binding text is line 229 read against line 222, and
  the runtime reaches it from the kernel alone with the retrieval line withheld
- The framing treats "both skill PASS against Project FAIL" as a property of the
  two pairs. It is a property of one sample each. Re-run, the skill fails the
  `TK-001` lane and the Project passes the `BG-001` lane
- The framing offers the three categories as exhaustive with an escape hatch.
  Both pairs fit `runtime fault` cleanly, so the hatch was not needed here, but
  the reproduction surfaced a fourth thing worth recording separately: Task Mode's
  "unless the request ... uses an explicit command" caveat, identical on both
  sides, licenses skipping the turn-1 question that both playbook files require.
  That is a genuine rule gap, it is symmetric, and it belongs to neither pair

## 8. What would settle what remains

The one number I would not carry forward without more samples is the Task lane's
Project failure rate against its skill failure rate, 6 of 8 against 2 of 8. That
gap is large enough to be real and small enough, at these sample sizes, to be
noise. The measurement that would settle it: twenty turn-1 samples per packaging
on the `$task` prompt, then the same twenty after adding the delivery verb to
`Custom Instructions.md` line 229 and to both Task Mode documents. If the Project
rate moves to the skill rate on the kernel edit alone, the redundancy asymmetry is
load-bearing and worth fixing as a parity item in its own right. If both move
together only after the Task Mode edit, the mode-document silence is the cause and
the packaging difference was noise.

## Next steps

- Re-grade neither pair from this report alone. A one-sample twin comparison on a
  nondeterministic turn cannot distinguish a packaging property from a draw, and
  `twin_divergence.py` has no way to know that, so the pair verdicts need a
  sample count before they carry weight
- Add the delivery verb to the two documents that name only the label or nothing
  at all: `Custom Instructions.md` line 229 and both Task Mode documents, matching
  `bug-mode.md` line 63 and its Project mirror, which are the only mode documents
  that state the act and the only lane with a clean reproduction rate
- Decide the Task Mode "unless the request uses an explicit command" caveat on its
  own merits, since it contradicts what `STK-001` and `PTK-001` both require of
  turn 1 and it produced a premature full-task draft in one Project sample
- Run the twenty-sample measurement in section 8 before spending any fix budget on
  the kernel-versus-mode-document question
