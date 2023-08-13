
import pytest
import sansjson
from sansjson.utils import Hasher


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
