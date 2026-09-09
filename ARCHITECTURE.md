# Architecture

## Trust boundary

The LLM is treated as an untrusted planner.

It can propose:

- actions
- tool calls
- deployment plans
- explanations

It cannot independently authorize itself.

The deterministic policy layer evaluates:

- environment
- risk
- permissions
- destructive behavior
- approval requirements

## Future MCP layer

Suggested servers:

- GitHub
- CI
- deployment simulator
- monitoring
- approval

Suggested flow:

Agent -> MCP -> Policy -> Approval -> Tool -> Verification -> Audit
