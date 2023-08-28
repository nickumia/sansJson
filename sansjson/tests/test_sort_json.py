
import pytest


@pytest.mark.parametrize(
    'a, b, t',
    [
        # Two-levels with list as leaf
        (
            """{'z': 1,
             'a': {
                 '12': True,
                 'ef': ['a', 1, False],
                 'ap': 0}}""",
            """{'a': {
                '12': True,
                'ap': 0,
                'ef': [False, 1, 'a']},
             'z': 1}""", "json"
        ),
    ]
)
def test_sorted(a, b, t, compare):
    assert compare
