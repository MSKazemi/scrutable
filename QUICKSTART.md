# Scrutable quick start

Use this guide to turn an unclear product or system idea into a first evidence-backed
decision package. This repository is currently a framework, not an executable
application, so the first run is performed manually or with an AI agent. Working
directly with Markdown and YAML is the intended interface, not a temporary workaround;
no CLI or API is required. An optional validator may check deterministic rules when it
becomes available, without taking ownership of the files.

## Choose where the run belongs

Keep this repository reusable. Put project-specific answers in the target project's
repository, normally under:

```text
runs/<YYYY-MM-DD>-<short-name>/
```

Use a separate assurance repository only when access control, regulation, or
independent review requires it. Record the chosen location in the run manifest.

## Ten-minute human path

1. Create the run directory in the target project. Use the canonical filenames in
   [`docs/09-output-convergence-and-implementation.md`](docs/09-output-convergence-and-implementation.md#output-package-layout)
   rather than inventing a second layout.
2. Copy [`templates/run-manifest.md`](templates/run-manifest.md) to
   `00-manifest.md` and record the target revision plus the Scrutable
   revision used for the run.
3. Copy [`templates/project-charter.md`](templates/project-charter.md) to
   `01-context-and-success.md`. Use
   [`templates/product-brief.md`](templates/product-brief.md) for
   `05-system-brief.md` when the fuller projection is needed.
4. Answer the ten project-profile questions in
   [`catalog/core/project-profile.yaml`](catalog/core/project-profile.yaml). `Unknown`
   is valid; unsupported certainty is not.
5. For every consequential answer, record evidence, confidence, owner, verification
   method, and review trigger.
6. Open only the domains activated by those answers. Use
   [`docs/01-aspects.md`](docs/01-aspects.md) to classify each domain as critical,
   important, relevant, or not applicable.
7. If regulation, safety criticality, or material sector-specific harm may apply,
   evaluate [`core.domain-pack.001`](catalog/core/domain-pack-governance-questions.yaml).
   A required but unavailable, unpublished, expired, suspended, or out-of-scope pack
   is a blocker.
8. Record the selected instances, answer revisions, and evidence in
   `03-question-answer-ledger.md`, following the worked YAML records in
   [`examples/sample-application/`](examples/sample-application/). Record decisions,
   risks, experiments, requirements, and tests using the templates in
   [`templates/`](templates/).
9. Copy [`templates/readiness-report.md`](templates/readiness-report.md) to
   `09-gate-and-assurance-report.md` and end with exactly one machine value:
   `proceed`, `proceed_with_conditions`, `pause`, or `stop`.

Start small. A useful first run may contain unknowns and a `pause` result. Its purpose
is to reveal what must be learned or decided next, not to create the appearance of
completeness.

## Ten-minute AI-assisted path

Give the agent access to this repository and the target project, then use this prompt:

```text
Apply Scrutable to this project.

Read ai-context.yaml and AGENTS.md first. Pin the target revision and scrutable
revision. Create a new runs/<run-id>/ directory in the target project. Start with the
ten project-profile questions, separate facts from assumptions, cite evidence, expose
critical blockers, and do not invent answers. Produce the minimum useful decision and
assurance package and return one permitted gate result. Do not deploy, contact people,
spend money, or control hardware.
```

For a more precise request, fill in
[`templates/agent-run-request.md`](templates/agent-run-request.md).

## Minimum useful output

A first run is useful when it contains:

- a pinned run manifest;
- a short product or system brief;
- the selected questions and current answer state;
- evidence, assumptions, and unknowns;
- decisions and rejected alternatives;
- risks, blockers, owners, and next experiments;
- a gate result and the reasons for it.

The complete output contract is in
[`docs/08-machine-operation-and-outputs.md`](docs/08-machine-operation-and-outputs.md).

## See a worked example

Start with [`examples/sample-application/`](examples/sample-application/) to see a
project profile, question instances, and answers. The example demonstrates structure;
it is not evidence that the framework or a product is successful.

## If you are changing the framework

Read [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`AGENTS.md`](AGENTS.md). Preserve stable
question IDs, validate declared relationships, update the relevant normative document,
and record material changes in [`CHANGELOG.md`](CHANGELOG.md).
