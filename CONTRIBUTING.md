# Contributing questions

Scrutable is useful only when its questions are clear, reusable, traceable, and
capable of changing a decision.

Contributions are accepted under [Apache-2.0](LICENSE), the license of this repository.
Please read [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) before participating, and report
security concerns privately via [`SECURITY.md`](SECURITY.md) rather than in a public
issue.

## Run the validator before you open a pull request

```bash
pip install -r tools/requirements.txt
make validate          # or: python3 tools/validate.py
```

CI runs the same command and a failure blocks the merge. The validator checks structure
only — schemas, stable-ID uniqueness, relationship targets, acyclicity,
coverage-manifest fidelity, Markdown links and anchors, and gate-vocabulary consistency.
It cannot judge whether a question is *good*; that is what the checklist below is for.

## The catalog is frozen at 199 questions

New question content is paused until the empirical gap is addressed — the framework has
never been run against an external subject, so its detection and false-blocker behaviour
is unmeasured. Adding questions in that state increases maintenance cost and the
appearance of completeness without increasing assurance; see
[`docs/13`](docs/13-quality-assurance-audit-and-roadmap.md) and
[ADR-0005](decisions/ADR-0005-deterministic-conformance-validator.md).

Still welcome during the freeze: fixes to existing questions, relationship corrections,
evidence and worked examples, validator checks, documentation, and — most valuable of
all — **a record of running the framework on a real project**.

## Before adding a question

Check whether an existing question can be refined, related, or given a better
activation rule. Avoid duplicates that differ only in wording.

A good question:

- exposes a consequential unknown, assumption, constraint, or risk;
- can be answered for a defined subject;
- states why the answer matters;
- identifies the evidence needed for high-impact claims;
- activates, depends on, or informs other work;
- is neutral and does not embed a preferred answer;
- is small enough to have a clear owner and state.

## Required fields

New templates must conform to [`schemas/question.schema.json`](schemas/question.schema.json)
and include a stable ID, question text, purpose, domain, lifecycle stages, answer
type, criticality, evidence expectations, and expected outputs.

Use IDs of the form `domain.topic.NNN`. IDs are permanent: deprecate a published
question instead of reusing its ID for a different meaning.

## Review checklist

- Is the question applicable to more than one project?
- Could two reasonable people interpret it the same way?
- Does it overlap with an existing question?
- Are dependencies and activations expressed as template IDs?
- Can the required evidence actually be produced or inspected?
- Does the question avoid promising that a single answer guarantees success?
- Is `criticality` proportionate to the consequence of getting the answer wrong?
  Note that `criticality` is an advisory authoring hint and is **not** the run-time
  ranking input — 196 of 199 published questions are already `high` or `critical`, so
  reaching for `critical` by default adds no information. See
  [ADR-0006](decisions/ADR-0006-criticality-is-advisory.md).

Template publication follows `draft -> reviewed -> published -> deprecated`.

## Keep prose and catalog integrated

The detailed Markdown banks and reusable catalog are different representations, not
independent inventories. When a numbered source question or a catalog question's
meaning changes:

1. update `coverage/prose-to-catalog.yaml`;
2. preserve every affected source question and stable ID;
3. recheck summary counts and every `catalog_id` target;
4. record whether the mapping is `exact`, `compressed`, `unmodeled`, or
   `guidance_only` without inflating the claim; and
5. update the changelog and any affected normative contract.

`catalog/core/project-profile.yaml` is a catalog container whose individual question
objects conform to `schemas/question.schema.json`. A run-specific project profile is
a different record and conforms to `schemas/project-profile.schema.json`.

## Domain packs

A specialized pack must follow the
[domain-pack governance contract](docs/17-domain-pack-governance.md) and conform to
[`schemas/domain-pack.schema.json`](schemas/domain-pack.schema.json). Repository
maintainership or agent authorship is not domain qualification. Do not mark a pack
`reviewed` or `published` without current authoritative sources, qualified scoped
approvals, blocker and waiver rules, positive and negative scenarios, incident or
audit evidence, limitations, expiry, and affected-run behavior.
