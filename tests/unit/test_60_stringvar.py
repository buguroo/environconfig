import pytest
from hypothesis import strategies as st
from hypothesis import given

from environconfig import StringVar


@given(st.text())
def test_stringvar_return_the_same_string(text):
    assert StringVar()._to_python(text) == text
