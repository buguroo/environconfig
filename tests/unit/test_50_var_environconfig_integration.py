from unittest.mock import MagicMock

import pytest

from environconfig import EnvironConfig
from environconfig import VarUnsetError, VarTypeCastError, UnknownVarError


def test_var_must_be_attached_to_environconfig_class(VarStub):
    class NoEnvironConfig:
        var = VarStub()

    with pytest.raises(TypeError):
        NoEnvironConfig.var


def test_var_must_be_attached_to_environconfig_instance(VarStub):
    class NoEnvironConfig:
        var = VarStub()

    with pytest.raises(TypeError):
        NoEnvironConfig().var


def test_unset_variable_and_no_default_raises(VarStub):
    class MyEnvironConfig(EnvironConfig):
        var = VarStub()

    ec = MyEnvironConfig(environ={})

    with pytest.raises(VarUnsetError):
        ec.var


def test_variable_calls_to_python(VarStub):

    vs = VarStub()
    vs._to_python = MagicMock()

    class MyEnvironConfig(EnvironConfig):
        var = vs

    ec = MyEnvironConfig(environ={'var': 'MYVALUE'})

    ec.var

    vs._to_python.assert_called_with('MYVALUE')


def test_variable_returns_default(VarStub):

    class MyEnvironConfig(EnvironConfig):
        var = VarStub(default='MYDEFAULT')

    ec = MyEnvironConfig(environ={})

    assert ec.var == 'MYDEFAULT'


def test_to_python_exceptions_are_masked(VarStub):
    vs = VarStub()
    vs._to_python = MagicMock(
        side_effect=RuntimeError("SHOULD BE CONVERTED TO VALUEERROR"))

    class MyEnvironConfig(EnvironConfig):
        var = vs

    ec = MyEnvironConfig(environ={'var': 'MYVALUE'})

    with pytest.raises(VarTypeCastError):
        ec.var


def test_verify_pass_if_all_provided(VarStub):
    class MyEnvironConfig(EnvironConfig):
        var1 = VarStub()
        var2 = VarStub()

    ec = MyEnvironConfig(environ={'var1': 'MYVALUE1',
                                  'var2': 'MYVALUE2'})

    assert ec.verify()


def test_verify_pass_if_not_provided_but_have_defaults(VarStub):
    class MyEnvironConfig(EnvironConfig):
        var1 = VarStub(default='MYVALUE1')
        var2 = VarStub(default='MYVALUE2')

    ec = MyEnvironConfig(environ={})

    assert ec.verify()


def test_verify_fails_if_not_provided_and_no_default(VarStub):
    class MyEnvironConfig(EnvironConfig):
        var1 = VarStub(default='MYVALUE1')
        var2 = VarStub()

    ec = MyEnvironConfig(environ={})

    assert not ec.verify()


def test_verify_one_success_if_provided(VarStub):
    class MyEnvironConfig(EnvironConfig):
        var1 = VarStub()

    ec = MyEnvironConfig(environ={'var1': 'MYVALUE1'})

    assert ec.verify('var1')


def test_verify_one_success_if_default(VarStub):
    class MyEnvironConfig(EnvironConfig):
        var1 = VarStub(default='MYVALUE1')

    ec = MyEnvironConfig(environ={})

    assert ec.verify('var1')


def test_verify_one_raise_if_unknown(VarStub):
    class MyEnvironConfig(EnvironConfig):
        var1 = VarStub(default='MYVALUE1')

    ec = MyEnvironConfig(environ={'var1': 'MYVALUE1'})

    with pytest.raises(UnknownVarError):
        assert ec.verify('var2')


def test_fail_if_not_provided_and_no_default(VarStub):
    class MyEnvironConfig(EnvironConfig):
        var1 = VarStub()

    ec = MyEnvironConfig(environ={})

    assert not ec.verify('var1')
