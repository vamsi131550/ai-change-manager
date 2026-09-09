# AI Change Manager

A personal open-source prototype for safe AI-assisted software change management.

## Core principle

**AI proposes. Policy decides. Humans approve risk. Systems execute.**

The system analyzes a change request, inspects a sandbox repository, runs validation, assesses risk, requests approval for risky actions, executes only authorized operations, verifies the result, and can trigger a rollback simulation.

> Personal project. Deployment and repositories are simulated/sandboxed. No production systems are connected.

## Architecture

```text
Change Request
      |
      v
Planning Agent
      |
      +--> Repository inspection
      +--> Dependency analysis
      +--> Tests
      +--> Risk assessment
      |
      v
Policy Engine
      |
   +--+---------+
   |            |
 auto        approval
   |            |
   +-----+------+
         |
         v
Execution
         |
         v
Verification
     |       |
  success  failure
     |       |
     |       v
     |    Rollback
     v
   Audit
```

## Starter implementation

The repository contains a deterministic risk/policy engine, change request models, audit events, sandbox command validation and a FastAPI API.

The MCP and LangGraph layers are deliberately left as extension points so the implementation can be understood and evolved rather than hiding everything behind generated code.

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
uvicorn change_manager.api:app --reload
```

Open `http://127.0.0.1:8000/docs`.

## Planned extensions

- MCP servers for GitHub, CI, deployment and monitoring
- LangGraph planner/executor/verifier
- sandboxed Git operations
- approval UI
- PostgreSQL audit store
- Redis locks
- OpenTelemetry
- deployment simulation
- rollback experiments
- red-team prompt-injection tests
