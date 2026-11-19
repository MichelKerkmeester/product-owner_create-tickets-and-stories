# Review Iteration 2

## Dispatcher

- Route: `Resolved route: mode=review target_agent=deep-review`
- Mode: review, dimension `security`, iteration 2 of 5 (JSONL-derived; the dispatch number agrees)
- Budget profile: `verify` (11 analysis calls used of 12 soft / 13 hard)
- Lifecycle: `new`, sessionId `2026-11-10T18:34:20Z`, generation 1
- Scope lock: the 89 files in `reviewScopeFiles`; findings below stay inside them
- Prior findings were read and are neither re-reported nor re-litigated; the one overlap is named as an extension in "Edge Cases"

## Dimension

`security`, the second of four. This pass owns the writer's trust boundary: what the browser-executed program reads from disk, what it interpolates into the logged-in page, what the shared validator and the Sync Loop scripts can write, and whether the public repository carries a secret or a private ClickUp link. The operator's four focus items are covered alongside it and each one is answered in "Edge Cases".

## Files Reviewed

- `AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md` - `:381` (image-source contract), `:396-412` (`esc`, `GRAY`, `inline`, `hold` restore), `:402-403` (upload registration), `:408` (link build), `:531` (local file read, page writer), `:544-551` (marker removal), `:556-589` (verify block and its delivery sentence), `:802` (session-folder sentence), `:871` (local file read, columns program), `:896-907` (columns verify)
- `AI Systems/Product Owner/benchmark/format/validate-output-format.cjs` - `:22-35` (`--write` flag gate), `:1602` (the only write call)
- `AI Systems/Product Owner/benchmark/format/run_fixtures.sh` - `:38`, `:49` (how the validator is invoked)
- `AI Systems/Product Owner/benchmark/gates/rule_parity.py` - `:191`, `:217` (declaration and content reads)
- `AI Systems/z — Claude Project Sync Loop/systems.py` - `:1-40` (declaration docstring)
- `AI Systems/z — Claude Project Sync Loop/systems.cjs` - write-call grep, no hits
- `AI Systems/z — Claude Project Sync Loop/README.md` - `:149`, `:200` (`resync_statement.py`)
- `AI Systems/Product Owner/SYNC.md` - `:18`, `:135`
- `AI Systems/Product Owner/sk-product-owner/SKILL.md` - `:6` (frontmatter version)
- `AI Systems/Product Owner/README.md` - `:128`, `:657`
- `AI Systems/Product Owner/.gitignore` - `:15` (push-target containment)
- `AI Systems/Product Owner/claude project/knowledge/Product Owner - Assets - Task Templates.md` - `:277-288` (feedback section shape)

## Findings - New

### P0 Findings

None.

### P1 Findings

1. **The page writer reads and uploads any path a markdown image names, so the session-folder contract is prose only** -- `AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:531` -- `inline()` registers every image whose source is not `https` as a local file at `:402-403` without inspecting it, and the upload loop then reads it with `fs.readFile(path.join(pwd, ...))` at `:531` (page writer) and `:871` (columns program). `path.join` normalizes `..`, so a body line such as `![logo](../../../.ssh/id_rsa)` resolves outside the Aside session folder, is base64-encoded, and is pasted into the logged-in ClickUp tab as `image/png` under the raw source string as its filename. ClickUp then stores the bytes as a page attachment and the content becomes visible to everyone with document access. The same section states the contract the code does not enforce, "An image with any other source is a file in the Aside session folder" at `:381`, repeated at `:802`.
Finding class: `security` (input containment on a file read that feeds a third-party upload).
Scope proof: both read sites are in the reviewed target (`:531`, `:871`); the registration site that makes the path attacker-chosen is `:402-403` in the same program; no containment check, `startsWith`, `resolve` comparison, extension allowlist or `existsSync` guard appears anywhere between them.
Affected surface hints: the browser-first page writer program, the side-by-side columns program, the image-source prose contract at `:381` and `:802`, and `mcp-click-up/SKILL.md` Section 1, which tells the agent to run the writer with a body it composed.
Case: a doc body that contains `![chart](../../../../.ssh/id_rsa)` is written through the program as documented; the upload loop reads the key, and the page ends up with an attachment holding it.

