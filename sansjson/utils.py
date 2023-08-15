
import json
import logging

log = logging.getLogger(__name__)

NONHOMOGENOUS_ORDER = [type(None), bool, int, float, str, list, object]


class Hasher:
    '''
    Hash class to ensure exact match

    If the json string representation is the same, it is guaranteed that
    the sorting was successful.

    Note: As of Python 3.7+, the insertion order of dictionaries are preserved.
    (https://docs.python.org/3.7/library/stdtypes.html#typesmapping)
    '''
    def __init__(self):
        self._data = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, v):
        self._data = v

    def __hash__(self):
        return hash(json.dumps(self.data))

    def __eq__(self, other):
        if isinstance(other, Sorter):
            return hash(self) == hash(Sorter)
        return NotImplemented


class Sorter(Hasher):
    '''
    Sorter class to check sortability + perform sorting

    Supported types:
        - _dict_: sort key order
        - _list_: see 'nonhomogenous'
        - _str_: convert to _dict_
    '''

    def __init__(self):
        super(Sorter, self).__init__()

    def is_sortable(self, deck):
        if isinstance(deck, dict):
            self.data = deck
            return True
        if isinstance(deck, str):
            try:
                self.data = json.loads(deck)
                return True
            except json.decoder.JSONDecodeError:
                log.error(
                    'Input is str, but could not be parsed into JSON dict.')
                return False
        if isinstance(deck, list):
            self.data = deck
            return True
        return False

    def sort(self, context=None):
        sorted_dict = {}
        if context is None:
            context = self.data

        if isinstance(context, list):
            # LEAF: just sort list
            return nonhomogenous(context)
        if isinstance(context, dict):
            # BRANCH: sort keys
            keys = nonhomogenous(context.keys())
            for k in keys:
                if self.is_sortable(context[k]):
                    # BRANCH: recursively check values
                    sorted_dict[k] = self.sort(context[k])
                else:
                    # LEAF: basic data types
                    sorted_dict[k] = context[k]

        return sorted_dict


def nonhomogenous(sans):
    '''
    Handle special nonhomogenous list sorting

    Use NONHOMOGENOUS_ORDER to handle priority of data types.
    '''
    try:
        # homogenous
        return sorted(sans)
    except TypeError:
        # nonhomogenous
        data_groups = {}
        for element in sans:
            data_type = type(element)
            if data_type in data_groups:
                data_groups[data_type].append(element)
            else:
                data_groups[data_type] = [element]

        final = []
        for dt in NONHOMOGENOUS_ORDER:
            if dt in data_groups.keys():
                if isinstance(None, dt):
                    final += data_groups[dt]
                else:
                    final += sorted(data_groups[dt])

        return final
