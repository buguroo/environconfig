import os

import pytest

from environconfig import EnvironConfig
from environconfig import EnvironConfigABC
from environconfig import VarUnsetError


def test_environconfig_is_environconfigabc():
    assert issubclass(EnvironConfig, EnvironConfigABC)


def test_default_environ_is_None():
    assert EnvironConfig.environ is None


def test_environ_can_be_overwritten():
    myenv = {}
    ec = EnvironConfig(environ=myenv)
    assert ec.environ is myenv


def test_environ_defaults_to_None():
    assert EnvironConfig().environ is None


def test_environ_must_be_a_mapping():
    with pytest.raises(TypeError):
        EnvironConfig(environ=[])


def test_default_prefix_is_empty():
    assert EnvironConfig.__varprefix__ == ''


def test_getvar_without_prefix_instance():
    ec = EnvironConfig(environ={'MYKEY': 'MYVALUE'})
    assert ec.getvar('MYKEY') == 'MYVALUE'


def test_getvar_with_prefix_instance():

    class EnvironStub(EnvironConfig):
        __varprefix__ = 'MYPREFFIX_'

    ec = EnvironStub(environ={'MYPREFFIX_KEY': 'MYVALUE'})
    assert ec.getvar('KEY') == 'MYVALUE'


def test_getvar_unset_var_instance():
    ec = EnvironConfig(environ={})

    with pytest.raises(VarUnsetError):
        ec.getvar("missingvar")


def test_getvar_without_prefix_class():

    class EnvironStub(EnvironConfig):
        environ = {'MYKEY': 'MYVALUE'}

    assert EnvironStub.getvar('MYKEY') == 'MYVALUE'


def test_getvar_with_prefix_class():

    class EnvironStub(EnvironConfig):
        __varprefix__ = 'MYPREFFIX_'
        environ = {'MYPREFFIX_KEY': 'MYVALUE'}


    assert EnvironStub.getvar('KEY') == 'MYVALUE'


def test_getvar_unset_var_class():

    class EnvironStub(EnvironConfig):
        __varprefix__ = 'MYPREFFIX_'
        environ = {}

    with pytest.raises(VarUnsetError):
        EnvironStub.getvar("missingvar")


def test_unset_environ_defaults_to_os_environ_class():
    for key, value in os.environ.items():
        assert EnvironConfig.getvar(key) == value


def test_unset_environ_defaults_to_os_environ_instance():
    env = EnvironConfig()
    for key, value in os.environ.items():
        assert env.getvar(key) == value


def test_verify_success_if_no_fields():
    assert EnvironConfig.verify()
