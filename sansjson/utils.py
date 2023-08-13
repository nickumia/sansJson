
import json
import logging

log = logging.getLogger(__name__)

NONHOMOGENOUS_ORDER = [type(None), bool, int, float, str, list, object]


class Hasher:

    def __init__(self):
        self._data = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, v):
        self._data = v

    # def __dict__(self):
    #     if type(self.data) == object:
    #         return hash(self.data)
    #     return super(Hasher, self).__dict__

    def __hash__(self):
        return hash(json.dumps(self.data))

    def __eq__(self, other):
        if isinstance(other, Sorter):
            return hash(self) == hash(Sorter)
        return NotImplemented


class Sorter(Hasher):

    def __init__(self):
        super(Sorter, self).__init__()

    def sortable(self, sans):
        if isinstance(sans, dict):
            self.data = sans
            return True
        if isinstance(sans, str):
            try:
                self.data = json.loads(sans)
                return True
            except json.decoder.JSONDecodeError:
                log.error(
                    'Input is str, but could not be parsed into JSON dict.')
                return False
        if isinstance(sans, list):
            self.data = sans
            return True
        return False

    def sort(self, context=None):
        new_dict = {}
        if context is None:
            context = self.data

        if isinstance(context, list):
            return nonhomogenous(context)
        if isinstance(context, dict):
            keys = nonhomogenous(context.keys())
            for k in keys:
                if isinstance(context[k], dict) or \
                   isinstance(context[k], list):
                    new_dict[k] = self.sort(context[k])
                else:
                    new_dict[k] = context[k]

        return new_dict


def nonhomogenous(sans):
    try:
        return sorted(sans)
    except TypeError:
        parts = {}
        for s in sans:
            t = type(s)
            if t in parts:
                parts[t].append(s)
            else:
                parts[t] = [s]

        final = []
        for t in NONHOMOGENOUS_ORDER:
            if t in parts.keys():
                if isinstance(None, t):
                    final += parts[t]
                else:
                    final += sorted(parts[t])

        return final
