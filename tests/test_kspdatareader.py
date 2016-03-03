import unittest
from unittest.mock import MagicMock, patch
from ..kspdatareader import KSPDataReader


class TestKSPDataReader(unittest.TestCase):
    def test__KSPDataReader_inits_with_empty_node_root(self):
        reader = KSPDataReader()
        assert len(reader.tree.values) == 0
        assert len(reader.tree.nodes) == 0

    def test__process_line_recognizes_node_name(self):
        pass
        KSPDataReader.handle_node_name = MagicMock(name='handle_node_name')
        reader = KSPDataReader()

        reader.process_line('GAME')

        reader.handle_node_name.assert_called_once_with('GAME')

    def test__ingest_lines_inserts_empty_node(self):
        pass
        # reader = KSPDataReader()
        # reader.ingest_lines(['GAME', '{', '}'])
        # assert reader.tree.nodes[0].name == 'GAME'
        # assert len(reader.tree.children[0].values) == 0
