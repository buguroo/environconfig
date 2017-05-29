import sys
from functools import partial

import pytest

from environconfig import EnvironVar
from environconfig import NoVarDefault
from environconfig import VarABC


_skipif_set_name = partial(
    pytest.mark.skipif,
    reason=("https://docs.python.org/3.6/reference/"
            "datamodel.html#object.__set_name__"))

skipif_native_set_name = partial(
    _skipif_set_name,
    sys.version_info >= (3, 6))

skipif_no_native_set_name = partial(
    _skipif_set_name,
    sys.version_info < (3, 6))


def test_basevar_is_varabc():
    assert issubclass(EnvironVar, VarABC)


@skipif_native_set_name()
def test_basevar_setname_without_name(VarStub):
    fs = VarStub()

    class MyClass:
        var = fs

    assert fs._name is None
    fs.__set_name__(MyClass)
    assert fs._name == "var"


@skipif_native_set_name()
def test_basevar_setname_without_name_bad_owner(VarStub):
    fs = VarStub()

    class MyClass:
        pass

    with pytest.raises(ValueError):
        fs.__set_name__(MyClass)


@skipif_no_native_set_name()
def test_basevar_setname_with_name(VarStub):
    fs = VarStub()

    class MyClass:
        var = fs

    assert fs._name == "var"


@skipif_native_set_name()
def test_basevar_getname_return_name(VarStub):
    fs = VarStub()

    class MyClass:
        var = fs

    assert fs.__get_name__(MyClass) == "var"


@skipif_native_set_name()
def test_basevar_getname_setname_if_not_set(VarStub):
    fs = VarStub()

    class MyClass:
        var = fs

    assert fs._name is None
    fs.__get_name__(MyClass)
    assert fs._name == "var"


def test_basevar_have_nodefault(VarStub):
    fs = VarStub()
    assert fs.default is NoVarDefault


def test_basevar_stores_default(VarStub):
    fs = VarStub(default="MYVALUE")
    assert fs.default == "MYVALUE"