```json
{"type":"claim","claim":"A non-https markdown image source is read from disk without confirming it resolves inside the Aside session folder, and the bytes are uploaded into the ClickUp page.","evidenceRefs":["AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:402-403","AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:531","AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:871","AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:381","AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:802"],"counterevidenceSought":"Searched the referenced section for a guard between registration and read (resolve, normalize, startsWith, allowlist, existsSync) and for prose that forbids outside paths; the only guard-like text is the session-folder sentence the code does not apply.","alternativeExplanation":"The body is authored by the assistant, so a traversal source would have to arrive through copied user content or a transcript, and the only reader is the operator's own workspace. That lowers likelihood but not impact, and the program is documented as the default path for every doc page.","finalSeverity":"P1","confidence":0.78,"downgradeTrigger":"Downgrade to P2 if `mcp-click-up/SKILL.md` Section 1 or the page-writer prose is shown to instruct the agent to reject any image source that is not a bare filename, and the check is verifiable before the read."}
```

### P2 Findings

2. **`esc` escapes HTML metacharacters but no link scheme, so a `javascript:` href survives into the pasted page** -- `AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:408` -- the link branch builds `<a href="${esc(href)}">`, and `esc` at `:396` touches only `&`, `<`, `>` and `"`. A markdown link whose target is `javascript:` or `data:text/html` therefore reaches the editor as a live attribute value; `esc` correctly blocks attribute breakout, so this is a scheme-policy gap rather than an injection hole. The verify block at `:560-572` counts blocks, dividers, gaps, columns, gray runs and leftovers and never inspects link targets, so nothing in the report would show it.
Finding class: `security` (sanitizer covers one concern, not the other).
Scope proof: the constructor is the single place every markdown link passes through (`:408`), and no later stage rewrites hrefs.
Affected surface hints: the page writer's `inline()` helper, the columns program's label builder at `:843`, and the delivery sentence at `:589` that treats a clean report as delivery.
Case: a body line `[open](javascript:alert(document.domain))` is written through the program; the page carries a link whose target is script, and the report still reads clean.

3. **`SYNC.md`'s standing version sentence names skill 1.2.11.0 while the same file records the move to 1.2.15.0** -- `AI Systems/Product Owner/SYNC.md:18` -- the paragraph that explains the two independent version fields says "`sk-product-owner/SKILL.md` frontmatter carries the skill version, currently 1.2.11.0". The frontmatter reads `version: 1.2.15.0` at `sk-product-owner/SKILL.md:6`, `README.md:128` states `sk-product-owner` 1.2.15.0, and `SYNC.md:135`, the newest maintenance entry, records "`sk-product-owner` to v1.2.15.0". A reader who takes the standing paragraph as the current state is three minor versions behind inside one file, which is the failure the file already logged at `:28` ("`SYNC.md` stated kernel v0.10.0 two bullets above the correct v0.11.1").
Finding class: `traceability` (hand-authored parity note states a superseded version as current).
Scope proof: the three conflicting sites are all inside the review target; the SKILL.md frontmatter is the mechanical source of truth and cannot drift silently because it is machine-read.
Affected surface hints: `SYNC.md` Section 1 version paragraph, the operator's version check before a Project upload, and any release note that quotes SYNC.md instead of the frontmatter.
Case: an operator confirming which skill version a Project upload carries reads `SYNC.md:18`, sees 1.2.11.0, and reports the 1.2.15.0 Project files as ahead of their source.

## Traceability Checks

