import re

from . import kspdatanode
from . import lineprocessor


class KSPDataReader(lineprocessor.LineProcessor):
    def __init__(self):
        super().__init__([
            (re.compile(r'([A-Z]+)'), self.handle_node_name),
        ])
        self.tree = kspdatanode.KSPDataNode()
        self.processing_table = {
            re.compile(r'([A-Z]+)'): self.handle_node_name,
        }

    def ingest_lines(self, lines):
        for line in lines:
            self.process_line(line)

    def process_line(self, line):
        for pattern, handler in self.processing_table.items():
            if pattern.match(line):
                handler(line)
                break

    def handle_node_name(self, line):
        print('handling node name', line)
        pass
