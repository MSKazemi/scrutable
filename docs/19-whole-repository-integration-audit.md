# Whole-repository integration audit

**Audit date:** 2026-08-12  
**Repository:** `MSKazemi/mohsen`  
**Branch:** `main`  
**Baseline:** `b2c5bd2fcfc0bc0c7826e18cbbb6ccdcfc42bb41`  
**Scope:** every file in the baseline tree, all internal joins, current branch and pull-request state, and the coordinated corrections recorded with this audit

## Verdict

All 92 baseline files were fetched from GitHub and reviewed individually. Every
Markdown file was read for meaning and cross-document consistency; every YAML and
JSON file was parsed; all declared schemas, identifiers, relationship targets,
examples, coverage records, links, and named paths were checked together.

After the corrections in this commit, `main` is internally coherent at the documented
protocol, structured-data, and schema levels. This is a point-in-time, independently
reproducible structural result, not a claim that the framework is complete, that its
rules are continuously enforced, or that it guarantees product outcomes.

## Method and limits

The audit combined:

1. line-by-line semantic review of every baseline file;
2. JSON and YAML parsing;
3. JSON Schema compilation and validation of all compatible catalog and example
   records;
4. global uniqueness, target-resolution, self-edge, and `depends_on` cycle checks;
5. example-to-catalog and example-answer joins;
6. prose-manifest count, preserved-source, source-path, and catalog-reference checks;
7. internal Markdown path and heading-fragment checks;
8. `ai-context.yaml` path checks; and
9. live GitHub inspection of `main`, open pull requests, historical merges, branches,
   and reported commit status checks.

“Word by word” is treated here as a complete human semantic read, not as a guarantee
that prose has one objectively correct interpretation. Mechanically decidable claims
were also tested so that the verdict does not depend only on reading judgment.

## Deterministic baseline results

| Check | Result |
|---|---:|
| Files | 92 |
| Markdown / YAML / JSON | 55 / 29 / 8 |
| Structured questions / unique IDs | 131 / 131 |
| Declared relationship edges / unresolved targets | 510 / 0 |
| Direct self-edges / `depends_on` cycles | 0 / 0 |
| Numbered prose questions / mapping groups | 396 / 43 |
| Compressed / guidance-only / exact / unmodeled mappings | 388 / 8 / 0 / 0 |
| Internal Markdown links / unresolved links | 172 / 0 |
| Example instances / answers | 4 / 1 |
| JSON or YAML parse failures | 0 |
| Schema, graph, example, coverage, link, or context-path errors | 0 |

After adding this audit and the coordinated corrections, the same suite reports 93
files (56 Markdown, 29 YAML, and 8 JSON), 184 resolving internal Markdown links, and
zero errors or warnings. Question, relationship, coverage, and example counts remain
131, 510, 396, and 4/1 respectively. The draft domain-pack manifest validates, and
negative fixtures confirm that a reviewed pack cannot rely on a rejecting approval or
an empty conditional approval.

The coverage manifest refers to 95 of 131 catalog IDs. Thirty-six catalog records
are not referenced by the seven-bank manifest: `business.referral.001`,
`core.catalog-quality.001`, `product.pivot-comparison.001`,
`team.communication.001`, `core.domain-pack.001` through `.008`, the eight
`team.change-*` records, the eight `team.continuity-*` records, and the eight
`operations.sensing-*` records. They were added by later structured graph work and are
not
missing targets or invalid records.

## Integration defects corrected

This audit corrected the following cross-file defects without changing published
question IDs:

- made Markdown and YAML canonical state everywhere and described graph files and
  databases only as derived projections;
- distinguished relationship fields embedded in question templates from relationship
  records carried by run data;
- consolidated three incompatible run directory examples into the canonical layout
  in `templates/run-manifest.md`;
- replaced a nonconforming answer example and an invalid lifecycle-stage example;
- aligned coverage and gate vocabularies, including `proceed_with_conditions`;
- identified `next-question-v1` separately from the controlling-bottleneck score and
  labeled richer prioritization as a future policy candidate;
- kept accepted risk separate from verified evidence;
- updated stale schema, link, pull-request, and branch counts;
- reframed the next automation as a read-only validator callable by CI or agents,
  with no mandatory CLI, API, database, or service;
