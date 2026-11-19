# Iteration 15: The Product Owner parent-hub change list

## Focus

Turn the hub anatomy from iteration 11 and the hub cost from iteration 12 into a concrete Product Owner change list: which files gain what, in which order, and which existing checks must learn the new structure. This opens the conversion question as an implementation-shaped answer while staying inside a research phase.

## Findings

1. Product Owner's bootstrap has four routing surfaces that move together: Section 3 STEP 1 names the skill to load, the Command Registry table lists every command, Routing Compatibility maps commands, and Document Loading Order plus the Full DAG list every path a request may read. [SOURCE: AI Systems/Product Owner/AGENTS.md:159] [SOURCE: AI Systems/Product Owner/AGENTS.md:186] [SOURCE: AI Systems/Product Owner/AGENTS.md:200] [SOURCE: AI Systems/Product Owner/AGENTS.md:230]
2. The command registry is a closed table of six commands plus `$quick`, so a FigJam flow command must be added there and in every other place that lists commands, including the skill router and the Project kernel. [SOURCE: AI Systems/Product Owner/AGENTS.md:186]
3. The hub conversion adds two registry files at the Product Owner root and makes them stage one of Section 3, with the packet's own `ROUTER.md` as stage two, exactly as the Moneybird hub does today. [SOURCE: AI Systems/Product Owner/AGENTS.md:159] [SOURCE: AI Systems/Moneybird Accountant/SKILL.md:30]
4. Product Owner already owns the checkers a hub change stresses: a router fixture runner with a differential corpus and route contract, and a format fixture runner with its validator, both named as the system's own pre-upload verification. [SOURCE: AI Systems/Product Owner/benchmark/router/run_fixtures.sh:1] [SOURCE: AI Systems/Product Owner/benchmark/format/run_fixtures.sh:1] [SOURCE: AI Systems/Product Owner/SYNC.md:27]
5. The Project mirror needs three coordinated edits, not one: a new knowledge document for the new mode, the kernel's command list, and a kernel H1 version bump in the same change, because a Project reader sees only those files and a kernel whose rules moved while its version stood still cannot be dated. [SOURCE: AI Systems/Product Owner/SYNC.md:19] [SOURCE: AI Systems/Product Owner/SYNC.md:20]
6. Ordering is load-bearing: registries first, then the packet `ROUTER.md`, then the bootstrap pointers, then the Project mirror, then the fixtures, because every later step cites the path the earlier step created. [INFERENCE: based on the Moneybird build order in its phase record and the PO bootstrap's path list]

## Ruled Out

- Adding the diagram capability as a seventh command inside the existing skill. The registry's five lanes are artifact modes with one workflow manifest; a canvas capability needs its own packet and router.
- Editing the Project kernel before the skill side lands. The kernel would then point at a path that does not exist yet.

## Dead Ends

- Looking for a PO-level route-table checker equivalent to Moneybird's `check-route-table.py`. The PO repo has fixtures but not a hub consistency checker, so that tool would be new.

## Edge Cases

- Ambiguous input: "change list" could mean files or phases. Selected files plus ordering, because sequencing is the part most likely to break.
- Contradictory evidence: none.
- Missing dependencies: the PO fixture scripts were not executed, so their coverage of a new command is unknown.
- Partial success: none.

## Sources Consulted

- `AI Systems/Product Owner/AGENTS.md:159,186,200,230`
- `AI Systems/Moneybird Accountant/SKILL.md:30`
- `AI Systems/Product Owner/benchmark/router/run_fixtures.sh`
- `AI Systems/Product Owner/benchmark/format/run_fixtures.sh`
- `AI Systems/Product Owner/SYNC.md:19,20,27`

## Assessment

- New information ratio: 0.85
- Questions addressed: what the Product Owner hub conversion requires and in what order.
- Questions answered: the Product Owner half of the hub question, at change-list level.

## Reflection

- What worked and why: deriving the change list from the bootstrap's own path tables kept it grounded, because those tables are the actual loading contract.
- What did not work and why: expecting a hub checker in the PO repo was wrong; the fixture runners are narrower.
- What I would do differently: list the Project-mirror edits in the same breath as the skill edits, since a hub change that stops at the skill side is invisible to a Project reader.

## Recommended Next Focus

Iteration 16: verify the gates that will judge this work. Read the Product Owner parity and format gate definitions to state exactly what an embedded skill and a FigJam command must pass, so the later phases can be planned against real checks.
