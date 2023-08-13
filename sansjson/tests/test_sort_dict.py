
import sansjson


def test_sortable_one_level():
    sJ = {'z': 1,
          'a': 2,
          'y': 3,
          'c': 4}
    assert sansjson.sort(sJ) == {
        'a': 2, 'c': 4, 'y': 3, 'z': 1
    }


def test_sortable_two_levels():
    sJ = {'z': 1,
          'a': {
              '12': True,
              'ef': False,
              'ap': 0},
          'y': 3,
          'c': {
              'yh': 'abc',
              'ue': 'def',
              '0': 'werg'}}
    assert sansjson.sort(sJ) == {
        'z': 1,
        'a': {
            '12': True,
            'ap': 0,
            'ef': False},
        'y': 3,
        'c': {
            '0': 'werg',
            'ue': 'def',
            'yh': 'abc'},
    }
