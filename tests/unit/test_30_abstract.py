import pytest

from environconfig import EnvironConfigABC, EnvironVar


def test_environconfigabc_interface():
    with pytest.raises(TypeError):
        EnvironConfigABC()

    class EnvironStub(EnvironConfigABC):
        def getvar(self, name):
            pass

    # SHOULD NOT RAISE
    EnvironStub()


def test_environconfigabc_register_fields_with_no_fields():

    class EnvironStub(EnvironConfigABC):
        def getvar(self, name):
            pass

    assert not EnvironStub.fields


def test_environconfigabc_register_fields_with_fields():

    class VarStub(EnvironVar):
        def _to_python(self, value):
            pass

    class EnvironStub(EnvironConfigABC):
        def getvar(self, name):
            pass
        var1 = VarStub()
        var2 = VarStub()

    assert "var1" in EnvironStub.fields
    assert "var2" in EnvironStub.fields


def test_varabc_interface():
    with pytest.raises(TypeError):
        EnvironVar()

    class VarStub(EnvironVar):
        def _to_python(self, value):
            pass

    # SHOULD NOT RAISE
    VarStub()
