# Product Questionbook quick start

Use this guide to turn an unclear product or system idea into a first evidence-backed
decision package. This repository is currently a framework, not an executable
application, so the first run is performed manually or with an AI agent.

## Choose where the run belongs

Keep this repository reusable. Put project-specific answers in the target project's
repository, normally under:

```text
runs/<YYYY-MM-DD>-<short-name>/
```

Use a separate assurance repository only when access control, regulation, or
independent review requires it. Record the chosen location in the run manifest.

## Ten-minute human path

1. Create the run directory in the target project.
2. Copy [`templates/run-manifest.md`](templates/run-manifest.md) and record the target
   revision plus the Product Questionbook revision used for the run.
3. Copy [`templates/product-brief.md`](templates/product-brief.md).
4. Answer the ten project-profile questions in
   [`catalog/core/project-profile.yaml`](catalog/core/project-profile.yaml). `Unknown`
   is valid; unsupported certainty is not.
5. For every consequential answer, record evidence, confidence, owner, verification
   method, and review trigger.
6. Open only the domains activated by those answers. Use
   [`docs/01-aspects.md`](docs/01-aspects.md) to classify each domain as critical,
   important, relevant, or not applicable.
7. Record decisions, risks, experiments, requirements, and tests using the templates
   in [`templates/`](templates/).
8. End with exactly one gate result: `proceed`, `proceed_with_conditions`, `pause`, or
   `stop`.

Start small. A useful first run may contain unknowns and a `pause` result. Its purpose
is to reveal what must be learned or decided next, not to create the appearance of
completeness.

## Ten-minute AI-assisted path

Give the agent access to this repository and the target project, then use this prompt:

```text
Apply Product Questionbook to this project.

Read ai-context.yaml and AGENTS.md first. Pin the target revision and questionbook
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
