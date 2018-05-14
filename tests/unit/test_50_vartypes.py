import pytest

from environconfig import EnvironVar
from environconfig import StringVar, IntVar, PathVar
from environconfig import IntVar, FloatVar, BooleanVar
from environconfig import BytesVar


@pytest.mark.parametrize("varclass", [StringVar, IntVar, PathVar,
                                      IntVar, FloatVar, BooleanVar,
                                      BytesVar])
def test_varclass_inherits_from_basevar(varclass):
    assert issubclass(varclass, EnvironVar)
