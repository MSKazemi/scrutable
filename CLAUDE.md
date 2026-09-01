@AGENTS.md

# Claude Code adapter

`AGENTS.md` above is the canonical, vendor-neutral instruction set for this repository and is
imported in full, so Claude Code and every other agent read exactly the same rules. The run,
evidence, output, self-improvement, visibility and permission rules are defined in
[`docs/11-usage-deployment-and-agent-integration.md`](docs/11-usage-deployment-and-agent-integration.md).

This file is only a compatibility entrypoint. Do not create Claude-specific framework behavior
or bypass the vendor-neutral validation and approval rules.
