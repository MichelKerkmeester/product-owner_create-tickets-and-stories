# Route Contract (executable)

Deterministic characterization of how the Barter Product Owner skill routes a
request to an artifact intent, sets Quick/Standard energy and decides whether
to ask one consolidated question, so routing behavior is testable without
invoking a model. The skill and project kernels are written against this
contract; claude.ai still interprets prose stochastically, so live adherence
testing remains mandatory.

## Files

- `route_contract.py`, the deterministic router: exact tokens, word-boundary
  keywords, artifact framing, confidence-gated semantic scoring, energy,
  disambiguation, resources and schema
- `fixtures.json`, the expected route objects, which is the test oracle
- `differential.py`, the anti-drift gate. It lifts the Smart Router pseudocode
  out of `sk-product-owner/references/router-contract.md`, executes it, and
  proves the contract agrees with it on tables, on each detection layer and on
  the whole route object
- `differential_corpus.json`, the differential inputs grouped by what each
  group exists to exercise. Fixture inputs are added automatically
- `run_fixtures.sh`, the gate runner. It runs both checks and exits 0 only
  when both pass

## Run

```bash
bash run_fixtures.sh
# or directly:
python3 route_contract.py fixtures.json
python3 differential.py
# a routing smoke test, one sample per detection layer:
python3 route_contract.py --self-check
# or inspect a single request:
python3 route_contract.py --request "\$doc write a bug report about the outage"
```

The positional argument is the fixture manifest and nothing else. A path that is
not a readable file exits 2 rather than routing the argument as a request string,
because `run_fixtures.sh` passes a bare filename and a renamed manifest used to
read as a green run over no fixtures at all. A request to inspect goes through
`--request`, and `--self-check` asserts the routing outcome each sample is owed
rather than only the schema, so a router that sends everything to Interactive
fails it.

## Route object

Every request resolves to one stable object:

```json
{
  "intent": "DOC",
  "energy": "STANDARD",
  "source": "command",
  "shape": null,
  "confidence": null,
  "needs_disambiguation": false,
  "resources": [
    "references/hvr-core.md",
    "references/conciseness.md",
    "references/doc-mode.md",
    "assets/doc-templates.md"
  ],
  "on_demand": [
    "references/human-voice-rules.md"
  ]
}
```

The schema rejects unknown or duplicate fields, so the manifest cannot drift
silently from the contract. `confidence` is `null` for command, framing and
conflict routes (those decisions do not depend on a topic score) and a float
in `[0, 1]` for semantic and fallback routes. `shape` is `STORY` or `EPIC`
on the Story lane and `null` everywhere else, and the schema rejects
both a shape on another intent and a Story route that resolved none, since
that route would load no scaffold. `resources` is what the route preloads and
`on_demand` is what it names without loading, and the schema rejects any file
that appears in both.

## Decision rules (durable rationale)

- **Exact tokens**: only a complete `$token` selects an artifact. `$task`,
  `$t`, `$bug`, `$b`, `$doc`, `$d`, `$story`, `$s`, `$prd`, `$p`, `$epic`, `$e`
  and `$task --subtask` are matched as whole tokens, never as substrings, so
  `$document`, `$docs`, `$debug`, `$stories`, `$epics` and an embedded alias
  never fire a command.
- **One Story lane, two shapes**: `$story`/`$s`/`$prd`/`$p` (Story) and
  `$epic`/`$e` (Epic) both bind STORY and never conflict with each other. The
  shape decides which single scaffold loads beside
  `references/story-mode.md`, so it is resolved before any file is read and is
  carried on the route object where a fixture can assert it. Command first,
  then framing read most-specific-shape-first, then the Story default, which
  is the only shape a topic score can honestly claim.
- **One primary intent, command wins**: an explicit command beats every
  natural-language signal, so `$doc write a bug report about the outage`
  binds DOC, not BUG. Two or more collected commands is a conflict routed to
  one consolidated question, never a silent pick.
