import os

import pytest

from environconfig import EnvironConfig
from environconfig import EnvironConfigABC
from environconfig import VarUnsetError


@pytest.mark.wip
def test_environconfig_is_environconfigabc():
    assert issubclass(EnvironConfig, EnvironConfigABC)


@pytest.mark.wip
def test_default_environ_is_os_environ():
    assert EnvironConfig.environ is os.environ


@pytest.mark.wip
def test_environ_can_be_overwritten():
    myenv = {}
    ec = EnvironConfig(environ=myenv)
    assert ec.environ is myenv


@pytest.mark.wip
def test_environ_defaults_to_os_environ():
    assert EnvironConfig().environ is os.environ


@pytest.mark.wip
def test_environ_must_be_a_mapping():
    with pytest.raises(TypeError):
        EnvironConfig(environ=None)


@pytest.mark.wip
def test_default_preffix_is_empty():
    assert EnvironConfig.__varpreffix__ == ''


@pytest.mark.wip
def test_getvar_without_preffix_instance():
    ec = EnvironConfig(environ={'MYKEY': 'MYVALUE'})
    assert ec.getvar('MYKEY') == 'MYVALUE'


@pytest.mark.wip
def test_getvar_with_preffix_instance():

    class EnvironStub(EnvironConfig):
        __varpreffix__ = 'MYPREFFIX_'

    ec = EnvironStub(environ={'MYPREFFIX_KEY': 'MYVALUE'})
    assert ec.getvar('KEY') == 'MYVALUE'


@pytest.mark.wip
def test_getvar_unset_var_instance():
    ec = EnvironConfig(environ={})

    with pytest.raises(VarUnsetError):
        ec.getvar("missingvar")


@pytest.mark.wip
def test_getvar_without_preffix_class():

    class EnvironStub(EnvironConfig):
        environ = {'MYKEY': 'MYVALUE'}

    assert EnvironStub.getvar('MYKEY') == 'MYVALUE'


@pytest.mark.wip
def test_getvar_with_preffix_class():

    class EnvironStub(EnvironConfig):
        __varpreffix__ = 'MYPREFFIX_'
        environ = {'MYPREFFIX_KEY': 'MYVALUE'}


    assert EnvironStub.getvar('KEY') == 'MYVALUE'


@pytest.mark.wip
def test_getvar_unset_var_class():

    class EnvironStub(EnvironConfig):
        __varpreffix__ = 'MYPREFFIX_'
        environ = {}

    with pytest.raises(VarUnsetError):
        EnvironStub.getvar("missingvar")
