# Security policy

## Scope

Product Questionbook is a documentation-first framework: Markdown, YAML, JSON Schema,
and one offline validator script. It runs no service, stores no user data, and has no
network surface. The realistic security concerns are therefore narrower than for an
application, and they are stated here rather than left implied.

**In scope**

- A defect in `tools/validate.py` — for example a check that silently passes when it
  should fail, or unsafe handling of a repository path.
- Content in this repository that could induce an agent to act unsafely — an
  instruction that would cause a run to exfiltrate data, write outside its run
  directory, or take an outward-facing action without authorization.
- Guidance that could lead a reader to a materially unsafe decision, such as a question
  or method that encourages recording secret material inside a run package.
- Supply-chain concerns in the declared dependencies (`tools/requirements.txt`) or the
  GitHub Actions workflow.

**Out of scope**

- The security of a product you assessed using this framework. That is yours.
- The correctness of an answer, evidence, or gate result in a run package. A run is
  advisory; see the assurance ladder in
  [`docs/13-quality-assurance-audit-and-roadmap.md`](docs/13-quality-assurance-audit-and-roadmap.md).
- Absence of a qualified domain pack. This is a declared limitation, not a
  vulnerability — see [`packs/README.md`](packs/README.md).

## Reporting a vulnerability

Report privately. Do **not** open a public issue for a suspected vulnerability.

- Preferred: GitHub private vulnerability reporting on
  [`MSKazemi/mohsen`](https://github.com/MSKazemi/mohsen/security/advisories/new).
- Alternative: email **mohsen.seyedkazemi@gmail.com** with `SECURITY` in the subject.

Please include the affected file and revision, what an attacker or a misled agent could
achieve, and a reproduction if you have one.

## What to expect

This project is maintained by one person without funding. The commitments below are
deliberately modest so that they are honest:

| Stage | Target |
|---|---|
| Acknowledgement of your report | within 7 days |
| Initial assessment and severity | within 30 days |
| Fix or a documented decision not to fix | best effort, communicated either way |

There is no bug-bounty programme and no paid triage. If a report is valid you will be
credited in `CHANGELOG.md` unless you ask otherwise.

## Never put secrets in a run package

A run package records candid assessment and is written to be read. If a run encounters
credentials, tokens, keys, or other secret material in a target repository:

- record that a **class** of secret exists and where the exposure risk lies;
- do **not** copy the values, and do **not** enumerate the file paths;
- treat the finding as a blocker for the target, and tell the target's owner directly.

Gitignoring a run directory is not a licence to write secrets into it.
