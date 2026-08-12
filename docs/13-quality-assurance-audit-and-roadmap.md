# Framework quality assurance audit and roadmap

**Audit snapshot:** 2026-08-12, `main` baseline commit `b2c5bd2`  
**Scope:** the Product Questionbook repository as a reusable question and assurance
framework; this is not an assessment of a product reviewed with the framework  
**Verdict:** promising and unusually explicit specification; not yet a proven or
continuously enforced quality-assurance system

## Direct conclusion

The repository should not claim that it guarantees a high-quality or successful
product. No general questionnaire can guarantee adoption, profit, safety, compliance,
delivery, or freedom from unknown failure modes.

The defensible target is narrower:

> For a pinned framework revision, declared policy, and bounded subject, the system
> can guarantee that its validation rules were executed; required applicable concerns
> were either supported by accepted evidence or explicitly accepted as risks; critical
> blockers were not averaged away; and every conclusion is traceable to versioned
> inputs, owners, and approvals.

The repository describes this target well. It cannot yet prove the target repeatedly
because most controls are prose and schemas rather than executable, required checks.

## What is already strong

- The framework explicitly rejects claims of perfection and separates structural
  assurance from real-world success.
- It covers the full lifecycle and treats evidence, uncertainty, ownership, review
  triggers, reversibility, failure, and retirement as first-class concerns.
- It distinguishes reusable templates from project-specific answers and preserves
  stable question IDs.
- It defines question-instance states, append-only history, typed relationships,
  outputs, blockers, adversarial review, bottleneck analysis, and governed
  self-improvement.
- It includes strong safeguards against fabricated evidence, agent consensus,
  unchecked autonomy, unsafe robot or device commands, and averaging away critical
  risk.
- The current structured catalog has good basic internal integrity.

These are valuable design properties. They are not the same as evidence that the
framework reliably improves decisions in practice.

## Audit evidence

The following facts were checked against `main` for this audit:

| Check | Observed result | Interpretation |
|---|---:|---|
| Structured questions | 131 | Useful starter graph, not parity with all prose questions or any specialized pack |
| Question IDs | 131 unique | No duplicate stable IDs found |
| Declared references | 510 | 278 `depends_on`; 172 `activates`; 58 `related_to`; 2 `refines` |
| Unresolved reference targets | 0 | Current dependency and activation targets resolve |
| Self-references | 0 | No direct self-edge found |
| `depends_on` cycles | 0 | Current dependency graph is acyclic |
| Required question fields missing | 0 | All records contain the fields required by `question.schema.json` |
| Publication status | 131 published | No draft or reviewed records remain in the universal catalog |
| Criticality | 69 critical, 59 high, 3 medium, 0 low | Severity is heavily concentrated at the top |
| Applicability | 11 always; 120 natural-language conditions | Most applicability cannot yet be evaluated deterministically |
| JSON Schemas | 8 | Prose coverage and domain-pack manifests are modeled; several assurance entities and semantic rules remain unmodeled |
| Commit status checks at snapshot | 0 reported | Validation is not a continuously required repository control |
| Worked examples | 1 synthetic application | Insufficient for efficacy, calibration, or domain claims |

This is a point-in-time audit, not a substitute for CI. The same checks must become
executable and mandatory to remain trustworthy after future changes.

## Bottleneck of bottlenecks

The controlling bottleneck is **the specification-to-evidence gap**:

> The repository can describe what a quality process should do, but it cannot yet
> continuously demonstrate that the right questions were selected, legal state
> transitions occurred, evidence satisfied policy, blockers were enforced, outputs
> were reproducible, or product decisions improved.

Adding more questions before closing this gap increases maintenance cost and the
appearance of completeness without proportionally increasing assurance. The first
investment should therefore be a small deterministic conformance validator and an
empirical evaluation loop, not a larger universal checklist or full application stack.

## Prioritized findings

