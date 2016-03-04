import unittest
from unittest.mock import MagicMock, patch
from ..kspdatareader import KSPDataReader


class TestKSPDataReader(unittest.TestCase):
    def test__KSPDataReader_inits_with_empty_node_root(self):
        reader = KSPDataReader()
        assert len(reader.tree.values) == 0
        assert len(reader.tree.nodes) == 0

    def test__process_lines_recognizes_node_name(self):
        KSPDataReader.handle_node_name = MagicMock(name='handle_node_name')
        reader = KSPDataReader()

        reader.process_lines(['GAME'])

        assert reader.handle_node_name.call_count == 1
        assert reader.handle_node_name.call_args[0][0].string == 'GAME'
        assert reader.handle_node_name.call_args[0][0].groups() == ('GAME', )

    def test__process_lines_recognizes_value_pair(self):
        KSPDataReader.handle_value_pair = mock = MagicMock(name='handle_value_pair')
        reader = KSPDataReader()

        line = 'foo = bar baz/qux'
        reader.process_lines([line])

        assert mock.call_count == 1
        assert mock.call_args[0][0].string == line
        assert mock.call_args[0][0].groups() == ('foo', 'bar baz/qux')

    def test__ingest_lines_inserts_empty_node(self):
        pass
        # reader = KSPDataReader()
        # reader.ingest_lines(['GAME', '{', '}'])
        # assert reader.tree.nodes[0].name == 'GAME'
        # assert len(reader.tree.children[0].values) == 0
