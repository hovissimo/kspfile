import re

from . import kspdatanode
from . import lineprocessor


class KSPDataReader(lineprocessor.LineProcessor):
    def __init__(self):
        super().__init__([
            (re.compile(r'\t*([^\s{}]+)\s*$'),
             self.handle_node_name),
            (re.compile(r'\t*(?P<name>[^\s{}]+) = (?P<value>.*?)\s*$'),
             self.handle_value_pair),
            (re.compile(r'\t*{$'),
             self.handle_open_brace),
            (re.compile(r'\t*}$'),
             self.handle_close_brace),
        ])
        self.tree = kspdatanode.KSPDataNode('')
        self.cursor = self.tree
        self
        self.__last_line = ''  # Hack for detecting problems with braces

    def handle_node_name(self, match):
        child = self.cursor.add_node(kspdatanode.KSPDataNode(match.groups()[0]))
        self.cursor = child
        self.__last_line = 'node_name'

    def handle_value_pair(self, match):
        self.cursor.add_value(*match.groups())
        self.__last_line = 'value_pair'

    def handle_open_brace(self, match):
        assert self.__last_line == 'node_name', \
            'Syntax problem.  Open brace not following node name.'
        self.__last_line = 'open_brace'

    def handle_close_brace(self, match):
        self.cursor = self.cursor.parent
        self.__last_line = 'close_brace'
