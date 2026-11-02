---
title: "Implementation Plan: Phase 2, company context fixtures"
description: "Three writers, one per company, run in parallel from briefs cut from the manifest. The orchestrator reads every file against its manifest row, then runs the values check, the em dash grep, the per-file Human Voice lint and the naming and vocabulary greps before committing in both repos."
trigger_phrases:
  - "company fixtures plan"
  - "one writer per company"
  - "fixture values check"
  - "fixture verification commands"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.2 -->
# Implementation Plan: Phase 2, company context fixtures

<!-- SPECKIT_LEVEL: 2 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|--------|-------|
| **Language/Stack** | Markdown fixtures, one Python values check, shell greps |
| **Framework** | Product Owner benchmark fixtures, which the phase 003 runner copies into each sandbox's `context/` when a scenario names them |
| **Storage** | Barter repo and the Product Owner public repo, under `AI Systems/Product Owner/benchmark/fixtures/companies/` |
| **Testing** | `scratch/check_manifest_values.py`, `grep`, `wc`, and `benchmark/grader/lint_replies.py --brief` on each file |

### Overview
The manifest in `spec.md` section 3 is the contract. A setup step writes a values check that reads that table, then cuts one brief per company from it. Three writers, one per company, write their context document and attachments in parallel. The orchestrator reads every file against its row, the shared values and the status traps, then runs the checks in section 5 and commits the folder in both repos. Nothing outside `benchmark/fixtures/companies/` changes.
<!-- /ANCHOR:summary -->

---

<!-- ANCHOR:quality-gates -->
## 2. QUALITY GATES

### Definition of Ready
- [x] The operator approved the plan and its 23-scenario catalog
- [x] Manifest, writing rules, shared values and status traps fixed in `spec.md`
- [ ] Phase 001 validated, or the orchestrator chose to run this phase beside it

### Definition of Done
- [ ] Every check in section 5 green on the committed state
- [ ] Every row of `acceptance-criteria.md` Met
- [ ] Fixtures committed in both repos, pushed only on the operator's go-ahead
<!-- /ANCHOR:quality-gates -->

---

<!-- ANCHOR:architecture -->
## 3. ARCHITECTURE

### Pattern
Manifest first, parallel writers, one reading pass, mechanical checks, commit.

### Key Components
- **Manifest**: the one table in `spec.md` section 3 that names every file, its kind, its citing scenarios and its hard values
- **Values check**: `scratch/check_manifest_values.py`, which parses that table, confirms each file sits in its company folder, and greps each backticked value with a fixed-string match
- **Writer briefs**: one per company in `scratch/`, holding that company's manifest rows, the shared values, the status traps, the writing rules and the corpus files to read for tone
- **Writers**: three Opus 5.5 agents at effort medium through the `opus-medium` definition, or the Agent tool's `model: opus` if that definition does not load
- **Fixtures**: 3 context documents and 22 attachments under `AI Systems/Product Owner/benchmark/fixtures/companies/<company>/`

### Data Flow
Manifest, then values check and briefs, then three writers, then the orchestrator's read, then the checks, then a commit in each repo. Phase 003 then names the files in each scenario's `- Attachments:` bullet, and the runner copies each one to `<sandbox>/context/<basename>`.

### Writer brief contents
- The company's manifest rows, pasted, with the instruction to copy each backticked value character for character
- The shared values and status traps that touch the company
- All eleven writing rules, rule 8 with the lint's exact hard checks: em dash, semicolon, curly quote, bullet ending in a full stop, second ellipsis, hard blocker word
- For tone and density, four corpus files: `Product Context/Tasks & Stories/Stories/Onboarding/26-08-13 - Creator - Onboarding v2 - Password reset.md`, `Product Context/Tasks & Stories/Stories/Onboarding/26-08-13 - Epic - Creator - Onboarding v2.md`, `Product Context/Tasks & Stories/Tasks/Feed v2.5/Function Rulesets/26-07-13 - BE - Fv2.5 - Function Ruleset - Trending-260713161113.md` and `Product Context/Tasks & Stories/Tasks/Creator/Bugs/26-06-15 - FE - Creator - Auto-Capitalization Not Respecting Device Settings.md`. A writer takes their density of numbers and names, never their facts
- Loomlist only: `AI Systems/Product Owner/sk-product-owner/assets/task-templates.md` section 3 for the parent task
- Fernhouse only: `AI Systems/Product Owner/sk-product-owner/assets/story-template.md`, so the draft departs from it in the ways the status traps name and no others
- A closing self-check the writer runs before returning: the em dash grep, the lint loop and the values check on its own folder
<!-- /ANCHOR:architecture -->

---

<!-- ANCHOR:affected-surfaces -->
## FIX ADDENDUM: AFFECTED SURFACES

