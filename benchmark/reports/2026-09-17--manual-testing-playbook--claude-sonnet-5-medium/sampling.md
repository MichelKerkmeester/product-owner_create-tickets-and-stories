# Sampling measurement, Product Owner twin divergences `BG-001` and `TK-001`

Phase 4 of the twin-divergence pass. `adjudication.md` graded both pairs runtime
fault on one shared cause and held both pending sampling, and its section 8 named
the measurement. The operator approved five runs per side per pair. This file
carries that measurement and nothing else. `adjudication.md` is untouched.

Both pairs turn on the same turn type: a clarification-only turn 1 that must
reach the user through the packaging's own delivery channel. The committed run
executed each scenario once per packaging, so `skill PASS against Project FAIL`
was one sample against one sample on a nondeterministic turn.

---

## 1. Pre-registered discriminators

Written before any sample ran, validated against the committed replies, and not
revised afterwards.

### What the binding text requires of a clarification-only turn

`adjudication.md` section 1 established the binding text: `Custom
Instructions.md` line 229 read against its framing sentence at line 222, plus
lines 89, 92 and 242, and not lines 88 or 182. Read together those require four
things of a reply that asks a question and delivers no finished artifact:

- line 229 gives the clarification an address in the export lane,
  `export/NNN - {task|bug|doc|PRD|Epic}-[description]-clarification.md`, with
  `intake` substituted when no artifact was resolved, and says it carries the
  question and nothing else
- line 242 fixes the only label this runtime may report a path under,
  `Export-equivalent path:`, and bans `Path:`, `Saved:` and `Verified:`
- line 89, the kernel's ALWAYS item 14, requires the export-equivalent path and
  the self-scan line after the block
- line 92, ALWAYS item 17, requires the `HVR self-scan:` line in every delivery
  response

The skill side's mirror of the same four sits at `SKILL.md` line 208 and
`references/interactive-mode.md` line 85, with the delivery verb swapped: the
clarification is written to `export/` and read back, and the reply names the path
and prints the self-scan line.

The three elements measured in `adjudication.md` section 2 were the Deliverable
Block, the `Export-equivalent path:` label and the `HVR self-scan:` line. The
discriminators below keep all three on the Project side, add the clarification
address that line 229 actually specifies, and add the no-premature-artifact
clause each scenario's own FAIL line names.

### Discriminator, pair `TK-001`

Applies to the **turn-1 reply text alone**. Prompt
`$task I need a task for the creator payout pause feature.` PASS only when every
clause holds, otherwise FAIL with the failing clauses named.

| Clause | Skill side (`STK-001`) | Project side (`PTK-001`) |
| --- | --- | --- |
| C1, asked and did not draft | no `^#{2,4} About` together with `^#{2,4} Requirements`, and no `- [ ]` checklist line | same test |
| C2, clarification addressed | matches `export/\s*\d{3}\s*-\s*(task\|intake)[^\n]*-clarification\.md` | same test |
| C3, delivery proof | matches `read[-\s]?back` and one of `verified\|succeed` | contains `Deliverable Block` and `Export-equivalent path:` |
| C4, self-scan | contains `HVR self-scan:` | same test |
| C5, no save claim | not applicable, the skill side is required to name a real path | no match for `(?<![-\w])(Path\|Saved\|Verified):` |

Derivation. C1 is `STK-001`'s FAIL line "saves the task before Turn 2" and
`PTK-001`'s "renders the final task before Turn 2", detected by the required task
sections and the checklist grammar both scenarios name at step 4. C2 is line 229
and `SKILL.md` line 208. C3 is the packaging's delivery channel, read-back on one
side and the rendered block plus its label on the other, which is the split the
root playbook fixes at section 1. C4 is kernel line 92 and the root playbook's
global evidence requirement. C5 is `PTK-001`'s FAIL line verbatim, "prints `Path:`
or `Saved:`, claims a local file".

Reproduces: `replies/STK-001-turn1.txt` scores PASS, matching the committed PASS.
`replies/PTK-001-turn1.txt` scores FAIL on C2, C3 and C4, matching the committed
FAIL, whose recorded reason was the same three elements.

### Discriminator, pair `BG-001`

Identical in shape, with the Bug lane's own artifact markers. Prompt
`$bug The payout pause toggle silently reverts to off.`

