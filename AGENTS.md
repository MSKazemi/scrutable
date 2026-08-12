# Product Questionbook agent instructions

## Purpose

Use this repository as a reusable decision and assurance framework. Do not present it
as an implemented autonomous engine. The current catalog, schemas, policies, and
templates may be applied manually or with agent assistance. Treat Markdown, YAML,
JSON Schema, and Git history as the primary interface. Do not require a CLI, API,
database, or service to perform a run. If an optional validator is available, use it
for deterministic checks and preserve its report; do not treat it as the source of
truth.

## Context loading

1. Read `ai-context.yaml` to classify the task and find canonical sources.
2. For a first framework run, use `QUICKSTART.md` and start with the ten question
   templates in `catalog/core/project-profile.yaml`. Do not confuse that catalog
   module with a run-specific project profile, which conforms to
   `schemas/project-profile.schema.json`.
3. Load only the activated domains and schemas; do not load every question bank by
   default. If regulation, safety criticality, or material sector-specific harm may
   apply, evaluate `core.domain-pack.001` and read
   `docs/17-domain-pack-governance.md`. Load only an in-scope, current, `published`
   pack; a required but unavailable pack is a blocker.
4. Before an assurance decision, read these normative files in order:
   - `docs/00-method.md`
   - `docs/08-machine-operation-and-outputs.md`
   - `docs/09-output-convergence-and-implementation.md`
   - `docs/10-self-improvement-and-adversarial-governance.md`
   - `docs/11-usage-deployment-and-agent-integration.md`
5. Before changing the reusable framework, also read `CONTRIBUTING.md`, the affected
   schemas, and the relevant normative document.

## Run protocol

- Put a target project's run artifacts in that target project's `runs/<run-id>/`
  directory unless an owner explicitly selects a separate assurance repository.
- Pin the target revision and `questionbook_ref` before analysis.
- Start with the ten questions in `catalog/core/project-profile.yaml` and activate
  conditional domains from recorded answers.
- Separate facts, observations, inferences, assumptions, predictions, preferences,
  and decisions. `Unknown` is valid; fabricated evidence is not.
- Every consequential claim needs evidence, confidence, an owner, a falsifier or
  verification method, and a review trigger.
- When accepted decisions depend on external state, use
  `docs/18-external-sensing-and-attention.md` and preserve source, query, time-window,
  retrieval, reliability, latency, and blind-spot records. Do not claim guaranteed or
  continuous visibility unless a separately authorized recurring process proves it.
- When the subject creates, transforms, ranks, recommends, stores, or distributes
  consequential content, use `docs/20-information-integrity-and-content-governance.md`.
  Do not equate provenance with truth or automate irreversible content decisions
  without the required context, review, appeal, correction, and propagation path.
- Keep candidate brainstorming separate from accepted answers.
- Expose critical blockers and the controlling bottleneck before recommending work.
- Propagate accepted changes into affected requirements, decisions, risks,
  experiments, metrics, tests, approvals, and artifacts.
- Use the canonical run layout in `docs/09-output-convergence-and-implementation.md`;
  do not invent a second filename or gate vocabulary.
- Return only `proceed`, `proceed_with_conditions`, `pause`, or `stop` as a gate result.
- Never deploy, contact people, spend money, or command hardware without separate
  explicit authorization and an appropriate adapter.

## Framework changes

- Preserve published stable question IDs; deprecate rather than repurpose them.
- Validate YAML records against `schemas/question.schema.json` and resolve every
  declared relationship target.
- When a numbered question bank or catalog mapping changes, update
  `coverage/prose-to-catalog.yaml` and preserve its source text, counts, and target
  resolution.
- Protect schemas, blocker rules, security controls, and approval policy from
  autonomous self-modification.
- Do not let an agent publish or self-approve a domain pack. Apply the qualified
  reviewer, authority, scenario, expiry, and reopening rules in
  `docs/17-domain-pack-governance.md`.
- Record material framework changes in `CHANGELOG.md` and the relevant decision or
  normative document.
- Keep vendor adapter files thin. Canonical behavior belongs in `docs/`, `catalog/`,
  `schemas/`, and `templates/`.
