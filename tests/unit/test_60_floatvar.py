import pytest
from hypothesis import strategies as st
from hypothesis import given, assume

from environconfig import FloatVar


def isfloat(value):
    try:
        float(value)
    except ValueError:
        return False
    else:
        return True


@given(st.floats(allow_nan=False))
def test_floatvar_with_float_value(value):
    assert FloatVar()._to_python(str(value)) == value


@given(st.text())
def test_floatvar_with_no_float_value(value):
    assume(not isfloat(value))
    with pytest.raises(ValueError):
        assert FloatVar()._to_python(value)
