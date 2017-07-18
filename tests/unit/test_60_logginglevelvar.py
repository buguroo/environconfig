import logging

import pytest
from hypothesis import strategies as st
from hypothesis import given, assume

from environconfig import LoggingLevelVar, VarTypeCastError


VALID_LEVELS = ["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG", "NOTSET"]


@pytest.mark.parametrize("levelname", VALID_LEVELS)
def test_logginglevelvar_return_valid_values(levelname):
    assert LoggingLevelVar()._to_python(levelname) == getattr(logging, levelname)


@given(st.text())
def test_logginglevelvar_fail_on_invalid_values(levelname):
    assume(levelname not in VALID_LEVELS)
    with pytest.raises(VarTypeCastError):
        LoggingLevelVar()._to_python(levelname)