| Check | Scope | Result |
|-------|-------|--------|
| `secrets_scan` (security) | all 12,470 tracked files in the public repo, patterns `pk_`, `ghp_`, `sk-`, `AKIA`, PEM headers, tracked `.env`/`.pem`/`.key` | No live credential. Every hit is a placeholder (`pk_1234567_ABCDEFGHIJKLMNOP`, `ghp_your_token_here`) or a token-format example inside install guides, plus an `AKIA` match that is an AWS access-key **id** inside an expired S3 presigned URL |
| `private_link_scan` (security) | `app.clickup.com` links in tracked files | No private workspace link. Task links use team id `000000000` with `EX-1001`..`EX-1006` placeholders (`claude project/knowledge/Product Owner - Examples - Story - Epic.md:62-73`); the rest are public settings pages. Scratch doc ids named in the packets (`2kyq4d0p-123315`) are ids, not links, and belong to scratch pages |
| `push_target_containment` (security) | `claude project/local/Product Owner - Local - Push Targets.md` | Contained: `.gitignore:15` ignores `claude project/local/`, the path is present on disk and untracked, so the doc/team targets `AGENTS.md:117` requires to stay local are not committed |
| `write_surface` (security) | validator `--write`, Sync Loop scripts, gate scripts | Contained: `--write` cannot be combined with an explicit file list (`validate-output-format.cjs:34`), its only write is `fs.writeFileSync(file, output)` over the enumerated skill sources at `:1602`, `systems.cjs` contains no write call, and `rule_parity.py` only opens files for reading (`:191`, `:217`) |
| `spec_code` (core) | code versus this section's own prose contract | Partial, as in iteration 1: the draw on `:381` and `:802` is crypto-free prose, yet both are contradicted by the read sites. No `spec.md` requirement was mapped this iteration |

## Integration Evidence

- Page writer entry point: `AI Systems/Product Owner/AGENTS.md:117` routes a doc page push to the writer that `mcp-click-up/SKILL.md` Section 1 names; the writer program under review is that writer, so the P1 read site is on the default path for every doc page, not an optional extra. Named exactly because the severity depends on it.
- Columns program: `mcp-click-up/references/mcp-tools.md:802` requires a local screenshot to sit in the Aside session folder the REPL reads as `pwd`, and `:871` is the second read site with the same gap.
- Validator `--write`: invoked from `benchmark/format/run_fixtures.sh:38` in read-only mode and from an operator directly for reformatting; its flag exclusivity is what keeps the write scoped.
- Parity gate declaration: `z — Claude Project Sync Loop/systems.py` holds the frozen pair map (`unmirrored_sources`, `adapted_pairs`, `vendored_shared_copies`). It is a declaration only; `systems.cjs` performs no writes, and the resync helper is `resync_statement.py` (`README.md:149`, `:200`), which rewrites one declared statement rather than the mirror tree.

## Edge Cases

- **Operator focus, item 1 (does the verify logic really prove a clean page).** Examined at `:556-589`. The block-level counters, the reload-before-read and the `leftovers` match are sound evidence that the paste landed. The weakness is the import comparison: `report.importDiff = norm(MD).filter((l) => !got.has(l))` at `:584` compares against a `Set`, so duplicate loss, ordering loss and any line already present elsewhere cannot fail. That is the same blindness iteration 1 recorded as P1 ("cannot fail on a lost divider or a lost indent"), so it is recorded here as an **extension of the open P1, not a new finding**. The security-relevant addition is that link targets are never compared, which is finding 2.
- **Operator focus, item 2 (flipped Mark-as-done rule and its byte-parity twin).** Reviewed only for security exposure: the rule is regex line matching over an in-memory line array, with no I/O, no evaluation and no interpolated path, and iteration 1 established that `MARK_AS_DONE`, `contentNeighbour` and `markAsDoneFindings` are textually identical in both validators. No security finding. The silent fixture stays **unverified**, because `cat -A` is unavailable on this host and I did not spend a call on `od -c`; it is carried, not cleared.
- **Operator focus, item 3 (feedback ticket template consistency with Task Mode and the mirrors).** Only the outer shape was compared: the source asset's Section 6 and the Project mirror's Section 6 open on the same two sentences and the same `{Team} - {Feature} - Feedback #{Round} - {App}: {Logic | UI/UX}` title, and both state the one-app-one-kind rule. Item-level field comparison against `references/task-mode.md` and the new example is **not done** and is deferred to iteration 3, where `spec_code` and `checklist_evidence` need those files anyway. This iteration must not be read as clearing it.
- **Operator focus, item 4 (version and count drift).** Addressed for the version axis and it produced finding 3. The count axis (README file counts, residency numbers, changelog totals) is **not** checked; it belongs with the traceability sweep in iteration 3.
- **Scope boundary on the secrets scan.** Scanning 12,470 tracked files found presigned Figma S3 URLs with an `AKIA…` key **id** inside `benchmark/reports/…/transcript-turn-*.md`. Those live under `benchmark/reports/`, which is outside the declared review target, and the signatures expired on 2026-11-02, so no finding is raised. Recorded so the clean result is not read as a repo-wide clearance.
- **P1 input path.** The markdown body is composed by the agent, so a traversal source is unlikely to be invented; the realistic route is copied user content, pasted ticket text or a transcript folded into a doc. Likelihood is scored down, impact is not, hence P1 with a named downgrade trigger rather than P0.
- **Reduced verification.** The P1 rests on reading both read sites and the registration site; I did not execute the program, so the runtime claim "ClickUp stores the bytes" is inference from `new File([bytes], name, {type:"image/png"})` at `:539` and the prose at `:513-524`. The code path itself is directly observed.

