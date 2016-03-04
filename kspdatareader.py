import re

from . import kspdatanode
from . import lineprocessor


class KSPDataReader(lineprocessor.LineProcessor):
    def __init__(self):
        super().__init__([
            (re.compile(r'^([A-Z]+)'),
             self.handle_node_name),
            (re.compile(r'^(?P<name>\w+) = (?P<value>.*)'),
             self.handle_value_pair),
        ])
        self.tree = kspdatanode.KSPDataNode()

    def handle_node_name(self, match):
        print('handling node name', match)

    def handle_value_pair(self, match):
        print('handling value pair', match)
