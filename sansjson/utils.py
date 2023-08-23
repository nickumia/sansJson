
from copy import deepcopy
import functools
import json
import logging

log = logging.getLogger(__name__)

NONHOMOGENOUS_ORDER = {type(None): 1, bool: 2, int: 3, float: 4, str: 5, list: 6, object: 7, dict: 8}


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

    def recursive_dict(self, context):
        sorted_dict = {}
        keys = nonhomogenous(context.keys())
        for k in keys:
            if self.is_sortable(context[k]):
                # BRANCH: recursively check values
                sorted_dict[k] = self.sort(context[k])
            else:
                # LEAF: basic data types
                sorted_dict[k] = context[k]
        return sorted_dict

    def sort(self, context=None):
        sorted_dict = {}
        if context is None:
            context = self.data

        if isinstance(context, list):
            # BRANCH: list of dicts
            if any([isinstance(i, dict) for i in context]):
                new_list = []

                for i, element in enumerate(context):
                    if isinstance(element, dict):
                        sorted_element = self.recursive_dict(element)
                        new_list.append(sorted_element)
                    else:
                        new_list.append(element)
                return nonhomogenous(new_list)
            # LEAF: just sort list
            return nonhomogenous(context)
        if isinstance(context, dict):
            # BRANCH: sort keys
            sorted_dict = self.recursive_dict(context)

        return sorted_dict


def dict_sort_key(dicta, dictb):
    dicta_list = False
    dictb_list = False
    try:
        k1 = list(dicta.keys())[0]
    except IndexError:
        # No more keys
        k1 = None
    except AttributeError:
        # list to list compare
        dicta_list = sorted([dicta], key=functools.cmp_to_key(dict_sort_key))
    try:
        k2 = list(dictb.keys())[0]
    except IndexError:
        # No more keys
        k2 = None
    except AttributeError:
        # list to list compare
        dictb_list = sorted([dictb], key=functools.cmp_to_key(dict_sort_key))

    if dicta_list and dictb_list:
        return sorted(dicta_list[0] + dictb_list[0], key=functools.cmp_to_key(dict_sort_key))

    # if k1 == dicta and k2 == dictb:
    #     if k1 > k2:
    #         return 1
    #     elif k2 > k1:
    #         return -1
    #     else:
    #         return 0

    # Dict with less keys is 'smaller'
    if k1 is None and k2 is None:
        return 0
    if k1 is None and k2 is not None:
        return -1
    if k1 is not None and k2 is None:
        return 1

    # JSON keys are ALWAYS str
    if k1 == k2:
        v1_type = type(dicta[k1])
        v2_type = type(dictb[k2])
        if v1_type != v2_type:
            if NONHOMOGENOUS_ORDER[v1_type] > NONHOMOGENOUS_ORDER[v2_type]:
                return 1
            else:
                # NONHOMOGENOUS_ORDER[v1_type] < NONHOMOGENOUS_ORDER[v2_type]:
                return -1
        else:
            if dicta[k1] == dictb[k2]:
                dicta_copy = deepcopy(dicta)
                dictb_copy = deepcopy(dictb)
                del dicta_copy[k1]
                del dictb_copy[k2]
                return dict_sort_key(dicta_copy, dictb_copy)
            else:
                if isinstance(dicta[k1], list) and isinstance(dictb[k2], list):
                    if isinstance(dicta[k1][0], dict) and isinstance(dictb[k2][0], dict):
                        smallest_key = dict_sort_key(dicta[k1], dictb[k2])
                        for dict_items in smallest_key:
                            for key, value in dict_items.items():
                                if key in dicta[k1][0]:
                                    if dicta[k1][0][key] == value:
                                        if key not in dictb[k2][0]:
                                            return -1
                                elif key in dictb[k2][0]:
                                    if dictb[k2][0][key] == value:
                                        if key not in dicta[k1][0]:
                                            return 1
                elif dicta[k1] > dictb[k2]:
                    return 1
                else:
                    return -1
    else:
        if k1 > k2:
            return 1
        else:
            return -1


def nonhomogenous(sans):
    '''
    Handle special nonhomogenous list sorting

    Use NONHOMOGENOUS_ORDER to handle priority of data types.
    '''
    try:
        # homogenous
        return sorted(sans)
    except TypeError:

        # TODO: nonhomogenous list of dicts and non-dicts

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
                elif dict == dt:
                    final += sorted(data_groups[dt], key=functools.cmp_to_key(dict_sort_key))
                else:
                    final += sorted(data_groups[dt])

        return final