| Clause | Skill side (`SBG-001`) | Project side (`PBG-001`) |
| --- | --- | --- |
| C1, asked and did not draft | no `1. Observed Behavior` together with `2. Expected Behavior`, and no `- [ ]` checklist line | same test |
| C2, clarification addressed | matches `export/\s*\d{3}\s*-\s*(bug\|intake)[^\n]*-clarification\.md` | same test |
| C3, delivery proof | matches `read[-\s]?back` and one of `verified\|succeed` | contains `Deliverable Block` and `Export-equivalent path:` |
| C4, self-scan | contains `HVR self-scan:` | same test |
| C5, no save claim | not applicable | no match for `(?<![-\w])(Path\|Saved\|Verified):` |

Derivation. C1 is the fixed bug structure both scenarios require at step 4,
`1. Observed Behavior` and `2. Expected Behavior` plus the four-item checklist,
against the shared FAIL line "drafts before Turn 2". C2 is `bug-mode.md` line 63
and its Project mirror at Bug Mode line 46, the only two mode documents that name
the delivery act outright. C3, C4 and C5 are as above.

Reproduces: `replies/SBG-001-turn1.txt` scores PASS, matching the committed PASS.
`replies/PBG-001-turn1.txt` scores FAIL on C2, C3 and C4, matching the committed
FAIL and its recorded reason.

### Calibration check on the rest of the committed Project set

Not part of either pair, run to confirm the three Project-side elements separate
the committed PASSes from the committed FAILs rather than failing everything.
`replies/PID-001-turn1.txt` and `replies/PDK-002-turn1.txt`, the two committed
Project PASSes, both carry `Deliverable Block`, `Export-equivalent path:` and
`HVR self-scan:`, so both satisfy C3, C4 and C5. They miss C1 or C2 only because
they are different scenarios: `PID-001`'s turn 1 is required to deliver a task,
and `PDK-002`'s clarification carries the `doc` artifact word rather than `bug`.
The two committed pair FAILs carry none of the three. The elements discriminate.

### What is measured separately rather than folded in

- a turn 1 that skips the question and renders the finished artifact fails C1.
  `adjudication.md` section 7 recorded that both Task Mode documents license this
  identically, at skill line 50 and Project line 30, "Ask one comprehensive
  question unless the request already contains enough direction or uses an
  explicit command", and `$task` is an explicit command. C1 scores it against the
  scenario's own line, which requires the question, and it is reported in its own
  row rather than pooled with the plain-chat failures
- whether a file reached disk is not a verdict clause on either side. The
  committed skill verdicts could not rest on it, because the harness in force
  during that run rebuilt the scratch tree on `--resume`. It is audited per
  sample from the session transcript and reported beside the distribution

---

## 2. Run configuration

Twenty new samples, five per side per pair, each a full two-turn conversation in a
fresh session. Harness invoked from the `AI Systems` directory:

```
HARNESS_SCRATCH=<one per sample> HARNESS_MODEL=claude-sonnet-5 HARNESS_EFFORT=medium \
  "z — Parity Gate/run_packaging.sh" "Product Owner" <skill|project> '<turn 1>' \
  --session $(uuidgen) --noweb
```

then the same script with `--resume <that uuid>` and the turn-2 prompt. Each sample
got its own `HARNESS_SCRATCH` so the twenty could run concurrently, and each session
uuid keys its own scratch subtree, so no capture collided. All forty calls returned a
non-empty reply file and every stderr held only its `session:` line.

`--noweb` is kept because the committed run used it on every call and the earlier
adjudication samples did too. Dropping it would have made the new samples a different
configuration from both.

Prompts were extracted from the scenario tables rather than retyped. The turn-1 and
turn-2 cells of the skill and Project files are byte-identical per turn, checked by
comparison: 57 and 240 characters for the Task lane, 53 and 277 for the Bug lane.

### The Project write-tool change, and whether the zero-write claim holds

It holds, and the default did not change what the Project side delivered, but the
change is not a null one and the prior Project samples are not the same configuration.

- in all ten new Project samples, across both turns, there were zero calls to `Write`,
  `Edit`, `NotebookEdit` or `Bash`, so nothing was attempted and nothing was denied.
  No file exists under any of the ten Project scratch trees
