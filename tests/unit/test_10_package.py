import pytest


@pytest.mark.wip
def test_package():
    try:
        import environconfig
    except ImportError as exc:
        assert False, exc
