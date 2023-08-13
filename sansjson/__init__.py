
from . import utils


def sort(sans):
    processor = utils.Sorter()
    if not processor.sortable(sans):
        raise SystemError('Input is not sortable.')

    return processor.sort()
