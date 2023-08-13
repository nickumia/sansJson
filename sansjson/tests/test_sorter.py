
import pytest
from sansjson.utils import Hasher


@pytest.mark.parametrize(
    'a, b',
    [
        # dict
        ({'a': 1, 'b': 2, 'c': 3}, True),
        # JSON str
        ('{"a": 1, "b": 2, "c": 3}', True),
        # list
        ([1, 3, 2], True),
        # JSON str (bad)
        ('{"a": 1, "b": 2, "c: 3}', False),
        # int
        (1, False),
        # none
        (None, False),
        # object
        (Hasher(), False)
    ]
)
def test_sortable(a, b, sortable_test):
    assert sortable_test