- distinguished the reusable catalog's ten project-profile questions from a
  run-specific project profile validated by JSON Schema;
- expanded the run profile subject enum to the subject types named by normative docs;
- integrated and validated the concurrently added domain-pack governance contract,
  schema, draft manifest, eight universal governance questions, and zero-published-pack
  claim, and made reviewed/published approval records reject `reject` decisions or
  empty conditional approvals;
- integrated and validated the concurrently added organizational-change and
  workforce-continuity modules, their activation edges, navigation, counts, and
  explicitly partial evidence status;
- integrated and validated the concurrently added external-sensing questions,
  source-to-decision contract, activation edge, navigation, non-guarantee boundary,
  and signal register; added the register's common trace metadata;
- added run, subject, framework-revision, graph-revision, and generation metadata to
  generated-artifact templates;
- completed README and quick-start routing and made coverage-manifest maintenance a
  contribution rule; and
- recorded the merged state of pull requests 1, 2, and 3 and the exact obsolete
  branch references that remain.

## Per-file disposition

Status meanings: **pass** means the file required no correction and its joins passed;
**aligned** means this audit corrected an integration inconsistency; **residual** means
the file is valid but transparently records or demonstrates incomplete future work.

### Root

| File | Status | Disposition |
|---|---|---|
| `AGENTS.md` | aligned | Canonical run layout, profile distinction, and coverage-update duty added. |
| `CHANGELOG.md` | aligned | Audit, current counts, and correction scope recorded. |
| `CLAUDE.md` | pass | Correctly delegates to the vendor-neutral agent contract. |
| `CONTRIBUTING.md` | aligned | Prose/catalog synchronization and profile distinction added. |
| `QUICKSTART.md` | aligned | Each step now names the exact canonical output file. |
| `README.md` | aligned | Template navigation completed and this audit linked. |
| `ai-context.yaml` | aligned | Canonical layout and audit path made machine-discoverable. |

### Catalog and coverage

| File | Status | Disposition |
|---|---|---|
| `catalog/README.md` | aligned | Catalog container and run-profile meanings distinguished. |
| `catalog/architecture/questions.yaml` | pass | Records validate; IDs and graph targets resolve. |
| `catalog/business/attraction-and-distribution-questions.yaml` | pass | Records validate; IDs and graph targets resolve. |
| `catalog/business/questions.yaml` | pass | Records validate; IDs and graph targets resolve. |
| `catalog/core/improvement-questions.yaml` | pass | Records validate; IDs and graph targets resolve. |
| `catalog/core/domain-pack-governance-questions.yaml` | pass | Eight governance records validate; IDs and graph targets resolve. |
| `catalog/core/project-profile.yaml` | pass | Ten reusable profile questions validate as a catalog container. |
| `catalog/data/questions.yaml` | pass | Records validate; IDs and graph targets resolve. |
| `catalog/ethics/questions.yaml` | pass | Records validate; IDs and graph targets resolve. |
| `catalog/legal/questions.yaml` | pass | Records validate; IDs and graph targets resolve. |
| `catalog/operations/questions.yaml` | pass | Records validate; IDs and graph targets resolve. |
| `catalog/operations/external-sensing-questions.yaml` | pass | Eight module records validate; IDs and graph targets resolve. |
| `catalog/performance/questions.yaml` | pass | Records validate; IDs and graph targets resolve. |
| `catalog/product/evolution-questions.yaml` | pass | Records validate; IDs and graph targets resolve. |
| `catalog/product/questions.yaml` | pass | Records validate; IDs and graph targets resolve. |
| `catalog/quality/questions.yaml` | pass | Records validate; IDs and graph targets resolve. |
| `catalog/reliability/questions.yaml` | pass | Records validate; IDs and graph targets resolve. |
| `catalog/retirement/questions.yaml` | pass | Records validate; IDs and graph targets resolve. |
| `catalog/security/questions.yaml` | pass | Records validate; IDs and graph targets resolve. |
| `catalog/team/questions.yaml` | pass | Records validate; IDs and graph targets resolve. |
| `catalog/team/organizational-change-questions.yaml` | pass | Eight module records validate; IDs and graph targets resolve. |
| `catalog/team/workforce-continuity-questions.yaml` | pass | Eight module records validate; IDs and graph targets resolve. |
| `catalog/users/questions.yaml` | pass | Records validate; IDs and graph targets resolve. |
| `catalog/ux/questions.yaml` | pass | Records validate; IDs and graph targets resolve. |
| `coverage/prose-to-catalog.yaml` | residual | Complete inventory; all 388 modeled questions remain conservatively compressed and await exact review. |