- in the earlier configuration all ten Project samples did call `Bash`, once or twice,
  twelve calls between them. Read from the transcripts, every one was a directory
  listing or a `find` used to locate the knowledge documents, and none wrote anything.
  So the zero-file result is the same in both configurations. The committed run's own
  two Project transcripts no longer exist on disk, so that run's tool use is taken from
  `README.md` section 6, which records one Project scenario writing a real file and the
  other six staying clean
- withholding `Bash` removed the tool every prior Project sample used to find its
  knowledge set. `Glob` took that role in all ten new samples, and every one of them
  then opened its lane document, so retrieval survived the change. This is a real
  difference in mechanism, which is why the prior Project samples keep their own rows
  below rather than being pooled with the new ones

The file-write question is settled from the transcripts rather than from a scratch-tree
walk alone, because a write tool takes an absolute path and could have landed outside
the tree. No tool input in any of the twenty transcripts named a path outside its own
scratch subtree.

### Harness behaviour worth recording

- nine of the ten new skill samples first called the `Skill` tool with
  `product-owner`, got `Unknown skill: product-owner`, and fell back to a
  filesystem-wide `find / -iname "SKILL.md" -path "*product-owner*"`. In one sample
  that find hit the 120-second limit and was moved to the background. This is the same
  pathology that made one earlier skill sample ungradable, recorded in
  `adjudication.md` section 3 as inconclusive
- in one of those samples the find returned a listing that included the authoritative
  `sk-product-owner` tree outside the scratch copy. It opened nothing there. The string
  `manual-testing-playbook` appears in none of the twenty transcripts, so the isolation
  the harness asserts was not breached, but it is asserted only inside the scratch tree
  and a filesystem-wide find reaches past it
- one Project sample called an `Artifact` tool on turn 2 and was told it is disabled
  for the session, and another called `ToolSearch` on turn 1. Both are the runtime
  looking for a rendering surface the CLI does not have

---

## 3. Samples on disk

Every sample counted below is persisted beside this file, one file per turn:

```
benchmark/reports/2026-09-17--manual-testing-playbook--claude-sonnet-5-medium/samples/
```

43 samples, named `<pair>-<arm>-<nn>-turn<n>.txt`, with `reused` in the stem for the
samples carried over from `adjudication.md` and `committed` for the four from the
committed run. `manifest.csv` in that directory carries one row per sample with its
origin, its turn-1 verdict, the clauses it failed and the session uuid it came from.
`<stem>.transcript.txt` beside each sample is a short extract of that session's tool
calls, marking which were write tools, plus the listing of that scratch tree's export
directory after both turns.

Counted by walking the directory: 43 turn-1 files, 24 turn-2 files (the twenty new
samples plus the four committed ones, whose turn 2 also exists in `replies/`), 39
transcript extracts, and `manifest.csv`. 43 manifest rows against 43 turn-1 files, and
43 against the sum of the four cell totals in section 4. The counts agree.

---

## 4. Distribution

Scored by the pre-registered discriminator against the turn-1 reply text. New and
reused samples are kept apart, and the Project side's reused samples are additionally
a different configuration, as section 2 explains.

### Pair `TK-001`, prompt `$task I need a task for the creator payout pause feature.`

| Arm | Origin | Samples | PASS | FAIL, plain chat | Reported separately | Config |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| skill | new | 5 | 3 | 2 | 0 | current |
| skill | reused | 7 | 4 | 2 | 1 stub | matches on turn 1 |
| skill | committed | 1 | 1 | 0 | 0 | writes available |
| **skill total** |  | **13** | **8** | **4** | **1** |  |
| project | new | 5 | 0 | 5 | 0 | current |
| project | reused | 7 | 1 | 5 | 1 premature draft | writes available |
| project | committed | 1 | 0 | 1 | 0 | writes available |
| **project total** |  | **13** | **1** | **11** | **1** |  |

Every plain-chat failure in this lane, on both arms, failed the same three clauses:
C2, C3 and C4. No clarification address, no delivery proof, no self-scan line. The
failure is character-identical across the two packagings.

The one reused skill sample reported separately is the stub recorded in
`adjudication.md` section 3: its captured reply is two lines about a timed-out
background command rather than a clarification turn. The discriminator scores it FAIL
on C3 and C4, and it is held out of the plain-chat count because the reply is a harness
artefact. The one reused Project sample reported separately is the premature draft:
it skipped the question and rendered a complete task on turn 1, failing C1 and C2.

