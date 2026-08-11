# Product Questionbook agent instructions

## Purpose

Use this repository as a reusable decision and assurance framework. Do not present it
as an implemented autonomous engine. The current catalog, schemas, policies, and
templates may be applied manually or with agent assistance.

## Before substantive work

Read these files in order:

1. `docs/00-method.md`
2. `docs/08-machine-operation-and-outputs.md`
3. `docs/09-output-convergence-and-implementation.md`
4. `docs/10-self-improvement-and-adversarial-governance.md`
5. `docs/11-usage-deployment-and-agent-integration.md`

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
- Keep candidate brainstorming separate from accepted answers.
- Expose critical blockers and the controlling bottleneck before recommending work.
- Propagate accepted changes into affected requirements, decisions, risks,
  experiments, metrics, tests, approvals, and artifacts.
- Return only `proceed`, `proceed_with_conditions`, `pause`, or `stop` as a gate result.
- Never deploy, contact people, spend money, or command hardware without separate
  explicit authorization and an appropriate adapter.

## Framework changes

- Preserve published stable question IDs; deprecate rather than repurpose them.
- Validate YAML records against `schemas/question.schema.json` and resolve every
  declared relationship target.
- Protect schemas, blocker rules, security controls, and approval policy from
  autonomous self-modification.
- Record material framework changes in `CHANGELOG.md` and the relevant decision or
  normative document.
- Keep vendor adapter files thin. Canonical behavior belongs in `docs/`, `catalog/`,
  `schemas/`, and `templates/`.

