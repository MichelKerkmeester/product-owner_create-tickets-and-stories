# Deep Review Report: Product Owner ClickUp session work

## 1. Executive Summary

- **Verdict:** CONDITIONAL
- **hasAdvisories:** true
- **Active findings:** P0 0, P1 2, P2 13 (after de-duplicating repeated registry rows and applying the iteration 5 downgrade)
- **Scope:** 89 files changed in outer commits 246b3f54..47b8b333, which carry Product Owner packets 026, 027 and 028, the vendored `mcp-click-up` copy of Skilled commit 4e46d8c0cb and the Sync Loop validator, fixtures and `systems.py`
- **Executor:** cli-pi, `opencode-go/deepseek-v4.1-flash` at max effort, 5 iterations (stop policy max-iterations). The llmgateway DevPass route returned `402 billing_error` on the first dispatch and was not retried
- **Operator review focus:** The ClickUp page writer converter and verify logic (does it really prove a clean page), the flipped Mark-as-done validator rule and its byte-parity twin, feedback ticket template consistency with Task Mode and the Claude Project mirrors, and version or count drift across READMEs, SYNC.md and changelogs

## 2. Planning Trigger

`/speckit:plan` is recommended for the two P1 findings. Both are small and local.

```json Planning Packet
{
  "triggered": true,
  "verdict": "CONDITIONAL",
  "hasAdvisories": true,
  "activeFindings": [
    {"id": "R2-P1-001", "severity": "P1", "file": "AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:531"},
    {"id": "R3-P1-001", "severity": "P1", "file": "AI Systems/Product Owner/specs/system/028-feedback-ticket-template/spec.md:93"}
  ],
  "remediationWorkstreams": ["WS1 page writer local-file containment", "WS2 028 verification evidence", "WS3 P2 advisories"],
  "specSeed": ["Constrain local image uploads to a basename in the Aside session folder with an image extension", "Cite validate_parity.py for mirror equality in 028"],
  "planSeed": ["Patch both upload sites in Skilled mcp-tools.md section 8 and re-vendor", "Edit 028 spec.md REQ-003 and its tasks verify line"],
  "findingClasses": ["trust_boundary", "spec_evidence_mismatch", "doc_count_drift", "duplication", "contract_gap"],
  "affectedSurfacesSeed": ["Skilled mcp-click-up/references/mcp-tools.md", "AI Systems/Product Owner/mcp-click-up/", "AI Systems/Product Owner/specs/system/028-feedback-ticket-template/", "AI Systems/Product Owner/sk-product-owner/README.md", "AI Systems/Product Owner/SYNC.md"],
  "fixCompletenessRequired": true
}
```

## 3. Active Finding Registry

| ID | Sev | Title | Dimension | File:line | Fix |
|----|-----|-------|-----------|-----------|-----|
| R2-P1-001 | P1 | Ungated local image read feeds a ClickUp upload | security | `mcp-click-up/references/mcp-tools.md:531`, `:871` | Accept only a basename inside the Aside session folder with a png, jpg, gif or webp extension, and set the MIME type from it |
| R3-P1-001 | P1 | 028 REQ-003 claims mirror equality from a phrase-count gate | traceability | `specs/system/028-feedback-ticket-template/spec.md:93` | Cite `validate_parity.py product-owner` (67/67), which checks declared pairs, and keep `rule_parity.py` for phrase counts |
| R1-P1-001 | P2 (downgraded) | Report fields `dividers`, `gray`, `checklist` carry no required value, so only `importDiff` catches a lost divider | correctness | `mcp-tools.md:583` | State the expected counts or compare them with the source |
| R1-P2-002 | P2 | `- - -` divider falls through to the bullet branch | correctness | `mcp-tools.md:416` | Add `- - -` to the divider test |
| R1-P2-003 | P2 | `--write` inserts dividers from the original neighbour lookup | correctness | `benchmark/format/validate-output-format.cjs:1594` | Recompute neighbours after each insert, or insert bottom-up |
| R1-P2-004 | P2 | Import normalizer exists in three diverged copies | maintainability | `mcp-tools.md:579` | One shared normalizer block reused by the programs |
| R2-P2-001 | P2 | `javascript:` link scheme survives `esc()` | security | `mcp-tools.md:408` | Allow only http, https and mailto hrefs |
| R2-P2-002 | P2 | SYNC.md standing sentence says skill 1.2.11.0, frontmatter says 1.2.15.0 | traceability | `SYNC.md:18` | Update the sentence |
| R3-P2-001 | P2 | 027 REQ-002 evidence names a file count HEAD no longer reproduces (73 vs 74) | traceability | `specs/system/027-mark-as-done-between-dividers/spec.md:81` | Restate as "all source files" or the current count |
| R3-P2-002 | P2 | `sk-product-owner/README.md` frontmatter says 1.2.6.0 while SKILL.md says 1.2.15.0 | traceability | `sk-product-owner/README.md:12` | Bump the README version |
| R3-P2-003 | P2 | The two READMEs disagree on the worked example count | traceability | `sk-product-owner/README.md:26` | Align the count |
| R4-P2-001 | P2 | `gapsLeft` computed by two expressions across the two browser programs | maintainability | `mcp-tools.md:694` | Use one expression |
| R4-P2-002 | P2 | Leftover marker set listed three times with three member lists | maintainability | `mcp-tools.md:570` | One shared pattern |
| R4-P2-003 | P2 | checkbox-form fixture carries a near-miss assertion inside a violation file | maintainability | `benchmark/format/run_fixtures.sh:172` | Move the near-miss into its own silent fixture |
| R4-P2-004 | P2 | The two fixture harnesses pin unequal subsets in two helper styles | maintainability | `z — Claude Project Sync Loop/run_fixtures.sh:487` | Share one expectation list |

