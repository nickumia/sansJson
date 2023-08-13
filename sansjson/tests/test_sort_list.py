
import sansjson


def test_sortable_homogenous():
    sJ = [3, 5, 4, 2]
    assert sansjson.sort(sJ) == [2, 3, 4, 5]


def test_sortable_nonhomogenous():
    sJ = [None, 'a', 2, None]
    assert sansjson.sort(sJ) == [None, None, 2, 'a']
