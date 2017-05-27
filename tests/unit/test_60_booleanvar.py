import pytest
from hypothesis import strategies as st
from hypothesis import given, assume

from environconfig import BooleanVar

TRUE_VALUES = ['1', 'yes', 'true', 'on']
FALSE_VALUES = ['0', 'no', 'false', 'off']


@pytest.mark.parametrize("text", TRUE_VALUES)
def test_booleanvar_true(text):
    assert BooleanVar()._to_python(text) is True


@pytest.mark.parametrize("text", FALSE_VALUES)
def test_booleanvar_false(text):
    assert BooleanVar()._to_python(text) is False


@given(st.text())
def test_booleanvar_other(text):
    assume(text not in (TRUE_VALUES + FALSE_VALUES))
    with pytest.raises(ValueError):
        BooleanVar()._to_python(text)
