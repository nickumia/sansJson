
import pytest


@pytest.mark.parametrize(
    'a, b, t',
    [
        # Two-levels with list as leaf
        (
            '{"z": 1, "a": {"12": true, "ef": ["a", 1, false], "ap": 0}}',
            '{"a": {"12": true, "ef": ["a", 1, false], "ap": 0}, "z": 1}',
            "json"
        ),
    ]
)
def test_sorted(a, b, t, compare):
    assert compare