| Surface | Current Role | Action | Verification |
|---------|--------------|--------|--------------|
| `benchmark/fixtures/companies/` | Does not exist | Create | Section 5, checks 1 to 12 |
| Skill sandbox build in the runner | Its rsync excludes `benchmark`, so no fixture enters the skill tree unasked | Unchanged | `grep -n '"--exclude", "benchmark"'` on the runner in `benchmark/reports/2026-09-25--manual-testing-playbook--claude-sonnet-5-medium/run/` |
| Project sandbox build in the runner | Copies `claude project/` only, and deletes top-level names holding `review` | Unchanged. Phase 003 adds the `context/` copy | REQ-009 keeps fixture names clear of `review` |
| Runner isolation proof | Fails on a name holding `testing-playbook` or a `benchmark` directory | Not a consumer here | REQ-009 and check 8 |
| Product Owner format gate | Walks `sk-product-owner/` and the kernel only | Not a consumer, so the rough draft adds no finding | `validate-output-format.cjs` with no argument, same result before and after |
| Playbook root and scenario files | Owned by phase 003 | Cite the manifest names | Phase 003's `load_playbook` check |

Required inventories:
- `grep -rn "fixtures/companies" "AI Systems/Product Owner"` before writing: no hit until phase 003 links the folder
- The scenario attachments table in `spec.md` against the plan's catalog: 23 rows, each scenario at the company the catalog names
<!-- /ANCHOR:affected-surfaces -->

---

<!-- ANCHOR:phases -->
## 4. IMPLEMENTATION PHASES

Follow the ordered tasks in `tasks.md`. It owns the Setup, Implementation and Verification phase checkboxes and task state.

Ordered steps:
1. Check the scenario attachments table against the plan's catalog
2. Write the values check and prove it fails on a planted miss
3. Create the three company folders and cut the three writer briefs
4. Dispatch the three writers in parallel
5. Read every returned file against its manifest row, the shared values and the status traps, and send misses back to that company's writer
6. Run checks 1 to 12 in section 5, fix in scope, and rerun all of them after any fix
7. Commit in Barter, then in the Product Owner public repo with no attribution line
8. Record the evidence in `acceptance-criteria.md`, `implementation-summary.md` and the `goal.md` log, and push only on the operator's go-ahead
<!-- /ANCHOR:phases -->

---

<!-- ANCHOR:testing -->
## 5. TESTING STRATEGY

| Test Type | Scope | Tools |
|-----------|-------|-------|
| Contract | Exact file set and every hard value (checks 1 and 2) | `find`, `scratch/check_manifest_values.py` |
| Voice | Em dash and the Human Voice hard checks on every file (checks 3 and 4) | `grep`, `lint_replies.py --brief` |
| Shape | Context and attachment length, context sections, dated headers, template markers (checks 5, 6, 7, 10, 12) | `wc`, `grep`, `head` |
| Isolation | Names, links, brands, test vocabulary (checks 8 and 9) | `find`, `grep` |
| Conflict | The digest pair disagrees on one claim and declares no authority (check 11) | `grep` |
| Manual | Realism, shared values, status traps, no real person | The orchestrator's read of all 25 files |

`lint_replies.py` runs on one file at a time. Given a folder it reads only the top level and writes `hvr-lint.csv` into the parent folder, which would leave a stray file inside `benchmark/fixtures/`.

Run from the repository root:

