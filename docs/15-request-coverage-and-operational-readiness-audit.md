# Request coverage and operational-readiness audit

**Audit date:** 2026-08-12  
**Audited branch:** `main`  
**Scope:** branch integration, self-improvement, usage and placement, inputs and
outputs, visibility and attention, algorithms, and coding-agent compatibility

## Verdict

All concerns in the request are represented on `main` at the **design and manual
protocol level**. They are not all implemented or empirically validated.

The precise status is:

- the two pull requests are merged and their intended content is consolidated on
  `main`;
- the reusable framework, structured catalog, schemas, templates, quick start, and
  agent instructions exist;
- the self-improvement, convergence, visibility, and agent-integration algorithms are
  specified;
- no deterministic conformance validator or required CI gate exists yet; a CLI, API,
  database, or service is optional and is not required for normal framework use;
- no system can guarantee attention from people, companies, agents, search engines,
  or news organizations; the framework can enforce only a measurable experiment,
  evidence, decision, and review process;
- the current maturity is A0 overall, with manually observed parts of A1. It is not
  yet A2. See the [quality audit](13-quality-assurance-audit-and-roadmap.md).

Do not translate “the question was added” into “the real-world risk is solved.” A
question creates a governed obligation to obtain evidence or explicitly carry the
uncertainty; it does not create the evidence.

## Branch-integration result

