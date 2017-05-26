from unittest.mock import MagicMock

import pytest

from environconfig import EnvironConfig
from environconfig import VarUnsetError


@pytest.mark.wip
def test_var_must_be_attached_to_environconfig_class(VarStub):
    class NoEnvironConfig:
        var = VarStub()

    with pytest.raises(TypeError):
        NoEnvironConfig.var


@pytest.mark.wip
def test_var_must_be_attached_to_environconfig_instance(VarStub):
    class NoEnvironConfig:
        var = VarStub()

    with pytest.raises(TypeError):
        NoEnvironConfig().var


@pytest.mark.wip
def test_unset_variable_and_no_default_raises(VarStub):
    class MyEnvironConfig(EnvironConfig):
        var = VarStub()

    ec = MyEnvironConfig(environ={})

    with pytest.raises(VarUnsetError):
        ec.var


@pytest.mark.wip
def test_set_variable_calls_to_python(VarStub):

    vs = VarStub()
    vs._to_python = MagicMock()

    class MyEnvironConfig(EnvironConfig):
        var = vs

    ec = MyEnvironConfig(environ={'var': 'MYVALUE'})

    ec.var

    vs._to_python.assert_called_with('MYVALUE')
