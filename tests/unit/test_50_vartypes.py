import pytest

from environconfig import EnvironVar
from environconfig import StringVar, IntVar, PathVar
from environconfig import IntVar, FloatVar, BooleanVar


@pytest.mark.parametrize("varclass", [StringVar, IntVar, PathVar,
                                      IntVar, FloatVar, BooleanVar])
def test_varclass_inherits_from_basevar(varclass):
    assert issubclass(varclass, EnvironVar)
