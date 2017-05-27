import pytest
from hypothesis import strategies as st
from hypothesis import given, assume

from environconfig import IntVar


@given(st.integers())
def test_intvar_with_integer_value(value):
    assert IntVar()._to_python(str(value)) == value


@given(st.text())
def test_intvar_with_no_integer_value(value):
    assume(not value.isnumeric())
    with pytest.raises(ValueError):
        assert IntVar()._to_python(value)
