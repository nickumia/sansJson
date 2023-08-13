
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
        'a': {
            '12': True,
            'ap': 0,
            'ef': False},
        'c': {
            '0': 'werg',
            'ue': 'def',
            'yh': 'abc'},
        'y': 3,
        'z': 1
    }


def test_sortable_three_levels():
    sJ = {'z': 1,
          'a': {
              '12': True,
              'ef': {
                  'def': 23,
                  'erf': 45,
                  'cop': 67},
              'ap': 0},
          'y': 3,
          'c': {
              'yh': 'abc',
              'ue': 'def',
              '0': {
                  'jun': False,
                  'jul': True,
                  'aug': 1}}}
    assert sansjson.sort(sJ) == {
        'a': {
            '12': True,
            'ef': {
                'cop': 67,
                'def': 23,
                'erf': 45},
            'ap': 0},
        'y': 3,
        'c': {
            'yh': 'abc',
            'ue': 'def',
            '0': {
                'aug': 1,
                'jul': True,
                'jun': False}},
        'z': 1
    }