```bash
F="AI Systems/Product Owner/benchmark/fixtures/companies"
LINT="AI Systems/Product Owner/benchmark/grader/lint_replies.py"
P="AI Systems/Product Owner/specs/013-po-realistic-playbook-opus-rerun/002-company-context-fixtures"

# 1. Exact set: prints 25
find "$F" -type f | wc -l

# 2. Every manifest file sits in its company folder and holds every value in its row: exit 0
python3 "$P/scratch/check_manifest_values.py"

# 3. No em dash (U+2014): prints nothing
grep -rn $'\xe2\x80\x94' "$F"

# 4. Human Voice lint per file: 25 lines reading clean, exit 0
find "$F" -name "*.md" -print0 | xargs -0 -n1 python3 "$LINT" --brief

# 5. Context documents: each 150 to 250 lines
wc -l "$F"/*/*-context.md

# 6. Context sections: prints 11 for each context document
grep -cE "^## (Product and surfaces|Personas and roles|Glossary|Services and integrations|Teams and discipline codes|Feature codes|Platforms and app versions|Currencies and locales|Key flows|Known constraints|Analytics conventions)$" "$F"/*/*-context.md

# 7. Attachments: each 20 to 150 lines
find "$F" -name "*.md" ! -name "*-context.md" -exec wc -l {} +

# 8. Names: both print nothing
find -E "$F" -type f ! -regex '.*/(roamstay|loomlist|fernhouse)-[a-z0-9-]+\.md'
find "$F" -type f \( -iname "*review*" -o -iname "*readme*" -o -iname "*benchmark*" -o -iname "*testing-playbook*" \)

# 9. Fictional and self-contained: each prints nothing
grep -rnE "https?://|www\." "$F"
grep -rnwE "Barter|Stripe|Adyen|PayPal|Klarna|Mollie|DHL|UPS|DPD|GLS|FedEx|PostNL|Booking\.com|Expedia|Airbnb|Notion|Shopify|Slack|Firebase|Twilio|SendGrid|Mailchimp|Visa|Mastercard|Apple Pay|Google Pay|Figma|ClickUp|Jira" "$F"
grep -rniE "\b[SP](ID|TK|BG|DK|ST|EP|IR)-[0-9]{3}\b|playbook|benchmark|fixture|scenario|grader" "$F"

# 10. Template markers: lists no file other than the two given inputs
grep -rlE "Resolution Checklist|Mark as done|A story is used to define|\*\*Checklist\*\*|\*\*User Story\*\*" "$F"

# 11. The digest pair: the first two print 0, the third prints nothing
grep -c "07:00" "$F/loomlist/loomlist-notification-spec.md"
grep -c "08:00" "$F/loomlist/loomlist-email-template-inventory.md"
grep -niE "canonical|source of truth|authoritative|retired|deprecated|superseded|outdated|approved" "$F/loomlist/loomlist-notification-spec.md" "$F/loomlist/loomlist-email-template-inventory.md"

# 12. Dated headers: prints nothing
find "$F" -name "*.md" ! -name "*-context.md" -exec sh -c 'head -5 "$1" | grep -qE "2026-0[1-9]-[0-3][0-9]" || echo "no dated header: $1"' _ {} \;
```

The values check exits 1 on the first run of its own planted-miss test, with one value removed from a copy of one fixture, before it is trusted on the real folder.
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

| Dependency | Type | Status | Impact if Blocked |
|------------|------|--------|-------------------|
| Approved scenario catalog | Internal | Green | Names and values would drift from the scenarios |
| Phase 001 | Internal | Yellow, no content dependency | Only the parent's transition rule orders the two phases |
| `lint_replies.py` and `hvr-core.md` | Internal | Green | No voice gate |
| `opus-medium` agent definition | Internal | Yellow | Writers fall back to `model: opus`, noted in the goal log |
| Operator go-ahead for the push | External | Pending | Commits stay local |
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

- **Trigger**: A check fails and cannot be fixed inside the fixtures folder, or the operator rejects the fixtures
- **Procedure**: Before the commit, delete `AI Systems/Product Owner/benchmark/fixtures/companies/`. After it, revert the fixture commit in each repo. No other file changes, so nothing else needs undoing
<!-- /ANCHOR:rollback -->

---


---

<!-- ANCHOR:phase-deps -->
## L2: PHASE DEPENDENCIES

```
Setup (values check, folders, briefs) ──┬──► Roamstay writer ───┐
                                         ├──► Loomlist writer ───┼──► Read and checks ──► Commit
                                         └──► Fernhouse writer ──┘
```

| Phase | Depends On | Blocks |
|-------|------------|--------|
| Setup | Approved catalog | Writers |
| Writers | Setup | Read and checks |
| Read and checks | All three writers | Commit |
| Commit | Every check green | Phase 003 citing the names |
<!-- /ANCHOR:phase-deps -->

---

<!-- ANCHOR:effort -->
## L2: EFFORT ESTIMATION

| Phase | Complexity | Estimated Effort |
|-------|------------|------------------|
| Setup | Low | About 20 minutes |
| Core Implementation | Med | About 45 minutes, three writers in parallel |
| Verification | Med | About 45 minutes, read, checks and fixes |
| **Total** | | **About 2 hours** |
<!-- /ANCHOR:effort -->

---

<!-- ANCHOR:enhanced-rollback -->
## L2: ENHANCED ROLLBACK

### Pre-deployment Checklist
- [ ] Every check in section 5 green on the working tree
- [ ] Only files under `benchmark/fixtures/companies/` staged in either repo
- [ ] The public repo commit message carries no attribution line

### Rollback Procedure
1. Revert the fixture commit in the Barter repo
2. Revert the matching commit in the Product Owner public repo
3. Confirm `find "AI Systems/Product Owner/benchmark/fixtures/companies" -type f` prints nothing
4. Tell phase 003 the names are withdrawn if it has started citing them

### Data Reversal
- **Has data migrations?** No
- **Reversal procedure**: N/A
<!-- /ANCHOR:enhanced-rollback -->

---