### Decisions

| File | Status | Disposition |
|---|---|---|
| `decisions/0001-product-questionbook-name.md` | pass | Naming decision and evidence limits remain consistent. |
| `decisions/ADR-0001-engine-implementation-stack.md` | pass | Clearly deferred and constrained by ADR-0003. |
| `decisions/ADR-0002-governed-adversarial-self-improvement.md` | pass | Governance boundary matches the operating documents. |
| `decisions/ADR-0003-text-first-agent-native-architecture.md` | pass | Accepted architecture is consistently treated as authoritative. |

### Human-readable question banks and normative documentation

| File | Status | Disposition |
|---|---|---|
| `docs/00-method.md` | pass | Method, evidence discipline, and outcomes are consistent. |
| `docs/01-aspects.md` | pass | Aspect inventory is represented in navigation and coverage. |
| `docs/02-core-questions.md` | pass | Numbered source text is preserved by the coverage manifest. |
| `docs/03-discovery-and-experience.md` | pass | Numbered source text is preserved by the coverage manifest. |
| `docs/04-engineering-data-and-integrations.md` | pass | Numbered source text is preserved by the coverage manifest. |
| `docs/05-trust-quality-and-operations.md` | pass | Numbered source text is preserved by the coverage manifest. |
| `docs/06-business-governance-and-evolution.md` | pass | Numbered source text is preserved by the coverage manifest. |
| `docs/07-naming-and-identity.md` | pass | Questions and eight guidance-only prompts are accounted. |
| `docs/08-machine-operation-and-outputs.md` | aligned | Run layout, lifecycle, coverage, scoring, and risk semantics reconciled. |
| `docs/09-output-convergence-and-implementation.md` | aligned | Answer example and scoring-policy boundaries corrected. |
| `docs/10-self-improvement-and-adversarial-governance.md` | pass | Separate bottleneck policy and governed change loop are coherent. |
| `docs/11-usage-deployment-and-agent-integration.md` | pass | Canonical run contract and permission boundary are coherent. |
| `docs/12-coverage-gaps-and-expansion-backlog.md` | aligned | Validator-first, optional-interface architecture restored. |
| `docs/13-quality-assurance-audit-and-roadmap.md` | aligned | Counts, manifest state, subject gap, and scoring interpretation updated. |
| `docs/14-human-and-ai-usability.md` | aligned | Completed discovery work separated from planned improvements. |
| `docs/15-request-coverage-and-operational-readiness-audit.md` | aligned | Live baseline counts and all three merged branches recorded. |
| `docs/16-prose-to-catalog-coverage.md` | residual | Correctly discloses compressed mappings and zero exact claims. |
| `docs/17-domain-pack-governance.md` | pass | Qualified pack activation, publication, blocker, expiry, and reopening rules are coherent. |
| `docs/18-external-sensing-and-attention.md` | pass | Source-to-decision loop and visibility non-guarantees are coherent. |
| `docs/19-whole-repository-integration-audit.md` | pass | This per-file audit and correction record. |
| `docs/assurance-rules.md` | pass | Evidence, blocker, risk, and output rules remain compatible. |
| `docs/coverage-model.md` | pass | Coverage states remain distinct and conservative. |
| `docs/domain-model.md` | aligned | Files are canonical; graph is a derived logical model. |
| `docs/output-contract.md` | aligned | Canonical records and reproducible projections clarified. |
| `docs/prioritization.md` | pass | `next-question-v1` matches stored example scores. |
| `docs/question-state-machine.md` | pass | State vocabulary and transition intent remain coherent. |
| `docs/structured-foundation.md` | aligned | Derived graph representation clarified. |
| `docs/terminology.md` | pass | Terms are compatible with the corrected contracts. |
| `docs/vision.md` | pass | Promise and non-guarantees remain honest. |

### Worked example

