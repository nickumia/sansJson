
import pytest
import sansjson
from sansjson.utils import Hasher, Sorter, JSONSorter


@pytest.fixture(scope='function')
def compare(a, b, function='pyobject'):
    bad = Hasher()
    bad.data = a

    if function == 'json':
        c = sansjson.sort_json(a)
    else:
        c = sansjson.sort_pyobject(a)

    reference = Hasher()
    reference.data = b

    good = Hasher()
    good.data = c

    assert hash(bad) != hash(good)
    assert hash(good) == hash(reference)

    return True


@pytest.fixture(scope='function')
def sortable_test(a, p, j):
    m = Sorter()
    n = JSONSorter()

    assert m.is_sortable(a) is p
    assert n.is_sortable(a) is j
    return True