| ID | Priority | Finding | Consequence |
|---|---|---|---|
| QA-01 | P0 | No deterministic conformance and semantic validator or required CI | The framework's strongest rules are advisory and can silently drift or be bypassed |
| QA-02 | P0 | No empirical benchmark or completed multi-project outcome loop | There is no evidence yet that the method finds consequential omissions better, reduces rework, or calibrates confidence |
| QA-03 | P0 | Assurance semantics exceed the eight existing schemas | Shape-valid records can still violate evidence, transition, blocker, approval, and risk-acceptance rules |
| QA-04 | P0 | The 396-question prose inventory is conservatively mapped to the 131-node catalog, but exact review and drift enforcement remain incomplete | Compressed semantics or later edits may still become invisible to selection, coverage, propagation, and learning |
| QA-05 | P1 | Criticality is inflated: 128 of 131 questions are high or critical | Prioritization loses discrimination and teams may experience alert fatigue or ritual compliance |
| QA-06 | P1 | 120 applicability rules are natural-language conditions | Different humans or agents can instantiate different graphs from the same input |
| QA-07 | P1 | The catalog now uses four relationship types, but most promised assurance edges remain absent | The promised graph has little machine-readable refinement, contradiction, evidence, decision, risk, test, or artifact semantics |
| QA-08 | P1 | Next-question and bottleneck scores are distinct, but neither has a complete versioned executable policy | Implementations can still normalize inputs or handle missing values differently |
| QA-09 | P1 | All catalog questions are published, but publication review evidence is not modeled | A valid record does not prove independent review, domain competence, or migration safety |
| QA-10 | P1 | One small synthetic example is the only worked run | Contradiction, staleness, accepted risk, cycles, adverse evidence, and gate failure are not demonstrated end to end |
| QA-11 | P2 | Repository adoption controls are immature | A private repository with no license, required status checks, or documented public compatibility policy limits independent scrutiny and reuse if public adoption is intended |

The separate [coverage-gap backlog](12-coverage-gaps-and-expansion-backlog.md) records
missing or shallow subject areas. This audit concentrates on whether the framework can
prove the quality of its own operation.

## Detailed criticism

### QA-01 — Written rules are not executable controls

The repository accurately labels the engine as future work. That honesty is important,
but it means claims such as deterministic selection, reverse-dependency invalidation,
fixed-point convergence, blocker enforcement, reproducible export, and gate evaluation
are design intentions rather than demonstrated behavior.

Required correction:

1. Implement one deterministic validator that can validate the repository and a run.
2. Make it callable by CI and agents; keep a command-line wrapper optional.
3. Run it for every change to protected framework assets and require it before merge.
4. Publish a machine-readable validation report tied to the commit SHA.

### QA-02 — The framework has no efficacy evidence

Internal consistency answers “Is the framework shaped correctly?” It does not answer
“Does using it improve decisions?” That requires real or carefully designed benchmark
runs, blinded review where possible, baselines, predicted outcomes, and later outcome
measurement.

Without this evidence, question count and coverage can become vanity metrics. A
smaller framework that exposes the controlling risk faster may be better than a larger
one.

Required correction:

- compare Questionbook-assisted reviews with a defined baseline;
- seed known hazards and measure severe-omission detection;
- measure false blockers, duplicate questions, time and evidence cost;
- track decision-change rate, downstream rework, and missed concerns found later;
- test calibration: high-confidence predictions should fail less often than
  medium- or low-confidence predictions;
- retain negative results and projects where the framework added no value.

### QA-03 — Schema validity is weaker than assurance validity

The eight schemas cover question templates, instances, answers, relationships,
project profiles, improvement cycles, prose coverage, and domain-pack manifests. The
output and domain contracts also rely on
evidence, decisions, requirements, risks, actions, metrics, tests, artifacts, gates,
policies, approvals, exceptions, and audit events. Those entities do not yet have a
complete shared contract.

Important semantic gaps include:

- `not_applicable` does not conditionally require a reason in the instance schema;
- `blocked` does not conditionally require a blocker;
- `verified` does not require an accepted answer with sufficient evidence;
- state-history `from` and `to` values are not restricted to legal states and legal
  transitions are not enforced by JSON Schema alone;
- an answer can have an empty evidence list, and `review_status` is optional;
- computed priority is not checked against the declared formula;
- critical risk acceptance authority and gate policy are prose, not executable data;
- cross-record subject, run, graph, and questionbook revision coherence is not
  enforced by JSON Schema alone.

Required correction: add missing entity schemas and implement cross-record semantic
validation outside JSON Schema.

### QA-04 — The canonical source of truth is incomplete

The first [coverage manifest](../coverage/prose-to-catalog.yaml) now accounts for all 396 numbered questions in the seven main banks and preserves their source text. It deliberately reports 388 compressed section mappings, eight guidance-only prompts, and zero exact mappings. This fixes the hidden-inventory problem, but not exact semantic parity.

The remaining correction is to independently review question-level equivalence, account for consequential unnumbered gate bullets and promoted backlog questions, and make source/catalog drift fail validation. Until then, compressed prose must remain visible during a run.

