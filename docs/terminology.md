# Terminology

| Term | Meaning |
|---|---|
| Project | The bounded effort using Scrutable to examine and improve a subject |
| Framework | Scrutable's concepts, rules, catalog, schemas, and workflows |
| Application | A future user interface or service implementing the framework |
| Subject | The application, service, feature, process, or organization being examined |
| Domain | A concern area such as security, product, reliability, or business |
| Lifecycle stage | When a concern matters: discover through retire |
| Question template | A reusable catalog definition independent of any project |
| Question instance | A template applied to one subject with state, owner, answer, and history |
| Answer | A project-specific response, including assumptions and confidence |
| Evidence | Inspectable support such as research, measurements, tests, prototypes, or records |
| Decision | An accountable conclusion supported by answers and evidence |
| Risk | An uncertain condition that may prevent a desired outcome |
| Artifact | A generated or referenced document, specification, report, model, or plan |
| Action | Work required to resolve a question, produce evidence, or mitigate a risk |
| Assurance | Confidence grounded in traceable evidence and explicit treatment of risk |
| Coverage | The status of applicable questions across domains and lifecycle stages |
| Activation | A rule or answer that makes another question applicable |
| Stale | Previously useful information that must be reconsidered after time or change |
| Accepted risk | A documented decision to proceed despite an unresolved concern |

## Distinctions that must remain explicit

### Framework, project, and application

The repository contains the **Scrutable framework**. A team uses it in an
**assessment project**. Software that executes the model is an **application**.

### Template and instance

A template is reusable and has a publication lifecycle. An instance belongs to one
project and has an interview lifecycle. Mixing them causes one project's answer,
owner, or status to leak into every other project.

### Answer and evidence

An answer is a claim. Evidence is inspectable support for that claim. High confidence
without evidence is still an unsupported answer.

### Complete and successful

Question-complete means the assurance rules are satisfied at a point in time. It does
not mean the subject will necessarily succeed in its market or never fail.

