import pytest


def test_package():
    try:
        import environconfig
    except ImportError as exc:
        assert False, exc
