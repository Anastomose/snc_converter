import pytest
from cdf_tools import new_func

def test_newfunc():
    new_func.something_new()
    assert new_func.something_new() is None

