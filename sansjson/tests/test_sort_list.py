
import sansjson


def test_sortable_homogenous():
    sJ = [3, 5, 4, 2]
    assert sansjson.sort(sJ) == [2, 3, 4, 5]


def test_sortable_nonhomogenous():
    sJ = [None, 'a', 2, None]
    assert sansjson.sort(sJ) == [None, None, 2, 'a']

    o = object()
    sJ = [None, 'z', 2, None, o, True, False, 1, 'a']
    assert sansjson.sort(sJ) == [None, None, False, True, 1, 2, 'a', 'z', o]
