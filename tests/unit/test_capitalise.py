import pytest
from capitalise.core import capitalise


def test_capitalise():
    test_value = "She sells sea shells on the sea shore"
    response = capitalise(value=test_value)
    assert response == "SHE SELLS SEA SHELLS ON THE SEA SHORE"


def test_value_error():
    test_value = 25
    with pytest.raises(ValueError):
        response = capitalise(value=test_value)