## Confirmed-Clean Surfaces

- `esc()` escaping order at `:396`: `&` is escaped first, so `&lt;` produced from a later `>` cannot be double-escaped into a live `<`. Attribute values are double-quoted everywhere they are built (`:408`, `:843`), so the unescaped `'` is not an escape route.
- `hold`/`keep` restore at `:412`: the sentinel is `\u0000<index>\u0000` and the restore runs after `esc`, so a markdown-supplied sentinel can only duplicate an already-escaped fragment or inject the literal `undefined`; it cannot reach unescaped HTML.
- Interpolation of markdown into the tool code: every injection is `JSON.stringify(...)` inside a template substitution, so backticks, quotes, `${` and newlines in the body cannot break out of the code string.
- Credential handling: the route is OAuth 2.1 with PKCE and reads no API key (`:57`), and the tracked guides carry placeholders only.
- Push-target secrecy: gitignored and untracked (verify above).

## Ruled Out

- **`--write` as an arbitrary-path write.** The flag is mutually exclusive with an explicit file list and the write iterates the enumerated sources only.
- **A committed secret anywhere in the public repo.** All token-shaped hits are documentation placeholders; the one high-entropy credential-shaped match is an AWS key id inside an expired signature, out of scope.
- **A committed private ClickUp link.** Links use a zeroed team id and placeholder task ids; push targets are gitignored.
- **Sync Loop scripts writing outside their folder.** `systems.cjs` has no write call; `rule_parity.py` only reads; the resync helper rewrites one declared statement rather than a mirror tree.
- **The flipped Mark-as-done rule as an injection or I/O surface.** Pure string matching over an in-memory array, identical in both twins.
- **Attribute breakout through `esc`.** Double-quoted attributes and `"` in the escape set; this does not extend to the scheme gap in finding 2.

## Next Focus

- Dimension: `traceability` (core `spec_code` and `checklist_evidence`, plus the deferred operator items)
- Focus area: map packets 026, 027 and 028 requirement rows to the code and prose that answer them, then finish the two deferred operator items, the feedback-ticket item-level parity across source, Task Mode and the two Project mirrors, and the count axis of README/SYNC drift
- Reason: two security passes have now cleared the trust boundary except for the P1 and its P2 neighbour, and the operator named template parity and count drift explicitly; iteration 3 is the pass that carries `checklist_evidence`, which is still pending
- Rotation status: correctness complete, security complete, traceability next, maintainability last
- Blocked carry-forward: the silent `- - -` fixture (no `cat -A` on this host; use `od -c`), and the twin validator's one-line offset difference between its checker and formatter callsites
- Productive carry-forward: reading a program's own prose as the oracle worked again (finding 1 is a sentence at `:381` the code does not apply), and pattern-scanning the tracked tree with the repo's own `git grep` is a cheap, high-yield security sweep
- Required evidence: `spec.md` requirement rows and `tasks.md` checklist rows in packets 026/027/028, `sk-product-owner/references/task-mode.md` feedback section, both Project Task Templates mirrors, the new Feedback Ticket example, and every version or count claim in `README.md`, `SYNC.md` and the changelogs

## Verdict

`CONDITIONAL`. No P0. One new P1 (ungated local image read feeding a ClickUp upload) joins the P1 carried from iteration 1, so the verdict cannot rise to PASS. Two new P2 findings are advisory: the unfiltered link scheme and the stale skill version in `SYNC.md`. Completeness was verified against the state projection, not assumed.

Review verdict: CONDITIONAL
