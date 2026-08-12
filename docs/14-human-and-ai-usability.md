# Human and AI usability contract

## Purpose

Product Questionbook must be understandable by a first-time human and reliably
navigable by an AI agent without requiring either reader to load the entire
repository. Friendliness means reducing time-to-first-use and ambiguity while
preserving evidence, safety, and traceability requirements.

This contract is an interface layer over the existing framework. It does not change
question semantics, lower assurance requirements, or imply that an executable engine
exists.

## Current assessment

The repository is already strong in deep documentation and machine structure:

- stable question IDs and a structured YAML catalog;
- JSON Schemas and typed graph relationships;
- a worked example and reusable templates;
- explicit agent instructions, state rules, outputs, and permission boundaries.

The controlling usability bottleneck is progressive disclosure. A new reader can see
the framework's breadth but must navigate many normative documents before completing a
small successful run. An agent can infer the structure, but previously lacked one
compact manifest declaring canonical sources, load order, outputs, limitations, and
authorization boundaries.

## Entry points

| Reader or task | First entry point | Next material |
| --- | --- | --- |
| First-time human | [`QUICKSTART.md`](../QUICKSTART.md) | Worked example and core project profile |
| Product owner | [`templates/product-brief.md`](../templates/product-brief.md) | Core and activated domain questions |
| AI agent applying the framework | [`ai-context.yaml`](../ai-context.yaml) | `AGENTS.md`, method, and core profile |
| AI agent changing the framework | [`AGENTS.md`](../AGENTS.md) | Contribution guide, schemas, and normative docs |
| Engine implementer | Machine and convergence contracts | Schemas, domain model, and ADR-0001 |
| Reviewer or auditor | Assurance rules and readiness report | Evidence ledger, blockers, and gate report |

The README should route readers to these paths before presenting the full document
map.

## Human-friendly requirements

1. A reader should understand what the repository is, what it is not, and its output
   from the first screen of the README.
2. A first useful run should not require reading every question bank.
3. Every quick-start step should name a file to open, copy, or produce.
4. Examples must distinguish illustrative structure from verified real-world evidence.
5. Navigation should use task-oriented labels such as “apply the framework,” “change
   the framework,” and “build the engine.”
6. `Unknown`, `pause`, and `stop` must be presented as valid outcomes.
7. New terminology should link to the terminology document instead of being redefined
   inconsistently.

## AI-friendly requirements

1. `ai-context.yaml` is the compact discovery manifest; `AGENTS.md` remains the
   behavioral instruction entrypoint.
2. Agents load only the context required for the task, then follow links to deeper
   normative material when activated.
3. The catalog and schemas are machine-readable truth; narrative documents explain
   intent and policy.
4. Every project run pins both the target revision and the framework revision.
5. Agents must distinguish facts, observations, inferences, assumptions, predictions,
   preferences, and decisions.
6. Missing evidence remains missing. Agents may propose research or experiments but
   may not convert generated text into accepted evidence.
7. Output paths, allowed gate values, required claim fields, and permission boundaries
   must be discoverable without natural-language inference.
8. Framework changes preserve stable IDs and require governed publication; an agent
   may not silently rewrite protected rules.

## Progressive context levels

### Level 1: discover

Load `ai-context.yaml` and the README. Determine whether the task is framework use,
framework change, engine implementation, or review.

### Level 2: start a run

Load `AGENTS.md`, `docs/00-method.md`, the core project profile, the matching schemas,
and the target project's evidence. Do not load every domain by default.

### Level 3: expand by activation

Load only domains activated by the project profile, risk classification, lifecycle
stage, dependencies, or reviewer request.

### Level 4: assure and decide

Load the output, convergence, adversarial-governance, and usage contracts. Resolve
blockers and produce one permitted gate result.

## Failure behavior

A friendly system is predictable when it cannot proceed:

| Condition | Required behavior |
| --- | --- |
| Missing evidence | Mark the claim unsupported or unknown; propose a verification action |
| Conflicting evidence | Preserve both sources, identify the conflict, and withhold acceptance |
| Stale dependency | Mark affected nodes and projections stale, then revalidate |
| Critical unresolved blocker | Return `pause` or `stop` |
| Missing authorization | Stop before the external or consequential action |
| Iteration does not converge | Report the unstable component and escalate; do not fabricate closure |
| Unsupported file or schema | Preserve the source, report the validation limit, and avoid silent coercion |

## Usability checks

Until automated checks exist, review releases against these questions:

- Can a new human find the quick start and worked example from the README?
- Can an agent find canonical sources, the minimal load order, allowed outputs, and
  prohibited actions from `ai-context.yaml`?
- Does each link resolve on `main`?
- Can the sample structure be checked against the declared schemas?
- Are question IDs unique and all relationship targets resolvable?
- Do important claims expose evidence, confidence, owner, verification, and review
  trigger?
- Does every gate report use an allowed value and surface critical blockers?

## Prioritized next improvements

| Priority | Improvement | Why it matters | Completion evidence |
| --- | --- | --- | --- |
| P0 | Quick start, README routing, AI manifest | Removes the entry and discovery bottleneck | A novice and agent can identify the correct path without reading all docs |
| P1 | Executable schema and relationship validator in CI | Converts documented rules into repeatable checks | Pull requests fail on invalid records, duplicate IDs, or broken relationships |
| P1 | Complete end-to-end example output bundle | Shows what “done” looks like | Example includes manifest, ledger, ADR, risks, tests, and gate report |
| P1 | Repository description, topics, license decision, and branch hygiene | Improves discovery and contribution clarity | Settings and legal status are explicit |
| P2 | CLI for initializing and validating runs | Reduces copying errors | One command creates a pinned valid run skeleton |
| P2 | Generated documentation index and link checker | Prevents navigation decay | CI verifies links and publishes the index |
| P3 | Interactive navigator | Helps nontechnical users traverse activated questions | Usability testing shows lower completion time and fewer missed blockers |

The P1 validator is the next controlling engineering improvement. More prose will not
make the repository materially more AI-reliable until declared schemas,
relationships, and links are automatically checked.

## Claims this interface may make

The repository may claim that it offers documented human and AI entrypoints,
structured machine-readable inputs, explicit outputs, and bounded failure behavior.
It must not claim that these files alone guarantee comprehension, correct agent
behavior, complete coverage, or product success. Those claims require executable
validation and empirical usability evidence.
