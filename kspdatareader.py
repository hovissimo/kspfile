import re

from . import kspdatanode
from . import lineprocessor


class KSPDataReader(lineprocessor.LineProcessor):
    def __init__(self):
        super().__init__([
            (re.compile(r'\t*([A-Z]+)'),
             self.handle_node_name),
            (re.compile(r'\t*(?P<name>\w+) = (?P<value>.*)'),
             self.handle_value_pair),
            (re.compile(r'\t*{$'),
             self.handle_open_brace),
            (re.compile(r'\t*}$'),
             self.handle_close_brace),
        ])
        self.tree = kspdatanode.KSPDataNode('')
        self.cursor = self.tree
        self
        self.last_line = ''

    def handle_node_name(self, match):
        child = self.cursor.add_node(kspdatanode.KSPDataNode(match.groups()[0]))
        self.cursor = child

    def handle_value_pair(self, match):
        self.cursor.add_value(*match.groups())

    def handle_open_brace(self, match):
        print('handling open brace')

    def handle_close_brace(self, match):
        print('handling close brace')
