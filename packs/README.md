# Domain packs

This directory is reserved for bounded, qualified modules that extend the universal
catalog for regulated, safety-critical, or otherwise specialized domains.

No expert-reviewed pack is currently published. Do not infer healthcare, financial,
children's, government, automotive, aviation, or industrial-control assurance from
the presence of generic questions or from the pack interface.

Read [`../docs/17-domain-pack-governance.md`](../docs/17-domain-pack-governance.md),
copy [`../templates/domain-pack-manifest.yaml`](../templates/domain-pack-manifest.yaml),
and validate the manifest against
[`../schemas/domain-pack.schema.json`](../schemas/domain-pack.schema.json). A pack may
support a gate only after its exact version and scope reach `published` with current
qualified approvals and scenario evidence.
