import pytest


@pytest.fixture
def VarStub():
    from environconfig import BaseVar

    class _VarStub(BaseVar):
        def _to_python(self, value):
            return value

    return _VarStub
