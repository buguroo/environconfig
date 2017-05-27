import pytest

from environconfig import VarUnsetError


def test_varuseterror_is_keyerror():
    assert issubclass(VarUnsetError, KeyError)
