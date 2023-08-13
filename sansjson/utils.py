
import json
import logging

log = logging.getLogger(__name__)


class Sorter:

    def __init__(self):
        self.data = None

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
