import pytest


@pytest.fixture
def VarStub():
    from environconfig import EnvironVar

    class _VarStub(EnvironVar):
        def _to_python(self, value):
            return value

    return _VarStub
