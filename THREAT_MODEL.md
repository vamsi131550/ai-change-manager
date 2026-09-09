# Threat Model

Threats considered:

1. Prompt injection in repository content
2. Agent requesting unauthorized tools
3. Agent attempting self-approval
4. Destructive commands
5. Duplicate execution
6. Missing approval
7. Secret exposure
8. Tool failure
9. Verification failure

Design response:

- treat repository content as untrusted data
- enforce tool-level permissions
- separate policy from LLM
- require approval for high-risk actions
- deny critical actions
- sandbox command execution
- audit every action
- verify after execution
