import unittest
from unittest.mock import MagicMock, Mock, patch

from ..kspdatareader import KSPDataReader
from .. import kspdatanode


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

    def test__process_lines_recognizes_open_brace(self):
        KSPDataReader.handle_open_brace = mock = MagicMock(name='handle_open_brace')
        reader = KSPDataReader()

        reader.process_lines(['{'])

        assert mock.call_count == 1
        assert mock.call_args[0][0].string == '{'

    def test__process_lines_recognizes_close_brace(self):
        KSPDataReader.handle_close_brace = mock = MagicMock(name='handle_close_brace')
        reader = KSPDataReader()

        reader.process_lines(['}'])

        assert mock.call_count == 1
        assert mock.call_args[0][0].string == '}'

    def test__KSPDataReader_calls_inits_node_for_new_node(self):
        with patch('pykspfile.kspdatanode.KSPDataNode') as mock:
            reader = KSPDataReader()
            reader.process_lines(['GAME', '{', '}'])
            mock.assert_called_with('GAME')

    def test__KSPDataReader_accepts_root_level_values(self):
        reader = KSPDataReader()
        reader.process_lines([
                              'foo = bar/baz qux',
                              'cool_guy = hovis',
                              '0 = Flight,Kerbin',
                              ])

        assert len(reader.tree.values) == 3
        assert reader.tree.values[0].name == 'foo'
        assert reader.tree.values[0].value == 'bar/baz qux'
        assert reader.tree.values[1].name == 'cool_guy'
        assert reader.tree.values[1].value == 'hovis'
        assert reader.tree.values[2].name == '0'
        assert reader.tree.values[2].value == 'Flight,Kerbin'
