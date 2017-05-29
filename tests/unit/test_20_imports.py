import importlib

import pytest

import environconfig

ABSTRACT = [
    "EnvironConfigABC",
    "VarABC"]

BASE = [
    "EnvironConfig",
    "BaseVar"]

VARS = [
    "StringVar",
    "PathVar",
    "IntVar",
    "FloatVar",
    "BooleanVar"]

EXCEPTIONS = [
    "VarUnsetError",
    "VarTypeCastError",
    "UnknownVarError"]

OTHER = [
    "NoVarDefault"]


@pytest.mark.parametrize("objectname",
                         ABSTRACT + BASE + VARS + EXCEPTIONS + OTHER)
def test_environconfig_imports(objectname):
    try:
        getattr(environconfig, objectname)
    except AttributeError as exc:
        assert False, exc
