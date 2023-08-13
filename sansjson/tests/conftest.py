
import pytest
import sansjson
from sansjson.utils import Hasher, Sorter


@pytest.fixture(scope='function')
def compare(a, b):
    bad = Hasher()
    bad.data = a

    c = sansjson.sort(a)

    good = Hasher()
    good.data = b

    reference = Hasher()
    reference.data = c

    assert hash(bad) != hash(good)
    assert hash(good) == hash(reference)

    return True


@pytest.fixture(scope='function')
def sortable_test(a, b):
    p = Sorter()

    assert p.sortable(a) is b
    return True
