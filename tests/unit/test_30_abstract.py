import pytest

from environconfig import EnvironConfigABC, VarABC


def test_environconfigabc_interface():
    with pytest.raises(TypeError):
        EnvironConfigABC()

    class EnvironStub(EnvironConfigABC):
        def getvar(self, name):
            pass

    # SHOULD NOT RAISE
    EnvironStub()


def test_varabc_interface():
    with pytest.raises(TypeError):
        VarABC()

    class VarStub(VarABC):
        def _to_python(self, value):
            pass

    # SHOULD NOT RAISE
    VarStub()
