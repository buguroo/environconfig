import pytest

from environconfig import VarUnsetError


@pytest.mark.wip
def test_varuseterror_is_keyerror():
    assert issubclass(VarUnsetError, KeyError)
