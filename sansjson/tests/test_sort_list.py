
import pytest
from sansjson.utils import Hasher

o = Hasher()


# TODO: fix objects
@pytest.mark.parametrize(
    'a, b',
    [
        # Homogenous
        (
            [3, 5, 4, 2],
            [2, 3, 4, 5]
        ),
        # Non-Homogenous
        (
            [None, 'a', 2, None],
            [None, None, 2, 'a']
        ),
        # Non-Homogenous Array 2
        (
            ['z', 1, 'a', 2, 'y', 3, 'c', 4],
            [1, 2, 3, 4, 'a', 'c', 'y', 'z']
        ),
        # Non-Homogenous 3
        (
            [None, 'z', 2, None, True, False, 1, 'a'],
            [None, None, False, True, 1, 2, 'a', 'z']
        ),
        # Array of 'objects'
        (
            [{'z': 1, 'a': 2}, {'y': 3, 'c': 4}],
            [{'a': 2, 'z': 1}, {'c': 4, 'y': 3}]
        ),
        # Array of 'objects' + other stuff
        (
            [{'z': 10, 'a': 2}, {'y': 3, 'c': 4}, 'a', 1, {'z': 1, 'a': 2}, True],
            [True, 1, 'a', {'a': 2, 'z': 1}, {'a': 2, 'z': 10}, {'c': 4, 'y': 3}]
        ),
        # Array of 'objects' + other stuff 2
        (
            [{'z': 10, 'a': 2, 'y': 3}, 'a', 1, {'a': [{'y': 3}, {'y': 0}, {'r': 0}]}, {'a': [{'x': 9}, {'s': 8}]}, True],
            [True, 1, 'a', {'a': 2, 'y': 3, 'z': 10}, {'a': [{'r': 0}, {'y': 0}, {'y': 3}]}, {'a': [{'s': 8}, {'x': 9}]}]
        ),
    ]
)
def test_sortable_homogenous(a, b, compare):
    assert compare
