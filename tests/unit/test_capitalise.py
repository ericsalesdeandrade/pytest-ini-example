import os
import pytest
from capitalise.core import capitalise


def test_capitalise() -> None:
    """
    Test capitalise function
    :return: None
    """
    test_value = "She sells sea shells on the sea shore"
    response = capitalise(value=test_value)
    assert response == "SHE SELLS SEA SHELLS ON THE SEA SHORE"


def test_value_error():
    """
    Test if Value Error is raised
    :return: None
    """
    test_value = 25
    with pytest.raises(ValueError):
        response = capitalise(value=test_value)


def test_load_env_vars() -> None:
    """
    Load Env Vars using pytest.ini
    :return: None
    """
    environment = os.environ.get("ENVIRONMENT")
    account = os.environ.get("ACCOUNT")
    assert environment == "dev"
    assert account == "12345"
