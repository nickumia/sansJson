
import sansjson.utils as su


def test_sortable_dict():
    p = su.Sorter()

    sJ = {'a': 1, 'b': 2, 'c': 3}
    assert p.sortable(sJ)


def test_sortable_json_str():
    p = su.Sorter()

    sJ = '{"a": 1, "b": 2, "c": 3}'
    assert p.sortable(sJ)

    sJ = '{"a": 1, "b": 2, "c: 3}'
    assert p.sortable(sJ) is False


def test_sortable_list():
    p = su.Sorter()

    sJ = [1, 3, 2]
    assert p.sortable(sJ)


def test_sortable_misc():
    p = su.Sorter()

    sJ = 1
    assert p.sortable(sJ) is False

    sJ = None
    assert p.sortable(sJ) is False

    assert p.sortable(p) is False
