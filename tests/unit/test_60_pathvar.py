import os

import pytest

from environconfig import PathVar


def test_pathvar_absolutepath():
    assert PathVar()._to_python("/root") == "/root"


def test_pathvar_expanduser():
    assert PathVar()._to_python("~") == os.path.expanduser("~")


def test_pathvar_relativepath():
    assert PathVar()._to_python("./test") == os.path.abspath("./test")


def test_pathvar_normalizepath():
    assert PathVar()._to_python("/A/foo/../B//C") == "/A/B/C"