Matched configuration only, five per side: skill 3 of 5 PASS against Project 0 of 5.
Fisher exact one-sided p = 0.083.

### Pair `BG-001`, prompt `$bug The payout pause toggle silently reverts to off.`

| Arm | Origin | Samples | PASS | FAIL, block not named | FAIL, all three absent | Config |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| skill | new | 5 | 5 | 0 | 0 | current |
| skill | reused | 2 | 2 | 0 | 0 | matches on turn 1 |
| skill | committed | 1 | 1 | 0 | 0 | writes available |
| **skill total** |  | **8** | **8** | **0** | **0** |  |
| project | new | 5 | 2 | 3 | 0 | current |
| project | reused | 3 | 1 | 2 | 0 | writes available |
| project | committed | 1 | 0 | 0 | 1 | writes available |
| **project total** |  | **9** | **3** | **5** | **1** |  |

The two Project failure modes are not the same defect. The committed `PBG-001` carried
none of the three elements. Every one of the five re-run failures carries the
`Export-equivalent path:` label and the `HVR self-scan:` line and renders the question
inside a fenced block, and fails C3 only because the reply never uses the words
`Deliverable Block`. That is a milder miss, and the committed failure's own form does
not reproduce in eight attempts.

Matched configuration only, five per side: skill 5 of 5 PASS against Project 2 of 5.
Fisher exact one-sided p = 0.083.

### What the transcripts add

The failing samples had the governing document open.

- all five new Project `$bug` samples opened `Product Owner - Templates - Bug Mode -
  v0.203.md`, whose line 46 reads "Render the question as its own Deliverable Block,
  labelled `export/[###] - bug-[description]-clarification.md`", and all five also
  opened the Interactive Mode document. Three then produced a reply with no Deliverable
  Block
- all five new Project `$task` samples opened Task Mode, which carries nothing about a
  clarification, and two also opened the Interactive Mode document, whose line 62 reads
  "A clarification is delivered like any other deliverable. The render-before-respond
  rule has no exception". All five failed, including both that opened it
- both failing new skill samples read `SKILL.md`, which carries the clarification
  export rule at line 208, and one of the two also read
  `references/interactive-mode.md`, whose line 85 states the same rule. Both delivered
  plain chat
- the disk corroborates the skill scores independently of the reply text. Each of the
  three compliant new skill `$task` samples wrote `001 - ...-clarification.md` on turn 1
  and numbered its turn-2 task `002`. Both failing samples wrote nothing on turn 1 and
  numbered their turn-2 task `001`, which is only possible if the clarification never
  existed. All five new skill `$bug` samples wrote the clarification and numbered the
  report `002`

---

## 5. Verdict per pair

### `TK-001`: a packaging property, category runtime fault

The Project side did not deliver the clarification in 5 of 5 matched samples and in
12 of 13 overall. That is not a draw. The skill side delivered it in 3 of 5 matched
samples and 8 of 12 gradable overall, so the direction the committed run recorded is
the true direction, and the difference is a rate difference rather than a capability
difference: both packagings produce both behaviours in this lane, and the Project side
produces the failing one nearly always.

Two qualifications belong with that verdict.

- the committed pair verdict is not itself reproducible. It needs skill PASS and
  Project FAIL together, which the measured rates put at roughly three paired draws in
  five. In the other two the pair agrees, both FAIL. So the pair should not be carried
  forward as a settled twin divergence, and `twin_divergence.py`'s one-sample
  comparison could not have known which it had drawn
- at exactly five per side the rate difference is p = 0.083 and is not established on
  the matched samples alone. It is established by the Project side's near-deterministic
  failure across both configurations, 1 PASS in 13, and by the identical failure
  clauses on both arms

Category is runtime fault, not a rule gap. The operator's test for a rule gap, both
sides returning both verdicts, does not fire on the matched five per side: the skill
arm returns both, the Project arm returns only FAIL. Pooling the prior-configuration
Project samples would make it fire, since one of those passed. The evidence against
reading that as a rule gap is direct: the failing samples had the rule open in the
transcript, and `adjudication.md` section 4 showed both runtimes stating the rule
correctly when asked about it neutrally.

### `BG-001`: a draw, category runtime fault

