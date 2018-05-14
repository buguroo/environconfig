import os

from hypothesis import strategies as st
from hypothesis import given

from environconfig import BytesVar


@given(st.text())
def test_bytesvar_decoded_are_strings(text):
    assert os.environ.decodevalue(BytesVar()._to_python(text)) == text
