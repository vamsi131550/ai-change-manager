from pathlib import Path


ALLOWED_COMMANDS = {"pytest", "python", "ruff"}


class SandboxViolation(ValueError):
    pass


def validate_command(command: list[str]) -> None:
    if not command:
        raise SandboxViolation("empty command")
    if command[0] not in ALLOWED_COMMANDS:
        raise SandboxViolation(f"command not allowed: {command[0]}")


def validate_repository(path: str) -> Path:
    p = Path(path).resolve()
    if not p.exists():
        raise FileNotFoundError(path)
    return p