The committed `PBG-001` failure does not reproduce. In 8 Project samples of the
identical prompt, 0 reproduced a reply missing all three elements, and every one
carried the `Export-equivalent path:` label and the `HVR self-scan:` line. The skill
side passed 8 of 8. So the recorded divergence, skill PASS against Project FAIL on the
three-element test, was the luck of one sample.

A milder Project-side defect does survive, and it is a separate item rather than a
rescue of the pair: 5 of 9 Project samples deliver the clarification under its label
and self-scan but never name it a Deliverable Block, which Bug Mode line 46 requires in
those words. Under the pre-registered discriminator that is a FAIL, and at five per
side, 5 of 5 against 2 of 5 gives p = 0.083. Whether it should be a FAIL is a grading
question this measurement cannot settle, because `PBG-001`'s own PASS line for turn 1
asks only for the question "under an export-equivalent label" while the lane document
it loads asks for the block by name.

What would settle each residual:

- for `TK-001`, the matched-configuration contrast at eight samples per side. If the
  rates hold at roughly 60 percent against 0 percent, eight per side reaches p = 0.013
  and six already reaches p = 0.030. Running the same eight after adding the delivery
  verb to `Custom Instructions.md` line 229 and to both Task Mode documents is the
  before-and-after test `adjudication.md` section 8 named, and it is the only one that
  separates the kernel's weaker wording from Task Mode's silence
- for `BG-001`, a decision on whether a fenced clarification under the
  `Export-equivalent path:` label counts as rendering the Deliverable Block when the
  runtime has no Canvas panel, taken against Bug Mode line 46 and `PBG-001`'s PASS
  line, and then five more Project samples scored under the settled clause. Nothing
  about the rate changes with more samples until that clause is decided, because every
  failure in this lane turns on it alone

---

## 6. Findings that belong to neither pair

- the premature-draft reading is real and reported separately, per its own rule. One
  Project `$task` sample skipped the question entirely and rendered a complete task on
  turn 1. Both Task Mode documents license that identically, at skill line 50 and
  Project line 30, "Ask one comprehensive question unless the request already contains
  enough direction or uses an explicit command", and `$task` is an explicit command.
  Scored against the scenario's own line, which requires the question, it is a FAIL on
  C1 and C2. It appeared once in 13 Project samples and never in 13 skill samples
- `adjudication.md` section 3 overstated the Bug lane's Project reproduction rate. It
  recorded "All three new Project samples rendered the clarification with the
  `Export-equivalent path:` label and the self-scan line" and concluded 3 of 3
  compliant. That is accurate about the two elements it names and it drops the third,
  the Deliverable Block, which is the element the committed `PBG-001` failure note
  listed first and which Bug Mode line 46 requires by name. Scored on all three, those
  same samples are 1 of 3, not 3 of 3. This is a defect in my own adjudication, found
  by applying a discriminator derived from the committed verdict rather than from the
  earlier note. It does not change that pair's verdict, since the committed failure's
  own form still fails to reproduce, but it does mean the Bug lane was not as clean as
  section 3 read
- `adjudication.md` section 5's sentence "the Project 6 of 8" for the Task lane holds
  up and hardens. Against 13 Project samples the lane is 1 compliant in 13

---

## Next steps

- treat `BG-001` as closed and drop it from the twin-divergence list. The committed
  Project failure does not reproduce in eight attempts, so re-grading the pair from the
  committed run alone would have recorded noise as a finding
- keep `TK-001` open as a Task-lane item rather than a pair verdict. The Project side
  fails this clarification turn in 12 of 13 samples, which is worth a fix, and the pair
  framing is the wrong container for it because the skill side fails the same way
- decide the `Deliverable Block` naming clause before spending any more samples on the
  Bug lane, since every remaining Project failure there turns on that one clause and no
  sample count moves it
- run the eight-per-side matched contrast on the Task lane before and after adding the
  delivery verb to `Custom Instructions.md` line 229 and both Task Mode documents,
  which is the measurement `adjudication.md` section 8 asked for and the only one that
  separates the kernel's weaker wording from Task Mode's silence
- raise the `Skill` tool fallback with whoever owns the harness. Nine of ten new skill
  samples spent a filesystem-wide `find` before locating their own files, one of those
  finds timed out, and the same pathology already cost the earlier adjudication one
  ungradable sample