[Pull request 1](https://github.com/MSKazemi/mohsen/pull/1) and
[pull request 2](https://github.com/MSKazemi/mohsen/pull/2) are closed as merged, and
there are no open pull requests. Their content has already been reconciled into the
current framework. Reapplying either old branch tree would be unsafe because it would
restore older versions of files that have since evolved on `main`.

GitHub can still show the two source branch names as `diverged` after a squash merge.
That is an ancestry effect: the squash commit has a new identity. It is not evidence
that the intended content is missing. Branch-reference deletion is repository hygiene,
not another content merge. Delete the obsolete references only after confirming no
open pull request or automation depends on them.

## Coverage matrix

| Requested concern | Status on `main` | Canonical evidence | Honest limitation |
|---|---|---|---|
| Integrate every branch without losing consistency | Content integrated | Merged PRs, changelog 0.6, current canonical files | Two obsolete branch names can remain until their refs are deleted |
| Explain self-improvement | Specified | [Self-improvement and adversarial governance](10-self-improvement-and-adversarial-governance.md) | The loop is not an autonomous runtime |
| Explain how to use the repository | Specified and quick-started | [Quick start](../QUICKSTART.md) and [usage protocol](11-usage-deployment-and-agent-integration.md) | Today a human or agent executes the protocol manually |
| Decide where project outputs belong | Specified | Target repository `runs/<run-id>/` by default | A separate assurance repository may be required by access or regulation |
| Define inputs | Specified | Usage protocol and [run manifest](../templates/run-manifest.md) | Missing inputs remain `unknown`; an agent must not invent them |
| Define outputs | Specified | [Machine/output contract](08-machine-operation-and-outputs.md) and [convergence contract](09-output-convergence-and-implementation.md) | The exporter is not implemented |
| Keep output consistent across different projects | Specified | Stable envelope with conditional domain content | Project-specific sections, evidence depth, and approvals vary |
| Cover people, companies, agents, web/search, advertising, and news visibility | Structured questions and loop exist | Usage protocol and `catalog/business/attraction-and-distribution-questions.yaml` | Visibility itself cannot be guaranteed |
| Explain background algorithms and the loop | Specified | Convergence, prioritization, state, and self-improvement documents | Policies are not yet one executable versioned implementation |
| Work with Codex, ChatGPT, Claude Code, and other agents | Protocol and adapters specified | `ai-context.yaml`, `AGENTS.md`, `CLAUDE.md`, and [agent run request](../templates/agent-run-request.md) | No end-to-end agent benchmark or Questionbook service exists |
| Check the claims rather than merely document them | Partially checked | [Quality audit](13-quality-assurance-audit-and-roadmap.md) and [usability contract](14-human-and-ai-usability.md) | Efficacy and real-project outcomes are not yet demonstrated |

## Recommended deployment model

Keep the framework and the target project adjacent:

```text
workspace/
  product-questionbook/       # clone of this repository, pinned to a main SHA
  target-project/
    runs/<run-id>/             # project-specific answers and assurance package
```

Clone only `main` when one local branch is desired:

```bash
git clone --branch main --single-branch git@github.com:MSKazemi/mohsen.git product-questionbook
```

The framework repository owns reusable questions, schemas, policies, algorithms,
templates, examples, and framework decisions. The target repository normally owns
its profile, answers, evidence links, decisions, specifications, risks, tests, gate
reports, and audit history. Every run pins both the target-project revision and the
Questionbook revision. Use the framework repository itself as the output location only
when Product Questionbook is the subject or an owner deliberately chooses a combined
repository.

## Input and output contracts

The stable input envelope contains:

- run identity, decision, owner, time budget, and evidence budget;
- subject identity, type, boundary, lifecycle stage, repository, and revision;
- beneficiaries, desired outcomes, success, failure, and guardrail measures;
- product, technical, financial, integration, legal, ethical, safety, and operational
  constraints;
- applicability, evidence, blocker, approval, and risk-tolerance policies;
- attributable evidence with scope, collection time, quality, confidence, and expiry;
- prior answers, decisions, experiments, incidents, metrics, risks, and actions.

The stable output is a **versioned decision and assurance package backed by a
traceable graph**. Its identity, state vocabulary, trace links, gate values, and base
directory structure remain consistent. Activated questions, domain projections,
evidence depth, and required approvals vary with the subject, stage, impact, and
policy. A justified `not_applicable` record is different from an omitted concern.

## End-to-end operating loop

1. Freeze the target and Questionbook revisions and create the run manifest.
2. Answer the ten project-profile questions; record `unknown` where evidence is
   missing.
3. Activate only applicable domains and construct the ready question frontier.
4. Rank blockers and unresolved questions by harm, uncertainty, irreversibility,
   dependency centrality, information gain, urgency, and resolution cost.
5. Attach evidence, confidence, owner, falsifier or verification, and review trigger
   to consequential claims.
6. Propagate accepted answers into decisions, requirements, risks, experiments,
   metrics, tests, approvals, and artifacts.
7. Mark reverse dependants stale after a consequential upstream change.
8. Attack the controlling bottleneck with independent critics and the cheapest safe
   test that distinguishes competing predictions.
9. Return exactly `proceed`, `proceed_with_conditions`, `pause`, or `stop`.
10. Compare predictions with observed outcomes at the review trigger and reopen the
    affected graph in a new bounded epoch.

For cyclic dependencies, identify strongly connected components, process the
condensed acyclic graph in dependency order, and iterate each cyclic component to a
fixed point or a declared budget. If it does not stabilize, return `pause` with the
unresolved alternatives and missing evidence.

## Self-improvement mechanism

Self-improvement is governed error correction:

> observe -> adversarially challenge -> identify the controlling bottleneck -> form
> alternatives -> run the cheapest discriminating test -> decide -> propagate ->
> measure prediction error -> propose a bounded change

The loop operates separately on four levels: application, idea, project graph, and
reusable repository. A failed application claim can reopen a project answer; it does
not automatically prove that the reusable catalog is wrong. Published question IDs,
schemas, blocker policy, security controls, and approval rules are protected assets.
Agents may propose changes, but an authorized maintainer must review and publish them.

The “brutal” review rule is evidence discipline, not theatrical aggression. Every
material criticism must name the target claim, causal failure mechanism, evidence for
and against it, uncertainty, falsifier, cheapest discriminating test, decision
consequence, owner, and stop or pivot threshold. Agent agreement is not independent
evidence.

## Visibility and qualified-attention mechanism

The catalog contains twelve stable questions covering:

- audience fit and harmful attention;
- positioning and proof;
- owned, earned, paid, partner, community, sales, search, marketplace, and integration
  channels;
- the complete reach-to-retained-value funnel;
- advertising incrementality and acquisition economics;
- retention, referral, and expansion;
- search, AI-agent, registry, marketplace, and platform discovery;
- attention quality and vanity or harmful demand;
- channel, account, algorithm, policy, partner, and reputation concentration;
- journalists, analysts, researchers, communities, and news coverage;
- organizational discovery, evaluation, procurement, integration, and renewal.

The loop is:

1. segment the exact people, organizations, agents, search systems, communities, and
   media actors whose attention can enable the declared outcome;
2. define denominated transitions from qualified reach to attention, activation,
   retained value, referral or expansion, and sustainable economics;
3. test message comprehension, distinctness, and proof before scaling a channel;
4. test human and machine discoverability, indexing, metadata, documentation,
   marketplaces, integrations, procurement, and media evidence packs;
5. run bounded channel experiments with a budget, comparison or holdout when
   possible, guardrails, and stop threshold;
6. find the evidence-backed funnel bottleneck that controls the most downstream
   retained value;
7. reallocate, change the product/message/channel, diversify, pause, or stop;
8. reopen the loop when audience behavior, algorithms, policy, cost, reputation,
   procurement, or news conditions change.

Supporting methods include cohort and survival analysis, randomized or
quasi-experimental advertising holdouts, Bayesian or sequential updates,
expected-information-gain prioritization, dependency-centrality analysis, and
constrained channel allocation. These methods reduce uncertainty. They cannot compel
an external actor to pay attention.

## Agent compatibility

The protocol is vendor-neutral. An agent-compatible environment needs repository
read/write access, stable Markdown/YAML/JSON handling, evidence provenance, an approval
boundary, and an auditable diff. Deterministic controls—schema and semantic validation,
state transitions, dependency propagation, blocker policy, gate evaluation, and
reproducible export—must remain outside the language model. The LLM may clarify,
brainstorm, challenge, and draft, but it may not manufacture evidence or approve its
own consequential recommendation.

The current repository is documentation-friendly for Codex, ChatGPT, Claude Code, and
similar systems through `ai-context.yaml`, `AGENTS.md`, `CLAUDE.md`, and the run-request
template. No separate application is required for this text-protocol integration.
However, there is not yet a deterministic validator, adapter test suite, permission
test suite, or benchmark showing reliable end-to-end behavior.

## Independent structural check of the audited snapshot

The live `main` tree was checked for the following properties:

- 131 question records and 131 unique stable IDs;
- 450 declared `depends_on` and `activates` references, with every target resolved;
- eight JSON files with valid JSON syntax;
- no missing required human or agent entrypoint;
- 172 internal Markdown file links checked with no missing target;
- no open pull request and both historical pull requests marked merged;
- no reported commit status checks on the audited `main` commit.

This is a structural snapshot, not a claim of semantic correctness, agent reliability,
domain completeness, or improved product outcomes.

## Remaining controlling bottleneck

The controlling bottleneck is no longer missing prose or a missing user application.
It is the absence of a deterministic, required, and empirically tested conformance and
assurance path. The next work should be:

1. implement the repository validator and run it as a required CI check;
2. refine the conservative prose-to-catalog manifest to independently reviewed question-level mappings and enforce drift checks;
3. complete the schemas and cross-record semantic validation;
4. add positive, negative, property, determinism, migration, and permission tests;
5. provide a complete end-to-end run, including a failing gate and outcome review;
6. test vendor-neutral agent use of the text protocol and add only the adapters that
   measured failures justify; keep CLI/API optional;
7. run independent real-project pilots and measure misses, false blockers, calibration,
   evidence cost, decision change, and later outcomes;
8. delete obsolete merged branch references after verifying no dependency remains.

Until those gates pass, the accurate claim is: Product Questionbook provides a
documented, structured, evidence-oriented text protocol for manual and agent-assisted
work. It does not yet provide automated conformance assurance, guaranteed visibility,
or guaranteed product success; it does not require a standalone application to be
useful.
