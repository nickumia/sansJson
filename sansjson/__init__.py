
from . import utils


def sort_pyobject(sans):
    processor = utils.Sorter()
    if not processor.is_sortable(sans):
        raise SystemError('Input is not sortable.')

    return processor.sort()


def sort_json(sans):
    processor = utils.JSONSorter()
    if not processor.is_sortable(sans):
        raise SystemError('Input is not sortable.')

    return processor.sort()