| File | Status | Disposition |
|---|---|---|
| `examples/sample-application/README.md` | residual | Valid illustrative subset, not a complete assurance package. |
| `examples/sample-application/answers.yaml` | pass | Answer validates and joins to its instance. |
| `examples/sample-application/project-profile.yaml` | pass | Profile validates against the expanded schema. |
| `examples/sample-application/question-instances.yaml` | pass | Four instances validate and reference catalog IDs. |

### Schemas

| File | Status | Disposition |
|---|---|---|
| `schemas/answer.schema.json` | residual | Structurally valid; cross-record evidence and review policy remain future semantic checks. |
| `schemas/domain-pack.schema.json` | pass | Draft manifest validates; published-pack gates remain intentionally unclaimed. |
| `schemas/improvement-cycle.schema.json` | residual | Structurally valid; full governance semantics remain partial. |
| `schemas/project-profile.schema.json` | aligned | Subject enum now matches normative subject types. |
| `schemas/prose-coverage.schema.json` | pass | Coverage manifest validates and reconciles with sources. |
| `schemas/question-instance.schema.json` | residual | Structurally valid; conditional state requirements remain future semantic checks. |
| `schemas/question.schema.json` | pass | All 131 question records validate. |
| `schemas/relationship.schema.json` | residual | Structurally valid; complete cross-record graph semantics remain future work. |

### Pack boundary

| File | Status | Disposition |
|---|---|---|
| `packs/README.md` | pass | Reserved directory, zero-published-pack disclaimer, and publication routing are coherent. |

### Templates

| File | Status | Disposition |
|---|---|---|
| `templates/adversarial-review.md` | aligned | Common trace metadata added. |
| `templates/agent-run-request.md` | pass | Correct input prompt and permission boundary; not a generated output artifact. |
| `templates/assurance-decision-record.md` | aligned | Common trace metadata added. |
| `templates/bottleneck-register.md` | aligned | Common trace metadata added. |
| `templates/decision-record.md` | aligned | Common trace metadata added. |
| `templates/domain-pack-manifest.yaml` | pass | Draft manifest matches the governance schema and claims no qualification. |
| `templates/external-signal-register.md` | aligned | Common trace metadata added to the sensing register. |
| `templates/improvement-cycle.md` | aligned | Common trace metadata added. |
| `templates/naming-brief.md` | aligned | Common trace metadata added. |
| `templates/product-brief.md` | aligned | Common trace metadata added. |
| `templates/project-charter.md` | aligned | Trace metadata and normative subject types added. |
| `templates/readiness-report.md` | aligned | Trace metadata and machine gate value corrected. |
| `templates/review-scorecard.md` | aligned | Common trace metadata added. |
| `templates/risk-register.md` | aligned | Common trace metadata added. |
| `templates/run-manifest.md` | pass | Canonical run identity, pins, gate, and coverage envelope. |

## Live GitHub integration state

At audit time there were no open pull requests. Pull requests 1, 2, and 3 were merged,
and their intended content was present on `main`. Three obsolete source refs still
exist:

- `agent/expand-integration-financial-continuity`;
- `agent/inquirygraph-foundation`; and
- `agent/text-first-agent-native-architecture`.

Their divergence is consistent with squash-merge ancestry and is not evidence of
missing content. Deleting those refs is repository hygiene, but this audit does not
delete them because branch deletion should follow an explicit dependency check and is
not required to integrate their content.

## Residual risks and next gates

The remaining material limitations are:

1. no committed deterministic validator, CI workflow, required status check, or
   branch-protection evidence;
2. only one small synthetic example and no complete failing-gate/outcome-review run;
3. eight schemas that do not yet encode all cross-record assurance semantics;
4. 388 compressed mappings and zero independently accepted exact mappings;
5. 120 natural-language applicability rules and 128 high-or-critical templates;
6. no empirical multi-project efficacy or agent-compatibility benchmark;
7. zero qualified published domain packs despite a valid governance interface;
8. three obsolete merged branch refs; and
9. no explicit license if public reuse is intended.

The controlling next improvement is a read-only deterministic conformance and
semantic validator, invoked in CI and by agents, followed by exact mapping review and
complete positive and negative run fixtures. These improvements must preserve the
accepted text-first architecture.