This is the first P0 item in the
[coverage-gap backlog](12-coverage-gaps-and-expansion-backlog.md#1-prose-to-catalog-parity).

### QA-05 — Criticality cannot prioritize when almost everything is critical

With 69 critical and 59 high questions, the catalog labels 98% of its nodes at the top
two severity levels. Criticality should describe consequence under explicit
conditions, not general importance. Otherwise gate queues become large, teams invent
exceptions, and true fatal concerns are obscured.

Required correction:

- separate inherent impact from context-specific criticality;
- calculate instance criticality from subject exposure and policy;
- reserve template-level `critical` for universally catastrophic or legally blocking
  cases, or replace it with a conditional criticality rule;
- calibrate labels against benchmark scenarios and false-blocker rates.

### QA-06 — Applicability is not reproducible

Natural-language applicability is appropriate for authoring the first version, but it
cannot support a deterministic guarantee. A versioned rule language must define
inputs, three-valued evaluation (`true`, `false`, `unknown`), explanation, errors, and
backward compatibility. An unknown applicability result must not silently become
`not_applicable`.

### QA-07 — The graph is currently a dependency graph, not the full assurance graph

The catalog now declares 510 references across `depends_on`, `activates`,
`related_to`, and `refines`. The broader model also describes contradictions,
evidence, decisions, risks, requirements, tests, owners, artifacts, supersession, and
review triggers. Those relationships must exist in project run data and be validated
before the graph can support the promised traceability and change-impact analysis.

### QA-08 — Ranking policy needs one versioned implementation

The repository intentionally contains different models for next-question priority and
controlling-bottleneck priority. `docs/prioritization.md` defines the current
`next-question-v1` baseline; the bottleneck score ranks a different decision object.
Each still needs a distinct machine-readable input schema, formula version,
normalization rule, missing-value policy, override policy, and test fixtures. A stored
`computed_score` must be recalculated, not trusted.

### QA-09 — Publication needs evidence and authority

All 131 universal catalog questions are marked `published`. The schema does not record reviewer identity,
review date, review method, domain qualification, approval, compatibility analysis, or
supporting run evidence. Git history helps, but it is not a substitute for the
publication decision contract described by the framework itself.

Protected changes should require an independent reviewer, migration analysis,
negative test, changelog entry, and explicit approval record.

### QA-10 — Examples do not exercise failure

The clinic example demonstrates a few states but not a completed assurance package.
The evaluation suite needs positive and negative fixtures for:

- legal and illegal state transitions;
- unresolved and contradictory evidence;
- stale answers and reverse-dependency invalidation;
- unknown applicability and justified non-applicability;
- accepted risk with insufficient and sufficient authority;
- fatal blockers that prevent a positive average score;
- dependency cycles and bounded convergence;
- changed framework versions and migration;
- deterministic regeneration from an identical snapshot.

### QA-11 — Repository governance affects trust

Private development can be intentional. If the goal includes broad adoption, however,
external users need clear licensing, supported-version and compatibility policy,
release tags, security reporting, contribution governance, and independently visible
validation results. These do not prove the framework is correct, but their absence
limits scrutiny, reproducibility, and safe reuse.

## Assurance levels

Use explicit levels rather than the word “guaranteed” by itself:

| Level | Claim | Minimum evidence |
|---|---|---|
| A0 — Documented | The method and limits are written | Normative documents and version history |
| A1 — Structurally valid | Files, schemas, IDs, links, and references are valid | Required CI report for the pinned commit |
| A2 — Semantically enforced | State, applicability, evidence, blocker, approval, and gate rules execute correctly | Scenario, negative, property, and determinism tests |
| A3 — Empirically calibrated | The framework's detection, false-blocker, time, and calibration behavior is measured | Versioned benchmark corpus and independent review |
| A4 — Domain-qualified | A declared domain and jurisdiction pack has qualified approval and current authorities | Pack-specific evidence, expert review, effective dates, and expiry |
| A5 — Outcome monitored | Predictions and decisions are compared with observed outcomes | Completed real-project outcome loops |

Current maturity is A0 overall, with manually observed portions of A1. The repository
should not claim A1 continuously until CI reproduces the checks, or A2 until semantic
validation exists.

No level guarantees market success or eliminates unknown unknowns. Each level states
what was checked and what remains outside the claim.

## Quality assurance package to provide

The next implementation should produce these durable deliverables:

1. **Quality-claim contract** — exact allowed and forbidden claims, scope, revision,
   policy, residual uncertainty, and expiry.
2. **Coverage manifest** — the conservative first manifest accounts for every numbered bank question; exact question-level review, additional source scopes, and automated drift enforcement remain.
3. **Deterministic conformance validator** — schema, link, ID, reference, state,
   applicability, evidence, risk, gate, score, and reproducibility checks. It must be
   callable by CI or agents; a CLI is an optional convenience adapter.
4. **Complete assurance schemas** — evidence, decision, requirement, risk, action,
   metric, test, artifact, gate, policy, approval, exception, and audit event.
5. **Machine-readable policy packs** — gate rules, critical blockers, evidence grades,
   risk authorities, expiries, and overrides.
6. **Test and benchmark corpus** — normal, adverse, contradictory, stale, cyclic,
   malicious, and migration scenarios.
7. **Evaluation report** — severe-omission detection, false blockers, calibration,
   reviewer agreement, decision-change rate, time, evidence cost, and later misses.
8. **Domain-pack interface and pilot** — activation, authority sources, qualification,
   versioning, tests, and expiry.
9. **Release and governance controls** — required CI, protected-asset review,
   compatibility policy, migrations, signed or attributable releases, and rollback.
10. **Field-trial records** — predictions, decisions, outcomes, misses, and resulting
    governed framework changes across multiple independent projects.

## Release gates for a credible quality claim

Do not describe the framework as an executable assurance system until all of these are
true:

### Gate 1 — Repository integrity

- every Markdown link and structured file validates in CI;
- every stable ID is unique and every declared target resolves;
- the catalog container and every question object validate;
- no forbidden dependency cycle or self-reference exists;
- generated counts and documentation claims match repository state;
- validation is required for protected changes.

### Gate 2 — Semantic correctness

- legal state transitions and conditional required fields are enforced;
- evidence grades, acceptance, expiry, contradiction, and staleness are executable;
- blocker, exception, approval, and risk-acceptance authority are machine-readable;
- the same frozen input and version produce byte-equivalent normalized state and the
  same gate result;
- invalid and adversarial fixtures fail for the intended reason.

### Gate 3 — Coverage parity

- every consequential prose question maps to stable graph nodes or is explicitly
  guidance-only;
- the mapping is checked in CI;
- `not modeled` is distinguishable from `not applicable` and `unanswered`;
- critical coverage is reviewed by accountable domain owners.

### Gate 4 — Empirical validation

- a preregistered benchmark compares the framework with a defined baseline;
- evaluators who score results are independent of the generated recommendation where
  practical;
- severe-omission recall, false-blocker rate, evidence cost, time to decision,
  calibration, and reviewer disagreement are reported together;
- negative and inconclusive results remain visible;
- thresholds are set before the release evaluation, not after observing results.

### Gate 5 — Domain qualification

- high-risk use activates an appropriate domain pack or explicitly blocks the claim;
- sources, jurisdictions, versions, qualified approvers, effective dates, and expiry
  are recorded;
- a generic framework result is never presented as legal, clinical, financial, or
  safety certification.

## Recommended implementation order

1. Freeze the assurance claim and version the policy vocabulary.
2. Refine the prose-to-catalog manifest to reviewed question-level mappings and enforce source/catalog drift checks.
3. Implement a read-only-by-default repository validator and make it required in CI; keep any CLI wrapper optional.
4. Add missing assurance schemas and semantic state/gate validation.
5. Add golden, negative, property, determinism, and migration tests.
6. Recalibrate criticality and implement a versioned applicability language.
7. Complete one end-to-end reference run, including a failing gate and outcome review.
8. Build a diverse benchmark corpus and compare against a baseline.
9. Pilot the process with multiple independent real projects.
10. Add one qualified domain pack before making high-risk domain claims.
11. Publish a versioned evaluation report and only then raise the assurance level.

## Framework-quality metrics

Do not optimize one metric in isolation. Track at least:

- severe concern recall and severity-weighted missed-concern rate;
- false critical-blocker and unnecessary-question rate;
- question decision-change rate and downstream unlock value;
- evidence acquisition time, cost, freshness, and rejection rate;
- time to a justified decision, not merely time to complete the questionnaire;
- prediction calibration by confidence band;
- inter-reviewer agreement on applicability, criticality, evidence, and gate result;
- contradictions or stale claims detected before and after a gate;
- downstream rework and incidents linked to missing or weak answers;
- catalog duplication, churn, deprecation, and compatibility cost;
- performance by subject type, lifecycle stage, risk class, organization, language,
  and domain pack;
- residual uncertainty and accepted risk, kept separate from verified evidence.

## Stop rules

Pause expansion or release when:

- validation is optional or cannot reproduce a reported result;
- a severe seeded concern passes an assurance gate unnoticed;
- criticality inflation makes the ready queue operationally unusable;
- unknown applicability is silently converted to non-applicable;
- a domain claim lacks qualified and current authority;
- benchmark gains disappear under independent review;
- the process costs more time or evidence than the decision warrants;
- framework changes optimize reported coverage while increasing false confidence.

## Final assessment

Product Questionbook already has a thoughtful architecture and a stronger assurance
philosophy than a normal checklist. Its main risk is **false maturity**: detailed
documents, schemas, and 131 published universal questions can look like operational proof even
though enforcement and efficacy are still unverified.

The correct next milestone is not “more comprehensive questions.” It is:

> A small, deterministic, tested conformance validator plus an independently evaluated
> corpus showing where the text-first framework helps, where it blocks incorrectly,
> and where it still misses important concerns.

Reaching that milestone would justify a precise structural-quality guarantee. It
would still not justify promising a perfect product—and the framework should continue
to say so explicitly.