- **Framing beats topic scoring**: explicit artifact framing ("write a bug
  report about...", "turn this into a PRD") outranks plain keyword
  scoring, matching the skill's own tie-break order.
- **Word-boundary keywords**: `bug` matches "file a bug" but never
  "debugging". `issue` and `broken` score BUG, but a synonym embedded inside
  a longer word never contributes a hit. Nine topics carry the 94 synonyms,
  and their table order is the tie-break when two topics score the same, so
  the order is part of the contract
- **A `$token` is a control, not subject matter**: token-shaped text is
  stripped before semantic scoring. The exact-token rule already refuses to
  read `$epics` as the `$epic` command, and without the strip the same text
  leaks straight back in as a keyword hit, so a statement about epics on the
  roadmap routes as a request to write one. The strip only removes tokens that
  start a whitespace-delimited word, so a price like `us$500` survives
- **A qualifier does not defeat a phrase**: real prompts write "a full
  story", "a quick story", "a proper PRD". Matching a multi-word phrase as an
  exact adjacent run meant one inserted adjective dropped a 0.85 route past
  every band into the fallback, so each gap inside a phrase now absorbs one
  intervening word. The bound is the guard: a single word per gap is an
  adjective or an article, the gap is whitespace-separated word characters
  only, so it cannot cross a comma or a full stop, and "create a task to
  write a PRD" still stays TASK because a task whose subject is another
  artifact keeps the route.
- **Confidence-gated directness**: Standard energy routes directly at 0.60
  and above and asks one consolidated question below it. Quick energy trusts
  the same score down to 0.40, and only below that falls back to Task, the
  narrow safe default from SKILL.md's Detection Sequence rule 12. This
  mirrors the live router's HIGH/MEDIUM/LOW/FALLBACK bands without asserting
  the exact prose difference between a MEDIUM confirmation line and a LOW
  clarify target, since neither changes the fixed-field route object.
- **Runtime discovery + guarded loading**: every routing call resolves
  resource names against the live `references/*.md` and `assets/*.md`
  inventory (discover, existence-check, dedupe). A renamed or deleted
  reference degrades to a smaller resource set instead of a dead path or
  crash. The guard stays lexical (`.absolute()`, never `.resolve()`), so a
  shared rule file carried as a symlink rather than as a copy still resolves
  for the existence check without walking the fence outside
  `sk-product-owner/`.
- **Always-on versus on demand**: the Human Voice card and the conciseness
  layer above it are preloaded on every route, and the full standard behind
  the card is not. Both halves are on the route object, so a fixture asserts
  the demotion rather than assuming it, and promoting the standard back into
  the always-on tier fails the gate.

## Drift guard

`sk-product-owner/references/router-contract.md` carries the same router as
pseudocode, and `SKILL.md`'s prose routing section states the two must never
drift. Nothing executes prose, so `differential.py` executes it: the fenced
block is lifted out of the markdown, run as a real module with no-op stubs for
its two side effects, and compared against this contract.

Four guards fire independently.

- **Copy parity**: the Claude Project mirror carries a third copy of the block
  and must stay byte-identical to the router contract's copy
- **Table parity**: semantic topics with their order, confidence overrides,
  thresholds, token and phrase regexes, resource lanes and the disambiguation
  checklist must match value for value, so a table drifts loudly even when no
  input happens to expose it
- **Behavior parity**: every corpus input is compared layer by layer (energy,
  commands, framing, top topic and score) and then as a whole route object, so
  a failure names which layer drifted rather than only which answer changed
- **Corpus coverage**: every command and alias, every documented false-prefix
  case and every semantic topic must be exercised, so behavior parity cannot
  pass by leaving a table untested

The two implementations report a route differently and the harness reconciles
the shapes without hiding a disagreement. The pseudocode names its sources in
prose where the contract uses a fixed enum, and it omits the confidence it had
already computed on the bare fallback branch, which the harness recovers from
the pseudocode's own scoring function.

## What this contract does not simulate

Doc Mode's source-authority and conflict gate (PENDING/BLOCKED/READY) needs
supplied source context that does not exist in a bare request string, the
same way Media Editor's tool-verification step is a live runtime concern the
oracle does not simulate. This contract fixes only the intent/energy routing
decision, not the downstream Doc drafting gate.