Evidence, claim-adjudication packets and edge cases for each row are in `iterations/iteration-00N.md`, where N is the digit after `R`.

## 4. Remediation Workstreams

1. **WS1 (P1):** contain the page writer's local image read (R2-P1-001), upstream in Skilled, then re-vendor into Product Owner
2. **WS2 (P1):** correct the 028 verification evidence (R3-P1-001)
3. **WS3 (P2 advisories):** version and count drift (R2-P2-002, R3-P2-001, R3-P2-002, R3-P2-003), converter edge cases (R1-P2-002, R2-P2-001, R1-P1-001), validator `--write` (R1-P2-003), duplication cleanup (R1-P2-004, R4-P2-001, R4-P2-002, R4-P2-003, R4-P2-004)

## 5. Spec Seed

- The page writer accepts a local image only by basename, inside the Aside session folder, with an image extension
- Link hrefs in the converter are limited to http, https and mailto
- 028 states mirror equality through `validate_parity.py`

## 6. Plan Seed

- Patch `mcp-tools.md` section 8 upload sites and the columns twin in Skilled, bump mcp-click-up, re-vendor
- Add `- - -` to the converter divider test and a scheme allowlist to links
- Edit 028 `spec.md` REQ-003 and `tasks.md` T004 verify text
- Fix the four version and count drifts in one pass

## 7. Traceability Status

- **Core `spec_code`:** partial. 026 and 027 requirements map to code and gates. 028 REQ-003 cites a gate that cannot fail on its claim (R3-P1-001)
- **Core `checklist_evidence`:** partial. 027 REQ-002 evidence count drifted (R3-P2-001)
- **Overlay `skill_agent`:** pass. Task Mode, Task Templates and routing agree on the feedback ticket shape
- **Overlay `feature_catalog_code`:** pass for the output-format-validator entry
- **Overlay `playbook_capability`:** pass for the 14 story-mode scenarios
- **Overlay `agent_cross_runtime`:** not applicable
- **AC_COVERAGE:** exempt (Level 1 packets)

## 8. Deferred Items

- The byte-parity description of the twin validators is behavioural, not byte-level. Reference parity compares behaviour and passed
- Kernel has no feedback-ticket export label or doc-count clause, recorded in 028 Known Limitations

## Dimension Expansion Map

No pivots ran. Swept directions: none recorded. Remaining frontier: live ClickUp verification of nested indents and `- - -` dividers.

## 9. Search Ledger

- **searchCoverage:** required bug classes state_transition, trust_boundary, spec_evidence_mismatch, doc_count_drift, duplication. Ruled out: state_transition, doc_count_drift, duplication (as blockers)
- **candidateCoverage:** assertion_coverage, contract_gap, count_drift, doc_code_drift, doc_count_drift, doc_drift, duplicate_logic, duplication, formatter_non_convergence, harness_parity and more
- **hasSearchDebt:** true. SL-307 (iteration 3, `benchmark/gates/rule_parity.py`, count_drift) stayed blocked. The verdict stays CONDITIONAL
- **ruledOutCandidates and cleanSearchProof:** recorded per iteration, starting with SL-005 (twin validators agree on markAsDoneFindings)

## 10. Audit Appendix

- **Convergence:** stop reason maxIterationsReached (operator-fixed 5). Graph convergence stayed STOP_BLOCKED on uncovered_dimensions in the graph signal while the reducer registry marks all four dimensions covered. Severity counts rose 4, 7, 11, 15, 18 raw rows. Iteration 5 added no new finding and downgraded one
- **Claim adjudication:** passed for iterations 1 to 4. Iteration 5 recorded `passed: false` because it re-emitted the two confirmed P1 rows as delta findings without new typed packets. Their packets exist in iterations 2 and 3
- **Adversarial self-check (orchestrator):** both active P1s re-read at HEAD. `mcp-tools.md:531` and `:871` read `path.join(pwd, file)` with no containment. `spec.md:93` cites `rule_parity.py`, whose docstring says a pair without the phrase is not a gap. Both confirmed
- **Core Protocols:** spec_code partial, checklist_evidence partial
- **Overlay Protocols:** skill_agent pass, feature_catalog_code pass, playbook_capability pass, agent_cross_runtime not applicable
- **Sources reviewed:** the 89 scope files, packet docs for 026 to 028, both validators and fixture corpora, `rule_parity.py`, `systems.py`
