import unittest
from ..kspdatanode import KSPDataNode


class TestKSPDataNode(unittest.TestCase):
    def test__add_value(self):
        node = KSPDataNode()

        node.add_value('foo', 'bar')

        value = node.values[0]
        assert len(node.values) == 1
        assert value.name == 'foo'
        assert value.value == 'bar'

    def test__values_retain_order(self):
        node = KSPDataNode()

        node.add_value('first', 'foo')
        node.add_value('second', 'bar')
        node.add_value('third', 'baz')

        assert node.values[0].name == 'first'
        assert node.values[1].name == 'second'
        assert node.values[2].name == 'third'

    def test__add_node(self):
        node = KSPDataNode()
        child_node = KSPDataNode()

        node.add_node(child_node)

        assert node.nodes[0] is child_node
