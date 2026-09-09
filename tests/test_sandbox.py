import pytest
from change_manager.sandbox import validate_command, SandboxViolation


def test_allowed_command():
    validate_command(["pytest", "-q"])


def test_disallowed_command():
    with pytest.raises(SandboxViolation):
        validate_command(["rm", "-rf", "/"])
